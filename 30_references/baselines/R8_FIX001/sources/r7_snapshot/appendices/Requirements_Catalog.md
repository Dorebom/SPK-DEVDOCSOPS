# 要求カタログ — SYS要求のレビュー用ビュー

原子要求の管理用正本は[data/requirements.json](../data/requirements.json)。本ファイルは同データから生成する。章本文は責務・動作・例外の説明を補う。原典判断は履歴保持し、R4でのルータ必須・機器接続別限定を[R4判断差分](R4_Decision_Changes.md)へ記録する。機器・実装・認証承認とは分ける。

要求件数：**124件**。全件DRAFT_FOR_REVIEW。原典ARCH対応24件と追加具体化要求を区別する。正式USDM IDは全件未対応として明示している。

## SYS-RESP-001 — DER実行責務の名称

HEMS側のDER操作実行責務をDER Power Controllerとし、家庭全体の最適化・負荷実行・機器側最終制約／保護から分離すること。

**対象章：** [第03章](../chapters/03_Responsibilities.md#ch-03)　**配賦：** H側DPC／構造設計
**根拠：** SOURCE_DERIVED / A01, A02　**原典：** ARCH-001
**検証：** 文書・契約レビュー。レビュー補足：責務・依存図レビュー。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-GRID-001 — 独立した出力制御経路

一般送配電事業者のスケジュール実行をHEMSのArbiter／Orchestrator／通常更新に依存させないこと。全サーバ通信は宅内ルータ経由とし、ECHONET Lite接続PCSではPCS内の出力制御機能、RS-485接続PCSではGW G側の取得・管理・PCS指示へ配賦すること。

**対象章：** [第10章](../chapters/10_Grid_Protection.md#ch-10)　**配賦：** ECHONET Lite接続PCS内OCU／RS-485用GW G側
**根拠：** SOURCE_DERIVED / A01, A03, A08, CTX-R3, CTX-R4, SP-R4　**原典：** ARCH-002
**検証：** T01, T02。レビュー補足：T01、T02。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-GRID-002 — 独立した系統連系保護

必要な機器側計測と保護動作をHEMSの動作・応答・承認に依存させず、通常APIから規定の復帰条件を迂回できないこと。

**対象章：** [第10章](../chapters/10_Grid_Protection.md#ch-10)　**配賦：** 機器側保護構成
**根拠：** SOURCE_DERIVED / A01, A03, A07　**原典：** ARCH-003
**検証：** T03。レビュー補足：T03。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-BOUND-001 — 通常APIの禁止操作

通常HEMSのAPIから保護設定、出力制御原本、G側時計、対象ID・容量根拠、認証側FWを直接変更できないこと。必要な保守は独立経路で扱うこと。

**対象章：** [第05章](../chapters/05_Control_Contracts.md#ch-05)　**配賦：** H側API／機器側通常受付／保守境界
**根拠：** SOURCE_DERIVED / A01, A04, A06　**原典：** ARCH-004
**検証：** T04, T05。レビュー補足：T04、T05。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-GRID-003 — 必須計測・時刻・保存の独立性

系統制御に必要な計測・時刻・保存・復旧をHEMSの停止・更新時にも適用プロファイル内で成立させ、HEMS用観測の欠損を無断代替しないこと。

**対象章：** [第10章](../chapters/10_Grid_Protection.md#ch-10)　**配賦：** PCS側／GW G側（選択プロファイルによる）
**根拠：** SOURCE_DERIVED / A04, A08　**原典：** ARCH-005
**検証：** T01, T06。レビュー補足：T01、T06。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-AUTH-001 — 資源と変換グループの権威

通常制御権をresourceと競合するconversion_groupへ結び付け、同一scopeに一つの論理的権威と有効な実行系列を定めること。

**対象章：** [第03章](../chapters/03_Responsibilities.md#ch-03)　**配賦：** Control Arbiter／Orchestrator
**根拠：** SOURCE_DERIVED / A02, A05, A06　**原典：** ARCH-006
**検証：** T07, T08。レビュー補足：T07、T08。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-AUTH-002 — 最後の送信境界の再検査

送信境界でepoch・対象・期限を再検査し旧待機操作を送信しないこと。すでに送信された操作の完全取消しを仮定せず実機状態を照合すること。

**対象章：** [第05章](../chapters/05_Control_Contracts.md#ch-05)　**配賦：** DPC／共通送信境界
**根拠：** SOURCE_DERIVED / A02, A06　**原典：** ARCH-007
**検証：** T07。レビュー補足：T07。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-ORCH-001 — ワークフローと補償の所有

複数機器の順序・並行度・進行・部分失敗をOrchestratorが所有し、機器単位実行と上位再計画を分離すること。補償は現権威・現制約で再評価すること。

**対象章：** [第06章](../chapters/06_Usecases.md#ch-06)　**配賦：** Energy Orchestrator／EMS／DPC
**根拠：** SOURCE_DERIVED / A02, A03　**原典：** ARCH-008
**検証：** T09。レビュー補足：T09。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-ADAPT-001 — Adapterの政策非所有

Adapterがactorごとの独自優先度や代替計画を判断せず、機器変換・通信・通常権威の契約検査を担うこと。

**対象章：** [第03章](../chapters/03_Responsibilities.md#ch-03)　**配賦：** Device Adapter／Transport
**根拠：** SOURCE_DERIVED / A02, A06, A09　**原典：** ARCH-009
**検証：** T07。レビュー補足：コード・契約レビュー、T07。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-CAP-001 — 機器別の実能力

操作の有無、値域、モード、更新間隔、機器内失効、結果確認を型式・FW・操作ごとのプロファイルで管理し、クラスだけから対応を推定しないこと。

**対象章：** [第04章](../chapters/04_Configurations_Profiles.md#ch-04)　**配賦：** Device Registry／DPC／Adapter
**根拠：** SOURCE_DERIVED / A05, A06　**原典：** ARCH-010
**検証：** T10, T11。レビュー補足：T10、T11。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-RESULT-001 — 受理と達成の区別

Received、Authorized、Sent、DeviceAccepted、Verified、Limited、Unmet、Unknown等の意味を区別し、受理応答だけで物理目標達成を通知しないこと。

**対象章：** [第05章](../chapters/05_Control_Contracts.md#ch-05)　**配賦：** DPC／Orchestrator／外部公開
**根拠：** SOURCE_DERIVED / A03, A06　**原典：** ARCH-011
**検証：** T12。レビュー補足：T12。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-TOPO-001 — 制約scopeの分離

resource、conversion_group、connection_point、protection_domainを区別し、制御・排他・容量・計測を適切なscopeへ関連付けること。

**対象章：** [第11章](../chapters/11_Power_Constraints.md#ch-11)　**配賦：** Domain Model／機器プロファイル
**根拠：** SOURCE_DERIVED / A05, A07　**原典：** ARCH-012
**検証：** T08, T13。レビュー補足：T08、T13。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-CONST-001 — 古い制約コピー

HEMS参照用制約の欠損・失効を無制限へ変換せず、機器側の制約原本とHEMS側の品質を別々に管理すること。

**対象章：** [第08章](../chapters/08_Advanced_EMS_Loads.md#ch-08)　**配賦：** EMS／Measurement／機器側制約
**根拠：** SOURCE_DERIVED / A06, A07　**原典：** ARCH-013
**検証：** T06, T14。レビュー補足：T06、T14。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-CONST-002 — 負荷急変時の制約成立

負荷遮断・EV離脱・機器離脱時にも適用条件を満たす独立制約構成を確認し、HEMSの負荷継続だけを成立条件にしないこと。

**対象章：** [第11章](../chapters/11_Power_Constraints.md#ch-11)　**配賦：** 機器側／サイト側制約構成
**根拠：** SOURCE_DERIVED / A07, A09　**原典：** ARCH-014
**検証：** T13。レビュー補足：T13。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-ISO-001 — 実行資源非干渉

契約で許したHEMS負荷・要求頻度・異常入力の範囲でG側の性能・失敗時動作を維持し、共有CPU・メモリ・通信等を評価すること。

**対象章：** [第15章](../chapters/15_Deployment_Isolation.md#ch-15)　**配賦：** 配置設計／共有資源所有者
**根拠：** SOURCE_DERIVED / A04, A08　**原典：** ARCH-015
**検証：** T15。レビュー補足：T15。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-OTA-001 — 更新と書込み権限の分離

HEMS更新成果物と権限からG側FW・保護設定等を変更できず、必要な更新・署名検証・復旧境界を分離すること。

**対象章：** [第13章](../chapters/13_Fault_Recovery_OTA.md#ch-13)　**配賦：** OTA／権限設計／機器側
**根拠：** SOURCE_DERIVED / A04, A08　**原典：** ARCH-016
**検証：** T04, T16。レビュー補足：T04、T16。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-OTA-002 — 復帰後の再照合

HEMS再起動後は現在の機器状態・時計・プロファイル・権威を再確認し、旧ログや旧Leaseからコマンドを盲目的に再生しないこと。

**対象章：** [第13章](../chapters/13_Fault_Recovery_OTA.md#ch-13)　**配賦：** Orchestrator／DPC／Arbiter
**根拠：** SOURCE_DERIVED / A03, A06, A08　**原典：** ARCH-017
**検証：** T16, T17。レビュー補足：T16、T17。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-EXPIRY-001 — 機器内保持と利用者期限

通常要求の機器内保持・失効を実機能力として確認し、系統制約維持と利用者の終了条件を別々の受入項目とすること。

**対象章：** [第13章](../chapters/13_Fault_Recovery_OTA.md#ch-13)　**配賦：** 機器プロファイル／DPC／製品仕様
**根拠：** SOURCE_DERIVED / A06, A08　**原典：** ARCH-018
**検証：** T17。レビュー補足：T17。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-COEX-001 — 別操作元との共存

本体・別HEMS・メーカーサービスの操作と共存する条件を定義し、内部Single Writerで外部排他を保証したとせず、無限上書きを防ぐこと。

**対象章：** [第13章](../chapters/13_Fault_Recovery_OTA.md#ch-13)　**配賦：** 設置構成／Arbiter／DPC
**根拠：** SOURCE_DERIVED / A03, A09　**原典：** ARCH-019
**検証：** T18。レビュー補足：T18。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-CERT-001 — 認証・接続・版の構成台帳

JETの登録構成・申請主体・適用版、接続条件、AIF等の実装版、機器・HEMS・G側の版を関連付け、別評価を一語で取得済みとしないこと。

**対象章：** [第16章](../chapters/16_Certification_Change.md#ch-16)　**配賦：** 構成管理／認証主体
**根拠：** SOURCE_DERIVED / A04, A05, A10　**原典：** ARCH-020
**検証：** T19。レビュー補足：T19。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-ISO-002 — 共通原因の評価

HEMSとG側の共通電源・reset・時計・通信・熱を評価し、別CPUや筐体分離だけで非干渉完了と判定しないこと。

**対象章：** [第15章](../chapters/15_Deployment_Isolation.md#ch-15)　**配賦：** HW／OS／配置設計
**根拠：** SOURCE_DERIVED / A04, A08　**原典：** ARCH-021
**検証：** T15, T16。レビュー補足：T15、T16。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-CHG-001 — 通常更新の前提確認

HEMS変更ごとにAPIの意味・値・モード・頻度・機器構成・共通基盤を比較し、社内非影響判断とメーカー／JET判断・製品リリースを分離すること。

**対象章：** [第16章](../chapters/16_Certification_Change.md#ch-16)　**配賦：** 変更影響評価／製品承認
**根拠：** SOURCE_DERIVED / A04, A09, A10　**原典：** ARCH-022
**検証：** T19。レビュー補足：T19、変更影響評価。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-TIME-001 — 保護と出力制御の時間分離

保護動作、遠隔出力制御、通常計画・観測・指令の周期・期限を分け、特定経路の停止時間や特定プロパティ間隔を全体へ流用しないこと。

**対象章：** [第14章](../chapters/14_Performance_Security.md#ch-14)　**配賦：** 時間仕様／機器プロファイル
**根拠：** SOURCE_DERIVED / A01, A06, A07, A08　**原典：** ARCH-023
**検証：** T02, T03, T13。レビュー補足：T02、T03、T13。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-LOG-001 — 相関を持つ証跡

要求ID、correlation、権威世代、時刻、対象scope、観測品質、プロファイル版、実行結果を対応付けて記録し、未取得理由を推測で確定しないこと。

**対象章：** [第09章](../chapters/09_Measurement_Data.md#ch-09)　**配賦：** ログ／全責務
**根拠：** SOURCE_DERIVED / A03, A06, A10　**原典：** ARCH-024
**検証：** T12, T19。レビュー補足：T12、T19。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-SCOPE-001 — 製品と接続依存の範囲

GW製品の責務、機器側契約、設置システム全体の受入を分け、外部依存要求をGW内実装の指示と混同しないこと。

**対象章：** [第01章](../chapters/01_Scope_Baseline.md#ch-01)　**配賦：** 仕様管理
**根拠：** SOURCE_DERIVED / A01, A08　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** 文書・契約レビュー。レビュー補足：仕様・契約レビュー。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-DEPLOY-001 — 接続種別に制約された二方式の配備

PCS_DIRECTはECHONET Lite接続PCSの自律取得に、GW_MANAGEDはRS-485接続PCSのGW管理に割り当て、いずれも宅内ルータ経由のサーバ接続を必須とすること。型式・FW・取得能力・接続／認証プロファイルを確認し、方式を通信種別と無関係に自由選択できる仕様としないこと。

**対象章：** [第15章](../chapters/15_Deployment_Isolation.md#ch-15)　**配賦：** アーキテクチャレビュー
**根拠：** USER_CONTEXT_DERIVED / A01, A08, A11, CTX-R3, CTX-R4, SP-R4　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** T01, SYS-T05。レビュー補足：仕様・契約レビュー。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-REQ-001 — 要求経路の統一

EnergyGoalは必要ならEMS計画を経由し、機器指定要求も通常Arbiter→Orchestrator→実行Controllerの経路を通すこと。

**対象章：** [第06章](../chapters/06_Usecases.md#ch-06)　**配賦：** 要求受付／Arbiter／Orchestrator
**根拠：** SOURCE_DERIVED / A02, A03　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T10。レビュー補足：仕様・契約レビュー。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-RS-001 — RS-485既存機能の独立扱い

RS-485接続PCSの既存通常制御・観測を中核機能として定義し、自律HEMS機能の無効化と一括で停止する依存を既定にしないこと。例外は適用構成で明示すること。

**対象章：** [第07章](../chapters/07_DER_Connections.md#ch-07)　**配賦：** 既存PCS制御／機能設定
**根拠：** USER_CONTEXT_DERIVED / CTX　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T01。レビュー補足：仕様・契約レビュー。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-RS-002 — RS-485通信仕様プロファイル

メーカー・型式・FW・採用PCS通信文書・局番・操作・応答の意味を特定し、未提示のプロトコルやレジスタを推定で固定しないこと。

**対象章：** [第07章](../chapters/07_DER_Connections.md#ch-07)　**配賦：** RS-485接続仕様
**根拠：** USER_CONTEXT_DERIVED / CTX　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T01, SYS-T02。レビュー補足：仕様・契約レビュー。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-RS-003 — RS-485通信役割の台帳

既存RS-485について通常操作専用・系統制御必須・共用要評価・不明を区別し、所有者・全書込み元・reset・更新範囲を台帳化すること。

**対象章：** [第04章](../chapters/04_Configurations_Profiles.md#ch-04)　**配賦：** 構成管理／既存実装調査
**根拠：** USER_CONTEXT_DERIVED / CTX, A08, A11　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T05。レビュー補足：仕様・契約レビュー。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-RS-004 — 方式名で配置を決めない

通常専用RS-485はH側Adapterを候補にできる一方、必須出力制御通信はHEMS停止に依存させないこと。方式名だけで一律G側又は認証影響外と決定しないこと。

**対象章：** [第15章](../chapters/15_Deployment_Isolation.md#ch-15)　**配賦：** 配置設計
**根拠：** USER_CONTEXT_DERIVED / CTX, A01, A08　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** T01, SYS-T05。レビュー補足：仕様・契約レビュー。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-RS-005 — 生電文の迂回防止

RS-485通常指令は認可されたPort／Adapterと送信所有者を通し、既存Poller・診断・新機能からの無管理の二重Setや保護操作の迂回を防ぐこと。

**対象章：** [第07章](../chapters/07_DER_Connections.md#ch-07)　**配賦：** 通常送信境界／既存移行
**根拠：** USER_CONTEXT_DERIVED / CTX, A02, A09　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T01, T04, T07。レビュー補足：仕様・契約レビュー。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-RS-006 — 共有バス負荷と読出し

共用RS-485では通常指令だけでなく状態読出し・再試行・再初期化の影響を含めて、必須系統通信の時間・継続条件を評価すること。

**対象章：** [第14章](../chapters/14_Performance_Security.md#ch-14)　**配賦：** RS-485所有者／性能設計
**根拠：** USER_CONTEXT_DERIVED / CTX, A08　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T04, SYS-T05, T15。レビュー補足：仕様・契約レビュー。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-SEM-001 — 経路間の意味同等性

RS-485とECHONET Liteで操作の意味・単位・符号・結果を対応付けるが、能力・待ち時間を同じと仮定せず、目標電力を上限制限へ黙って変換しないこと。

**対象章：** [第07章](../chapters/07_DER_Connections.md#ch-07)　**配賦：** DPC／両Adapter
**根拠：** USER_CONTEXT_DERIVED / CTX, A06　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T02。レビュー補足：仕様・契約レビュー。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-EL-001 — Controller／Device役割の区別

GWから他社機器を操作するController側と、外部HEMSへ公開するDevice側を区別し、公開対象と実資源の対応を明示すること。

**対象章：** [第07章](../chapters/07_DER_Connections.md#ch-07)　**配賦：** ECHONET Lite接続／外部公開
**根拠：** USER_CONTEXT_DERIVED / CTX　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T03。レビュー補足：仕様・契約レビュー。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-EL-002 — 公開応答の意味

外部HEMSへの応答と内部の長時間の達成確認を区別し、採用規格の応答意味・時間を守ること。内部状態を独自の標準電文として追加しないこと。

**対象章：** [第07章](../chapters/07_DER_Connections.md#ch-07)　**配賦：** ECHONET Lite公開仕様
**根拠：** USER_CONTEXT_DERIVED / CTX, A06　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T03, T12。レビュー補足：仕様・契約レビュー。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-ROUTE-001 — 経路同一性と切替

同一機器の複数経路は同一性・操作同等性・旧権威・残留要求を確認して管理し、未確認の自動フェイルオーバーを必須機能にしないこと。

**対象章：** [第07章](../chapters/07_DER_Connections.md#ch-07)　**配賦：** Device Registry／Arbiter／DPC
**根拠：** SYSTEM_SPEC_PROPOSAL / CTX, A05, A06　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T07, T17。レビュー補足：仕様・契約レビュー。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-CAP-002 — UNKNOWNの限定運転

未知の能力・制約適用は確認済み操作又は読取専用等へ用途別に限定し、未知を無制限や対応済みにしないこと。一律停止指令にも置き換えないこと。

**対象章：** [第04章](../chapters/04_Configurations_Profiles.md#ch-04)　**配賦：** 機器対応判定／EMS
**根拠：** SOURCE_DERIVED / A05, A06　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** T10, T14。レビュー補足：仕様・契約レビュー。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-RESULT-002 — 原因不明の保持

出力が目標より小さいだけで電力会社抑制・熱・SoC等の原因を断定せず、取得できる根拠がなければreason=UNKNOWNとして扱うこと。

**対象章：** [第05章](../chapters/05_Control_Contracts.md#ch-05)　**配賦：** DPC／外部公開
**根拠：** SOURCE_DERIVED / A03, A09　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** T12, T18。レビュー補足：仕様・契約レビュー。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-RESULT-003 — 値の段階分離

要求値・送信値・確認できた設定値・実運転状態・実測を分け、取得不能な段階を未確認として公開・記録すること。

**対象章：** [第05章](../chapters/05_Control_Contracts.md#ch-05)　**配賦：** DPC／Measurement／ログ
**根拠：** SYSTEM_SPEC_PROPOSAL / A06, CTX　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T02, T12。レビュー補足：仕様・契約レビュー。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-RETRY-001 — 再送と再計画の責任

通信再送、機器操作の再実行、複数機器補償、再計画を責務で分け、多層の無制限再送や二重補償を行わないこと。

**対象章：** [第13章](../chapters/13_Fault_Recovery_OTA.md#ch-13)　**配賦：** Transport／DPC／Orchestrator／EMS
**根拠：** SOURCE_DERIVED / A02, A09　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** T09, T12。レビュー補足：仕様・契約レビュー。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-LOAD-001 — 負荷実行とDER実行

充電専用EV・給湯・空調等はFLCの責務とし、EV充放電等のDER操作と能力を区別して計画・実行すること。

**対象章：** [第08章](../chapters/08_Advanced_EMS_Loads.md#ch-08)　**配賦：** Flexible Load Controller／DPC
**根拠：** SOURCE_DERIVED / A01, A02, A05　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T10, T13。レビュー補足：仕様・契約レビュー。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-EMS-001 — 利用可能能力での計画

計画は利用可能Capability・観測品質・利用者条件・有効な参照制約に基づき、未対応機能を推測しないこと。内部自律要求も通常権威の対象とすること。

**対象章：** [第08章](../chapters/08_Advanced_EMS_Loads.md#ch-08)　**配賦：** EMS／Arbiter
**根拠：** SOURCE_DERIVED / A03, A06　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T10, T10, T14。レビュー補足：仕様・契約レビュー。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-MEAS-001 — 観測基準と品質

計測点、AC/DC、単位・符号、観測元、品質、実機時刻／受信時刻を区別し、古い値・不明値を新鮮な実測として扱わないこと。

**対象章：** [第09章](../chapters/09_Measurement_Data.md#ch-09)　**配賦：** Measurement Service
**根拠：** SOURCE_DERIVED / A02, A07　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** T06, T12, SYS-T08。レビュー補足：仕様・契約レビュー。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-MEAS-002 — 経路・オブジェクトの二重計上防止

同一Hybrid PCS、家庭全体と分岐、同一機器の異経路の計測をscopeで整理し、同じ物理量を独立出力として重複集計しないこと。

**対象章：** [第09章](../chapters/09_Measurement_Data.md#ch-09)　**配賦：** Measurement／Topology
**根拠：** USER_CONTEXT_DERIVED / A05, A07, CTX　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** T08, SYS-T04, SYS-T08。レビュー補足：仕様・契約レビュー。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-DATA-001 — 用途別保存

短期制御データ、エネルギー実績、監査記録、G側原本を用途別に定義し、保存期間・粒度・容量を未確認の一律値にしないこと。

**対象章：** [第09章](../chapters/09_Measurement_Data.md#ch-09)　**配賦：** データ仕様／製品運用
**根拠：** SYSTEM_SPEC_PROPOSAL / CTX, A11　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T08。レビュー補足：仕様・契約レビュー。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-DATA-002 — 欠測を含む抽出

計測の欠測、機器交換、時刻異常、集計基準を保った抽出方式を定義し、取得不能を0として偽装しないこと。具体形式は適用要件で確定すること。

**対象章：** [第09章](../chapters/09_Measurement_Data.md#ch-09)　**配賦：** データ仕様／外部公開
**根拠：** SYSTEM_SPEC_PROPOSAL / CTX, A07　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T08。レビュー補足：仕様・契約レビュー。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-CFG-001 — 運転調停と設定調停の分離

設定更新の反映可能状態・設定世代と通常制御権を区別し、設定RPCの受付だけでシステム全体の適用完了としないこと。

**対象章：** [第12章](../chapters/12_Configuration_Lifecycle.md#ch-12)　**配賦：** 設定Usecase／状態所有者
**根拠：** USER_CONTEXT_DERIVED / A02, CTX　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T06。レビュー補足：仕様・契約レビュー。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-CFG-002 — 通常変更と緊急復旧

高優先度実行に影響する通常設定は保留・拒否・定義済み反映を行い、緊急復旧は独立Usecaseで認可すること。通常priorityでG側権限を取得できないこと。

**対象章：** [第12章](../chapters/12_Configuration_Lifecycle.md#ch-12)　**配賦：** 設定調停／復旧Usecase
**根拠：** USER_CONTEXT_DERIVED / A02, CTX　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T06, T04。レビュー補足：仕様・契約レビュー。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-CFG-003 — 復元境界

バックアップ復元時は型式・FW・機器識別・プロファイル・設定世代を照合し、一般HEMS復元でG側設定・時計・FWを上書きしないこと。

**対象章：** [第12章](../chapters/12_Configuration_Lifecycle.md#ch-12)　**配賦：** 保守／設定管理
**根拠：** SYSTEM_SPEC_PROPOSAL / A08, CTX　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T06, T16。レビュー補足：仕様・契約レビュー。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-PERF-001 — 操作ごとの時間契約

1秒周期要求を対象機器・操作・同時台数・保証段階に結び付け、計画演算周期から全機器の毎秒設定を導かないこと。

**対象章：** [第14章](../chapters/14_Performance_Security.md#ch-14)　**配賦：** 性能設計／DPC／接続仕様
**根拠：** USER_CONTEXT_DERIVED / A06, CTX　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** T11, SYS-T04。レビュー補足：仕様・契約レビュー。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-PERF-002 — 有限な資源上限

キュー、最大頻度・バースト、再接続、保存容量等の上限と飽和時動作を定義すること。置換可能な要求だけを整理し、権威・期限を再検査すること。

**対象章：** [第14章](../chapters/14_Performance_Security.md#ch-14)　**配賦：** Runtime／送信境界
**根拠：** SOURCE_DERIVED / A06, A09　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** T05, T11, T15。レビュー補足：仕様・契約レビュー。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-SEC-001 — 接続セキュリティ文脈

従来接続と認証・暗号化接続の識別を維持し、復号後も機器識別・認証状態・経路・鮮度を許可操作へ結び付けること。

**対象章：** [第14章](../chapters/14_Performance_Security.md#ch-14)　**配賦：** Security／Transport Adapter
**根拠：** SOURCE_DERIVED / A08　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T09, T04。レビュー補足：仕様・契約レビュー。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-SEC-002 — 評価体系の分離

JC-STAR等のセキュリティ・製品運用の評価を系統連系やECHONET Lite評価と別管理し、本添付にないレベル・適用版・運用期限を確定済みとしないこと。

**対象章：** [第14章](../chapters/14_Performance_Security.md#ch-14)　**配賦：** セキュリティ要求／製品運用
**根拠：** USER_CONTEXT_DERIVED / A04, A08, CTX　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** 文書・契約レビュー。レビュー補足：仕様・契約レビュー。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-FAULT-001 — 通信断位置の区別

通常HEMSリンク、上位スケジュール通信、G側必須通信、G側計測・時刻の異常を分け、各適用プロファイルの動作で評価すること。

**対象章：** [第13章](../chapters/13_Fault_Recovery_OTA.md#ch-13)　**配賦：** 接続プロファイル／障害管理
**根拠：** SOURCE_DERIVED / A08　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T05, T02, T06。レビュー補足：仕様・契約レビュー。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-CERT-002 — 試験免除の非保証

分離構造や固定APIを将来のJET試験免除・手続き不要の保証にせず、原典の先行説明補正と個別確認の限界を保持すること。

**対象章：** [第16章](../chapters/16_Certification_Change.md#ch-16)　**配賦：** 認証影響管理
**根拠：** SOURCE_DERIVED / A04, A12　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** 文書・契約レビュー。レビュー補足：仕様・契約レビュー。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-MIG-001 — 既存経路の棚卸し

As-Isの全書込み点・権威・workflow owner・必須系統通信を調査し、中央集約を既定解にせず、資源ごとに移行所有者を切り替えること。

**対象章：** [第18章](../chapters/18_Migration.md#ch-18)　**配賦：** 移行設計／既存調査
**根拠：** USER_CONTEXT_DERIVED / A11, CTX　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T01, T07。レビュー補足：仕様・契約レビュー。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-MIG-002 — Legacy適用差

Domain／Port／テストを共通化しても、Legacyが分離条件を満たさなければNextと同じ非干渉・更新・運転保証を適用しないこと。

**対象章：** [第18章](../chapters/18_Migration.md#ch-18)　**配賦：** 製品構成管理／移行
**根拠：** SOURCE_DERIVED / A11　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** 文書・契約レビュー。レビュー補足：仕様・契約レビュー。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-BASE-001 — ドラフトと評価状態

原典のDEC・TBD・ARCH・T番号を維持し、本書の追加提案を識別すること。文書QA、実装、実機、認証判断を別状態で記録すること。

**対象章：** [第01章](../chapters/01_Scope_Baseline.md#ch-01)　**配賦：** 文書・構成管理
**根拠：** SOURCE_DERIVED / A10, A11　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** 文書・契約レビュー。レビュー補足：仕様・契約レビュー。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-VERIFY-001 — 検証条件と証拠

要求・型式・版・接続・profile・測定点・閾値・評価窓・注入位置をrun_idへ関連付け、未確定又は未実施をPASSにしないこと。

**対象章：** [第17章](../chapters/17_Verification.md#ch-17)　**配賦：** 検証責任者
**根拠：** SOURCE_DERIVED / A10　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** T19。レビュー補足：仕様・契約レビュー。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-CTX-001 — 外部役割の分離

一般送配電事業者、FW配信、上位管理・監視、宅内Web UI、リモートアプリ、宅内ルータを論理的に識別し、同一物理基盤であっても通信・権限・障害・更新の責任を区別すること。

**対象章：** [第02章](../chapters/02_System_Context.md#ch-02)　**配賦：** システム構成／サービス責任者
**根拠：** USER_CONTEXT_DERIVED / CTX-R2, SP-R2　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T11。レビュー補足：R2接続・権限・状態・負荷プロファイルで検証。閾値未確定で包括的PASSを付けない。。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-CTX-002 — GWと外部サービスの保証境界

GW製品機能とクラウド・アプリ・ルータ・接続機器への依存条件を分け、接続開始方向、対象版、可用性、責任者を接続プロファイルで管理すること。

**対象章：** [第02章](../chapters/02_System_Context.md#ch-02)　**配賦：** 製品・サービスIF管理
**根拠：** SYSTEM_SPEC_PROPOSAL / CTX-R2, SP-R2　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T11, SYS-T13。レビュー補足：R2接続・権限・状態・負荷プロファイルで検証。閾値未確定で包括的PASSを付けない。。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-NORTH-001 — 用途別Usecaseへの振分け

上位と宅内からの要求を情報取得、通常運転、設定変更、GW内部操作、FW更新へ分類し、認可・相関を共通化しつつ各状態所有者へ配賦すること。通常運転以外を一律DPCへ通さないこと。

**対象章：** [第20章](../chapters/20_Northbound_Monitoring_FW.md#ch-20)　**配賦：** 要求受付／各Usecase
**根拠：** USER_CONTEXT_DERIVED / CTX-R2, SP-R2　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T11, SYS-T17。レビュー補足：R2接続・権限・状態・負荷プロファイルで検証。閾値未確定で包括的PASSを付けない。。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-NORTH-002 — 操作者と配送主体の認可

上位接続主体と委譲された操作者、住宅・GW・所属世代、操作scopeを認証・認可し、自己申告のactorやpriorityだけで権限を付与しないこと。

**対象章：** [第20章](../chapters/20_Northbound_Monitoring_FW.md#ch-20)　**配賦：** 境界認可／上位サービス
**根拠：** SYSTEM_SPEC_PROPOSAL / CTX-R2, SP-R2　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T14, SYS-T16。レビュー補足：R2接続・権限・状態・負荷プロファイルで検証。閾値未確定で包括的PASSを付けない。。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-NORTH-003 — オフライン要求の有限性

操作別にオフライン時の拒否又は明示的な期限付き保留を規定し、配送・実行時に期限、権限、所属・設定世代を再検査すること。旧要求を再接続だけで復活させないこと。

**対象章：** [第20章](../chapters/20_Northbound_Monitoring_FW.md#ch-20)　**配賦：** 上位キュー／GW受付
**根拠：** SYSTEM_SPEC_PROPOSAL / CTX-R2, SP-R2　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T16, SYS-T24。レビュー補足：R2接続・権限・状態・負荷プロファイルで検証。閾値未確定で包括的PASSを付けない。。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-NORTH-004 — 重複排除と結果照合

要求の主体・対象・世代・種別をscopeに重複を管理し、同じキーで異なる内容を拒否すること。結果不明時は追跡IDで照合し、保証期間外の完全exactly-onceを主張しないこと。

**対象章：** [第20章](../chapters/20_Northbound_Monitoring_FW.md#ch-20)　**配賦：** GW要求記録／上位配送
**根拠：** SYSTEM_SPEC_PROPOSAL / CTX-R2, SP-R2　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T16, SYS-T21。レビュー補足：R2接続・権限・状態・負荷プロファイルで検証。閾値未確定で包括的PASSを付けない。。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-NORTH-005 — 有限な監視・診断負荷

宅内・上位・アプリの監視を公開Viewへ集約し、Fresh Read・履歴・診断の取得量、頻度、並行度と中断条件を制限すること。端末増加に比例する無制限の実機ポーリングを生じさせないこと。

**対象章：** [第09章](../chapters/09_Measurement_Data.md#ch-09)　**配賦：** Query／Telemetry／資源管理
**根拠：** SYSTEM_SPEC_PROPOSAL / CTX-R2, SP-R2　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T18, SYS-T25。レビュー補足：R2接続・権限・状態・負荷プロファイルで検証。閾値未確定で包括的PASSを付けない。。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-NORTH-006 — イベントの欠落と再同期

stream・起動世代・順序を識別し、重複・逆転・欠落・バッファあふれを検知して品質表示と状態再同期を行うこと。操作結果・設定監査と計測の保持方針を区別すること。

**対象章：** [第09章](../chapters/09_Measurement_Data.md#ch-09)　**配賦：** Telemetry／上位保存
**根拠：** SYSTEM_SPEC_PROPOSAL / CTX-R2, SP-R2　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T21, SYS-T28。レビュー補足：R2接続・権限・状態・負荷プロファイルで検証。閾値未確定で包括的PASSを付けない。。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-NORTH-007 — チャネル非依存の操作権限と監査

宅内・上位・アプリの入口だけで優先度・管理権限を決めず、認可された操作者とscopeを用いること。要求、設定版、Job、配送主体、結果を相関して監査できること。

**対象章：** [第20章](../chapters/20_Northbound_Monitoring_FW.md#ch-20)　**配賦：** 認可／監査／通常調停
**根拠：** SYSTEM_SPEC_PROPOSAL / CTX-R2, SP-R2　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T14, SYS-T15, SYS-T21。レビュー補足：R2接続・権限・状態・負荷プロファイルで検証。閾値未確定で包括的PASSを付けない。。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-CFG-004 — 設定世代の競合検査

同じ設定scopeに対する基準世代の検査と予約・commitを設定所有者で整合させ、古い世代の同時変更を競合又は明示的調整として処理すること。

**対象章：** [第12章](../chapters/12_Configuration_Lifecycle.md#ch-12)　**配賦：** Configuration Service
**根拠：** SYSTEM_SPEC_PROPOSAL / CTX-R2, SP-R2　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T15。レビュー補足：R2接続・権限・状態・負荷プロファイルで検証。閾値未確定で包括的PASSを付けない。。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-CFG-005 — 希望・保存・有効設定の分離

クラウド希望値、GWの受理・保存設定、各反映先の有効設定を区別し、部分反映を公開すること。再接続・リストアで古いクラウド希望値を無条件適用しないこと。

**対象章：** [第12章](../chapters/12_Configuration_Lifecycle.md#ch-12)　**配賦：** Configuration Service／上位同期
**根拠：** SYSTEM_SPEC_PROPOSAL / CTX-R2, SP-R2　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T15, SYS-T28。レビュー補足：R2接続・権限・状態・負荷プロファイルで検証。閾値未確定で包括的PASSを付けない。。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-CFG-006 — ネットワーク設定の到達性確認

経路を変更する設定について、事前検証、反映Job、確認チャネル、確定条件、認可された復旧を規定し、G側共有経路への影響を評価してから許可すること。

**対象章：** [第12章](../chapters/12_Configuration_Lifecycle.md#ch-12)　**配賦：** 接続管理／設定調停
**根拠：** SYSTEM_SPEC_PROPOSAL / CTX-R2, SP-R2　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T13, SYS-T22。レビュー補足：R2接続・権限・状態・負荷プロファイルで検証。閾値未確定で包括的PASSを付けない。。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-GWOP-001 — 内部機能操作の許可リスト

GW内部機能操作を対象・パラメータ・状態・scope・権限・結果を持つ明示Usecaseとして公開し、任意shell・DB・メモリ・PCS生電文等の書込みへ拡張しないこと。

**対象章：** [第20章](../chapters/20_Northbound_Monitoring_FW.md#ch-20)　**配賦：** Lifecycle・Operation Service
**根拠：** USER_CONTEXT_DERIVED / CTX-R2, SP-R2　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T17, SYS-T23。レビュー補足：R2接続・権限・状態・負荷プロファイルで検証。閾値未確定で包括的PASSを付けない。。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-GWOP-002 — 高影響操作と変更の排他

GW内部再起動・停止・設定反映・FW適用の共有影響scopeを調整し、前提状態、取消し、結果不明、復帰を管理すること。リセットや復元がG側へ及ぶものをH側操作として無条件許可しないこと。

**対象章：** [第12章](../chapters/12_Configuration_Lifecycle.md#ch-12)　**配賦：** ライフサイクル／設定／更新管理
**根拠：** SYSTEM_SPEC_PROPOSAL / CTX-R2, SP-R2　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T17, SYS-T20, SYS-T22。レビュー補足：R2接続・権限・状態・負荷プロファイルで検証。閾値未確定で包括的PASSを付けない。。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-UI-001 — 直接無線の宅内Web UI

端末ブラウザからGWへ直接無線で接続する宅内監視・許可操作の利用構成を定義し、到達先、認証、開始・終了条件、クラウド不通時の利用範囲を規定すること。

**対象章：** [第20章](../chapters/20_Northbound_Monitoring_FW.md#ch-20)　**配賦：** Local Web UI／無線管理
**根拠：** USER_CONTEXT_DERIVED / CTX-R2, SP-R2　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T12。レビュー補足：R2接続・権限・状態・負荷プロファイルで検証。閾値未確定で包括的PASSを付けない。。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-UI-002 — ルータ経由の宅内Web UI

端末から宅内ルータを介した無線接続でGWのWeb UIを利用する構成を定義し、端末隔離、セグメント、発見・到達、クラウド不要の条件を示すこと。

**対象章：** [第20章](../chapters/20_Northbound_Monitoring_FW.md#ch-20)　**配賦：** Local Web UI／接続プロファイル
**根拠：** USER_CONTEXT_DERIVED / CTX-R2, SP-R2　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T13。レビュー補足：R2接続・権限・状態・負荷プロファイルで検証。閾値未確定で包括的PASSを付けない。。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-UI-003 — 直接接続とWANの独立した可用性

直接無線接続、ルータ接続、AP／STA同時動作、WAN到達、上位同期を別属性とし、直接接続をインターネット共有又は同時動作保証へ読み替えないこと。

**対象章：** [第02章](../chapters/02_System_Context.md#ch-02)　**配賦：** 製品構成／無線管理
**根拠：** SYSTEM_SPEC_PROPOSAL / CTX-R2, SP-R2　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T12, SYS-T13, SYS-T22。レビュー補足：R2接続・権限・状態・負荷プロファイルで検証。閾値未確定で包括的PASSを付けない。。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-UI-004 — クラウド非依存のローカル利用

基本画面・必要なローカルAPI・事前に確立したローカル認可を用い、外部サービス断でも条件内で宅内監視を可能とすること。クラウド不要を認証不要にせず、初回登録・失効条件を別定義すること。

**対象章：** [第20章](../chapters/20_Northbound_Monitoring_FW.md#ch-20)　**配賦：** Local Web UI／認可
**根拠：** SYSTEM_SPEC_PROPOSAL / CTX-R2, SP-R2　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T12, SYS-T23, SYS-T24。レビュー補足：R2接続・権限・状態・負荷プロファイルで検証。閾値未確定で包括的PASSを付けない。。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-UI-005 — Web境界と互換性

直接・LAN接続でも接続先識別・暗号化・セッション・Origin等を保護し、CSRF・不正クロスオリジン・名前解決悪用等への対策と試験を定めること。Web資産とAPI非互換時の動作を規定すること。

**対象章：** [第14章](../chapters/14_Performance_Security.md#ch-14)　**配賦：** Web／セキュリティ／リリース
**根拠：** SYSTEM_SPEC_PROPOSAL / CTX-R2, SP-R2　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T23, SYS-T27。レビュー補足：R2接続・権限・状態・負荷プロファイルで検証。閾値未確定で包括的PASSを付けない。。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-APP-001 — クラウド経由リモートアプリ

スマートフォンアプリと上位クラウド及び対象GWを結ぶ監視・操作経路を定義し、対象住宅・GW、役割、操作結果を対応付けること。GWの直接WAN公開やスマートフォン中継を必須にしないこと。

**対象章：** [第20章](../chapters/20_Northbound_Monitoring_FW.md#ch-20)　**配賦：** アプリ／上位サービス／GW
**根拠：** USER_CONTEXT_DERIVED / CTX-R2, SP-R2　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T14, SYS-T24。レビュー補足：R2接続・権限・状態・負荷プロファイルで検証。閾値未確定で包括的PASSを付けない。。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-APP-002 — 受付段階と鮮度の表示

アプリ・Web・上位でクラウド受付、GW受付、設定反映、内部Job完了、機器受理と達成、FW稼働確認を区別し、古い情報・接続不能・結果不明を明示すること。

**対象章：** [第20章](../chapters/20_Northbound_Monitoring_FW.md#ch-20)　**配賦：** 公開API／Web／アプリ
**根拠：** SYSTEM_SPEC_PROPOSAL / CTX-R2, SP-R2　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T21, SYS-T24。レビュー補足：R2接続・権限・状態・負荷プロファイルで検証。閾値未確定で包括的PASSを付けない。。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-APP-003 — 所属変更と資格失効

所有者変更・GW再登録・紛失端末等の処理で所属世代、上位・ローカル資格、待機要求、履歴のアクセスを整合させること。失効通知を受信できない期間の権限寿命と制限を明示すること。

**対象章：** [第20章](../chapters/20_Northbound_Monitoring_FW.md#ch-20)　**配賦：** 認可／登録／上位アプリ
**根拠：** SYSTEM_SPEC_PROPOSAL / CTX-R2, SP-R2　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T14, SYS-T26。レビュー補足：R2接続・権限・状態・負荷プロファイルで検証。閾値未確定で包括的PASSを付けない。。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-FW-001 — 配信と承認と適用の分離

FW配布物の承認・認証、配送、対象・適用時期の運用要求、GWでの検証・適用・復帰を別責務とし、配送成功を適用許可・更新成功と扱わないこと。

**対象章：** [第20章](../chapters/20_Northbound_Monitoring_FW.md#ch-20)　**配賦：** リリース管理／FWサーバ／Update Manager
**根拠：** USER_CONTEXT_DERIVED / CTX-R2, SP-R2, EXT-FW-01, EXT-FW-02　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T11, SYS-T19, SYS-T20。レビュー補足：R2接続・権限・状態・負荷プロファイルで検証。閾値未確定で包括的PASSを付けない。。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-FW-002 — 配布物の対象・完全性・系列確認

FWと保護されたメタデータの真正性・完全性、対象機種・HW・依存版・領域・サイズ・許可更新系列・現在状態を検査し、検証不適合な配布物を通常経路から適用しないこと。

**対象章：** [第20章](../chapters/20_Northbound_Monitoring_FW.md#ch-20)　**配賦：** Update Manager／更新権限
**根拠：** SYSTEM_SPEC_PROPOSAL / CTX-R2, SP-R2, EXT-FW-01, EXT-FW-02　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T19。レビュー補足：R2接続・権限・状態・負荷プロファイルで検証。閾値未確定で包括的PASSを付けない。。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-FW-003 — H/G更新権限と認可復旧

H側の配布物・キー・書込み経路からG側FW・設定へ到達できないこと。復旧用の版と設定schemaを認可し、任意ダウングレードと管理された復旧を区別すること。

**対象章：** [第13章](../chapters/13_Fault_Recovery_OTA.md#ch-13)　**配賦：** 更新・起動機構／権限境界
**根拠：** SYSTEM_SPEC_PROPOSAL / CTX-R2, SP-R2, EXT-FW-01, EXT-FW-02　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T19, SYS-T20。レビュー補足：R2接続・権限・状態・負荷プロファイルで検証。閾値未確定で包括的PASSを付けない。。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-FW-004 — 更新段階と永続復旧情報

取得、検証、適用待ち、適用、起動、稼働確認、復旧を別状態として記録・通知し、段階別に中断・取消し・再開を定義すること。正常終了前処理だけをG側継続の根拠にしないこと。

**対象章：** [第13章](../chapters/13_Fault_Recovery_OTA.md#ch-13)　**配賦：** Update Manager／ライフサイクル
**根拠：** SYSTEM_SPEC_PROPOSAL / CTX-R2, SP-R2, EXT-FW-01, EXT-FW-02　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T20, SYS-T21。レビュー補足：R2接続・権限・状態・負荷プロファイルで検証。閾値未確定で包括的PASSを付けない。。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-FW-005 — 配信障害と更新転送負荷の限定

FW配信断・取得失敗だけで現行の通常運転・監視を停止させないこと。転送・再試行・保存・CPUの上限とG側共有経路への非干渉条件を規定すること。

**対象章：** [第14章](../chapters/14_Performance_Security.md#ch-14)　**配賦：** 更新通信／資源管理
**根拠：** SYSTEM_SPEC_PROPOSAL / CTX-R2, SP-R2, EXT-FW-01, EXT-FW-02　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T18, SYS-T25。レビュー補足：R2接続・権限・状態・負荷プロファイルで検証。閾値未確定で包括的PASSを付けない。。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-STATE-001 — 内部情報の選択的公開

GW内部情報・状態を許可された公開Viewとして提供し、主体と住宅・GWのscopeで制限すること。秘密鍵・資格情報・不要な個人情報等を診断・ログに混入させないこと。

**対象章：** [第09章](../chapters/09_Measurement_Data.md#ch-09)　**配賦：** Query／診断／情報管理
**根拠：** USER_CONTEXT_DERIVED / CTX-R2, SP-R2　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T18, SYS-T23。レビュー補足：R2接続・権限・状態・負荷プロファイルで検証。閾値未確定で包括的PASSを付けない。。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-STATE-002 — 観測とクラウドコピーの区別

実機観測、GW取得、クラウド受信、表示の時刻・品質と版を区別し、時刻不明を偽装しないこと。クラウドコピーを機器実状態又はGW有効設定の正本としないこと。

**対象章：** [第09章](../chapters/09_Measurement_Data.md#ch-09)　**配賦：** Measurement／上位保存／UI
**根拠：** SYSTEM_SPEC_PROPOSAL / CTX-R2, SP-R2　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T21, SYS-T28。レビュー補足：R2接続・権限・状態・負荷プロファイルで検証。閾値未確定で包括的PASSを付けない。。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-SVC-001 — サービス・UI・FW互換性の管理

GW、Web/API、上位API、アプリ、設定schema、FW配布物、機器プロファイルの互換範囲をリリースへ関連付け、未知操作・非互換時の拒否又は限定動作を定義すること。

**対象章：** [第16章](../chapters/16_Certification_Change.md#ch-16)　**配賦：** リリース・構成管理
**根拠：** SYSTEM_SPEC_PROPOSAL / CTX-R2, SP-R2　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T27。レビュー補足：R2接続・権限・状態・負荷プロファイルで検証。閾値未確定で包括的PASSを付けない。。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-ISO-003 — 外部接続追加時の共有影響

ルータ、無線、NIC、帯域、clock、reset、電源等の共有依存を台帳化し、Web・上位設定・FW・内部操作による変更がG側独立性を壊さないことを確認すること。

**対象章：** [第15章](../chapters/15_Deployment_Isolation.md#ch-15)　**配賦：** 配置／共有資源／検証
**根拠：** SYSTEM_SPEC_PROPOSAL / CTX-R2, SP-R2　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T18, SYS-T22, SYS-T25。レビュー補足：R2接続・権限・状態・負荷プロファイルで検証。閾値未確定で包括的PASSを付けない。。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-CHG-002 — クラウド・UI変更の非影響判定

クラウド・Web・アプリだけの変更でも、通常要求の頻度・モード・値域・対象・設定・共有資源の前提変化を評価し、名称だけで認証影響外又は試験不要と判断しないこと。

**対象章：** [第16章](../chapters/16_Certification_Change.md#ch-16)　**配賦：** 変更管理／認証主体との確認
**根拠：** SYSTEM_SPEC_PROPOSAL / CTX-R2, SP-R2　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T27。レビュー補足：R2接続・権限・状態・負荷プロファイルで検証。閾値未確定で包括的PASSを付けない。。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-GSEL-001 — 機器接続別の取得・適用契約

ECHONET Lite接続PCSではPCS_DIRECTとしてPCS内機能が宅内ルータ経由で取得・検証・保存・時刻適用を行うこと。RS-485接続PCSではGW_MANAGEDとしてGW G側が宅内ルータ経由で取得・管理し、RS-485によるPCS指示・必要監視を担うこと。後者を透過中継に縮めないこと。

**対象章：** [第21章](../chapters/21_Grid_Connection_Selection.md#ch-21)　**配賦：** プロファイル・PCS／GW G側
**根拠：** USER_CONTEXT_DERIVED / CTX-R3, SP-R3, CTX-R4, SP-R4　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T29, SYS-T30。レビュー補足：方式別プロファイル・選択条件・機器動作のレビュー。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-GSEL-002 — 確認済み構成からの選択

方式をR4の機器接続別対応表と型式・HW/FW・取得能力・接続契約・認証構成へ結び付けること。RS-485接続PCSのPCS_DIRECT、ECHONET Lite接続PCSのGW_MANAGED、非PCSのPCS_DIRECT及び未確認の構成を現行対応範囲として自動有効化しないこと。

**対象章：** [第21章](../chapters/21_Grid_Connection_Selection.md#ch-21)　**配賦：** 製品構成管理
**根拠：** SYSTEM_SPEC_PROPOSAL / CTX-R3, SP-R3, CTX-R4, SP-R4　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T31。レビュー補足：方式別プロファイル・選択条件・機器動作のレビュー。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-GSEL-003 — scopeと適用主体の一意性

同じスケジュール適用scopeの能動主体を一つとし、重複対象と共有変換グループを検査すること。PCSの保護・機器制限をこの排他に含めて無効化しないこと。

**対象章：** [第21章](../chapters/21_Grid_Connection_Selection.md#ch-21)　**配賦：** G側構成管理・PCS
**根拠：** SYSTEM_SPEC_PROPOSAL / CTX-R3, SP-R3　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T32, SYS-T41。レビュー補足：方式別プロファイル・選択条件・機器動作のレビュー。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-GSEL-004 — 通常要求経路の非迂回

両方式で通常Arbiter・Orchestrator・DPCの役割を維持し、通常要求がPCS側又はG側の系統制約強制を迂回できないこと。

**対象章：** [第21章](../chapters/21_Grid_Connection_Selection.md#ch-21)　**配賦：** H側DPC・G側・PCS
**根拠：** SYSTEM_SPEC_PROPOSAL / CTX-R3, SP-R3　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T29, SYS-T30, SYS-T39。レビュー補足：方式別プロファイル・選択条件・機器動作のレビュー。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-GSEL-005 — GW管理方式のH側非依存

GW_MANAGEDの取得・保存・時計・PCS指示・必要監視をH側停止・更新・高負荷に依存させないこと。実行配置と共有driver・resetを証拠化すること。

**対象章：** [第21章](../chapters/21_Grid_Connection_Selection.md#ch-21)　**配賦：** GW G側・配置設計
**根拠：** SYSTEM_SPEC_PROPOSAL / CTX-R3, SP-R3　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T30, SYS-T35, SYS-T39。レビュー補足：方式別プロファイル・選択条件・機器動作のレビュー。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-GSEL-006 — 正本と資格情報の領域分離

スケジュール・時刻・対象情報・資格情報の正本を選択されたPCS側又はGW G側に保持し、H側は必要な読取コピーのみを利用すること。

**対象章：** [第21章](../chapters/21_Grid_Connection_Selection.md#ch-21)　**配賦：** PCS／GW G側・公開サービス
**根拠：** SYSTEM_SPEC_PROPOSAL / CTX-R3, SP-R3　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T29, SYS-T30, SYS-T37, SYS-T38。レビュー補足：方式別プロファイル・選択条件・機器動作のレビュー。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-GSEL-007 — 適用条件内の施工保守による構成変更

方式に影響する変更を機器・接続構成の管理変更とし、独立認可・期待設定世代・R4適用表・必要手続き・実機確認を満たすこと。認可された保守であっても適用外の方式組合せを許可しないこと。同一PCSの任意切替を必須機能としないこと。

**対象章：** [第21章](../chapters/21_Grid_Connection_Selection.md#ch-21)　**配賦：** 系統保守・構成管理
**根拠：** SYSTEM_SPEC_PROPOSAL / CTX-R3, SP-R3, CTX-R4, SP-R4　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T31, SYS-T33, SYS-T40。レビュー補足：方式別プロファイル・選択条件・機器動作のレビュー。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-GSEL-008 — 制約を維持する引継ぎ

新主体を非能動で準備し、切替中の確認済み制約保持又は必要停止を成立させ、旧適用主体の停止・フェンスを確認してから新主体を有効化すること。保護・最終制約を解除しないこと。

**対象章：** [第21章](../chapters/21_Grid_Connection_Selection.md#ch-21)　**配賦：** G側保守・PCS
**根拠：** SYSTEM_SPEC_PROPOSAL / CTX-R3, SP-R3　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T33, SYS-T34。レビュー補足：方式別プロファイル・選択条件・機器動作のレビュー。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-GSEL-009 — 古い経路と残留指令の無効化

切替で系統構成世代を更新し、旧送信元・キュー・遅延応答・PCS残留を確認すること。PCS非対応の世代番号だけで実機の排他を保証しないこと。

**対象章：** [第21章](../chapters/21_Grid_Connection_Selection.md#ch-21)　**配賦：** 最終通信境界・PCS
**根拠：** SYSTEM_SPEC_PROPOSAL / CTX-R3, SP-R3　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T32, SYS-T34, SYS-T42。レビュー補足：方式別プロファイル・選択条件・機器動作のレビュー。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-GSEL-010 — 自動方式切替の非採用

通信断・監視断・時刻異常を理由とする無条件の他方式への自動切替を行わず、同じ方式で保持情報と適用プロファイルの縮退・復旧に従うこと。

**対象章：** [第21章](../chapters/21_Grid_Connection_Selection.md#ch-21)　**配賦：** PCS／GW G側・運用
**根拠：** SYSTEM_SPEC_PROPOSAL / CTX-R3, SP-R3　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T36。レビュー補足：方式別プロファイル・選択条件・機器動作のレビュー。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-GSEL-011 — H停止とGW全体喪失の区別

GW_MANAGEDでH側限定停止とGW全体電源断を区別し、後者ではPCSの必須通信喪失時動作を評価すること。H/G分離から全筐体無停止を保証しないこと。

**対象章：** [第21章](../chapters/21_Grid_Connection_Selection.md#ch-21)　**配賦：** G側・PCS・障害管理
**根拠：** SYSTEM_SPEC_PROPOSAL / CTX-R3, SP-R3　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T35, SYS-T36。レビュー補足：方式別プロファイル・選択条件・機器動作のレビュー。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-GSEL-012 — 共用PCS通信の所有

共用ポート・設定を二主体が独立書込みしないこと。G側最終送信所有又は確認済みの機器側独立チャネルで制約を維持し、通常読出し・FW転送で必須通信を阻害しないこと。

**対象章：** [第21章](../chapters/21_Grid_Connection_Selection.md#ch-21)　**配賦：** G側通信・Adapter・PCS
**根拠：** SYSTEM_SPEC_PROPOSAL / CTX-R3, SP-R3　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T39。レビュー補足：方式別プロファイル・選択条件・機器動作のレビュー。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-GSEL-013 — 表示状態と実適用の分離

desired/configured/active mode、機器接続種別、宅内ルータ経路、取得主体、scope、適用状態、観測時刻・品質、構成変更Jobを区別すること。PCS_DIRECTの表示をPCS自律取得方式（宅内ルータ経由・GW非経由）とし、GWのWAN到達やECHONET Lite応答からPCSのサーバ取得成功を推定しないこと。

**対象章：** [第21章](../chapters/21_Grid_Connection_Selection.md#ch-21)　**配賦：** Query・Telemetry・上位／Web／アプリ
**根拠：** SYSTEM_SPEC_PROPOSAL / CTX-R3, SP-R3, CTX-R4, SP-R4　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T38。レビュー補足：方式別プロファイル・選択条件・機器動作のレビュー。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-GSEL-014 — 非公開状態の扱い

PCS_DIRECTで取得できないスケジュール版・制限理由等をUNKNOWN又はNOT_EXPOSEDとして扱い、推定を原本又は確定原因として公開しないこと。

**対象章：** [第21章](../chapters/21_Grid_Connection_Selection.md#ch-21)　**配賦：** 公開サービス
**根拠：** SYSTEM_SPEC_PROPOSAL / CTX-R3, SP-R3　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T38。レビュー補足：方式別プロファイル・選択条件・機器動作のレビュー。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-GSEL-015 — H更新と方式bindingの不変

H側FW更新・一般バックアップ／リストアから方式binding、G側原本・資格・時刻・FWを変更しないこと。G側更新は独立した対象・認可・評価・復旧で管理すること。

**対象章：** [第21章](../chapters/21_Grid_Connection_Selection.md#ch-21)　**配賦：** H/G更新管理
**根拠：** SYSTEM_SPEC_PROPOSAL / CTX-R3, SP-R3　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T37, SYS-T40。レビュー補足：方式別プロファイル・選択条件・機器動作のレビュー。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-GSEL-016 — 方式別の認証構成評価

二方式それぞれの機器・GW G側・計測・通信・FW・設定・適用版を評価し、一方の認証確認又は社内PASSを他方式へ無条件転用しないこと。

**対象章：** [第21章](../chapters/21_Grid_Connection_Selection.md#ch-21)　**配賦：** 認証主体・変更管理
**根拠：** SYSTEM_SPEC_PROPOSAL / CTX-R3, SP-R3　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T40。レビュー補足：方式別プロファイル・選択条件・機器動作のレビュー。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-GSEL-017 — 共有scopeの全体制約

RS-485接続PCSのGW管理とECHONET Lite接続PCSの自律取得が同一住宅に混在する場合、各経路は宅内ルータを共有してよいが、重複するスケジュール適用scopeと共有PCS・連系点の容量配分を確認すること。HEMS最適化やルータを全体制約の唯一の適用主体にしないこと。

**対象章：** [第21章](../chapters/21_Grid_Connection_Selection.md#ch-21)　**配賦：** トポロジー・G側構成
**根拠：** SYSTEM_SPEC_PROPOSAL / CTX-R3, SP-R3, CTX-R4, SP-R4　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T41。レビュー補足：方式別プロファイル・選択条件・機器動作のレビュー。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-GSEL-018 — 切替中断時の永続復旧

切替中のJobと構成世代を永続記録し、電断・再起動後は有効主体と実機状態を照合してから復旧すること。結果不明時の盲目的な旧方式復元又は新旧同時適用を禁止すること。

**対象章：** [第21章](../chapters/21_Grid_Connection_Selection.md#ch-21)　**配賦：** 系統構成管理・PCS
**根拠：** SYSTEM_SPEC_PROPOSAL / CTX-R3, SP-R3　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T34, SYS-T42。レビュー補足：方式別プロファイル・選択条件・機器動作のレビュー。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-GSEL-019 — 機器交換と再登録

PCS又はGW交換・工場初期化・対象登録変更で旧資格・旧scope・旧設定を無条件に復元せず、対応プロファイルと現在の制約成立を再確認すること。

**対象章：** [第21章](../chapters/21_Grid_Connection_Selection.md#ch-21)　**配賦：** 保守・登録・移行
**根拠：** SYSTEM_SPEC_PROPOSAL / CTX-R3, SP-R3　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T31, SYS-T42。レビュー補足：方式別プロファイル・選択条件・機器動作のレビュー。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-GSEL-020 — 選択と適用結果の監査

方式選択・変更の主体、理由、旧新mode・設定世代・scope、検証／切替各段階、認証等の確認記録、実機確認結果を相関付け、未完了・不明と完了を区別して保持すること。

**対象章：** [第21章](../chapters/21_Grid_Connection_Selection.md#ch-21)　**配賦：** 監査・構成管理
**根拠：** SYSTEM_SPEC_PROPOSAL / CTX-R3, SP-R3　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T33, SYS-T38, SYS-T40, SYS-T42。レビュー補足：方式別プロファイル・選択条件・機器動作のレビュー。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-GNET-001 — 宅内ルータ必須経路

出力制御サーバ向けのPCS又はGW G側の取得要求と取得応答は、すべて宅内ルータを経由すること。ルータを省いた経路、GW経由のPCS代理取得、スマートフォンのテザリング等を自動的な代替経路として追加しないこと。

**対象章：** [第02章](../chapters/02_System_Context.md#ch-02)　**配賦：** 通信構成・PCS／GW G側
**根拠：** USER_CONTEXT_DERIVED / CTX-R4, SP-R4　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T43, SYS-T44。レビュー補足：R4のルータ経路・機器接続別契約を資料・シミュレータ・実機で分けて確認。静的検査を実機試験と扱わない。。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-GNET-002 — PCS自律取得の対象限定

GW非経由のPCS自律取得はECHONET Lite接続PCSだけを対象とし、GW H側・G側をアプリケーション代理取得者又は必須のIP転送・NAT・ブリッジとして介在させないこと。非PCS機器やGWの仮想公開オブジェクトへ自律取得権限を一般化しないこと。

**対象章：** [第21章](../chapters/21_Grid_Connection_Selection.md#ch-21)　**配賦：** 機器プロファイル・ネットワーク配置
**根拠：** USER_CONTEXT_DERIVED / CTX-R4, SP-R4　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T43, SYS-T45, SYS-T50。レビュー補足：R4のルータ経路・機器接続別契約を資料・シミュレータ・実機で分けて確認。静的検査を実機試験と扱わない。。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-GNET-003 — RS-485のGW管理経路

RS-485接続PCSのスケジュール取得・管理は宅内ルータ経由でGW G側が担い、適用する制約又は制約適用済み指令をRS-485へ送出し、必要な監視を継続すること。PCS自身が出力制御サーバへ接続する経路を当該構成へ設けないこと。

**対象章：** [第21章](../chapters/21_Grid_Connection_Selection.md#ch-21)　**配賦：** GW G側・PCS通信所有者
**根拠：** USER_CONTEXT_DERIVED / CTX-R4, SP-R4　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T44, SYS-T48。レビュー補足：R4のルータ経路・機器接続別契約を資料・シミュレータ・実機で分けて確認。静的検査を実機試験と扱わない。。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-GNET-004 — 通常EL通信と出力制御サーバ通信の分離

ECHONET LiteによるGW–PCSの通常操作・観測と、PCS–出力制御サーバの取得通信を別契約として識別すること。後者のプロトコル・資格情報・時刻・保存は機器プロファイルで確認し、ECHONET Liteクラス検出だけで取得能力を認定しないこと。

**対象章：** [第07章](../chapters/07_DER_Connections.md#ch-07)　**配賦：** Device Registry・EL Adapter・PCS
**根拠：** SYSTEM_SPEC_PROPOSAL / CTX-R4, SP-R4　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T43, SYS-T45, SYS-T49。レビュー補足：R4のルータ経路・機器接続別契約を資料・シミュレータ・実機で分けて確認。静的検査を実機試験と扱わない。。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-GNET-005 — ルータ共有障害と保持動作

WAN断、宅内ルータ全停止、片側LAN到達喪失、出力制御サーバ到達不能を、H側単独停止及びRS-485必須通信断から区別すること。PCS側又はGW G側は保持済み情報と適用プロファイルに従い縮退し、通信喪失を制約なし又は無制限出力へ変換しないこと。

**対象章：** [第13章](../chapters/13_Fault_Recovery_OTA.md#ch-13)　**配賦：** 障害管理・PCS／GW G側
**根拠：** SYSTEM_SPEC_PROPOSAL / CTX-R4, SP-R4　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T46, SYS-T48。レビュー補足：R4のルータ経路・機器接続別契約を資料・シミュレータ・実機で分けて確認。静的検査を実機試験と扱わない。。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-GNET-006 — ルータ混雑と変更影響

宅内ルータ・無線・WANをFW転送、上位監視、Web利用、両PCS経路で共有する影響を評価し、GW側で管理できる負荷を制限すること。家庭用ルータのQoS等を無条件保証せず、SSID・DHCP・DNS・経路・AP/STA変更で取得又は通常監視を失う条件を記録すること。

**対象章：** [第15章](../chapters/15_Deployment_Isolation.md#ch-15)　**配賦：** ネットワーク・更新・配置評価
**根拠：** SYSTEM_SPEC_PROPOSAL / CTX-R4, SP-R4　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T47, SYS-T48。レビュー補足：R4のルータ経路・機器接続別契約を資料・シミュレータ・実機で分けて確認。静的検査を実機試験と扱わない。。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-GNET-007 — 経路別の可観測性

router到達、GWの上位到達、PCSの通常EL到達、PCSのサーバ取得、スケジュール保持・適用を別の状態・時刻・品質として公開すること。取得不能なPCS情報はUNKNOWN又はNOT_EXPOSEDとし、GWのpingやEL応答だけをPCS取得成功の根拠にしないこと。

**対象章：** [第20章](../chapters/20_Northbound_Monitoring_FW.md#ch-20)　**配賦：** Query・Web UI・クラウド・アプリ
**根拠：** SYSTEM_SPEC_PROPOSAL / CTX-R4, SP-R4　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T49。レビュー補足：R4のルータ経路・機器接続別契約を資料・シミュレータ・実機で分けて確認。静的検査を実機試験と扱わない。。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-GNET-008 — 旧方式設定の再評価

R3以前のPCS_DIRECT／GW_MANAGED設定をR4へ移行する際、実機PCS・確認済み接続種別・宅内ルータ経路を照合すること。PCS_DIRECT識別子は互換のため保持しても意味と許可範囲を再評価し、不適合設定を黙って別方式へ変更又は再有効化しないこと。

**対象章：** [第18章](../chapters/18_Migration.md#ch-18)　**配賦：** 構成移行・独立保守
**根拠：** SYSTEM_SPEC_PROPOSAL / CTX-R4, SP-R4　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T45, SYS-T50。レビュー補足：R4のルータ経路・機器接続別契約を資料・シミュレータ・実機で分けて確認。静的検査を実機試験と扱わない。。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-GNET-009 — 混在構成の独立所有

同一ルータ配下にRS-485用GW G側とECHONET Lite接続PCSが存在する場合、対象scope・取得主体・資格情報・スケジュール原本を分離し、GWがEL接続PCSの代理取得・代理適用を追加しないこと。共有連系点の適合は別途評価すること。

**対象章：** [第11章](../chapters/11_Power_Constraints.md#ch-11)　**配賦：** 系統構成・PCS／GW G側
**根拠：** SYSTEM_SPEC_PROPOSAL / CTX-R4, SP-R4　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T43, SYS-T44, SYS-T46。レビュー補足：R4のルータ経路・機器接続別契約を資料・シミュレータ・実機で分けて確認。静的検査を実機試験と扱わない。。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-GNET-010 — 直接Web接続の非代替

端末–GWの直接無線Web接続は維持するが、出力制御サーバへのルータ非経由回線やEL接続PCSへの中継経路とみなさないこと。Web接続モード変更がG側のルータ接続に及ぼす影響を事前確認すること。

**対象章：** [第20章](../chapters/20_Northbound_Monitoring_FW.md#ch-20)　**配賦：** Local Web・無線管理
**根拠：** SYSTEM_SPEC_PROPOSAL / CTX-R4, SP-R4　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T47。レビュー補足：R4のルータ経路・機器接続別契約を資料・シミュレータ・実機で分けて確認。静的検査を実機試験と扱わない。。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-GNET-011 — 経路を含む変更証拠

H側更新の非干渉評価に、実ルータ経路、端点、共有NIC・設定・負荷・電源・時刻・必須PCS通信を含めること。GW非経由でも共有ルータ故障を無影響と扱わず、文書上の分離をJET判断・試験不要の保証へ読み替えないこと。

**対象章：** [第16章](../chapters/16_Certification_Change.md#ch-16)　**配賦：** リリース評価・認証主体
**根拠：** SYSTEM_SPEC_PROPOSAL / CTX-R4, SP-R4　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T47, SYS-T48。レビュー補足：R4のルータ経路・機器接続別契約を資料・シミュレータ・実機で分けて確認。静的検査を実機試験と扱わない。。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

## SYS-GNET-012 — 多重IF・仮想機器の分類

物理PCSが複数IFを持つ場合、選択済みの接続構成・物理ID・変換グループ・取得主体を一つのbindingで管理すること。GWがRS-485機器をELオブジェクトとして公開してもその実機をEL自律取得へ変更せず、異なる経路に同一scopeを重複登録しないこと。

**対象章：** [第04章](../chapters/04_Configurations_Profiles.md#ch-04)　**配賦：** 機器登録・構成管理
**根拠：** SYSTEM_SPEC_PROPOSAL / CTX-R4, SP-R4　**原典：** 追加具体化（原典ARCHの上書きなし）
**検証：** SYS-T45, SYS-T50。レビュー補足：R4のルータ経路・機器接続別契約を資料・シミュレータ・実機で分けて確認。静的検査を実機試験と扱わない。。
**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。

<!-- R6:OPEN_QUESTIONS -->
<a id="oq-list-appendices-requirements-catalog-md"></a>
## Open Questions — 本ノートを完成させるための未決事項

本ノートに関係する質問を、下表の正本章で管理する。同じ質問を別IDで重複起票せず、回答・採用値・決定記録を参照元にも反映する。履歴本文は当時の状態であり、現在の未決事項が解消した証拠にはしない。

| Open Question・正本章 | 具体的に不足する判断 | 解消時に必要な成果物 |
|---|---|---|
| [OQ-R6-19-01](../chapters/19_Open_Issues_Sources.md#oq-r6-19-01) | 正式USDMの正本・IDは何か。124件のSYSと今回の補完項目を誰が要求へ対応付け、重複・不足・対象外を承認するか。 | USDM→機能→SYS/補完項目→設計→検証の対応を版付きで完成し、未記入を適合扱いしない。 |
| [OQ-R6-04-01](../chapters/04_Configurations_Profiles.md#oq-r6-04-01) | 既存GWの全機能は何か。高度エネマネ追加後に維持・変更・廃止する機能と初回採用機能はどれか。候補ではなく採用済みとできる根拠は何か。 | 機能一覧を既存仕様・コード調査と突合し、候補機能の採否・対象リリース・非対応理由を機能表で承認する。 |
| [OQ-R6-17-01](../chapters/17_Verification.md#oq-r6-17-01) | 既存69試験と追加項目を、どの構成と数値で判定するか。試験以外の確認方法を含め、要求ごとの合否基準と評価責任者は誰か。 | 受入プロファイルを実条件で記入し、各SYS/補完項目→方法→成果物の対応を完成する。実施状態はNOT_RUNと別管理する。 |

担当者・期限・状態はリンク先を正本とする。新たな数値や認証判断を本参照表だけで確定しない。
