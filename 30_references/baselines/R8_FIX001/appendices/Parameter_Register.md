# パラメータ・受入閾値台帳

> **R8：** 現行章への参照先を再配賦した規範別冊候補。記入・承認未了を完成としない。全体MOCと本編の責務分担に従う。


全件未確定。`null`は未確定であり、0、無制限、未使用を意味しない。対象構成、根拠文書・版、確認者、決定日を追加して確定する。原典の数値例を製品閾値としてコピーしない。

| ID | パラメータ | 単位／形式 | 適用scope | 確認根拠 | 関連TBD | 値 |
|---|---|---|---|---|---|---|
| PAR-PLAN-01 | 計画演算周期・期限 | s | strategy | 対象の1秒要求と製品保証段階 | SYS-TBD-006 | TBD |
| PAR-MEAS-01 | 取得周期と機器内更新周期 | s | device/quantity | メーカー仕様と実測 | TBD-008 | TBD |
| PAR-MEAS-02 | 制御に用いる最大鮮度 | s | operation/quantity | 遅延・時計品質・用途 | SYS-TBD-006 | TBD |
| PAR-CMD-01 | 最小設定更新間隔 | s | device/operation/profile | 適用AIF又はPCS仕様とFW | TBD-008 | TBD |
| PAR-CMD-02 | 最大バースト・同時要求 | count | route/operation | 負荷・機器状態遷移 | SYS-TBD-006 | TBD |
| PAR-CMD-03 | 応答期限 | s | transaction/profile | プロトコルと最悪応答 | SYS-TBD-002 | TBD |
| PAR-CMD-04 | 再試行回数・間隔 | count/s | transaction/operation | 機器内実行・残留・応答 | SYS-TBD-002 | TBD |
| PAR-RESULT-01 | 達成確認窓・許容差 | s/W or quantity unit | operation/measurement point | 測定基準と物理応答 | TBD-008 | TBD |
| PAR-RESULT-02 | Unknownの再確認期限・保持 | s | operation/usecase | 機器確認能力と利用者契約 | SYS-TBD-008 | TBD |
| PAR-AUTH-01 | Lease・冪等情報の期間 | s | authority/request | 再起動・時計・機器保持 | TBD-007 | TBD |
| PAR-RS-01 | 接続条件・局数 | profile/count | bus | 採用PCS通信仕様・台帳 | SYS-TBD-002 | TBD |
| PAR-RS-02 | 制御・監視・必須通信のバス予算 | ratio/time | bus/route_role | 全電文種と最悪時再試行 | SYS-TBD-006 | TBD |
| PAR-EL-01 | 接続台数・探索・取得予算 | count/time | network/profile | 接続版と混在・実機確認 | SYS-TBD-006 | TBD |
| PAR-GRID-01 | スケジュール取得・適用・有効期限 | profile-specific | grid_connection_profile | 一般送配電事業者・機器仕様 | TBD-003 | TBD |
| PAR-GRID-02 | G側必須通信異常時動作・時間 | profile-specific | grid_required_route | 適用構成と正式仕様 | TBD-004 | TBD |
| PAR-GRID-03 | 系統連系保護の条件・動作時間 | profile-specific | protection_domain | 対象機器・認証構成 | TBD-004 | TBD |
| PAR-GRID-04 | 過渡応答・許容差・評価窓 | profile-specific | scope/quantity | 適用プロファイル | TBD-003 | TBD |
| PAR-GRID-05 | 制約の容量基準・対象scope | W/profile | resource/group/PCC | 契約・配線・対象設備 | TBD-003 | TBD |
| PAR-CFG-01 | 設定反映状態・保留期限 | state/s | configuration usecase | 高優先度実行と復旧契約 | SYS-TBD-009 | TBD |
| PAR-DATA-01 | 短期・長期・監査の保持期間 | duration | dataset | 製品／制度／運用要求 | SYS-TBD-010 | TBD |
| PAR-DATA-02 | 保存粒度・容量・書込み予算 | time/bytes | dataset/device | データ定義・容量・寿命 | SYS-TBD-010 | TBD |
| PAR-ISO-01 | CPU・メモリ・キュー・帯域予算 | resource-specific | H/G/shared | 配置と最大負荷評価 | TBD-011 | TBD |
| PAR-ENV-01 | 温度・電源・reset・設置条件 | profile-specific | product/configuration | HW・共有故障評価 | TBD-011 | TBD |
| PAR-SEC-01 | 認証・暗号化・資格情報・保守許可 | profile-specific | connection/security | メーカー・脅威分析・採用規格 | TBD-012 | TBD |
| PAR-UP-01 | 上位要求・イベント・再接続の頻度とburst | profile-specific | upper-connection | R2の対象構成・採用IF・製品運用と負荷/復旧評価 | SYS-TBD-020 | TBD |
| PAR-UP-02 | オフライン要求のTTLと保留上限 | s/count | operation-kind | R2の対象構成・採用IF・製品運用と負荷/復旧評価 | SYS-TBD-019 | TBD |
| PAR-UP-03 | 重複排除・結果照会の保持期間 | s | principal/target/operation | R2の対象構成・採用IF・製品運用と負荷/復旧評価 | SYS-TBD-019 | TBD |
| PAR-UP-04 | 監視取得・報告・画面更新周期と鮮度 | s | measurement/view | R2の対象構成・採用IF・製品運用と負荷/復旧評価 | SYS-TBD-020 | TBD |
| PAR-UP-05 | Web/アプリの同時セッション数・認可寿命 | count/s | access-profile | R2の対象構成・採用IF・製品運用と負荷/復旧評価 | SYS-TBD-016 | TBD |
| PAR-UP-06 | 履歴/診断のページサイズ・容量・同時Job上限 | bytes/count | query-job | R2の対象構成・採用IF・製品運用と負荷/復旧評価 | SYS-TBD-020 | TBD |
| PAR-UP-07 | イベント保存量・監査優先度・再同期窓 | bytes/s | event-stream | R2の対象構成・採用IF・製品運用と負荷/復旧評価 | SYS-TBD-019 | TBD |
| PAR-UP-08 | 直接無線の稼働条件・有効時間・接続数 | profile-specific | local-direct | R2の対象構成・採用IF・製品運用と負荷/復旧評価 | SYS-TBD-014 | TBD |
| PAR-UP-09 | ネットワーク変更の確認期限・復旧猶予 | s | network-config | R2の対象構成・採用IF・製品運用と負荷/復旧評価 | SYS-TBD-021 | TBD |
| PAR-UP-10 | FW画像/一時保存/復旧領域の必要容量 | bytes | update-target | R2の対象構成・採用IF・製品運用と負荷/復旧評価 | SYS-TBD-018 | TBD |
| PAR-UP-11 | FW転送帯域・再試行・CPU予算 | profile-specific | update-session | R2の対象構成・採用IF・製品運用と負荷/復旧評価 | SYS-TBD-020 | TBD |
| PAR-UP-12 | FW適用・起動・稼働確認・復旧期限 | s | update-phase | R2の対象構成・採用IF・製品運用と負荷/復旧評価 | SYS-TBD-018 | TBD |
| PAR-UP-13 | 高影響内部Jobの期限・並行実行・取消し条件 | profile-specific | gw-operation | R2の対象構成・採用IF・製品運用と負荷/復旧評価 | SYS-TBD-017 | TBD |
| PAR-UP-14 | オフライン認可・失効伝達・所有者変更の期限 | s | authorization-scope | R2の対象構成・採用IF・製品運用と負荷/復旧評価 | SYS-TBD-016 | TBD |
| PAR-UP-15 | TLS/鍵/接続先識別/ローカル名前解決プロファイル | profile-specific | local-and-cloud | R2の対象構成・採用IF・製品運用と負荷/復旧評価 | SYS-TBD-015 | TBD |
| PAR-UP-16 | GW/Web/API/クラウド/アプリの互換範囲 | version-profile | release | R2の対象構成・採用IF・製品運用と負荷/復旧評価 | SYS-TBD-023 | TBD |
| PAR-GSEL-01 | 方式切替準備・旧主体停止確認・適用確認の各期限 | s | grid-scope/switch-phase | 方式ごとの適用仕様・機器・実行配置・保守手順の確認 | SYS-TBD-026 | TBD |
| PAR-GSEL-02 | スケジュール保持・期限・時刻許容差 | profile-specific | mode/utility/device | 方式ごとの適用仕様・機器・実行配置・保守手順の確認 | SYS-TBD-028 | TBD |
| PAR-GSEL-03 | G側PCS指示・監視周期と通信断時動作条件 | profile-specific | mode/required-route | 方式ごとの適用仕様・機器・実行配置・保守手順の確認 | SYS-TBD-028 | TBD |
| PAR-GSEL-04 | 切替中の制約保持・必要停止・復旧条件 | profile-specific | grid-scope | 方式ごとの適用仕様・機器・実行配置・保守手順の確認 | SYS-TBD-026 | TBD |
| PAR-GSEL-05 | GW G側のCPU・通信・保存・バス負荷上限 | profile-specific | deployment | 方式ごとの適用仕様・機器・実行配置・保守手順の確認 | SYS-TBD-025 | TBD |
| PAR-GSEL-06 | 方式・適用状態の公開項目と最大観測経過時間 | profile-specific | mode/device | 方式ごとの適用仕様・機器・実行配置・保守手順の確認 | SYS-TBD-029 | TBD |
| PAR-GNET-01 | 宅内ルータ経路の必須LAN/WAN・名前解決・アドレス条件 | profile-specific | router/GW/EL_PCS | R4の実配線・機器仕様・ネットワーク条件と受入試験で決定 | SYS-TBD-031 | TBD |
| PAR-GNET-02 | 取得経路断の検出・再接続・再取得条件 | profile-specific | mode/device/network | R4の実配線・機器仕様・ネットワーク条件と受入試験で決定 | SYS-TBD-032 | TBD |
| PAR-GNET-03 | FW・監視の送信量／並行数と取得通信の共存予算 | profile-specific | shared_router/NIC/WAN | R4の実配線・機器仕様・ネットワーク条件と受入試験で決定 | SYS-TBD-032 | TBD |
| PAR-GNET-04 | PCS独立取得状態の公開項目と鮮度・不明判定 | profile-specific | EL_PCS/UI/cloud | R4の実配線・機器仕様・ネットワーク条件と受入試験で決定 | SYS-TBD-033 | TBD |

## 数値の扱い

1秒は先行ユーザー要求の対象候補であり、送信・達成・全機器共通保証ではない。添付の60秒は特定AIF・操作の説明例、5分は引用元の定義する内部通信異常の例である。いずれも適用文書・実機・経路・版を確認して該当プロファイルへ登録する。今回これらの規格を再検証していない。



<a id="open-questions"></a>
## Open Questions — 本ノートの完成に必要な確認


### 他章で回答する関連質問

| OQ・正本章 | 残る判断 | 完了条件 |
|---|---|---|
| [OQ-R6-19-02](../chapters/V_Lifecycle/V-07_Trace_Open_Questions.md#oq-r6-19-02) | 各OQの実担当者、回答期限、提案G0〜G4の採否と正式レビュー日をどう定めるか。未決のまま許される作業と停止する判断はどこか。 | OQへ担当・期限・決定者を記入し、回答→根拠確認→承認→本文/台帳/テスト反映の閉鎖手順を合意する。 |
