---
schema: spkgw.governance-note/v1
document_id: TPL-GOV-RESEARCH
project: SPK-GW_HEMS
document_type: TEMPLATE
revision: 1.2.0
status: TEMPLATE
title: 調査・原文・解釈・影響
owner: null
created_on: '2026-10-08'
updated_on: '2026-10-08'
classification: INTERNAL
source_baseline: BL-R9-0001
trace_contract: spkgw.lifecycle-tags/v2
phase_ids: []
phase_scope: UNASSIGNED
activity_type: RESEARCH
related_ids: []
thread_id: THR-SPKGW-GOV-000001
related_thread_ids: []
document_trace_id: DTR-SPKGW-TEMPLATE-000009
item_trace_ids: []
---

# 調査・原文・解釈・影響

## 調査の目的と範囲
RES ID、TASK、主Trace／関連Trace、phase_ids、問い、範囲外、入力版を記入する。

## 原資料と取得状況
source_id・原本hash・locator・未取得部分を参照。原資料は30_referencesへ保持。

## 事実・解釈・仮説
原文／観測、解釈、仮説、確度・制限を分ける。要件の理由を捏造しない。

## 結論・採否・次作業
対応可能／不適合／追加調査も正当な結果。影響SYS／設計／IF／テスト、DEC・OQ・派生TASKへリンクする。

## 追跡関係
調査→対象はinvestigates、結論→調査実行はresult_of、採用要求・設計→確認済み調査結果はderives_from。

## R12：文書と項目の識別

文書は`document_trace_id`（DTR）、個別項目は`item_trace_id`（ITR）、目的の束ねは任意の`thread_id`（THR）。本文中の旧「Trace」が作業相関を表す場合はTHRを指す。[TraceID標準](../STD_03_TraceID.md)に従い、文書リンクを項目の実装・検証リンクの代わりにしない。工程は英字略称、担当未確定はUNASSIGNED。

## Open Questions
未取得資料・残る判断・確認相手・期限を記入する。
