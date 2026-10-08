---
description: "標準・計画・チケット・証跡・進捗・Copilot入口を作成または更新する作業に適用する指示"
applyTo: "governance/**,work/**,.github/**"
---

# Governance and work-record instructions

Version: 1.0.0 / 2026-10-07 / DRAFT_FOR_ADOPTION

既存ファイルには差分をマージし、採用時に`applyTo`を実際の標準・作業記録の配置に合わせてください。

- [PROJECT_PROFILE](../../governance/PROJECT_PROFILE.md)、[STD-03](../../governance/STD/STD-03_WORK_CONTROL.md)、[STD-08](../../governance/STD/STD-08_PROGRESS_MANAGEMENT.md)、[STD-09](../../governance/STD/STD-09_CONFIGURATION_AND_RELEASE.md)を読み、選択済みの正本を更新してください。既存管理システムと競合する正本を増やさないでください。
- 事実、推定、提案、実際の採用判断を区別してください。計画の基準値、実績、完了予測を分け、承認済み計画の日付やスコープを実績に合わせて上書きしないでください。
- 作業状態はDRAFT / READY / IN_PROGRESS / IN_REVIEW / CHANGES_REQUESTED / ACCEPTED / CANCELLEDを使い、阻害は別項目impediment=NONE / BLOCKEDで示してください。
- 受入条件と証跡に基づいて状態を更新してください。ACCEPTEDには実際の受入判断の根拠が必要です。テンプレート、AIの推奨、PRの自動表示から人の判断を生成しないでください。
- 試験結果はPASS / FAIL / NOT_RUN / BLOCKED / INCONCLUSIVEを区別してください。試験のBLOCKEDとチケットのimpedimentは別項目として扱ってください。
- ID、対象revision、証跡の参照、判断者、判断時刻を追跡できるようにしてください。既存証跡を上書きして失敗や未実行を隠さないでください。
- 報告では未把握の実績・工数・期限を明示してください。予測値には根拠と不確実性を添え、AIの作業量をそのまま進捗率にしないでください。
- STD、テンプレート、Copilot指示を変更するときは、利用中の作業への影響と版の変更を記録してください。矛盾するルールを追加して現在の承認条件を回避しないでください。
- 認可内の実績記録は更新を進めてください。計画採用・要求変更・例外採用が必要な部分は、具体的な差分と根拠を示してください。
