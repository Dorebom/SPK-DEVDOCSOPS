---
schema: spkgw.governance-note/v1
document_id: TPL-GOV-AI-CAPABILITY
project: SPK-GW_HEMS
document_type: TEMPLATE
revision: 1.3.0
status: TEMPLATE
title: 人・AIのCapability観測ログ（任意）
owner: null
document_trace_id: DTR-SPKGW-TEMPLATE-000018
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

# 人・AIのCapability観測ログ（任意）

## 1. 対象と正本参照
| 項目 | 記入 |
|---|---|
| TASK／DTR／ITR／THR | 未記入。登録IDを参照し、原文のIDを削除しない |
| 入力文書版・基準commit・対象機種・FW・接続 | 未記入 |
| 未commit差分・対象外・実行認可 | 未記入 |
| 作成者・確認者・日時 | 未記入。本人・承認を推測しない |

本ファイルは未記入テンプレート。コピー時は新DTR・native ID・実際の配置リンクを設定し、状態を実記録に合わせる。記録が不要な小変更は既存TASK内へ必要項目を記載してよい。費用・TASK state・製品採用状態の第二正本にしない。

## 2. Actorと実際の能力提供
| Actor ID・種別 | 仕事・役割・範囲 | 入力と品質 | 出力版・検証・受入参照 |
|---|---|---|---|
| 未記入 | 未記入 | 未記入 | 未記入 |

人の設計・実装・評価を含む。モデル名・ツール版が不明ならUNKNOWN。提出と受入、AI追加レビューと独立審査を区別する。

## 3. 観測と原票
| 指標 | 値・単位 | 実測／申告／推定／未取得 | 原票・対象期間・重複範囲 |
|---|---|---|---|
| 人の初回・評価・修正工数 | 未記入 | 未記入 | control原票参照 |
| AI実行・再試行・待機 | 未記入 | 未記入 | EXE／ログ参照 |
| 承認待ち・依存待ち・手戻り | 未記入 | 未記入 | TASK／イベント参照 |
| 利用費・配賦 | 未記入 | 未記入 | control原票参照 |

経過時間と人時・AI時間を合算して生産性にしない。定額料金から作業別実課金を作らない。週1件を強制しない。全TASKの受入条件にはしない。

## 4. 事実と改善仮説
相対規模・リスク・環境、成功と失敗の観測、欠測、比較条件、再利用できる入力、悪化させたくない指標、次の小さな改善、必要なCHG/DEC：未記入。

根拠：[測定STD](../STD_18_AI_Measurement_Improvement.md)。自動集計ツールは今回未追加。

## Open Questions
未回答の判断・数値・対象版・担当・確定期限を記入する。未記入を承認済み・合格・0に置換しない。[統合方針](../AI_STD_Integration.md)を参照。
