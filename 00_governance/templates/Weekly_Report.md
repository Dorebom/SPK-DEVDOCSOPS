---
schema: spkgw.governance-note/v1
document_id: RPT-SPKGW-EXAMPLE
project: SPK-GW_HEMS
document_type: TEMPLATE
revision: 1.3.0
status: TEMPLATE
title: 週次進捗・予算報告
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
document_trace_id: DTR-SPKGW-TEMPLATE-000014
item_trace_ids: []
---

# 週次進捗・予算報告

対象期間、締め日時、入力hash、文書/計画/予算版、受入成果、状態別件数、未見積・未入力、基準差、残作業、AC/OC/ETC/EAC/VAC、BLOCKED・リスク、決定依頼、次のTASKを記す。

報告値は集計結果を用い、未入力を0へ変えない。

## R12：文書と項目の識別

文書は`document_trace_id`（DTR）、個別項目は`item_trace_id`（ITR）、目的の束ねは任意の`thread_id`（THR）。本文中の旧「Trace」が作業相関を表す場合はTHRを指す。[TraceID標準](../STD_03_TraceID.md)に従い、文書リンクを項目の実装・検証リンクの代わりにしない。工程は英字略称、担当未確定はUNASSIGNED。

## R13追補：基準計画の切替と阻害
同じ締め時点の旧/新計画ID、受入済み基準工数の分子/分母/率、変更理由と承認根拠を併記する。取消しを無断で分母から除かない。WIP・待機・見通し・追加された作業は観測原票付きで表示し、自動算出未対応なら手計算根拠を明示する。

## Open Questions

未記入欄を実担当・根拠・値で置換する。サンプルは作業・支出・量産操作の認可ではない。
