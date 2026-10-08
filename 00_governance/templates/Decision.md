---
schema: spkgw.governance-note/v1
document_id: DEC-SPKGW-EXAMPLE
project: SPK-GW_HEMS
document_type: TEMPLATE
revision: 1.2.0
status: TEMPLATE
title: 判断・承認記録
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
document_trace_id: DTR-SPKGW-TEMPLATE-000004
item_trace_ids: []
---

# 判断・承認記録

対象・旧新版・対象hash、判断者と権限範囲、実判断日時、決定、理由、比較案、条件・期限、影響TASK/PLN/BUD/BL、根拠EVDを記す。

テンプレートにAPPROVEDを記入しただけで本人認証や契約承認にはならない。

## R12：文書と項目の識別

文書は`document_trace_id`（DTR）、個別項目は`item_trace_id`（ITR）、目的の束ねは任意の`thread_id`（THR）。本文中の旧「Trace」が作業相関を表す場合はTHRを指す。[TraceID標準](../STD_03_TraceID.md)に従い、文書リンクを項目の実装・検証リンクの代わりにしない。工程は英字略称、担当未確定はUNASSIGNED。

## Open Questions

未記入欄を実担当・根拠・値で置換する。サンプルは作業・支出・量産操作の認可ではない。
