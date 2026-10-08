---
title: "指令経路 — クラウド・HEMS・電力会社・各機器のユースケース"
project: SPK-GW_HEMS
version: "1.0"
created: 2026-10-06
updated: 2026-10-06
status: recommended-draft
language: ja
tags: [SPK-GW_HEMS, architecture, HEMS, JET]
---

# 指令経路 — クラウド・HEMS・電力会社・各機器のユースケース

## 0. 図の前提

以下は設計案のユースケースです。各機器が対応する操作・時刻制約・通信断時動作は [機器プロファイル](templates/Device_Profile.md) で確定させます。図中の `Adapter経由` は、通常運転の通信経路です。系統制約を迂回する裏口ではありません。

## UC-01：クラウドから家庭全体の目標を受信

例：「17～18時の購入電力を3 kW以下にしたい」。現在の購入電力が6 kWなら、HEMSは蓄電池2 kW放電とEV充電1 kW削減の計画を候補にできます。これは説明用の定常計算であり、機器の可用性や制約を確認して採用します。

```mermaid
sequenceDiagram
    autonumber
    participant C as 外部クラウド
    participant I as 要求受付
    participant H as 高度エネマネ
    participant A as Control Arbiter
    participant O as Orchestrator
    participant D as DER Power Controller
    participant L as Flexible Load Controller
    participant K as 実機群
    C->>I: 家庭全体の購入電力目標
    I->>I: 認証・権限・期限・重複確認
    I->>H: EnergyGoal
    H->>H: 計測とCapabilityから計画案を作成
    H->>A: 資源別ControlRequestと競合範囲
    alt 計画を実行する権限がある
        A-->>O: 許可済み計画と各資源の制御権
        par 蓄電池の制御
            O->>D: 2 kW放電の実行要求
            D->>K: Adapter経由の蓄電池操作
        and EV充電の制御
            O->>L: 1 kW充電削減の実行要求
            L->>K: Adapter経由のEV充電操作
        end
        K-->>D: 蓄電池の状態・実測
        K-->>L: EV充電の状態・実測
        D-->>O: DER実行結果
        L-->>O: 負荷実行結果
        O-->>H: 計画結果と残る目標差
        H-->>I: 達成・未達・再計画結果
        I-->>C: 受付状態と実行結果を分けて報告
    else 全体または一部が不許可
        A-->>H: 拒否・部分許可と理由
        H->>H: 許可範囲内で再計画
    end
```

複数機器の操作は物理的に原子的ではありません。図の並行実行は、順序・電力過渡が許される場合の例です。必要なら「充電削減を確認してから放電開始」等の順序へ変更します。採用する順序はOrchestratorが所有します。

## UC-02：特定のDERへの直接的な通常運転要求

例：「蓄電池Bを2 kWで放電」。機器選定の最適化は省略できますが、通常運転の権限・競合確認は省略しません。

```mermaid
sequenceDiagram
    autonumber
    participant C as クラウドまたは利用者UI
    participant I as 要求受付Usecase
    participant A as Control Arbiter
    participant O as Orchestrator
    participant D as DER Power Controller
    participant E as Device Adapter
    participant K as 蓄電池システム
    C->>I: 蓄電池Bを2 kW放電
    I->>A: 正規化したControlRequest
    alt 許可
        A-->>O: Authorityと実行要求
        O->>D: 蓄電池Bの操作を実行
        D->>D: Capability・状態・制御権世代を確認
        D->>E: 機器プロファイルに従う操作系列
        E->>K: 通常運転の設定要求
        K-->>E: 受理または不可応答
        E-->>D: 設定要求の応答
        D->>E: 状態・実電力の確認
        E->>K: 状態取得
        K-->>E: 観測可能な状態・実電力
        E-->>D: 観測結果と品質
        D-->>O: 達成・制限・未達・不明
        O-->>I: 実行結果
        I-->>C: 結果通知
    else 競合または権限不足
        A-->>I: 拒否または保留
        I-->>C: 理由付き応答
    end
```

