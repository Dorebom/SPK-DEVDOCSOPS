---
schema: spkgw.governance-note/v1
document_id: GOV-MOC-001
project: SPK-GW_HEMS
document_type: MOC
revision: 1.3.0
status: DRAFT_FOR_REVIEW
title: 開発プロセス・進捗・予算管理 MOC
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
document_trace_id: DTR-SPKGW-GOV-000001
item_trace_ids: []
---

# 開発プロセス・進捗・予算管理 MOC

## 1. 読む順序と適用

R9の原資料→分析→草案→正本フローを保持し、開発作業・進捗・予算の管理を追加した。製品文書BaselineはBL-R9-0001を変更せず、管理標準はGOV-1.3.0、ワークスペース配布版はR13。R12のDTR/ITR分離に加え、添付AI_STDの整合する確認観点を選択統合した。ユーザー指定の17工程と調査・会議を、文書DTR・項目ITR・版付き所在と型付き関係で追う。管理ルールの整備は、実予算・担当者・製品要件の承認ではない。

最初は01→02→03→05→04→07→08→Tool_Governanceの順で読む。Trace運用は[操作ガイド](Tool_Traceability.md)と[全工程例](Trace_Lifecycle_Example.md)を併読する。実際の作業はTaskテンプレートを使う。

## 2. 標準一覧

| ID | ノート | 主な契約 |
|---|---|---|
| STD-GOV-001 | [開発ガバナンス・責任・正本境界](STD_01_Authority_Ownership.md) | 本STD群はSPK-GW_HEMSの調査、既存仕様取込み、要求・USDM、外部／システム仕様、設計、実装、単体・結合・実機試験、認証、製造、 |
| STD-GOV-002 | [FrontMatter・ノート属性・編集規則](STD_02_FrontMatter.md) | YAML FrontMatterをファイル先頭に1回だけ置く。UTF-8、LF、キー重複禁止。YAMLの暗黙型を避け、日付・ID・状態・版は |
| STD-GOV-003 | [文書・項目TraceIDと17工程](STD_03_TraceID.md) | DTR・ITR・THR、可読工程、版付き根拠関係 |
| STD-GOV-004 | [全作業タスク・WBS・状態遷移](STD_04_Task_WBS.md) | 調査、会議、要求、USDM、仕様、設計、実装、単体／結合／機能／実機試験、デザインレビュー、独立評価、修正、認証相談、文書取込み、リリース、 |
| STD-GOV-005 | [17開発工程・作業種別・判断ゲート](STD_05_Process_Gates.md) | 17工程、活動種別、判断条件の分離 |
| STD-GOV-006 | [実行・レビュー・証拠・受入の記録](STD_06_Execution_Review_Evidence.md) | 実行ごとにEXE ID、TASK ID、TraceID、Actor、実行役割、開始終了時刻、入力Baseline/commit、対象・環境、 |
| STD-GOV-007 | [進捗・日程・残作業・報告](STD_07_Progress_Schedule.md) | 作業状態（着手・レビュー待ち等）、成果物受入、消費工数／費用を独立管理する。計画期間の経過や予算消化を機能完成率に変換しない。見積がない作業 |
| STD-GOV-008 | [予算・実績原価・発注残・完成時見込](STD_08_Budget_Cost.md) | 人件費、委託費、実機・部品、試験・認証、クラウド・AI利用、ライセンス、旅費等を対象にする。管理会計上の原価と現金支払を別にする。本STDは |
| STD-GOV-009 | [変更・リスク・課題・エスカレーション](STD_09_Change_Risk.md) | 要求、仕様、設計、実装、IF、対応機器、データ、計画、予算、役割・権限の変更をCHGで識別する。旧新差、理由、対象Baseline、影響ID |
| STD-GOV-010 | [人・AIの作業契約と開発支援](STD_10_AI_Collaboration.md) | 人とAIは実行・観測・計画・評価・改善の役割を持てる。作業開始時にTASK、TraceID、現在の役割、入力Baseline、原資料、許可範 |
| STD-GOV-011 | [構成・文書採用・リリース管理](STD_11_Release_Baselines.md) | 製品仕様Baseline（BL）、開発計画（PLN）、予算（BUD）は別ID。相互の適用を参照し、CURRENT.jsonを使うR9の文書公 |
| STD-GOV-012 | [進捗会議・日報週報・意思決定](STD_12_Reports_Decisions.md) | TASKの状態、control.jsonの実績・見通し、承認したPLN/BUDから集計する。報告書のパーセントや合計だけを手で直さない。期間 |
| STD-GOV-013 | [管理データ検証・移行・例外](STD_13_Validation_Migration.md) | 自動検査の範囲、手動判断、移行・例外の扱い |

