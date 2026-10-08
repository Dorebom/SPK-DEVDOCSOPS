---
title: "機器構成パターン・機能適用条件"
document_id: "SPKGW-SYS-I-05"
revision: "R8"
updated: 2026-10-07
status: DRAFT_FOR_REVIEW
part: "I"
---

<a id="i-05"></a>
# I-05 機器構成パターン・機能適用条件

[全体MOCへ](../../00_MOC.md#part-i)

**本章の対象：** 代表3構成、機器分類、能力・版・台数等の構成軸、構成ごとの機能可否。

**記載区分：** 既存R7の有効な記述とR6補完項を再配置。章構成・読み分けの案以外に、新しい実装・権限・数値・適合を確定していない。旧版に由来する具体値や規格参照は当時の確認範囲を引き継ぐ。

## 本章の責務と他章との境界

本編では責務・経路・故障影響が異なる代表構成を示す。詳細なメーカー・型式・HW/FW・台数・配線・プロパティ・受入証拠は `Configuration_Patterns.md` と `Device_Profile_Extended.md` に置く。

代表は `CFG-RS / CFG-EL / CFG-MIX`。存在する図は対応承認ではない。構成の機能可否と利用者の認可は別の判定であり、一時的WAN断を新しい販売構成として増やさない。PCSなし構成を今回追加採用しない。


## 本編に残す代表構成

| ID | 構成 | 取得・適用主体 | 通常操作経路 | 確認状態 |
|---|---|---|---|---|
| [CFG-RS](../../appendices/Configuration_Patterns.md#cfg-rs) | RS-485接続PCS構成 | GW G側 | GW G側 ⇄ RS-485 ⇄ PCS | 型式・版・台数・適合は未承認 |
| [CFG-EL](../../appendices/Configuration_Patterns.md#cfg-el) | ECHONET Lite接続PCS構成 | 各対象PCSの出力制御機能 | GW H側 EL Controller ⇄ 宅内LAN/AP ⇄ PCS EL機器IF | 型式・版・台数・適合は未承認 |
| [CFG-MIX](../../appendices/Configuration_Patterns.md#cfg-mix) | RS-485＋ECHONET Lite PCS混在構成 | RS-485対象はGW G側、EL対象は当該PCS | RS-485必須指令経路とEL通常操作経路を独立識別 | 型式・版・台数・適合は未承認 |

機器構成で責務・経路・故障影響が変わるものは本編で表示する。機種・FW版・台数・プロパティ差は規範別冊に置き、実際に設置した個体・配線・設定は施工記録へ結び付ける。

**利用可能性の判定案：** 製品・機能の採用、構成Capability、ロール・対象の認可、現在状態・制約・制御権を別に評価する。未搭載／構成非対応／権限不足／一時不可を混同しない。

<a id="legacy-4-1"></a>
## I-05.1 分類軸を分離する

**移行元：** [R7旧4.1節](../../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/04_Configurations_Profiles.md)。

| 軸 | 管理対象 | 他軸から自動決定しない事項 |
|---|---|---|
| 製品・配備 | HW、H/G版、PCS_DIRECT／GW_MANAGED、CPU配置、接続構成 | 認証・動作保証 |
| 通信 | RS-485の接続先／通信仕様、ECHONET Liteクラス・EOJ・版 | 全操作対応、電力会社の対象 |
| Capability | 実際の操作・値域・間隔・結果確認能力 | クラス名だけからの推測 |
| 系統・契約 | 設備範囲、連系点、容量の根拠、制御方式 | 一律の全国ルール |
| 認証構成 | 型式、装置、計測、FW、操作範囲、登録主体 | 任意GWとの組合せ適合 |
| 実行時状態 | 有効設定、接続、健全性、観測鮮度、制御権 | 不在・無効・障害を同じOFFにしない |

<a id="legacy-4-2"></a>
## I-05.2 機器群と責務

**移行元：** [R7旧4.2節](../../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/04_Configurations_Profiles.md)。

PV・蓄電池・EV充放電器等のDER操作はDPC、充電専用EV・給湯・空調等はFlexible Load Controller、メータはMeasurement Serviceを基本とする。燃料電池・CHP・風力・周波数制御等は添付の候補／条件付き拡張をそのまま保持し、初回リリースの必須機能へ昇格しない。

クラスコードの一覧は原文05_Device_Classes.mdを参照する。本書では重複した「最新版クラス表」を別管理しない。RS-485機器にEOJの存在を要求せず、ECHONET Lite機器にRS-485アドレスを要求しない。

<a id="legacy-4-3"></a>
## I-05.3 識別と共有資源

**移行元：** [R7旧4.3節](../../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/04_Configurations_Profiles.md)。

`physical_device_id`、`resource_id`、`conversion_group_id`、`connection_point_id`、通信endpointを別に持つ。同一Hybrid PCSのPV・蓄電池・PCSオブジェクトを三台の独立変換器として管理しない。容量、排他、計測集計は適切なscopeへ結び付ける。

本書での追加案として、通信endpointに`route_id`を設ける。複数経路で見える同一物理機器には、同一性を確認した根拠を保持する。探索結果だけで同一と推定して統合したり、別機器として二重制御したりしない。

<a id="legacy-4-4"></a>
## I-05.4 接続プロファイルの最小内容

**移行元：** [R7旧4.4節](../../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/04_Configurations_Profiles.md)。

| 項目 | 共通 | RS-485固有／ECHONET Lite固有 |
|---|---|---|
| Identity | メーカー・型式・HW/FW・物理／論理資源 | バス・ポート・局番／ノード・EOJ |
| Protocol | 採用文書・版 | PCS通信仕様の名称／Lite・APPENDIX・AIFの実装版 |
| Operation | 意味・単位・符号・許可状態・頻度 | 電文・レジスタ／プロパティと操作系列 |
| Observation | 計測点・品質・時刻・更新間隔 | 取得手順・通知・読み戻し |
| Authority | scope・外部操作元・機器側排他 | 送信所有者と経路共存 |
| Expiry | 受付期限・機器内保持・解除 | 機器側タイムアウト／未対応の別 |
| Grid | 適用対象・強制所有者・通常API非迂回根拠 | route_role、機器内又は外付けの出力制御構成 |
| Certification | 登録主体・構成・適用版・確認記録 | 確認済みの接続組合せ |
| Evaluation | 資料確認・シミュレータ・実機・対応判定 | 未実施をNOT_RUNとする |

<a id="legacy-4-6"></a>
## I-05.5 適用判定と不足情報

**移行元：** [R7旧4.6節](../../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/04_Configurations_Profiles.md)。

`GridApplicability = APPLICABLE / NOT_APPLICABLE / UNKNOWN`を添付どおり保持する。UNKNOWNの内容に応じ、読取専用や確認済みの限定操作へ縮退するが、一律に停止指令を送らない。停止自体が適切かも機器・用途で確認する。

初期接続型式、対応する高度エネマネ戦略、性能値、G側配置、認証登録範囲は未確定。製品構成ごとのサポート表を埋めるまで全組合せ対応を宣言しない。

<a id="legacy-4-7"></a>
## I-05.6 接続・サービス適用プロファイル

**移行元：** [R7旧4.7節](../../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/04_Configurations_Profiles.md)。

LOCAL_DIRECT、LOCAL_ROUTER、REMOTE_CLOUD、FW_DELIVERYを別の適用軸とする。AP／STA同時動作、直接接続方式、クラウド／FWサーバの同一基盤配置、アプリのローカル切替は未確定である。機器プロファイルと同様に、製品HW/FW、Web/API版、クラウドサービス版、アプリ互換、認可、接続開始方向、IPv4／IPv6と公開ポートの有無を対応付ける。

直接無線接続機能の搭載、有効設定、現在接続、インターネット到達、上位同期を別状態として管理する。詳細は[第02章](I-04_System_Context.md#i-04)及び[IF台帳](../../appendices/External_Interface_Register.md)。

<a id="legacy-4-8"></a>
## I-05.7 出力制御接続プロファイル

**移行元：** [R7旧4.8節](../../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/04_Configurations_Profiles.md)。

`grid_connection_mode`はEL接続PCS=PCS_DIRECT、RS-485接続PCS=GW_MANAGEDというR4の対応表で限定する。概念上は異なる属性だが、通信構成と方式の組合せは独立に自由選択できない。G側実配置、GridApplicability、CPU配置、通常HEMS有効設定は別途管理する。未設定はUNCONFIGUREDとして状態管理し、有効な接続方式値に自動変換しない。

設定単位は対象設備・変換グループ・連系点等の制約scopeで定義する案とし、同一scopeのスケジュール適用主体は一つにする。複数scopeの混在も、共通PCS・共通連系点で重複する制約／容量配分を評価したプロファイルに限る。詳細は[方式選択章](I-05_Configurations.md#i-05)。

<a id="legacy-4-9"></a>
## I-05.8 物理機器と多重IFの分類

**移行元：** [R7旧4.9節](../../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/04_Configurations_Profiles.md)。

EL接続PCSだけがGW非経由取得の対象である。単なるELプロパティ検出、GWのDevice側による仮想公開、RS-485機器のEL表現を独立PCS取得とみなさない。両IF機器は物理ID・選択済み接続・scope・取得能力の確認でbindingを決める。R3設定はR4適用表で再評価する。

<a id="legacy-4-10-2"></a>
<a id="slot-r6-04-02"></a>
## I-05.9 機器・ソフトウェア・接続の対応組合せ

**移行元：** [R7旧4.10.2節](../../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/04_Configurations_Profiles.md)。

**補完項目ID：** `SLOT-R6-04-02`。**対応観点：** C04, C10（[レビューA1](../../../../../30_references/baselines/R8_FIX001/sources/review/R5_Coverage_Review_A1.md)）。

R5の既存原則は保持するが、この項の全対象・具体条件・規範参照は未確定。

**本項に記載する仕様項目：**

- メーカー・型式・HW/FW。
- 読み書き能力・台数・必要計測。
- 認証構成と対象外組合せ。

**本項の完成判定：** 機器プロファイルと製品構成表に実型式・版・操作・制限・確認資料を登録する。

**具体的な不足：** [OQ-R6-04-02](I-05_Configurations.md#oq-r6-04-02)。採用値・参照版・対象外理由は回答後に本項又は版指定の規範別冊へ反映する。

<a id="legacy-21-1"></a>
## I-05.10 変更後の適用表

**移行元：** [R7旧21.1節](../../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/21_Grid_Connection_Selection.md)。

**すべての出力制御サーバ通信は宅内ルータ経由。GWを介さない取得要求・応答はECHONET Lite接続PCSだけとする。**

| 本製品で使用する機器・接続構成 | 方式識別子 | 表示名 | スケジュール取得・保存・時刻適用の主体 | サーバ取得経路 |
|---|---|---|---|---|
| ECHONET Lite接続PCS | PCS_DIRECT | PCS自律取得方式（宅内ルータ経由・GW非経由） | PCS内の出力制御機能 | PCS ↔ 宅内ルータ ↔ インターネット ↔ 出力制御サーバ |
| RS-485接続PCS | GW_MANAGED | GW管理方式（宅内ルータ経由・RS-485指示） | GWのG側 | GW G側 ↔ 宅内ルータ ↔ インターネット ↔ 出力制御サーバ |
| その他のEL機器／計測器／仮想オブジェクト | この表からは割当てない | 対象外又は別途評価 | 推測しない | 自律取得を一般化しない |

機器種別・制約責務・通信方式は概念上異なる属性だが、**R4の対応する組合せはこの表で制限する。** RS-485 PCSのPCS_DIRECT、EL接続PCSのGW_MANAGED、ルータを通らない取得を現在の選択肢へ含めない。これはRS-485又はECHONET Lite規格自体の一般的な能力制約を主張するものではない。

R3のPCS_DIRECT識別子は参照互換のため保持する。「直接」は表示から外し、物理的直結の意味を持たせない。識別子保持は無条件の旧設定再利用ではなく、型式・実接続・取得主体をR4の表で再検証する。

同じPCSが複数IFを持つ場合、実際に採用する接続プロファイルで分類する。GWがRS-485 PCSをELオブジェクトとして公開しても、物理PCSをEL自律取得とみなさない。未登録・未確認の機器へ自動的にmodeを割り当てない。

<a id="legacy-21-4"></a>
## I-05.11 選択単位・混在・一意性

**移行元：** [R7旧21.4節](../../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/21_Grid_Connection_Selection.md)。

選択単位は`grid_control_scope_id`で表す設備／変換グループ／連系点等の範囲と、物理PCS・確認済み接続プロファイルのbindingである。R3と異なり、構成確認後も自由な二者択一ではなく21.1の適用表に制約される。

同じ宅内ルータ配下にEL自律取得PCSとRS-485のGW管理PCSが併存することは構成候補として扱える。ただし同一scopeの能動スケジュール適用主体は一つとする。保護機能、機器内の独立制限はこの排他で停止させない。

共通連系点の合算制約を複数PCSで成立させる場合、独立した計測・制約配分・適用所有者が必要かをプロファイルで確認する。ルータが同じことやGWが合計値を監視できることを、全体制約の保証にしない。別scopeへの同じID・容量の重複割当てを防ぐ。

<a id="legacy-21-5"></a>
## I-05.12 設定・経路・状態のモデル

**移行元：** [R7旧21.5節](../../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/21_Grid_Connection_Selection.md)。

| 項目 | R4の扱い |
|---|---|
| normal_connection_class | ECHONET_LITE_PCS／RS485_PCS。物理PCSの採用接続で決定 |
| device_kind／physical_device_id | PCS自身か、非PCS／GW仮想公開かを区別 |
| supported_modes | R4適用表と機器・構成確認で得た許可集合。通常は対応する一方式 |
| desired／configured／active mode | 希望・承認保存・現実の適用を区別。未設定を補完しない |
| display_name | PCS_DIRECTはPCS自律取得方式（宅内ルータ経由・GW非経由） |
| router_profile_id／request_path／response_path | 宅内ルータを含む往復経路。PCS_DIRECTにはGW転送点を含めない |
| server_protocol_profile_id | サーバ通信契約。EL通信プロファイルとは別 |
| schedule_owner／constraint_owner／grid_control_scope_id | 原本・適用責任と最終強制の対応 |
| grid_control_epoch／configuration_revision | 系統構成世代。Arbiter epochとは別 |
| PCS取得能力の確認記録 | 型式・FW・メーカー根拠。ELクラス存在だけでは不可 |
| Job・取得・保持・適用・観測時刻・品質 | 受付／保存／実適用、不明・非公開を区別 |

[二方式テンプレート](../../data/grid_connection_profiles.json)はv2へ改版し、機器接続種別・ルータ必須・往復経路を追加した。両テンプレートはTEMPLATE_NOT_DEPLOYABLE、active_mode=null、確認記録は空欄である。[経路データ](../../data/grid_network_routes.json)も設計モデルであって実測データではない。

<a id="legacy-21-12"></a>
## I-05.13 未確定事項・導入条件

**移行元：** [R7旧21.12節](../../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/21_Grid_Connection_Selection.md)。

R4で確定したのは宅内ルータ必須とGW非経由対象の限定である。型式、PCSの独立取得仕様、ルータ–PCS/GWの媒体・ネットワーク設定、G側実装、異常時数値、両IF機器のbinding、現地変更手順はSYS-TBD-024〜034等で確認する。

「EL接続PCSならすべて標準で自律取得できる」「同一PCSの二方式切替が実装済み」「R4移行時に既設機を自動修正できる」とはしない。R3の旧構成がR4適用外なら、記録と現在の制約維持を確認して認可された保守判断に移し、通常H側更新で稼働中のG構成を書き換えない。

<a id="legacy-21-13-1"></a>
<a id="slot-r6-21-01"></a>
## I-05.14 機種別取得主体・公開状態・実経路

**移行元：** [R7旧21.13.1節](../../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/21_Grid_Connection_Selection.md)。

**補完項目ID：** `SLOT-R6-21-01`。**対応観点：** C04, C10, C17（[レビューA1](../../../../../30_references/baselines/R8_FIX001/sources/review/R5_Coverage_Review_A1.md)）。

R5の既存原則は保持するが、この項の全対象・具体条件・規範参照は未確定。

**本項に記載する仕様項目：**

- EL PCS自律/GW G側管理の型式。
- ルータ・取得プロトコル・資格情報。
- 公開/非公開と可否確認。

**本項の完成判定：** 機器接続別の取得プロファイルと管理主体、公開項目の根拠を登録する。非公開はNOT_EXPOSEDと明記する。

**具体的な不足：** [OQ-R6-21-01](I-05_Configurations.md#oq-r6-21-01)。採用値・参照版・対象外理由は回答後に本項又は版指定の規範別冊へ反映する。


<a id="open-questions"></a>
## Open Questions — 本ノートの完成に必要な確認

以下が本章で回答を管理する質問。関連台帳は参照ビューであり、承認や数値を二重管理しない。

<a id="oq-r6-04-02"></a>
### OQ-R6-04-02 — 機器・ソフトウェア・接続の対応組合せ

**対象項：** [SLOT-R6-04-02](I-05_Configurations.md#slot-r6-04-02)。状態：**OPEN**。

**質問：** 初回対応するPCS・空調・給湯・計測器・USB機器はどの型式/版か。全機能対応、観測のみ、非対応をどの組合せで保証するか。

**必要資料・完了条件：** 機器プロファイルと製品構成表に実型式・版・操作・制限・確認資料を登録する。

**決定担当：** 未割当（候補：機器接続・製品企画）。承認者：未定。

**確定時点：** G1 — 該当する構造・HW・安全・セキュリティ境界の設計固定前（提案）。回答期限：未定。

**未解決時の制約：** 「機器・ソフトウェア・接続の対応組合せ」を対象構成の確定保証・実装受入根拠として使用しない。

**関連する既存ID：** TBD-001, SYS-TBD-024, SYS-TBD-006。

**回答：** 未記入。**決定記録：** 未記入。

<a id="oq-r6-21-01"></a>
### OQ-R6-21-01 — 機種別取得主体・公開状態・実経路

**対象項：** [SLOT-R6-21-01](I-05_Configurations.md#slot-r6-21-01)。状態：**OPEN**。

**質問：** EL接続PCSの自律取得能力・プロトコル・資格情報の管理仕様は何か。RS-485のGW管理と併せて、どの型式/版で実経路・公開状態を確認できるか。

**必要資料・完了条件：** 機器接続別の取得プロファイルと管理主体、公開項目の根拠を登録する。非公開はNOT_EXPOSEDと明記する。

**決定担当：** 未割当（候補：PCSメーカー・G側・ネットワーク設計）。承認者：未定。

**確定時点：** G1 — 該当する構造・HW・安全・セキュリティ境界の設計固定前（提案）。回答期限：未定。

**未解決時の制約：** 「機種別取得主体・公開状態・実経路」を対象構成の確定保証・実装受入根拠として使用しない。

**関連する既存ID：** SYS-TBD-024, SYS-TBD-029, SYS-TBD-033, PAR-GNET-04, PAR-GSEL-06。

**回答：** 未記入。**決定記録：** 未記入。
