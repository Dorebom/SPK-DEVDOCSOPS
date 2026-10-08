---
title: "SPK-GW製品の機能（要件）一覧"
document_id: "SPKGW-SYS-II-02"
revision: "R8"
updated: 2026-10-07
status: DRAFT_FOR_REVIEW
part: "II"
---

<a id="ii-02"></a>
# II-02 SPK-GW製品の機能（要件）一覧

[全体MOCへ](../../00_MOC.md#part-ii)

**本章の対象：** GW32機能群、全体機能への対応、既存・追加・将来の採否。

**記載区分：** 既存R7の有効な記述とR6補完項を再配置。章構成・読み分けの案以外に、新しい実装・権限・数値・適合を確定していない。旧版に由来する具体値や規格参照は当時の確認範囲を引き継ぐ。

## 本章の責務と他章との境界

GW製品自身が担当する32機能群を本章で一覧表示する。各行は全体機能ID、担当責務、関連SYS要求、適用条件、OQへ接続する。機能IDは要求IDやクラス／プロセス名の置換ではない。

認証・認可、検証、ログ等の**非機能要求を実現する具体機能**もここに含める。IVは品質目標・共通制約を所有し、本章の機能記述と参照関係を持つ。

## SPK-GW製品の機能一覧（32機能群）

| ID | 機能・要求の要約 | 実現責任／GW内担当 | 対応する機能 |
|---|---|---|---|
| [GW-FN-001](#gw-fn-001) | **要求受付・認証認可・用途別振分け**：操作主体・対象・期限・重複を確認し、通常制御／設定／GW内部操作／情報取得／更新へ振り分ける。 | H側の境界API・Usecase | [S-FN-002](../I_System/I-03_System_Functions.md#s-fn-002)、[S-FN-003](../I_System/I-03_System_Functions.md#s-fn-003)、[S-FN-004](../I_System/I-03_System_Functions.md#s-fn-004)、[S-FN-005](../I_System/I-03_System_Functions.md#s-fn-005)、[S-FN-009](../I_System/I-03_System_Functions.md#s-fn-009)、[S-FN-010](../I_System/I-03_System_Functions.md#s-fn-010)、[S-FN-019](../I_System/I-03_System_Functions.md#s-fn-019) |
| [GW-FN-002](#gw-fn-002) | **通常制御権・競合調停**：資源・変換グループの権限、優先関係、世代、期限を管理する。 | H側 Control Arbiter | [S-FN-004](../I_System/I-03_System_Functions.md#s-fn-004)、[S-FN-005](../I_System/I-03_System_Functions.md#s-fn-005)、[S-FN-006](../I_System/I-03_System_Functions.md#s-fn-006)、[S-FN-015](../I_System/I-03_System_Functions.md#s-fn-015) |
| [GW-FN-003](#gw-fn-003) | **複数機器の実行進行・補償**：実行順序・部分成功・取消し・補償を一つの所有者で扱い、必要なら再計画へ戻す。 | H側 Energy Orchestrator | [S-FN-004](../I_System/I-03_System_Functions.md#s-fn-004)、[S-FN-005](../I_System/I-03_System_Functions.md#s-fn-005)、[S-FN-006](../I_System/I-03_System_Functions.md#s-fn-006)、[S-FN-007](../I_System/I-03_System_Functions.md#s-fn-007)、[S-FN-015](../I_System/I-03_System_Functions.md#s-fn-015) |
| [GW-FN-004](#gw-fn-004) | **DERの通常操作・達成確認**：許可済みDER要求を機器別操作系列へ展開し、受理・達成・制限・不明を区別する。 | H側 DER Power Controller | [S-FN-004](../I_System/I-03_System_Functions.md#s-fn-004)、[S-FN-006](../I_System/I-03_System_Functions.md#s-fn-006)、[S-FN-007](../I_System/I-03_System_Functions.md#s-fn-007)、[S-FN-015](../I_System/I-03_System_Functions.md#s-fn-015) |
| [GW-FN-005](#gw-fn-005) | **空調・給湯等の負荷操作**：機器側安全・本体設定・利用可能能力を尊重して、許可済み負荷操作と結果確認を行う。 | H側 Flexible Load Controller | [S-FN-005](../I_System/I-03_System_Functions.md#s-fn-005)、[S-FN-006](../I_System/I-03_System_Functions.md#s-fn-006)、[S-FN-007](../I_System/I-03_System_Functions.md#s-fn-007) |
| [GW-FN-006](#gw-fn-006) | **高度エネマネの計画生成**：計測・利用者条件・利用可能能力から運転計画を生成する。自家消費・料金・購入電力・充電期限等の採否は未決。 | H側 Advanced EMS | [S-FN-006](../I_System/I-03_System_Functions.md#s-fn-006) |
| [GW-FN-007](#gw-fn-007) | **実績評価・再計画・入力不足時縮退**：実績・機器離脱・制約変化を評価し、再計画又は明示した縮退へ移る。 | H側 Advanced EMS／Orchestrator | [S-FN-007](../I_System/I-03_System_Functions.md#s-fn-007)、[S-FN-015](../I_System/I-03_System_Functions.md#s-fn-015) |
| [GW-FN-008](#gw-fn-008) | **計測・状態の取得正規化**：単位・符号・計測点・鮮度・品質を保持し、同一設備や量を二重計上しない。 | H側 Measurement／Device State | [S-FN-001](../I_System/I-03_System_Functions.md#s-fn-001)、[S-FN-007](../I_System/I-03_System_Functions.md#s-fn-007)、[S-FN-016](../I_System/I-03_System_Functions.md#s-fn-016)、[S-FN-017](../I_System/I-03_System_Functions.md#s-fn-017) |
| [GW-FN-009](#gw-fn-009) | **履歴保存・抽出・上位同期**：短期／長期／監査の用途別保存、欠測を含む抽出と再同期を行う。 | H側 Data／Telemetry | [S-FN-001](../I_System/I-03_System_Functions.md#s-fn-001)、[S-FN-003](../I_System/I-03_System_Functions.md#s-fn-003)、[S-FN-016](../I_System/I-03_System_Functions.md#s-fn-016)、[S-FN-017](../I_System/I-03_System_Functions.md#s-fn-017) |
| [GW-FN-010](#gw-fn-010) | **機器探索・登録・識別・能力管理**：物理装置、資源、接続、機器オブジェクト、機器版の対応を管理し、不明能力の推測書込みをしない。 | H側 Device Inventory／Adapter | [S-FN-004](../I_System/I-03_System_Functions.md#s-fn-004)、[S-FN-005](../I_System/I-03_System_Functions.md#s-fn-005)、[S-FN-008](../I_System/I-03_System_Functions.md#s-fn-008)、[S-FN-020](../I_System/I-03_System_Functions.md#s-fn-020) |
| [GW-FN-011](#gw-fn-011) | **RS-485 PCS通常操作・状態通信**：既存通常操作と状態取得を維持し、G側必須指令との送信所有・負荷・非迂回契約に従って通信する。 | H側要求元＋G側／固定PCS通信所有者 | [S-FN-004](../I_System/I-03_System_Functions.md#s-fn-004)、[S-FN-008](../I_System/I-03_System_Functions.md#s-fn-008)、[S-FN-012](../I_System/I-03_System_Functions.md#s-fn-012) |
| [GW-FN-012](#gw-fn-012) | **ECHONET Lite Controller**：H側LAN→宅内LAN/AP→PCS・空調・給湯・計測器のEL機器IFと、通常操作・観測の要求応答を行う。 | H側 ECHONET Lite Controller／Adapter | [S-FN-001](../I_System/I-03_System_Functions.md#s-fn-001)、[S-FN-004](../I_System/I-03_System_Functions.md#s-fn-004)、[S-FN-005](../I_System/I-03_System_Functions.md#s-fn-005)、[S-FN-008](../I_System/I-03_System_Functions.md#s-fn-008) |
| [GW-FN-013](#gw-fn-013) | **ECHONET Lite Device側公開**：外部HEMSへ許可する機器情報・操作を公開し、内部の実機対応と応答の意味を保持する。 | H側 ECHONET Lite Device Adapter | [S-FN-018](../I_System/I-03_System_Functions.md#s-fn-018) |
| [GW-FN-014](#gw-fn-014) | **GW G側スケジュール取得・管理**：宅内ルータ経由で出力制御情報を取得・検証・保存し、適用時刻・有効性・資格情報を管理する。 | GW G側の出力制御機能 | [S-FN-012](../I_System/I-03_System_Functions.md#s-fn-012) |
| [GW-FN-015](#gw-fn-015) | **GW G側の出力制御指示・必須監視**：適用制約に従いRS-485 PCSへ指示し、必要な状態・通信異常を監視する。 | GW G側＋確認済みPCS実行契約 | [S-FN-012](../I_System/I-03_System_Functions.md#s-fn-012)、[S-FN-015](../I_System/I-03_System_Functions.md#s-fn-015) |
| [GW-FN-016](#gw-fn-016) | **PCS側の出力制御・保護状態の参照**：提供可能な制約・状態だけを参照する。非公開は不明とし、EL PCSの取得・適用やPCS保護そのものを代行しない。 | H側の観測・公開View | [S-FN-001](../I_System/I-03_System_Functions.md#s-fn-001)、[S-FN-013](../I_System/I-03_System_Functions.md#s-fn-013)、[S-FN-014](../I_System/I-03_System_Functions.md#s-fn-014)、[S-FN-016](../I_System/I-03_System_Functions.md#s-fn-016) |
| [GW-FN-017](#gw-fn-017) | **上位管理・監視サーバ接続**：認可された要求を用途別に配送し、状態・結果・内部情報の許可項目を公開する。 | H側 Northbound Adapter／API | [S-FN-003](../I_System/I-03_System_Functions.md#s-fn-003)、[S-FN-009](../I_System/I-03_System_Functions.md#s-fn-009)、[S-FN-010](../I_System/I-03_System_Functions.md#s-fn-010)、[S-FN-016](../I_System/I-03_System_Functions.md#s-fn-016)、[S-FN-019](../I_System/I-03_System_Functions.md#s-fn-019) |
| [GW-FN-018](#gw-fn-018) | **宅内Web UI提供・ローカルAPI**：直接無線又は宅内ルータ経由の端末に、基本監視・許可操作を提供する。 | H側 Web／Local API | [S-FN-002](../I_System/I-03_System_Functions.md#s-fn-002) |
| [GW-FN-019](#gw-fn-019) | **リモートアプリ用状態・結果連携**：GWはクラウドへ状態・操作結果を返す。スマートフォン画面やアプリ実装そのものをGW内機能にしない。 | H側上位API／クラウド向け公開View | [S-FN-003](../I_System/I-03_System_Functions.md#s-fn-003)、[S-FN-016](../I_System/I-03_System_Functions.md#s-fn-016) |
| [GW-FN-020](#gw-fn-020) | **設定管理・変更調停**：設定の希望・保存・有効状態、世代競合、反映可否、部分反映、通常と緊急復旧を区別する。 | H側 Configuration／各状態所有者 | [S-FN-009](../I_System/I-03_System_Functions.md#s-fn-009)、[S-FN-015](../I_System/I-03_System_Functions.md#s-fn-015)、[S-FN-020](../I_System/I-03_System_Functions.md#s-fn-020) |
| [GW-FN-021](#gw-fn-021) | **ネットワーク設定の変更・到達性復旧**：接続設定を変更し、適用結果と到達性を確認して規定された復旧へ移る。 | H側の認可されたNetwork Config | [S-FN-009](../I_System/I-03_System_Functions.md#s-fn-009)、[S-FN-021](../I_System/I-03_System_Functions.md#s-fn-021) |
| [GW-FN-022](#gw-fn-022) | **内部機能操作・ライフサイクルJob**：許可リスト内の探索・開始停止・再起動・診断等をJobとして処理し、高影響操作を調整する。 | H側 Lifecycle／Operation Service | [S-FN-010](../I_System/I-03_System_Functions.md#s-fn-010)、[S-FN-015](../I_System/I-03_System_Functions.md#s-fn-015)、[S-FN-016](../I_System/I-03_System_Functions.md#s-fn-016)、[S-FN-020](../I_System/I-03_System_Functions.md#s-fn-020) |
| [GW-FN-023](#gw-fn-023) | **FW取得・配布物検証**：配信・承認・適用を分け、対象・完全性・互換性・系列を確認する。 | H側 Update Manager（対象領域は個別管理） | [S-FN-011](../I_System/I-03_System_Functions.md#s-fn-011) |
| [GW-FN-024](#gw-fn-024) | **FW適用・稼働確認・復旧**：許可された更新を実行し、永続状態に基づいて復帰・旧要求照合を行う。H更新にG更新を混入させない。 | H側 Update Manager／独立したG更新の境界 | [S-FN-011](../I_System/I-03_System_Functions.md#s-fn-011)、[S-FN-015](../I_System/I-03_System_Functions.md#s-fn-015) |
| [GW-FN-025](#gw-fn-025) | **警報・監査・診断情報の公開**：故障・操作・品質・相関情報を記録し、許可された警報・診断情報を通知・抽出する。 | H側 Logging／Diagnostics／Telemetry | [S-FN-016](../I_System/I-03_System_Functions.md#s-fn-016)、[S-FN-019](../I_System/I-03_System_Functions.md#s-fn-019)、[S-FN-020](../I_System/I-03_System_Functions.md#s-fn-020) |
| [GW-FN-026](#gw-fn-026) | **故障検出・再接続・結果再照合**：WAN/LAN/GW/RS-485等の障害位置を区別し、要求残留・期限・重複を照合して縮退・復旧する。 | H側とG側それぞれの障害所有者 | [S-FN-007](../I_System/I-03_System_Functions.md#s-fn-007)、[S-FN-015](../I_System/I-03_System_Functions.md#s-fn-015)、[S-FN-021](../I_System/I-03_System_Functions.md#s-fn-021) |
| [GW-FN-027](#gw-fn-027) | **資格情報・所属・失効・認可の管理**：操作者と配送主体を区別し、所属変更・資格情報の更新失効・環境と対象範囲に従ってアクセスを制限する。 | GW各認可境界／資格情報所有者 | [S-FN-019](../I_System/I-03_System_Functions.md#s-fn-019)、[S-FN-020](../I_System/I-03_System_Functions.md#s-fn-020) |
| [GW-FN-028](#gw-fn-028) | **H/G境界の限定操作・不正入力拒否**：通常APIから保護設定・系統スケジュール原本等へ迂回させず、専用保守と通常権限を分ける。 | H/G境界と最終通常送信境界 | [S-FN-012](../I_System/I-03_System_Functions.md#s-fn-012)、[S-FN-013](../I_System/I-03_System_Functions.md#s-fn-013)、[S-FN-014](../I_System/I-03_System_Functions.md#s-fn-014)、[S-FN-019](../I_System/I-03_System_Functions.md#s-fn-019) |
| [GW-FN-029](#gw-fn-029) | **製造初期化・施工・試運転の機器側支援**：個体識別・初期設定・登録・引渡し確認に必要な機器側機能を定義する。詳細機能はR6補完対象。 | GW製造／施工用の限定機能（採否未決） | [S-FN-008](../I_System/I-03_System_Functions.md#s-fn-008)、[S-FN-020](../I_System/I-03_System_Functions.md#s-fn-020) |
| [GW-FN-030](#gw-fn-030) | **バックアップ・初期化・交換・消去**：設定復元の境界を保ち、交換・所有者変更・廃棄で対象データと資格を整理する。 | H側Config／保守・個別G保守の境界 | [S-FN-009](../I_System/I-03_System_Functions.md#s-fn-009)、[S-FN-019](../I_System/I-03_System_Functions.md#s-fn-019)、[S-FN-020](../I_System/I-03_System_Functions.md#s-fn-020) |
| [GW-FN-031](#gw-fn-031) | **複数通信・USB等の接続管理**：IPv4/IPv6・Wi-SUN・USB等の持越し要求について、搭載・有効・接続・認証・故障を区別する。 | GW通信基盤／Transport／Security Adapter | [S-FN-008](../I_System/I-03_System_Functions.md#s-fn-008)、[S-FN-021](../I_System/I-03_System_Functions.md#s-fn-021) |
| [GW-FN-032](#gw-fn-032) | **起動・停止・操作開始条件の管理**：設定・時計・機器・旧要求の照合結果に応じ、監視・通常制御・自律制御を段階的に許可する。 | H側／G側の独立したLifecycle | [S-FN-015](../I_System/I-03_System_Functions.md#s-fn-015)、[S-FN-020](../I_System/I-03_System_Functions.md#s-fn-020) |

## 機能別の適用・根拠カード

<a id="gw-fn-001"></a>
### GW-FN-001 — 要求受付・認証認可・用途別振分け

操作主体・対象・期限・重複を確認し、通常制御／設定／GW内部操作／情報取得／更新へ振り分ける。

**適用条件：** 対象機器・版・操作・状態・数値の確定後に適用

**判断状態：** R6_DESIGN_DRAFT。採用リリース・実装確認・正式USDM対応は未確定。

**実現責任／GW内担当：** H側の境界API・Usecase。

**機能配賦：** [S-FN-002](../I_System/I-03_System_Functions.md#s-fn-002) ／ [S-FN-003](../I_System/I-03_System_Functions.md#s-fn-003) ／ [S-FN-004](../I_System/I-03_System_Functions.md#s-fn-004) ／ [S-FN-005](../I_System/I-03_System_Functions.md#s-fn-005) ／ [S-FN-009](../I_System/I-03_System_Functions.md#s-fn-009) ／ [S-FN-010](../I_System/I-03_System_Functions.md#s-fn-010) ／ [S-FN-019](../I_System/I-03_System_Functions.md#s-fn-019)。

**関連SYS要求：** [SYS-REQ-001](../../appendices/Requirements_Catalog.md#sys-req-001)、[SYS-NORTH-001](../../appendices/Requirements_Catalog.md#sys-north-001)、[SYS-NORTH-002](../../appendices/Requirements_Catalog.md#sys-north-002)、[SYS-NORTH-007](../../appendices/Requirements_Catalog.md#sys-north-007)。

**詳細章：** [II-03_Control_Execution](II-03_Control_Execution.md) ／ [III-02_Cloud_GW](../III_Interfaces/III-02_Cloud_GW.md) ／ [IV-03_Security_Privacy](../IV_Quality/IV-03_Security_Privacy.md)。

**具体的な不足：** [OQ-R6-20-01](../III_Interfaces/III-02_Cloud_GW.md#oq-r6-20-01) ／ [OQ-R6-27-01](../IV_Quality/IV-03_Security_Privacy.md#oq-r6-27-01)。

<a id="gw-fn-002"></a>
### GW-FN-002 — 通常制御権・競合調停

資源・変換グループの権限、優先関係、世代、期限を管理する。

**適用条件：** 対象機器・版・操作・状態・数値の確定後に適用

**判断状態：** R6_DESIGN_DRAFT。採用リリース・実装確認・正式USDM対応は未確定。

**実現責任／GW内担当：** H側 Control Arbiter。

**機能配賦：** [S-FN-004](../I_System/I-03_System_Functions.md#s-fn-004) ／ [S-FN-005](../I_System/I-03_System_Functions.md#s-fn-005) ／ [S-FN-006](../I_System/I-03_System_Functions.md#s-fn-006) ／ [S-FN-015](../I_System/I-03_System_Functions.md#s-fn-015)。

**関連SYS要求：** [SYS-AUTH-001](../../appendices/Requirements_Catalog.md#sys-auth-001)、[SYS-AUTH-002](../../appendices/Requirements_Catalog.md#sys-auth-002)、[SYS-COEX-001](../../appendices/Requirements_Catalog.md#sys-coex-001)。

**詳細章：** [II-03_Control_Execution](II-03_Control_Execution.md)。

**具体的な不足：** [OQ-R6-05-01](II-03_Control_Execution.md#oq-r6-05-01)。

<a id="gw-fn-003"></a>
### GW-FN-003 — 複数機器の実行進行・補償

実行順序・部分成功・取消し・補償を一つの所有者で扱い、必要なら再計画へ戻す。

**適用条件：** 対象機器・版・操作・状態・数値の確定後に適用

**判断状態：** R6_DESIGN_DRAFT。採用リリース・実装確認・正式USDM対応は未確定。

**実現責任／GW内担当：** H側 Energy Orchestrator。

**機能配賦：** [S-FN-004](../I_System/I-03_System_Functions.md#s-fn-004) ／ [S-FN-005](../I_System/I-03_System_Functions.md#s-fn-005) ／ [S-FN-006](../I_System/I-03_System_Functions.md#s-fn-006) ／ [S-FN-007](../I_System/I-03_System_Functions.md#s-fn-007) ／ [S-FN-015](../I_System/I-03_System_Functions.md#s-fn-015)。

**関連SYS要求：** [SYS-ORCH-001](../../appendices/Requirements_Catalog.md#sys-orch-001)、[SYS-RETRY-001](../../appendices/Requirements_Catalog.md#sys-retry-001)。

**詳細章：** [II-03_Control_Execution](II-03_Control_Execution.md) ／ [I-06_Usecases](../I_System/I-06_Usecases.md)。

**具体的な不足：** [OQ-R6-06-01](../I_System/I-06_Usecases.md#oq-r6-06-01) ／ [OQ-R6-06-02](../I_System/I-06_Usecases.md#oq-r6-06-02)。

<a id="gw-fn-004"></a>
### GW-FN-004 — DERの通常操作・達成確認

許可済みDER要求を機器別操作系列へ展開し、受理・達成・制限・不明を区別する。

**適用条件：** 対象機器・版・操作・状態・数値の確定後に適用

**判断状態：** R6_DESIGN_DRAFT。採用リリース・実装確認・正式USDM対応は未確定。

**実現責任／GW内担当：** H側 DER Power Controller。

**機能配賦：** [S-FN-004](../I_System/I-03_System_Functions.md#s-fn-004) ／ [S-FN-006](../I_System/I-03_System_Functions.md#s-fn-006) ／ [S-FN-007](../I_System/I-03_System_Functions.md#s-fn-007) ／ [S-FN-015](../I_System/I-03_System_Functions.md#s-fn-015)。

**関連SYS要求：** [SYS-RESP-001](../../appendices/Requirements_Catalog.md#sys-resp-001)、[SYS-RESULT-001](../../appendices/Requirements_Catalog.md#sys-result-001)、[SYS-RESULT-002](../../appendices/Requirements_Catalog.md#sys-result-002)、[SYS-RESULT-003](../../appendices/Requirements_Catalog.md#sys-result-003)、[SYS-SEM-001](../../appendices/Requirements_Catalog.md#sys-sem-001)。

**詳細章：** [II-04_DER_Load_Control](II-04_DER_Load_Control.md) ／ [III-07_RS485_PCS](../III_Interfaces/III-07_RS485_PCS.md) ／ [III-06_ECHONET_Lite](../III_Interfaces/III-06_ECHONET_Lite.md)。

**具体的な不足：** [OQ-R6-05-02](II-03_Control_Execution.md#oq-r6-05-02) ／ [OQ-R6-07-01](../III_Interfaces/III-07_RS485_PCS.md#oq-r6-07-01) ／ [OQ-R6-07-02](../III_Interfaces/III-06_ECHONET_Lite.md#oq-r6-07-02)。

<a id="gw-fn-005"></a>
### GW-FN-005 — 空調・給湯等の負荷操作

機器側安全・本体設定・利用可能能力を尊重して、許可済み負荷操作と結果確認を行う。

**適用条件：** 対象機器・版・操作・状態・数値の確定後に適用

**判断状態：** R6_DESIGN_DRAFT。採用リリース・実装確認・正式USDM対応は未確定。

**実現責任／GW内担当：** H側 Flexible Load Controller。

**機能配賦：** [S-FN-005](../I_System/I-03_System_Functions.md#s-fn-005) ／ [S-FN-006](../I_System/I-03_System_Functions.md#s-fn-006) ／ [S-FN-007](../I_System/I-03_System_Functions.md#s-fn-007)。

**関連SYS要求：** [SYS-LOAD-001](../../appendices/Requirements_Catalog.md#sys-load-001)。

**詳細章：** [II-04_DER_Load_Control](II-04_DER_Load_Control.md) ／ [III-06_ECHONET_Lite](../III_Interfaces/III-06_ECHONET_Lite.md)。

**具体的な不足：** [OQ-R6-08-03](II-04_DER_Load_Control.md#oq-r6-08-03)。

<a id="gw-fn-006"></a>
### GW-FN-006 — 高度エネマネの計画生成

計測・利用者条件・利用可能能力から運転計画を生成する。自家消費・料金・購入電力・充電期限等の採否は未決。

**適用条件：** 採用した戦略と、その必要Capabilityが成立する構成

**判断状態：** R6_DESIGN_DRAFT。採用リリース・実装確認・正式USDM対応は未確定。

**実現責任／GW内担当：** H側 Advanced EMS。

**機能配賦：** [S-FN-006](../I_System/I-03_System_Functions.md#s-fn-006)。

**関連SYS要求：** [SYS-EMS-001](../../appendices/Requirements_Catalog.md#sys-ems-001)、[SYS-CONST-001](../../appendices/Requirements_Catalog.md#sys-const-001)。

**詳細章：** [II-05_Advanced_EMS](II-05_Advanced_EMS.md)。

**具体的な不足：** [OQ-R6-08-01](II-05_Advanced_EMS.md#oq-r6-08-01) ／ [OQ-R6-08-02](II-05_Advanced_EMS.md#oq-r6-08-02)。

<a id="gw-fn-007"></a>
### GW-FN-007 — 実績評価・再計画・入力不足時縮退

実績・機器離脱・制約変化を評価し、再計画又は明示した縮退へ移る。

**適用条件：** 対象機器・版・操作・状態・数値の確定後に適用

**判断状態：** R6_DESIGN_DRAFT。採用リリース・実装確認・正式USDM対応は未確定。

**実現責任／GW内担当：** H側 Advanced EMS／Orchestrator。

**機能配賦：** [S-FN-007](../I_System/I-03_System_Functions.md#s-fn-007) ／ [S-FN-015](../I_System/I-03_System_Functions.md#s-fn-015)。

**関連SYS要求：** [SYS-EMS-001](../../appendices/Requirements_Catalog.md#sys-ems-001)、[SYS-CONST-001](../../appendices/Requirements_Catalog.md#sys-const-001)、[SYS-RESULT-002](../../appendices/Requirements_Catalog.md#sys-result-002)。

**詳細章：** [II-05_Advanced_EMS](II-05_Advanced_EMS.md) ／ [II-10_Fault_Alarm_Diagnostics](II-10_Fault_Alarm_Diagnostics.md)。

**具体的な不足：** [OQ-R6-08-02](II-05_Advanced_EMS.md#oq-r6-08-02)。

<a id="gw-fn-008"></a>
### GW-FN-008 — 計測・状態の取得正規化

単位・符号・計測点・鮮度・品質を保持し、同一設備や量を二重計上しない。

**適用条件：** 対象機器・版・操作・状態・数値の確定後に適用

**判断状態：** R6_DESIGN_DRAFT。採用リリース・実装確認・正式USDM対応は未確定。

**実現責任／GW内担当：** H側 Measurement／Device State。

**機能配賦：** [S-FN-001](../I_System/I-03_System_Functions.md#s-fn-001) ／ [S-FN-007](../I_System/I-03_System_Functions.md#s-fn-007) ／ [S-FN-016](../I_System/I-03_System_Functions.md#s-fn-016) ／ [S-FN-017](../I_System/I-03_System_Functions.md#s-fn-017)。

**関連SYS要求：** [SYS-MEAS-001](../../appendices/Requirements_Catalog.md#sys-meas-001)、[SYS-MEAS-002](../../appendices/Requirements_Catalog.md#sys-meas-002)、[SYS-STATE-001](../../appendices/Requirements_Catalog.md#sys-state-001)、[SYS-STATE-002](../../appendices/Requirements_Catalog.md#sys-state-002)。

**詳細章：** [II-07_Measurement_Data](II-07_Measurement_Data.md)。

**具体的な不足：** [OQ-R6-09-01](II-07_Measurement_Data.md#oq-r6-09-01) ／ [OQ-R6-11-01](../I_System/I-07_Responsibilities_Constraints.md#oq-r6-11-01)。

<a id="gw-fn-009"></a>
### GW-FN-009 — 履歴保存・抽出・上位同期

短期／長期／監査の用途別保存、欠測を含む抽出と再同期を行う。

**適用条件：** 対象機器・版・操作・状態・数値の確定後に適用

**判断状態：** R6_DESIGN_DRAFT。採用リリース・実装確認・正式USDM対応は未確定。

**実現責任／GW内担当：** H側 Data／Telemetry。

**機能配賦：** [S-FN-001](../I_System/I-03_System_Functions.md#s-fn-001) ／ [S-FN-003](../I_System/I-03_System_Functions.md#s-fn-003) ／ [S-FN-016](../I_System/I-03_System_Functions.md#s-fn-016) ／ [S-FN-017](../I_System/I-03_System_Functions.md#s-fn-017)。

**関連SYS要求：** [SYS-DATA-001](../../appendices/Requirements_Catalog.md#sys-data-001)、[SYS-DATA-002](../../appendices/Requirements_Catalog.md#sys-data-002)、[SYS-NORTH-006](../../appendices/Requirements_Catalog.md#sys-north-006)。

**詳細章：** [II-07_Measurement_Data](II-07_Measurement_Data.md) ／ [IV-08_Data_Log_UI_Quality](../IV_Quality/IV-08_Data_Log_UI_Quality.md)。

**具体的な不足：** [OQ-R6-09-02](../IV_Quality/IV-08_Data_Log_UI_Quality.md#oq-r6-09-02) ／ [OQ-R6-09-03](II-07_Measurement_Data.md#oq-r6-09-03)。

<a id="gw-fn-010"></a>
### GW-FN-010 — 機器探索・登録・識別・能力管理

物理装置、資源、接続、機器オブジェクト、機器版の対応を管理し、不明能力の推測書込みをしない。

**適用条件：** 対象機器・版・操作・状態・数値の確定後に適用

**判断状態：** R6_DESIGN_DRAFT。採用リリース・実装確認・正式USDM対応は未確定。

**実現責任／GW内担当：** H側 Device Inventory／Adapter。

**機能配賦：** [S-FN-004](../I_System/I-03_System_Functions.md#s-fn-004) ／ [S-FN-005](../I_System/I-03_System_Functions.md#s-fn-005) ／ [S-FN-008](../I_System/I-03_System_Functions.md#s-fn-008) ／ [S-FN-020](../I_System/I-03_System_Functions.md#s-fn-020)。

**関連SYS要求：** [SYS-CAP-001](../../appendices/Requirements_Catalog.md#sys-cap-001)、[SYS-CAP-002](../../appendices/Requirements_Catalog.md#sys-cap-002)、[SYS-ROUTE-001](../../appendices/Requirements_Catalog.md#sys-route-001)、[SYS-GNET-012](../../appendices/Requirements_Catalog.md#sys-gnet-012)。

**詳細章：** [II-06_Device_Management](II-06_Device_Management.md) ／ [I-05_Configurations](../I_System/I-05_Configurations.md)。

**具体的な不足：** [OQ-R6-04-02](../I_System/I-05_Configurations.md#oq-r6-04-02) ／ [OQ-R6-04-03](II-06_Device_Management.md#oq-r6-04-03)。

<a id="gw-fn-011"></a>
### GW-FN-011 — RS-485 PCS通常操作・状態通信

既存通常操作と状態取得を維持し、G側必須指令との送信所有・負荷・非迂回契約に従って通信する。

**適用条件：** RS-485 PCS。H側からの無制限な生電文アクセスを意味しない

**判断状態：** R6_DESIGN_DRAFT。採用リリース・実装確認・正式USDM対応は未確定。

**実現責任／GW内担当：** H側要求元＋G側／固定PCS通信所有者。

**機能配賦：** [S-FN-004](../I_System/I-03_System_Functions.md#s-fn-004) ／ [S-FN-008](../I_System/I-03_System_Functions.md#s-fn-008) ／ [S-FN-012](../I_System/I-03_System_Functions.md#s-fn-012)。

**関連SYS要求：** [SYS-RS-001](../../appendices/Requirements_Catalog.md#sys-rs-001)、[SYS-RS-002](../../appendices/Requirements_Catalog.md#sys-rs-002)、[SYS-RS-003](../../appendices/Requirements_Catalog.md#sys-rs-003)、[SYS-RS-005](../../appendices/Requirements_Catalog.md#sys-rs-005)、[SYS-RS-006](../../appendices/Requirements_Catalog.md#sys-rs-006)。

**詳細章：** [III-07_RS485_PCS](../III_Interfaces/III-07_RS485_PCS.md) ／ [II-08_GW_Grid_Control](II-08_GW_Grid_Control.md)。

**具体的な不足：** [OQ-R6-07-01](../III_Interfaces/III-07_RS485_PCS.md#oq-r6-07-01) ／ [OQ-R6-15-01](II-01_GW_Architecture.md#oq-r6-15-01)。

<a id="gw-fn-012"></a>
### GW-FN-012 — ECHONET Lite Controller

H側LAN→宅内LAN/AP→PCS・空調・給湯・計測器のEL機器IFと、通常操作・観測の要求応答を行う。

**適用条件：** EL接続機器。PCS自身のサーバ取得とは別通信

**判断状態：** R6_DESIGN_DRAFT。採用リリース・実装確認・正式USDM対応は未確定。

**実現責任／GW内担当：** H側 ECHONET Lite Controller／Adapter。

**機能配賦：** [S-FN-001](../I_System/I-03_System_Functions.md#s-fn-001) ／ [S-FN-004](../I_System/I-03_System_Functions.md#s-fn-004) ／ [S-FN-005](../I_System/I-03_System_Functions.md#s-fn-005) ／ [S-FN-008](../I_System/I-03_System_Functions.md#s-fn-008)。

**関連SYS要求：** [SYS-EL-001](../../appendices/Requirements_Catalog.md#sys-el-001)、[SYS-GNET-004](../../appendices/Requirements_Catalog.md#sys-gnet-004)、[SYS-CAP-001](../../appendices/Requirements_Catalog.md#sys-cap-001)。

**詳細章：** [III-06_ECHONET_Lite](../III_Interfaces/III-06_ECHONET_Lite.md) ／ [I-04_System_Context](../I_System/I-04_System_Context.md)。

**具体的な不足：** [OQ-R6-07-02](../III_Interfaces/III-06_ECHONET_Lite.md#oq-r6-07-02)。

<a id="gw-fn-013"></a>
### GW-FN-013 — ECHONET Lite Device側公開

外部HEMSへ許可する機器情報・操作を公開し、内部の実機対応と応答の意味を保持する。

**適用条件：** 対象機器・版・操作・状態・数値の確定後に適用

**判断状態：** R6_DESIGN_DRAFT。採用リリース・実装確認・正式USDM対応は未確定。

**実現責任／GW内担当：** H側 ECHONET Lite Device Adapter。

**機能配賦：** [S-FN-018](../I_System/I-03_System_Functions.md#s-fn-018)。

**関連SYS要求：** [SYS-EL-001](../../appendices/Requirements_Catalog.md#sys-el-001)、[SYS-EL-002](../../appendices/Requirements_Catalog.md#sys-el-002)、[SYS-GNET-012](../../appendices/Requirements_Catalog.md#sys-gnet-012)。

**詳細章：** [III-06_ECHONET_Lite](../III_Interfaces/III-06_ECHONET_Lite.md)。

**具体的な不足：** [OQ-R6-07-02](../III_Interfaces/III-06_ECHONET_Lite.md#oq-r6-07-02)。

<a id="gw-fn-014"></a>
### GW-FN-014 — GW G側スケジュール取得・管理

宅内ルータ経由で出力制御情報を取得・検証・保存し、適用時刻・有効性・資格情報を管理する。

**適用条件：** RS-485 PCS向けGW_MANAGED。EL PCSの代理取得には使用しない

**判断状態：** R6_DESIGN_DRAFT。採用リリース・実装確認・正式USDM対応は未確定。

**実現責任／GW内担当：** GW G側の出力制御機能。

**機能配賦：** [S-FN-012](../I_System/I-03_System_Functions.md#s-fn-012)。

**関連SYS要求：** [SYS-GRID-001](../../appendices/Requirements_Catalog.md#sys-grid-001)、[SYS-GRID-003](../../appendices/Requirements_Catalog.md#sys-grid-003)、[SYS-GSEL-001](../../appendices/Requirements_Catalog.md#sys-gsel-001)、[SYS-GSEL-005](../../appendices/Requirements_Catalog.md#sys-gsel-005)、[SYS-GSEL-006](../../appendices/Requirements_Catalog.md#sys-gsel-006)、[SYS-GNET-001](../../appendices/Requirements_Catalog.md#sys-gnet-001)、[SYS-GNET-003](../../appendices/Requirements_Catalog.md#sys-gnet-003)。

**詳細章：** [II-08_GW_Grid_Control](II-08_GW_Grid_Control.md) ／ [III-08_Utility_Server](../III_Interfaces/III-08_Utility_Server.md)。

**具体的な不足：** [OQ-R6-10-01](../V_Lifecycle/V-04_Compliance.md#oq-r6-10-01) ／ [OQ-R6-21-01](../I_System/I-05_Configurations.md#oq-r6-21-01)。

<a id="gw-fn-015"></a>
### GW-FN-015 — GW G側の出力制御指示・必須監視

適用制約に従いRS-485 PCSへ指示し、必要な状態・通信異常を監視する。

**適用条件：** RS-485 PCS。H側停止とGW全体停止は別条件

**判断状態：** R6_DESIGN_DRAFT。採用リリース・実装確認・正式USDM対応は未確定。

**実現責任／GW内担当：** GW G側＋確認済みPCS実行契約。

**機能配賦：** [S-FN-012](../I_System/I-03_System_Functions.md#s-fn-012) ／ [S-FN-015](../I_System/I-03_System_Functions.md#s-fn-015)。

**関連SYS要求：** [SYS-GSEL-004](../../appendices/Requirements_Catalog.md#sys-gsel-004)、[SYS-GSEL-005](../../appendices/Requirements_Catalog.md#sys-gsel-005)、[SYS-GSEL-011](../../appendices/Requirements_Catalog.md#sys-gsel-011)、[SYS-GSEL-012](../../appendices/Requirements_Catalog.md#sys-gsel-012)、[SYS-GNET-003](../../appendices/Requirements_Catalog.md#sys-gnet-003)。

**詳細章：** [II-08_GW_Grid_Control](II-08_GW_Grid_Control.md) ／ [III-07_RS485_PCS](../III_Interfaces/III-07_RS485_PCS.md)。

**具体的な不足：** [OQ-R6-10-02](../I_System/I-07_Responsibilities_Constraints.md#oq-r6-10-02) ／ [OQ-R6-15-01](II-01_GW_Architecture.md#oq-r6-15-01) ／ [OQ-R6-21-01](../I_System/I-05_Configurations.md#oq-r6-21-01)。

<a id="gw-fn-016"></a>
### GW-FN-016 — PCS側の出力制御・保護状態の参照

提供可能な制約・状態だけを参照する。非公開は不明とし、EL PCSの取得・適用やPCS保護そのものを代行しない。

**適用条件：** PCSが公開する情報の範囲内。OBSERVE_ONLYの配賦

**判断状態：** R6_DESIGN_DRAFT。採用リリース・実装確認・正式USDM対応は未確定。

**実現責任／GW内担当：** H側の観測・公開View。

**機能配賦：** [S-FN-001](../I_System/I-03_System_Functions.md#s-fn-001) ／ [S-FN-013](../I_System/I-03_System_Functions.md#s-fn-013) ／ [S-FN-014](../I_System/I-03_System_Functions.md#s-fn-014) ／ [S-FN-016](../I_System/I-03_System_Functions.md#s-fn-016)。

**関連SYS要求：** [SYS-GSEL-013](../../appendices/Requirements_Catalog.md#sys-gsel-013)、[SYS-GSEL-014](../../appendices/Requirements_Catalog.md#sys-gsel-014)、[SYS-GNET-007](../../appendices/Requirements_Catalog.md#sys-gnet-007)、[SYS-GNET-004](../../appendices/Requirements_Catalog.md#sys-gnet-004)。

**詳細章：** [II-07_Measurement_Data](II-07_Measurement_Data.md) ／ [I-07_Responsibilities_Constraints](../I_System/I-07_Responsibilities_Constraints.md)。

**具体的な不足：** [OQ-R6-21-01](../I_System/I-05_Configurations.md#oq-r6-21-01) ／ [OQ-R6-09-01](II-07_Measurement_Data.md#oq-r6-09-01)。

<a id="gw-fn-017"></a>
### GW-FN-017 — 上位管理・監視サーバ接続

認可された要求を用途別に配送し、状態・結果・内部情報の許可項目を公開する。

**適用条件：** 対象機器・版・操作・状態・数値の確定後に適用

**判断状態：** R6_DESIGN_DRAFT。採用リリース・実装確認・正式USDM対応は未確定。

**実現責任／GW内担当：** H側 Northbound Adapter／API。

**機能配賦：** [S-FN-003](../I_System/I-03_System_Functions.md#s-fn-003) ／ [S-FN-009](../I_System/I-03_System_Functions.md#s-fn-009) ／ [S-FN-010](../I_System/I-03_System_Functions.md#s-fn-010) ／ [S-FN-016](../I_System/I-03_System_Functions.md#s-fn-016) ／ [S-FN-019](../I_System/I-03_System_Functions.md#s-fn-019)。

**関連SYS要求：** [SYS-NORTH-001](../../appendices/Requirements_Catalog.md#sys-north-001)、[SYS-NORTH-002](../../appendices/Requirements_Catalog.md#sys-north-002)、[SYS-NORTH-003](../../appendices/Requirements_Catalog.md#sys-north-003)、[SYS-NORTH-004](../../appendices/Requirements_Catalog.md#sys-north-004)、[SYS-NORTH-005](../../appendices/Requirements_Catalog.md#sys-north-005)、[SYS-GWOP-001](../../appendices/Requirements_Catalog.md#sys-gwop-001)、[SYS-STATE-001](../../appendices/Requirements_Catalog.md#sys-state-001)。

**詳細章：** [III-02_Cloud_GW](../III_Interfaces/III-02_Cloud_GW.md) ／ [II-03_Control_Execution](II-03_Control_Execution.md)。

**具体的な不足：** [OQ-R6-20-01](../III_Interfaces/III-02_Cloud_GW.md#oq-r6-20-01) ／ [OQ-R6-20-05](../III_Interfaces/III-02_Cloud_GW.md#oq-r6-20-05)。

<a id="gw-fn-018"></a>
### GW-FN-018 — 宅内Web UI提供・ローカルAPI

直接無線又は宅内ルータ経由の端末に、基本監視・許可操作を提供する。

**適用条件：** 直接方式・AP/STA同時動作・画面範囲は未決。サーバ回線の代替ではない

**判断状態：** R6_DESIGN_DRAFT。採用リリース・実装確認・正式USDM対応は未確定。

**実現責任／GW内担当：** H側 Web／Local API。

**機能配賦：** [S-FN-002](../I_System/I-03_System_Functions.md#s-fn-002)。

**関連SYS要求：** [SYS-UI-001](../../appendices/Requirements_Catalog.md#sys-ui-001)、[SYS-UI-002](../../appendices/Requirements_Catalog.md#sys-ui-002)、[SYS-UI-003](../../appendices/Requirements_Catalog.md#sys-ui-003)、[SYS-UI-004](../../appendices/Requirements_Catalog.md#sys-ui-004)、[SYS-UI-005](../../appendices/Requirements_Catalog.md#sys-ui-005)、[SYS-GNET-010](../../appendices/Requirements_Catalog.md#sys-gnet-010)。

**詳細章：** [III-04_Local_Web](../III_Interfaces/III-04_Local_Web.md) ／ [IV-08_Data_Log_UI_Quality](../IV_Quality/IV-08_Data_Log_UI_Quality.md)。

**具体的な不足：** [OQ-R6-02-02](../I_System/I-04_System_Context.md#oq-r6-02-02) ／ [OQ-R6-20-02](../IV_Quality/IV-08_Data_Log_UI_Quality.md#oq-r6-20-02)。

<a id="gw-fn-019"></a>
### GW-FN-019 — リモートアプリ用状態・結果連携

GWはクラウドへ状態・操作結果を返す。スマートフォン画面やアプリ実装そのものをGW内機能にしない。

**適用条件：** 対象機器・版・操作・状態・数値の確定後に適用

**判断状態：** R6_DESIGN_DRAFT。採用リリース・実装確認・正式USDM対応は未確定。

**実現責任／GW内担当：** H側上位API／クラウド向け公開View。

**機能配賦：** [S-FN-003](../I_System/I-03_System_Functions.md#s-fn-003) ／ [S-FN-016](../I_System/I-03_System_Functions.md#s-fn-016)。

**関連SYS要求：** [SYS-APP-001](../../appendices/Requirements_Catalog.md#sys-app-001)、[SYS-APP-002](../../appendices/Requirements_Catalog.md#sys-app-002)、[SYS-NORTH-006](../../appendices/Requirements_Catalog.md#sys-north-006)、[SYS-STATE-002](../../appendices/Requirements_Catalog.md#sys-state-002)。

**詳細章：** [III-05_Remote_App](../III_Interfaces/III-05_Remote_App.md) ／ [III-02_Cloud_GW](../III_Interfaces/III-02_Cloud_GW.md)。

**具体的な不足：** [OQ-R6-20-02](../IV_Quality/IV-08_Data_Log_UI_Quality.md#oq-r6-20-02) ／ [OQ-R6-20-05](../III_Interfaces/III-02_Cloud_GW.md#oq-r6-20-05)。

<a id="gw-fn-020"></a>
### GW-FN-020 — 設定管理・変更調停

設定の希望・保存・有効状態、世代競合、反映可否、部分反映、通常と緊急復旧を区別する。

**適用条件：** 対象機器・版・操作・状態・数値の確定後に適用

**判断状態：** R6_DESIGN_DRAFT。採用リリース・実装確認・正式USDM対応は未確定。

**実現責任／GW内担当：** H側 Configuration／各状態所有者。

**機能配賦：** [S-FN-009](../I_System/I-03_System_Functions.md#s-fn-009) ／ [S-FN-015](../I_System/I-03_System_Functions.md#s-fn-015) ／ [S-FN-020](../I_System/I-03_System_Functions.md#s-fn-020)。

**関連SYS要求：** [SYS-CFG-001](../../appendices/Requirements_Catalog.md#sys-cfg-001)、[SYS-CFG-002](../../appendices/Requirements_Catalog.md#sys-cfg-002)、[SYS-CFG-004](../../appendices/Requirements_Catalog.md#sys-cfg-004)、[SYS-CFG-005](../../appendices/Requirements_Catalog.md#sys-cfg-005)。

**詳細章：** [II-09_Settings_Lifecycle](II-09_Settings_Lifecycle.md)。

**具体的な不足：** [OQ-R6-12-02](II-09_Settings_Lifecycle.md#oq-r6-12-02) ／ [OQ-R6-12-03](II-09_Settings_Lifecycle.md#oq-r6-12-03)。

<a id="gw-fn-021"></a>
### GW-FN-021 — ネットワーク設定の変更・到達性復旧

接続設定を変更し、適用結果と到達性を確認して規定された復旧へ移る。

**適用条件：** 対象機器・版・操作・状態・数値の確定後に適用

**判断状態：** R6_DESIGN_DRAFT。採用リリース・実装確認・正式USDM対応は未確定。

**実現責任／GW内担当：** H側の認可されたNetwork Config。

**機能配賦：** [S-FN-009](../I_System/I-03_System_Functions.md#s-fn-009) ／ [S-FN-021](../I_System/I-03_System_Functions.md#s-fn-021)。

**関連SYS要求：** [SYS-CFG-006](../../appendices/Requirements_Catalog.md#sys-cfg-006)、[SYS-GNET-006](../../appendices/Requirements_Catalog.md#sys-gnet-006)。

**詳細章：** [II-09_Settings_Lifecycle](II-09_Settings_Lifecycle.md) ／ [III-09_Network_Peripherals](../III_Interfaces/III-09_Network_Peripherals.md)。

**具体的な不足：** [OQ-R6-26-03](../V_Lifecycle/V-02_Commissioning_Handover.md#oq-r6-26-03) ／ [OQ-R6-12-02](II-09_Settings_Lifecycle.md#oq-r6-12-02)。

<a id="gw-fn-022"></a>
### GW-FN-022 — 内部機能操作・ライフサイクルJob

許可リスト内の探索・開始停止・再起動・診断等をJobとして処理し、高影響操作を調整する。

**適用条件：** 対象機器・版・操作・状態・数値の確定後に適用

**判断状態：** R6_DESIGN_DRAFT。採用リリース・実装確認・正式USDM対応は未確定。

**実現責任／GW内担当：** H側 Lifecycle／Operation Service。

**機能配賦：** [S-FN-010](../I_System/I-03_System_Functions.md#s-fn-010) ／ [S-FN-015](../I_System/I-03_System_Functions.md#s-fn-015) ／ [S-FN-016](../I_System/I-03_System_Functions.md#s-fn-016) ／ [S-FN-020](../I_System/I-03_System_Functions.md#s-fn-020)。

**関連SYS要求：** [SYS-GWOP-001](../../appendices/Requirements_Catalog.md#sys-gwop-001)、[SYS-GWOP-002](../../appendices/Requirements_Catalog.md#sys-gwop-002)。

**詳細章：** [II-09_Settings_Lifecycle](II-09_Settings_Lifecycle.md) ／ [III-10_Maintenance_Interfaces](../III_Interfaces/III-10_Maintenance_Interfaces.md)。

**具体的な不足：** [OQ-R6-20-01](../III_Interfaces/III-02_Cloud_GW.md#oq-r6-20-01)。

<a id="gw-fn-023"></a>
### GW-FN-023 — FW取得・配布物検証

配信・承認・適用を分け、対象・完全性・互換性・系列を確認する。

**適用条件：** 対象機器・版・操作・状態・数値の確定後に適用

**判断状態：** R6_DESIGN_DRAFT。採用リリース・実装確認・正式USDM対応は未確定。

**実現責任／GW内担当：** H側 Update Manager（対象領域は個別管理）。

**機能配賦：** [S-FN-011](../I_System/I-03_System_Functions.md#s-fn-011)。

**関連SYS要求：** [SYS-FW-001](../../appendices/Requirements_Catalog.md#sys-fw-001)、[SYS-FW-002](../../appendices/Requirements_Catalog.md#sys-fw-002)、[SYS-FW-005](../../appendices/Requirements_Catalog.md#sys-fw-005)。

**詳細章：** [II-11_Firmware_Update](II-11_Firmware_Update.md) ／ [III-03_FW_Server](../III_Interfaces/III-03_FW_Server.md)。

**具体的な不足：** [OQ-R6-20-04](II-11_Firmware_Update.md#oq-r6-20-04)。

<a id="gw-fn-024"></a>
### GW-FN-024 — FW適用・稼働確認・復旧

許可された更新を実行し、永続状態に基づいて復帰・旧要求照合を行う。H更新にG更新を混入させない。

**適用条件：** 対象機器・版・操作・状態・数値の確定後に適用

**判断状態：** R6_DESIGN_DRAFT。採用リリース・実装確認・正式USDM対応は未確定。

**実現責任／GW内担当：** H側 Update Manager／独立したG更新の境界。

**機能配賦：** [S-FN-011](../I_System/I-03_System_Functions.md#s-fn-011) ／ [S-FN-015](../I_System/I-03_System_Functions.md#s-fn-015)。

**関連SYS要求：** [SYS-OTA-001](../../appendices/Requirements_Catalog.md#sys-ota-001)、[SYS-OTA-002](../../appendices/Requirements_Catalog.md#sys-ota-002)、[SYS-FW-003](../../appendices/Requirements_Catalog.md#sys-fw-003)、[SYS-FW-004](../../appendices/Requirements_Catalog.md#sys-fw-004)。

**詳細章：** [II-11_Firmware_Update](II-11_Firmware_Update.md)。

**具体的な不足：** [OQ-R6-20-04](II-11_Firmware_Update.md#oq-r6-20-04) ／ [OQ-R6-13-02](II-11_Firmware_Update.md#oq-r6-13-02)。

<a id="gw-fn-025"></a>
### GW-FN-025 — 警報・監査・診断情報の公開

故障・操作・品質・相関情報を記録し、許可された警報・診断情報を通知・抽出する。

**適用条件：** 対象機器・版・操作・状態・数値の確定後に適用

**判断状態：** R6_DESIGN_DRAFT。採用リリース・実装確認・正式USDM対応は未確定。

**実現責任／GW内担当：** H側 Logging／Diagnostics／Telemetry。

**機能配賦：** [S-FN-016](../I_System/I-03_System_Functions.md#s-fn-016) ／ [S-FN-019](../I_System/I-03_System_Functions.md#s-fn-019) ／ [S-FN-020](../I_System/I-03_System_Functions.md#s-fn-020)。

**関連SYS要求：** [SYS-LOG-001](../../appendices/Requirements_Catalog.md#sys-log-001)、[SYS-STATE-001](../../appendices/Requirements_Catalog.md#sys-state-001)、[SYS-NORTH-005](../../appendices/Requirements_Catalog.md#sys-north-005)。

**詳細章：** [II-10_Fault_Alarm_Diagnostics](II-10_Fault_Alarm_Diagnostics.md) ／ [IV-08_Data_Log_UI_Quality](../IV_Quality/IV-08_Data_Log_UI_Quality.md)。

**具体的な不足：** [OQ-R6-20-03](II-10_Fault_Alarm_Diagnostics.md#oq-r6-20-03) ／ [OQ-R6-09-03](II-07_Measurement_Data.md#oq-r6-09-03)。

<a id="gw-fn-026"></a>
### GW-FN-026 — 故障検出・再接続・結果再照合

WAN/LAN/GW/RS-485等の障害位置を区別し、要求残留・期限・重複を照合して縮退・復旧する。

**適用条件：** 対象機器・版・操作・状態・数値の確定後に適用

**判断状態：** R6_DESIGN_DRAFT。採用リリース・実装確認・正式USDM対応は未確定。

**実現責任／GW内担当：** H側とG側それぞれの障害所有者。

**機能配賦：** [S-FN-007](../I_System/I-03_System_Functions.md#s-fn-007) ／ [S-FN-015](../I_System/I-03_System_Functions.md#s-fn-015) ／ [S-FN-021](../I_System/I-03_System_Functions.md#s-fn-021)。

**関連SYS要求：** [SYS-FAULT-001](../../appendices/Requirements_Catalog.md#sys-fault-001)、[SYS-EXPIRY-001](../../appendices/Requirements_Catalog.md#sys-expiry-001)、[SYS-RETRY-001](../../appendices/Requirements_Catalog.md#sys-retry-001)、[SYS-GNET-005](../../appendices/Requirements_Catalog.md#sys-gnet-005)。

**詳細章：** [II-10_Fault_Alarm_Diagnostics](II-10_Fault_Alarm_Diagnostics.md) ／ [I-08_System_States](../I_System/I-08_System_States.md)。

**具体的な不足：** [OQ-R6-13-01](II-10_Fault_Alarm_Diagnostics.md#oq-r6-13-01) ／ [OQ-R6-20-05](../III_Interfaces/III-02_Cloud_GW.md#oq-r6-20-05)。

<a id="gw-fn-027"></a>
### GW-FN-027 — 資格情報・所属・失効・認可の管理

操作者と配送主体を区別し、所属変更・資格情報の更新失効・環境と対象範囲に従ってアクセスを制限する。

**適用条件：** 対象機器・版・操作・状態・数値の確定後に適用

**判断状態：** R6_DESIGN_DRAFT。採用リリース・実装確認・正式USDM対応は未確定。

**実現責任／GW内担当：** GW各認可境界／資格情報所有者。

**機能配賦：** [S-FN-019](../I_System/I-03_System_Functions.md#s-fn-019) ／ [S-FN-020](../I_System/I-03_System_Functions.md#s-fn-020)。

**関連SYS要求：** [SYS-SEC-001](../../appendices/Requirements_Catalog.md#sys-sec-001)、[SYS-NORTH-002](../../appendices/Requirements_Catalog.md#sys-north-002)、[SYS-NORTH-007](../../appendices/Requirements_Catalog.md#sys-north-007)、[SYS-APP-003](../../appendices/Requirements_Catalog.md#sys-app-003)。

**詳細章：** [IV-03_Security_Privacy](../IV_Quality/IV-03_Security_Privacy.md) ／ [I-02_Actors_Roles](../I_System/I-02_Actors_Roles.md)。

**具体的な不足：** [OQ-R6-27-02](../IV_Quality/IV-03_Security_Privacy.md#oq-r6-27-02) ／ [OQ-R6-27-03](../IV_Quality/IV-03_Security_Privacy.md#oq-r6-27-03) ／ [OQ-R6-27-04](../IV_Quality/IV-03_Security_Privacy.md#oq-r6-27-04)。

<a id="gw-fn-028"></a>
### GW-FN-028 — H/G境界の限定操作・不正入力拒否

通常APIから保護設定・系統スケジュール原本等へ迂回させず、専用保守と通常権限を分ける。

**適用条件：** 対象機器・版・操作・状態・数値の確定後に適用

**判断状態：** R6_DESIGN_DRAFT。採用リリース・実装確認・正式USDM対応は未確定。

**実現責任／GW内担当：** H/G境界と最終通常送信境界。

**機能配賦：** [S-FN-012](../I_System/I-03_System_Functions.md#s-fn-012) ／ [S-FN-013](../I_System/I-03_System_Functions.md#s-fn-013) ／ [S-FN-014](../I_System/I-03_System_Functions.md#s-fn-014) ／ [S-FN-019](../I_System/I-03_System_Functions.md#s-fn-019)。

**関連SYS要求：** [SYS-BOUND-001](../../appendices/Requirements_Catalog.md#sys-bound-001)、[SYS-GSEL-004](../../appendices/Requirements_Catalog.md#sys-gsel-004)、[SYS-GSEL-006](../../appendices/Requirements_Catalog.md#sys-gsel-006)、[SYS-OTA-001](../../appendices/Requirements_Catalog.md#sys-ota-001)。

**詳細章：** [III-01_Boundary_Contracts](../III_Interfaces/III-01_Boundary_Contracts.md) ／ [IV-07_Isolation_Shared_Resources](../IV_Quality/IV-07_Isolation_Shared_Resources.md)。

**具体的な不足：** [OQ-R6-03-02](../III_Interfaces/III-01_Boundary_Contracts.md#oq-r6-03-02) ／ [OQ-R6-15-02](../IV_Quality/IV-07_Isolation_Shared_Resources.md#oq-r6-15-02)。

<a id="gw-fn-029"></a>
### GW-FN-029 — 製造初期化・施工・試運転の機器側支援

個体識別・初期設定・登録・引渡し確認に必要な機器側機能を定義する。詳細機能はR6補完対象。

**適用条件：** 対象機器・版・操作・状態・数値の確定後に適用

**判断状態：** R6_COMPLETION_CANDIDATE。採用リリース・実装確認・正式USDM対応は未確定。

**実現責任／GW内担当：** GW製造／施工用の限定機能（採否未決）。

**機能配賦：** [S-FN-008](../I_System/I-03_System_Functions.md#s-fn-008) ／ [S-FN-020](../I_System/I-03_System_Functions.md#s-fn-020)。

**関連SYS要求：** [SYS-GSEL-019](../../appendices/Requirements_Catalog.md#sys-gsel-019)、[SYS-SVC-001](../../appendices/Requirements_Catalog.md#sys-svc-001)。

**詳細章：** [II-06_Device_Management](II-06_Device_Management.md) ／ [V-01_Manufacturing_Shipping](../V_Lifecycle/V-01_Manufacturing_Shipping.md) ／ [V-02_Commissioning_Handover](../V_Lifecycle/V-02_Commissioning_Handover.md)。

**具体的な不足：** [OQ-R6-26-01](../V_Lifecycle/V-01_Manufacturing_Shipping.md#oq-r6-26-01) ／ [OQ-R6-26-02](../V_Lifecycle/V-01_Manufacturing_Shipping.md#oq-r6-26-02) ／ [OQ-R6-26-03](../V_Lifecycle/V-02_Commissioning_Handover.md#oq-r6-26-03) ／ [OQ-R6-26-04](../V_Lifecycle/V-02_Commissioning_Handover.md#oq-r6-26-04)。

<a id="gw-fn-030"></a>
### GW-FN-030 — バックアップ・初期化・交換・消去

設定復元の境界を保ち、交換・所有者変更・廃棄で対象データと資格を整理する。

**適用条件：** 対象機器・版・操作・状態・数値の確定後に適用

**判断状態：** R6_COMPLETION_CANDIDATE。採用リリース・実装確認・正式USDM対応は未確定。

**実現責任／GW内担当：** H側Config／保守・個別G保守の境界。

**機能配賦：** [S-FN-009](../I_System/I-03_System_Functions.md#s-fn-009) ／ [S-FN-019](../I_System/I-03_System_Functions.md#s-fn-019) ／ [S-FN-020](../I_System/I-03_System_Functions.md#s-fn-020)。

**関連SYS要求：** [SYS-CFG-003](../../appendices/Requirements_Catalog.md#sys-cfg-003)、[SYS-APP-003](../../appendices/Requirements_Catalog.md#sys-app-003)、[SYS-GSEL-019](../../appendices/Requirements_Catalog.md#sys-gsel-019)。

**詳細章：** [II-09_Settings_Lifecycle](II-09_Settings_Lifecycle.md) ／ [V-03_Maintenance_Retirement](../V_Lifecycle/V-03_Maintenance_Retirement.md)。

**具体的な不足：** [OQ-R6-12-04](II-09_Settings_Lifecycle.md#oq-r6-12-04) ／ [OQ-R6-26-05](../V_Lifecycle/V-03_Maintenance_Retirement.md#oq-r6-26-05) ／ [OQ-R6-26-06](../V_Lifecycle/V-03_Maintenance_Retirement.md#oq-r6-26-06)。

<a id="gw-fn-031"></a>
### GW-FN-031 — 複数通信・USB等の接続管理

IPv4/IPv6・Wi-SUN・USB等の持越し要求について、搭載・有効・接続・認証・故障を区別する。

**適用条件：** 対象機器・版・操作・状態・数値の確定後に適用

**判断状態：** R6_CARRYOVER_SCOPE_TBD。採用リリース・実装確認・正式USDM対応は未確定。

**実現責任／GW内担当：** GW通信基盤／Transport／Security Adapter。

**機能配賦：** [S-FN-008](../I_System/I-03_System_Functions.md#s-fn-008) ／ [S-FN-021](../I_System/I-03_System_Functions.md#s-fn-021)。

**関連SYS要求：** [SYS-SEC-001](../../appendices/Requirements_Catalog.md#sys-sec-001)、[SYS-CAP-001](../../appendices/Requirements_Catalog.md#sys-cap-001)、[SYS-MIG-002](../../appendices/Requirements_Catalog.md#sys-mig-002)。

**詳細章：** [III-09_Network_Peripherals](../III_Interfaces/III-09_Network_Peripherals.md) ／ [II-06_Device_Management](II-06_Device_Management.md)。

**具体的な不足：** [OQ-R6-07-03](../III_Interfaces/III-09_Network_Peripherals.md#oq-r6-07-03) ／ [OQ-R6-18-01](../V_Lifecycle/V-05_Change_Migration_Release.md#oq-r6-18-01)。

<a id="gw-fn-032"></a>
### GW-FN-032 — 起動・停止・操作開始条件の管理

設定・時計・機器・旧要求の照合結果に応じ、監視・通常制御・自律制御を段階的に許可する。

**適用条件：** 対象機器・版・操作・状態・数値の確定後に適用

**判断状態：** R6_DESIGN_DRAFT。採用リリース・実装確認・正式USDM対応は未確定。

**実現責任／GW内担当：** H側／G側の独立したLifecycle。

**機能配賦：** [S-FN-015](../I_System/I-03_System_Functions.md#s-fn-015) ／ [S-FN-020](../I_System/I-03_System_Functions.md#s-fn-020)。

**関連SYS要求：** [SYS-OTA-002](../../appendices/Requirements_Catalog.md#sys-ota-002)、[SYS-CAP-002](../../appendices/Requirements_Catalog.md#sys-cap-002)、[SYS-GSEL-011](../../appendices/Requirements_Catalog.md#sys-gsel-011)。

**詳細章：** [II-09_Settings_Lifecycle](II-09_Settings_Lifecycle.md) ／ [I-08_System_States](../I_System/I-08_System_States.md)。

**具体的な不足：** [OQ-R6-12-01](II-09_Settings_Lifecycle.md#oq-r6-12-01) ／ [OQ-R6-13-02](II-11_Firmware_Update.md#oq-r6-13-02)。

<a id="legacy-4-10-1"></a>
<a id="slot-r6-04-01"></a>
## II-02.1 既存・追加・変更・廃止機能の母集団

**移行元：** [R7旧4.10.1節](../../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/04_Configurations_Profiles.md)。

**補完項目ID：** `SLOT-R6-04-01`。**対応観点：** C04, C05（[レビューA1](../../../../../30_references/baselines/R8_FIX001/sources/review/R5_Coverage_Review_A1.md)）。

R5の既存原則は保持するが、この項の全対象・具体条件・規範参照は未確定。

**本項に記載する仕様項目：**

- 機能ID・目的・根拠USDM。
- 変更区分と採用区分。
- Legacy/Next・HW/FW・機器・通信の適用。

**本項の完成判定：** 機能一覧を既存仕様・コード調査と突合し、候補機能の採否・対象リリース・非対応理由を機能表で承認する。

**具体的な不足：** [OQ-R6-04-01](II-02_GW_Functions.md#oq-r6-04-01)。採用値・参照版・対象外理由は回答後に本項又は版指定の規範別冊へ反映する。


<a id="open-questions"></a>
## Open Questions — 本ノートの完成に必要な確認

以下が本章で回答を管理する質問。関連台帳は参照ビューであり、承認や数値を二重管理しない。

<a id="oq-r6-04-01"></a>
### OQ-R6-04-01 — 既存・追加・変更・廃止機能の母集団

**対象項：** [SLOT-R6-04-01](II-02_GW_Functions.md#slot-r6-04-01)。状態：**OPEN**。

**質問：** 既存GWの全機能は何か。高度エネマネ追加後に維持・変更・廃止する機能と初回採用機能はどれか。候補ではなく採用済みとできる根拠は何か。

**必要資料・完了条件：** 機能一覧を既存仕様・コード調査と突合し、候補機能の採否・対象リリース・非対応理由を機能表で承認する。

**決定担当：** 未割当（候補：製品企画・既存製品担当）。承認者：未定。

**確定時点：** G0 — 製品スコープ・機能採否・要求Baselineの承認前（提案）。回答期限：未定。

**未解決時の制約：** 「既存・追加・変更・廃止機能の母集団」を対象構成の確定保証・実装受入根拠として使用しない。

**関連する既存ID：** SYS-TBD-005, SYS-TBD-011, TBD-010。

**回答：** 未記入。**決定記録：** 未記入。

### 他章で回答する関連質問

| OQ・正本章 | 残る判断 | 完了条件 |
|---|---|---|
| [OQ-R6-02-02](../I_System/I-04_System_Context.md#oq-r6-02-02) | 直接無線Webはどの無線方式を使うか。ルータ接続と同時利用できるか。クラウド断でも利用できる画面と認証条件は何か。 | 直接接続/宅内ルータ/リモートの構成別機能表と到達・再接続の確認方法を定義する。 |
| [OQ-R6-03-02](../III_Interfaces/III-01_Boundary_Contracts.md#oq-r6-03-02) | H内及びH/G APIの必須項目、エラー体系、旧版互換、頻度・キュー上限をどの契約に固定するか。G側が受ける通常要求の許可リストは何か。 | Internal IF契約を操作単位で埋め、正規/不正/過負荷/再起動の契約試験条件を定義する。 |
| [OQ-R6-04-02](../I_System/I-05_Configurations.md#oq-r6-04-02) | 初回対応するPCS・空調・給湯・計測器・USB機器はどの型式/版か。全機能対応、観測のみ、非対応をどの組合せで保証するか。 | 機器プロファイルと製品構成表に実型式・版・操作・制限・確認資料を登録する。 |
| [OQ-R6-04-03](II-06_Device_Management.md#oq-r6-04-03) | 探索した機器をいつ登録し、書込を許すか。交換・アドレス変更・多重IF・GW仮想EL公開をどう識別し、旧要求と履歴を扱うか。 | 探索/登録/交換/解除のUCと重複判定・書込解禁条件を定義し、旧設定移行の判定例を用意する。 |
| [OQ-R6-05-01](II-03_Control_Execution.md#oq-r6-05-01) | 利用者、本体操作、各クラウド、既存運転、高度エネマネが競合するとき、操作別の優先順位と同順位処理をどう決めるか。途中実行の取消しをどこまで保証するか。 | 通常操作の優先表、同時実行許可表、要求失効と補償の決定表を機器能力と対応付ける。 |
| [OQ-R6-05-02](II-03_Control_Execution.md#oq-r6-05-02) | 各操作の達成をどの計測点・許容差・確認時間で判定するか。応答や観測がない場合にUnknownを何時まで保持し、何を利用者へ返すか。 | 操作別結果判定表とUnknownの再照合・終端方針を定義し、APIとUIの同一意味を確認する。 |
| [OQ-R6-06-01](../I_System/I-06_Usecases.md#oq-r6-06-01) | 採用した全機能に代表UCがあるか。既存RS-485監視、内部操作、設定、FW、各EMS戦略に未記載の正常・異常系列はないか。 | 機能→UC→SYS→確認方法の双方向表を完成し、各UCに前提・結果・例外を記載する。 |
| [OQ-R6-06-02](../I_System/I-06_Usecases.md#oq-r6-06-02) | クラウド設定と宅内操作、FW更新と系統スケジュール切替、機器離脱と再計画が同時に発生したとき、どの系列を受入対象にするか。 | 横断シナリオ表を作成し、担当・順序・観測・タイムアウト・失敗後状態を指定する。 |
| [OQ-R6-07-01](../III_Interfaces/III-07_RS485_PCS.md#oq-r6-07-01) | 既存PCSの実プロトコル、電文/レジスタ、応答の意味、局数・配線条件は何か。通常操作とG側必須通信をどの送信者・予算で管理するか。 | PCS別接続仕様の版と電文対応を確定し、RS-485全書込点・最終送信境界・通信負荷表を登録する。 |
| [OQ-R6-07-02](../III_Interfaces/III-06_ECHONET_Lite.md#oq-r6-07-02) | 機器ごとのEL/AIF版・実装プロパティ・更新間隔は何か。GWのDevice側は何を公開し、RS-485資源や他社PCSとの対応と不可応答をどう定義するか。 | 対応するEL機器と操作・観測表を埋め、Controller/Device共存、公開能力の上限、未対応応答を確認する。 |
| [OQ-R6-07-03](../III_Interfaces/III-09_Network_Peripherals.md#oq-r6-07-03) | IPv4/IPv6、Wi-SUN、USB通信ドングル、USBバックアップ等をどの製品で採用するか。経路優先度、抜去・ハング時動作、認証あり/なし混在をどう規定するか。 | 持越し要求を採用/対象外へ仕分け、採用品の媒体・型式・状態遷移・資源上限を接続プロファイルへ登録する。 |
| [OQ-R6-08-01](II-05_Advanced_EMS.md#oq-r6-08-01) | 自家消費、料金、ピーク、充電期限のどの戦略を初回採用するか。機器構成・入力欠損・手動変更に応じた開始/解除/再開条件は何か。 | 戦略ごとの採否と機能仕様を機能表・UCへ展開し、入力/結果/異常分岐の未定を除く。 |
| [OQ-R6-08-02](II-05_Advanced_EMS.md#oq-r6-08-02) | 採用戦略の予測データ・料金データはどこから取得し、どの品質まで使うか。最適解が得られない/期限に間に合わない場合、どの代替動作と通知にするか。 | 戦略入力辞書、計画・再計画条件、未達時動作、評価シナリオと受入指標を確定する。 |
| [OQ-R6-08-03](II-04_DER_Load_Control.md#oq-r6-08-03) | 空調・給湯・蓄電池等の何を操作するか。設定範囲、快適性、終了時の運転残留、本体操作尊重を機種別にどう制約するか。 | DPC/FLCの操作別機能表を機器プロファイルと安全評価へ対応付け、未対応機能を実装済みと扱わない。 |
| [OQ-R6-09-01](II-07_Measurement_Data.md#oq-r6-09-01) | 公開・保存・制御利用する全データ項目は何か。AC/DC、電力/電力量、符号・精度・時刻・欠測・推定の表現をどう統一するか。 | 実項目ごとの辞書に型・単位・基準点・所有者・品質・利用先を記入し、二重計上をレビューする。 |
| [OQ-R6-09-02](../IV_Quality/IV-08_Data_Log_UI_Quality.md#oq-r6-09-02) | どの項目をどの粒度/期間保存するか。電断で許す損失、積算リセット・機器交換、容量枯渇時の削除・警報はどうするか。 | 用途別保持表、容量・寿命計算、電断/満杯/時刻補正の期待結果を定義する。 |
| [OQ-R6-09-03](II-07_Measurement_Data.md#oq-r6-09-03) | オフライン中の履歴を何件/期間保持し、上位とどう整合するか。利用者へ出せる項目・形式と、修理/所有者変更で消す範囲は何か。 | 同期・抽出・消去仕様をデータ項目単位で確定し、欠測と取得不能をデータ0としないテストを定める。 |
| [OQ-R6-10-01](../V_Lifecycle/V-04_Compliance.md#oq-r6-10-01) | 対象エリア・連系契約・設備範囲・正式仕様の版は何か。取得・保持・適用・期限切れ・通信異常時の値と条件は何か。 | 選択方式ごとの系統接続プロファイルに正式資料・適用範囲・値・確認者を登録する。 |
| [OQ-R6-10-02](../I_System/I-07_Responsibilities_Constraints.md#oq-r6-10-02) | 対象PCSの通常操作で出力制約や保護を上書きできない根拠は何か。独立計測・保護復帰・必要通信を誰が担い、H停止時に何を維持するか。 | メーカー説明・機能分担・許可操作・適用評価の記録をそろえ、必要な受入条件を[旧17章の再配置先](../../appendices/Chapter_Migration_Map.md#old-ch-17)へ配賦する。 |
| [OQ-R6-11-01](../I_System/I-07_Responsibilities_Constraints.md#oq-r6-11-01) | 制約と計測の基準点はどこか。PV/蓄電池/Hybrid PCSの共有容量と契約容量をどの配線図・機器仕様へ対応付けるか。 | 配線図、制約表、データ辞書を同じ資源ID・基準点で突合し、合算/非合算の対象を確定する。 |
| [OQ-R6-12-01](II-09_Settings_Lifecycle.md#oq-r6-12-01) | 工場初期、未登録、時刻無効、PCS不在、H/G片側未起動で、各機能をいつ開始してよいか。起動完了条件と待ち期限・失敗後の動作は何か。 | 状態遷移表と状態×操作許可表を埋め、初回/通常/縮退起動・停止系列をレビューする。 |
| [OQ-R6-12-02](II-09_Settings_Lifecycle.md#oq-r6-12-02) | 製品が管理する全設定キーと既定値は何か。製造/施工/通常/系統保守の変更権限と、機能・機種別の有効条件は何か。 | 設定項目一覧へ実キー・型・範囲・既定値・保存先・変更条件を登録し、G側項目を一般H設定から区別する。 |
| [OQ-R6-12-03](II-09_Settings_Lifecycle.md#oq-r6-12-03) | 同時変更や高優先度運転中の設定を、何秒/どの状態まで保留するか。緊急復旧で割り込める操作と部分反映の回復手順は何か。 | 操作別の反映条件、世代競合、保留期限、部分反映・緊急変更の決定表と確認方法を確定する。 |
| [OQ-R6-12-04](II-09_Settings_Lifecycle.md#oq-r6-12-04) | 一般設定バックアップと初期化で何を保存・削除するか。G側FW/時計/設定/資格情報をどう除外し、異機種・旧版への復元をどう判定するか。 | 対象項目と版互換表、初期化種別、復元前検査・失敗後状態を定義し、製造・廃棄と整合させる。 |
| [OQ-R6-13-01](II-10_Fault_Alarm_Diagnostics.md#oq-r6-13-01) | 全故障の検出条件・復帰条件・再試行の上限は何か。同じ故障の頻発、正常応答の一時回復、遅延応答をどう扱うか。 | 故障・警報対応表と復旧の決定表を作り、各閾値と通知・試験IDを結び付ける。 |
| [OQ-R6-13-02](II-11_Firmware_Update.md#oq-r6-13-02) | FW適用中断や起動不能から何を条件に復旧するか。H/G更新範囲、復帰先版、残る機器指令と保存データの処置は何か。 | 更新・復旧プロファイルと各障害点の期待状態を確定する。A/B領域等の方式は資料確認なく採用しない。 |
| [OQ-R6-15-01](II-01_GW_Architecture.md#oq-r6-15-01) | GW_MANAGEDのG側を実際にどこへ配置するか。H側停止・更新に共倒れする資源は何か。独立通常チャネルを採用するなら非迂回を何で確認するか。 | 配備・依存・更新単位・故障注入点の台帳を実HW/OS/PCS資料で埋め、成立と未達を分類する。 |
| [OQ-R6-15-02](../IV_Quality/IV-07_Isolation_Shared_Resources.md#oq-r6-15-02) | 非干渉を説明する入力・負荷・故障条件と比較Baselineは何か。共有ルータ・電源・OS変更をどの評価へ含め、誰が判断するか。 | 前提条件、各変更区分、必要な資料と試験の一覧をメーカー/評価担当と整理する。試験免除の確約にはしない。 |
| [OQ-R6-18-01](../V_Lifecycle/V-05_Change_Migration_Release.md#oq-r6-18-01) | As-Isのどの機能・通信・設定・挙動を維持するか。Legacyへ戻せない機能や、未確認の持越し項目をどの製品で対象外にするか。 | 既存機能母集団と完全なTo-Beの適用表を突合し、差分だけを正本にしない移行方針を確定する。 |
| [OQ-R6-20-01](../III_Interfaces/III-02_Cloud_GW.md#oq-r6-20-01) | 上位管理が読み書きする実項目と内部操作はどれか。プロトコル、公開schema、役割権限、完了通知・エラーをどう固定するか。 | 16件の論理IFを実契約へ展開し、公開操作台帳を実項目・権限・状態・結果へ対応付ける。 |
| [OQ-R6-20-02](../IV_Quality/IV-08_Data_Log_UI_Quality.md#oq-r6-20-02) | 宅内Web・スマートフォン・本体表示で提供する画面と項目は何か。対応端末、更新周期、色以外の区別、重要操作確認、多言語等の適用をどう決めるか。 | 画面×項目×操作×ロール表と対応端末表、利用者タスクの受入条件を確定する。ピクセル設計はUI詳細へ配賦する。 |
| [OQ-R6-20-03](II-10_Fault_Alarm_Diagnostics.md#oq-r6-20-03) | 通信断、出力制限、Unknown、更新失敗、保存異常等をどの警報として誰へ通知するか。確認・抑止・再通知・解除の条件と優先順位は何か。 | 警報台帳を故障ID・UI・上位イベントへ対応付け、確認済みが制約解除を意味しない条件を明記する。 |
| [OQ-R6-20-04](II-11_Firmware_Update.md#oq-r6-20-04) | FW配信が扱う対象はH側のみか、独立G保守を含む別配布か。画像形式・検証・適用条件・旧版復帰と各画面の成功判定をどう定めるか。 | 更新プロファイルを画像/対象/版/認可/段階/復旧条件で確定し、一般H更新からG変更を除外する。 |
| [OQ-R6-20-05](../III_Interfaces/III-02_Cloud_GW.md#oq-r6-20-05) | 上位断中にどの要求を保留し、何時まで同一要求と判断するか。オフライン認可の寿命と、アプリが表示できる過去状態の条件は何か。 | 操作別キュー/TTL/冪等保持、再同期、端末・所有者変更時の失効と表示規則を確定する。 |
| [OQ-R6-21-01](../I_System/I-05_Configurations.md#oq-r6-21-01) | EL接続PCSの自律取得能力・プロトコル・資格情報の管理仕様は何か。RS-485のGW管理と併せて、どの型式/版で実経路・公開状態を確認できるか。 | 機器接続別の取得プロファイルと管理主体、公開項目の根拠を登録する。非公開はNOT_EXPOSEDと明記する。 |
| [OQ-R6-26-01](../V_Lifecycle/V-01_Manufacturing_Shipping.md#oq-r6-26-01) | 個体IDと鍵/証明書をどの工程で投入し、再作業・不良品・重複をどう扱うか。出荷時に無効にする製造/開発機能と確認方法は何か。 | 製造プロファイルに投入主体・識別・秘密管理・再作業・閉鎖条件を記載し、手順書ID/版へ配賦する。 |
| [OQ-R6-26-02](../V_Lifecycle/V-01_Manufacturing_Shipping.md#oq-r6-26-02) | 出荷時の設定、運転可否、搭載FW・鍵、試験モード閉鎖を何で検査するか。GWが校正責任を持つ量はあるか。ラベル・付属品は何か。 | 出荷状態/検査/校正適用/記録/梱包の条件を確定し、機器が勝手に制御開始しない初期条件を起動仕様と整合する。 |
| [OQ-R6-26-03](../V_Lifecycle/V-02_Commissioning_Handover.md#oq-r6-26-03) | 施工者はどの順序で住宅・GW・機器・計測点を登録するか。EL自律取得/RS-485 GW管理とルータ経路をどう確認し、未完了時に何を禁止するか。 | 施工UCを初期接続から構成承認まで完結させ、チェック項目・失敗時戻り先・記録・引渡し条件を定める。 |
| [OQ-R6-26-04](../V_Lifecycle/V-02_Commissioning_Handover.md#oq-r6-26-04) | 現地試運転では何を確認し、どの記録で利用開始を許すか。非公開のPCS状態や通信断時制限を利用者へどう説明し、引渡しを確認するか。 | 試運転/引渡し条件表を安全・受入仕様へ対応付け、施工手順と利用者説明の文書ID/版を確定する。 |
| [OQ-R6-26-05](../V_Lifecycle/V-03_Maintenance_Retirement.md#oq-r6-26-05) | GW/PCS/計測器交換、移設、所有者変更で、何のIDとデータを継承し何を失効させるか。G側構成・資格の再設定と検収は誰が行うか。 | 交換/移設/所有者変更のデータ・資格・接続移行表と再試運転条件を記録する。 |
| [OQ-R6-26-06](../V_Lifecycle/V-03_Maintenance_Retirement.md#oq-r6-26-06) | 廃棄・返却でどの秘密・履歴・所属情報を消すか。起動不能やオフラインで消去/失効ができない場合の隔離・確認・責任は何か。 | 消去・失効・廃止のシステム機能と完了記録を規定し、廃棄手順・プライバシー要求へ配賦する。 |
| [OQ-R6-27-01](../IV_Quality/IV-03_Security_Privacy.md#oq-r6-27-01) | どの資産と脅威を評価対象にするか。宅内/直接無線/上位/EL/RS-485/製造/保守の入口ごとに、対策と検証と残留リスクを誰が承認するか。 | 脅威→資産/境界→対策→要求→確認方法の表を作成し、採用するJC-STAR等の項目と区別して対応付ける。 |
| [OQ-R6-27-02](../IV_Quality/IV-03_Security_Privacy.md#oq-r6-27-02) | 各資格情報の生成者・保存先・寿命・更新・失効・漏えい復旧をどう定めるか。時刻無効・上位断中の検証とG側資格の独立管理はどうするか。 | 鍵/証明書/アカウントのライフサイクル表と失効・復旧試験条件を製造/運用文書へ対応付ける。 |
| [OQ-R6-27-03](../IV_Quality/IV-03_Security_Privacy.md#oq-r6-27-03) | 各IFの暗号・認証・接続先識別・セッション方式を何にするか。従来EL機器と認証対応機器の許可操作、復号後の文脈保持をどう規定するか。 | IF別セキュリティプロファイルを確定し、失敗/混在/失効/セッションの受入条件を定義する。新たな標準暗号を全機器へ仮定しない。 |
| [OQ-R6-27-04](../IV_Quality/IV-03_Security_Privacy.md#oq-r6-27-04) | 量産機で残す保守・開発経路は何か。どの条件で一時有効化し、操作範囲・監査・自動無効化をどう制約するか。FW署名検証の失敗時は何を許すか。 | 保守経路台帳と許可操作/有効化/失効条件を定義し、任意shellやG設定への迂回を防ぐ検証へ結ぶ。 |
