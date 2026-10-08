---
title: "システム全体の機能（要件）一覧"
document_id: "SPKGW-SYS-I-03"
revision: "R8"
updated: 2026-10-07
status: DRAFT_FOR_REVIEW
part: "I"
---

<a id="i-03"></a>
# I-03 システム全体の機能（要件）一覧

[全体MOCへ](../../00_MOC.md#part-i)

**本章の対象：** 全体21機能群と、GW・PCS・クラウド・アプリ等への配賦。

**記載区分：** 既存R7の有効な記述とR6補完項を再配置。章構成・読み分けの案以外に、新しい実装・権限・数値・適合を確定していない。旧版に由来する具体値や規格参照は当時の確認範囲を引き継ぐ。

## 本章の責務と他章との境界

システム全体の機能一覧をこの章へ明示する。GWだけでなくPCS、機器、クラウド、アプリの担当を含む。既存21機能群を一覧化したもので、初回採用・既存全機能棚卸し・正式USDMの確定を意味しない。

同じ一覧をGW仕様へ複製せず、`S-FN-* → GW-FN-*／外部要素` の配賦として扱う。PCS自律取得と系統連系保護を、GWの実装責任へ誤配賦しない。

## システム全体の機能一覧（21機能群）

| ID | 機能・要求の要約 | 実現責任／GW内担当 | 対応する機能 |
|---|---|---|---|
| [S-FN-001](#s-fn-001) | **エネルギー・設備状態の把握**：機器と計測器の状態・電力等を、品質・鮮度とともに把握する。 | 機器・計測器＋GW＋表示先 | [GW-FN-008](../II_GW/II-02_GW_Functions.md#gw-fn-008)、[GW-FN-009](../II_GW/II-02_GW_Functions.md#gw-fn-009)、[GW-FN-012](../II_GW/II-02_GW_Functions.md#gw-fn-012)、[GW-FN-016](../II_GW/II-02_GW_Functions.md#gw-fn-016) |
| [S-FN-002](#s-fn-002) | **宅内モニタリング・操作**：宅内ブラウザから監視し、認可された操作と結果を確認する。 | 端末ブラウザ＋GW＋宅内LAN/AP（直接無線は別経路） | [GW-FN-001](../II_GW/II-02_GW_Functions.md#gw-fn-001)、[GW-FN-018](../II_GW/II-02_GW_Functions.md#gw-fn-018) |
| [S-FN-003](#s-fn-003) | **リモートモニタリング・操作**：スマートフォンアプリからクラウド経由で対象住宅を監視・操作する。 | アプリ＋クラウド＋宅内ルータ＋GW＋対象機器 | [GW-FN-001](../II_GW/II-02_GW_Functions.md#gw-fn-001)、[GW-FN-009](../II_GW/II-02_GW_Functions.md#gw-fn-009)、[GW-FN-017](../II_GW/II-02_GW_Functions.md#gw-fn-017)、[GW-FN-019](../II_GW/II-02_GW_Functions.md#gw-fn-019) |
| [S-FN-004](#s-fn-004) | **PV・蓄電池等の通常運転**：許可されたDER操作を実機へ届け、受理と観測による達成を区別する。 | GW＋PCS／DER | [GW-FN-001](../II_GW/II-02_GW_Functions.md#gw-fn-001)、[GW-FN-002](../II_GW/II-02_GW_Functions.md#gw-fn-002)、[GW-FN-003](../II_GW/II-02_GW_Functions.md#gw-fn-003)、[GW-FN-004](../II_GW/II-02_GW_Functions.md#gw-fn-004)、[GW-FN-010](../II_GW/II-02_GW_Functions.md#gw-fn-010)、[GW-FN-011](../II_GW/II-02_GW_Functions.md#gw-fn-011)、[GW-FN-012](../II_GW/II-02_GW_Functions.md#gw-fn-012) |
| [S-FN-005](#s-fn-005) | **空調・給湯等の負荷操作**：快適性・機器安全を尊重して、採用された負荷操作を実行する。 | GW＋空調・給湯等 | [GW-FN-001](../II_GW/II-02_GW_Functions.md#gw-fn-001)、[GW-FN-002](../II_GW/II-02_GW_Functions.md#gw-fn-002)、[GW-FN-003](../II_GW/II-02_GW_Functions.md#gw-fn-003)、[GW-FN-005](../II_GW/II-02_GW_Functions.md#gw-fn-005)、[GW-FN-010](../II_GW/II-02_GW_Functions.md#gw-fn-010)、[GW-FN-012](../II_GW/II-02_GW_Functions.md#gw-fn-012) |
| [S-FN-006](#s-fn-006) | **高度エネマネ運転計画**：自家消費・料金・購入電力・充電期限等の採用戦略で運転を計画する。 | GW＋対応機器＋採用時の外部情報源 | [GW-FN-002](../II_GW/II-02_GW_Functions.md#gw-fn-002)、[GW-FN-003](../II_GW/II-02_GW_Functions.md#gw-fn-003)、[GW-FN-004](../II_GW/II-02_GW_Functions.md#gw-fn-004)、[GW-FN-005](../II_GW/II-02_GW_Functions.md#gw-fn-005)、[GW-FN-006](../II_GW/II-02_GW_Functions.md#gw-fn-006) |
| [S-FN-007](#s-fn-007) | **計画評価・再計画**：実績・制約・機器離脱・入力不足を踏まえ、再計画又は縮退を行う。 | GW＋機器状態／観測 | [GW-FN-003](../II_GW/II-02_GW_Functions.md#gw-fn-003)、[GW-FN-004](../II_GW/II-02_GW_Functions.md#gw-fn-004)、[GW-FN-005](../II_GW/II-02_GW_Functions.md#gw-fn-005)、[GW-FN-007](../II_GW/II-02_GW_Functions.md#gw-fn-007)、[GW-FN-008](../II_GW/II-02_GW_Functions.md#gw-fn-008)、[GW-FN-026](../II_GW/II-02_GW_Functions.md#gw-fn-026) |
| [S-FN-008](#s-fn-008) | **設備登録・接続構成管理**：機器・物理設備・計測点・制御能力・版・接続を整合させる。 | GW＋機器＋認可された施工／管理主体 | [GW-FN-010](../II_GW/II-02_GW_Functions.md#gw-fn-010)、[GW-FN-011](../II_GW/II-02_GW_Functions.md#gw-fn-011)、[GW-FN-012](../II_GW/II-02_GW_Functions.md#gw-fn-012)、[GW-FN-029](../II_GW/II-02_GW_Functions.md#gw-fn-029)、[GW-FN-031](../II_GW/II-02_GW_Functions.md#gw-fn-031) |
| [S-FN-009](#s-fn-009) | **設定変更・保存・復元**：許可した設定を世代管理し、希望・保存・有効状態と競合を区別する。 | 操作端末／上位＋GWの設定所有者 | [GW-FN-001](../II_GW/II-02_GW_Functions.md#gw-fn-001)、[GW-FN-017](../II_GW/II-02_GW_Functions.md#gw-fn-017)、[GW-FN-020](../II_GW/II-02_GW_Functions.md#gw-fn-020)、[GW-FN-021](../II_GW/II-02_GW_Functions.md#gw-fn-021)、[GW-FN-030](../II_GW/II-02_GW_Functions.md#gw-fn-030) |
| [S-FN-010](#s-fn-010) | **GW内部機能の操作**：認可された開始停止・再探索・再起動等をJobとして実行する。 | 利用主体／上位＋GW | [GW-FN-001](../II_GW/II-02_GW_Functions.md#gw-fn-001)、[GW-FN-017](../II_GW/II-02_GW_Functions.md#gw-fn-017)、[GW-FN-022](../II_GW/II-02_GW_Functions.md#gw-fn-022) |
| [S-FN-011](#s-fn-011) | **FW配信・適用・復旧**：配布物の承認・配送・検証・適用・復旧を別主体／段階で管理する。 | リリース承認主体＋FWサーバ＋GW | [GW-FN-023](../II_GW/II-02_GW_Functions.md#gw-fn-023)、[GW-FN-024](../II_GW/II-02_GW_Functions.md#gw-fn-024) |
| [S-FN-012](#s-fn-012) | **RS-485 PCSの遠隔出力制御**：GW G側が宅内ルータ経由でスケジュールを取得・管理し、RS-485でPCSへ指示する。 | 出力制御サーバ＋ルータ＋GW G側＋RS-485 PCS | [GW-FN-011](../II_GW/II-02_GW_Functions.md#gw-fn-011)、[GW-FN-014](../II_GW/II-02_GW_Functions.md#gw-fn-014)、[GW-FN-015](../II_GW/II-02_GW_Functions.md#gw-fn-015)、[GW-FN-028](../II_GW/II-02_GW_Functions.md#gw-fn-028) |
| [S-FN-013](#s-fn-013) | **EL接続PCSの自律出力制御**：PCS自身が宅内ルータ経由で取得・保存・適用する。GWを代理取得器にしない。 | 出力制御サーバ＋ルータ＋EL接続PCS | [GW-FN-016](../II_GW/II-02_GW_Functions.md#gw-fn-016)、[GW-FN-028](../II_GW/II-02_GW_Functions.md#gw-fn-028) |
| [S-FN-014](#s-fn-014) | **PCS側の系統連系保護**：機器側の独立した保護を成立させ、HEMSの応答・承認を待たない。 | PCS等の確認対象保護機能 | [GW-FN-016](../II_GW/II-02_GW_Functions.md#gw-fn-016)、[GW-FN-028](../II_GW/II-02_GW_Functions.md#gw-fn-028) |
| [S-FN-015](#s-fn-015) | **競合・通信断・停止・復旧の協調**：通常要求の競合と、障害位置別の残留・失効・復旧を管理する。 | GW H/G＋PCS＋ネットワーク＋各サービス | [GW-FN-002](../II_GW/II-02_GW_Functions.md#gw-fn-002)、[GW-FN-003](../II_GW/II-02_GW_Functions.md#gw-fn-003)、[GW-FN-004](../II_GW/II-02_GW_Functions.md#gw-fn-004)、[GW-FN-007](../II_GW/II-02_GW_Functions.md#gw-fn-007)、[GW-FN-015](../II_GW/II-02_GW_Functions.md#gw-fn-015)、[GW-FN-020](../II_GW/II-02_GW_Functions.md#gw-fn-020)、[GW-FN-022](../II_GW/II-02_GW_Functions.md#gw-fn-022)、[GW-FN-024](../II_GW/II-02_GW_Functions.md#gw-fn-024)、[GW-FN-026](../II_GW/II-02_GW_Functions.md#gw-fn-026)、[GW-FN-032](../II_GW/II-02_GW_Functions.md#gw-fn-032) |
| [S-FN-016](#s-fn-016) | **警報・通知・診断**：異常と操作結果を記録・通知し、公開範囲内で診断可能にする。 | GW＋クラウド／UI＋機器 | [GW-FN-008](../II_GW/II-02_GW_Functions.md#gw-fn-008)、[GW-FN-009](../II_GW/II-02_GW_Functions.md#gw-fn-009)、[GW-FN-016](../II_GW/II-02_GW_Functions.md#gw-fn-016)、[GW-FN-017](../II_GW/II-02_GW_Functions.md#gw-fn-017)、[GW-FN-019](../II_GW/II-02_GW_Functions.md#gw-fn-019)、[GW-FN-022](../II_GW/II-02_GW_Functions.md#gw-fn-022)、[GW-FN-025](../II_GW/II-02_GW_Functions.md#gw-fn-025) |
| [S-FN-017](#s-fn-017) | **履歴の保存・提出・利用**：用途別のデータを保持し、期間・品質・欠測を明示して抽出する。 | GW＋採用するクラウド保存／利用先 | [GW-FN-008](../II_GW/II-02_GW_Functions.md#gw-fn-008)、[GW-FN-009](../II_GW/II-02_GW_Functions.md#gw-fn-009) |
| [S-FN-018](#s-fn-018) | **外部HEMSとの機器公開連携**：GWがDevice側として許可する情報・操作を外部HEMSへ提供する。 | 外部HEMS＋GW＋実機対応 | [GW-FN-013](../II_GW/II-02_GW_Functions.md#gw-fn-013) |
| [S-FN-019](#s-fn-019) | **利用者識別・権限・所属管理**：4種類の利用者に対して、認可・失効・対象範囲・監査を適用する。 | 利用者＋GW／クラウド／製造保守の各認可境界 | [GW-FN-001](../II_GW/II-02_GW_Functions.md#gw-fn-001)、[GW-FN-017](../II_GW/II-02_GW_Functions.md#gw-fn-017)、[GW-FN-025](../II_GW/II-02_GW_Functions.md#gw-fn-025)、[GW-FN-027](../II_GW/II-02_GW_Functions.md#gw-fn-027)、[GW-FN-028](../II_GW/II-02_GW_Functions.md#gw-fn-028)、[GW-FN-030](../II_GW/II-02_GW_Functions.md#gw-fn-030) |
| [S-FN-020](#s-fn-020) | **製造・施工・保守・交換・廃棄支援**：個体識別から引渡し、交換、所有者変更、消去まで必要な支援を定義する。 | メーカー／メンテナンス／ユーザ＋GW＋支援基盤 | [GW-FN-010](../II_GW/II-02_GW_Functions.md#gw-fn-010)、[GW-FN-020](../II_GW/II-02_GW_Functions.md#gw-fn-020)、[GW-FN-022](../II_GW/II-02_GW_Functions.md#gw-fn-022)、[GW-FN-025](../II_GW/II-02_GW_Functions.md#gw-fn-025)、[GW-FN-027](../II_GW/II-02_GW_Functions.md#gw-fn-027)、[GW-FN-029](../II_GW/II-02_GW_Functions.md#gw-fn-029)、[GW-FN-030](../II_GW/II-02_GW_Functions.md#gw-fn-030)、[GW-FN-032](../II_GW/II-02_GW_Functions.md#gw-fn-032) |
| [S-FN-021](#s-fn-021) | **通信・周辺機器の構成と復旧**：通信方式・USB等の採用条件、接続・故障・復旧を管理する。 | GW＋宅内ルータ＋周辺機器 | [GW-FN-021](../II_GW/II-02_GW_Functions.md#gw-fn-021)、[GW-FN-026](../II_GW/II-02_GW_Functions.md#gw-fn-026)、[GW-FN-031](../II_GW/II-02_GW_Functions.md#gw-fn-031) |

## 機能別の適用・根拠カード

<a id="s-fn-001"></a>
### S-FN-001 — エネルギー・設備状態の把握

機器と計測器の状態・電力等を、品質・鮮度とともに把握する。

**適用条件：** 対応する計測能力と計測点が確定する構成

**判断状態：** R6_DESIGN_DRAFT。採用リリース・実装確認・正式USDM対応は未確定。

**実現責任／GW内担当：** 機器・計測器＋GW＋表示先。

**機能配賦：** [GW-FN-008](../II_GW/II-02_GW_Functions.md#gw-fn-008) ／ [GW-FN-009](../II_GW/II-02_GW_Functions.md#gw-fn-009) ／ [GW-FN-012](../II_GW/II-02_GW_Functions.md#gw-fn-012) ／ [GW-FN-016](../II_GW/II-02_GW_Functions.md#gw-fn-016)。

**関連SYS要求：** [SYS-CAP-001](../../appendices/Requirements_Catalog.md#sys-cap-001)、[SYS-DATA-001](../../appendices/Requirements_Catalog.md#sys-data-001)、[SYS-DATA-002](../../appendices/Requirements_Catalog.md#sys-data-002)、[SYS-EL-001](../../appendices/Requirements_Catalog.md#sys-el-001)、[SYS-GNET-004](../../appendices/Requirements_Catalog.md#sys-gnet-004)、[SYS-GNET-007](../../appendices/Requirements_Catalog.md#sys-gnet-007)、[SYS-GSEL-013](../../appendices/Requirements_Catalog.md#sys-gsel-013)、[SYS-GSEL-014](../../appendices/Requirements_Catalog.md#sys-gsel-014)、[SYS-MEAS-001](../../appendices/Requirements_Catalog.md#sys-meas-001)、[SYS-MEAS-002](../../appendices/Requirements_Catalog.md#sys-meas-002)、[SYS-NORTH-006](../../appendices/Requirements_Catalog.md#sys-north-006)、[SYS-STATE-001](../../appendices/Requirements_Catalog.md#sys-state-001)、[SYS-STATE-002](../../appendices/Requirements_Catalog.md#sys-state-002)。

**詳細章：** [II-07_Measurement_Data](../II_GW/II-07_Measurement_Data.md) ／ [IV-08_Data_Log_UI_Quality](../IV_Quality/IV-08_Data_Log_UI_Quality.md) ／ [III-06_ECHONET_Lite](../III_Interfaces/III-06_ECHONET_Lite.md) ／ [I-04_System_Context](I-04_System_Context.md) ／ [I-07_Responsibilities_Constraints](I-07_Responsibilities_Constraints.md)。

**具体的な不足：** [OQ-R6-09-01](../II_GW/II-07_Measurement_Data.md#oq-r6-09-01)。

<a id="s-fn-002"></a>
### S-FN-002 — 宅内モニタリング・操作

宅内ブラウザから監視し、認可された操作と結果を確認する。

**適用条件：** 直接無線／ルータ経由。採用条件は個別確定

**判断状態：** R6_DESIGN_DRAFT。採用リリース・実装確認・正式USDM対応は未確定。

**実現責任／GW内担当：** 端末ブラウザ＋GW＋宅内LAN/AP（直接無線は別経路）。

**機能配賦：** [GW-FN-001](../II_GW/II-02_GW_Functions.md#gw-fn-001) ／ [GW-FN-018](../II_GW/II-02_GW_Functions.md#gw-fn-018)。

**関連SYS要求：** [SYS-GNET-010](../../appendices/Requirements_Catalog.md#sys-gnet-010)、[SYS-NORTH-001](../../appendices/Requirements_Catalog.md#sys-north-001)、[SYS-NORTH-002](../../appendices/Requirements_Catalog.md#sys-north-002)、[SYS-NORTH-007](../../appendices/Requirements_Catalog.md#sys-north-007)、[SYS-REQ-001](../../appendices/Requirements_Catalog.md#sys-req-001)、[SYS-UI-001](../../appendices/Requirements_Catalog.md#sys-ui-001)、[SYS-UI-002](../../appendices/Requirements_Catalog.md#sys-ui-002)、[SYS-UI-003](../../appendices/Requirements_Catalog.md#sys-ui-003)、[SYS-UI-004](../../appendices/Requirements_Catalog.md#sys-ui-004)、[SYS-UI-005](../../appendices/Requirements_Catalog.md#sys-ui-005)。

**詳細章：** [II-03_Control_Execution](../II_GW/II-03_Control_Execution.md) ／ [III-02_Cloud_GW](../III_Interfaces/III-02_Cloud_GW.md) ／ [IV-03_Security_Privacy](../IV_Quality/IV-03_Security_Privacy.md) ／ [III-04_Local_Web](../III_Interfaces/III-04_Local_Web.md) ／ [IV-08_Data_Log_UI_Quality](../IV_Quality/IV-08_Data_Log_UI_Quality.md)。

**具体的な不足：** [OQ-R6-02-02](I-04_System_Context.md#oq-r6-02-02) ／ [OQ-R6-20-02](../IV_Quality/IV-08_Data_Log_UI_Quality.md#oq-r6-20-02)。

<a id="s-fn-003"></a>
### S-FN-003 — リモートモニタリング・操作

スマートフォンアプリからクラウド経由で対象住宅を監視・操作する。

**適用条件：** GWはアプリの実装主体ではない

**判断状態：** R6_DESIGN_DRAFT。採用リリース・実装確認・正式USDM対応は未確定。

**実現責任／GW内担当：** アプリ＋クラウド＋宅内ルータ＋GW＋対象機器。

**機能配賦：** [GW-FN-001](../II_GW/II-02_GW_Functions.md#gw-fn-001) ／ [GW-FN-009](../II_GW/II-02_GW_Functions.md#gw-fn-009) ／ [GW-FN-017](../II_GW/II-02_GW_Functions.md#gw-fn-017) ／ [GW-FN-019](../II_GW/II-02_GW_Functions.md#gw-fn-019)。

**関連SYS要求：** [SYS-APP-001](../../appendices/Requirements_Catalog.md#sys-app-001)、[SYS-APP-002](../../appendices/Requirements_Catalog.md#sys-app-002)、[SYS-DATA-001](../../appendices/Requirements_Catalog.md#sys-data-001)、[SYS-DATA-002](../../appendices/Requirements_Catalog.md#sys-data-002)、[SYS-GWOP-001](../../appendices/Requirements_Catalog.md#sys-gwop-001)、[SYS-NORTH-001](../../appendices/Requirements_Catalog.md#sys-north-001)、[SYS-NORTH-002](../../appendices/Requirements_Catalog.md#sys-north-002)、[SYS-NORTH-003](../../appendices/Requirements_Catalog.md#sys-north-003)、[SYS-NORTH-004](../../appendices/Requirements_Catalog.md#sys-north-004)、[SYS-NORTH-005](../../appendices/Requirements_Catalog.md#sys-north-005)、[SYS-NORTH-006](../../appendices/Requirements_Catalog.md#sys-north-006)、[SYS-NORTH-007](../../appendices/Requirements_Catalog.md#sys-north-007)、[SYS-REQ-001](../../appendices/Requirements_Catalog.md#sys-req-001)、[SYS-STATE-001](../../appendices/Requirements_Catalog.md#sys-state-001)、[SYS-STATE-002](../../appendices/Requirements_Catalog.md#sys-state-002)。

**詳細章：** [II-03_Control_Execution](../II_GW/II-03_Control_Execution.md) ／ [III-02_Cloud_GW](../III_Interfaces/III-02_Cloud_GW.md) ／ [IV-03_Security_Privacy](../IV_Quality/IV-03_Security_Privacy.md) ／ [II-07_Measurement_Data](../II_GW/II-07_Measurement_Data.md) ／ [IV-08_Data_Log_UI_Quality](../IV_Quality/IV-08_Data_Log_UI_Quality.md) ／ [III-05_Remote_App](../III_Interfaces/III-05_Remote_App.md)。

**具体的な不足：** [OQ-R6-20-01](../III_Interfaces/III-02_Cloud_GW.md#oq-r6-20-01) ／ [OQ-R6-20-02](../IV_Quality/IV-08_Data_Log_UI_Quality.md#oq-r6-20-02)。

<a id="s-fn-004"></a>
### S-FN-004 — PV・蓄電池等の通常運転

許可されたDER操作を実機へ届け、受理と観測による達成を区別する。

**適用条件：** RS-485／ELの能力と更新間隔を別確認

**判断状態：** R6_DESIGN_DRAFT。採用リリース・実装確認・正式USDM対応は未確定。

**実現責任／GW内担当：** GW＋PCS／DER。

**機能配賦：** [GW-FN-001](../II_GW/II-02_GW_Functions.md#gw-fn-001) ／ [GW-FN-002](../II_GW/II-02_GW_Functions.md#gw-fn-002) ／ [GW-FN-003](../II_GW/II-02_GW_Functions.md#gw-fn-003) ／ [GW-FN-004](../II_GW/II-02_GW_Functions.md#gw-fn-004) ／ [GW-FN-010](../II_GW/II-02_GW_Functions.md#gw-fn-010) ／ [GW-FN-011](../II_GW/II-02_GW_Functions.md#gw-fn-011) ／ [GW-FN-012](../II_GW/II-02_GW_Functions.md#gw-fn-012)。

**関連SYS要求：** [SYS-AUTH-001](../../appendices/Requirements_Catalog.md#sys-auth-001)、[SYS-AUTH-002](../../appendices/Requirements_Catalog.md#sys-auth-002)、[SYS-CAP-001](../../appendices/Requirements_Catalog.md#sys-cap-001)、[SYS-CAP-002](../../appendices/Requirements_Catalog.md#sys-cap-002)、[SYS-COEX-001](../../appendices/Requirements_Catalog.md#sys-coex-001)、[SYS-EL-001](../../appendices/Requirements_Catalog.md#sys-el-001)、[SYS-GNET-004](../../appendices/Requirements_Catalog.md#sys-gnet-004)、[SYS-GNET-012](../../appendices/Requirements_Catalog.md#sys-gnet-012)、[SYS-NORTH-001](../../appendices/Requirements_Catalog.md#sys-north-001)、[SYS-NORTH-002](../../appendices/Requirements_Catalog.md#sys-north-002)、[SYS-NORTH-007](../../appendices/Requirements_Catalog.md#sys-north-007)、[SYS-ORCH-001](../../appendices/Requirements_Catalog.md#sys-orch-001)、[SYS-REQ-001](../../appendices/Requirements_Catalog.md#sys-req-001)、[SYS-RESP-001](../../appendices/Requirements_Catalog.md#sys-resp-001)、[SYS-RESULT-001](../../appendices/Requirements_Catalog.md#sys-result-001)、[SYS-RESULT-002](../../appendices/Requirements_Catalog.md#sys-result-002)、[SYS-RESULT-003](../../appendices/Requirements_Catalog.md#sys-result-003)、[SYS-RETRY-001](../../appendices/Requirements_Catalog.md#sys-retry-001)、[SYS-ROUTE-001](../../appendices/Requirements_Catalog.md#sys-route-001)、[SYS-RS-001](../../appendices/Requirements_Catalog.md#sys-rs-001)、[SYS-RS-002](../../appendices/Requirements_Catalog.md#sys-rs-002)、[SYS-RS-003](../../appendices/Requirements_Catalog.md#sys-rs-003)、[SYS-RS-005](../../appendices/Requirements_Catalog.md#sys-rs-005)、[SYS-RS-006](../../appendices/Requirements_Catalog.md#sys-rs-006)、[SYS-SEM-001](../../appendices/Requirements_Catalog.md#sys-sem-001)。

**詳細章：** [II-03_Control_Execution](../II_GW/II-03_Control_Execution.md) ／ [III-02_Cloud_GW](../III_Interfaces/III-02_Cloud_GW.md) ／ [IV-03_Security_Privacy](../IV_Quality/IV-03_Security_Privacy.md) ／ [I-06_Usecases](I-06_Usecases.md) ／ [II-04_DER_Load_Control](../II_GW/II-04_DER_Load_Control.md) ／ [III-07_RS485_PCS](../III_Interfaces/III-07_RS485_PCS.md) ／ [III-06_ECHONET_Lite](../III_Interfaces/III-06_ECHONET_Lite.md) ／ [II-06_Device_Management](../II_GW/II-06_Device_Management.md) ／ [I-05_Configurations](I-05_Configurations.md) ／ [II-08_GW_Grid_Control](../II_GW/II-08_GW_Grid_Control.md) ／ [I-04_System_Context](I-04_System_Context.md)。

**具体的な不足：** [OQ-R6-07-01](../III_Interfaces/III-07_RS485_PCS.md#oq-r6-07-01) ／ [OQ-R6-07-02](../III_Interfaces/III-06_ECHONET_Lite.md#oq-r6-07-02)。

<a id="s-fn-005"></a>
### S-FN-005 — 空調・給湯等の負荷操作

快適性・機器安全を尊重して、採用された負荷操作を実行する。

**適用条件：** 必要なELプロパティ・機器能力を確認

**判断状態：** R6_DESIGN_DRAFT。採用リリース・実装確認・正式USDM対応は未確定。

**実現責任／GW内担当：** GW＋空調・給湯等。

**機能配賦：** [GW-FN-001](../II_GW/II-02_GW_Functions.md#gw-fn-001) ／ [GW-FN-002](../II_GW/II-02_GW_Functions.md#gw-fn-002) ／ [GW-FN-003](../II_GW/II-02_GW_Functions.md#gw-fn-003) ／ [GW-FN-005](../II_GW/II-02_GW_Functions.md#gw-fn-005) ／ [GW-FN-010](../II_GW/II-02_GW_Functions.md#gw-fn-010) ／ [GW-FN-012](../II_GW/II-02_GW_Functions.md#gw-fn-012)。

**関連SYS要求：** [SYS-AUTH-001](../../appendices/Requirements_Catalog.md#sys-auth-001)、[SYS-AUTH-002](../../appendices/Requirements_Catalog.md#sys-auth-002)、[SYS-CAP-001](../../appendices/Requirements_Catalog.md#sys-cap-001)、[SYS-CAP-002](../../appendices/Requirements_Catalog.md#sys-cap-002)、[SYS-COEX-001](../../appendices/Requirements_Catalog.md#sys-coex-001)、[SYS-EL-001](../../appendices/Requirements_Catalog.md#sys-el-001)、[SYS-GNET-004](../../appendices/Requirements_Catalog.md#sys-gnet-004)、[SYS-GNET-012](../../appendices/Requirements_Catalog.md#sys-gnet-012)、[SYS-LOAD-001](../../appendices/Requirements_Catalog.md#sys-load-001)、[SYS-NORTH-001](../../appendices/Requirements_Catalog.md#sys-north-001)、[SYS-NORTH-002](../../appendices/Requirements_Catalog.md#sys-north-002)、[SYS-NORTH-007](../../appendices/Requirements_Catalog.md#sys-north-007)、[SYS-ORCH-001](../../appendices/Requirements_Catalog.md#sys-orch-001)、[SYS-REQ-001](../../appendices/Requirements_Catalog.md#sys-req-001)、[SYS-RETRY-001](../../appendices/Requirements_Catalog.md#sys-retry-001)、[SYS-ROUTE-001](../../appendices/Requirements_Catalog.md#sys-route-001)。

**詳細章：** [II-03_Control_Execution](../II_GW/II-03_Control_Execution.md) ／ [III-02_Cloud_GW](../III_Interfaces/III-02_Cloud_GW.md) ／ [IV-03_Security_Privacy](../IV_Quality/IV-03_Security_Privacy.md) ／ [I-06_Usecases](I-06_Usecases.md) ／ [II-04_DER_Load_Control](../II_GW/II-04_DER_Load_Control.md) ／ [III-06_ECHONET_Lite](../III_Interfaces/III-06_ECHONET_Lite.md) ／ [II-06_Device_Management](../II_GW/II-06_Device_Management.md) ／ [I-05_Configurations](I-05_Configurations.md) ／ [I-04_System_Context](I-04_System_Context.md)。

**具体的な不足：** [OQ-R6-08-03](../II_GW/II-04_DER_Load_Control.md#oq-r6-08-03)。

<a id="s-fn-006"></a>
### S-FN-006 — 高度エネマネ運転計画

自家消費・料金・購入電力・充電期限等の採用戦略で運転を計画する。

**適用条件：** 候補戦略を初回必須としない

**判断状態：** R6_DESIGN_DRAFT。採用リリース・実装確認・正式USDM対応は未確定。

**実現責任／GW内担当：** GW＋対応機器＋採用時の外部情報源。

**機能配賦：** [GW-FN-002](../II_GW/II-02_GW_Functions.md#gw-fn-002) ／ [GW-FN-003](../II_GW/II-02_GW_Functions.md#gw-fn-003) ／ [GW-FN-004](../II_GW/II-02_GW_Functions.md#gw-fn-004) ／ [GW-FN-005](../II_GW/II-02_GW_Functions.md#gw-fn-005) ／ [GW-FN-006](../II_GW/II-02_GW_Functions.md#gw-fn-006)。

**関連SYS要求：** [SYS-AUTH-001](../../appendices/Requirements_Catalog.md#sys-auth-001)、[SYS-AUTH-002](../../appendices/Requirements_Catalog.md#sys-auth-002)、[SYS-COEX-001](../../appendices/Requirements_Catalog.md#sys-coex-001)、[SYS-CONST-001](../../appendices/Requirements_Catalog.md#sys-const-001)、[SYS-EMS-001](../../appendices/Requirements_Catalog.md#sys-ems-001)、[SYS-LOAD-001](../../appendices/Requirements_Catalog.md#sys-load-001)、[SYS-ORCH-001](../../appendices/Requirements_Catalog.md#sys-orch-001)、[SYS-RESP-001](../../appendices/Requirements_Catalog.md#sys-resp-001)、[SYS-RESULT-001](../../appendices/Requirements_Catalog.md#sys-result-001)、[SYS-RESULT-002](../../appendices/Requirements_Catalog.md#sys-result-002)、[SYS-RESULT-003](../../appendices/Requirements_Catalog.md#sys-result-003)、[SYS-RETRY-001](../../appendices/Requirements_Catalog.md#sys-retry-001)、[SYS-SEM-001](../../appendices/Requirements_Catalog.md#sys-sem-001)。

**詳細章：** [II-03_Control_Execution](../II_GW/II-03_Control_Execution.md) ／ [I-06_Usecases](I-06_Usecases.md) ／ [II-04_DER_Load_Control](../II_GW/II-04_DER_Load_Control.md) ／ [III-07_RS485_PCS](../III_Interfaces/III-07_RS485_PCS.md) ／ [III-06_ECHONET_Lite](../III_Interfaces/III-06_ECHONET_Lite.md) ／ [II-05_Advanced_EMS](../II_GW/II-05_Advanced_EMS.md)。

**具体的な不足：** [OQ-R6-08-01](../II_GW/II-05_Advanced_EMS.md#oq-r6-08-01) ／ [OQ-R6-08-02](../II_GW/II-05_Advanced_EMS.md#oq-r6-08-02)。

<a id="s-fn-007"></a>
### S-FN-007 — 計画評価・再計画

実績・制約・機器離脱・入力不足を踏まえ、再計画又は縮退を行う。

**適用条件：** 達成条件と原因不明の扱いを区別

**判断状態：** R6_DESIGN_DRAFT。採用リリース・実装確認・正式USDM対応は未確定。

**実現責任／GW内担当：** GW＋機器状態／観測。

**機能配賦：** [GW-FN-003](../II_GW/II-02_GW_Functions.md#gw-fn-003) ／ [GW-FN-004](../II_GW/II-02_GW_Functions.md#gw-fn-004) ／ [GW-FN-005](../II_GW/II-02_GW_Functions.md#gw-fn-005) ／ [GW-FN-007](../II_GW/II-02_GW_Functions.md#gw-fn-007) ／ [GW-FN-008](../II_GW/II-02_GW_Functions.md#gw-fn-008) ／ [GW-FN-026](../II_GW/II-02_GW_Functions.md#gw-fn-026)。

**関連SYS要求：** [SYS-CONST-001](../../appendices/Requirements_Catalog.md#sys-const-001)、[SYS-EMS-001](../../appendices/Requirements_Catalog.md#sys-ems-001)、[SYS-EXPIRY-001](../../appendices/Requirements_Catalog.md#sys-expiry-001)、[SYS-FAULT-001](../../appendices/Requirements_Catalog.md#sys-fault-001)、[SYS-GNET-005](../../appendices/Requirements_Catalog.md#sys-gnet-005)、[SYS-LOAD-001](../../appendices/Requirements_Catalog.md#sys-load-001)、[SYS-MEAS-001](../../appendices/Requirements_Catalog.md#sys-meas-001)、[SYS-MEAS-002](../../appendices/Requirements_Catalog.md#sys-meas-002)、[SYS-ORCH-001](../../appendices/Requirements_Catalog.md#sys-orch-001)、[SYS-RESP-001](../../appendices/Requirements_Catalog.md#sys-resp-001)、[SYS-RESULT-001](../../appendices/Requirements_Catalog.md#sys-result-001)、[SYS-RESULT-002](../../appendices/Requirements_Catalog.md#sys-result-002)、[SYS-RESULT-003](../../appendices/Requirements_Catalog.md#sys-result-003)、[SYS-RETRY-001](../../appendices/Requirements_Catalog.md#sys-retry-001)、[SYS-SEM-001](../../appendices/Requirements_Catalog.md#sys-sem-001)、[SYS-STATE-001](../../appendices/Requirements_Catalog.md#sys-state-001)、[SYS-STATE-002](../../appendices/Requirements_Catalog.md#sys-state-002)。

**詳細章：** [II-03_Control_Execution](../II_GW/II-03_Control_Execution.md) ／ [I-06_Usecases](I-06_Usecases.md) ／ [II-04_DER_Load_Control](../II_GW/II-04_DER_Load_Control.md) ／ [III-07_RS485_PCS](../III_Interfaces/III-07_RS485_PCS.md) ／ [III-06_ECHONET_Lite](../III_Interfaces/III-06_ECHONET_Lite.md) ／ [II-05_Advanced_EMS](../II_GW/II-05_Advanced_EMS.md) ／ [II-10_Fault_Alarm_Diagnostics](../II_GW/II-10_Fault_Alarm_Diagnostics.md) ／ [II-07_Measurement_Data](../II_GW/II-07_Measurement_Data.md) ／ [I-08_System_States](I-08_System_States.md)。

**具体的な不足：** [OQ-R6-08-02](../II_GW/II-05_Advanced_EMS.md#oq-r6-08-02)。

<a id="s-fn-008"></a>
### S-FN-008 — 設備登録・接続構成管理

機器・物理設備・計測点・制御能力・版・接続を整合させる。

**適用条件：** 検出だけで全操作対応にしない

**判断状態：** R6_DESIGN_DRAFT。採用リリース・実装確認・正式USDM対応は未確定。

**実現責任／GW内担当：** GW＋機器＋認可された施工／管理主体。

**機能配賦：** [GW-FN-010](../II_GW/II-02_GW_Functions.md#gw-fn-010) ／ [GW-FN-011](../II_GW/II-02_GW_Functions.md#gw-fn-011) ／ [GW-FN-012](../II_GW/II-02_GW_Functions.md#gw-fn-012) ／ [GW-FN-029](../II_GW/II-02_GW_Functions.md#gw-fn-029) ／ [GW-FN-031](../II_GW/II-02_GW_Functions.md#gw-fn-031)。

**関連SYS要求：** [SYS-CAP-001](../../appendices/Requirements_Catalog.md#sys-cap-001)、[SYS-CAP-002](../../appendices/Requirements_Catalog.md#sys-cap-002)、[SYS-EL-001](../../appendices/Requirements_Catalog.md#sys-el-001)、[SYS-GNET-004](../../appendices/Requirements_Catalog.md#sys-gnet-004)、[SYS-GNET-012](../../appendices/Requirements_Catalog.md#sys-gnet-012)、[SYS-GSEL-019](../../appendices/Requirements_Catalog.md#sys-gsel-019)、[SYS-MIG-002](../../appendices/Requirements_Catalog.md#sys-mig-002)、[SYS-ROUTE-001](../../appendices/Requirements_Catalog.md#sys-route-001)、[SYS-RS-001](../../appendices/Requirements_Catalog.md#sys-rs-001)、[SYS-RS-002](../../appendices/Requirements_Catalog.md#sys-rs-002)、[SYS-RS-003](../../appendices/Requirements_Catalog.md#sys-rs-003)、[SYS-RS-005](../../appendices/Requirements_Catalog.md#sys-rs-005)、[SYS-RS-006](../../appendices/Requirements_Catalog.md#sys-rs-006)、[SYS-SEC-001](../../appendices/Requirements_Catalog.md#sys-sec-001)、[SYS-SVC-001](../../appendices/Requirements_Catalog.md#sys-svc-001)。

**詳細章：** [II-06_Device_Management](../II_GW/II-06_Device_Management.md) ／ [I-05_Configurations](I-05_Configurations.md) ／ [III-07_RS485_PCS](../III_Interfaces/III-07_RS485_PCS.md) ／ [II-08_GW_Grid_Control](../II_GW/II-08_GW_Grid_Control.md) ／ [III-06_ECHONET_Lite](../III_Interfaces/III-06_ECHONET_Lite.md) ／ [I-04_System_Context](I-04_System_Context.md) ／ [V-01_Manufacturing_Shipping](../V_Lifecycle/V-01_Manufacturing_Shipping.md) ／ [V-02_Commissioning_Handover](../V_Lifecycle/V-02_Commissioning_Handover.md) ／ [III-09_Network_Peripherals](../III_Interfaces/III-09_Network_Peripherals.md)。

**具体的な不足：** [OQ-R6-04-02](I-05_Configurations.md#oq-r6-04-02) ／ [OQ-R6-04-03](../II_GW/II-06_Device_Management.md#oq-r6-04-03)。

<a id="s-fn-009"></a>
### S-FN-009 — 設定変更・保存・復元

許可した設定を世代管理し、希望・保存・有効状態と競合を区別する。

**適用条件：** G側系統設定は通常設定と別契約

**判断状態：** R6_DESIGN_DRAFT。採用リリース・実装確認・正式USDM対応は未確定。

**実現責任／GW内担当：** 操作端末／上位＋GWの設定所有者。

**機能配賦：** [GW-FN-001](../II_GW/II-02_GW_Functions.md#gw-fn-001) ／ [GW-FN-017](../II_GW/II-02_GW_Functions.md#gw-fn-017) ／ [GW-FN-020](../II_GW/II-02_GW_Functions.md#gw-fn-020) ／ [GW-FN-021](../II_GW/II-02_GW_Functions.md#gw-fn-021) ／ [GW-FN-030](../II_GW/II-02_GW_Functions.md#gw-fn-030)。

**関連SYS要求：** [SYS-APP-003](../../appendices/Requirements_Catalog.md#sys-app-003)、[SYS-CFG-001](../../appendices/Requirements_Catalog.md#sys-cfg-001)、[SYS-CFG-002](../../appendices/Requirements_Catalog.md#sys-cfg-002)、[SYS-CFG-003](../../appendices/Requirements_Catalog.md#sys-cfg-003)、[SYS-CFG-004](../../appendices/Requirements_Catalog.md#sys-cfg-004)、[SYS-CFG-005](../../appendices/Requirements_Catalog.md#sys-cfg-005)、[SYS-CFG-006](../../appendices/Requirements_Catalog.md#sys-cfg-006)、[SYS-GNET-006](../../appendices/Requirements_Catalog.md#sys-gnet-006)、[SYS-GSEL-019](../../appendices/Requirements_Catalog.md#sys-gsel-019)、[SYS-GWOP-001](../../appendices/Requirements_Catalog.md#sys-gwop-001)、[SYS-NORTH-001](../../appendices/Requirements_Catalog.md#sys-north-001)、[SYS-NORTH-002](../../appendices/Requirements_Catalog.md#sys-north-002)、[SYS-NORTH-003](../../appendices/Requirements_Catalog.md#sys-north-003)、[SYS-NORTH-004](../../appendices/Requirements_Catalog.md#sys-north-004)、[SYS-NORTH-005](../../appendices/Requirements_Catalog.md#sys-north-005)、[SYS-NORTH-007](../../appendices/Requirements_Catalog.md#sys-north-007)、[SYS-REQ-001](../../appendices/Requirements_Catalog.md#sys-req-001)、[SYS-STATE-001](../../appendices/Requirements_Catalog.md#sys-state-001)。

**詳細章：** [II-03_Control_Execution](../II_GW/II-03_Control_Execution.md) ／ [III-02_Cloud_GW](../III_Interfaces/III-02_Cloud_GW.md) ／ [IV-03_Security_Privacy](../IV_Quality/IV-03_Security_Privacy.md) ／ [II-09_Settings_Lifecycle](../II_GW/II-09_Settings_Lifecycle.md) ／ [III-09_Network_Peripherals](../III_Interfaces/III-09_Network_Peripherals.md) ／ [V-03_Maintenance_Retirement](../V_Lifecycle/V-03_Maintenance_Retirement.md)。

**具体的な不足：** [OQ-R6-12-02](../II_GW/II-09_Settings_Lifecycle.md#oq-r6-12-02) ／ [OQ-R6-12-03](../II_GW/II-09_Settings_Lifecycle.md#oq-r6-12-03) ／ [OQ-R6-12-04](../II_GW/II-09_Settings_Lifecycle.md#oq-r6-12-04)。

<a id="s-fn-010"></a>
### S-FN-010 — GW内部機能の操作

認可された開始停止・再探索・再起動等をJobとして実行する。

**適用条件：** 任意shell・内部RPCの無制限公開ではない

**判断状態：** R6_DESIGN_DRAFT。採用リリース・実装確認・正式USDM対応は未確定。

**実現責任／GW内担当：** 利用主体／上位＋GW。

**機能配賦：** [GW-FN-001](../II_GW/II-02_GW_Functions.md#gw-fn-001) ／ [GW-FN-017](../II_GW/II-02_GW_Functions.md#gw-fn-017) ／ [GW-FN-022](../II_GW/II-02_GW_Functions.md#gw-fn-022)。

**関連SYS要求：** [SYS-GWOP-001](../../appendices/Requirements_Catalog.md#sys-gwop-001)、[SYS-GWOP-002](../../appendices/Requirements_Catalog.md#sys-gwop-002)、[SYS-NORTH-001](../../appendices/Requirements_Catalog.md#sys-north-001)、[SYS-NORTH-002](../../appendices/Requirements_Catalog.md#sys-north-002)、[SYS-NORTH-003](../../appendices/Requirements_Catalog.md#sys-north-003)、[SYS-NORTH-004](../../appendices/Requirements_Catalog.md#sys-north-004)、[SYS-NORTH-005](../../appendices/Requirements_Catalog.md#sys-north-005)、[SYS-NORTH-007](../../appendices/Requirements_Catalog.md#sys-north-007)、[SYS-REQ-001](../../appendices/Requirements_Catalog.md#sys-req-001)、[SYS-STATE-001](../../appendices/Requirements_Catalog.md#sys-state-001)。

**詳細章：** [II-03_Control_Execution](../II_GW/II-03_Control_Execution.md) ／ [III-02_Cloud_GW](../III_Interfaces/III-02_Cloud_GW.md) ／ [IV-03_Security_Privacy](../IV_Quality/IV-03_Security_Privacy.md) ／ [II-09_Settings_Lifecycle](../II_GW/II-09_Settings_Lifecycle.md) ／ [III-10_Maintenance_Interfaces](../III_Interfaces/III-10_Maintenance_Interfaces.md)。

**具体的な不足：** [OQ-R6-20-01](../III_Interfaces/III-02_Cloud_GW.md#oq-r6-20-01)。

<a id="s-fn-011"></a>
### S-FN-011 — FW配信・適用・復旧

配布物の承認・配送・検証・適用・復旧を別主体／段階で管理する。

**適用条件：** 対象領域とG側独立更新を別管理

**判断状態：** R6_DESIGN_DRAFT。採用リリース・実装確認・正式USDM対応は未確定。

**実現責任／GW内担当：** リリース承認主体＋FWサーバ＋GW。

**機能配賦：** [GW-FN-023](../II_GW/II-02_GW_Functions.md#gw-fn-023) ／ [GW-FN-024](../II_GW/II-02_GW_Functions.md#gw-fn-024)。

**関連SYS要求：** [SYS-FW-001](../../appendices/Requirements_Catalog.md#sys-fw-001)、[SYS-FW-002](../../appendices/Requirements_Catalog.md#sys-fw-002)、[SYS-FW-003](../../appendices/Requirements_Catalog.md#sys-fw-003)、[SYS-FW-004](../../appendices/Requirements_Catalog.md#sys-fw-004)、[SYS-FW-005](../../appendices/Requirements_Catalog.md#sys-fw-005)、[SYS-OTA-001](../../appendices/Requirements_Catalog.md#sys-ota-001)、[SYS-OTA-002](../../appendices/Requirements_Catalog.md#sys-ota-002)。

**詳細章：** [II-11_Firmware_Update](../II_GW/II-11_Firmware_Update.md) ／ [III-03_FW_Server](../III_Interfaces/III-03_FW_Server.md)。

**具体的な不足：** [OQ-R6-20-04](../II_GW/II-11_Firmware_Update.md#oq-r6-20-04)。

<a id="s-fn-012"></a>
### S-FN-012 — RS-485 PCSの遠隔出力制御

GW G側が宅内ルータ経由でスケジュールを取得・管理し、RS-485でPCSへ指示する。

**適用条件：** GW_MANAGED。H側通常EMSから独立

**判断状態：** R6_DESIGN_DRAFT。採用リリース・実装確認・正式USDM対応は未確定。

**実現責任／GW内担当：** 出力制御サーバ＋ルータ＋GW G側＋RS-485 PCS。

**機能配賦：** [GW-FN-011](../II_GW/II-02_GW_Functions.md#gw-fn-011) ／ [GW-FN-014](../II_GW/II-02_GW_Functions.md#gw-fn-014) ／ [GW-FN-015](../II_GW/II-02_GW_Functions.md#gw-fn-015) ／ [GW-FN-028](../II_GW/II-02_GW_Functions.md#gw-fn-028)。

**関連SYS要求：** [SYS-BOUND-001](../../appendices/Requirements_Catalog.md#sys-bound-001)、[SYS-GNET-001](../../appendices/Requirements_Catalog.md#sys-gnet-001)、[SYS-GNET-003](../../appendices/Requirements_Catalog.md#sys-gnet-003)、[SYS-GRID-001](../../appendices/Requirements_Catalog.md#sys-grid-001)、[SYS-GRID-003](../../appendices/Requirements_Catalog.md#sys-grid-003)、[SYS-GSEL-001](../../appendices/Requirements_Catalog.md#sys-gsel-001)、[SYS-GSEL-004](../../appendices/Requirements_Catalog.md#sys-gsel-004)、[SYS-GSEL-005](../../appendices/Requirements_Catalog.md#sys-gsel-005)、[SYS-GSEL-006](../../appendices/Requirements_Catalog.md#sys-gsel-006)、[SYS-GSEL-011](../../appendices/Requirements_Catalog.md#sys-gsel-011)、[SYS-GSEL-012](../../appendices/Requirements_Catalog.md#sys-gsel-012)、[SYS-OTA-001](../../appendices/Requirements_Catalog.md#sys-ota-001)、[SYS-RS-001](../../appendices/Requirements_Catalog.md#sys-rs-001)、[SYS-RS-002](../../appendices/Requirements_Catalog.md#sys-rs-002)、[SYS-RS-003](../../appendices/Requirements_Catalog.md#sys-rs-003)、[SYS-RS-005](../../appendices/Requirements_Catalog.md#sys-rs-005)、[SYS-RS-006](../../appendices/Requirements_Catalog.md#sys-rs-006)。

**詳細章：** [III-07_RS485_PCS](../III_Interfaces/III-07_RS485_PCS.md) ／ [II-08_GW_Grid_Control](../II_GW/II-08_GW_Grid_Control.md) ／ [III-08_Utility_Server](../III_Interfaces/III-08_Utility_Server.md) ／ [III-01_Boundary_Contracts](../III_Interfaces/III-01_Boundary_Contracts.md) ／ [IV-07_Isolation_Shared_Resources](../IV_Quality/IV-07_Isolation_Shared_Resources.md)。

**具体的な不足：** [OQ-R6-10-01](../V_Lifecycle/V-04_Compliance.md#oq-r6-10-01) ／ [OQ-R6-21-01](I-05_Configurations.md#oq-r6-21-01)。

<a id="s-fn-013"></a>
### S-FN-013 — EL接続PCSの自律出力制御

PCS自身が宅内ルータ経由で取得・保存・適用する。GWを代理取得器にしない。

**適用条件：** PCS_DIRECTはEL接続PCSのみ。GW配賦は参照・非迂回支援

**判断状態：** R6_DESIGN_DRAFT。採用リリース・実装確認・正式USDM対応は未確定。

**実現責任／GW内担当：** 出力制御サーバ＋ルータ＋EL接続PCS。

**機能配賦：** [GW-FN-016](../II_GW/II-02_GW_Functions.md#gw-fn-016) ／ [GW-FN-028](../II_GW/II-02_GW_Functions.md#gw-fn-028)。

**関連SYS要求：** [SYS-BOUND-001](../../appendices/Requirements_Catalog.md#sys-bound-001)、[SYS-GNET-002](../../appendices/Requirements_Catalog.md#sys-gnet-002)、[SYS-GNET-004](../../appendices/Requirements_Catalog.md#sys-gnet-004)、[SYS-GNET-007](../../appendices/Requirements_Catalog.md#sys-gnet-007)、[SYS-GRID-001](../../appendices/Requirements_Catalog.md#sys-grid-001)、[SYS-GSEL-004](../../appendices/Requirements_Catalog.md#sys-gsel-004)、[SYS-GSEL-006](../../appendices/Requirements_Catalog.md#sys-gsel-006)、[SYS-GSEL-013](../../appendices/Requirements_Catalog.md#sys-gsel-013)、[SYS-GSEL-014](../../appendices/Requirements_Catalog.md#sys-gsel-014)、[SYS-OTA-001](../../appendices/Requirements_Catalog.md#sys-ota-001)。

**詳細章：** [II-07_Measurement_Data](../II_GW/II-07_Measurement_Data.md) ／ [I-07_Responsibilities_Constraints](I-07_Responsibilities_Constraints.md) ／ [III-01_Boundary_Contracts](../III_Interfaces/III-01_Boundary_Contracts.md) ／ [IV-07_Isolation_Shared_Resources](../IV_Quality/IV-07_Isolation_Shared_Resources.md)。

**具体的な不足：** [OQ-R6-21-01](I-05_Configurations.md#oq-r6-21-01)。

<a id="s-fn-014"></a>
### S-FN-014 — PCS側の系統連系保護

機器側の独立した保護を成立させ、HEMSの応答・承認を待たない。

**適用条件：** GWは状態参照と迂回防止のみ。保護そのものはGW機能に数えない

**判断状態：** R6_DESIGN_DRAFT。採用リリース・実装確認・正式USDM対応は未確定。

**実現責任／GW内担当：** PCS等の確認対象保護機能。

**機能配賦：** [GW-FN-016](../II_GW/II-02_GW_Functions.md#gw-fn-016) ／ [GW-FN-028](../II_GW/II-02_GW_Functions.md#gw-fn-028)。

**関連SYS要求：** [SYS-BOUND-001](../../appendices/Requirements_Catalog.md#sys-bound-001)、[SYS-GNET-004](../../appendices/Requirements_Catalog.md#sys-gnet-004)、[SYS-GNET-007](../../appendices/Requirements_Catalog.md#sys-gnet-007)、[SYS-GRID-002](../../appendices/Requirements_Catalog.md#sys-grid-002)、[SYS-GSEL-004](../../appendices/Requirements_Catalog.md#sys-gsel-004)、[SYS-GSEL-006](../../appendices/Requirements_Catalog.md#sys-gsel-006)、[SYS-GSEL-013](../../appendices/Requirements_Catalog.md#sys-gsel-013)、[SYS-GSEL-014](../../appendices/Requirements_Catalog.md#sys-gsel-014)、[SYS-OTA-001](../../appendices/Requirements_Catalog.md#sys-ota-001)。

**詳細章：** [II-07_Measurement_Data](../II_GW/II-07_Measurement_Data.md) ／ [I-07_Responsibilities_Constraints](I-07_Responsibilities_Constraints.md) ／ [III-01_Boundary_Contracts](../III_Interfaces/III-01_Boundary_Contracts.md) ／ [IV-07_Isolation_Shared_Resources](../IV_Quality/IV-07_Isolation_Shared_Resources.md)。

**具体的な不足：** [OQ-R6-10-02](I-07_Responsibilities_Constraints.md#oq-r6-10-02)。

<a id="s-fn-015"></a>
### S-FN-015 — 競合・通信断・停止・復旧の協調

通常要求の競合と、障害位置別の残留・失効・復旧を管理する。

**適用条件：** H停止・GW全体停止・ルータ停止を分離

**判断状態：** R6_DESIGN_DRAFT。採用リリース・実装確認・正式USDM対応は未確定。

**実現責任／GW内担当：** GW H/G＋PCS＋ネットワーク＋各サービス。

**機能配賦：** [GW-FN-002](../II_GW/II-02_GW_Functions.md#gw-fn-002) ／ [GW-FN-003](../II_GW/II-02_GW_Functions.md#gw-fn-003) ／ [GW-FN-004](../II_GW/II-02_GW_Functions.md#gw-fn-004) ／ [GW-FN-007](../II_GW/II-02_GW_Functions.md#gw-fn-007) ／ [GW-FN-015](../II_GW/II-02_GW_Functions.md#gw-fn-015) ／ [GW-FN-020](../II_GW/II-02_GW_Functions.md#gw-fn-020) ／ [GW-FN-022](../II_GW/II-02_GW_Functions.md#gw-fn-022) ／ [GW-FN-024](../II_GW/II-02_GW_Functions.md#gw-fn-024) ／ [GW-FN-026](../II_GW/II-02_GW_Functions.md#gw-fn-026) ／ [GW-FN-032](../II_GW/II-02_GW_Functions.md#gw-fn-032)。

**関連SYS要求：** [SYS-AUTH-001](../../appendices/Requirements_Catalog.md#sys-auth-001)、[SYS-AUTH-002](../../appendices/Requirements_Catalog.md#sys-auth-002)、[SYS-CAP-002](../../appendices/Requirements_Catalog.md#sys-cap-002)、[SYS-CFG-001](../../appendices/Requirements_Catalog.md#sys-cfg-001)、[SYS-CFG-002](../../appendices/Requirements_Catalog.md#sys-cfg-002)、[SYS-CFG-004](../../appendices/Requirements_Catalog.md#sys-cfg-004)、[SYS-CFG-005](../../appendices/Requirements_Catalog.md#sys-cfg-005)、[SYS-COEX-001](../../appendices/Requirements_Catalog.md#sys-coex-001)、[SYS-CONST-001](../../appendices/Requirements_Catalog.md#sys-const-001)、[SYS-EMS-001](../../appendices/Requirements_Catalog.md#sys-ems-001)、[SYS-EXPIRY-001](../../appendices/Requirements_Catalog.md#sys-expiry-001)、[SYS-FAULT-001](../../appendices/Requirements_Catalog.md#sys-fault-001)、[SYS-FW-003](../../appendices/Requirements_Catalog.md#sys-fw-003)、[SYS-FW-004](../../appendices/Requirements_Catalog.md#sys-fw-004)、[SYS-GNET-003](../../appendices/Requirements_Catalog.md#sys-gnet-003)、[SYS-GNET-005](../../appendices/Requirements_Catalog.md#sys-gnet-005)、[SYS-GSEL-004](../../appendices/Requirements_Catalog.md#sys-gsel-004)、[SYS-GSEL-005](../../appendices/Requirements_Catalog.md#sys-gsel-005)、[SYS-GSEL-011](../../appendices/Requirements_Catalog.md#sys-gsel-011)、[SYS-GSEL-012](../../appendices/Requirements_Catalog.md#sys-gsel-012)、[SYS-GWOP-001](../../appendices/Requirements_Catalog.md#sys-gwop-001)、[SYS-GWOP-002](../../appendices/Requirements_Catalog.md#sys-gwop-002)、[SYS-ORCH-001](../../appendices/Requirements_Catalog.md#sys-orch-001)、[SYS-OTA-001](../../appendices/Requirements_Catalog.md#sys-ota-001)、[SYS-OTA-002](../../appendices/Requirements_Catalog.md#sys-ota-002)、[SYS-RESP-001](../../appendices/Requirements_Catalog.md#sys-resp-001)、[SYS-RESULT-001](../../appendices/Requirements_Catalog.md#sys-result-001)、[SYS-RESULT-002](../../appendices/Requirements_Catalog.md#sys-result-002)、[SYS-RESULT-003](../../appendices/Requirements_Catalog.md#sys-result-003)、[SYS-RETRY-001](../../appendices/Requirements_Catalog.md#sys-retry-001)、[SYS-SEM-001](../../appendices/Requirements_Catalog.md#sys-sem-001)。

**詳細章：** [II-03_Control_Execution](../II_GW/II-03_Control_Execution.md) ／ [I-06_Usecases](I-06_Usecases.md) ／ [II-04_DER_Load_Control](../II_GW/II-04_DER_Load_Control.md) ／ [III-07_RS485_PCS](../III_Interfaces/III-07_RS485_PCS.md) ／ [III-06_ECHONET_Lite](../III_Interfaces/III-06_ECHONET_Lite.md) ／ [II-05_Advanced_EMS](../II_GW/II-05_Advanced_EMS.md) ／ [II-10_Fault_Alarm_Diagnostics](../II_GW/II-10_Fault_Alarm_Diagnostics.md) ／ [II-08_GW_Grid_Control](../II_GW/II-08_GW_Grid_Control.md) ／ [II-09_Settings_Lifecycle](../II_GW/II-09_Settings_Lifecycle.md) ／ [III-10_Maintenance_Interfaces](../III_Interfaces/III-10_Maintenance_Interfaces.md) ／ [II-11_Firmware_Update](../II_GW/II-11_Firmware_Update.md) ／ [I-08_System_States](I-08_System_States.md)。

**具体的な不足：** [OQ-R6-05-01](../II_GW/II-03_Control_Execution.md#oq-r6-05-01) ／ [OQ-R6-13-01](../II_GW/II-10_Fault_Alarm_Diagnostics.md#oq-r6-13-01)。

<a id="s-fn-016"></a>
### S-FN-016 — 警報・通知・診断

異常と操作結果を記録・通知し、公開範囲内で診断可能にする。

**適用条件：** 情報の鮮度・権限・通知先を個別確定

**判断状態：** R6_DESIGN_DRAFT。採用リリース・実装確認・正式USDM対応は未確定。

**実現責任／GW内担当：** GW＋クラウド／UI＋機器。

**機能配賦：** [GW-FN-008](../II_GW/II-02_GW_Functions.md#gw-fn-008) ／ [GW-FN-009](../II_GW/II-02_GW_Functions.md#gw-fn-009) ／ [GW-FN-016](../II_GW/II-02_GW_Functions.md#gw-fn-016) ／ [GW-FN-017](../II_GW/II-02_GW_Functions.md#gw-fn-017) ／ [GW-FN-019](../II_GW/II-02_GW_Functions.md#gw-fn-019) ／ [GW-FN-022](../II_GW/II-02_GW_Functions.md#gw-fn-022) ／ [GW-FN-025](../II_GW/II-02_GW_Functions.md#gw-fn-025)。

**関連SYS要求：** [SYS-APP-001](../../appendices/Requirements_Catalog.md#sys-app-001)、[SYS-APP-002](../../appendices/Requirements_Catalog.md#sys-app-002)、[SYS-DATA-001](../../appendices/Requirements_Catalog.md#sys-data-001)、[SYS-DATA-002](../../appendices/Requirements_Catalog.md#sys-data-002)、[SYS-GNET-004](../../appendices/Requirements_Catalog.md#sys-gnet-004)、[SYS-GNET-007](../../appendices/Requirements_Catalog.md#sys-gnet-007)、[SYS-GSEL-013](../../appendices/Requirements_Catalog.md#sys-gsel-013)、[SYS-GSEL-014](../../appendices/Requirements_Catalog.md#sys-gsel-014)、[SYS-GWOP-001](../../appendices/Requirements_Catalog.md#sys-gwop-001)、[SYS-GWOP-002](../../appendices/Requirements_Catalog.md#sys-gwop-002)、[SYS-LOG-001](../../appendices/Requirements_Catalog.md#sys-log-001)、[SYS-MEAS-001](../../appendices/Requirements_Catalog.md#sys-meas-001)、[SYS-MEAS-002](../../appendices/Requirements_Catalog.md#sys-meas-002)、[SYS-NORTH-001](../../appendices/Requirements_Catalog.md#sys-north-001)、[SYS-NORTH-002](../../appendices/Requirements_Catalog.md#sys-north-002)、[SYS-NORTH-003](../../appendices/Requirements_Catalog.md#sys-north-003)、[SYS-NORTH-004](../../appendices/Requirements_Catalog.md#sys-north-004)、[SYS-NORTH-005](../../appendices/Requirements_Catalog.md#sys-north-005)、[SYS-NORTH-006](../../appendices/Requirements_Catalog.md#sys-north-006)、[SYS-STATE-001](../../appendices/Requirements_Catalog.md#sys-state-001)、[SYS-STATE-002](../../appendices/Requirements_Catalog.md#sys-state-002)。

**詳細章：** [II-07_Measurement_Data](../II_GW/II-07_Measurement_Data.md) ／ [IV-08_Data_Log_UI_Quality](../IV_Quality/IV-08_Data_Log_UI_Quality.md) ／ [I-07_Responsibilities_Constraints](I-07_Responsibilities_Constraints.md) ／ [III-02_Cloud_GW](../III_Interfaces/III-02_Cloud_GW.md) ／ [II-03_Control_Execution](../II_GW/II-03_Control_Execution.md) ／ [III-05_Remote_App](../III_Interfaces/III-05_Remote_App.md) ／ [II-09_Settings_Lifecycle](../II_GW/II-09_Settings_Lifecycle.md) ／ [III-10_Maintenance_Interfaces](../III_Interfaces/III-10_Maintenance_Interfaces.md) ／ [II-10_Fault_Alarm_Diagnostics](../II_GW/II-10_Fault_Alarm_Diagnostics.md)。

**具体的な不足：** [OQ-R6-20-03](../II_GW/II-10_Fault_Alarm_Diagnostics.md#oq-r6-20-03)。

<a id="s-fn-017"></a>
### S-FN-017 — 履歴の保存・提出・利用

用途別のデータを保持し、期間・品質・欠測を明示して抽出する。

**適用条件：** 保持期間・形式・制度対象は未決

**判断状態：** R6_DESIGN_DRAFT。採用リリース・実装確認・正式USDM対応は未確定。

**実現責任／GW内担当：** GW＋採用するクラウド保存／利用先。

**機能配賦：** [GW-FN-008](../II_GW/II-02_GW_Functions.md#gw-fn-008) ／ [GW-FN-009](../II_GW/II-02_GW_Functions.md#gw-fn-009)。

**関連SYS要求：** [SYS-DATA-001](../../appendices/Requirements_Catalog.md#sys-data-001)、[SYS-DATA-002](../../appendices/Requirements_Catalog.md#sys-data-002)、[SYS-MEAS-001](../../appendices/Requirements_Catalog.md#sys-meas-001)、[SYS-MEAS-002](../../appendices/Requirements_Catalog.md#sys-meas-002)、[SYS-NORTH-006](../../appendices/Requirements_Catalog.md#sys-north-006)、[SYS-STATE-001](../../appendices/Requirements_Catalog.md#sys-state-001)、[SYS-STATE-002](../../appendices/Requirements_Catalog.md#sys-state-002)。

**詳細章：** [II-07_Measurement_Data](../II_GW/II-07_Measurement_Data.md) ／ [IV-08_Data_Log_UI_Quality](../IV_Quality/IV-08_Data_Log_UI_Quality.md)。

**具体的な不足：** [OQ-R6-09-02](../IV_Quality/IV-08_Data_Log_UI_Quality.md#oq-r6-09-02) ／ [OQ-R6-09-03](../II_GW/II-07_Measurement_Data.md#oq-r6-09-03)。

<a id="s-fn-018"></a>
### S-FN-018 — 外部HEMSとの機器公開連携

GWがDevice側として許可する情報・操作を外部HEMSへ提供する。

**適用条件：** 仮想EL公開でRS-485 PCSの取得主体を変更しない

**判断状態：** R6_DESIGN_DRAFT。採用リリース・実装確認・正式USDM対応は未確定。

**実現責任／GW内担当：** 外部HEMS＋GW＋実機対応。

**機能配賦：** [GW-FN-013](../II_GW/II-02_GW_Functions.md#gw-fn-013)。

**関連SYS要求：** [SYS-EL-001](../../appendices/Requirements_Catalog.md#sys-el-001)、[SYS-EL-002](../../appendices/Requirements_Catalog.md#sys-el-002)、[SYS-GNET-012](../../appendices/Requirements_Catalog.md#sys-gnet-012)。

**詳細章：** [III-06_ECHONET_Lite](../III_Interfaces/III-06_ECHONET_Lite.md)。

**具体的な不足：** [OQ-R6-07-02](../III_Interfaces/III-06_ECHONET_Lite.md#oq-r6-07-02)。

<a id="s-fn-019"></a>
### S-FN-019 — 利用者識別・権限・所属管理

4種類の利用者に対して、認可・失効・対象範囲・監査を適用する。

**適用条件：** 4分類は今回確定。具体権限・委譲は未承認

**判断状態：** R6_DESIGN_PLUS_USER_CONFIRMED_ROLE_SET。採用リリース・実装確認・正式USDM対応は未確定。

**実現責任／GW内担当：** 利用者＋GW／クラウド／製造保守の各認可境界。

**機能配賦：** [GW-FN-001](../II_GW/II-02_GW_Functions.md#gw-fn-001) ／ [GW-FN-017](../II_GW/II-02_GW_Functions.md#gw-fn-017) ／ [GW-FN-025](../II_GW/II-02_GW_Functions.md#gw-fn-025) ／ [GW-FN-027](../II_GW/II-02_GW_Functions.md#gw-fn-027) ／ [GW-FN-028](../II_GW/II-02_GW_Functions.md#gw-fn-028) ／ [GW-FN-030](../II_GW/II-02_GW_Functions.md#gw-fn-030)。

**関連SYS要求：** [SYS-APP-003](../../appendices/Requirements_Catalog.md#sys-app-003)、[SYS-BOUND-001](../../appendices/Requirements_Catalog.md#sys-bound-001)、[SYS-CFG-003](../../appendices/Requirements_Catalog.md#sys-cfg-003)、[SYS-GSEL-004](../../appendices/Requirements_Catalog.md#sys-gsel-004)、[SYS-GSEL-006](../../appendices/Requirements_Catalog.md#sys-gsel-006)、[SYS-GSEL-019](../../appendices/Requirements_Catalog.md#sys-gsel-019)、[SYS-GWOP-001](../../appendices/Requirements_Catalog.md#sys-gwop-001)、[SYS-LOG-001](../../appendices/Requirements_Catalog.md#sys-log-001)、[SYS-NORTH-001](../../appendices/Requirements_Catalog.md#sys-north-001)、[SYS-NORTH-002](../../appendices/Requirements_Catalog.md#sys-north-002)、[SYS-NORTH-003](../../appendices/Requirements_Catalog.md#sys-north-003)、[SYS-NORTH-004](../../appendices/Requirements_Catalog.md#sys-north-004)、[SYS-NORTH-005](../../appendices/Requirements_Catalog.md#sys-north-005)、[SYS-NORTH-007](../../appendices/Requirements_Catalog.md#sys-north-007)、[SYS-OTA-001](../../appendices/Requirements_Catalog.md#sys-ota-001)、[SYS-REQ-001](../../appendices/Requirements_Catalog.md#sys-req-001)、[SYS-SEC-001](../../appendices/Requirements_Catalog.md#sys-sec-001)、[SYS-STATE-001](../../appendices/Requirements_Catalog.md#sys-state-001)。

**詳細章：** [II-03_Control_Execution](../II_GW/II-03_Control_Execution.md) ／ [III-02_Cloud_GW](../III_Interfaces/III-02_Cloud_GW.md) ／ [IV-03_Security_Privacy](../IV_Quality/IV-03_Security_Privacy.md) ／ [II-10_Fault_Alarm_Diagnostics](../II_GW/II-10_Fault_Alarm_Diagnostics.md) ／ [IV-08_Data_Log_UI_Quality](../IV_Quality/IV-08_Data_Log_UI_Quality.md) ／ [I-02_Actors_Roles](I-02_Actors_Roles.md) ／ [III-01_Boundary_Contracts](../III_Interfaces/III-01_Boundary_Contracts.md) ／ [IV-07_Isolation_Shared_Resources](../IV_Quality/IV-07_Isolation_Shared_Resources.md) ／ [II-09_Settings_Lifecycle](../II_GW/II-09_Settings_Lifecycle.md) ／ [V-03_Maintenance_Retirement](../V_Lifecycle/V-03_Maintenance_Retirement.md)。

**具体的な不足：** [OQ-R6-01-01](I-02_Actors_Roles.md#oq-r6-01-01) ／ [OQ-R6-27-02](../IV_Quality/IV-03_Security_Privacy.md#oq-r6-27-02)。

<a id="s-fn-020"></a>
### S-FN-020 — 製造・施工・保守・交換・廃棄支援

個体識別から引渡し、交換、所有者変更、消去まで必要な支援を定義する。

**適用条件：** 詳細機能はR6補完対象。製造試験設備等をGW内部と混同しない

**判断状態：** R6_COMPLETION_CANDIDATE。採用リリース・実装確認・正式USDM対応は未確定。

**実現責任／GW内担当：** メーカー／メンテナンス／ユーザ＋GW＋支援基盤。

**機能配賦：** [GW-FN-010](../II_GW/II-02_GW_Functions.md#gw-fn-010) ／ [GW-FN-020](../II_GW/II-02_GW_Functions.md#gw-fn-020) ／ [GW-FN-022](../II_GW/II-02_GW_Functions.md#gw-fn-022) ／ [GW-FN-025](../II_GW/II-02_GW_Functions.md#gw-fn-025) ／ [GW-FN-027](../II_GW/II-02_GW_Functions.md#gw-fn-027) ／ [GW-FN-029](../II_GW/II-02_GW_Functions.md#gw-fn-029) ／ [GW-FN-030](../II_GW/II-02_GW_Functions.md#gw-fn-030) ／ [GW-FN-032](../II_GW/II-02_GW_Functions.md#gw-fn-032)。

**関連SYS要求：** [SYS-APP-003](../../appendices/Requirements_Catalog.md#sys-app-003)、[SYS-CAP-001](../../appendices/Requirements_Catalog.md#sys-cap-001)、[SYS-CAP-002](../../appendices/Requirements_Catalog.md#sys-cap-002)、[SYS-CFG-001](../../appendices/Requirements_Catalog.md#sys-cfg-001)、[SYS-CFG-002](../../appendices/Requirements_Catalog.md#sys-cfg-002)、[SYS-CFG-003](../../appendices/Requirements_Catalog.md#sys-cfg-003)、[SYS-CFG-004](../../appendices/Requirements_Catalog.md#sys-cfg-004)、[SYS-CFG-005](../../appendices/Requirements_Catalog.md#sys-cfg-005)、[SYS-GNET-012](../../appendices/Requirements_Catalog.md#sys-gnet-012)、[SYS-GSEL-011](../../appendices/Requirements_Catalog.md#sys-gsel-011)、[SYS-GSEL-019](../../appendices/Requirements_Catalog.md#sys-gsel-019)、[SYS-GWOP-001](../../appendices/Requirements_Catalog.md#sys-gwop-001)、[SYS-GWOP-002](../../appendices/Requirements_Catalog.md#sys-gwop-002)、[SYS-LOG-001](../../appendices/Requirements_Catalog.md#sys-log-001)、[SYS-NORTH-002](../../appendices/Requirements_Catalog.md#sys-north-002)、[SYS-NORTH-005](../../appendices/Requirements_Catalog.md#sys-north-005)、[SYS-NORTH-007](../../appendices/Requirements_Catalog.md#sys-north-007)、[SYS-OTA-002](../../appendices/Requirements_Catalog.md#sys-ota-002)、[SYS-ROUTE-001](../../appendices/Requirements_Catalog.md#sys-route-001)、[SYS-SEC-001](../../appendices/Requirements_Catalog.md#sys-sec-001)、[SYS-STATE-001](../../appendices/Requirements_Catalog.md#sys-state-001)、[SYS-SVC-001](../../appendices/Requirements_Catalog.md#sys-svc-001)。

**詳細章：** [II-06_Device_Management](../II_GW/II-06_Device_Management.md) ／ [I-05_Configurations](I-05_Configurations.md) ／ [II-09_Settings_Lifecycle](../II_GW/II-09_Settings_Lifecycle.md) ／ [III-10_Maintenance_Interfaces](../III_Interfaces/III-10_Maintenance_Interfaces.md) ／ [II-10_Fault_Alarm_Diagnostics](../II_GW/II-10_Fault_Alarm_Diagnostics.md) ／ [IV-08_Data_Log_UI_Quality](../IV_Quality/IV-08_Data_Log_UI_Quality.md) ／ [IV-03_Security_Privacy](../IV_Quality/IV-03_Security_Privacy.md) ／ [I-02_Actors_Roles](I-02_Actors_Roles.md) ／ [V-01_Manufacturing_Shipping](../V_Lifecycle/V-01_Manufacturing_Shipping.md) ／ [V-02_Commissioning_Handover](../V_Lifecycle/V-02_Commissioning_Handover.md) ／ [V-03_Maintenance_Retirement](../V_Lifecycle/V-03_Maintenance_Retirement.md) ／ [I-08_System_States](I-08_System_States.md)。

**具体的な不足：** [OQ-R6-26-01](../V_Lifecycle/V-01_Manufacturing_Shipping.md#oq-r6-26-01) ／ [OQ-R6-26-05](../V_Lifecycle/V-03_Maintenance_Retirement.md#oq-r6-26-05) ／ [OQ-R6-26-06](../V_Lifecycle/V-03_Maintenance_Retirement.md#oq-r6-26-06)。

<a id="s-fn-021"></a>
### S-FN-021 — 通信・周辺機器の構成と復旧

通信方式・USB等の採用条件、接続・故障・復旧を管理する。

**適用条件：** IPv4/IPv6・Wi-SUN・USBの全対応を未確認で宣言しない

**判断状態：** R6_CARRYOVER_SCOPE_TBD。採用リリース・実装確認・正式USDM対応は未確定。

**実現責任／GW内担当：** GW＋宅内ルータ＋周辺機器。

**機能配賦：** [GW-FN-021](../II_GW/II-02_GW_Functions.md#gw-fn-021) ／ [GW-FN-026](../II_GW/II-02_GW_Functions.md#gw-fn-026) ／ [GW-FN-031](../II_GW/II-02_GW_Functions.md#gw-fn-031)。

**関連SYS要求：** [SYS-CAP-001](../../appendices/Requirements_Catalog.md#sys-cap-001)、[SYS-CFG-006](../../appendices/Requirements_Catalog.md#sys-cfg-006)、[SYS-EXPIRY-001](../../appendices/Requirements_Catalog.md#sys-expiry-001)、[SYS-FAULT-001](../../appendices/Requirements_Catalog.md#sys-fault-001)、[SYS-GNET-005](../../appendices/Requirements_Catalog.md#sys-gnet-005)、[SYS-GNET-006](../../appendices/Requirements_Catalog.md#sys-gnet-006)、[SYS-MIG-002](../../appendices/Requirements_Catalog.md#sys-mig-002)、[SYS-RETRY-001](../../appendices/Requirements_Catalog.md#sys-retry-001)、[SYS-SEC-001](../../appendices/Requirements_Catalog.md#sys-sec-001)。

**詳細章：** [II-09_Settings_Lifecycle](../II_GW/II-09_Settings_Lifecycle.md) ／ [III-09_Network_Peripherals](../III_Interfaces/III-09_Network_Peripherals.md) ／ [II-10_Fault_Alarm_Diagnostics](../II_GW/II-10_Fault_Alarm_Diagnostics.md) ／ [I-08_System_States](I-08_System_States.md) ／ [II-06_Device_Management](../II_GW/II-06_Device_Management.md)。

**具体的な不足：** [OQ-R6-07-03](../III_Interfaces/III-09_Network_Peripherals.md#oq-r6-07-03)。

<a id="open-questions"></a>
## Open Questions — 本ノートの完成に必要な確認


### 他章で回答する関連質問

| OQ・正本章 | 残る判断 | 完了条件 |
|---|---|---|
| [OQ-R6-01-01](I-02_Actors_Roles.md#oq-r6-01-01) | 4分類の名称はユーザ／メンテナンス／メーカー／開発者で確定。権限・委任・対象・環境・承認等は未決。 | ロール×利用局面×操作範囲表を承認し、[旧20章の再配置先](../../appendices/Chapter_Migration_Map.md#old-ch-20)、[旧26章の再配置先](../../appendices/Chapter_Migration_Map.md#old-ch-26)、[旧27章の再配置先](../../appendices/Chapter_Migration_Map.md#old-ch-27)へ対応付ける。 |
| [OQ-R6-01-02](I-01_Purpose_Scope.md#oq-r6-01-02) | 既存運転維持、宅内監視、リモート操作、高度エネマネについて、どの条件で何を達成すれば商品として合格とするか。非対応用途は何か。 | 目的→機能→成功シナリオの対応表を作り、条件なしの省エネ率等を保証しない成功基準を[旧17章の再配置先](../../appendices/Chapter_Migration_Map.md#old-ch-17)へ登録する。 |
| [OQ-R6-02-02](I-04_System_Context.md#oq-r6-02-02) | 直接無線Webはどの無線方式を使うか。ルータ接続と同時利用できるか。クラウド断でも利用できる画面と認証条件は何か。 | 直接接続/宅内ルータ/リモートの構成別機能表と到達・再接続の確認方法を定義する。 |
| [OQ-R6-04-01](../II_GW/II-02_GW_Functions.md#oq-r6-04-01) | 既存GWの全機能は何か。高度エネマネ追加後に維持・変更・廃止する機能と初回採用機能はどれか。候補ではなく採用済みとできる根拠は何か。 | 機能一覧を既存仕様・コード調査と突合し、候補機能の採否・対象リリース・非対応理由を機能表で承認する。 |
| [OQ-R6-04-02](I-05_Configurations.md#oq-r6-04-02) | 初回対応するPCS・空調・給湯・計測器・USB機器はどの型式/版か。全機能対応、観測のみ、非対応をどの組合せで保証するか。 | 機器プロファイルと製品構成表に実型式・版・操作・制限・確認資料を登録する。 |
| [OQ-R6-04-03](../II_GW/II-06_Device_Management.md#oq-r6-04-03) | 探索した機器をいつ登録し、書込を許すか。交換・アドレス変更・多重IF・GW仮想EL公開をどう識別し、旧要求と履歴を扱うか。 | 探索/登録/交換/解除のUCと重複判定・書込解禁条件を定義し、旧設定移行の判定例を用意する。 |
| [OQ-R6-05-01](../II_GW/II-03_Control_Execution.md#oq-r6-05-01) | 利用者、本体操作、各クラウド、既存運転、高度エネマネが競合するとき、操作別の優先順位と同順位処理をどう決めるか。途中実行の取消しをどこまで保証するか。 | 通常操作の優先表、同時実行許可表、要求失効と補償の決定表を機器能力と対応付ける。 |
| [OQ-R6-07-01](../III_Interfaces/III-07_RS485_PCS.md#oq-r6-07-01) | 既存PCSの実プロトコル、電文/レジスタ、応答の意味、局数・配線条件は何か。通常操作とG側必須通信をどの送信者・予算で管理するか。 | PCS別接続仕様の版と電文対応を確定し、RS-485全書込点・最終送信境界・通信負荷表を登録する。 |
| [OQ-R6-07-02](../III_Interfaces/III-06_ECHONET_Lite.md#oq-r6-07-02) | 機器ごとのEL/AIF版・実装プロパティ・更新間隔は何か。GWのDevice側は何を公開し、RS-485資源や他社PCSとの対応と不可応答をどう定義するか。 | 対応するEL機器と操作・観測表を埋め、Controller/Device共存、公開能力の上限、未対応応答を確認する。 |
| [OQ-R6-07-03](../III_Interfaces/III-09_Network_Peripherals.md#oq-r6-07-03) | IPv4/IPv6、Wi-SUN、USB通信ドングル、USBバックアップ等をどの製品で採用するか。経路優先度、抜去・ハング時動作、認証あり/なし混在をどう規定するか。 | 持越し要求を採用/対象外へ仕分け、採用品の媒体・型式・状態遷移・資源上限を接続プロファイルへ登録する。 |
| [OQ-R6-08-01](../II_GW/II-05_Advanced_EMS.md#oq-r6-08-01) | 自家消費、料金、ピーク、充電期限のどの戦略を初回採用するか。機器構成・入力欠損・手動変更に応じた開始/解除/再開条件は何か。 | 戦略ごとの採否と機能仕様を機能表・UCへ展開し、入力/結果/異常分岐の未定を除く。 |
| [OQ-R6-08-02](../II_GW/II-05_Advanced_EMS.md#oq-r6-08-02) | 採用戦略の予測データ・料金データはどこから取得し、どの品質まで使うか。最適解が得られない/期限に間に合わない場合、どの代替動作と通知にするか。 | 戦略入力辞書、計画・再計画条件、未達時動作、評価シナリオと受入指標を確定する。 |
| [OQ-R6-08-03](../II_GW/II-04_DER_Load_Control.md#oq-r6-08-03) | 空調・給湯・蓄電池等の何を操作するか。設定範囲、快適性、終了時の運転残留、本体操作尊重を機種別にどう制約するか。 | DPC/FLCの操作別機能表を機器プロファイルと安全評価へ対応付け、未対応機能を実装済みと扱わない。 |
| [OQ-R6-09-01](../II_GW/II-07_Measurement_Data.md#oq-r6-09-01) | 公開・保存・制御利用する全データ項目は何か。AC/DC、電力/電力量、符号・精度・時刻・欠測・推定の表現をどう統一するか。 | 実項目ごとの辞書に型・単位・基準点・所有者・品質・利用先を記入し、二重計上をレビューする。 |
| [OQ-R6-09-02](../IV_Quality/IV-08_Data_Log_UI_Quality.md#oq-r6-09-02) | どの項目をどの粒度/期間保存するか。電断で許す損失、積算リセット・機器交換、容量枯渇時の削除・警報はどうするか。 | 用途別保持表、容量・寿命計算、電断/満杯/時刻補正の期待結果を定義する。 |
| [OQ-R6-09-03](../II_GW/II-07_Measurement_Data.md#oq-r6-09-03) | オフライン中の履歴を何件/期間保持し、上位とどう整合するか。利用者へ出せる項目・形式と、修理/所有者変更で消す範囲は何か。 | 同期・抽出・消去仕様をデータ項目単位で確定し、欠測と取得不能をデータ0としないテストを定める。 |
| [OQ-R6-10-01](../V_Lifecycle/V-04_Compliance.md#oq-r6-10-01) | 対象エリア・連系契約・設備範囲・正式仕様の版は何か。取得・保持・適用・期限切れ・通信異常時の値と条件は何か。 | 選択方式ごとの系統接続プロファイルに正式資料・適用範囲・値・確認者を登録する。 |
| [OQ-R6-10-02](I-07_Responsibilities_Constraints.md#oq-r6-10-02) | 対象PCSの通常操作で出力制約や保護を上書きできない根拠は何か。独立計測・保護復帰・必要通信を誰が担い、H停止時に何を維持するか。 | メーカー説明・機能分担・許可操作・適用評価の記録をそろえ、必要な受入条件を[旧17章の再配置先](../../appendices/Chapter_Migration_Map.md#old-ch-17)へ配賦する。 |
| [OQ-R6-12-02](../II_GW/II-09_Settings_Lifecycle.md#oq-r6-12-02) | 製品が管理する全設定キーと既定値は何か。製造/施工/通常/系統保守の変更権限と、機能・機種別の有効条件は何か。 | 設定項目一覧へ実キー・型・範囲・既定値・保存先・変更条件を登録し、G側項目を一般H設定から区別する。 |
| [OQ-R6-12-03](../II_GW/II-09_Settings_Lifecycle.md#oq-r6-12-03) | 同時変更や高優先度運転中の設定を、何秒/どの状態まで保留するか。緊急復旧で割り込める操作と部分反映の回復手順は何か。 | 操作別の反映条件、世代競合、保留期限、部分反映・緊急変更の決定表と確認方法を確定する。 |
| [OQ-R6-12-04](../II_GW/II-09_Settings_Lifecycle.md#oq-r6-12-04) | 一般設定バックアップと初期化で何を保存・削除するか。G側FW/時計/設定/資格情報をどう除外し、異機種・旧版への復元をどう判定するか。 | 対象項目と版互換表、初期化種別、復元前検査・失敗後状態を定義し、製造・廃棄と整合させる。 |
| [OQ-R6-13-01](../II_GW/II-10_Fault_Alarm_Diagnostics.md#oq-r6-13-01) | 全故障の検出条件・復帰条件・再試行の上限は何か。同じ故障の頻発、正常応答の一時回復、遅延応答をどう扱うか。 | 故障・警報対応表と復旧の決定表を作り、各閾値と通知・試験IDを結び付ける。 |
| [OQ-R6-17-02](../V_Lifecycle/V-06_Verification_Validation.md#oq-r6-17-02) | 自家消費、充電期限、快適性、監視・操作について、どの住宅条件とシナリオで利用目的の達成を確認するか。未達や制限の説明が適切なことをどう判定するか。 | 目的別Validationシナリオを製品企画・利用者代表の確認へ回し、指標・条件・受入者を決める。 |
| [OQ-R6-19-01](../V_Lifecycle/V-07_Trace_Open_Questions.md#oq-r6-19-01) | 正式USDMの正本・IDは何か。124件のSYSと今回の補完項目を誰が要求へ対応付け、重複・不足・対象外を承認するか。 | USDM→機能→SYS/補完項目→設計→検証の対応を版付きで完成し、未記入を適合扱いしない。 |
| [OQ-R6-20-01](../III_Interfaces/III-02_Cloud_GW.md#oq-r6-20-01) | 上位管理が読み書きする実項目と内部操作はどれか。プロトコル、公開schema、役割権限、完了通知・エラーをどう固定するか。 | 16件の論理IFを実契約へ展開し、公開操作台帳を実項目・権限・状態・結果へ対応付ける。 |
| [OQ-R6-20-02](../IV_Quality/IV-08_Data_Log_UI_Quality.md#oq-r6-20-02) | 宅内Web・スマートフォン・本体表示で提供する画面と項目は何か。対応端末、更新周期、色以外の区別、重要操作確認、多言語等の適用をどう決めるか。 | 画面×項目×操作×ロール表と対応端末表、利用者タスクの受入条件を確定する。ピクセル設計はUI詳細へ配賦する。 |
| [OQ-R6-20-03](../II_GW/II-10_Fault_Alarm_Diagnostics.md#oq-r6-20-03) | 通信断、出力制限、Unknown、更新失敗、保存異常等をどの警報として誰へ通知するか。確認・抑止・再通知・解除の条件と優先順位は何か。 | 警報台帳を故障ID・UI・上位イベントへ対応付け、確認済みが制約解除を意味しない条件を明記する。 |
| [OQ-R6-20-04](../II_GW/II-11_Firmware_Update.md#oq-r6-20-04) | FW配信が扱う対象はH側のみか、独立G保守を含む別配布か。画像形式・検証・適用条件・旧版復帰と各画面の成功判定をどう定めるか。 | 更新プロファイルを画像/対象/版/認可/段階/復旧条件で確定し、一般H更新からG変更を除外する。 |
| [OQ-R6-21-01](I-05_Configurations.md#oq-r6-21-01) | EL接続PCSの自律取得能力・プロトコル・資格情報の管理仕様は何か。RS-485のGW管理と併せて、どの型式/版で実経路・公開状態を確認できるか。 | 機器接続別の取得プロファイルと管理主体、公開項目の根拠を登録する。非公開はNOT_EXPOSEDと明記する。 |
| [OQ-R6-26-01](../V_Lifecycle/V-01_Manufacturing_Shipping.md#oq-r6-26-01) | 個体IDと鍵/証明書をどの工程で投入し、再作業・不良品・重複をどう扱うか。出荷時に無効にする製造/開発機能と確認方法は何か。 | 製造プロファイルに投入主体・識別・秘密管理・再作業・閉鎖条件を記載し、手順書ID/版へ配賦する。 |
| [OQ-R6-26-05](../V_Lifecycle/V-03_Maintenance_Retirement.md#oq-r6-26-05) | GW/PCS/計測器交換、移設、所有者変更で、何のIDとデータを継承し何を失効させるか。G側構成・資格の再設定と検収は誰が行うか。 | 交換/移設/所有者変更のデータ・資格・接続移行表と再試運転条件を記録する。 |
| [OQ-R6-26-06](../V_Lifecycle/V-03_Maintenance_Retirement.md#oq-r6-26-06) | 廃棄・返却でどの秘密・履歴・所属情報を消すか。起動不能やオフラインで消去/失効ができない場合の隔離・確認・責任は何か。 | 消去・失効・廃止のシステム機能と完了記録を規定し、廃棄手順・プライバシー要求へ配賦する。 |
| [OQ-R6-27-02](../IV_Quality/IV-03_Security_Privacy.md#oq-r6-27-02) | 各資格情報の生成者・保存先・寿命・更新・失効・漏えい復旧をどう定めるか。時刻無効・上位断中の検証とG側資格の独立管理はどうするか。 | 鍵/証明書/アカウントのライフサイクル表と失効・復旧試験条件を製造/運用文書へ対応付ける。 |
