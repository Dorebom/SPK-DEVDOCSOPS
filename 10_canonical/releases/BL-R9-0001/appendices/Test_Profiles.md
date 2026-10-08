# 試験プロファイルと受入条件

> **R8：** 現行章への参照先を再配賦した規範別冊候補。記入・承認未了を完成としない。全体MOCと本編の責務分担に従う。


これは未実施の試験計画。原典のT01〜T19を継承し、RS-485等の追加SYS-Tを分ける。実行データ正本：[test_catalog.json](../data/test_catalog.json)。

## すべてのRunに必要な情報

run_id、宅内ルータ構成とFW、往復経路・端点・採用機器接続種別、要求ID、試験ID、対象HW/FW、HEMS/G側版、機器プロファイル、PCS_DIRECT/GW_MANAGED、grid_control_scope_id、G側実配置、grid_control_epoch、切替Job、route_role、配線・計測点、契約・認証適用版、設定、時計基準、初期状態、注入位置・条件、要求系列、観測品質、波形／イベント、閾値・評価窓、結果、評価者を記録する。

数値・プロファイル未確定で判定できないときはINCONCLUSIVE、未実施はNOT_RUN。対象外はNOT_APPLICABLEと根拠を記録する。文書・シミュレータの確認を実機保護の合格としない。

## 原典の試験を実行条件へ展開する際の注意

負の電力値は採用符号で充電の正常値になり得る。T05では負値という形式だけで異常とせず、operation・符号・許可範囲から正常／範囲外を判定する。物理切離しは通常クライアントが任意に切離し可能な構成での試験であり、必須G側通信を切った場合は別注入として扱う。活線・保護試験は専門の安全設備・手順・担当者で行う。

<!-- GENERATED: 69 test records -->

<a id="t01"></a>
## T01 — HEMS停止・プロセスkill・再起動・物理切離し

**来歴：** SOURCE_INHERITED　**状態：** NOT_RUN

**期待結果：** G側のスケジュール実行、必要計測、保護が適用仕様内で成立する

**要求：** SYS-GRID-001, SYS-GRID-003, SYS-DEPLOY-001, SYS-RS-004

**受入プロファイル：** TBD_PER_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="t02"></a>
## T02 — 電力会社通信断、保存済みスケジュール、有効期限境界

**来歴：** SOURCE_INHERITED　**状態：** NOT_RUN

**期待結果：** 適用プロファイルの縮退・更新・失効処理に従う

**要求：** SYS-GRID-001, SYS-TIME-001, SYS-FAULT-001

**受入プロファイル：** TBD_PER_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="t03"></a>
## T03 — HEMS高負荷中に系統異常を模擬

**来歴：** SOURCE_INHERITED　**状態：** NOT_RUN

**期待結果：** 保護動作の独立性と規定の動作条件を確認。安全設備・専門環境で実施

**要求：** SYS-GRID-002, SYS-TIME-001

**受入プロファイル：** TBD_PER_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="t04"></a>
## T04 — HEMS資格情報・OTA経路からG側設定／FWへの書込みを試行

**来歴：** SOURCE_INHERITED　**状態：** NOT_RUN

**期待結果：** 認可されない。操作ログを残す

**要求：** SYS-BOUND-001, SYS-OTA-001, SYS-RS-005, SYS-CFG-002, SYS-SEC-001

**受入プロファイル：** TBD_PER_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="t05"></a>
## T05 — 過大値、負値、未対応モード、破損電文、旧版、最大頻度

**来歴：** SOURCE_INHERITED　**状態：** NOT_RUN

**期待結果：** 許可範囲外入力が拒否または定義済み動作となり、制約強制を破らない

**要求：** SYS-BOUND-001, SYS-PERF-002

**受入プロファイル：** TBD_PER_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="t06"></a>
## T06 — HEMS時計異常、計測停止、G側時計／保存異常を個別注入

**来歴：** SOURCE_INHERITED　**状態：** NOT_RUN

**期待結果：** 独立性、異常検出、適用されるG側動作を確認

**要求：** SYS-GRID-003, SYS-CONST-001, SYS-MEAS-001, SYS-FAULT-001

**受入プロファイル：** TBD_PER_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="t07"></a>
## T07 — 権威交代直前の送信待ち、Lease失効、旧応答到来

**来歴：** SOURCE_INHERITED　**状態：** NOT_RUN

**期待結果：** 旧要求が新規に送信されない。すでに送信済み分は実機状態で照合する

**要求：** SYS-AUTH-001, SYS-AUTH-002, SYS-ADAPT-001, SYS-RS-005, SYS-MIG-001

**受入プロファイル：** TBD_PER_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="t08"></a>
## T08 — 同じHybrid PCSの複数EOJへ競合要求

**来歴：** SOURCE_INHERITED　**状態：** NOT_RUN

