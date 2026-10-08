---
title: "SPK-GW_HEMS システム仕様書 — 全体MOC"
document_id: "SPKGW-SYS-MOC"
revision: "R9"
updated: 2026-10-08
status: DRAFT_FOR_REVIEW
---

# SPK-GW_HEMS システム仕様書
## R9 — 5部44章・原資料／作業／正本の分離

**ここが現行仕様書の唯一の目次入口。** ユーザーが再掲したPart I〜Vを本MOCの5区分とし、44章の独立Markdownを配下に置いた。旧R7の「5部入口＋旧27章併存」ではない。過去の「R7」呼称だけで正本を選ばず、本MOCの版と入力ハッシュを確認する。

**構成の正本：** 既定の5部構成と今回指定された原資料／作業／正本の分離。**内容の継承元：** R8-FIX001（元ZIPと展開原本を30_referencesに保存）。**技術判断：** 既存の21全体機能群、32GW機能群、4利用者、代表3構成、124 SYS要求、69試験、既存85 OQと管理用6 OQを保持し、未確定の数値・採用・権限・認証は決定していない。

[統合閲覧版](90_All_In_One.md) ／ [仕様完成ガイド](01_Completion_Guide.md) ／ [旧新章対応](appendices/Chapter_Migration_Map.md) ／ [管理補強の確認範囲](../../../00_governance/R9_Change_Log.md)


**R9管理方式：** 本書は10_canonical/CURRENT.jsonが選択する文書BaselineのMOCである。原資料は30_references、分析は20_work/analysis、編集草案は20_work/draftsに分離する。44章の製品内容と既存IDを維持する。管理方式への同意は、未確定の製品要求・機種・権限・USDM理由の承認ではない。

[取り込み・マージ標準](../../../00_governance/STD_Import_Merge.md) ／ [CLI操作ガイド](../../../00_governance/Tool_Operations.md) ／ [管理補強と検証範囲](../../../00_governance/R9_Change_Log.md)

## 本編・別冊・手順書の分担

| 分類 | 正本として扱う内容 |
|---|---|
| 本編I | システム価値・21機能群、4利用者の概要、代表3構成、全体責務・ユースケース・状態 |
| 本編II | GW32機能群、H/G内の実現責務、制御・観測・設定・G側出力制御・更新 |
| 本編III | 境界ごとの両端、情報方向、経路、認可、入出力、異常時契約 |
| 本編IV | 共通品質目標・制約。認証やログ等の実現機能はIIへ対応付ける |
| 本編V | 製造から廃棄、適用規格、変更・適合・検証、要求・OQの管理 |
| 規範別冊候補 | 操作単位権限表、型式別構成表、IF／設定／データ／パラメータ詳細。版・対象・承認を本体と結ぶ |
| 関連手順書・詳細設計 | 操作順・内部実装。本編で未許可の機能・権限・機種対応を新設しない |

## 維持する構成条件

全出力制御サーバ通信は宅内ルータ経由。RS-485 PCSはGW G側が取得・管理・指示し、EL接続PCSはPCS自身がGW非経由で取得する。H側EL Controllerは宅内LAN/APを介してPCS・空調・給湯・計測器へ通常EL通信する。直接無線Webはローカル経路で、出力制御サーバの代替WAN回線ではない。

<a id="part-i"></a>
## Part I　システム全体仕様

**答える問い：** 住宅エネルギーシステム全体として何を実現するか？

