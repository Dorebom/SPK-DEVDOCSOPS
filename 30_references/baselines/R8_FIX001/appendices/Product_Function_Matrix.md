# 製品全機能・構成マトリクス

> **R8：** 現行章への参照先を再配賦した規範別冊候補。記入・承認未了を完成としない。全体MOCと本編の責務分担に従う。


R6追加。網羅性レビューA1に基づく記入用の規範候補であり、値・機能採否・機器適合・承認は未確定。空欄・TBDを既定値や対象外として使わない。

## 記入項目

| フィールド | 完成に必要な内容 |
|---|---|
| 機能ID・名称・分類 | 製品の正式機能ID。下表のFN-DRAFTは棚卸し行であり、SYS要求の代用ではない |
| 目的・USDM | 利用者要求・理由・上位ID・対象シナリオ |
| 変更区分 | 既存維持／追加／変更／廃止と根拠 |
| 採用区分 | 初回必須／任意／将来／対象外。全候補の初回採用とはしない |
| 製品構成 | Legacy/Next、機種、HW/H/G/PCS/クラウド/アプリ版 |
| 成立条件 | 接続機器、Capability、LAN/WAN、認証、設定、状態、必要データ |
| 動作・例外 | 入力、開始/終了、正常/異常/取消し、結果、未達時の契約 |
| 受入と承認 | 関連SYS・UC・検証・利用目的確認・条件・承認者・日付 |

## R5から抽出した棚卸し開始行

下表は**母集団を完成させるための開始行**であり、既存製品の全機能を調査し終えた一覧ではない。採用・変更・適用構成・数値はすべてTBD。追加した項目がそのまま実装必須になるわけではない。

