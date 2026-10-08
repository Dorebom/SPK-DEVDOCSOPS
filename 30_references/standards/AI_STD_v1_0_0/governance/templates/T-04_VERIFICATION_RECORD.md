---
document_id: T-04
title: 検証・評価・受入参照テンプレート
version: 1.0.0
status: DRAFT_FOR_ADOPTION
updated: 2026-10-07
---

# T-04 検証・評価・受入参照テンプレート

本ファイルは [STD-07](../../governance/STD/STD-07_VERIFICATION_AND_ACCEPTANCE.md) のための未記入テンプレートである。
既存の試験記録を正本とする場合は、その参照と今回の差分だけ記録する。R0 の小変更は必要欄をチケットへ記入すればよい。
`{{...}}` は実値・参照・理由付きの対象外・担当付きの未確定へ置き換える。未実施・未判断を合格や承認で埋めない。
コピー後のメタデータとリンクは実際の配置先に合わせる。上記 `status` はテンプレートの採用状態であり、検証結果や作業状態ではない。

## 1. 識別・対象

| 項目 | 記入欄 |
|---|---|
| 検証記録 ID | {{VERIFICATION_RECORD_ID}} |
| チケット正本 | {{TICKET_REF}} |
| 要求・受入条件／設計 | {{REQUIREMENT_AND_DESIGN_REF}} |
| `base_revision` | {{BASE_REVISION}} |
| `candidate_revision` | {{CANDIDATE_REVISION_OR_IDENTIFIABLE_DIFF}} |
| 対象製品・ハード・方式 | {{TARGET_CONFIGURATION}} |
| `risk_class` | {{R0_OR_R1_OR_R2}} |
| 確認計画・既存試験仕様 | {{VERIFICATION_PLAN_REF_OR_THIS_RECORD}} |
| 実行・記録者／日時 | {{EXECUTOR_AND_EXECUTED_AT}} |

## 2. 確認環境・適用範囲

| 項目 | 記入欄 |
|---|---|
| ホスト／対象ビルド／模擬／実機等 | {{ENVIRONMENT_TYPE}} |
| OS・ビルド構成・機器版 | {{ENVIRONMENT_ID_OR_REPRODUCTION_REF}} |
| 試験データ・設定・準備条件 | {{TEST_DATA_AND_PRECONDITIONS}} |
| 適用する機器・方式・機能 | {{TESTED_SCOPE}} |
| 対象外とその理由 | {{OUT_OF_SCOPE_AND_REASON}} |
| 実運用との相違・制約 | {{ENVIRONMENT_DIFFERENCES_AND_LIMITATIONS}} |

実機を使用していない場合、そのことを明記する。模擬環境の成立を実機成立へ読み替えない。

## 3. 実行結果

結果は `PASS` / `FAIL` / `NOT_RUN` / `BLOCKED` / `INCONCLUSIVE` のいずれかを用いる。
適用しない確認は、上の対象外欄へ理由を記録し、合格件数に含めない。

| 確認 ID | 要求・受入条件 ID | 方法・コマンド・手順 | 期待結果 | 実際の結果 | 結果 | 証拠参照 |
|---|---|---|---|---|---|---|
| {{CHECK_ID}} | {{REQUIREMENT_OR_AC_ID}} | {{PROCEDURE_OR_REF}} | {{EXPECTED_RESULT}} | {{OBSERVATION_OR_NOT_EXECUTED_REASON}} | {{RESULT}} | {{EVIDENCE_REF}} |

- 結果の要点: {{RESULT_SUMMARY}}
- 基準版との比較が必要な場合の結果: {{BASELINE_COMPARISON_REF_OR_NOT_NEEDED_REASON}}
- 変更後の最終差分と試験対象の一致: {{TARGET_IDENTITY_CHECK}}

自動試験の件数を使う場合は、未実施や対象外を混ぜず、ログで必要な試験の実行を確認する。
細かな実行ログは証拠置場へ保存し、同じログを複数の文書へ貼り付けない。

## 4. 失敗・未実施・判断不能と残る影響

| 確認・課題 ID | 結果／事象 | 理由・影響 | 対応と担当 | 次回確認時点・関連チケット |
|---|---|---|---|---|
| {{CHECK_OR_ISSUE_ID}} | {{RESULT_OR_FINDING}} | {{REASON_AND_IMPACT}} | {{ACTION_AND_OWNER}} | {{DUE_AND_TICKET_REF}} |

- 必須受入条件の未充足: {{UNSATISFIED_CRITERIA_OR_NONE_WITH_BASIS}}
- 今回の変更に起因するか未確定な問題: {{UNRESOLVED_CAUSALITY_OR_NONE}}
- 既存不具合として比較確認した問題: {{EXISTING_DEFECT_EVIDENCE_OR_NONE}}
- チケット側の阻害記録: {{IMPEDIMENT_REF_OR_NONE}}

`BLOCKED` の結果があっても、チケットの作業状態は保存する。阻害は別項目 `impediment=BLOCKED` で管理する。

## 5. 修正後の再確認

再確認が必要な場合だけ記入する。以前の失敗を削除して上書きしない。

| 元の確認 ID・結果 | 修正対象版 | 再確認内容・理由 | 結果 | 証拠参照 |
|---|---|---|---|---|
| {{ORIGINAL_CHECK_AND_RESULT}} | {{FIX_REVISION}} | {{RECHECK_SCOPE_AND_REASON}} | {{RESULT}} | {{EVIDENCE_REF}} |

## 6. 評価記録

| 項目 | 記入欄 |
|---|---|
| 評価者・実施日時 | {{REVIEWER_AND_REVIEWED_AT}} |
| 実施形態 | {{OTHER_PERSON_OR_SELF_LATER_OR_AI_ASSISTED}} |
| 確認した対象・観点 | {{REVIEW_SCOPE_AND_CRITERIA}} |
| 受入条件と証拠の対応 | {{COVERAGE_AND_EVIDENCE_REF}} |
| 指摘・残るリスク | {{FINDINGS_AND_RESIDUAL_RISKS}} |
| 推奨する判断と理由 | {{RECOMMENDATION_AND_REASON}} |
| 必要な専門評価・例外判断 | {{EXPERT_OR_EXCEPTION_REF_OR_NOT_APPLICABLE}} |

AI は評価と推奨を記入できる。自己評価や AI の追加確認を、実施していない独立した人の審査と表現しない。

## 7. 受入判断の正本参照

受入判断は、権限を持つ人の実際の記録を参照する。別に正本がある場合は下表を複写せず、正本リンク一つでよい。
AI による評価・記録作成は受入承認ではない。未判断の場合はそのまま `未判断` とする。

| 項目 | 記入欄 |
|---|---|
| 受入判断の正本 | {{ACCEPTANCE_DECISION_REF_OR_NOT_DECIDED}} |
| 判断の対象版・構成 | {{ACCEPTED_TARGET_OR_NOT_DECIDED}} |
| 権限を持つ人の判断者・日時 | {{HUMAN_DECIDER_AND_TIMESTAMP_OR_NOT_DECIDED}} |
| 実際の判断内容・条件 | {{RECORDED_DECISION_AND_CONDITIONS_OR_NOT_DECIDED}} |
| 例外・残リスクの正式判断 | {{EXCEPTION_REF_OR_NOT_APPLICABLE}} |
| チケットの更新先 | {{TICKET_REF}} |

`ACCEPTED` は人の受入判断を確認してから反映する。受入だけでベースライン変更・リリース・実運用確認を完了扱いにしない。
