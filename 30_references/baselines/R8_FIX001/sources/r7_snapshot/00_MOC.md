# MOC — SPK-GW_HEMS システム仕様書 R7

2026-10-07／DRAFT_FOR_REVIEW。I/IIに二段の機能一覧を追加した。5部の入口から既存27詳細章を読む構成で、全章の物理移動・改番ではない。4利用者名は確定、権限・対応構成の詳細は提案／未確定。

## 5部の入口

| Part | 本編入口 | 主な内容 |
|---|---|---|
| I | [システム全体仕様](parts/I_System_Specification.md) | 全体21機能群 |
| II | [SPK-GW製品仕様](parts/II_GW_Product_Specification.md) | GW32機能群 |
| III | [境界インターフェース仕様](parts/III_Boundary_Interfaces.md) | 境界・品質・ライフサイクルの索引 |
| IV | [横断品質・制約仕様](parts/IV_Quality_Constraints.md) | 境界・品質・ライフサイクルの索引 |
| V | [ライフサイクル・適合・検証](parts/V_Lifecycle_Verification.md) | 境界・品質・ライフサイクルの索引 |

## 今回追加の規範候補別冊

| 別冊 | 内容 |
|---|---|
| [二段機能・既存要求・R6棚卸しの対応](appendices/Functional_Allocation.md) | 二段機能・既存要求・R6棚卸しの対応 |
| [4利用者の機能・操作権限（規範別冊候補）](appendices/Role_Function_Access.md) | 4利用者の機能・操作権限（規範別冊候補） |
| [機器構成パターン・対応条件（規範別冊候補）](appendices/Configuration_Patterns.md) | 機器構成パターン・対応条件（規範別冊候補） |
| [R7変更内容・確認結果・正本の分担](appendices/R7_Change_Summary.md) | R7変更内容・確認結果・正本の分担 |

## 既存詳細章（番号・内容を維持）