| 章 | 主な記載項目 |
|---|---|
| [I-01 文書目的・適用範囲・システム境界](chapters/I_System/I-01_Purpose_Scope.md) | 文書の正本、製品目的、保証境界、対象外、関連文書の優先関係 |
| [I-02 システム利用者・運用概念・利用機能](chapters/I_System/I-02_Actors_Roles.md) | ユーザ／メンテナンス／メーカー／開発者の4分類、利用場面、機能範囲の概要 |
| [I-03 システム全体の機能（要件）一覧](chapters/I_System/I-03_System_Functions.md) | 全体21機能群と、GW・PCS・クラウド・アプリ等への配賦 |
| [I-04 システムコンテキスト・ネットワーク接続](chapters/I_System/I-04_System_Context.md) | 外部サービス、宅内ルータ、GW、両PCS、EL負荷・計測器の全体図と接続拡大図 |
| [I-05 機器構成パターン・機能適用条件](chapters/I_System/I-05_Configurations.md) | 代表3構成、機器分類、能力・版・台数等の構成軸、構成ごとの機能可否 |
| [I-06 システムユースケース・横断振る舞い](chapters/I_System/I-06_Usecases.md) | 正常・代替・異常・同時事象、上位から実機までのエンドツーエンド動作 |
| [I-07 全体責務配分・電力制約・保護](chapters/I_System/I-07_Responsibilities_Constraints.md) | 全体の責任境界、出力制御と保護、連系点・変換グループ・計測範囲 |
| [I-08 システム状態・可用機能・成立条件](chapters/I_System/I-08_System_States.md) | H停止、GW停止、WAN断、ルータ停止等で全体として何を継続・制限するか |

<a id="part-ii"></a>
## Part II　SPK-GW製品仕様

**答える問い：** GW自身が何を実現するか？

| 章 | 主な記載項目 |
|---|---|
| [II-01 GW論理構成・H/G責務・状態所有者](chapters/II_GW/II-01_GW_Architecture.md) | GW内の配賦、状態の正本、固定送信所有者、配置未決事項 |
| [II-02 SPK-GW製品の機能（要件）一覧](chapters/II_GW/II-02_GW_Functions.md) | GW32機能群、全体機能への対応、既存・追加・将来の採否 |
| [II-03 要求受付・通常制御権・実行調整](chapters/II_GW/II-03_Control_Execution.md) | 用途別振分け、Arbiter、Orchestrator、世代・期限・受理と達成 |
| [II-04 DER制御・負荷制御・結果確認](chapters/II_GW/II-04_DER_Load_Control.md) | DER Power Controller、Flexible Load Controller、操作系列と結果の意味 |
| [II-05 高度エネルギーマネジメント](chapters/II_GW/II-05_Advanced_EMS.md) | 採用戦略、計画、実績評価、再計画、入力不足時の縮退 |
| [II-06 機器探索・登録・識別・Capability管理](chapters/II_GW/II-06_Device_Management.md) | 探索・登録・解除・交換、同一機器、多重IF、書込み解禁条件 |
| [II-07 計測・状態・履歴・データ公開機能](chapters/II_GW/II-07_Measurement_Data.md) | Measurement、正規化、観測品質、保存・抽出・同期・状態コピー |
| [II-08 GW G側の出力制御機能](chapters/II_GW/II-08_GW_Grid_Control.md) | RS-485対象の取得・検証・保存・時刻適用・指示・必須監視 |
| [II-09 設定・起動停止・内部機能操作](chapters/II_GW/II-09_Settings_Lifecycle.md) | 設定世代、反映・復元、起動条件、状態別許可、内部Job |
| [II-10 障害検出・縮退復旧・警報診断機能](chapters/II_GW/II-10_Fault_Alarm_Diagnostics.md) | 障害コード、再送・再照合、残留要求、通知・確認・解除 |
| [II-11 FW取得・検証・適用・復旧機能](chapters/II_GW/II-11_Firmware_Update.md) | 配信と適用の分離、H/G更新、更新中断・起動不能からの復旧 |

<a id="part-iii"></a>
## Part III　境界インターフェース仕様

**答える問い：** 境界を越えて何を交換するか？

