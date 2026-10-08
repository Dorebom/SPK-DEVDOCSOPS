---
schema: spkgw.governance-note/v1
document_id: GOV-CHANGE-R11
project: SPK-GW_HEMS
document_type: REPORT
revision: 1.1.0
status: DRAFT_FOR_REVIEW
title: R11変更記録・17工程Trace
owner: null
trace_id: TRC-SPKGW-000001
created_on: '2026-10-08'
updated_on: '2026-10-08'
classification: INTERNAL
source_baseline: BL-R9-0001
related_ids: []
---

# R11変更記録・17工程Trace

## 1. 対象と根拠
ユーザーの[17工程・関連調査／会議の用途指定](../30_references/decisions/CTX-R11-TRACE.md)を受け、R10のTrace標準・工程分類・関連運用を具体化した。ワークスペース版R11／管理STD版GOV-1.1.0。17工程の名称・内容はユーザー指定、IDコード・型付き関係・チェック方法は今回の実装案。

## 2. 主な変更
STD-GOV-003と005を改訂し、FrontMatter/TASK・証拠・進捗・費用・変更・AI・リリース・会議・検査標準を同期した。会議／調査／Trace計画テンプレート、工程・関係型JSON、版付きグラフSchema、tracecheck.pyを追加。govcheck.pyは17工程属性・関連Traceを理解し、旧TASKを互換読出しする。

## 3. 既存記録の扱い
10_canonicalの全ファイル、製品仕様のCURRENTとBL-R9-0001、R10の4候補TASK、実Actor／工数／予算control.json、specflowコード、R8原本・復元済みmanifestを変更しない。工程適用や実成果を推定登録せず、trace_graphは既存ガバナンスTraceの工程TBDから開始する。

上書きした既存ファイルは[R10変更前スナップショット](../30_references/governance/R10_snapshot/)へバイト保存する。[入力・差分台帳](R11_Input_Provenance.json)で対象を確認できる。旧ZIP全体の入れ子同梱は行わず、元ZIPのSHA-256を記録する。

## 4. 変更の限界
工程別・版別の参照構造と未完表示を実装。実開発全タスクの移行、Git/課題サービス自動同期、承認本人の認証、製品合格、金額配賦、自動Baseline採用は未実装。既存specflowのprepare済み未公開候補はtoolchain hash変更のため再prepare・再承認が必要。

## 5. 検証
[TRACE_QA](../20_work/analysis/project/reports/TRACE_QA.md)と配布検査結果を参照。過去R10のGOV_QAは当時の実施記録として保持し、今回の結果へ書き換えない。

## Open Questions
[管理OQ](Open_Questions.md)のTRACE-01〜04が実運用の未決。実予算・権限・機種・試験結果を今回の管理改版で承認しない。