| 仮行ID | 棚卸しする機能群 | 入力で分かる位置付け | 対応章 | 担当OQ |
|---|---|---|---|---|
| FN-DRAFT-01 | RS-485接続PCSの既存制御・状態監視 | 既存機能の維持を検討する入力前提 | 04・07・18 | [OQ-R6-04-01](../chapters/II_GW/II-02_GW_Functions.md#oq-r6-04-01) |
| FN-DRAFT-02 | ECHONET Lite ControllerによるPCSの通常操作・観測 | R5の接続・責務に記載 | 02・07 | [OQ-R6-07-02](../chapters/III_Interfaces/III-06_ECHONET_Lite.md#oq-r6-07-02) |
| FN-DRAFT-03 | 空調・給湯等のEL操作 | FLCとEL Controllerの経路を記載 | 02・08 | [OQ-R6-08-03](../chapters/II_GW/II-04_DER_Load_Control.md#oq-r6-08-03) |
| FN-DRAFT-04 | 計測器・PCS・負荷状態の取得 | Measurement/Device Stateの経路を記載 | 02・09 | [OQ-R6-09-01](../chapters/II_GW/II-07_Measurement_Data.md#oq-r6-09-01) |
| FN-DRAFT-05 | GWのECHONET Lite Device側公開 | 既存共存・仮想公開を検討 | 07・20 | [OQ-R6-07-02](../chapters/III_Interfaces/III-06_ECHONET_Lite.md#oq-r6-07-02) |
| FN-DRAFT-06 | 通常制御権・実行・結果管理 | 通常要求の共通契約を記載 | 05・06 | [OQ-R6-05-01](../chapters/II_GW/II-03_Control_Execution.md#oq-r6-05-01) |
| FN-DRAFT-07 | 自家消費・料金・購入電力・充電期限の最適化 | [旧8章の再配置先](Chapter_Migration_Map.md#old-ch-08)の候補。初回一括採用ではない | 08 | [OQ-R6-08-01](../chapters/II_GW/II-05_Advanced_EMS.md#oq-r6-08-01) |
| FN-DRAFT-08 | 計画評価・再計画・入力欠損時縮退 | 戦略枠組みを記載 | 08・13 | [OQ-R6-08-02](../chapters/II_GW/II-05_Advanced_EMS.md#oq-r6-08-02) |
| FN-DRAFT-09 | RS-485対象のGW G側出力制御 | R5の取得主体・ルータ経路条件 | 10・21 | [OQ-R6-21-01](../chapters/I_System/I-05_Configurations.md#oq-r6-21-01) |
| FN-DRAFT-10 | EL接続PCSの自律取得状態参照 | PCS自律取得は機器側責務。非公開も許容 | 09・21 | [OQ-R6-21-01](../chapters/I_System/I-05_Configurations.md#oq-r6-21-01) |
| FN-DRAFT-11 | 上位管理・監視・設定・内部操作 | R2〜R5で追加された公開契約 | 20 | [OQ-R6-20-01](../chapters/III_Interfaces/III-02_Cloud_GW.md#oq-r6-20-01) |
| FN-DRAFT-12 | 宅内Web UI・直接無線・ルータ経由 | 構成を記載。方式と画面内容は未決 | 02・20 | [OQ-R6-20-02](../chapters/IV_Quality/IV-08_Data_Log_UI_Quality.md#oq-r6-20-02) |
| FN-DRAFT-13 | クラウド経由リモートアプリ | 構成を記載。実装/通知詳細は未決 | 20 | [OQ-R6-20-02](../chapters/IV_Quality/IV-08_Data_Log_UI_Quality.md#oq-r6-20-02) |
| FN-DRAFT-14 | FW取得・検証・更新・復旧 | H/G境界を記載。実更新方式は未決 | 13・20 | [OQ-R6-20-04](../chapters/II_GW/II-11_Firmware_Update.md#oq-r6-20-04) |
| FN-DRAFT-15 | 設定競合・保存・反映・リストア | 処理原則を記載。全設定キーは未決 | 12・20 | [OQ-R6-12-02](../chapters/II_GW/II-09_Settings_Lifecycle.md#oq-r6-12-02) |
| FN-DRAFT-16 | 短期/長期保存・監査・履歴出力 | 保持・抽出の原則を記載 | 09 | [OQ-R6-09-02](../chapters/IV_Quality/IV-08_Data_Log_UI_Quality.md#oq-r6-09-02) |
| FN-DRAFT-17 | 故障・警報・診断・通知 | 故障分類はある。警報体系は補完対象 | 13・20 | [OQ-R6-20-03](../chapters/II_GW/II-10_Fault_Alarm_Diagnostics.md#oq-r6-20-03) |
| FN-DRAFT-18 | IPv4/IPv6・Wi-SUN・USB関連 | 先行持越し要求。採否・機種条件を確認 | 07・18 | [OQ-R6-07-03](../chapters/III_Interfaces/III-09_Network_Peripherals.md#oq-r6-07-03) |
| FN-DRAFT-19 | 製造初期化・施工・試運転 | ライフサイクル補完対象 | 26 | [OQ-R6-26-01](../chapters/V_Lifecycle/V-01_Manufacturing_Shipping.md#oq-r6-26-01) |
| FN-DRAFT-20 | 修理・交換・移設・廃棄・サービス終了 | ライフサイクル補完対象 | 26 | [OQ-R6-26-05](../chapters/V_Lifecycle/V-03_Maintenance_Retirement.md#oq-r6-26-05) |
| FN-DRAFT-21 | 認証・認可・秘密・更新保護・失効 | 原則を記載。具体方式は未決 | 14・27 | [OQ-R6-27-01](../chapters/IV_Quality/IV-03_Security_Privacy.md#oq-r6-27-01) |



<a id="open-questions"></a>
## Open Questions — 本ノートの完成に必要な確認


### 他章で回答する関連質問

| OQ・正本章 | 残る判断 | 完了条件 |
|---|---|---|
| [OQ-R6-04-01](../chapters/II_GW/II-02_GW_Functions.md#oq-r6-04-01) | 既存GWの全機能は何か。高度エネマネ追加後に維持・変更・廃止する機能と初回採用機能はどれか。候補ではなく採用済みとできる根拠は何か。 | 機能一覧を既存仕様・コード調査と突合し、候補機能の採否・対象リリース・非対応理由を機能表で承認する。 |
| [OQ-R6-05-01](../chapters/II_GW/II-03_Control_Execution.md#oq-r6-05-01) | 利用者、本体操作、各クラウド、既存運転、高度エネマネが競合するとき、操作別の優先順位と同順位処理をどう決めるか。途中実行の取消しをどこまで保証するか。 | 通常操作の優先表、同時実行許可表、要求失効と補償の決定表を機器能力と対応付ける。 |
| [OQ-R6-07-02](../chapters/III_Interfaces/III-06_ECHONET_Lite.md#oq-r6-07-02) | 機器ごとのEL/AIF版・実装プロパティ・更新間隔は何か。GWのDevice側は何を公開し、RS-485資源や他社PCSとの対応と不可応答をどう定義するか。 | 対応するEL機器と操作・観測表を埋め、Controller/Device共存、公開能力の上限、未対応応答を確認する。 |
| [OQ-R6-07-03](../chapters/III_Interfaces/III-09_Network_Peripherals.md#oq-r6-07-03) | IPv4/IPv6、Wi-SUN、USB通信ドングル、USBバックアップ等をどの製品で採用するか。経路優先度、抜去・ハング時動作、認証あり/なし混在をどう規定するか。 | 持越し要求を採用/対象外へ仕分け、採用品の媒体・型式・状態遷移・資源上限を接続プロファイルへ登録する。 |
| [OQ-R6-08-01](../chapters/II_GW/II-05_Advanced_EMS.md#oq-r6-08-01) | 自家消費、料金、ピーク、充電期限のどの戦略を初回採用するか。機器構成・入力欠損・手動変更に応じた開始/解除/再開条件は何か。 | 戦略ごとの採否と機能仕様を機能表・UCへ展開し、入力/結果/異常分岐の未定を除く。 |
| [OQ-R6-08-02](../chapters/II_GW/II-05_Advanced_EMS.md#oq-r6-08-02) | 採用戦略の予測データ・料金データはどこから取得し、どの品質まで使うか。最適解が得られない/期限に間に合わない場合、どの代替動作と通知にするか。 | 戦略入力辞書、計画・再計画条件、未達時動作、評価シナリオと受入指標を確定する。 |
| [OQ-R6-08-03](../chapters/II_GW/II-04_DER_Load_Control.md#oq-r6-08-03) | 空調・給湯・蓄電池等の何を操作するか。設定範囲、快適性、終了時の運転残留、本体操作尊重を機種別にどう制約するか。 | DPC/FLCの操作別機能表を機器プロファイルと安全評価へ対応付け、未対応機能を実装済みと扱わない。 |
| [OQ-R6-09-01](../chapters/II_GW/II-07_Measurement_Data.md#oq-r6-09-01) | 公開・保存・制御利用する全データ項目は何か。AC/DC、電力/電力量、符号・精度・時刻・欠測・推定の表現をどう統一するか。 | 実項目ごとの辞書に型・単位・基準点・所有者・品質・利用先を記入し、二重計上をレビューする。 |
| [OQ-R6-09-02](../chapters/IV_Quality/IV-08_Data_Log_UI_Quality.md#oq-r6-09-02) | どの項目をどの粒度/期間保存するか。電断で許す損失、積算リセット・機器交換、容量枯渇時の削除・警報はどうするか。 | 用途別保持表、容量・寿命計算、電断/満杯/時刻補正の期待結果を定義する。 |
| [OQ-R6-12-02](../chapters/II_GW/II-09_Settings_Lifecycle.md#oq-r6-12-02) | 製品が管理する全設定キーと既定値は何か。製造/施工/通常/系統保守の変更権限と、機能・機種別の有効条件は何か。 | 設定項目一覧へ実キー・型・範囲・既定値・保存先・変更条件を登録し、G側項目を一般H設定から区別する。 |
| [OQ-R6-20-01](../chapters/III_Interfaces/III-02_Cloud_GW.md#oq-r6-20-01) | 上位管理が読み書きする実項目と内部操作はどれか。プロトコル、公開schema、役割権限、完了通知・エラーをどう固定するか。 | 16件の論理IFを実契約へ展開し、公開操作台帳を実項目・権限・状態・結果へ対応付ける。 |
| [OQ-R6-20-02](../chapters/IV_Quality/IV-08_Data_Log_UI_Quality.md#oq-r6-20-02) | 宅内Web・スマートフォン・本体表示で提供する画面と項目は何か。対応端末、更新周期、色以外の区別、重要操作確認、多言語等の適用をどう決めるか。 | 画面×項目×操作×ロール表と対応端末表、利用者タスクの受入条件を確定する。ピクセル設計はUI詳細へ配賦する。 |
| [OQ-R6-20-03](../chapters/II_GW/II-10_Fault_Alarm_Diagnostics.md#oq-r6-20-03) | 通信断、出力制限、Unknown、更新失敗、保存異常等をどの警報として誰へ通知するか。確認・抑止・再通知・解除の条件と優先順位は何か。 | 警報台帳を故障ID・UI・上位イベントへ対応付け、確認済みが制約解除を意味しない条件を明記する。 |
| [OQ-R6-20-04](../chapters/II_GW/II-11_Firmware_Update.md#oq-r6-20-04) | FW配信が扱う対象はH側のみか、独立G保守を含む別配布か。画像形式・検証・適用条件・旧版復帰と各画面の成功判定をどう定めるか。 | 更新プロファイルを画像/対象/版/認可/段階/復旧条件で確定し、一般H更新からG変更を除外する。 |
| [OQ-R6-21-01](../chapters/I_System/I-05_Configurations.md#oq-r6-21-01) | EL接続PCSの自律取得能力・プロトコル・資格情報の管理仕様は何か。RS-485のGW管理と併せて、どの型式/版で実経路・公開状態を確認できるか。 | 機器接続別の取得プロファイルと管理主体、公開項目の根拠を登録する。非公開はNOT_EXPOSEDと明記する。 |
| [OQ-R6-26-01](../chapters/V_Lifecycle/V-01_Manufacturing_Shipping.md#oq-r6-26-01) | 個体IDと鍵/証明書をどの工程で投入し、再作業・不良品・重複をどう扱うか。出荷時に無効にする製造/開発機能と確認方法は何か。 | 製造プロファイルに投入主体・識別・秘密管理・再作業・閉鎖条件を記載し、手順書ID/版へ配賦する。 |
| [OQ-R6-26-05](../chapters/V_Lifecycle/V-03_Maintenance_Retirement.md#oq-r6-26-05) | GW/PCS/計測器交換、移設、所有者変更で、何のIDとデータを継承し何を失効させるか。G側構成・資格の再設定と検収は誰が行うか。 | 交換/移設/所有者変更のデータ・資格・接続移行表と再試運転条件を記録する。 |
| [OQ-R6-27-01](../chapters/IV_Quality/IV-03_Security_Privacy.md#oq-r6-27-01) | どの資産と脅威を評価対象にするか。宅内/直接無線/上位/EL/RS-485/製造/保守の入口ごとに、対策と検証と残留リスクを誰が承認するか。 | 脅威→資産/境界→対策→要求→確認方法の表を作成し、採用するJC-STAR等の項目と区別して対応付ける。 |