**期待結果：** グループ資源の容量・排他を破らず、二重計上しない

**要求：** SYS-AUTH-001, SYS-TOPO-001, SYS-MEAS-002

**受入プロファイル：** TBD_PER_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="t09"></a>
## T09 — 複数機器計画の一部のみ受理・実行

**来歴：** SOURCE_INHERITED　**状態：** NOT_RUN

**期待結果：** 部分状態を保持し、二重補償をせず、現在条件で再計画する

**要求：** SYS-ORCH-001, SYS-RETRY-001

**受入プロファイル：** TBD_PER_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="t10"></a>
## T10 — 未対応プロパティ・機器版変更・Capability欠損

**来歴：** SOURCE_INHERITED　**状態：** NOT_RUN

**期待結果：** 推測で書込みを開始しない。用途に応じて限定・読取専用等へ

**要求：** SYS-CAP-001, SYS-CAP-002, SYS-EMS-001

**受入プロファイル：** TBD_PER_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="t11"></a>
## T11 — 高頻度の計画変更を入力

**来歴：** SOURCE_INHERITED　**状態：** NOT_RUN

**期待結果：** 機器／操作の最小更新間隔を守り、期限切れ要求を間引く

**要求：** SYS-CAP-001, SYS-PERF-001, SYS-PERF-002

**受入プロファイル：** TBD_PER_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="t12"></a>
## T12 — Set受理後に出力未達、応答だけ消失、計測だけ消失

**来歴：** SOURCE_INHERITED　**状態：** NOT_RUN

**期待結果：** Accepted／Verified／Unmet／Unknown等を正しく分離する

**要求：** SYS-RESULT-001, SYS-LOG-001, SYS-EL-002, SYS-RESULT-002, SYS-RESULT-003, SYS-RETRY-001, SYS-MEAS-001

**受入プロファイル：** TBD_PER_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="t13"></a>
## T13 — PV＋蓄電池＋V2H、負荷遮断、EV離脱、変換器制限

**来歴：** SOURCE_INHERITED　**状態：** NOT_RUN

**期待結果：** 連系点・機器・グループと過渡評価条件で適合判定する

**要求：** SYS-TOPO-001, SYS-CONST-002, SYS-TIME-001, SYS-LOAD-001

**受入プロファイル：** TBD_PER_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="t14"></a>
## T14 — HEMS参照用制約が古い・不明・取得不能

**来歴：** SOURCE_INHERITED　**状態：** NOT_RUN

**期待結果：** G側制約を緩和せず、HEMSが明示した縮退方針で動作する

**要求：** SYS-CONST-001, SYS-CAP-002, SYS-EMS-001

**受入プロファイル：** TBD_PER_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="t15"></a>
## T15 — CPU最大負荷、メモリ圧迫、帯域集中、温度・電源条件

**来歴：** SOURCE_INHERITED　**状態：** NOT_RUN

**期待結果：** G側の時間・通信・電力制御・保護性能が範囲内にある

**要求：** SYS-ISO-001, SYS-ISO-002, SYS-RS-006, SYS-PERF-002

**受入プロファイル：** TBD_PER_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="t16"></a>
## T16 — OTA中断、H側watchdog、ロールバック、電源断復帰

**来歴：** SOURCE_INHERITED　**状態：** NOT_RUN

**期待結果：** G側の不正変更を防止。共有故障とH側限定故障を区別する

**要求：** SYS-OTA-001, SYS-OTA-002, SYS-ISO-002, SYS-CFG-003

**受入プロファイル：** TBD_PER_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="t17"></a>
## T17 — HEMS停止時に実機が最後の通常要求を保持

**来歴：** SOURCE_INHERITED　**状態：** NOT_RUN

**期待結果：** 期限・SoC・運転残留の仕様と利用者要求の整合を確認する

**要求：** SYS-OTA-002, SYS-EXPIRY-001, SYS-ROUTE-001

**受入プロファイル：** TBD_PER_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="t18"></a>
## T18 — 本体操作・メーカークラウドとの同時操作

**来歴：** SOURCE_INHERITED　**状態：** NOT_RUN

**期待結果：** 定義した優先関係・共存条件に従い、設定の無限上書きを起こさない

**要求：** SYS-COEX-001, SYS-RESULT-002

**受入プロファイル：** TBD_PER_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="t19"></a>
## T19 — リリース前後の構成・依存・要求・結果を照合

**来歴：** SOURCE_INHERITED　**状態：** NOT_RUN

**期待結果：** 変更影響と適用試験版を追跡でき、未確定事項が隠されていない

**要求：** SYS-CERT-001, SYS-CHG-001, SYS-LOG-001, SYS-VERIFY-001

