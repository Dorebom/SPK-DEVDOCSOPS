---
title: "通常運転要求・制御権・実行結果の契約"
document_id: "SPKGW-SYS-R6-05"
revision: "R6"
updated: 2026-10-06
status: DRAFT_FOR_REVIEW
source_baseline: "System_Spec_R5 + Coverage_Review_A1 + CTX-R6"
---

<a id="ch-05"></a>
# 05. 通常運転要求・制御権・実行結果の契約

根拠：[06_Contracts.md](../sources/architecture/06_Contracts.md) ／ [03_Command_Flows.md](../sources/architecture/03_Command_Flows.md) ／ [09_Risks_Alternatives.md](../sources/architecture/09_Risks_Alternatives.md)。ユーザー明示事項・本書の具体化案は本文で区別する。

## 5.1 意味論を固定する

添付の`spkgw.control-request/v1`、`spkgw.control-authority/v1`等はDomain契約例であり、標準のECHONET Lite電文ではない。C構造体、IPC、JSON等を確定する前に、操作の意味・対象・単位・符号・期限・権限・結果を固定する。

| 契約 | 必須とする意味 | 備考 |
|---|---|---|
| EnergyGoal | 目的・対象時間・拘束条件・要求元 | 機器配分が必要ならEMSへ |
| ControlRequest | request/correlation、actor、resource/group/PCC、operation、値、期間、idempotency、policy_class | 送信者の数値priorityだけで優先度を決めない |
| ControlAuthority | authority、resource_scope、holder、epoch、期限、許可操作、policy_revision | 最後の共通送信境界でも確認 |
| Capability | 実在する操作、値域、最小更新間隔、失効・理由取得能力、profile | 未確認はUNKNOWN／EXAMPLE扱い |
| ConstraintObservation | source、quantity、scope、基準、上限、有効時刻、品質、強制所有者 | READ_ONLY_MIRROR、原本ではない |
| ExecutionResult | 要求・権威・対象、受理段階、観測条件、達成／制限／未達／不明 | 達成とプロトコル応答を分離 |

具体スキーマの必須項目・列挙・互換性は別レビュー対象である。添付の例示値やIDを製品設定として登録しない。

## 5.2 操作の区別

`REQUEST_ACTIVE_POWER`の目標値、通常運転の電力上限、運転モード、スケジュール要求、解除は意味が異なる。本書の具体化案として、operationと操作プロファイルで区別し、未対応の電力目標を黙って電力上限へ変換して成功にしない。許可された代替がある場合は結果に明示する。

通常APIに保護閾値変更、出力制御解除、スケジュール原本設定、G側時計設定、発電所ID変更、認証側FW書込みを公開しない。モードAPIにも許可リストを持たせ、任意の数値で自立・再連系・系統支援へ移れる仕様にしない。

## 5.3 権威・期限と送信境界

Arbiterの採否判定後にも権威交代は起こり得る。DPCで実行前確認し、最後の共通送信境界でepoch・対象・期限を再確認する。旧世代の待機操作は送信しない。Adapterはこの契約検査を行ってよいが、独自の運転優先ポリシーを作らない。

すでに送信した電文、機器内キュー、機器が保持する設定はGWのepochで完全取消しできるとは限らない。取消し可能範囲を区別し、機器状態を照合して現在の権威で補正する。内部Leaseによるexactly-once又は機器自動停止は保証しない。

外部予定時刻・期限はタイムゾーン付き実時刻、経過時間は単調時計を用いる設計を継承する。再起動時に旧単調時計や旧権威をそのまま復元しない。G側時計は別に管理する。

## 5.4 実行状態

