---
schema: spkgw.governance-note/v1
document_id: GOV-OQ-001
project: SPK-GW_HEMS
document_type: MOC
revision: 1.3.0
status: DRAFT_FOR_REVIEW
title: ガバナンス導入 Open Questions
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
document_trace_id: DTR-SPKGW-GOV-000003
item_trace_ids:
- ITR-SPKGW-QUESTION-000092
- ITR-SPKGW-QUESTION-000093
- ITR-SPKGW-QUESTION-000094
---

# ガバナンス導入 Open Questions

担当者・期限は未割当。以下は新しい管理詳細の未決であり、製品OQの追加・閉鎖は行っていない。

| ID | 未決 | 必要な回答・完了条件 | 担当候補／確定時点 |
|---|---|---|---|
| OQ-GOV-001 | 担当・権限 | PM、Owner、レビュア、仕様承認、予算・購買承認を誰に割り当てるか。Actorと職務範囲・兼任例外を確定する。 | プロジェクト責任者／該当ルールの実運用開始前 |
| OQ-GOV-002 | 計画・日程 | 既存全作業の母集団、WBS、milestone、期日、見積り、管理作業の扱いは何か。提案ゲートと正式承認の対応を決める。 | プロジェクト責任者／該当ルールの実運用開始前 |
| OQ-GOV-003 | 予算・単価 | 承認総額、費目、通貨、税基準、内部工数単価、AI・共通費配賦、予備費・購買権限を確定する。 | プロジェクト責任者／該当ルールの実運用開始前 |
| OQ-GOV-004 | 締めと是正 | 日次／週次／月次の締め、実績収集の範囲、遅延・超過閾値、エスカレーション先を決める。 | プロジェクト責任者／該当ルールの実運用開始前 |
| OQ-GOV-005 | 実運用環境 | Windows/WSL/Git/共有ストレージでの権限・同時編集・バックアップ・CIを確認する。 | プロジェクト責任者／該当ルールの実運用開始前 |
| OQ-GOV-006 | 過去STDとの正式統合 | 既に配布した別STDがある場合、その実体・版・優先関係を確認する。今回取得できない旧STDの内容を推定しない。 | プロジェクト責任者／該当ルールの実運用開始前 |

4ロールの名称、フォルダ分離、5部44章、原本非改変は再質問しない。実値が決まるまで無制限・全権限・完了済みにしない。各回答は根拠・決定者・日時・対象標準版を残す。

## R11追加：ライフサイクルTraceの具体化
17工程と調査・会議を追う用途は回答済み。以下は実運用に向けた未確定詳細。

| ID | 未決事項 | 完了条件 | 担当・期限 |
|---|---|---|---|
| OQ-GOV-TRACE-01 | 実際の開発テーマの粒度と、既存TASKの17工程対応は何か | 実Traceの目的・scope、旧phaseからの対応、共有成果と派生関係をレビュー | 未割当・運用開始前 |
| OQ-GOV-TRACE-02 | コード／試験／議事の版をどこで保存・固定するか | repo/commit・原票・機密参照の取得方式を決め、未取得を不明として表示 | 未割当・実成果の取り込み前 |
| OQ-GOV-TRACE-03 | 各Trace・工程の必須成果と対象外判断者は誰か | phase_plan、必須kind、受入証拠、N/A根拠、承認範囲を確定 | 未割当・ゲート判定前 |
| OQ-GOV-TRACE-04 | 多テーマ会議・共通基盤の費用配賦をどう行うか | 原票一意、配賦合計1、会議議題と派生TASK、実承認方式を確認 | 未割当・実原価報告前 |

## R12：文書と項目の識別

文書は`document_trace_id`（DTR）、個別項目は`item_trace_id`（ITR）、目的の束ねは任意の`thread_id`（THR）。本文中の旧「Trace」が作業相関を表す場合はTHRを指す。[TraceID標準](STD_03_TraceID.md)に従い、文書リンクを項目の実装・検証リンクの代わりにしない。工程は英字略称、担当未確定はUNASSIGNED。

## R13：AI_STDの選択統合に残る適用確認

<a id="oq-gov-aistd-01"></a>
### OQ-GOV-AISTD-01 — AI入口ファイルの適用環境
問い：どのIDE/クライアント版・実行モード・対象リポジトリで6入口ファイルを利用するか。読み込み、権限、秘密・ネットワークをどう確認するか。
完了条件：[環境確認票](templates/Copilot_Environment_Check.md)へ実測と公式資料の適用版を登録。原資料の製品機能情報を無確認で現行扱いしない。
担当候補：開発環境管理・セキュリティ責任者。担当/期限/判断者：未割当。適用前に確定。状態：OPEN、回答：未記入。

<a id="oq-gov-aistd-02"></a>
### OQ-GOV-AISTD-02 — 委託・脆弱性対応の契約値
問い：委託先ごとの利用権、成果物引渡し、保守範囲、一次/確定回答、修正提供、顧客通知の責任と期限は何か。
完了条件：契約/製品運用と[委託先回答票](templates/Supplier_Response.md)を対応付け、未回答と対象外を識別。規格の期限を推測しない。
担当候補：委託管理・製品運用・セキュリティ担当。実担当/日付：未割当。委託契約・運用採用前に確定。状態：OPEN、回答：未記入。

<a id="oq-gov-aistd-03"></a>
### OQ-GOV-AISTD-03 — 測定・WIP・観測費用の運用値
問い：WIP制限、作業粒度、測定対象と頻度、母集団/比較条件、AI定額費の配賦をどう決めるか。
完了条件：既存進捗・予算正本へのリンクと測定定義を承認し、固定WIP=2や週1件ログを無断採用しない。未観測は未取得と表示。
担当候補：PM・会計/運用・改善担当。実担当/日付：未割当。数値運用・比較報告前に確定。状態：OPEN、回答：未記入。

## Open Questions

上表をこのノートの回答正本とする。全件OPEN、担当・実日付は未確定。
