---
schema: spkgw.governance-note/v1
document_id: STD-GOV-013
project: SPK-GW_HEMS
document_type: STANDARD
revision: 1.2.0
status: DRAFT_FOR_REVIEW
title: 管理データ検証・移行・例外
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
document_trace_id: DTR-SPKGW-GOV-000020
item_trace_ids: []
---

# 管理データ検証・移行・例外

## 1. 検査を分ける
| 検査 | 対象 | 実行 |
|---|---|---|
| 文書Baseline | 選択snapshot・旧原本・仕様ID・生成鮮度 | 既存specflow audit-baseline / validate |
| FrontMatterと作業管理 | 新規管理ノート・TASK・Actor・Trace・依存・受入 | govcheck validate |
| 予算・進捗 | 工数・通貨・実績・発注残・見込・基準 | govcheck report |
| 製品試験 | コード／実機／安全／性能／認証 | 各TASKと既存試験体系。今回未実施 |
| 運用承認 | 正当な承認者・実会計・内容判断 | 人のレビュー、社内システム。CLIのPASSで代替不可 |
固定件数を編集検査の合否条件にしない。サンプルのID数を増やしても型・参照・計算が正しければ受け入れる。

## 2. ツールが検査すること
FrontMatterの重複キー、必須属性・型・状態、TASKの重複ID・不明Actor/Trace/要求等、自己依存・循環・不明依存、READY以降の前提、DONEの受入証拠、原価原票重複・通貨混在・発注超過・ETC不足、参照パス逸脱・hash不一致、締め日の未来実績を確認する。
実際の人物の本人確認、承認者の所属・委任が正当か、見積りの妥当性、原価の会計照合、仕様の意味や証拠の十分性、法規・認証適合は自動確認しない。適用範囲はTool_Governance.mdを参照する。

## 3. 採用前の最小チェック
既存canonicalと30_referencesを変更していないこと、新旧ID対応、管理標準とTaskテンプレートの整合、同じ数値の複数正本がないこと、未確定が0や許可へ変換されていないこと、影響するpending prepareを無効扱いとして再生成することを確認する。

## 4. 過去タスクの移行
全作業母集団は既存プロジェクト表・会議録・コミット・依頼から棚卸しし、実作業と記録不足を区別する。過去の開始終了・費用・承認を推測で埋めない。過去DONEをimportする場合は証拠を照合し、不明ならIN_REVIEW又は移行保留として分類する。4つの初期PROPOSEDタスクは導入準備であり、実開発全体のWBS棚卸し済みを意味しない。

## 5. 例外・更新
標準変更は自身もCHG/レビュー対象。schemasの互換性を確認する。記録を直すために不正値を検査対象外へ隠さない。規則を段階導入する時は対象ノート範囲、期限、責任者、未適用リスクを公開する。

## 6. R11：Trace専用検査と限界
`tracecheck.py validate`でschema・ID・工程・参照版・原本hash・関係型・指定版・確認記録を検査する。`report --trace`は17工程の適用／記録／不足を表示する。`impact --node`は逆依存の再評価候補であって、自動の変更承認ではない。

既存govcheckとspecflowの検査を置換しない。Trace同一、グラフ連結、LINKED_RECORDSは製品試験PASS・工程承認・安全性の証明ではない。局所変更で省略する工程は根拠付きNOT_APPLICABLE、未決はTBDにする。旧phase対応、実成果の登録、外部リポジトリ検証は人が確認する。

## R12：文書と項目の識別

文書は`document_trace_id`（DTR）、個別項目は`item_trace_id`（ITR）、目的の束ねは任意の`thread_id`（THR）。本文中の旧「Trace」が作業相関を表す場合はTHRを指す。[TraceID標準](STD_03_TraceID.md)に従い、文書リンクを項目の実装・検証リンクの代わりにしない。工程は英字略称、担当未確定はUNASSIGNED。

## Open Questions

担当・実予算・承認閾値・運用環境の未決は [GOV Open Questions](Open_Questions.md) を参照する。本文の運用案は、未確定の製品仕様や支出の承認を代行しない。
