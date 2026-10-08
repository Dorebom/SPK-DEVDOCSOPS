---
schema: spkgw.governance-note/v1
document_id: PLN-SPKGW-EXAMPLE
project: SPK-GW_HEMS
document_type: TEMPLATE
revision: 1.2.0
status: TEMPLATE
title: 計画・WBS・マイルストーン案
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
document_trace_id: DTR-SPKGW-TEMPLATE-000007
item_trace_ids: []
---

# 計画・WBS・マイルストーン案

対象Baseline、スコープ、WBS全leaf、既存／追加／変更／取消し、担当、依存、開始・終了、基準工数weight、成果区分DISCRETE/LOE、工程ゲート、リスク、承認対象hashを記す。

| task_id | WBS | Owner | 基準工数 | 基準開始 | 基準終了 | 依存 | 受入条件 |
|---|---|---|---|---|---|---|---|

未記入は未確定。予算基準はBUDで別承認する。

## R12：文書と項目の識別

文書は`document_trace_id`（DTR）、個別項目は`item_trace_id`（ITR）、目的の束ねは任意の`thread_id`（THR）。本文中の旧「Trace」が作業相関を表す場合はTHRを指す。[TraceID標準](../STD_03_TraceID.md)に従い、文書リンクを項目の実装・検証リンクの代わりにしない。工程は英字略称、担当未確定はUNASSIGNED。

## Open Questions

未記入欄を実担当・根拠・値で置換する。サンプルは作業・支出・量産操作の認可ではない。
