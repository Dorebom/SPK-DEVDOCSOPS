---
schema: spkgw.governance-note/v1
document_id: CHG-SPKGW-EXAMPLE
project: SPK-GW_HEMS
document_type: TEMPLATE
revision: 1.3.0
status: TEMPLATE
title: 変更要求・影響評価
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
document_trace_id: DTR-SPKGW-TEMPLATE-000003
item_trace_ids: []
---

# 変更要求・影響評価

変更目的、原本、旧新差、要求/IF/構成/権限/性能/G側/試験影響、費用・期間、代替案、却下時の影響、承認者・範囲、実施TASK、検証、採用Baselineを記す。

## R12：文書と項目の識別

文書は`document_trace_id`（DTR）、個別項目は`item_trace_id`（ITR）、目的の束ねは任意の`thread_id`（THR）。本文中の旧「Trace」が作業相関を表す場合はTHRを指す。[TraceID標準](../STD_03_TraceID.md)に従い、文書リンクを項目の実装・検証リンクの代わりにしない。工程は英字略称、担当未確定はUNASSIGNED。

## R13追補：適用条件を先に比較
[変更影響票](Change_Impact.md)を必要に応じ使う。対象機種/HW/FW、As-Is/To-Be、経路、操作/計測点、単位・時間起点を確認してから同値/追加/適用差/矛盾を判断する。R2は境界影響区分であり、全通常作業の禁止でもツール許可でもない。

## Open Questions

未記入欄を実担当・根拠・値で置換する。サンプルは作業・支出・量産操作の認可ではない。