## 3. 既存R9との接続

[取り込み・マージ標準](STD_Import_Merge.md)、[specflow操作](Tool_Operations.md)、[抽出能力](Extraction_Capability.md)は有効なまま。元4ノートは改変せず、FrontMatterは[legacy登録](legacy_documents.json)で管理する。

[管理ツール操作](Tool_Governance.md) ／ [テンプレート一覧](templates/README.md) ／ [未決事項](Open_Questions.md) ／ [検査範囲](Validation_Coverage.md) ／ [初期タスク](../20_work/drafts/project/tasks/)

## 4. 共通フロー

```text
原資料 30_references
  → analysis：原文抽出・照合・リスク・見積
  → drafts：TASK・仕様候補・計画案
  → EXE・証拠・レビュー → 受入
  → 文書採用(specflow) / 計画・予算承認 / 製品リリースは別判定
  → 10_canonicalへ承認範囲だけ保存
  → 進捗・AC/OC/ETC/EAC・課題を再評価
```

## 5. 実績と移行状態

実Actor、実予算・単価、契約・実績、正式日程は未登録。導入準備4タスクはPROPOSED。OQは[専用台帳](Open_Questions.md)へ集約し、製品OQ91件は変更しない。例・合成試験は実運営に計上しない。

文書・項目の実移行範囲は[索引](../20_work/analysis/project/reports/TRACE_INDEX.md)で確認する。既存TRCはテーマTHRへ対応し、文書・項目へ流用しない。

## 6. 構造定義

[FrontMatter Schema](schemas/frontmatter.schema.json) ／ [Task Schema](schemas/task.schema.json) ／ [管理台帳Schema](schemas/project-control.schema.json) ／ [現行変更記録](R13_Change_Log.md)

## R11のTrace強化
[TraceID標準](STD_03_TraceID.md) ／ [17工程標準](STD_05_Process_Gates.md) ／ [Trace操作](Tool_Traceability.md) ／ [例](Trace_Lifecycle_Example.md) ／ [版付きグラフSchema](schemas/lifecycle-trace.schema.json)。

実Traceはcontrol.jsonの宣言を保持。成果・関係・適用計画はanalysis/project/trace_graph.json。既存4候補TASKを未確認で17工程へ割り当てず、工程TBD・成果未登録を明示する。Traceの記録網羅と製品の進捗・費用・承認を同一視しない。[変更記録](R11_Change_Log.md)を参照。

## R12：文書と項目の識別

文書は`document_trace_id`（DTR）、個別項目は`item_trace_id`（ITR）、目的の束ねは任意の`thread_id`（THR）。本文中の旧「Trace」が作業相関を表す場合はTHRを指す。[TraceID標準](STD_03_TraceID.md)に従い、文書リンクを項目の実装・検証リンクの代わりにしない。工程は英字略称、担当未確定はUNASSIGNED。

## R13：添付AI_STDからの選択統合
R13は管理基盤の追補版（GOV-1.3.0）。[採否・原資料対応](AI_STD_Integration.md)、[変更記録](R13_Change_Log.md)、[プロジェクト索引](PROJECT_PROFILE.md)、[Copilot入口](Tool_Copilot.md)を参照。BL-R9-0001・DTR/ITR/THR・17工程・TASK状態・予算正本は維持する。

| ID | 追加標準 | 使う場面 |
|---|---|---|
| STD-GOV-014 | [要求・仕様・変更影響](STD_14_Requirements_Change_Impact.md) | 目的/変更前後/影響/検証を結ぶ |
| STD-GOV-015 | [設計・判断](STD_15_Design_Decisions.md) | 責務・配置・契約・状態・並行・不変・検証 |
| STD-GOV-016 | [実装・C・Yocto](STD_16_Implementation_C_Yocto.md) | 適用するC実装、再現ビルド、回帰 |
| STD-GOV-017 | [セキュリティ・委託先](STD_17_Security_Supplier.md) | 最小技術回答、脆弱性対応 |
| STD-GOV-018 | [測定・改善](STD_18_AI_Measurement_Improvement.md) | 欠測・比較条件・任意Capabilityログ |

標準の追加は、実予算・実担当・製品数値・正式権限の承認ではない。既存標準に追記した26規則群と、既存形式に合わせたテンプレート/6入口を使用する。添付の作業状態、進捗ウェイト、フォルダ、固定頻度は採用しない。

## Open Questions

担当・実予算・承認閾値・運用環境の未決は [GOV Open Questions](Open_Questions.md) を参照する。本文の運用案は、未確定の製品仕様や支出の承認を代行しない。