**受入プロファイル：** TBD_PER_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="sys-t01"></a>
## SYS-T01 — 既存RS-485通常制御・監視とHEMS無効／停止／再起動の回帰

**来歴：** SYSTEM_SPEC_ADDITION　**状態：** NOT_RUN

**期待結果：** 適用構成で保証する既存運転を維持し、旧・新書込みの二重化がなく、G側必須依存の有無を別に判定する

**要求：** SYS-RS-001, SYS-RS-002, SYS-RS-005, SYS-MIG-001

**受入プロファイル：** TBD_PER_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="sys-t02"></a>
## SYS-T02 — 両経路の同一意味操作、目標／上限差、符号・単位・未対応・丸め

**来歴：** SYSTEM_SPEC_ADDITION　**状態：** NOT_RUN

**期待結果：** 機器別能力を守り、未対応を成功扱いせず、要求・送信・設定・観測の段階を対応付ける

**要求：** SYS-RS-002, SYS-SEM-001, SYS-RESULT-003

**受入プロファイル：** TBD_PER_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="sys-t03"></a>
## SYS-T03 — GWのController／Device共存、外部HEMS→RS-485、自己公開・重複検出

**来歴：** SYSTEM_SPEC_ADDITION　**状態：** NOT_RUN

**期待結果：** 通常受付と調停を迂回せず、公開プロトコルの応答と達成確認を分け、制御ループを起こさない

**要求：** SYS-EL-001, SYS-EL-002

**受入プロファイル：** TBD_PER_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="sys-t04"></a>
## SYS-T04 — RS-485＋ECHONET Liteの混在、最大台数・要求集中・計測の重複

**来歴：** SYSTEM_SPEC_ADDITION　**状態：** NOT_RUN

**期待結果：** 機器ごとの待ち時間・期限・部分実行を守り、遅い経路が保証条件を壊さず、二重集計しない

**要求：** SYS-RS-006, SYS-MEAS-002, SYS-PERF-001

**受入プロファイル：** TBD_PER_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="sys-t05"></a>
## SYS-T05 — route_roleを確定したRS-485の通常リンク断／G必須通信断／共有サービス再起動

**来歴：** SYSTEM_SPEC_ADDITION　**状態：** NOT_RUN

**期待結果：** 注入点ごとに適用仕様の動作を確認する。HEMS停止で必須経路が失われたなら分離要件未達を記録する

**要求：** SYS-DEPLOY-001, SYS-RS-003, SYS-RS-004, SYS-RS-006, SYS-FAULT-001

**受入プロファイル：** TBD_PER_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="sys-t06"></a>
## SYS-T06 — 高優先度実行中の通常設定、緊急復旧、部分反映、旧設定リストア

**来歴：** SYSTEM_SPEC_ADDITION　**状態：** NOT_RUN

**期待結果：** 受付・保存・適用を区別し、許可状態と世代を守り、緊急処理や復元でG側設定を書き換えない

**要求：** SYS-CFG-001, SYS-CFG-002, SYS-CFG-003

**受入プロファイル：** TBD_PER_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="sys-t07"></a>
## SYS-T07 — 同一物理設備の二経路、装置交換、採用する場合の経路切替

**来歴：** SYSTEM_SPEC_ADDITION　**状態：** NOT_RUN

**期待結果：** 同一性と旧権威・残留要求を照合し、未確認の自動切替・二重Set・古い設定の流用をしない

**要求：** SYS-ROUTE-001

**受入プロファイル：** TBD_PER_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="sys-t08"></a>
## SYS-T08 — 欠測、時刻異常、積算リセット、機器交換、保存飽和、データ抽出

**来歴：** SYSTEM_SPEC_ADDITION　**状態：** NOT_RUN

**期待結果：** 欠測を0にせず基準・品質・履歴を保持し、保存負荷で独立系統制御を壊さない

**要求：** SYS-MEAS-001, SYS-MEAS-002, SYS-DATA-001, SYS-DATA-002

**受入プロファイル：** TBD_PER_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="sys-t09"></a>
## SYS-T09 — 認証・暗号化機器と従来機器の混在、復号後の共通処理、経路切替

**来歴：** SYSTEM_SPEC_ADDITION　**状態：** NOT_RUN

**期待結果：** 接続識別・認証状態・鮮度が保持され、許可操作が別経路やデータ値だけで昇格しない

**要求：** SYS-SEC-001

**受入プロファイル：** TBD_PER_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="sys-t10"></a>
## SYS-T10 — 全体目標・直接要求・自律HEMS、DERとFlexible Loadの混合実行

**来歴：** SYSTEM_SPEC_ADDITION　**状態：** NOT_RUN

**期待結果：** Arbiter→Orchestrator→DPC/FLCの責務を守り、機器能力で制限された部分結果と再計画を管理する

**要求：** SYS-REQ-001, SYS-LOAD-001, SYS-EMS-001

