---
schema: spkgw.governance-note/v1
document_id: GOV-TOOL-001
project: SPK-GW_HEMS
document_type: STANDARD
revision: 1.2.0
status: DRAFT_FOR_REVIEW
title: 開発管理ツール操作と適用限界
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
document_trace_id: DTR-SPKGW-GOV-000022
item_trace_ids: []
---

# 開発管理ツール操作と適用限界

## 1. インストールと初期確認
ワークスペース直下で実行する。Python3.11以上。追加依存はPyYAML、jsonschema。R9のspecflow依存は変更せず、追加requirementsを使う。
```powershell
python -m pip install -r .\00_governance\requirements.txt
python .\tools\specflow.py current
python .\tools\specflow.py audit-baseline
python .\tools\specflow.py validate
python .\tools\govcheck.py validate
python .\tools\govcheck.py report
```
初期レポートは導入準備4件のみ。未割当・未見積・PLAN_NOT_APPROVED・BUDGET_NOT_APPROVED・ACTUALS_NOT_CONFIRMEDが表示される。PASSは記入状態と参照の整合であり、計画・予算・作業着手の承認ではない。

## 2. 新しいTASK
```powershell
python .\tools\govcheck.py new-task `
  --title "原資料の対象機種・版・適用範囲を確認する" `
  --trace THR-SPKGW-GOV-000001 `
  --wbs WBS-SPKGW-BOOT
```
UUID由来の新IDを返し、20_work/drafts/project/tasksへPROPOSEDで作成する。TraceとWBSはcontrol.jsonに事前登録する。作業状態の変更コマンド、WBSの自動分解、担当者の自動割当は実装しない。TASKを編集して再検査する。新TASKの作成では既存と同じworkspace lockを用い、ソースの対立を避ける。他の手編集やGitがこのロックを守る保証はない。

## 3. 管理台帳
編集先は20_work/analysis/project/control.json。Actor、Trace、WBS、plan、budget、effort、costs、commitments、forecasts、evidence、runs、decisions、edgesを管理する。項目はschemas/project-control.schema.jsonに従う。
planとbudgetは承認済み入力の写しではなく、本管理台帳の現行参照内容として扱う。正式採用時にはこの内容・承認証拠・hashを10_canonical/management/baselinesへ凍結し、以後の変更は新IDとする。自動凍結／管理Baseline切替は今回の支援ツール範囲外であり、記録レビューで確認する。承認実体・版付き保存を行わずにAPPROVEを自称しない。
実績は原票、Actor、task、証拠へリンクする。費用のreverses_idは元行と同額の取消に限る。部分調整は全額取消＋正しい新原価として記録する。発注額を超える場合は承認済み発注変更を先に反映する。
forecastは各taskにつき現在値1件。過去の見通しは20_work/analysis/project/evidence又は版管理に保存して、最新だけをcurrent集合へ入れる。forecastのETCは未履行発注残を含む。
actuals_complete_throughに締め日を入れる場合は、actuals_confirmationの人Actorと証拠も必要。これは会計システムの照合を自動実行した意味ではない。

## 4. 日付とレポート
```powershell
python .\tools\govcheck.py report --as-of 2026-10-08 `
  --out 20_work/analysis/project/reports/REPORT-20261008-01.json
```
出力先はreports配下だけ。既存ファイルへの上書きを拒否する。単一ファイルは一時ファイル＋置換で保存するが、同時実行や共有ストレージの完全トランザクションを保証しない。reportsを書き込むと配布時のルートManifestは現状態と異なるため、verify_packageは配布ZIPの検証に使う。
--as-ofは台帳全件がその締め日までの現在ビューであることを検査する。後日の実績が混在したまま過去日時を指定すると拒否する。任意時点への自動巻戻し機能ではない。過去報告は当時の入力hash・Git版・保存レポートを使用する。

## 5. 実装した検査
FrontMatter、ID、Actor/Trace/WBS/SYS等の参照、依存循環、READY以降のOwner・実行者・レビュー・見積・着手判断、DONEの受入・証拠hash・残作業、原票重複、単一通貨・税、発注超過、ETC発注残包含、入力時刻を検査する。相互TASK/EXEを検査する。
進捗は承認planのDISCRETE leaf工数ウェイトによる0/100方式。LOEは別件数、summaryの直接費用・実績は拒否。未予算・未締め・残見積欠落ならEAC/VACはnull。recorded_AC=0は「記録済み金額の合計0」であり、原価0の保証ではない。

## 6. 未実装・手動管理
状態変更履歴の完全自動追跡、全STDの機械強制、本人認証・組織権限検証、銀行／会計・購買同期、税計算・為替換算、CPM／資源平準化／自動スケジュール、正式EVM、メール通知、Git／IDE承認ボタン制御、製品機能の実行・認証判断は行わない。TaskのDONEを確認しただけで製品試験PASSとはしない。
R9 specflowの各コマンドにTASK必須のフックは未実装。管理台帳でrun_id/prepared hash/receiptへの関連を記録し、運用レビューで確認する。

## 7. 既存prepareの注意
新規toolsの追加でR9 toolchain_hashが変わる。古い承認候補をpublishせず再prepare・レビュー・承認する。現行BL-R9-0001とCURRENT、受領原本、製品要求の内容は本追加では変えていない。

## R11：工程・活動属性とTrace検査
新規TASKには`--phase CONCEPT`〜`IMPROVE`、`--activity RESEARCH`等を指定できる。`--related-trace`は補助テーマを追加する。作成後の複数phase_idsはCROSS_PHASEとして明記。引数省略はPROPOSED・UNASSIGNEDであり実施工程を推定しない。

```powershell
python .\tools\tracecheck.py validate
python .\tools\tracecheck.py report --trace THR-SPKGW-GOV-000001
```

詳細は[Trace運用ガイド](Tool_Traceability.md)。govcheckはFrontMatter/TASK属性、tracecheckは登録した成果関係、specflowは仕様の正本／生成物を検査する。いずれか1つで全標準の遵守を証明しない。

## R12：文書と項目の識別

文書は`document_trace_id`（DTR）、個別項目は`item_trace_id`（ITR）、目的の束ねは任意の`thread_id`（THR）。本文中の旧「Trace」が作業相関を表す場合はTHRを指す。[TraceID標準](STD_03_TraceID.md)に従い、文書リンクを項目の実装・検証リンクの代わりにしない。工程は英字略称、担当未確定はUNASSIGNED。

## Open Questions

[ガバナンスOQ](Open_Questions.md)を参照。担当・実予算・正式運用条件は未確定。
