---
document_id: GOV-PROFILE
title: プロジェクト適用設定
version: 1.0.0
status: DRAFT_FOR_ADOPTION
updated: 2026-10-07
---

# PROJECT_PROFILE プロジェクト適用設定

本ファイルはSTDの適用先、正本、権限、運用値を1か所にまとめる。**現在は提案値と未設定値を含み、既存の組織規程・要求・設計・計画を置き換えていない。** 未設定値をAIが事実や承認済みの値として補ってはならない。

## 1. 最初に確定する5項目

1. 適用するリポジトリ・製品版と、採用するSTDの範囲。
2. プロジェクト責任者、技術責任者、受入責任者。兼務可。
3. 要求・設計・チケット・計画・証跡の正本の場所。
4. Copilotへ委任する通常作業と、変更判断が必要な境界。
5. この設定を採用した人、日付、根拠、適用開始。

全項目の完成まで一切の作業を停止する運用にはしない。既存の有効な認可を引き継ぎ、不足が影響する判断だけを保留する。

## 2. 適用範囲と所有者

| キー | 初期値・提案値 | 記入・確認内容 |
| --- | --- | --- |
| project_id | SPK-GW_HEMS | プロジェクト識別 |
| repository | UNSET | URLまたはローカルリポジトリの識別 |
| product_versions | UNSET | 適用する機種・HW・FW/SW版 |
| std_version | 1.0.0 | 本パッケージ版 |
| adoption_status | DRAFT_FOR_ADOPTION | 採用時にADOPTED / PARTIALLY_ADOPTED、停止時にSUSPENDEDと範囲を記録 |
| project_owner | UNSET | 計画、予算、残存リスクの責任者 |
| technical_owner | UNSET | 要求解釈と設計境界の責任者 |
| progress_owner | UNSET | 正本と報告の整合を確認する人 |
| acceptance_owner | UNSET | チケット受入の責任者 |
| release_owner | UNSET | 配布の責任者 |
| security_owner | UNSET | 情報保護、脆弱性対応の責任者 |
| supplier_contact | UNSET | 委託先の技術回答窓口 |

値は役割名のみで済ませず、実運用開始時には担当者または担当グループを特定する。担当者の交代は履歴に残す。

## 3. 正本の選択

`MARKDOWN` は新規導入時の候補であり、既存Issue運用を移す指示ではない。GitHub Issues等を採用済みなら `ISSUE_TRACKER` と実在する場所を記入する。以下のパスは**配置候補**であり、このZIPに製品の実記録が含まれるという意味ではない。

| キー | 初期値・候補 | ルール |
| --- | --- | --- |
| progress_source_of_truth | MARKDOWN | MARKDOWN / ISSUE_TRACKER のどちらか1つ |
| progress_source_location | work/tickets | ISSUE_TRACKER時はプロジェクト・クエリ等を特定 |
| plan_source_location | work/plans | 採用済み計画の正本 |
| report_location | work/reports | 週報等の時点付きスナップショット |
| decision_location | work/decisions | 設計・変更・受入等の判断 |
| evidence_location | work/evidence | アクセス制限を含む実際の保管先 |
| requirements_source | UNSET | 既存の要求・外部仕様・USDMの正本 |
| system_spec_source | UNSET | 既存のシステム仕様の正本 |
| design_source | UNSET | As-Is/To-Be別の採用状態と正本 |
| code_source | UNSET | ソース管理先と対象branch/revision |
| test_source | UNSET | テスト仕様・実装・実機条件の正本 |
| knowledge_source | UNSET | 既存copilot-knowledge等があれば参照を維持 |
| baseline_id | UNSET | 採用済み計画版。ソースcommitと区別 |

Markdown正本の場合、Issue/Projectsは必要に応じて表示・連絡に使う。Issue正本の場合、Markdown週報は作成時点と取得元を持つ参照用スナップショットとする。両方を独立に編集して状態を競合させない。

## 4. Copilotの利用範囲と権限

| キー | 設定案・未確認事項 |
| --- | --- |
| approved_account | UNSET：組織が許可したアカウント |
| approved_plan_and_policy | UNSET：契約・組織ポリシーを確認 |
| client_environment | Windows 11 / VS Codeを想定。WSL利用・実バージョンは未確認 |
| approved_modes_and_models | UNSET：IDE/Local agent/Agent Host/Cloud/Review等の許可範囲 |
| permitted_data | UNSET：入力可能な機密区分、委託先資料の扱い |
| execution_scope | 認可済みチケット内の調査・設計詳細化・実装・検証・ローカル記録を候補とする |
| external_write_scope | UNSET：Issue/PR/外部記録への書込みを認める範囲 |
| protected_operations | 要求・設計原則・計画基準変更、受入、統合・リリース、対外送信の権限を明示 |
| tool_permissions | 現在の組織設定を継承。標準導入だけで変更しない |
| usage_budget | UNSET：費用・回数・時間の運用上限。料金仕様は実契約を確認 |

