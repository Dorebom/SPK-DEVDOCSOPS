---
schema: spkgw.governance-note/v1
document_id: GOV-VALIDATION-001
project: SPK-GW_HEMS
document_type: STANDARD
revision: 1.0.0
status: DRAFT_FOR_REVIEW
title: STDと自動検査・人の確認の分担
owner: null
trace_id: TRC-SPKGW-000001
created_on: '2026-10-08'
updated_on: '2026-10-08'
classification: INTERNAL
source_baseline: BL-R9-0001
related_ids: []
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

## Open Questions

[ガバナンスOQ](Open_Questions.md)を参照。担当・実予算・正式運用条件は未確定。