**受入プロファイル：** TBD_PER_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="sys-t11"></a>
## SYS-T11 — 外部サーバ役割と5操作種別の配送を全接続経路で照合

**来歴：** SYSTEM_SPEC_ADDITION　**状態：** NOT_RUN

**期待結果：** 上位監視・通常運転・設定・内部操作・FW更新が各所有者へ分離され、配信主体が系統制約解除や任意書込み権を得ない

**要求：** SYS-CTX-001, SYS-CTX-002, SYS-NORTH-001, SYS-FW-001

**受入プロファイル：** TBD_PER_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="sys-t12"></a>
## SYS-T12 — 直接無線で端末を接続しWAN・外部DNS・CDN・上位認証接続を遮断

**来歴：** SYSTEM_SPEC_ADDITION　**状態：** NOT_RUN

**期待結果：** 対応プロファイルと有効なローカル認可の下で基本Web監視・許可操作が成立し、未認証操作を拒否する。直接接続がWAN又はAP/STA同時性を保証しない表示になる

**要求：** SYS-UI-001, SYS-UI-003, SYS-UI-004

**受入プロファイル：** TBD_PER_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="sys-t13"></a>
## SYS-T13 — ルータ経由監視、端末隔離、別セグメント、AP/STA切替、到達先変更

**来歴：** SYSTEM_SPEC_ADDITION　**状態：** NOT_RUN

**期待結果：** 到達条件を満たす構成でWebが動作し、非到達・WAN断を区別する。直接公開ポートを必須化せず、設定反映の到達確認と復旧条件に従う

**要求：** SYS-CTX-002, SYS-CFG-006, SYS-UI-002, SYS-UI-003

**受入プロファイル：** TBD_PER_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="sys-t14"></a>
## SYS-T14 — リモートアプリの利用者・住宅・GW・ロール違い、所属失効

**来歴：** SYSTEM_SPEC_ADDITION　**状態：** NOT_RUN

**期待結果：** 別住宅・未許可機能を操作・参照できず、上位サービス認証と操作者認可を区別する。正常操作は通常経路と追跡IDを保持する

**要求：** SYS-NORTH-002, SYS-NORTH-007, SYS-APP-001, SYS-APP-003

**受入プロファイル：** TBD_PER_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="sys-t15"></a>
## SYS-T15 — ローカルと上位が同じ基準設定世代で競合し、一部反映を遅延・失敗

**来歴：** SYSTEM_SPEC_ADDITION　**状態：** NOT_RUN

**期待結果：** 設定scopeの予約・commitが整合し、競合を明示する。保存値・有効値・各反映先世代が追跡でき、全反映前にAPPLIEDとしない

**要求：** SYS-NORTH-007, SYS-CFG-004, SYS-CFG-005

**受入プロファイル：** TBD_PER_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="sys-t16"></a>
## SYS-T16 — 上位保留要求の期限切れ・重複・逆順・同一キー異内容・再認可

**来歴：** SYSTEM_SPEC_ADDITION　**状態：** NOT_RUN

**期待結果：** 期限と主体・対象・所属世代を実行時まで検査する。重複の無条件再実行や同一キーで異内容の置換を行わず、結果不明は照会で整合する

**要求：** SYS-NORTH-002, SYS-NORTH-003, SYS-NORTH-004

**受入プロファイル：** TBD_PER_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="sys-t17"></a>
## SYS-T17 — GW内部再探索・H側再起動・停止と設定/FWの競合、未許可操作

**来歴：** SYSTEM_SPEC_ADDITION　**状態：** NOT_RUN

**期待結果：** 許可されたJobだけ実行し、対象scopeを調整する。任意shell・DB・生電文・G側resetを通常経路で実行できず、復帰と完了を独立確認する

**要求：** SYS-NORTH-001, SYS-GWOP-001, SYS-GWOP-002

**受入プロファイル：** TBD_PER_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="sys-t18"></a>
## SYS-T18 — 多数のWeb/アプリ監視とFresh Read・履歴・診断・FW取得を同時最大実行

**来歴：** SYSTEM_SPEC_ADDITION　**状態：** NOT_RUN

**期待結果：** データのscope・秘密除去を維持し、有限な頻度・容量・並行度とbackpressureで制御する。G側と通常操作の確定済み時間条件を破らない

**要求：** SYS-NORTH-005, SYS-FW-005, SYS-STATE-001, SYS-ISO-003

**受入プロファイル：** TBD_PER_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="sys-t19"></a>
## SYS-T19 — FWの署名/真正性不適合、改変、別機種・領域・依存版・旧系列を入力

**来歴：** SYSTEM_SPEC_ADDITION　**状態：** NOT_RUN

