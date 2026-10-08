---
title: "MOC — SPK-GW_HEMS 推奨最終形"
project: SPK-GW_HEMS
version: "1.0"
created: 2026-10-06
updated: 2026-10-06
status: recommended-draft
language: ja
tags: [SPK-GW_HEMS, architecture, HEMS, JET]
---

# MOC — SPK-GW_HEMS 推奨最終形

## 全体の読み順

| ノート | 主に答える問い |
|---|---|
| [01 全体アーキテクチャ](01_Architecture.md) | どこがHEMSで、どこが系統制御なのか |
| [02 責務とレイヤー](02_Responsibilities.md) | Arbiter、Orchestrator、DER Power Controllerの違いは何か |
| [03 指令経路とユースケース](03_Command_Flows.md) | クラウド・HEMS・電力会社の指示が機器へどう届くか |
| [04 JET認証影響分離](04_JET_Isolation.md) | 何を固定し、何を説明し、何が再評価対象になるか |
| [05 機器分類とトポロジー](05_Device_Classes.md) | どの機器をどのControllerが扱い、出力制御対象をどう判定するか |
| [06 インターフェースと状態契約](06_Contracts.md) | 要求、制御権、期限、結果をどう表すか |
| [07 電力制約モデル](07_Power_Constraints.md) | 機器出力と連系点逆潮流の制約をどう区別するか |
| [08 配置・障害・OTA](08_Deployment_Failures_OTA.md) | HEMS停止時にも何を継続させるか |
| [09 制約・問題点・対応策](09_Risks_Alternatives.md) | できなくなること、残るリスク、代替策は何か |
| [10 要求と受入試験](10_Requirements_Tests.md) | どの根拠で設計の成立を確認するか |
| [11 移行・判断・未確定事項](11_Migration_Decisions.md) | As-Isからどう進め、何をまだ決めていないか |
| [12 出典と確認範囲](12_Sources.md) | 何が公開仕様で、何が設計提案か |

## 目的別の入口

**機器までの指令経路を理解する**場合は、01 → 02 → 03 → 06 の順に読みます。

**将来のJET変更審査を軽くしたい**場合は、04 → 08 → 09 → 10 と [変更影響評価テンプレート](templates/Release_Impact_Checklist.md) を読みます。

**対応するPV・蓄電池・V2H等を決める**場合は、05 → 07 → 06 と [機器プロファイルテンプレート](templates/Device_Profile.md) を読みます。

**既存EIG/HEMS実装へ段階導入する**場合は、02 → 11 → 10 を読みます。レイヤーとプロセスは同一ではなく、単一Coreへの集中を前提にしません。

## 核となる責務分離

| 判断すること | 責務 |
|---|---|
| 何を達成したいか | 外部クラウド・利用者・HEMSの目標 |
| 何をすれば達成できるか | 高度エネルギーマネジメント |
| 誰の通常運転要求を採用するか | Control Arbiter |
| 許可された計画をどう進めるか | Energy Orchestrator |
| DERごとの操作をどう実行・確認するか | DER Power Controller |
| どの電文・プロパティへ変換するか | Device Adapter |
| 実際に何を実行できるか | 機器側の運転制御・制約強制 |
| 系統異常に対して何を停止・解列するか | 系統連系保護 |

## 設計上の境界

通常運転の**希望**と、系統側の**制約**は同じ優先順位キューに入れません。HEMSが制約情報のコピーを計画に使うことと、HEMSが制約の成立責任を持つことも区別します。

全編を一つで読む場合： [統合版](90_All_In_One.md)。
