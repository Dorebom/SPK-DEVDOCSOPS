---
schema: spkgw.governance-note/v1
document_id: TPL-GOV-RELEASE
project: SPK-GW_HEMS
document_type: TEMPLATE
revision: 1.3.0
status: TEMPLATE
title: リリース候補・判定・復旧記録
owner: null
document_trace_id: DTR-SPKGW-TEMPLATE-000019
item_trace_ids: []
thread_id: THR-SPKGW-GOV-000001
related_thread_ids: []
trace_contract: spkgw.lifecycle-tags/v2
phase_ids:
- RELPREP
- RELEASE
phase_scope: CROSS_PHASE
activity_type: UNSPECIFIED
created_on: '2026-10-08'
updated_on: '2026-10-08'
classification: INTERNAL
source_baseline: BL-R9-0001
related_ids: []
---

# リリース候補・判定・復旧記録

## 1. 対象と正本参照
| 項目 | 記入 |
|---|---|
| TASK／DTR／ITR／THR | 未記入。登録IDを参照し、原文のIDを削除しない |
| 入力文書版・基準commit・対象機種・FW・接続 | 未記入 |
| 未commit差分・対象外・実行認可 | 未記入 |
| 作成者・確認者・日時 | 未記入。本人・承認を推測しない |

本ファイルは未記入テンプレート。コピー時は新DTR・native ID・実際の配置リンクを設定し、状態を実記録に合わせる。記録が不要な小変更は既存TASK内へ必要項目を記載してよい。費用・TASK state・製品採用状態の第二正本にしない。

## 2. 候補の同一性
候補Baseline、repository/commit、dirty diffとhash、ビルド環境・MACHINE/DISTRO/layer、配布物manifest、依存・ライセンス、対応機種・版・設定・データ：未記入。

## 3. 判定資料
要求と検証EXE/EVD、未実施・既知問題・期限付き例外、回帰差分、役割／安全／認証／契約への影響、説明資料、実判断者とDEC：未記入。

## 4. 導入と復旧
配布・導入対象、機能制限・手順、データ移行・資格失効、旧版に戻せる条件、G側保守の分離、起動確認、失敗時の対応窓口：未記入。

文書Baseline選択、製品のリリース、予算支出、メーカー/JETの変更判断は別承認。テンプレート記入だけで公開しない。

根拠：[リリースSTD](../STD_11_Release_Baselines.md)、原資料T-08。

## Open Questions
未回答の判断・数値・対象版・担当・確定期限を記入する。未記入を承認済み・合格・0に置換しない。[統合方針](../AI_STD_Integration.md)を参照。