**期待結果：** 保護メタデータと画像・対象を照合し、通常管理者経路でも不適合を拒否する。H側経路からG側へ書けず、許可復旧以外の任意ダウングレードを拒否する

**要求：** SYS-FW-001, SYS-FW-002, SYS-FW-003

**受入プロファイル：** TBD_PER_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="sys-t20"></a>
## SYS-T20 — FW取得・適用・起動・稼働確認の各段階で通信断・中断・電断・並行再起動

**来歴：** SYSTEM_SPEC_ADDITION　**状態：** NOT_RUN

**期待結果：** 段階とJobを復元し、認可された継続・復旧又は復旧要求を返す。取得完了と更新成功を区別し、G側の継続をH側前処理の成功に依存させない

**要求：** SYS-GWOP-002, SYS-FW-001, SYS-FW-003, SYS-FW-004

**受入プロファイル：** TBD_PER_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="sys-t21"></a>
## SYS-T21 — クラウドACKのみ、GW受理のみ、実機受理後未達、観測欠損、通知逆転

**来歴：** SYSTEM_SPEC_ADDITION　**状態：** NOT_RUN

**期待結果：** Web/アプリが受付段階・設定反映・Job・更新稼働確認と実機達成を区別する。時刻・品質・相関を保持し、現在値又は成功を偽装しない

**要求：** SYS-NORTH-004, SYS-NORTH-006, SYS-NORTH-007, SYS-APP-002, SYS-FW-004, SYS-STATE-002

**受入プロファイル：** TBD_PER_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="sys-t22"></a>
## SYS-T22 — SSID/IP/route/上位接続先変更で応答経路を断ち、共用G側依存も照合

**来歴：** SYSTEM_SPEC_ADDITION　**状態：** NOT_RUN

**期待結果：** 段階反映と新経路確認又は認可復旧に従う。共有資源の影響未評価なら制限し、正常H操作と称してG側時計・通信・resetを破らない

**要求：** SYS-CFG-006, SYS-GWOP-002, SYS-UI-003, SYS-ISO-003

**受入プロファイル：** TBD_PER_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="sys-t23"></a>
## SYS-T23 — 直接AP/LANで未認可Webアクセス、CSRF/Origin/Host悪用、診断秘密混入を試験環境で検証

**来歴：** SYSTEM_SPEC_ADDITION　**状態：** NOT_RUN

**期待結果：** 対象プロファイルの認証・接続先識別・暗号・セッション対策を維持し、越権・秘密の公開・任意内部操作を拒否する。ローカルのクラウド独立性を認証迂回にしない

**要求：** SYS-GWOP-001, SYS-UI-004, SYS-UI-005, SYS-STATE-001

**受入プロファイル：** TBD_PER_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="sys-t24"></a>
## SYS-T24 — 上位管理サービス停止・WAN断・再接続と操作期限境界

**来歴：** SYSTEM_SPEC_ADDITION　**状態：** NOT_RUN

**期待結果：** 条件内のローカル監視・自律制御を継続し、アプリは最終値/オフラインを表示する。旧操作を復活させず、FW経路やG側独立性を不必要に失わない

**要求：** SYS-NORTH-003, SYS-UI-004, SYS-APP-001, SYS-APP-002

**受入プロファイル：** TBD_PER_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="sys-t25"></a>
## SYS-T25 — FW配信サービスのみ停止、低速化、容量不足、再接続集中

**来歴：** SYSTEM_SPEC_ADDITION　**状態：** NOT_RUN

**期待結果：** FW取得を保留/制限し、稼働中の監視・通常運転を止めない。確定した帯域・CPU・保存予算とG側非干渉条件を維持する

**要求：** SYS-NORTH-005, SYS-FW-005, SYS-ISO-003

**受入プロファイル：** TBD_PER_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="sys-t26"></a>
## SYS-T26 — 所有者変更・GW再登録の後、旧アプリ/ローカル資格/保留要求で操作

**来歴：** SYSTEM_SPEC_ADDITION　**状態：** NOT_RUN

**期待結果：** 新所属世代へ一致しない要求と参照を拒否し、旧同期設定を復元しない。失効情報未到達期間は定義した寿命・操作制限に従う

**要求：** SYS-APP-003

**受入プロファイル：** TBD_PER_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="sys-t27"></a>
## SYS-T27 — GW/Web/API/クラウド/アプリ版を混在させ、クラウド要求頻度や共通OSを変更

**来歴：** SYSTEM_SPEC_ADDITION　**状態：** NOT_RUN

**期待結果：** 互換範囲を検査し未知操作を拒否又は限定する。バイナリ変更有無だけで非影響とせず、要求負荷・更新領域・共有資源の変更を記録する

**要求：** SYS-UI-005, SYS-SVC-001, SYS-CHG-002

