---
schema: spkgw.governance-note/v1
document_id: TPL-GOV-CHANGE-IMPACT
project: SPK-GW_HEMS
document_type: TEMPLATE
revision: 1.3.0
status: TEMPLATE
title: 変更差分・影響分析
owner: null
document_trace_id: DTR-SPKGW-TEMPLATE-000015
item_trace_ids: []
thread_id: THR-SPKGW-GOV-000001
related_thread_ids: []
trace_contract: spkgw.lifecycle-tags/v2
phase_ids:
- REQSPEC
- SYSDES
phase_scope: CROSS_PHASE
activity_type: UNSPECIFIED
created_on: '2026-10-08'
updated_on: '2026-10-08'
classification: INTERNAL
source_baseline: BL-R9-0001
related_ids: []
---

# 変更差分・影響分析

## 1. 対象と正本参照
| 項目 | 記入 |
|---|---|
| TASK／DTR／ITR／THR | 未記入。登録IDを参照し、原文のIDを削除しない |
| 入力文書版・基準commit・対象機種・FW・接続 | 未記入 |
| 未commit差分・対象外・実行認可 | 未記入 |
| 作成者・確認者・日時 | 未記入。本人・承認を推測しない |

本ファイルは未記入テンプレート。コピー時は新DTR・native ID・実際の配置リンクを設定し、状態を実記録に合わせる。記録が不要な小変更は既存TASK内へ必要項目を記載してよい。費用・TASK state・製品採用状態の第二正本にしない。

## 2. 目的と変更前後
問題・理由、発生条件、As-Isの根拠、To-Be案、維持する契約、適用外：未記入。

## 3. 影響の確認
| 観点 | 変更・波及先 | 根拠・未調査 | 受入条件・確認方法 |
|---|---|---|---|
| 公開要求・API・互換 | 未記入 | 未記入 | 未記入 |
| 制御権・設定・状態・並行 | 未記入 | 未記入 | 未記入 |
| 通信・時間・CPU・メモリ・保存 | 未記入 | 未記入 | 未記入 |
| 起動停止・更新復元・残留要求 | 未記入 | 未記入 | 未記入 |
| セキュリティ・安全・認証・委託 | 未記入 | 未記入 | 未記入 |
| 既存回帰・機種・日程・費用 | 未記入 | 未記入 | 未記入 |

影響なしは調査対象と証拠を示す。R0/R1/R2のwork-impact区分と根拠、必要なCHG／判断への参照：未記入。未解決境界変更と既認可内の調査を分ける。

## 4. 反映・受入
実差分との一致、本文・台帳・図・テストの更新先、検証EXE/EVD、残る影響、受入記録：未記入。作業認可・設計判断・DONE・リリースを別にする。

根拠：[要求・変更STD](../STD_14_Requirements_Change_Impact.md)、原資料T-02の意味を現行ID・状態へ変換。

## Open Questions
未回答の判断・数値・対象版・担当・確定期限を記入する。未記入を承認済み・合格・0に置換しない。[統合方針](../AI_STD_Integration.md)を参照。
