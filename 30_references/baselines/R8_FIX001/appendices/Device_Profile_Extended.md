# DER機器・接続・認証プロファイル — RS-485／ECHONET Lite拡張テンプレート

> **R8：** 現行章への参照先を再配賦した規範別冊候補。記入・承認未了を完成としない。全体MOCと本編の責務分担に従う。


未記入テンプレート。原典[Device_Profile](../sources/architecture/templates/Device_Profile.md)を置換せず、本書の接続具体化を追補する。すべてのTBD／UNKNOWNは未確認であり、対応済みの例ではない。

## 1. 構成と同一性

| 項目 | 記入欄 |
|---|---|
| Profile ID／revision／資料確認日 | TBD |
| メーカー・型式・HW・FW | TBD |
| physical_device_id／resource_id | TBD |
| conversion_group_id／connection_point_id | TBD |
| PCS_DIRECT／GW_MANAGED・G側実配置・確認状態 | TBD |
| route_id／通信方式 | TBD |
| 同一物理設備に対する他経路・確認根拠 | TBD |
| 初期対応Usecase・製品構成 | TBD |

## 2. RS-485の場合

| 項目 | 記入欄 |
|---|---|
| 通信仕様名称・版・根拠ファイル | TBD |
| ポート／バス／局番・対応装置 | TBD |
| route_role | UNKNOWN |
| 既存書込み元・読出し元の一覧 | TBD |
| 最後の共通送信境界・所有者 | TBD |
| 通常電文とG側必須電文・必要観測の区別 | TBD |
| 通信・Driver更新、再初期化、resetの影響 | TBD |
| 接続台数・バス時間予算・再試行 | TBD |
| H側限定切離しとGW全体停止のそれぞれの動作根拠 | TBD |

## 3. ECHONET Liteの場合

| 項目 | 記入欄 |
|---|---|
| ノード識別・クラス・EOJ | TBD |
| 実装Lite／APPENDIX／AIF版 | TBD |
| Controller側の対象／GWのDevice側公開 | TBD |
| プロパティマップ・対応モード・メーカー資料 | TBD |
| Transport・認証／暗号化状態 | TBD |
| 外部公開と実resource/groupの対応 | TBD |
| 本体UI・純正サービス・別HEMSとの共存 | TBD |

未使用の方式欄は、根拠付きでNOT_APPLICABLEとする。空欄や未記入を対象外と読み替えない。

## 4. 通常操作・観測の対応

| 共通操作又は量 | 対応 | 機器固有操作／取得 | 単位・符号・計測点 | 許可状態・順序 | 最小間隔 | 応答と達成確認 |
|---|---|---|---|---|---|---|
| 運転状態読取 | UNKNOWN | TBD | TBD | TBD | TBD | TBD |
| 実電力・SoC等 | UNKNOWN | TBD | TBD | TBD | TBD | TBD |
| 運転モード要求 | UNKNOWN | TBD | TBD | TBD | TBD | TBD |
| 充放電の目標電力 | UNKNOWN | TBD | TBD | TBD | TBD | TBD |
| 通常運転の電力上限 | UNKNOWN | TBD | TBD | TBD | TBD | TBD |
| PV通常出力制限 | UNKNOWN | TBD | TBD | TBD | TBD | TBD |
| Q／力率等 | UNKNOWN | TBD | TBD | TBD | TBD | TBD |
| 要求の解除・機器内期限 | UNKNOWN | TBD | TBD | TBD | TBD | TBD |
| 制限理由 | UNKNOWN | TBD | TBD | TBD | TBD | TBD |

電力目標と電力上限を同一操作にしない。変換できない操作は拒否し、確認できない結果は不明とする。機器内期限未対応ならGW内部Leaseで補えたとしない。

## 5. 系統・認証・強制経路

| 項目 | 記入欄 |
|---|---|
| 一般送配電事業者・接続／契約条件 | TBD |
| GridApplicabilityと根拠 | UNKNOWN |
| 制約quantity／scope／容量基準 | TBD |
| 出力制御ユニット・最終強制所有者 | TBD |
| 必須計測・G側時刻・永続状態 | TBD |
| 通常操作が制約・保護を迂回しない根拠 | TBD |
| 認証申請主体・登録構成・ソフト識別 | TBD |
| 適用仕様・試験版・必要な変更手続き | TBD |
| HEMS停止時に継続する機能と依存資源 | TBD |
| 複数PCS・連系点全体制約の成立根拠 | TBD |

## 6. 異常・残留・性能

| 条件 | 実機／G側動作 | HEMS動作 | 閾値・証拠・判定 |
|---|---|---|---|
| 通常操作リンク断 | TBD | TBD | TBD |
| 上位スケジュール通信断 | TBD | TBD | TBD |
| G側必須通信断 | TBD | TBD | TBD |
| 最終要求の保持／期限切れ | TBD | TBD | TBD |
| 本体操作・別クラウド | TBD | TBD | TBD |
| HEMSクラッシュ・OTA | TBD | TBD | TBD |
| 時計・計測・保存異常 | TBD | TBD | TBD |
| バス／ネットワーク最大負荷 | TBD | TBD | TBD |
| EV離脱・負荷急変・共通故障 | TBD | TBD | TBD |

## 7. 評価状態

資料確認：TBD。シミュレータ：NOT_RUN。実機・HIL：NOT_RUN。認証構成：TBD。製品対応承認：TBD。

## R4の必須追補

現在の対象はEL接続PCS=PCS_DIRECT（PCS自律取得）、RS-485接続PCS=GW_MANAGED。サーバ取得は全て宅内ルータ経由。R3以前の通信種別によらないmode選択・PCS直接という表示を有効な仕様としない。物理PCSとGW仮想EL公開、多重IFの採用bindingを区別する。

記入・確認欄：物理PCS ID／接続種別／mode／router profile／往復経路／取得主体／通常EL契約とサーバ通信契約／PCS自律取得能力根拠／共有ルータ・NIC・WAN負荷／WAN・LAN・GW・RS-485の個別故障条件／R3設定移行判定／未完了事項。

方式変更を受け付ける操作が記載されていても、適用表外の組合せを権限だけで許可しない。監視Viewから実機能力を推定せず、不明・非公開・古い情報を区別する。



<a id="open-questions"></a>
## Open Questions — 本ノートの完成に必要な確認


### 他章で回答する関連質問

| OQ・正本章 | 残る判断 | 完了条件 |
|---|---|---|
| [OQ-R6-19-02](../chapters/V_Lifecycle/V-07_Trace_Open_Questions.md#oq-r6-19-02) | 各OQの実担当者、回答期限、提案G0〜G4の採否と正式レビュー日をどう定めるか。未決のまま許される作業と停止する判断はどこか。 | OQへ担当・期限・決定者を記入し、回答→根拠確認→承認→本文/台帳/テスト反映の閉鎖手順を合意する。 |
