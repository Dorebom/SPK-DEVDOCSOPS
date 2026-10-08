---
schema: spkgw.governance-note/v1
document_id: GOV-PROFILE-001
project: SPK-GW_HEMS
document_type: REPORT
revision: 1.3.0
status: DRAFT_FOR_REVIEW
title: 開発ワークスペースの適用・正本参照プロファイル
owner: null
document_trace_id: DTR-SPKGW-GOV-000032
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

# 開発ワークスペースの適用・正本参照プロファイル

## 1. 本書の用途
添付AI_STDのPROJECT_PROFILEを、既存R12の正本を案内する索引として取り込む。製品要求・Actor・予算・進捗の第二の正本にはしない。作業の認可は登録TASKと判断記録から確認し、本書の設置だけで実行範囲を増やさない。

| 対象 | 正本／参照先 | 現在の扱い |
|---|---|---|
| 開発標準 | [全体MOC](00_MOC.md) | GOV-1.3.0、R13の選択統合。未確定値は補完しない |
| 文書Baseline | [CURRENT](../10_canonical/CURRENT.json) | BL-R9-0001を継続。配布R13と製品Baselineの版は別 |
| 文書・項目・テーマ | [Trace標準](STD_03_TraceID.md) | DTR／ITR／THR、既存native IDを維持 |
| 17工程 | [工程標準](STD_05_Process_Gates.md) | REQAN／REQSPEC／ARCH／IMPL／UT等の可読コード |
| TASKの編集正本 | [tasks](../20_work/drafts/project/tasks/) | stateの正本。受入証拠付きDONE。実4候補TASKを今回完了しない |
| Actor・工数・原価・計画・予算 | [control.json](../20_work/analysis/project/control.json) | 実担当・実予算・実績は未登録。原票を複製しない |
| 草案／分析／原資料 | [取り込み標準](STD_Import_Merge.md) | 20_work/drafts／20_work/analysis／30_references |
| 製品構成・4利用者の権限 | 選択BaselineのPart I／規範別冊 | 開発Actorの役割を製品の認可ロールへ自動変換しない |

## 2. 作業開始時に確認する環境
| 確認項目 | 記録先・未確定時の扱い |
|---|---|
| リポジトリ／基準commit／未commit差分 | TASKの入力版、EXEと差分証拠。HEADだけを固定参照にしない |
| ホストOS・IDE・AIモード・利用可能ツール | 実作業の確認記録。原資料のWindows／VS Code記述を実測値にしない |
| 対象製品・Yocto/C・MACHINE/DISTRO・layer版 | 採用した作業・製品構成ごとに確認。未確認なら適用未確認 |
| ビルド／静的解析／テストコマンド | 版付き既存設計・CI・TASKの認可範囲。存在しないコマンドを推測しない |
| 実機／ネットワーク／資格情報 | 使用許可と秘密情報の扱いを確認。資料を持つことと接続許可は別 |
| WIP上限・作業粒度・報告頻度 | [進捗標準](STD_07_Progress_Schedule.md)。初期値を推測しない |
| 単価・予算・支払／税基準 | [予算標準](STD_08_Budget_Cost.md)。本書には値を複製しない |

## 3. 原資料から採用しなかった設定
旧governance／work/ticketsのパス、別チケット状態、別進捗ウェイト、半日〜2日を一律とする粒度、WIP=2、週1件Capabilityログ、半年の実施予定を今回の確定設定にしない。SHIRABE／HIBIKI接続も将来参考であり現行ツールの依存ではない。

## Open Questions
[管理OQ](Open_Questions.md)のOQ-GOV-AISTD-01〜03及び既存担当・予算・環境OQを参照。実リポジトリ・コマンド・取引条件・実行権限は実担当が記入する。
