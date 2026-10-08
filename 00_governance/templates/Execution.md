---
schema: spkgw.governance-note/v1
document_id: EXE-SPKGW-EXAMPLE
project: SPK-GW_HEMS
document_type: TEMPLATE
revision: 1.3.0
status: TEMPLATE
title: 実行記録
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
document_trace_id: DTR-SPKGW-TEMPLATE-000005
item_trace_ids: []
---

# 実行記録

TASK／Trace／Actor／実行役割／開始終了時刻／入力Baseline・commit・hash／環境／ツール・版／コマンド／終了コード／出力／証拠／判定／未実施・残課題を記す。

人の工数とAI待機時間は別。実行ログを見ていない結果をPASSとしない。

## R12：文書と項目の識別

文書は`document_trace_id`（DTR）、個別項目は`item_trace_id`（ITR）、目的の束ねは任意の`thread_id`（THR）。本文中の旧「Trace」が作業相関を表す場合はTHRを指す。[TraceID標準](../STD_03_TraceID.md)に従い、文書リンクを項目の実装・検証リンクの代わりにしない。工程は英字略称、担当未確定はUNASSIGNED。

## R13追補：再現・安全・確認の境界
基準commit・dirty diff、ツール／ホスト／対象環境、実コマンド、終了コード、入力と証拠hashを記録する。ホストビルド、対象ビルド、実機挙動を分ける。NOT_RUNと理由を残し、閾値・skip・warningを変更して成功に見せない。

## Open Questions

未記入欄を実担当・根拠・値で置換する。サンプルは作業・支出・量産操作の認可ではない。
