---
schema: spkgw.governance-note/v1
document_id: GOV-VALIDATION-001
project: SPK-GW_HEMS
document_type: STANDARD
revision: 1.3.0
status: DRAFT_FOR_REVIEW
title: STDと自動検査・人の確認の分担
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
document_trace_id: DTR-SPKGW-GOV-000026
item_trace_ids: []
---

# STDと自動検査・人の確認の分担

| 標準の論点 | 自動で確認 | 人・運用で確認 |
|---|---|---|
| FrontMatter | スキーマ、非空、重複キー、日付、型 | 記述の意味、公開区分、過去ノート移行 |
| Trace | 参照先存在、ID一意性、証拠hash | 因果関係の正当性、原文解釈 |
| TASK | 状態必要項目、依存、DONE条件、summary非加算 | 本当に全作業が登録されたか、粒度・受入十分性 |
| Actor・承認 | 登録、HUMAN/AI区分、承認記録の存在 | 本人認証、職務権限、独立性、委任 |
| 進捗 | 基準工数weighted 0/100、未見積、基準外 | 現場の実状、基準計画が正当に承認されたか |
| 費用 | 原票key、decimal、通貨・税、取消、OC、ETC | 原票金額、配賦、会計・検収の実態 |
| 予算 | BAC/AC/ETC/EAC/VAC計算、未締め抑止 | 支出認可、予備費、月次照合、基準凍結 |
| リスク・変更 | ID関連の存在 | 影響・対策・優先・是正判断 |
| AI | 記録フォーマット | 実行権限、原資料利用許可、捏造・意味レビュー |
| 製品安全・認証 | 本ツールでは判定しない | 既存製品試験・メーカー・認証主体 |

自動PASSは上表の限定範囲。導入時の合成回帰はtools/tests/test_governance.py、実施ログは20_work/analysis/project/reportsのGOV_QAを参照する。既存R9回帰も別に実行し、実仕様数値は試験fixtureへ入れない。

## R11追加の検査範囲
| 対象 | 自動検査 | 限界 |
|---|---|---|
| 新TASKの工程・活動 | CONCEPT〜IMPROVE、主工程との整合、関連Trace実在、着手時未割当禁止 | 旧TASKは互換・警告。工程の意味分類は人が確認 |
| 成果node | 一意ID、成果＋版、ローカルpath/hash、明示anchor/JSONポインタ | Git fetch・文書意味の同一性は未自動化 |
| edge | 両端実在、型、主要な端点種別、重複・自己循環、導出循環 | すべての型の意味妥当性・完全な依存網は人が確認 |
| 確認記録 | Actor参照、日時、根拠、対象レコードhash | 本人認証・電子署名・職務権限は未実装 |
| 工程レポート | 17工程適用、必要kind、確認済み根拠との連結、旧版・孤立 | 工程承認・製品試験合格ではない |
| 変更影響 | 型付き依存の逆参照 | 未登録依存・物理影響・認証判断は別評価 |
| 費用 | R10の原票単位集計を維持 | 新しい多Trace配賦計算は未追加 |

## R12：文書と項目の識別

文書は`document_trace_id`（DTR）、個別項目は`item_trace_id`（ITR）、目的の束ねは任意の`thread_id`（THR）。本文中の旧「Trace」が作業相関を表す場合はTHRを指す。[TraceID標準](STD_03_TraceID.md)に従い、文書リンクを項目の実装・検証リンクの代わりにしない。工程は英字略称、担当未確定はUNASSIGNED。

## R13追補：文書統合と実運用の検証範囲
[統合記録](AI_STD_Integration.md)の原資料hash、採用箇所、参照、旧版保存、canonical/既存管理原票の不変、DTR/ITR整合を専用検査する。Cコード安全性、Yoctoビルド、委託先回答の十分性、Copilotクライアント読込み、比較指標の因果性を自動証明しない。既存govcheck/tracecheck/specflowの検査・演算契約は維持。結果はanalysisのR13検証報告へ記録する。

## Open Questions

[ガバナンスOQ](Open_Questions.md)を参照。担当・実予算・正式運用条件は未確定。