**受入プロファイル：** TBD_PER_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="sys-t28"></a>
## SYS-T28 — イベントバッファあふれ・GW再起動・順序逆転・再同期と旧希望設定復元

**来歴：** SYSTEM_SPEC_ADDITION　**状態：** NOT_RUN

**期待結果：** 欠落と起動世代を明示して現在状態を再同期する。G側原本を変更せず、有効設定世代を古いクラウドコピーで上書きしない

**要求：** SYS-NORTH-006, SYS-CFG-005, SYS-STATE-002

**受入プロファイル：** TBD_PER_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="sys-t29"></a>
## SYS-T29 — EL接続PCSが宅内ルータ経由で自律取得・適用中にGW通常操作・H停止・GW全停止を分けて実施

**来歴：** SYSTEM_SPEC_ADDITION　**状態：** NOT_RUN

**期待結果：** PCSがGWをアプリケーション中継又は必須IP転送に使わず取得・適用し、GW通常要求で制約が解除されない。ルータ及びPCS電源が維持された試験条件を明記する

**要求：** SYS-GSEL-001, SYS-GSEL-004, SYS-GSEL-006

**受入プロファイル：** TBD_PER_MODE_AND_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="sys-t30"></a>
## SYS-T30 — RS-485接続PCSに対しGW G側が宅内ルータ経由で取得・保存・適用・指示し、H側を停止

**来歴：** SYSTEM_SPEC_ADDITION　**状態：** NOT_RUN

**期待結果：** G側の取得・時計・保存・RS-485指示・必須監視が成立し、H側を必須中継にしない。実行配置が未成立なら分離試験を合格にしない

**要求：** SYS-GSEL-001, SYS-GSEL-004, SYS-GSEL-005, SYS-GSEL-006

**受入プロファイル：** TBD_PER_MODE_AND_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="sys-t31"></a>
## SYS-T31 — R4適用表外の組合せ、未選択・未対応PCS・不一致FW・旧世代・認可不足で有効化要求

**来歴：** SYSTEM_SPEC_ADDITION　**状態：** NOT_RUN

**期待結果：** RS-485のPCS_DIRECT、EL接続PCSのGW_MANAGED、非PCS自律取得、ルータ無しを拒否する。既存適用を無断変更せず、自動PCS_DIRECTや無制限へ補完しない

**要求：** SYS-GSEL-002, SYS-GSEL-007, SYS-GSEL-019

**受入プロファイル：** TBD_PER_MODE_AND_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="sys-t32"></a>
## SYS-T32 — 同一scopeへPCS_DIRECTとGW_MANAGEDを同時有効化し、旧経路遅延指示も注入

**来歴：** SYSTEM_SPEC_ADDITION　**状態：** NOT_RUN

**期待結果：** 重複有効化を拒否又は規定の要復旧へ。旧系列を確認済みの機器手段でフェンスし、PCS保護を停止しない

**要求：** SYS-GSEL-003, SYS-GSEL-009

**受入プロファイル：** TBD_PER_MODE_AND_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="sys-t33"></a>
## SYS-T33 — R4適用表を満たす初期配備又は承認済み機器・接続構成変更を実施

**来歴：** SYSTEM_SPEC_ADDITION　**状態：** NOT_RUN

**期待結果：** 変更後の実機接続種別と方式を照合し、制約保持、旧主体フェンス、適用確認、監査を行う。同一PCSの自由な両方向切替を合格条件としない。切替非対応構成では手順を限定する

**要求：** SYS-GSEL-007, SYS-GSEL-008, SYS-GSEL-020

**受入プロファイル：** TBD_PER_MODE_AND_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="sys-t34"></a>
## SYS-T34 — 準備・旧主体停止・新主体有効化の各境界で通信断・電断・確認応答喪失

**来歴：** SYSTEM_SPEC_ADDITION　**状態：** NOT_RUN

**期待結果：** 永続Jobと実機状態を照合し、未確認の二重有効化や盲目的ロールバックをしない。プロファイルの安全状態と復旧手順を維持する

**要求：** SYS-GSEL-008, SYS-GSEL-009, SYS-GSEL-018

**受入プロファイル：** TBD_PER_MODE_AND_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="sys-t35"></a>
## SYS-T35 — PCS_DIRECT／GW_MANAGEDでH限定停止とGW全筐体停止を分けて注入

**来歴：** SYSTEM_SPEC_ADDITION　**状態：** NOT_RUN

**期待結果：** H限定障害では独立性を確認。GW_MANAGEDの全体停止ではPCSの必須通信断時動作を評価し、継続不能を誤って非干渉PASSにしない

**要求：** SYS-GSEL-005, SYS-GSEL-011

**受入プロファイル：** TBD_PER_MODE_AND_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="sys-t36"></a>
## SYS-T36 — 両方式でサーバ通信断・保持期限境界・時刻異常・監視断を注入