| 既存章 | 扱う内容 |
|---|---|
| [01. 文書管理・適用範囲・仕様の確定度](chapters/01_Scope_Baseline.md) | 文書管理・適用範囲・仕様の確定度 |
| [02. 外部サービス・宅内接続を含むシステム構成](chapters/02_System_Context.md) | 外部サービス・宅内接続を含むシステム構成 |
| [03. 責務・レイヤー・状態所有権](chapters/03_Responsibilities.md) | 責務・レイヤー・状態所有権 |
| [04. 製品構成・機器分類・接続プロファイル](chapters/04_Configurations_Profiles.md) | 製品構成・機器分類・接続プロファイル |
| [05. 通常運転要求・制御権・実行結果の契約](chapters/05_Control_Contracts.md) | 通常運転要求・制御権・実行結果の契約 |
| [06. システムユースケース・横断振る舞い](chapters/06_Usecases.md) | システムユースケース・横断振る舞い |
| [07. DER制御・観測と方式別実行仕様](chapters/07_DER_Connections.md) | DER制御・観測と方式別実行仕様 |
| [08. 高度エネマネ・Flexible Load・運転方針](chapters/08_Advanced_EMS_Loads.md) | 高度エネマネ・Flexible Load・運転方針 |
| [09. 計測・状態・保存・外部公開](chapters/09_Measurement_Data.md) | 計測・状態・保存・外部公開 |
| [10. 一般送配電事業者・遠隔出力制御・系統連系保護](chapters/10_Grid_Protection.md) | 一般送配電事業者・遠隔出力制御・系統連系保護 |
| [11. 電力制約・トポロジー・過渡条件](chapters/11_Power_Constraints.md) | 電力制約・トポロジー・過渡条件 |
| [12. 設定管理・運用状態・ライフサイクル](chapters/12_Configuration_Lifecycle.md) | 設定管理・運用状態・ライフサイクル |
| [13. 障害・縮退・復旧・OTA](chapters/13_Fault_Recovery_OTA.md) | 障害・縮退・復旧・OTA |
| [14. 時間・性能・容量・セキュリティ](chapters/14_Performance_Security.md) | 時間・性能・容量・セキュリティ |
| [15. 配置案・認証影響分離境界・共有資源](chapters/15_Deployment_Isolation.md) | 配置案・認証影響分離境界・共有資源 |
| [16. JET・認証構成・変更影響・リリース](chapters/16_Certification_Change.md) | JET・認証構成・変更影響・リリース |
| [17. 要求・試験・受入条件・証跡](chapters/17_Verification.md) | 要求・試験・受入条件・証跡 |
| [18. As-Is・To-Be・差分・段階移行](chapters/18_Migration.md) | As-Is・To-Be・差分・段階移行 |
| [19. 設計判断・未確定事項・出典・レビュー](chapters/19_Open_Issues_Sources.md) | 設計判断・未確定事項・出典・レビュー |
| [20. 上位管理・宅内Web UI・リモートアプリ・FW配信](chapters/20_Northbound_Monitoring_FW.md) | 上位管理・宅内Web UI・リモートアプリ・FW配信 |
| [21. 出力制御接続方式の選択・責務・切替](chapters/21_Grid_Connection_Selection.md) | 出力制御接続方式の選択・責務・切替 |
| [22. 物理・電気・機構・設置仕様](chapters/22_Physical_Electrical_Installation.md) | 物理・電気・機構・設置仕様 |
| [23. 環境・EMC・静電気・輸送保管仕様](chapters/23_Environment_EMC_Transport.md) | 環境・EMC・静電気・輸送保管仕様 |
| [24. 製品安全・危険源・遠隔操作安全](chapters/24_Product_Remote_Safety.md) | 製品安全・危険源・遠隔操作安全 |
| [25. 信頼性・可用性・保守性・耐久性](chapters/25_Reliability_Availability_Maintainability.md) | 信頼性・可用性・保守性・耐久性 |
| [26. 製造・出荷・施工・引渡し・修理・廃棄](chapters/26_Manufacturing_Commissioning_Retirement.md) | 製造・出荷・施工・引渡し・修理・廃棄 |
| [27. セキュリティ・プライバシー・資格情報ライフサイクル](chapters/27_Security_Privacy_Lifecycle.md) | セキュリティ・プライバシー・資格情報ライフサイクル |

## 既存別冊