ECHONET Lite蓄電池AIFでは、Set_Resは受理応答であり、物理動作の完了通知ではありません。[S07](12_Sources.md#s07) 本設計では、受理と達成を別ステータスで管理します。

## UC-03：クラウドを使わない自律的な高度エネマネ

```mermaid
flowchart LR
    T["時刻到来・計測更新・予測更新"] --> H["高度エネマネ<br/>自家消費・料金・充電期限を計画"]
    H --> A["Control Arbiter<br/>利用者・他クラウドとの競合を確認"]
    A --> O["Orchestrator"]
    O --> D["DER Power Controller"]
    O --> L["Flexible Load Controller"]
    D --> K["実機<br/>Adapter経由"]
    L --> K
    K -.-> M["Measurement Service"]
    M -.-> H
```

自律HEMSも一つの通常運転要求元です。「内部の処理だから常に最高優先」とはしません。優先関係は制御ポリシーに定義します。

## UC-04：電力会社の出力制御とHEMS要求が同時に存在

```mermaid
sequenceDiagram
    autonumber
    participant U as 電力会社サーバ
    participant S as 出力制御ユニット
    participant G as 機器内の制約強制
    participant P as 電力変換部
    participant D as DER Power Controller
    participant H as HEMS上位処理
    S->>U: スケジュール取得のため接続
    U-->>S: 対象設備の出力制御スケジュール
    S->>S: 検証・保存・時刻による適用
    S->>G: 対象範囲と上限制約
    H->>D: 許可済み通常運転要求
    D->>G: Adapter経由の機器操作要求
    G->>G: 独立計測と機器状態から許容運転を決定
    G->>P: 制約内の指令
    G-->>D: 提供可能な運転状態・実測
    D-->>H: 通常運転要求に対する結果
    H->>H: 必要に応じて再計画
    Note over S,P: 電力会社制約はHEMSの判断や応答を待たない
    Note over H,D: 参照する制約情報は原本ではない
```

公開PCS仕様は、スケジュールによる出力制御ユニットとPCSの構成を定義しています。[S05](12_Sources.md#s05) この図はそれに通常運転経路を併存させる設計案であり、特定メーカー機器の実装図ではありません。

## UC-05：機器側制限・本体操作・故障によって計画が成立しなくなる

```mermaid
sequenceDiagram
    autonumber
    participant K as 機器
    participant E as Device Adapter
    participant D as DER Power Controller
    participant O as Orchestrator
    participant H as 高度エネマネ
    participant A as Control Arbiter
    K->>K: 本体操作・SoC制限・保護等で状態変化
    K-->>E: 通知または状態取得への応答
    E-->>D: 正規化した観測と品質
    D->>D: 要求と観測の不一致を評価
    D-->>O: 制限・未達・ローカル変更・不明
    O-->>H: 計画の再評価を要求
    H->>H: 代替操作または目標緩和を検討
    H->>A: 新しいControlRequest
    A-->>O: 現在条件で許可された操作
    Note over K,D: 機器の保護動作はHEMSの承認を待たない
```

機器の出力が小さいだけでは、電力会社の出力制御、熱制限、SoC制限、日射不足、ユーザー操作のどれが原因か確定できません。理由が取得できないときは `reason=UNKNOWN` として報告し、推測を確定原因として記録しません。

利用者の本体操作をHEMSが無条件に上書きし続けないように、ローカル操作検知後の扱いを制御ポリシーと機器プロファイルに定義します。

## UC-06：HEMSのOTA・再起動

```mermaid
sequenceDiagram
    autonumber
    participant O as HEMS Orchestrator
    participant D as DER Power Controller
    participant K as 機器の通常運転受付
    participant S as 出力制御ユニット
    participant G as 機器内の系統制御
    O->>D: 更新前に実行を整理
    D->>K: 機器仕様で可能な終了・継続設定
    D-->>O: 更新前状態と未完了要求を記録
    O->>O: HEMS更新・再起動
    S->>G: 保存スケジュールを継続実行
    G->>G: 系統制約と保護を継続
    O->>D: 復帰後の状態照合
    D->>K: 実機状態を再取得
    K-->>D: 現在状態
    D-->>O: 現在状態と旧要求との差分
    O->>O: 旧コマンドを盲目的再生せず再調停
    Note over K,G: 通常要求の保持と系統制御継続は別の契約
```

正常なOTAでは更新前整理を行えますが、電源断・クラッシュ時には実行できません。したがって、OTA前処理だけを安全根拠にせず、機器側の通信断・要求残留動作を評価します。

## UC-07：系統異常による保護動作

```mermaid
flowchart LR
    M["系統側の独立計測"] --> P["系統連系保護<br/>機器側で判定"]
    P --> A["保護停止・必要な解列"]
    P -.-> S["公開可能な保護状態"]
    S -.-> H["HEMS<br/>表示・記録・再計画停止"]
```

これは上位から届く通常運転要求ではありません。HEMSを通過させず、保護の成立後に状態を参照します。復帰や再連系も適用仕様の管理下とし、HEMSの通常操作APIで強制解除しません。

関連： [契約](06_Contracts.md)／[障害](08_Deployment_Failures_OTA.md)／[試験](10_Requirements_Tests.md)
