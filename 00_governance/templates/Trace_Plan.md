---
schema: spkgw.governance-note/v1
document_id: TPL-GOV-TRACE
project: SPK-GW_HEMS
document_type: TEMPLATE
revision: 1.2.0
status: TEMPLATE
title: Traceテーマ・17工程・必要成果の計画
owner: null
created_on: '2026-10-08'
updated_on: '2026-10-08'
classification: INTERNAL
source_baseline: BL-R9-0001
trace_contract: spkgw.lifecycle-tags/v2
phase_ids: []
phase_scope: UNASSIGNED
activity_type: PROJECT_MANAGEMENT
related_ids: []
thread_id: THR-SPKGW-GOV-000001
related_thread_ids: []
document_trace_id: DTR-SPKGW-TEMPLATE-000013
item_trace_ids: []
---

# Traceテーマ・17工程・必要成果の計画

## テーマの定義
control.json.tracesへ不変TraceID、目的、根拠を登録する。本文には対象製品・機能・変更範囲、起点、対象外を記載する。

## 工程適用と必要な証拠
trace_graph.jsonのphase_planにCONCEPT〜IMPROVEを1件ずつ登録。APPLICABLE／NOT_APPLICABLE／TBD、必要成果kind、根拠、確認記録を持つ。N/Aは理由と決定証拠が必要。

## 入力・成果・関係
各成果の安定IDとrevision、node_id、主／関連Trace、phase_ids、ファイルhash・場所を登録する。上流・下流の関係を型付きedgeで持つ。

## 継続・分岐・改善
リリースでTraceを切らない。新目的には新Traceを作りsplit_from／follow_up_toで関連付ける。

## R12：文書と項目の識別

文書は`document_trace_id`（DTR）、個別項目は`item_trace_id`（ITR）、目的の束ねは任意の`thread_id`（THR）。本文中の旧「Trace」が作業相関を表す場合はTHRを指す。[TraceID標準](../STD_03_TraceID.md)に従い、文書リンクを項目の実装・検証リンクの代わりにしない。工程は英字略称、担当未確定はUNASSIGNED。

## Open Questions
粒度、対象工程、必須成果、確認担当・証拠を具体化する。