| 章 | 主な記載項目 |
|---|---|
| [III-01 IF一覧・共通契約・H/G内部境界](chapters/III_Interfaces/III-01_Boundary_Contracts.md) | 既存16IFの配置、方向・責務・schema・時間・認可・互換性と内部境界 |
| [III-02 上位管理・監視サーバ—GWインターフェース](chapters/III_Interfaces/III-02_Cloud_GW.md) | 設定、GW内部操作、情報取得、通常要求配送、オフライン・重複・通知 |
| [III-03 FW配信サーバ—GWインターフェース](chapters/III_Interfaces/III-03_FW_Server.md) | 配布物・メタデータ配送と更新運用要求の区別 |
| [III-04 宅内Web UI—GWインターフェース](chapters/III_Interfaces/III-04_Local_Web.md) | 直接無線とルータ経由、画面資産・Local API、到達性と認可 |
| [III-05 スマートフォンアプリ—クラウド連携](chapters/III_Interfaces/III-05_Remote_App.md) | アプリ—クラウド境界と、クラウド—GW境界を通した監視・操作 |
| [III-06 ECHONET Lite Controller／Deviceインターフェース](chapters/III_Interfaces/III-06_ECHONET_Lite.md) | H側からPCS・空調・給湯・計測器への通常ELと、GWの機器側公開 |
| [III-07 RS-485 PCSインターフェース](chapters/III_Interfaces/III-07_RS485_PCS.md) | 通常指令と必須系統指令、通信所有、プロトコル・応答・状態取得 |
| [III-08 出力制御サーバ—取得クライアントインターフェース](chapters/III_Interfaces/III-08_Utility_Server.md) | GW G側とEL PCS自身の二つの通信終端、すべて宅内ルータ経由 |
| [III-09 ネットワーク・無線・USB等の接続プロファイル](chapters/III_Interfaces/III-09_Network_Peripherals.md) | IPv4/IPv6・Wi-SUN・USB等の持越し要求、適用する物理接続条件 |
| [III-10 製造・施工・保守・開発インターフェース](chapters/III_Interfaces/III-10_Maintenance_Interfaces.md) | 独立G保守、系統構成変更、通常APIと開発経路の区別 |

<a id="part-iv"></a>
## Part IV　横断品質・制約仕様

**答える問い：** どの品質・制約条件で成立させるか？

| 章 | 主な記載項目 |
|---|---|
| [IV-01 性能・時間・精度・容量](chapters/IV_Quality/IV-01_Performance_Capacity.md) | 計画／観測／設定／保護の時間、最大負荷・資源予算・飽和動作 |
| [IV-02 信頼性・可用性・保守性・耐久性](chapters/IV_Quality/IV-02_Reliability_Availability.md) | 許容停止、復旧、データ損失、連続稼働、保守、使用・書込み寿命 |
| [IV-03 セキュリティ・プライバシー](chapters/IV_Quality/IV-03_Security_Privacy.md) | 脅威・資産・対策、認可・鍵ライフサイクル、通信保護、データ消去 |
| [IV-04 製品安全・遠隔操作安全](chapters/IV_Quality/IV-04_Product_Safety.md) | GW・PCS・負荷・利用者の危険源、安全状態、誤操作防止、残留リスク |
| [IV-05 物理・電気・機構・設置条件](chapters/IV_Quality/IV-05_Physical_Electrical.md) | 電源、消費電力、端子・配線、外形、取付、放熱、本体表示 |
| [IV-06 環境・EMC・静電気・輸送保管](chapters/IV_Quality/IV-06_Environment_EMC.md) | 温湿度、屋外、防塵防水、EMC、ESD、サージ、輸送・保管 |
| [IV-07 非干渉・認証影響分離・共有資源制約](chapters/IV_Quality/IV-07_Isolation_Shared_Resources.md) | H/G境界、CPU・時刻・保存・通信・電源・リセット・宅内ルータ |
| [IV-08 データ完全性・ログ・UI品質](chapters/IV_Quality/IV-08_Data_Log_UI_Quality.md) | 保存完全性、監査相関、UIの表示・操作性・対応端末の受入条件 |