| 別冊 | 内容 |
|---|---|
| [Change_Summary.md](appendices/Change_Summary.md) | 改訂差分の要約 |
| [Requirements_Catalog.md](appendices/Requirements_Catalog.md) | システム要求124件 |
| [Traceability.md](appendices/Traceability.md) | ARCH・SYS・試験の対応 |
| [Test_Profiles.md](appendices/Test_Profiles.md) | 試験69件と受入条件 |
| [Open_Issues.md](appendices/Open_Issues.md) | 原典判断10件・未確定事項48件 |
| [Parameter_Register.md](appendices/Parameter_Register.md) | 未確定パラメータ50件 |
| [Device_Profile_Extended.md](appendices/Device_Profile_Extended.md) | 機器プロファイル拡張テンプレート |
| [Deployment_Binding.md](appendices/Deployment_Binding.md) | 配置・通信所有の台帳テンプレート |
| [Release_Impact_Addendum.md](appendices/Release_Impact_Addendum.md) | 変更影響評価の追補 |
| [External_Interface_Register.md](appendices/External_Interface_Register.md) | 外部IF・上位契約16件 |
| [Northbound_Operation_Catalog.md](appendices/Northbound_Operation_Catalog.md) | 上位・Web・アプリの操作候補16件 |
| [R2_Review_Checklist.md](appendices/R2_Review_Checklist.md) | R2レビュー入口（履歴） |
| [R3_Decision_Changes.md](appendices/R3_Decision_Changes.md) | R3判断変更（履歴） |
| [Grid_Connection_Profile.md](appendices/Grid_Connection_Profile.md) | R4機器接続別・ルータ経路プロファイル |
| [R3_Review_Checklist.md](appendices/R3_Review_Checklist.md) | R3レビュー入口（履歴） |
| [R4_Decision_Changes.md](appendices/R4_Decision_Changes.md) | R4判断・適用範囲の変更 |
| [R4_Review_Checklist.md](appendices/R4_Review_Checklist.md) | R4レビュー入口 |
| [R5_Diagram_Changes.md](appendices/R5_Diagram_Changes.md) | R5・通常ECHONET Lite接続の明示 |
| [Product_Function_Matrix.md](appendices/Product_Function_Matrix.md) | 製品全機能・構成マトリクス |
| [Normative_References_Glossary.md](appendices/Normative_References_Glossary.md) | 用語集・規範参照の確定台帳 |
| [Interface_Contract_Detail.md](appendices/Interface_Contract_Detail.md) | 外部・内部IF契約の具体化項目 |
| [Data_Dictionary.md](appendices/Data_Dictionary.md) | 計測・状態・履歴データ辞書の具体化項目 |
| [Configuration_Register.md](appendices/Configuration_Register.md) | 設定項目・既定値・反映・復元の一覧項目 |
| [State_Permission_Matrix.md](appendices/State_Permission_Matrix.md) | 状態遷移・起動停止・操作許可の記入項目 |
| [UI_Alarm_Register.md](appendices/UI_Alarm_Register.md) | UI・警報・通知の規範候補台帳 |
| [Quality_Acceptance_Profiles.md](appendices/Quality_Acceptance_Profiles.md) | 品質・利用目的・ライフサイクル受入の具体化項目 |
| [R6_Change_Summary.md](appendices/R6_Change_Summary.md) | R6改訂内容・保持範囲・未確定の扱い |
| [Coverage_Completion_Map.md](appendices/Coverage_Completion_Map.md) | 網羅性34観点とR6章節項・Open Questionの対応 |
| [Open_Question_Register.md](appendices/Open_Question_Register.md) | Open Question横断台帳・既存TBDとの対応 |

[統合版](90_All_In_One.md) ／ [編集・完成ガイド](01_Completion_Guide.md) ／ [文書QA](DOCUMENT_QA.md)


## Open Questions — 本ノートの完成に必要な確認

既存OQの正本は `data/completion_items.json`。本一覧は参照で、別の回答正本を作らない。4利用者の確定事項は `data/known_answers_r7.json` を併読する。承認・数値・適合を未確認で補完しない。

| OQ・正本章 | 具体的な質問／未回答部分 | 必要資料・完了条件 |
|---|---|---|
| [OQ-R6-04-01](chapters/04_Configurations_Profiles.md#oq-r6-04-01) | 既存GWの全機能は何か。高度エネマネ追加後に維持・変更・廃止する機能と初回採用機能はどれか。候補ではなく採用済みとできる根拠は何か。 | 機能一覧を既存仕様・コード調査と突合し、候補機能の採否・対象リリース・非対応理由を機能表で承認する。 |
| [OQ-R6-01-01](chapters/01_Scope_Baseline.md#oq-r6-01-01) | 【一部回答済み】4分類の名称は今回確定。権限・委譲・環境等は未決。 初回製品で誰が利用・施工・管理・保守するか。各ロールの操作権限、本人確認、委譲と責任をどこまで分けるか。 | ロール×利用局面×操作範囲表を承認し、第20・26・27章へ対応付ける。 |
| [OQ-R6-04-02](chapters/04_Configurations_Profiles.md#oq-r6-04-02) | 初回対応するPCS・空調・給湯・計測器・USB機器はどの型式/版か。全機能対応、観測のみ、非対応をどの組合せで保証するか。 | 機器プロファイルと製品構成表に実型式・版・操作・制限・確認資料を登録する。 |