```mermaid
stateDiagram-v2
    [*] --> Received
    Received --> Rejected: 認可・形式・期限等で不適合
    Received --> Authorized: 通常制御権取得
    Authorized --> Expired: 送信前失効
    Authorized --> Sent: 送信境界再確認
    Sent --> DeviceAccepted: 受理確認
    Sent --> Failed: 明確な不可応答
    Sent --> Unknown: 応答喪失
    DeviceAccepted --> Verified: 観測条件で達成確認
    DeviceAccepted --> Limited: 根拠付きの制限確認
    DeviceAccepted --> Unmet: 未達を観測
    DeviceAccepted --> Unknown: 実状態確認不可
    Unknown --> Verified: 後続照合で達成確認
    Unknown --> Unmet: 後続照合で未達確認
    Rejected --> [*]
    Expired --> [*]
    Failed --> [*]
    Verified --> [*]
    Limited --> [*]
    Unmet --> [*]
```

この図は添付のモデルを継承する。Unknownは自動的にFailed／再試行へ落とさない。Unknownの保持期限・手動エスカレーション・未解決終端の形式は本書で勝手に追加確定せず、SYS-TBD-008で決める。

| 区別 | 規定 |
|---|---|
| 受理と達成 | 応答が受理か、反映か、運転到達かを操作ごとに対応付ける |
| Verified | 測定点・許容差・確認窓の条件内での確認。永久達成ではない |
| LimitedとUnmet | 制限理由が取得できた場合のみLimited。低出力から原因を断定しない |
| Expiredと機器停止 | GWの実行権限失効は実機の停止確認ではない |
| Timeoutと不実行 | 応答喪失時に機器が実行済みの可能性を残す |

## 5.5 要求と観測の対応：追加の具体化案

要求値、送信値、読み戻した設定、実運転状態、実測値を分け、値が得られない段階はUNKNOWNとして記録する。単位・符号・時刻基準を各値に結び付ける。相関IDは因果の追跡に用いるが、同時刻に同値が観測されたことだけで他の操作元の関与を否定しない。

通知の重複・順序逆転・遅延応答はrequest/correlation/epochで整合させ、旧応答で旧権威を復活させない。冪等キーの保存期間・再利用条件・再起動後の有効範囲は未確定パラメータとして管理する。

## 5.9 R2追加：上位公開Envelopeと経路区分

上位・ローカルの共通境界ではrequest_id、主体／配送サービス、対象住宅・GW・所属世代、操作種別、scope、期限、idempotency_key、payload/schema版を必要な契約に合わせて検査する。フィールド名は案であり、既存ControlRequestの意味を置き換えない。