**来歴：** SYSTEM_SPEC_ADDITION　**状態：** NOT_RUN

**期待結果：** 選択中の方式で規定縮退・復旧を行い、無条件100%復帰・他方式自動切替を行わない

**要求：** SYS-GSEL-010, SYS-GSEL-011

**受入プロファイル：** TBD_PER_MODE_AND_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="sys-t37"></a>
## SYS-T37 — H側OTA／一般バックアップ復元／初期化に古い方式bindingやG設定を混入

**来歴：** SYSTEM_SPEC_ADDITION　**状態：** NOT_RUN

**期待結果：** H側権限では方式・G原本・資格・時刻・FWを変更できず、G更新は独立した認可に従う

**要求：** SYS-GSEL-006, SYS-GSEL-015

**受入プロファイル：** TBD_PER_MODE_AND_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="sys-t38"></a>
## SYS-T38 — Web／クラウド／アプリへ方式・適用情報を配信し、PCS非公開・古いコピー・切替途中を含める

**来歴：** SYSTEM_SPEC_ADDITION　**状態：** NOT_RUN

**期待結果：** 設定と有効方式、Job、品質を分離。NOT_EXPOSED／UNKNOWNを正しく表示し、設定受付を切替完了としない

**要求：** SYS-GSEL-006, SYS-GSEL-013, SYS-GSEL-014, SYS-GSEL-020

**受入プロファイル：** TBD_PER_MODE_AND_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="sys-t39"></a>
## SYS-T39 — GW管理のRS-485必須経路に通常Set・読出し負荷を集中し、共有ルータにFW転送負荷を加える

**来歴：** SYSTEM_SPEC_ADDITION　**状態：** NOT_RUN

**期待結果：** 最終送信所有者と資源契約が制約の上書きを防ぎ、規定の指示・監視・取得条件又は縮退条件を満たす。ルータ側の未知のQoS能力を前提にしない

**要求：** SYS-GSEL-004, SYS-GSEL-005, SYS-GSEL-012

**受入プロファイル：** TBD_PER_MODE_AND_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="sys-t40"></a>
## SYS-T40 — 二方式間変更、H/Gの各更新、共有driver／reset変更で構成・認証証拠を照合

**来歴：** SYSTEM_SPEC_ADDITION　**状態：** NOT_RUN

**期待結果：** 方式・接続・ソフト・計測・設定ごとに影響評価し、片方式の認証／試験結果やH単独判定を無条件流用しない

**要求：** SYS-GSEL-007, SYS-GSEL-015, SYS-GSEL-016, SYS-GSEL-020

**受入プロファイル：** TBD_PER_MODE_AND_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="sys-t41"></a>
## SYS-T41 — 独立scopeと共有PCS／共通連系点で二方式を混在させ容量配分・負荷離脱を試験

**来歴：** SYSTEM_SPEC_ADDITION　**状態：** NOT_RUN

**期待結果：** 重複scopeを検出し、確認済み全体制約でのみ稼働。個別上限の重複配分を合計適合としない

**要求：** SYS-GSEL-003, SYS-GSEL-017

**受入プロファイル：** TBD_PER_MODE_AND_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="sys-t42"></a>
## SYS-T42 — 切替未完了中の再起動、GW／PCS交換、旧資格・旧binding・遅延応答の復元

**来歴：** SYSTEM_SPEC_ADDITION　**状態：** NOT_RUN

**期待結果：** 実対象・現在世代・所有者を再照合し、旧制御を復活させない。結果不明は要復旧と監査に残す

**要求：** SYS-GSEL-009, SYS-GSEL-018, SYS-GSEL-019, SYS-GSEL-020

**受入プロファイル：** TBD_PER_MODE_AND_CONFIGURATION。未確定条件を実施済み・合格としない。

<a id="sys-t43"></a>
## SYS-T43 — EL接続PCSの取得要求・応答とGWからの通常EL通信を別に追跡しGWを停止

**来歴：** SYSTEM_SPEC_ADDITION　**状態：** NOT_RUN

**期待結果：** PCS→宅内ルータ→出力制御サーバと逆向き応答を確認し、GWの代理取得・IP中継に依存しない。通常EL通信とサーバ通信を別のプロトコル契約として照合する

**要求：** SYS-GNET-001, SYS-GNET-002, SYS-GNET-004, SYS-GNET-009

**受入プロファイル：** TBD_PER_ROUTER_DEVICE_BINDING。未確定条件を実施済み・合格としない。

<a id="sys-t44"></a>
## SYS-T44 — RS-485 PCSのGW取得・適用・応答経路を追跡する

**来歴：** SYSTEM_SPEC_ADDITION　**状態：** NOT_RUN