組織が許可しない情報を渡す前に、その情報を使わずに進められる範囲を切り出す。指示ファイルが読み込まれることと、操作権限を与えることは別である。

## 5. 開発・評価・リリース設定

| キー | 提案値・記入欄 |
| --- | --- |
| branch_strategy | 既存方式を継承。未定なら主ブランチ＋作業ブランチ＋PR |
| review_mode | 1名兼務／複数担当を記入。必要な専門レビューを識別 |
| build_commands | UNSET：公式リポジトリ手順を参照。ダミーコマンドを実行しない |
| test_commands | UNSET：対象版に実在するコマンドを参照 |
| target_matrix | UNSET：HW/FW/通信/出力制御方式/認証有無の組合せ |
| required_ci_checks | UNSET：利用可能なら設定。未構築なら代替記録を定義 |
| release_gate | STD-07/09を基準に必要試験と責任者を確定 |
| evidence_retention | UNSET：期間・保管先・権限・バックアップを出荷判断までに決定 |
| security_response_times | UNSET：深刻度・契約・制度を確認して担当者が決定 |
| certification_scope | UNSET：JC-STAR/JETの適用対象・版・担当・根拠 |

## 6. 進捗管理の初期運用値

下記は運用を開始するための提案値であり、組織の必須値や実績値ではない。

| キー | 提案値 | 運用上の注意 |
| --- | --- | --- |
| work_calendar | 平日を想定した仮設定 | 休日、稼働率、出張、実機利用枠は実カレンダーで確定 |
| wip_limit | 主担当あたり同時2件 | 上限超過時は理由と戻す時期を記録 |
| report_cadence | 作業終了時＋週次＋阻害発生時 | 短い事実更新を基本とする |
| progress_weight | ベースライン時の合意見積重み | 正式集計はACCEPTEDだけを完了とする |
| blocked_escalation | 次回作業を止めると判明した時点で記録・共有 | 定時報告まで重大阻害を隠さない |
| forecast_method | 依存・残作業・稼働予定に基づく幅付き予測 | 不確かな完了日を確約にしない |
| metrics_sample | 週1件程度の代表作業から開始 | AIの生成行数を成果指標にしない |

## 7. SPK-GW_HEMSの設計文脈

以下はユーザーとの議論で示された方向を、参照漏れ防止のために記録したもの。承認済みの詳細設計・実装・実機試験・認証完了を主張しない。実作業では上表に登録した現行正本を優先する。

- Yocto Linux上のC主体の既存製品へHEMS機能を追加する。As-IsとTo-Be、共通仕様と追加仕様を区別する。
- 通常のエネルギー制御と、電力会社の遠隔出力制御・系統保護に関係する責務を混同しない。
- HEMS側の機器制御の名称は **DER Power Controller** とする方向。
- 出力制御は、PCSが取得する方式とGWが取得・管理して指示する方式を製品選択肢として扱う。
- 出力制御サーバとの通信は宅内ルータ経由。GWを介さずPCS自身が要求・応答する対象はECHONET Lite機器のPCSに限る。RS-485接続PCSではGWが担う。
- 一部の機器制御に1秒間隔の要求がある。全ての通信を一律1秒周期と読み替えない。
- 既存機器と認証・暗号対応機器の混在、制御競合、設定更新、通信断、再起動、方式切替を検討する。

参照元はこの会話に提供された2026-10-05〜10-06のプロジェクト文脈。元のリポジトリ・現行仕様書の全内容は今回未取得である。

## 8. 採用記録

| 項目 | 記入欄 |
| --- | --- |
| 適用するSTD・範囲 | UNSET |
| 既存ルールとの差分・整合方法 | UNSET |
| 採用判断者 | UNSET |
| 採用日時・適用開始 | UNSET |
| 判断の根拠・参照 | UNSET |
| 未採用項目・確認担当・期限 | UNSET |

既存の認可記録がある場合は、参照を追記して採用範囲を明確にできる。形式のために過去の有効な判断を取り直す必要はない。

プロジェクトでの採用状態の正本は、この節と `adoption_status` である。各STDの `DRAFT_FOR_ADOPTION` は配布時の状態であり、この設定の有効な採用記録を確認して採用範囲へ適用できる。配布原本の全ヘッダを一括変更しなければ運用開始できない、という意味ではない。STD本文を変更した場合は改訂版と差分を管理する。

## 関連ノート

- [MOC：STD一覧](STD/STD-00_INDEX.md)
- [日常運用ガイド](OPERATION_GUIDE.md)
- [STD-01 ガバナンス](STD/STD-01_GOVERNANCE.md)
