---
schema: spkgw.governance-note/v1
document_id: GOV-TEMPLATES-001
project: SPK-GW_HEMS
document_type: MOC
revision: 1.3.0
status: DRAFT_FOR_REVIEW
title: 管理テンプレート一覧
owner: null
created_on: '2026-10-08'
updated_on: '2026-10-08'
classification: INTERNAL
source_baseline: BL-R9-0001
related_ids: []
thread_id: THR-SPKGW-GOV-000001
related_thread_ids: []
trace_contract: spkgw.lifecycle-tags/v2
phase_ids: []
phase_scope: UNASSIGNED
activity_type: UNSPECIFIED
document_trace_id: DTR-SPKGW-TEMPLATE-000008
item_trace_ids: []
---

# 管理テンプレート一覧

Task.mdは実TASKの雛形。その他は文書TEMPLATEで、用途別に実ID・種別を設定してから採用する。

| テンプレート | 用途 |
|---|---|
| [Task.md](Task.md) | 作業状態・完了条件 |
| [Plan.md](Plan.md) | 計画・WBS・マイルストーン案 |
| [Budget.md](Budget.md) | 予算・原価管理基準案 |
| [Execution.md](Execution.md) | 実行記録 |
| [Review.md](Review.md) | レビュー・受入記録 |
| [Change.md](Change.md) | 変更要求・影響評価 |
| [Risk.md](Risk.md) | リスク・課題 |
| [Decision.md](Decision.md) | 判断・承認記録 |
| [Weekly_Report.md](Weekly_Report.md) | 週次進捗・予算報告 |
| [AI_Work_Order.md](AI_Work_Order.md) | AI作業指示 |

## R11追加
[Traceテーマ・工程計画](Trace_Plan.md) ／ [会議・議題](Meeting.md) ／ [調査](Research.md)。Taskの17工程属性と併用する。例示は実施・承認済みではない。

## R12：文書と項目の識別

文書は`document_trace_id`（DTR）、個別項目は`item_trace_id`（ITR）、目的の束ねは任意の`thread_id`（THR）。本文中の旧「Trace」が作業相関を表す場合はTHRを指す。[TraceID標準](../STD_03_TraceID.md)に従い、文書リンクを項目の実装・検証リンクの代わりにしない。工程は英字略称、担当未確定はUNASSIGNED。

## R13追加テンプレート
[変更影響](Change_Impact.md)／[設計](Design_Note.md)／[委託先回答](Supplier_Response.md)／[任意Capabilityログ](AI_Capability_Log.md)／[リリース](Release.md)／[Copilot環境確認](Copilot_Environment_Check.md)。小変更はTASKに必要欄をまとめてよい。未記入票は実績や承認の根拠にしない。

## Open Questions

[ガバナンスOQ](../Open_Questions.md)へ接続する。Taskテンプレートはcontrol.jsonに登録済みのTrace/Actor/WBSへ対応させる。