**期待結果：** GW G側→宅内ルータ→サーバ→宅内ルータ→G側→RS-485 PCSの責務・経路が一致し、PCS自身のサーバ取得経路がない。受理・適用・実測を区別する

**要求：** SYS-GNET-001, SYS-GNET-003, SYS-GNET-009

**受入プロファイル：** TBD_PER_ROUTER_DEVICE_BINDING。未確定条件を実施済み・合格としない。

<a id="sys-t45"></a>
## SYS-T45 — 機器接続種別・mode・ルータ経路・取得能力を不整合にした構成を検査する

**来歴：** SYSTEM_SPEC_ADDITION　**状態：** NOT_RUN

**期待結果：** EL検出のみ、RS-485のPCS_DIRECT、非PCS自律取得、EL接続PCSのGW_MANAGED、未知の型式・経路を有効化しない。分類は本製品の対応範囲として判定する

**要求：** SYS-GNET-002, SYS-GNET-004, SYS-GNET-008, SYS-GNET-012

**受入プロファイル：** TBD_PER_ROUTER_DEVICE_BINDING。未確定条件を実施済み・合格としない。

<a id="sys-t46"></a>
## SYS-T46 — WANのみ断、ルータ全停止、PCS側だけのLAN断を個別に注入し保持期限境界を通す

**来歴：** SYSTEM_SPEC_ADDITION　**状態：** NOT_RUN

**期待結果：** 取得主体が保持済みスケジュールで規定の継続／縮退を行い、期限切れも機器別規定へ進む。RS-485健全性とEL通常通信喪失を別表示し、無制限復帰・自動方式変更をしない

**要求：** SYS-GNET-005, SYS-GNET-009

**受入プロファイル：** TBD_PER_ROUTER_DEVICE_BINDING。未確定条件を実施済み・合格としない。

<a id="sys-t47"></a>
## SYS-T47 — FW取得・監視集中・ルータ設定変更・GW直接Webモード変更を行う

**来歴：** SYSTEM_SPEC_ADDITION　**状態：** NOT_RUN

**期待結果：** 共有通信の資源上限・再接続・縮退を確認する。直接Webをサーバ回線の代替にせず、SSID／経路変更をG側無影響と自動判定しない。外部ルータの制御不能条件を記録する

**要求：** SYS-GNET-006, SYS-GNET-010, SYS-GNET-011

**受入プロファイル：** TBD_PER_ROUTER_DEVICE_BINDING。未確定条件を実施済み・合格としない。

<a id="sys-t48"></a>
## SYS-T48 — H限定停止、GW全電断、ルータ電断、RS-485断を個別に注入する

**来歴：** SYSTEM_SPEC_ADDITION　**状態：** NOT_RUN

**期待結果：** EL自律取得のGW非依存とルータ依存、GW管理のH非依存とGW／RS-485依存を別判定する。保存・時刻・必要計測・通信断時処置を実配置で確認する

**要求：** SYS-GNET-003, SYS-GNET-005, SYS-GNET-006, SYS-GNET-011

**受入プロファイル：** TBD_PER_ROUTER_DEVICE_BINDING。未確定条件を実施済み・合格としない。

<a id="sys-t49"></a>
## SYS-T49 — GW WAN正常だがPCSサーバ取得不能、EL応答正常だがPCS情報非公開等を組み合わせる

**来歴：** SYSTEM_SPEC_ADDITION　**状態：** NOT_RUN

**期待結果：** 画面・クラウドはGW上位接続、PCS通常接続、PCSサーバ取得・適用の状態と鮮度を区別し、非公開・未観測をUNKNOWN／NOT_EXPOSEDとする

**要求：** SYS-GNET-004, SYS-GNET-007

**受入プロファイル：** TBD_PER_ROUTER_DEVICE_BINDING。未確定条件を実施済み・合格としない。

<a id="sys-t50"></a>
## SYS-T50 — R3設定復元、GW仮想ELオブジェクト、両IF PCS、同一scope二重登録を評価する

**来歴：** SYSTEM_SPEC_ADDITION　**状態：** NOT_RUN

**期待結果：** 旧設定をR4の物理PCS・接続種別・ルータ経路に照合し、仮想EL公開を独立PCS取得と誤分類しない。不適合設定を盲目的に再有効化・別方式変更せず、復旧は認可された手順に従う

**要求：** SYS-GNET-002, SYS-GNET-008, SYS-GNET-012

**受入プロファイル：** TBD_PER_ROUTER_DEVICE_BINDING。未確定条件を実施済み・合格としない。


## Open Questions — 本ビューの完成

[OQ-R6-19-01](../chapters/V_Lifecycle/V-07_Trace_Open_Questions.md#oq-r6-19-01)：正式USDM・要求対応。[OQ-R6-17-01](../chapters/V_Lifecycle/V-06_Verification_Validation.md#oq-r6-17-01)：受入条件。
