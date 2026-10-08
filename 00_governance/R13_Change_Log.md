---
schema: spkgw.governance-note/v1
document_id: GOV-CHANGELOG-R13
project: SPK-GW_HEMS
document_type: REPORT
revision: 1.3.0
status: DRAFT_FOR_REVIEW
title: R13：AI_STD選択統合の変更記録
owner: null
document_trace_id: DTR-SPKGW-GOV-000034
item_trace_ids: []
thread_id: THR-SPKGW-GOV-000001
related_thread_ids: []
trace_contract: spkgw.lifecycle-tags/v2
phase_ids:
- IMPROVE
phase_scope: PHASE_SPECIFIC
activity_type: UNSPECIFIED
created_on: '2026-10-08'
updated_on: '2026-10-08'
classification: INTERNAL
source_baseline: BL-R9-0001
related_ids: []
---

# R13：AI_STD選択統合の変更記録

## 1. 入力と優先
ユーザー添付AI_STD v1.0.0から整合する内容を選択し、R12の管理契約へ適合させた。両原本を上書きしない。ユーザー指示は「採用可能な部分だけ適切なファイルに追加」であり、添付の全ルール・製品値・権限の承認ではない。

## 2. 変更
既存STDへの追補、新設STD-GOV-014〜018、6補助テンプレート、既存7テンプレートの記入観点、短い6AI入口、適用プロファイル、採否台帳を追加。DTRの旧版を保存し新revisionを登録、26規則群と出典断片をITRで接続する。

## 3. 維持
選択済み製品Baseline BL-R9-0001、CURRENT、receipts、既存製品要求・試験・OQ、旧原資料、TASK4件、control.json、既存ツール・スキーマ・17工程・Trace命名・計算は変更しない。規則内容の機械的な全強制を新設したとはしない。

## 4. 状態
追加STDのstatusはDRAFT_FOR_REVIEW、空テンプレートはTEMPLATE。技術・管理の確認者は未割当。一般的な指示への同意と、個別レビュー/予算/リリース承認を区別する。詳細は[選択統合記録](AI_STD_Integration.md)、検証実績は[analysisのR13報告](../20_work/analysis/project/reports/AI_STD_R13_QA.md)。

## Open Questions
[管理OQ](Open_Questions.md)へ既存課題を維持し、AIクライアント、委託契約値、測定運用値の3件を追加した。担当/期限/実値は未記入。
