---
schema: spkgw.governance-note/v1
document_id: GOV-TOOL-COPILOT-001
project: SPK-GW_HEMS
document_type: REPORT
revision: 1.3.0
status: DRAFT_FOR_REVIEW
title: Copilot入口・プロンプトの条件付き利用
owner: null
document_trace_id: DTR-SPKGW-GOV-000033
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

# Copilot入口・プロンプトの条件付き利用

## 1. 追加したもの
添付の入口ファイルを現在のフォルダ・ID・状態へ翻訳した。使用するAIがこれらの形式を解釈できる環境での補助であり、アクセス制御・実行認可・レビュー承認の代わりではない。

| ファイル | 役割 |
|---|---|
| [.github/copilot-instructions.md](../.github/copilot-instructions.md) | 全体の短い入口、正本と禁止事項 |
| [development.instructions.md](../.github/instructions/development.instructions.md) | 開発ファイルに関する条件付き規則 |
| [governance.instructions.md](../.github/instructions/governance.instructions.md) | 文書・管理記録・原資料の操作境界 |
| [work-start.prompt.md](../.github/prompts/work-start.prompt.md) | 作業開始時の入力・認可・実行計画 |
| [work-review.prompt.md](../.github/prompts/work-review.prompt.md) | 候補版に対するレビュー |
| [progress-update.prompt.md](../.github/prompts/progress-update.prompt.md) | 同一締め時点での進捗・予算報告 |

ファイル形式ごとに必要なメタデータを残す。DTRはsidecarに登録し、GitHub用FrontMatterへ無関係な承認・権限フィールドを挿入しない。

## 2. 利用前に確認すること
[確認票](templates/Copilot_Environment_Check.md)で、製品名・クライアント版・実行モード、共通指示とパス指示の読込み、プロンプトの起動、対象パス、ツール利用権限、sandbox、ネットワーク、機密扱いを実測する。指示全文が自動読込みされる前提を置かず、必要なSTDを明示する。

未対応なら同じ本文を参照資料として使うか、承認された利用方式を選ぶ。UIの承認や組織の制限を自動クリック等で迂回する指示ではない。プロンプトの適用確認ができても、毎回の遵守や製品合格は別である。

## 3. 外部仕様に関する保留
添付REFERENCESの2026-10-07時点のVS Code／GitHub記述は原資料として保存したが、今回外部検証していない。Agent Host、inline suggestions、content exclusion、Copilot approvals等の可否をR13の確定した製品仕様として採用しない。現環境を確認し必要なら当該版の公式資料と証拠を30_referencesへ登録する。

## 4. 管理ツールとの関係
入口は[既存操作](Tool_Governance.md)と[Trace操作](Tool_Traceability.md)を案内する。標準を追記しただけでgovcheckに設計・C品質・人の認可の意味検査が追加されたとはしない。[選択統合検査](AI_STD_Integration.md)も原資料・参照・保存の検査である。

## Open Questions
OQ-GOV-AISTD-01：[管理OQ](Open_Questions.md)。実クライアント、対象リポジトリ、読込み・ツール権限・機密取扱いの実測はNOT_RUN。
