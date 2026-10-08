---
schema: spkgw.governance-note/v1
document_id: GOV-TEMPLATES-001
project: SPK-GW_HEMS
document_type: MOC
revision: 1.1.0
status: DRAFT_FOR_REVIEW
title: 管理テンプレート一覧
owner: null
trace_id: TRC-SPKGW-000001
created_on: '2026-10-08'
updated_on: '2026-10-08'
classification: INTERNAL
source_baseline: BL-R9-0001
related_ids: []
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

## Open Questions

[ガバナンスOQ](../Open_Questions.md)へ接続する。Taskテンプレートはcontrol.jsonに登録済みのTrace/Actor/WBSへ対応させる。