通常運転は本章の権威・実行結果へ対応させ、設定・内部操作・情報取得・FW更新は各担当Usecaseへ分ける。要求種類が違ってもG側禁止操作、監査、機器への迂回防止を共有する。クラウド受付／GW受付／機器受理／達成の区別は[第20章](20_Northbound_Monitoring_FW.md#ch-20)による。


## 5.10 R3導入・R4適用：通常権威と系統構成世代の分離

通常ControlRequestのArbiter epochは、出力制御方式の切替権限を付与しない。GW_MANAGEDのG側はgrid_control_epoch・対象scope・スケジュール版を独立管理し、旧経路からの遅延要求を確認可能な最終境界で拒否する。実PCSがこの世代を理解しない場合は、送信元無効化、キュー処理、機器側設定確認・実状態照合で旧経路をフェンスする。内部番号を追加しただけで実機の排他やexactly-onceを保証しない。

<!-- R6:COMPLETION_ITEMS -->

> **R6の補完範囲：** 以下はレビューA1から追加した章節項の記入枠であり、数値・機種・機能採否・個別規格適用を推定した確定仕様ではない。各項末のリンクから、本章末尾の具体的な質問・必要資料・確定時点を確認できる。

**記入先・関連する規範候補別冊：** [外部・内部IF契約の具体化項目](../appendices/Interface_Contract_Detail.md) ／ [品質・利用目的・ライフサイクル受入の具体化項目](../appendices/Quality_Acceptance_Profiles.md)

## 5.11 操作別の調停と実行確定条件

<a id="slot-r6-05-01"></a>
### 5.11.1 優先関係・同順位・取消し・並行実行

**補完項目ID：** `SLOT-R6-05-01`。**対応観点：** C07, C13（[レビューA1](../sources/review/R5_Coverage_Review_A1.md)）。

R5の既存原則は保持するが、この項の全対象・具体条件・規範参照は未確定。

**本項に記載する仕様項目：**

- 主体×操作×競合scope。
- 同順位・部分許可・Lease。
- 取消し・補償・最後の送信境界。

**本項の完成判定：** 通常操作の優先表、同時実行許可表、要求失効と補償の決定表を機器能力と対応付ける。

**具体的な不足：** [OQ-R6-05-01](#oq-r6-05-01)。採用値・参照版・対象外理由は回答後に本項又は版指定の規範別冊へ反映する。

<a id="slot-r6-05-02"></a>
### 5.11.2 結果・確認窓・不明状態の終端

**補完項目ID：** `SLOT-R6-05-02`。**対応観点：** C07, C22（[レビューA1](../sources/review/R5_Coverage_Review_A1.md)）。

R5の既存原則は保持するが、この項の全対象・具体条件・規範参照は未確定。

**本項に記載する仕様項目：**

- 受理/送信/機器受理/達成の条件。
- 許容差・評価窓・理由の根拠。
- Unknownの再確認・終端・通知。

**本項の完成判定：** 操作別結果判定表とUnknownの再照合・終端方針を定義し、APIとUIの同一意味を確認する。

**具体的な不足：** [OQ-R6-05-02](#oq-r6-05-02)。採用値・参照版・対象外理由は回答後に本項又は版指定の規範別冊へ反映する。

<!-- R6:OPEN_QUESTIONS -->
<a id="oq-list-chapters-05-control-contracts-md"></a>
## Open Questions — 本ノートを完成させるための未決事項

以下は本章の具体的な未決事項。**担当者・回答期限の日付・採用値・承認結果は未確定**である。担当ロールと確定ゲートは提案。回答を得ただけでは閉じず、根拠確認・決定・本文と関連台帳への反映を行う。
全体索引：[Open Question横断台帳](../appendices/Open_Question_Register.md)。各質問の編集正本は[data/completion_items.json](../data/completion_items.json)。

<a id="oq-r6-05-01"></a>
### OQ-R6-05-01 — 優先関係・同順位・取消し・並行実行

**対象項：** [5.11.1 優先関係・同順位・取消し・並行実行](#slot-r6-05-01)

**質問：** 利用者、本体操作、各クラウド、既存運転、高度エネマネが競合するとき、操作別の優先順位と同順位処理をどう決めるか。途中実行の取消しをどこまで保証するか。

**必要資料・完了条件：** 通常操作の優先表、同時実行許可表、要求失効と補償の決定表を機器能力と対応付ける。

**決定担当：** 未割当（候補：制御設計・製品企画）。承認者：未定。

**確定時点：** G2＝該当するIF・データ・操作等の詳細契約確定前（提案）。回答期限の日付：未定。

**未解決時の制約：** 「優先関係・同順位・取消し・並行実行」を対象構成の確定保証・実装受入根拠として使用しない。

**既存ID：** TBD-009, TBD-007, PAR-AUTH-01。

**状態：** OPEN。**回答：** 未記入。**決定記録：** 未記入。

<a id="oq-r6-05-02"></a>
### OQ-R6-05-02 — 結果・確認窓・不明状態の終端

**対象項：** [5.11.2 結果・確認窓・不明状態の終端](#slot-r6-05-02)

**質問：** 各操作の達成をどの計測点・許容差・確認時間で判定するか。応答や観測がない場合にUnknownを何時まで保持し、何を利用者へ返すか。

**必要資料・完了条件：** 操作別結果判定表とUnknownの再照合・終端方針を定義し、APIとUIの同一意味を確認する。

**決定担当：** 未割当（候補：制御・測定・UI設計）。承認者：未定。

**確定時点：** G3＝該当する検証仕様・受入プロファイルの確定前（提案）。回答期限の日付：未定。

**未解決時の制約：** 「結果・確認窓・不明状態の終端」を対象構成の確定保証・実装受入根拠として使用しない。

**既存ID：** SYS-TBD-008, TBD-008, PAR-RESULT-01, PAR-RESULT-02。

**状態：** OPEN。**回答：** 未記入。**決定記録：** 未記入。
