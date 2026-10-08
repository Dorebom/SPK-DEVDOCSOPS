# 配置・通信所有・認証影響の対応テンプレート

本書独自の台帳方式。機器・コード・配線を調査するための未記入表であり、実配置の報告ではない。

## 1. 配置選択

| 項目 | 内容 |
|---|---|
| 製品構成ID・HW／ソフト版 | TBD |
| 出力制御接続方式 | TBD：PCS_DIRECT／GW_MANAGEDから対応構成に従い選択 |
| G側実配置・CPU／OS | TBD：方式選択とは別に確定 |
| grid_control_scope_id・設定版・有効所有者 | TBD |
| G側機能の所有者・装置 | TBD |
| 最終制約・保護・必要計測の所有者 | TBD |
| メーカー／認証申請主体 | TBD |
| 採用判断・承認者・根拠 | TBD |

## 2. 経路所有権

| route_id | 接続先・装置 | 方式・仕様版 | route_role | 送信／読出し所有者 | HEMS停止時 | 更新・reset範囲 | 依存証拠 |
|---|---|---|---|---|---|---|---|
| TBD | TBD | RS-485／その他を記入 | UNKNOWN | TBD | TBD | TBD | TBD |
| TBD | TBD | ECHONET Lite／その他を記入 | UNKNOWN | TBD | TBD | TBD | TBD |

route_roleはNORMAL_OPERATION_ONLY、GRID_CONTROL_REQUIRED、SHARED_REQUIRES_REVIEW、UNKNOWN。役割が複数の電文に跨るなら電文群・観測群を分けた明細を添付する。

## 3. 論理責務と実配置

| 論理責務 | 状態正本 | 実プロセス／装置 | 共有資源 | 現行書込み点 | To-Be所有者 | 切替条件 |
|---|---|---|---|---|---|---|
| Control Arbiter | 権威・epoch・Lease | TBD | TBD | TBD | TBD | TBD |
| Orchestrator | 採用計画と進行 | TBD | TBD | TBD | TBD | TBD |
| DPC | 個別DER実行 | TBD | TBD | TBD | TBD | TBD |
| FLC | 負荷実行 | TBD | TBD | TBD | TBD | TBD |
| Measurement | HEMS観測品質 | TBD | TBD | TBD | TBD | TBD |
| RS-485 Adapter／Transport | 通信 | TBD | TBD | TBD | TBD | TBD |
| ECHONET Lite Adapter | 通信・公開対応 | TBD | TBD | TBD | TBD | TBD |
| OCU／系統制約／保護 | 原本・必要状態 | TBD | TBD | TBD | TBD | TBD |

## 4. 選択方式の成立確認

- [ ] 通常APIが出力制御と保護を迂回しない根拠がある。
- [ ] HEMSを必須にしないスケジュール・計測・時刻・保持・機器通信がある。
- [ ] 既存RS-485の切離し・再起動で何が停止するかを特定した。
- [ ] G側必須通信と通常操作通信を別々の故障注入点として評価した。
- [ ] 負荷急変・複数PCSのscopeを機器側／サイト側で成立させられる。
- [ ] HEMS更新の対象・権限・resetと共有資源の評価がある。
- [ ] 機器・認証構成・許可操作の組合せを確認した。

未チェックは未確認。満たせない事項がある場合は、両方式いずれも適合PASSにせず、未達・実配置変更・サポート制限をレビューする。

## R2追加：上位・無線・更新の配置と依存（未記入）

| 論理要素 | 配置・実行主体 | 接続開始側 | H/G共通資源 | 書込み・reset scope | 版・根拠 | 状態 |
|---|---|---|---|---|---|---|
| 上位接続Adapter | TBD | TBD | TBD | TBD | TBD | UNCONFIRMED |
| Local Web UI Service | TBD | ブラウザ起点案 | TBD | TBD | TBD | UNCONFIRMED |
| 直接無線／STA | TBD | TBD | TBD | TBD | TBD | UNCONFIRMED |
| FW Update Manager | TBD | GW取得案 | TBD | TBD | TBD | UNCONFIRMED |
| 配信・署名・適用認可 | TBD | 機能別 | TBD | TBD | TBD | UNCONFIRMED |
| 上位設定・内部操作 | TBD | 論理要求と接続方向を分離 | TBD | TBD | TBD | UNCONFIRMED |

同一物理サーバでも操作権限の共有を前提にしない。同一無線チップでもAP／STA同時利用・無影響な切替を仮定しない。


## R3追加：切替と全体停止

PCS_DIRECTはPCS内取得・適用、GW_MANAGEDはGW G側取得・適用を配賦する。H側切離しとGW全体切離しを別試験条件にする。旧主体フェンス・新主体確認・安全状態・復旧手順・認証／登録確認は[方式プロファイル](Grid_Connection_Profile.md)に記録する。

## R4の必須追補

現在の対象はEL接続PCS=PCS_DIRECT（PCS自律取得）、RS-485接続PCS=GW_MANAGED。サーバ取得は全て宅内ルータ経由。R3以前の通信種別によらないmode選択・PCS直接という表示を有効な仕様としない。物理PCSとGW仮想EL公開、多重IFの採用bindingを区別する。

記入・確認欄：物理PCS ID／接続種別／mode／router profile／往復経路／取得主体／通常EL契約とサーバ通信契約／PCS自律取得能力根拠／共有ルータ・NIC・WAN負荷／WAN・LAN・GW・RS-485の個別故障条件／R3設定移行判定／未完了事項。

方式変更を受け付ける操作が記載されていても、適用表外の組合せを権限だけで許可しない。監視Viewから実機能力を推定せず、不明・非公開・古い情報を区別する。

<!-- R6:OPEN_QUESTIONS -->
<a id="oq-list-appendices-deployment-binding-md"></a>
## Open Questions — 本ノートを完成させるための未決事項

本ノートに関係する質問を、下表の正本章で管理する。同じ質問を別IDで重複起票せず、回答・採用値・決定記録を参照元にも反映する。履歴本文は当時の状態であり、現在の未決事項が解消した証拠にはしない。

| Open Question・正本章 | 具体的に不足する判断 | 解消時に必要な成果物 |
|---|---|---|
| [OQ-R6-15-01](../chapters/15_Deployment_Isolation.md#oq-r6-15-01) | GW_MANAGEDのG側を実際にどこへ配置するか。H側停止・更新に共倒れする資源は何か。独立通常チャネルを採用するなら非迂回を何で確認するか。 | 配備・依存・更新単位・故障注入点の台帳を実HW/OS/PCS資料で埋め、成立と未達を分類する。 |
| [OQ-R6-15-02](../chapters/15_Deployment_Isolation.md#oq-r6-15-02) | 非干渉を説明する入力・負荷・故障条件と比較Baselineは何か。共有ルータ・電源・OS変更をどの評価へ含め、誰が判断するか。 | 前提条件、各変更区分、必要な資料と試験の一覧をメーカー/評価担当と整理する。試験免除の確約にはしない。 |

担当者・期限・状態はリンク先を正本とする。新たな数値や認証判断を本参照表だけで確定しない。
