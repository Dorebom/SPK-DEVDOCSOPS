---
schema: spkgw.governance-note/v1
document_id: TPL-GOV-TRACE
project: SPK-GW_HEMS
document_type: TEMPLATE
revision: 1.1.0
status: TEMPLATE
title: Traceテーマ・17工程・必要成果の計画
owner: null
trace_id: TRC-SPKGW-000001
created_on: '2026-10-08'
updated_on: '2026-10-08'
classification: INTERNAL
source_baseline: BL-R9-0001
trace_contract: spkgw.lifecycle-tags/v1
related_trace_ids: []
phase_ids: []
phase_scope: UNASSIGNED
activity_type: PROJECT_MANAGEMENT
related_ids: []
---

# Traceテーマ・17工程・必要成果の計画

## テーマの定義
control.json.tracesへ不変TraceID、目的、根拠を登録する。本文には対象製品・機能・変更範囲、起点、対象外を記載する。

## 工程適用と必要な証拠
trace_graph.jsonのphase_planにP01〜P17を1件ずつ登録。APPLICABLE／NOT_APPLICABLE／TBD、必要成果kind、根拠、確認記録を持つ。N/Aは理由と決定証拠が必要。

## 入力・成果・関係
各成果の安定IDとrevision、node_id、主／関連Trace、phase_ids、ファイルhash・場所を登録する。上流・下流の関係を型付きedgeで持つ。

## 継続・分岐・改善
リリースでTraceを切らない。新目的には新Traceを作りsplit_from／follow_up_toで関連付ける。

## Open Questions
粒度、対象工程、必須成果、確認担当・証拠を具体化する。
