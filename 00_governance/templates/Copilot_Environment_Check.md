---
schema: spkgw.governance-note/v1
document_id: TPL-GOV-COPILOT-ENV
project: SPK-GW_HEMS
document_type: TEMPLATE
revision: 1.3.0
status: TEMPLATE
title: AI入口ファイルの実環境確認
owner: null
document_trace_id: DTR-SPKGW-TEMPLATE-000020
item_trace_ids: []
thread_id: THR-SPKGW-GOV-000001
related_thread_ids: []
trace_contract: spkgw.lifecycle-tags/v2
phase_ids:
- IMPL
- IMPROVE
phase_scope: CROSS_PHASE
activity_type: UNSPECIFIED
created_on: '2026-10-08'
updated_on: '2026-10-08'
classification: INTERNAL
source_baseline: BL-R9-0001
related_ids: []
---

# AI入口ファイルの実環境確認

## 1. 対象と正本参照
| 項目 | 記入 |
|---|---|
| TASK／DTR／ITR／THR | 未記入。登録IDを参照し、原文のIDを削除しない |
| 入力文書版・基準commit・対象機種・FW・接続 | 未記入 |
| 未commit差分・対象外・実行認可 | 未記入 |
| 作成者・確認者・日時 | 未記入。本人・承認を推測しない |

本ファイルは未記入テンプレート。コピー時は新DTR・native ID・実際の配置リンクを設定し、状態を実記録に合わせる。記録が不要な小変更は既存TASK内へ必要項目を記載してよい。費用・TASK state・製品採用状態の第二正本にしない。

## 2. 確認対象
クライアント製品・版、実行モード、リポジトリcommit、実行者、確認日時、ポリシー・許可ツール：未記入。

| ケース | 方法・期待する挙動 | 実測／証拠／結果 |
|---|---|---|
| 共通指示の適用 | 対象作業で入口・正本を参照できるか | NOT_RUN |
| パス別指示 | 対象／対象外ファイルで適用差を確認 | NOT_RUN |
| プロンプト3種 | 起動・必要ファイル参照・副作用を確認 | NOT_RUN |
| 実アクセス制御 | 原資料・正本・秘密情報・実機への権限を確認 | NOT_RUN |
| ツール承認・隔離・ネットワーク | 指示を超える操作を許可しないこと | NOT_RUN |
| 状態・Trace | DTR/ITR/THR、可読工程、DONE条件を保持 | NOT_RUN |

記載ファイルの存在だけで結果をPASSにしない。確認範囲・限界、未対応時の正規の利用方法：未記入。

根拠：[利用ガイド](../Tool_Copilot.md)。特定バージョンの機能を保証する表ではない。

## Open Questions
未回答の判断・数値・対象版・担当・確定期限を記入する。未記入を承認済み・合格・0に置換しない。[統合方針](../AI_STD_Integration.md)を参照。
