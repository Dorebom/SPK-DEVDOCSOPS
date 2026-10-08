---
schema: spkgw.governance-note/v1
document_id: EVD-SPKGW-EXAMPLE
project: SPK-GW_HEMS
document_type: TEMPLATE
revision: 1.3.0
status: TEMPLATE
title: レビュー・受入記録
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
document_trace_id: DTR-SPKGW-TEMPLATE-000010
item_trace_ids: []
---

# レビュー・受入記録

対象TASK・成果物hash・要件ID、実行者、レビューActor、独立性、基準版、各完了条件と根拠、指摘、是正確認、ACCEPT/REWORK/REJECT、判定日時を記す。

レビュー資料が存在することと、受入を承認したことは別。

## R12：文書と項目の識別

文書は`document_trace_id`（DTR）、個別項目は`item_trace_id`（ITR）、目的の束ねは任意の`thread_id`（THR）。本文中の旧「Trace」が作業相関を表す場合はTHRを指す。[TraceID標準](../STD_03_TraceID.md)に従い、文書リンクを項目の実装・検証リンクの代わりにしない。工程は英字略称、担当未確定はUNASSIGNED。

## R13追補：自己評価と独立評価
評価者・実施形態・対象revision、差分・契約・異常・資源・互換・未実施を記す。指摘→対応→再確認の参照を残す。AIの二回目レビューを他者による独立審査と表現しない。結果とTASK受入は別記録。

## Open Questions

未記入欄を実担当・根拠・値で置換する。サンプルは作業・支出・量産操作の認可ではない。