<a id="part-v"></a>
## Part V　製品ライフサイクル・適合・検証

**答える問い：** どう成立を確認し、変更・運用するか？

| 章 | 主な記載項目 |
|---|---|
| [V-01 製造・初期書込み・出荷](chapters/V_Lifecycle/V-01_Manufacturing_Shipping.md) | 個体識別、資格情報投入、製造モード閉鎖、出荷検査・校正 |
| [V-02 施工・初期設定・試運転・引渡し](chapters/V_Lifecycle/V-02_Commissioning_Handover.md) | 配線・登録・計測対応、構成有効化、切替中断、利用者引渡し |
| [V-03 運用保守・修理交換・廃棄・サービス終了](chapters/V_Lifecycle/V-03_Maintenance_Retirement.md) | 交換・所有者変更、秘密消去、支援期間、脆弱性対応との接続 |
| [V-04 適用規格・制度・認証構成](chapters/V_Lifecycle/V-04_Compliance.md) | JET／EL・AIF／JC-STAR等の区別、版・条項・適用構成・根拠 |
| [V-05 変更影響・互換性・移行・リリース](chapters/V_Lifecycle/V-05_Change_Migration_Release.md) | 既存維持、Legacy/Next、非干渉評価、変更手続きとリリースの別承認 |
| [V-06 検証・妥当性確認・受入](chapters/V_Lifecycle/V-06_Verification_Validation.md) | 既存69試験、型式・版・数値・測定方法、利用目的の成立確認 |
| [V-07 要求トレース・仕様完成・Open Question管理](chapters/V_Lifecycle/V-07_Trace_Open_Questions.md) | SYS・機能・IF・構成・試験とOQ、未決事項の回答・責任・確定時点 |

## 規範別冊・管理台帳

| 別冊 | 役割 |
|---|---|
| [Functional_Allocation](appendices/Functional_Allocation.md) | 全体機能・GW機能・要求の対応 |
| [Role_Function_Access](appendices/Role_Function_Access.md) | 4ロール×操作の詳細権限案 |
| [Configuration_Patterns](appendices/Configuration_Patterns.md) | 代表型と機種・版・台数の適用条件 |
| [Product_Function_Matrix](appendices/Product_Function_Matrix.md) | 既存製品機能の採否・構成への展開 |
| [Device_Profile_Extended](appendices/Device_Profile_Extended.md) | 機器ごとの能力・通信・認証根拠 |
| [External_Interface_Register](appendices/External_Interface_Register.md) | 既存16論理IFの台帳 |
| [Interface_Contract_Detail](appendices/Interface_Contract_Detail.md) | IFのschema・時間・認可等の具体化 |
| [Grid_Connection_Profile](appendices/Grid_Connection_Profile.md) | 二取得経路と構成binding |
| [Data_Dictionary](appendices/Data_Dictionary.md) | 観測・公開データの実項目 |
| [Configuration_Register](appendices/Configuration_Register.md) | 設定値・既定値・権限・反映 |
| [State_Permission_Matrix](appendices/State_Permission_Matrix.md) | 状態別の操作許可 |
| [UI_Alarm_Register](appendices/UI_Alarm_Register.md) | UI・警報・通知の詳細 |
| [Parameter_Register](appendices/Parameter_Register.md) | 性能・容量・保持等50件の未確定パラメータ |
| [Quality_Acceptance_Profiles](appendices/Quality_Acceptance_Profiles.md) | 品質と利用目的の受入条件 |
| [Normative_References_Glossary](appendices/Normative_References_Glossary.md) | 用語・適用文書と版 |
| [Requirements_Catalog](appendices/Requirements_Catalog.md) | 124システム要求の本文 |
| [Test_Profiles](appendices/Test_Profiles.md) | 69試験計画、実施状態はNOT_RUN |
| [Traceability](appendices/Traceability.md) | 原典ARCHとSYS・試験 |
| [Coverage_Completion_Map](appendices/Coverage_Completion_Map.md) | レビュー34観点と85補完項の対応 |
| [Open_Issues](appendices/Open_Issues.md) | 原典判断と既存48未決事項 |
| [Open_Question_Register](appendices/Open_Question_Register.md) | 85 OQの担当章と残る判断 |
| [Deployment_Binding](appendices/Deployment_Binding.md) | 配置・通信所有の記録 |
| [Release_Impact_Addendum](appendices/Release_Impact_Addendum.md) | 変更影響・リリースの追補 |
| [Northbound_Operation_Catalog](appendices/Northbound_Operation_Catalog.md) | 公開操作候補 |

