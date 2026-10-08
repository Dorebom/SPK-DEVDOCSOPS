---
schema: spkgw.governance-note/v1
document_id: GOV-TRACE-EXAMPLE-001
project: SPK-GW_HEMS
document_type: REPORT
revision: 1.2.0
status: DRAFT_FOR_REVIEW
title: 文書と項目を分けたTrace記述例
owner: null
document_trace_id: DTR-SPKGW-GOV-000025
item_trace_ids: []
thread_id: THR-SPKGW-GOV-000001
related_thread_ids: []
trace_contract: spkgw.lifecycle-tags/v2
phase_ids: []
phase_scope: UNASSIGNED
activity_type: UNSPECIFIED
created_on: '2026-10-08'
updated_on: '2026-10-08'
classification: INTERNAL
source_baseline: BL-R9-0001
related_ids: []
---

# 文書と項目を分けたTrace記述例

## 1. 説明例であること

本ノートとJSONテンプレートは仮想例。実製品の要求・設計・コード・試験・権限として登録済みとしない。

| 工程 | 文書TraceID例 | 個別項目TraceID例 | 項目の意味 |
|---|---|---|---|
| REQSPEC | DTR-SPKGW-SPEC-900001 | ITR-SPKGW-REQ-900001 | 蓄電池の通常要求の有効期限を定義する要求 |
| ARCH | DTR-SPKGW-SPEC-900002 | ITR-SPKGW-ARCH-900001 | 送信直前の有効期限再検査を担う設計 |
| IMPL | DTR-SPKGW-CODE-900001 | ITR-SPKGW-CODE-900001 | 固定commitにある対象関数の実装 |
| UT | DTR-SPKGW-SPEC-900003 | ITR-SPKGW-UT-900001 | 期限切れ要求を送信しない単体試験ケース |
| UT | DTR-SPKGW-REGISTER-900001 | ITR-SPKGW-RESULT-900001 | 当該ケースを特定ビルド・環境で実行した結果 |

項目はARCH refines REQ、CODE implements ARCH、UT verifies REQ/CODE、RESULT result_of UTのように結ぶ。**同じDTRの全項目へ一括してverifiesを付けない。** 実装側が2つの要求を満たす場合は2辺。別ノートへ同じ要求を移してもITR-REQは不変。

## 2. 会議・調査・原資料

会議録はDTR-MEETING等（文書種別を辞書へ追加して使う）、各議題はITR-AGENDA。規格PDFや既存ExcelはDTR-REFERENCE、参照条項・セル範囲をITR-REFで識別する。会議の議題はdiscussesで要求を参照し、採用判断は別ITR-DEC。本文から理由が分からなければ不明のままOQへ戻す。

## 3. 今回の実データ

[文書索引](../20_work/analysis/project/reports/TRACE_DOCUMENTS.md)と[項目索引](../20_work/analysis/project/reports/TRACE_ITEMS.md)は実在R11資料から移行した一覧。原資料条項や製品コードの全量登録・全工程の根拠鎖完成ではない。

## Open Questions

実担当・実成果・運用環境は[管理OQ](Open_Questions.md)で確定する。製品要求・工程完了の承認ではない。
