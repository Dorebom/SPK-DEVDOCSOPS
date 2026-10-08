---
schema: spkgw.governance-note/v1
document_id: BUD-SPKGW-EXAMPLE
project: SPK-GW_HEMS
document_type: TEMPLATE
revision: 1.2.0
status: TEMPLATE
title: 予算・原価管理基準案
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
document_trace_id: DTR-SPKGW-TEMPLATE-000002
item_trace_ids: []
---

# 予算・原価管理基準案

| 項目 | 記入値 |
|---|---|
| 期間・WBS・リリース | 未確定 |
| 通貨・税基準・原価と現金区分 | 未確定 |
| 内部工数単価・費目・委託費 | 未確定 |
| 予備費・承認上限・変更閾値 | 未確定 |
| AI・クラウド費の配賦 | 未確定 |
| 原票・会計照合・締め | 未確定 |
| 承認者・対象hash・日付 | 未承認 |

BAC/AC/OC/ETC/EAC/VACはSTD-GOV-008に従う。発注残を含むETCへOCを再加算しない。

## R12：文書と項目の識別

文書は`document_trace_id`（DTR）、個別項目は`item_trace_id`（ITR）、目的の束ねは任意の`thread_id`（THR）。本文中の旧「Trace」が作業相関を表す場合はTHRを指す。[TraceID標準](../STD_03_TraceID.md)に従い、文書リンクを項目の実装・検証リンクの代わりにしない。工程は英字略称、担当未確定はUNASSIGNED。

## Open Questions

未記入欄を実担当・根拠・値で置換する。サンプルは作業・支出・量産操作の認可ではない。
