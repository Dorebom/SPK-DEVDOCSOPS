---
document_id: T-03
title: 設計ノートテンプレート
version: 1.0.0
status: DRAFT_FOR_ADOPTION
updated: 2026-10-07
---

# T-03 設計ノートテンプレート

本ファイルは [STD-05](../../governance/STD/STD-05_DESIGN.md) のための未記入テンプレートである。
小変更では必要な欄をチケットへ記入すればよい。既存設計で説明されている項目は、版付き参照と今回の差分だけを書く。
`{{...}}` は実値・参照・理由付きの対象外・担当付きの未確定に置き換える。
コピー後のメタデータとリンクは実際の配置先に合わせる。上記 `status` はテンプレートの採用状態であり、設計判断や作業の状態ではない。

## 1. 識別・入力

| 項目 | 記入欄 |
|---|---|
| 設計記録 ID | {{DESIGN_RECORD_ID}} |
| チケット正本 | {{TICKET_REF}} |
| 目的・対象 | {{GOAL_AND_SCOPE}} |
| 要求・受入条件 | {{REQUIREMENT_REF}} |
| 変更影響分析 | {{CHANGE_IMPACT_REF}} |
| 既存設計・コード・基準版 | {{BASE_DESIGN_AND_CODE_REF}} |
| As-Is / To-Be・動作方式 | {{APPLICABLE_CONFIGURATION}} |
| `risk_class` | {{R0_OR_R1_OR_R2}} |
| 作成・更新者／日時 | {{AUTHOR_AND_UPDATED_AT}} |

## 2. 確認した事実と不明点

| 種別 | 内容 | 根拠／確認担当・必要時期 |
|---|---|---|
| 確認済み事実 | {{OBSERVED_FACT}} | {{EVIDENCE_REF}} |
| 仮定・不明点 | {{ASSUMPTION_OR_UNKNOWN}} | {{OWNER_AND_DUE}} |
| 承認済み設計判断 | {{EXISTING_DECISION_OR_NONE}} | {{DECISION_REF}} |

AI が提案した事項を、既存実装の事実や承認済み判断として記入しない。

## 3. 設計差分と責務・配置

- 変更の要点: {{PROPOSED_DESIGN_CHANGE}}
- 維持する条件・契約: {{INVARIANTS_AND_CONSTRAINTS_REF}}
- 適用範囲・対象外: {{APPLICABILITY_AND_EXCLUSIONS}}

| 責務・要素 | レイヤー | モジュール・主要関数 | OS プロセス／実行文脈 | 今回の変更 |
|---|---|---|---|---|
| {{RESPONSIBILITY}} | {{LAYER}} | {{MODULE_REF}} | {{PROCESS_AND_CONTEXT}} | {{CHANGE_OR_UNCHANGED}} |

構成図・シーケンス図が理解に役立つ場合は、ここへ貼付または既存図を参照する: {{DIAGRAM_REF_OR_NOT_NEEDED_REASON}}
レイヤーを OS プロセスと同じものとして描かない。現状の図と提案の図を区別する。

## 4. インターフェース契約

| 項目 | 今回の差分または既存契約への参照 |
|---|---|
| 発生源・受信主体・作用先 | {{ACTORS_AND_ENDPOINTS}} |
| 入出力・単位・範囲・既定値 | {{DATA_CONTRACT_REF}} |
| 受理・完了・実機反映の通知 | {{SUCCESS_SEMANTICS}} |
| エラー・無効値・タイムアウト | {{FAILURE_SEMANTICS}} |
| 再試行・重複・順序逆転 | {{RETRY_AND_ORDERING}} |
| 公開 API・保存形式・互換性 | {{COMPATIBILITY_AND_DECISION_REF}} |

## 5. 状態・競合・異常時

| 現在状態 | 入力・条件 | 判断・動作 | 次状態・有効値 | 確認方法 |
|---|---|---|---|---|
| {{STATE}} | {{EVENT}} | {{ACTION}} | {{NEXT_STATE}} | {{TEST_REF}} |

- 状態・共有データの所有者と更新経路: {{STATE_OWNERSHIP}}
- 制御権・優先度・設定更新の競合: {{ARBITRATION_RULE_REF}}
- 通信断・停止・再起動・復旧後の扱い: {{RECOVERY_RULE_REF}}
- 周期・期限・キュー・資源上限: {{TIMING_RESOURCE_REF_OR_TBD}}
- 対応外機器・認証混在・方式切替への影響: {{VARIANT_IMPACT_OR_NOT_APPLICABLE_REASON}}

## 6. 案の比較と判断

比較が不要な小変更は理由を記載して表を省略してよい。

| 案 | 要求の充足・利点 | 制約・リスク・工数 | 今回の扱い |
|---|---|---|---|
| {{OPTION_A}} | {{BENEFITS}} | {{COSTS_AND_RISKS}} | {{PROPOSED_OR_REJECTED_REASON}} |
| {{OPTION_B_IF_NEEDED}} | {{BENEFITS}} | {{COSTS_AND_RISKS}} | {{PROPOSED_OR_REJECTED_REASON}} |

- 提案または採用済みの案: {{PROPOSED_OR_ADOPTED_OPTION_WITH_STATUS}}
- 選定理由: {{REASON}}
- 既存の作業認可への参照: {{TASK_AUTHORIZATION_REF}}
- R2 の境界変更・必要な専門評価: {{BOUNDARY_CHANGE_AND_REVIEW_OR_NOT_APPLICABLE}}
- 権限を持つ人の設計判断への参照: {{DECISION_REF_OR_NOT_DECIDED}}

設計案の作成、設計判断、実装の受入、リリースの判断はそれぞれ区別する。

## 7. 検証への接続とレビュー記録

| 設計判断・不変条件 | 確認方法・対象環境 | 試験または証拠への参照 |
|---|---|---|
| {{DESIGN_CLAIM}} | {{VERIFICATION_METHOD}} | {{TEST_OR_EVIDENCE_REF}} |

| 指摘 ID | 評価者・観点 | 指摘と根拠 | 対応・残るリスク | 再確認の参照 |
|---|---|---|---|---|
| {{FINDING_ID}} | {{REVIEWER_AND_PERSPECTIVE}} | {{FINDING_AND_EVIDENCE}} | {{DISPOSITION}} | {{RECHECK_REF_OR_NOT_RUN}} |

- 評価の実施形態: {{OTHER_PERSON_OR_SELF_LATER_OR_AI_ASSISTED}}
- 実装中に変更した設計と理由: {{IMPLEMENTATION_DEVIATION_REF_OR_NONE}}
- 未解決点・担当・必要時期: {{OPEN_ITEMS_OR_NONE_WITH_BASIS}}

別時間の自己評価や AI の追加レビューを、実施していない独立審査と記載しない。
