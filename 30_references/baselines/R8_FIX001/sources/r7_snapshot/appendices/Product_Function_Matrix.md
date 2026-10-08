# 製品全機能・構成マトリクス

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
| FN-DRAFT-01 | RS-485接続PCSの既存制御・状態監視 | 既存機能の維持を検討する入力前提 | 04・07・18 | [OQ-R6-04-01](../chapters/04_Configurations_Profiles.md#oq-r6-04-01) |
| FN-DRAFT-02 | ECHONET Lite ControllerによるPCSの通常操作・観測 | R5の接続・責務に記載 | 02・07 | [OQ-R6-07-02](../chapters/07_DER_Connections.md#oq-r6-07-02) |
| FN-DRAFT-03 | 空調・給湯等のEL操作 | FLCとEL Controllerの経路を記載 | 02・08 | [OQ-R6-08-03](../chapters/08_Advanced_EMS_Loads.md#oq-r6-08-03) |
| FN-DRAFT-04 | 計測器・PCS・負荷状態の取得 | Measurement/Device Stateの経路を記載 | 02・09 | [OQ-R6-09-01](../chapters/09_Measurement_Data.md#oq-r6-09-01) |
| FN-DRAFT-05 | GWのECHONET Lite Device側公開 | 既存共存・仮想公開を検討 | 07・20 | [OQ-R6-07-02](../chapters/07_DER_Connections.md#oq-r6-07-02) |
| FN-DRAFT-06 | 通常制御権・実行・結果管理 | 通常要求の共通契約を記載 | 05・06 | [OQ-R6-05-01](../chapters/05_Control_Contracts.md#oq-r6-05-01) |
| FN-DRAFT-07 | 自家消費・料金・購入電力・充電期限の最適化 | 第8章の候補。初回一括採用ではない | 08 | [OQ-R6-08-01](../chapters/08_Advanced_EMS_Loads.md#oq-r6-08-01) |
| FN-DRAFT-08 | 計画評価・再計画・入力欠損時縮退 | 戦略枠組みを記載 | 08・13 | [OQ-R6-08-02](../chapters/08_Advanced_EMS_Loads.md#oq-r6-08-02) |
| FN-DRAFT-09 | RS-485対象のGW G側出力制御 | R5の取得主体・ルータ経路条件 | 10・21 | [OQ-R6-21-01](../chapters/21_Grid_Connection_Selection.md#oq-r6-21-01) |
| FN-DRAFT-10 | EL接続PCSの自律取得状態参照 | PCS自律取得は機器側責務。非公開も許容 | 09・21 | [OQ-R6-21-01](../chapters/21_Grid_Connection_Selection.md#oq-r6-21-01) |
| FN-DRAFT-11 | 上位管理・監視・設定・内部操作 | R2〜R5で追加された公開契約 | 20 | [OQ-R6-20-01](../chapters/20_Northbound_Monitoring_FW.md#oq-r6-20-01) |
| FN-DRAFT-12 | 宅内Web UI・直接無線・ルータ経由 | 構成を記載。方式と画面内容は未決 | 02・20 | [OQ-R6-20-02](../chapters/20_Northbound_Monitoring_FW.md#oq-r6-20-02) |
| FN-DRAFT-13 | クラウド経由リモートアプリ | 構成を記載。実装/通知詳細は未決 | 20 | [OQ-R6-20-02](../chapters/20_Northbound_Monitoring_FW.md#oq-r6-20-02) |
| FN-DRAFT-14 | FW取得・検証・更新・復旧 | H/G境界を記載。実更新方式は未決 | 13・20 | [OQ-R6-20-04](../chapters/20_Northbound_Monitoring_FW.md#oq-r6-20-04) |
| FN-DRAFT-15 | 設定競合・保存・反映・リストア | 処理原則を記載。全設定キーは未決 | 12・20 | [OQ-R6-12-02](../chapters/12_Configuration_Lifecycle.md#oq-r6-12-02) |
| FN-DRAFT-16 | 短期/長期保存・監査・履歴出力 | 保持・抽出の原則を記載 | 09 | [OQ-R6-09-02](../chapters/09_Measurement_Data.md#oq-r6-09-02) |
| FN-DRAFT-17 | 故障・警報・診断・通知 | 故障分類はある。警報体系は補完対象 | 13・20 | [OQ-R6-20-03](../chapters/20_Northbound_Monitoring_FW.md#oq-r6-20-03) |
| FN-DRAFT-18 | IPv4/IPv6・Wi-SUN・USB関連 | 先行持越し要求。採否・機種条件を確認 | 07・18 | [OQ-R6-07-03](../chapters/07_DER_Connections.md#oq-r6-07-03) |
| FN-DRAFT-19 | 製造初期化・施工・試運転 | ライフサイクル補完対象 | 26 | [OQ-R6-26-01](../chapters/26_Manufacturing_Commissioning_Retirement.md#oq-r6-26-01) |
| FN-DRAFT-20 | 修理・交換・移設・廃棄・サービス終了 | ライフサイクル補完対象 | 26 | [OQ-R6-26-05](../chapters/26_Manufacturing_Commissioning_Retirement.md#oq-r6-26-05) |
| FN-DRAFT-21 | 認証・認可・秘密・更新保護・失効 | 原則を記載。具体方式は未決 | 14・27 | [OQ-R6-27-01](../chapters/27_Security_Privacy_Lifecycle.md#oq-r6-27-01) |

<!-- R6:OPEN_QUESTIONS -->
<a id="oq-list-appendices-product-function-matrix-md"></a>
## Open Questions — 本ノートを完成させるための未決事項

本ノートに関係する質問を、下表の正本章で管理する。同じ質問を別IDで重複起票せず、回答・採用値・決定記録を参照元にも反映する。履歴本文は当時の状態であり、現在の未決事項が解消した証拠にはしない。

| Open Question・正本章 | 具体的に不足する判断 | 解消時に必要な成果物 |
|---|---|---|
| [OQ-R6-04-01](../chapters/04_Configurations_Profiles.md#oq-r6-04-01) | 既存GWの全機能は何か。高度エネマネ追加後に維持・変更・廃止する機能と初回採用機能はどれか。候補ではなく採用済みとできる根拠は何か。 | 機能一覧を既存仕様・コード調査と突合し、候補機能の採否・対象リリース・非対応理由を機能表で承認する。 |
| [OQ-R6-04-02](../chapters/04_Configurations_Profiles.md#oq-r6-04-02) | 初回対応するPCS・空調・給湯・計測器・USB機器はどの型式/版か。全機能対応、観測のみ、非対応をどの組合せで保証するか。 | 機器プロファイルと製品構成表に実型式・版・操作・制限・確認資料を登録する。 |
| [OQ-R6-08-01](../chapters/08_Advanced_EMS_Loads.md#oq-r6-08-01) | 自家消費、料金、ピーク、充電期限のどの戦略を初回採用するか。機器構成・入力欠損・手動変更に応じた開始/解除/再開条件は何か。 | 戦略ごとの採否と機能仕様を機能表・UCへ展開し、入力/結果/異常分岐の未定を除く。 |
| [OQ-R6-18-01](../chapters/18_Migration.md#oq-r6-18-01) | As-Isのどの機能・通信・設定・挙動を維持するか。Legacyへ戻せない機能や、未確認の持越し項目をどの製品で対象外にするか。 | 既存機能母集団と完全なTo-Beの適用表を突合し、差分だけを正本にしない移行方針を確定する。 |

担当者・期限・状態はリンク先を正本とする。新たな数値や認証判断を本参照表だけで確定しない。