[原資料台帳](appendices/Source_Register.md)

[マージ判断・出典断片](appendices/Import_Merge_Decisions.md)

[USDM対応](appendices/USDM_Traceability.md)

## 本書の読み方・編集順

全体を把握する際は I-01 → I-04 → I-03 → I-05 → II-02 の順に読む。担当機能を実装・委託する際はIIの該当章とIIIの接続境界を組み合わせ、IVの制約とVの受入・変更条件を参照する。機能可否・ロール認可・実行可否・認証適用は同一の判定にしない。

草案へ複製して章本文・正本JSON・章末OQを編集し、prepareで一式生成・検証する。承認後のみpublishで現行Baselineを切り替える。履歴資料や生成済みコピーを別の回答正本にしない。


<a id="open-questions"></a>
## Open Questions — 本ノートの完成に必要な確認


### 他章で回答する関連質問

| OQ・正本章 | 残る判断 | 完了条件 |
|---|---|---|
| [OQ-R6-01-01](chapters/I_System/I-02_Actors_Roles.md#oq-r6-01-01) | 4分類の名称はユーザ／メンテナンス／メーカー／開発者で確定。権限・委任・対象・環境・承認等は未決。 | ロール×利用局面×操作範囲表を承認し、[旧20章の再配置先](appendices/Chapter_Migration_Map.md#old-ch-20)、[旧26章の再配置先](appendices/Chapter_Migration_Map.md#old-ch-26)、[旧27章の再配置先](appendices/Chapter_Migration_Map.md#old-ch-27)へ対応付ける。 |
| [OQ-R6-04-01](chapters/II_GW/II-02_GW_Functions.md#oq-r6-04-01) | 既存GWの全機能は何か。高度エネマネ追加後に維持・変更・廃止する機能と初回採用機能はどれか。候補ではなく採用済みとできる根拠は何か。 | 機能一覧を既存仕様・コード調査と突合し、候補機能の採否・対象リリース・非対応理由を機能表で承認する。 |
| [OQ-R6-04-02](chapters/I_System/I-05_Configurations.md#oq-r6-04-02) | 初回対応するPCS・空調・給湯・計測器・USB機器はどの型式/版か。全機能対応、観測のみ、非対応をどの組合せで保証するか。 | 機器プロファイルと製品構成表に実型式・版・操作・制限・確認資料を登録する。 |
| [OQ-R6-17-01](chapters/V_Lifecycle/V-06_Verification_Validation.md#oq-r6-17-01) | 既存69試験と追加項目を、どの構成と数値で判定するか。試験以外の確認方法を含め、要求ごとの合否基準と評価責任者は誰か。 | 受入プロファイルを実条件で記入し、各SYS/補完項目→方法→成果物の対応を完成する。実施状態はNOT_RUNと別管理する。 |
| [OQ-R6-19-02](chapters/V_Lifecycle/V-07_Trace_Open_Questions.md#oq-r6-19-02) | 各OQの実担当者、回答期限、提案G0〜G4の採否と正式レビュー日をどう定めるか。未決のまま許される作業と停止する判断はどこか。 | OQへ担当・期限・決定者を記入し、回答→根拠確認→承認→本文/台帳/テスト反映の閉鎖手順を合意する。 |
