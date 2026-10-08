# SPK-GW_HEMS システム仕様書 R7

2026-10-07／DRAFT_FOR_REVIEW。R6を基準に、5部の入口と二段の機能一覧を追加した。既存27詳細章は改番・移動せず保持する。

[I. システム全体機能21群](parts/I_System_Specification.md) ／ [II. GW機能32群](parts/II_GW_Product_Specification.md) ／ [MOC](00_MOC.md) ／ [統合版](90_All_In_One.md)

## 追加内容

[機能配賦・要求対応](appendices/Functional_Allocation.md)、[4利用者の機能・操作権限](appendices/Role_Function_Access.md)、[3代表構成と適用条件](appendices/Configuration_Patterns.md)、[変更内容](appendices/R7_Change_Summary.md)を追加した。

権限表は13操作群の提案。4利用者名以外の権限を承認したものではない。構成型は責務の代表例であり、実機のサポート認定ではない。機能一覧はR6の既知内容から抽出し、既存実装の全機能調査を完了してはいない。

## 維持条件

全出力制御サーバ通信は宅内ルータ経由。EL接続PCSのみGW非経由で自律取得し、RS-485接続PCSはGW G側が取得・管理・指示する。通常EL接続・上位・Web・アプリ・FW配信とH/G分離を維持する。124 SYS要求・69試験・85 OQを改番・承認・実行しない。

## 編集と検査

[編集・完成ガイド](01_Completion_Guide.md)の正本で編集し、`python tools/rebuild_views.py`、`python tools/validate_package.py --refresh-manifest`、`python tools/validate_package.py`の順で再生成・検査する。文書QAは実機・安全・性能・認証の検証ではない。


## Open Questions — 本ノートの完成に必要な確認

既存OQの正本は `data/completion_items.json`。本一覧は参照で、別の回答正本を作らない。4利用者の確定事項は `data/known_answers_r7.json` を併読する。承認・数値・適合を未確認で補完しない。

| OQ・正本章 | 具体的な質問／未回答部分 | 必要資料・完了条件 |
|---|---|---|
| [OQ-R6-04-01](chapters/04_Configurations_Profiles.md#oq-r6-04-01) | 既存GWの全機能は何か。高度エネマネ追加後に維持・変更・廃止する機能と初回採用機能はどれか。候補ではなく採用済みとできる根拠は何か。 | 機能一覧を既存仕様・コード調査と突合し、候補機能の採否・対象リリース・非対応理由を機能表で承認する。 |
| [OQ-R6-01-01](chapters/01_Scope_Baseline.md#oq-r6-01-01) | 【一部回答済み】4分類の名称は今回確定。権限・委譲・環境等は未決。 初回製品で誰が利用・施工・管理・保守するか。各ロールの操作権限、本人確認、委譲と責任をどこまで分けるか。 | ロール×利用局面×操作範囲表を承認し、第20・26・27章へ対応付ける。 |
| [OQ-R6-04-02](chapters/04_Configurations_Profiles.md#oq-r6-04-02) | 初回対応するPCS・空調・給湯・計測器・USB機器はどの型式/版か。全機能対応、観測のみ、非対応をどの組合せで保証するか。 | 機器プロファイルと製品構成表に実型式・版・操作・制限・確認資料を登録する。 |
