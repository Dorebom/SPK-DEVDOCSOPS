# SPK-GW_HEMS AI・GitHub Copilot協働開発STD

**版：1.0.0／作成日：2026-10-07／状態：DRAFT_FOR_ADOPTION（導入案）**

要求・設計・実装・テスト・レビュー・進捗管理を、GitHub Copilotと人が共同で進めるためのMarkdownノート一式です。Windows 11／VS Code、Yocto Linux／C、既存製品へのHEMS機能追加を想定しています。

標準本文12冊、MOC、適用設定、日常運用ガイド、テンプレート10冊、記入例2冊、Copilot向け入口を収録しています。**日常の通常変更は、作業チケットに必要な記録を集約して運用できます。** 全てのテンプレートを毎回作成する必要はありません。

## 1. 最初に読むノート

1. [日常運用ガイド](governance/OPERATION_GUIDE.md)：日々どう使うか。
2. [PROJECT_PROFILE](governance/PROJECT_PROFILE.md)：適用先、正本、担当者、認可範囲。
3. [STD一覧・MOC](governance/STD/STD-00_INDEX.md)：必要な標準を探す。

通常の作業は [T-01 作業チケット](governance/templates/T-01_WORK_TICKET.md) から開始します。リスクや規模に応じて、差分影響、設計、検証、進捗等のテンプレートを追加します。

## 2. 配置先

ZIPを作業用フォルダへ展開し、内容を確認してから対象リポジトリへ配置してください。製品コード・既存設定は今回変更していません。

| パッケージ内の場所 | リポジトリ内の配置先 | 役割 |
| --- | --- | --- |
| `governance/STD/` | `governance/STD/` | 標準の正本 |
| `governance/PROJECT_PROFILE.md` | 同じ場所 | このプロジェクトへの適用設定 |
| `governance/OPERATION_GUIDE.md` | 同じ場所 | 日常の使い方 |
| `governance/templates/` | 同じ場所 | 未記入ひな形 |
| `governance/examples/` | 同じ場所 | 架空の記入例 |
| `.github/copilot-instructions.md` | `.github/copilot-instructions.md` | Copilotへ読ませる短い入口 |
| `.github/instructions/` | `.github/instructions/` | 対象ファイル別の補助指示 |
| `.github/prompts/` | `.github/prompts/` | 対応環境で手動実行する任意プロンプト |

既存の `governance`、`AGENTS.md`、`.github/copilot-instructions.md` 等がある場合は、**既存ファイルと差分を確認して必要部分を統合**します。ZIPを既存フォルダへ一括上書きしないでください。現在のリポジトリが未提供のため、ファイル名・既存ルールの衝突は導入先で確認する必要があります。

既存配置が `docs/governance/` 等なら、その場所へ合わせて入口・相対リンク・パス別指示の `applyTo` を調整します。実際のチケットや証跡はSTDフォルダに混ぜず、PROJECT_PROFILEで指定した場所へ置きます。

## 3. 導入時の短い手順

1. PROJECT_PROFILEの最初の5項目を記入し、既存の有効な規程・認可・正本を関連付ける。
2. まず通常変更1件へ適用する。主な読み物はSTD-01、03、07、08。
3. Copilot入口を既存設定へ統合し、対象チケットと必要なSTDを明示して開始する。
4. 変更と実際の検証結果を記録し、人の受入判断と分けて進捗へ反映する。
5. 週次に受入済み成果、残作業、阻害、予測を確認し、必要な改善だけ標準へ戻す。

本パッケージの作成依頼は完了しています。業務の責任者・認可対象が未提供のため、採用判断欄は未記入です。既存の有効な依頼・委任で通常作業を続けることは、この設定表を埋めるために取り消されません。

## 4. Copilotへ渡す開始文

以下をチャットへ貼り、`TASK-XXXX` を実在するチケットに置き換えます。利用環境に応じて該当ファイルを添付・参照してください。

```text
governance/PROJECT_PROFILE.md と governance/STD/STD-00_INDEX.md を読み、
対象チケット TASK-XXXX に必要な標準と正本を確認してください。
認可済みの範囲で、影響確認、実装または文書変更、必要な検証、
チケットと進捗正本の更新まで進めてください。
通常の手順選択や修正で同じ認可を取り直す必要はありません。
要求・設計境界・計画基準の変更が必要なら、根拠と代案を具体化してください。
実行していない試験、人が決めていない受入、未更新の外部台帳を完了扱いにせず、
変更内容、実行した確認、残作業、次の行動を報告してください。
```

フォルダを置いただけで全STDが自動読込されるとは仮定しません。短い入口から、実際の作業に必要なファイルを明示して読みます。具体的な対応範囲は [STD-02](governance/STD/STD-02_COPILOT_USAGE.md) を参照してください。

### 任意のプロンプト

| ファイル | 用途 |
| --- | --- |
| [work-start.prompt.md](.github/prompts/work-start.prompt.md) | 認可済み作業の開始と完了までの記録 |
| [work-review.prompt.md](.github/prompts/work-review.prompt.md) | 要求・差分・証跡の評価 |
| [progress-update.prompt.md](.github/prompts/progress-update.prompt.md) | 正本と証跡に基づく進捗更新 |

確認時点のVS Code公式資料では、prompt filesはLocal agentでは利用でき、Agent Hostでは読み込まれません。従って3ファイルは任意の補助です。未対応環境では本文をチャットへ貼り、参照ファイルを明示して使用できます。本文の `../../governance/...` はプロンプトファイルからの相対パスなので、貼付時は `governance/...` 等のリポジトリ基準の指定へ直すか、実ファイルを添付します。[VS-02](https://code.visualstudio.com/docs/agent-customization/prompt-files)

## 5. このSTDで区別すること

- **作業認可**：何をどこまで実施してよいか。
- **検証結果**：何を実際に確認し、何が未実施か。
- **受入判断**：その成果物を受け入れたか。
- **計画変更**：約束した対象・期日・重みを変更するか。
- **リリース判断**：どの製品・版・対象へ配布するか。

R0/R1の通常作業は有効な認可の中で進めます。R2の変更は影響と選択肢を示して該当責任者が判断します。AIは人とともに計画・実行・観測・評価・改善に参加し、判断の根拠をそろえます。

## 6. 適用上の位置付け

この一式は、既存製品の仕様・設計を追加決定したものでも、実装・実機試験・JC-STAR/JET承認の完了記録でもありません。SHIRABEの専用実行プロトコルやJSONランタイムは導入条件にしていません。日々の記録を、将来のSHIRABE/HIBIKI連携や能力評価に利用できる形にしています。

例に含まれる進捗、工数、日付、人物ラベル、チケットの成果は全て架空です。実績台帳へコピーしないでください。

## 7. 参照と確認結果

- [公式情報・作成根拠](governance/REFERENCES.md)
- [パッケージ確認結果](PACKAGE_CHECK.md)
- `MANIFEST_SHA256.txt`：配布ファイルの内容識別用。製品の認証・署名を表すものではありません。

## 版履歴

| 版 | 日付 | 内容 |
| --- | --- | --- |
| 1.0.0 | 2026-10-07 | GitHub Copilot協働開発・進捗管理のSTD一式を新規作成。導入先の正式採用は未記録 |
