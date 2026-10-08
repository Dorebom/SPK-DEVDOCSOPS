# SPK-GW_HEMS：作業の入口

このファイルは補助指示であり、実アクセス制御・ツール許可・承認を付与しない。まず[適用プロファイル](../00_governance/PROJECT_PROFILE.md)と[MOC](../00_governance/00_MOC.md)、対象TASKを読み、必要なSTDを明示参照する。

- TASK、作業認可、入力Baseline/commit/dirty diff、許可パス、受入条件を確認する。認可内の通常作業は継続し、境界変更・秘密/外部送信・実機・破壊的操作は正規の判断を得る。
- 10_canonicalの選択済み版と30_references原本を書き換えない。編集は20_work/drafts、抽出・分析・証拠は20_work/analysis。specflowのprepare/承認/publishを使う。
- 文書DTR・項目ITR・任意テーマTHRを区別し、既存native IDと可読工程名を残す。未確認の関係・理由・試験結果を作らない。
- TASK stateはPROPOSED/READY/IN_PROGRESS/BLOCKED/ON_HOLD/IN_REVIEW/DONE/CANCELLED。DONEは受入記録と証拠が必要。原資料のACCEPTED等で上書きしない。
- 対象機種・H/G・通信・最終制約・認証影響を守り、通常APIで保護や出力制御を迂回しない。
- 実施したコマンド・差分・証拠・NOT_RUNと理由・残る判断を報告する。自己評価と独立レビュー、TASK完了とリリースを分ける。

詳細：[AI協働](../00_governance/STD_10_AI_Collaboration.md)、[入口の適用確認](../00_governance/Tool_Copilot.md)。全STDが自動的に読まれるとは扱わない。
