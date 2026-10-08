---
document_id: T-02
title: 変更・影響分析テンプレート
version: 1.0.0
status: DRAFT_FOR_ADOPTION
updated: 2026-10-07
---

# T-02 変更・影響分析テンプレート

本ファイルは [STD-04](../../governance/STD/STD-04_REQUIREMENTS_AND_CHANGE.md) を実行するための未記入テンプレートである。
チケット内で同じ項目を満たせる場合は別ファイルを作らず、必要な欄だけコピーする。
`{{...}}` を実値・参照・`未確定: 担当と期限`・`対象外: 理由` のいずれかに置き換える。空欄を「問題なし」と解釈しない。
コピー後のメタデータとリンクは実際の配置先に合わせる。上記 `status` はテンプレートの採用状態であり、作業や判断の状態ではない。

## 1. 識別・参照

| 項目 | 記入欄 |
|---|---|
| 変更記録 ID | {{CHANGE_RECORD_ID}} |
| チケット正本 | {{TICKET_REF}} |
| 要求・受入条件 | {{REQUIREMENT_REF}} |
| 仕様・設計正本 | {{SPEC_DESIGN_REF}} |
| 対象製品・ハード・方式 | {{TARGET_CONFIGURATION}} |
| As-Is / To-Be・既設 / 新規 | {{APPLICABLE_SCOPE}} |
| `base_revision` | {{BASE_REVISION}} |
| `candidate_revision` | {{CANDIDATE_REVISION_OR_NOT_CREATED}} |
| `risk_class` | {{R0_OR_R1_OR_R2}} |
| 調査・更新者／日時 | {{AUTHOR_AND_UPDATED_AT}} |
| `task_authorized_by` / `task_authorization_ref` | {{TICKET_AUTHORITY_REF}} |

作業認可はチケットを参照すればよく、同じ承認記録の複製は不要。

## 2. 目的と変更前後

| 項目 | 記入欄 |
|---|---|
| 問題・要望と目的 | {{PROBLEM_AND_GOAL}} |
| 発生条件・対象 | {{TRIGGER_AND_SCOPE}} |
| 現在の挙動・根拠 | {{BEFORE_BEHAVIOR_AND_EVIDENCE}} |
| 変更後の挙動 | {{AFTER_BEHAVIOR}} |
| 維持する条件・契約 | {{INVARIANTS_AND_CONSTRAINTS_REF}} |
| 今回の対象外 | {{OUT_OF_SCOPE_AND_REASON}} |

## 3. 差分と影響

必要な行を追加する。既存設計・コード・委託先回答へのリンクでよい。
「影響なし」は調査した対象と根拠を記載し、未調査・判断不能と区別する。

| 変更箇所・対象 | 変更内容 | 波及先・利用者 | 影響と根拠／未調査範囲 |
|---|---|---|---|
| {{MODULE_OR_INTERFACE}} | {{CHANGE}} | {{AFFECTED_TARGETS}} | {{IMPACT_AND_EVIDENCE}} |

| 確認観点 | 結論・根拠または不明点 |
|---|---|
| 外部要求・振る舞い・公開 API | {{FINDING_OR_NOT_APPLICABLE_REASON}} |
| 制御権・優先度・設定変更・競合 | {{FINDING_OR_NOT_APPLICABLE_REASON}} |
| 状態・永続データ・停止・再起動 | {{FINDING_OR_NOT_APPLICABLE_REASON}} |
| 通信・時間・資源・プロセス間境界 | {{FINDING_OR_NOT_APPLICABLE_REASON}} |
| 認証認可・秘密情報・更新・依存 | {{FINDING_OR_NOT_APPLICABLE_REASON}} |
| 対象機器・方式・As-Is / To-Be・移行 | {{FINDING_OR_NOT_APPLICABLE_REASON}} |
| 安全・認証・外部契約・委託先 | {{FINDING_OR_NOT_APPLICABLE_REASON}} |
| 既存試験・実機・日程・費用 | {{FINDING_OR_NOT_APPLICABLE_REASON}} |

小変更では上表の関連する行だけ残してよい。削除した観点に本来存在する影響を隠してはならない。

## 4. 受入条件と確認方法

| 要求・条件 ID | 期待結果・判定方法 | 確認環境・対象方式 | 試験・証拠の参照 |
|---|---|---|---|
| {{REQUIREMENT_OR_AC_ID}} | {{EXPECTED_RESULT}} | {{TEST_ENVIRONMENT}} | {{TEST_OR_EVIDENCE_REF}} |

未確定の数値は `TBD: 決定担当と必要時期` とする。
実施結果は [T-04](../../governance/templates/T-04_VERIFICATION_RECORD.md) 相当の記録へリンクし、この表に転記しない。

## 5. リスク・不明点・必要判断

| ID | 事象・不明点 | 影響 | 対応・判断者 | 必要時期／参照 |
|---|---|---|---|---|
| {{RISK_OR_QUESTION_ID}} | {{ISSUE}} | {{IMPACT}} | {{ACTION_AND_OWNER}} | {{DUE_OR_RECORD_REF}} |

- リスク区分の根拠: {{RISK_CLASS_REASON}}
- 既存認可内で進める範囲: {{AUTHORIZED_CONTINUATION}}
- R2 の境界変更がある場合の提案・代替案: {{BOUNDARY_CHANGE_PROPOSAL_OR_NOT_APPLICABLE}}
- 境界判断の正本参照: {{DECISION_REF_OR_NOT_DECIDED}}
- 阻害がある場合: {{TICKET_IMPEDIMENT_REF_OR_NONE}}

R0 / R1 の認可範囲内の実装・確認を進めるために、同じ承認を取り直さない。
R2 の判断待ちでも、認可された調査・提案・分離環境試作は進める。

## 6. 変更後の確認

- 実際の差分と影響分析の一致: {{CHECK_RESULT_AND_REF}}
- 仕様・設計正本の更新先または更新チケット: {{DOC_UPDATE_REF_OR_REASON}}
- 検証記録: {{VERIFICATION_RECORD_REF}}
- 残る影響・未確認: {{RESIDUAL_ITEMS_OR_NONE_WITH_BASIS}}
- 受入判断の正本参照: {{ACCEPTANCE_REF_OR_NOT_DECIDED}}

本記録の作成・更新は受入承認ではない。判断者や判断日時を推測して記入しない。
