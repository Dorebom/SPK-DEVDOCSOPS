---
schema: spkgw.governance-note/v1
document_id: GOV-CHANGE-001
project: SPK-GW_HEMS
document_type: STANDARD
revision: 1.0.0
status: DRAFT_FOR_REVIEW
title: R10：開発ガバナンス追加・変更記録
owner: null
trace_id: TRC-SPKGW-000001
created_on: '2026-10-08'
updated_on: '2026-10-08'
classification: INTERNAL
source_baseline: BL-R9-0001
related_ids: []
---

# R10：開発ガバナンス追加・変更記録

## 入力と内容
入力はSPK-GW_HEMS_System_Spec_20261008_R9.zip。入力hash・全ファイルhashはR10_Input_Provenance.jsonを参照する。ユーザーの整備要求は30_references/decisions/CTX-R10-GOV.mdへ保存した。前回のR9取り込み・分析・草案・正本の分離を維持する。
STD-GOV-001〜013、FrontMatter・TraceID・TASK/WBS・工程・レビュー・進捗・予算・変更・AI・リリース・報告・検証を追加した。テンプレート、3スキーマ、govcheck支援ツール、初期導入4TASK、管理OQ6件を追加。個別予算、氏名、期日、工数実績、製品の数値・権限は創作しない。

## 非変更範囲
10_canonical/CURRENT.json、BL-R9-0001の全ファイルと採用記録、30_referencesの既存ファイル、既存specflowコード・スキーマ、R9ガバナンス4本文をバイト不変に保持する。既存製品の124要求、69試験、91OQを改訂・承認しない。R10はワークスペース配布版であり、新しい製品仕様Baselineを採用した版ではない。

## 変更対象
ルートREADME.mdとpackage_info.json、ルートManifestは更新する。新規のtools追加により今後のprepareのtoolhashは変わるので、旧pending候補は再prepareする。既存原本zipをもう一段丸ごと入れ子同梱しない。元R9のhash比較表を保持する。

## 実施範囲
今回の追加はSTDと管理支援。実プロジェクト全WBS・実予算の移行、Windows／NAS環境、実会計の接続、製品実機・JET評価は未実施。タスク・費用の例は合成テストに隔離する。

## Open Questions

[ガバナンスOQ](Open_Questions.md)を参照。担当・実予算・正式運用条件は未確定。
