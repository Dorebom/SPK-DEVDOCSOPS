---
schema: spkgw.governance-note/v1
document_id: TASK-SPKGW-EXAMPLE
project: SPK-GW_HEMS
document_type: TASK
revision: 1.3.0
status: DRAFT_FOR_REVIEW
title: 作業の具体的な成果を記入
owner: null
created_on: '2026-10-08'
updated_on: '2026-10-08'
classification: INTERNAL
source_baseline: BL-R9-0001
related_ids: []
task_id: TASK-SPKGW-EXAMPLE
state: PROPOSED
kind: DISCRETE
phase: UNASSIGNED
trace_contract: spkgw.lifecycle-tags/v2
phase_ids: []
phase_scope: UNASSIGNED
activity_type: UNSPECIFIED
priority: UNASSIGNED
wbs_id: WBS-SPKGW-BOOT
milestone_id: null
parent_task_id: null
summary: false
depends_on: []
assignees: []
reviewers: []
linked_ids:
- STD-GOV-004
artifacts: []
acceptance_criteria:
- 完了を判断できる条件を記入する
estimate_hours: null
remaining_hours: null
forecast_finish: null
baseline_plan_id: null
approval_refs: []
run_ids: []
evidence_ids: []
acceptance: null
blocker: null
cancellation: null
thread_id: THR-SPKGW-GOV-000001
related_thread_ids: []
document_trace_id: DTR-SPKGW-TEMPLATE-000012
item_trace_ids: []
---

# 作業タスク

## 目的・背景
原資料又は依頼と、何を完了させるか。

## 入力・版・適用条件
Baseline/commit/source_idと対象機器・IF。

## 範囲内／範囲外
許可する変更と、原本・正本・本番・G側等の禁止境界。

## 実施内容
予定と実績を分ける。

## 成果物・完了条件・検証
FrontMatterの条件とEVD/EXE/レビューを対応させる。

## 実績・残作業・差分
費用・工数の正本はcontrol.json。ここへ別の合計を作らない。

## R12：文書と項目の識別

文書は`document_trace_id`（DTR）、個別項目は`item_trace_id`（ITR）、目的の束ねは任意の`thread_id`（THR）。本文中の旧「Trace」が作業相関を表す場合はTHRを指す。[TraceID標準](../STD_03_TraceID.md)に従い、文書リンクを項目の実装・検証リンクの代わりにしない。工程は英字略称、担当未確定はUNASSIGNED。

## R13追補：粒度・認可・引継ぎ
小変更なら本TASKに変更前後・維持条件・影響・検証の必要項目だけを記し、別紙を必須にしない。着手の権限根拠とR0/R1/R2のwork-impact区分を本文で記録する。別FSMやbaseline_weightは追加しない。DONEは受入証拠と残工数の規則による。

引継ぎ：現在state/認可、基準/候補版とdirty diff、変更点/証拠、実施/NOT_RUN、未決・制限、次の1〜3アクション。担当者と承認は推測しない。

## Open Questions
未確定事項と対応OQ、担当・解除条件を記載する。
