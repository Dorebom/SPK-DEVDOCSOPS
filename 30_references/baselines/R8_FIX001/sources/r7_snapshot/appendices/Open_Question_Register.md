# Open Question横断台帳・既存TBDとの対応

R6の具体化質問は**85件**。初版作成時はすべて未回答・OPEN。個別の現在状態は正本章の質問カードで確認する。既存48件のTBDや50件のパラメータを削除・解消・改番したものではなく、章の完成に必要な問いへ分解・対応付けた管理ビューである。単純に48＋85件を独立課題の合計とは数えない。

質問と項目の正本：[data/completion_items.json](../data/completion_items.json)。章末尾と本一覧は生成ビュー。回答欄・担当者・期限等を正本で更新し、`python tools/rebuild_views.py`で同期する。

## 提案する確定ゲート

| ゲート | 確定時点の案 |
|---|---|
| G0 | 製品スコープ・機能採否・要求Baselineの承認前 |
| G1 | 該当するアーキテクチャ・HW・安全境界の設計固定前 |
| G2 | 該当するIF・データ・操作等の詳細契約確定前 |
| G3 | 該当する検証仕様・受入プロファイルの確定前 |
| G4 | 該当製品のリリース・施工引渡し・サービス運用開始前 |

G0〜G4は本改訂で提案した文書完成の判断時点であり、既存プロジェクトの承認済み日程や役職ではない。担当者名・実日付・承認者は未定。OQ-R6-19-02で正式な管理方法へ対応付ける。

## 質問一覧

| OQ・正本章 | 具体的な質問 | 担当候補／確定ゲート |
|---|---|---|
| [OQ-R6-01-01](../chapters/01_Scope_Baseline.md#oq-r6-01-01)<br/>1.9.1 利用者・施工者・運用者・保守者の役割 | 初回製品で誰が利用・施工・管理・保守するか。各ロールの操作権限、本人確認、委譲と責任をどこまで分けるか。 | 製品企画・運用・セキュリティ<br/>G0（提案） |
| [OQ-R6-01-02](../chapters/01_Scope_Baseline.md#oq-r6-01-02)<br/>1.9.2 製品価値と対象外の判定 | 既存運転維持、宅内監視、リモート操作、高度エネマネについて、どの条件で何を達成すれば商品として合格とするか。非対応用途は何か。 | 製品企画・要求責任者<br/>G0（提案） |
| [OQ-R6-01-03](../chapters/01_Scope_Baseline.md#oq-r6-01-03)<br/>1.10.1 用語・略語・数値表記 | 製品で使う用語、画面名、通信名、単位表記をどの辞書に統一するか。既存製品との同義語や禁止する曖昧語は何か。 | システム設計・製品企画<br/>G1（提案） |
| [OQ-R6-01-04](../chapters/01_Scope_Baseline.md#oq-r6-01-04)<br/>1.10.2 規範別冊の版と仕様完成条件 | HW仕様、通信仕様、運用手順、USDMなど、完成時に参照する正本のID・版・承認者は何か。未決を残せる文書ゲートはどこか。 | 要求責任者・品質保証<br/>G0（提案） |
| [OQ-R6-02-01](../chapters/02_System_Context.md#oq-r6-02-01)<br/>2.8.1 実ネットワークと接続先の実体 | 対象住宅のGW H/G、EL接続PCS、通常EL機器はどのLAN・AP・有線ポートへ接続するか。ルータの必要条件と外部サービスの運用責任は何か。 | ネットワーク・製品運用・施工設計<br/>G1（提案） |
| [OQ-R6-02-02](../chapters/02_System_Context.md#oq-r6-02-02)<br/>2.8.2 宅内直接Webとルータ接続の成立条件 | 直接無線Webはどの無線方式を使うか。ルータ接続と同時利用できるか。クラウド断でも利用できる画面と認証条件は何か。 | 無線・Web・セキュリティ設計<br/>G1（提案） |
| [OQ-R6-03-01](../chapters/03_Responsibilities.md#oq-r6-03-01)<br/>3.10.1 実装配賦・状態所有者一覧 | Arbiter、Orchestrator、DPC/FLC、Measurement、設定・更新・G側を誰が実装し、どの状態の唯一の更新者となるか。既存Core以外の処理はどこへ配賦するか。 | システム・ソフト構造設計<br/>G1（提案） |
| [OQ-R6-03-02](../chapters/03_Responsibilities.md#oq-r6-03-02)<br/>3.10.2 H内・H/G境界契約の具体項目 | H内及びH/G APIの必須項目、エラー体系、旧版互換、頻度・キュー上限をどの契約に固定するか。G側が受ける通常要求の許可リストは何か。 | ソフトIF設計・G側設計<br/>G2（提案） |
| [OQ-R6-04-01](../chapters/04_Configurations_Profiles.md#oq-r6-04-01)<br/>4.10.1 既存・追加・変更・廃止機能の母集団 | 既存GWの全機能は何か。高度エネマネ追加後に維持・変更・廃止する機能と初回採用機能はどれか。候補ではなく採用済みとできる根拠は何か。 | 製品企画・既存製品担当<br/>G0（提案） |
| [OQ-R6-04-02](../chapters/04_Configurations_Profiles.md#oq-r6-04-02)<br/>4.10.2 機器・ソフトウェア・接続の対応組合せ | 初回対応するPCS・空調・給湯・計測器・USB機器はどの型式/版か。全機能対応、観測のみ、非対応をどの組合せで保証するか。 | 機器接続・製品企画<br/>G1（提案） |
| [OQ-R6-04-03](../chapters/04_Configurations_Profiles.md#oq-r6-04-03)<br/>4.11.1 探索・登録・解除・交換・同一性 | 探索した機器をいつ登録し、書込を許すか。交換・アドレス変更・多重IF・GW仮想EL公開をどう識別し、旧要求と履歴を扱うか。 | 機器接続・施工・データ設計<br/>G2（提案） |
| [OQ-R6-05-01](../chapters/05_Control_Contracts.md#oq-r6-05-01)<br/>5.11.1 優先関係・同順位・取消し・並行実行 | 利用者、本体操作、各クラウド、既存運転、高度エネマネが競合するとき、操作別の優先順位と同順位処理をどう決めるか。途中実行の取消しをどこまで保証するか。 | 制御設計・製品企画<br/>G2（提案） |
| [OQ-R6-05-02](../chapters/05_Control_Contracts.md#oq-r6-05-02)<br/>5.11.2 結果・確認窓・不明状態の終端 | 各操作の達成をどの計測点・許容差・確認時間で判定するか。応答や観測がない場合にUnknownを何時まで保持し、何を利用者へ返すか。 | 制御・測定・UI設計<br/>G3（提案） |
| [OQ-R6-06-01](../chapters/06_Usecases.md#oq-r6-06-01)<br/>6.11.1 機能とUCの双方向対応 | 採用した全機能に代表UCがあるか。既存RS-485監視、内部操作、設定、FW、各EMS戦略に未記載の正常・異常系列はないか。 | 要求・システム設計・テスト設計<br/>G2（提案） |
| [OQ-R6-06-02](../chapters/06_Usecases.md#oq-r6-06-02)<br/>6.11.2 横断条件・同時事象・利用場面 | クラウド設定と宅内操作、FW更新と系統スケジュール切替、機器離脱と再計画が同時に発生したとき、どの系列を受入対象にするか。 | システム・結合テスト設計<br/>G3（提案） |
| [OQ-R6-07-01](../chapters/07_DER_Connections.md#oq-r6-07-01)<br/>7.12.1 RS-485電文・接続条件・送信所有権 | 既存PCSの実プロトコル、電文/レジスタ、応答の意味、局数・配線条件は何か。通常操作とG側必須通信をどの送信者・予算で管理するか。 | PCSメーカー・GW通信設計<br/>G2（提案） |
| [OQ-R6-07-02](../chapters/07_DER_Connections.md#oq-r6-07-02)<br/>7.12.2 ECHONET Lite Controller/Deviceの対象能力 | 機器ごとのEL/AIF版・実装プロパティ・更新間隔は何か。GWのDevice側は何を公開し、RS-485資源や他社PCSとの対応と不可応答をどう定義するか。 | ECHONET Lite・機器接続設計<br/>G2（提案） |
| [OQ-R6-07-03](../chapters/07_DER_Connections.md#oq-r6-07-03)<br/>7.12.3 IPv4/IPv6・Wi-SUN・USB等の持越し要求 | IPv4/IPv6、Wi-SUN、USB通信ドングル、USBバックアップ等をどの製品で採用するか。経路優先度、抜去・ハング時動作、認証あり/なし混在をどう規定するか。 | 通信・組込み・製品企画<br/>G1（提案） |
| [OQ-R6-08-01](../chapters/08_Advanced_EMS_Loads.md#oq-r6-08-01)<br/>8.6.1 高度エネマネ戦略の採否・適用・解除 | 自家消費、料金、ピーク、充電期限のどの戦略を初回採用するか。機器構成・入力欠損・手動変更に応じた開始/解除/再開条件は何か。 | エネルギーマネジメント・製品企画<br/>G0（提案） |
| [OQ-R6-08-02](../chapters/08_Advanced_EMS_Loads.md#oq-r6-08-02)<br/>8.6.2 予測・計画・目標未達の扱い | 採用戦略の予測データ・料金データはどこから取得し、どの品質まで使うか。最適解が得られない/期限に間に合わない場合、どの代替動作と通知にするか。 | EMS・データ・テスト設計<br/>G2（提案） |
| [OQ-R6-08-03](../chapters/08_Advanced_EMS_Loads.md#oq-r6-08-03)<br/>8.6.3 DER/負荷の個別操作と快適性条件 | 空調・給湯・蓄電池等の何を操作するか。設定範囲、快適性、終了時の運転残留、本体操作尊重を機種別にどう制約するか。 | 機器制御・製品安全<br/>G2（提案） |
| [OQ-R6-09-01](../chapters/09_Measurement_Data.md#oq-r6-09-01)<br/>9.12.1 実項目・型・単位・品質・計測点 | 公開・保存・制御利用する全データ項目は何か。AC/DC、電力/電力量、符号・精度・時刻・欠測・推定の表現をどう統一するか。 | 計測・データ・制御設計<br/>G2（提案） |
| [OQ-R6-09-02](../chapters/09_Measurement_Data.md#oq-r6-09-02)<br/>9.13.1 保存容量・集計・電断時完全性 | どの項目をどの粒度/期間保存するか。電断で許す損失、積算リセット・機器交換、容量枯渇時の削除・警報はどうするか。 | データ・組込み・製品運用<br/>G3（提案） |
| [OQ-R6-09-03](../chapters/09_Measurement_Data.md#oq-r6-09-03)<br/>9.13.2 上位同期・履歴エクスポート・削除 | オフライン中の履歴を何件/期間保持し、上位とどう整合するか。利用者へ出せる項目・形式と、修理/所有者変更で消す範囲は何か。 | クラウド・データ・プライバシー担当<br/>G2（提案） |
| [OQ-R6-10-01](../chapters/10_Grid_Protection.md#oq-r6-10-01)<br/>10.8.1 エリア・契約・スケジュール仕様の版 | 対象エリア・連系契約・設備範囲・正式仕様の版は何か。取得・保持・適用・期限切れ・通信異常時の値と条件は何か。 | 系統連系担当・PCSメーカー<br/>G1（提案） |
| [OQ-R6-10-02](../chapters/10_Grid_Protection.md#oq-r6-10-02)<br/>10.8.2 通常API非迂回・保護・復帰の確認 | 対象PCSの通常操作で出力制約や保護を上書きできない根拠は何か。独立計測・保護復帰・必要通信を誰が担い、H停止時に何を維持するか。 | PCSメーカー・G側・安全設計<br/>G1（提案） |
| [OQ-R6-11-01](../chapters/11_Power_Constraints.md#oq-r6-11-01)<br/>11.7.1 基準点・容量・変換グループの対応 | 制約と計測の基準点はどこか。PV/蓄電池/Hybrid PCSの共有容量と契約容量をどの配線図・機器仕様へ対応付けるか。 | 電力・計測・施工設計<br/>G1（提案） |
| [OQ-R6-11-02](../chapters/11_Power_Constraints.md#oq-r6-11-02)<br/>11.7.2 混在設備・過渡・実出力の合否 | 異なる取得主体のPCSが同じ連系点にある場合、誰が全体制約を強制するか。負荷急変時に使う評価窓・許容差・応答条件と対応外組合せは何か。 | 電力制御・PCSメーカー・評価担当<br/>G3（提案） |
| [OQ-R6-12-01](../chapters/12_Configuration_Lifecycle.md#oq-r6-12-01)<br/>12.8.1 起動完了・未登録・縮退・停止 | 工場初期、未登録、時刻無効、PCS不在、H/G片側未起動で、各機能をいつ開始してよいか。起動完了条件と待ち期限・失敗後の動作は何か。 | システム・起動/復旧設計<br/>G2（提案） |
| [OQ-R6-12-02](../chapters/12_Configuration_Lifecycle.md#oq-r6-12-02)<br/>12.9.1 設定キー・型・範囲・既定値・権限 | 製品が管理する全設定キーと既定値は何か。製造/施工/通常/系統保守の変更権限と、機能・機種別の有効条件は何か。 | 設定・製品企画・セキュリティ<br/>G2（提案） |
| [OQ-R6-12-03](../chapters/12_Configuration_Lifecycle.md#oq-r6-12-03)<br/>12.9.2 同時変更・部分反映・緊急変更 | 同時変更や高優先度運転中の設定を、何秒/どの状態まで保留するか。緊急復旧で割り込める操作と部分反映の回復手順は何か。 | 設定・制御・運用設計<br/>G2（提案） |
| [OQ-R6-12-04](../chapters/12_Configuration_Lifecycle.md#oq-r6-12-04)<br/>12.9.3 バックアップ・工場初期化・移行 | 一般設定バックアップと初期化で何を保存・削除するか。G側FW/時計/設定/資格情報をどう除外し、異機種・旧版への復元をどう判定するか。 | 設定・更新・保守設計<br/>G2（提案） |
| [OQ-R6-13-01](../chapters/13_Fault_Recovery_OTA.md#oq-r6-13-01)<br/>13.9.1 検出閾値・重大度・復帰・再発 | 全故障の検出条件・復帰条件・再試行の上限は何か。同じ故障の頻発、正常応答の一時回復、遅延応答をどう扱うか。 | 信頼性・組込み・運用設計<br/>G3（提案） |
| [OQ-R6-13-02](../chapters/13_Fault_Recovery_OTA.md#oq-r6-13-02)<br/>13.9.2 更新中断・起動不能・実機残留要求 | FW適用中断や起動不能から何を条件に復旧するか。H/G更新範囲、復帰先版、残る機器指令と保存データの処置は何か。 | 更新・G側・保守設計<br/>G3（提案） |
| [OQ-R6-14-01](../chapters/14_Performance_Security.md#oq-r6-14-01)<br/>14.11.1 機能別の時間・精度・容量プロファイル | 1秒要求の対象と保証段階、接続台数、最悪負荷、遅延・精度・許容差は何か。どの測定点・統計条件で合否を判定するか。 | 性能・制御・品質保証<br/>G3（提案） |
| [OQ-R6-14-02](../chapters/14_Performance_Security.md#oq-r6-14-02)<br/>14.11.2 同時最大負荷・上限・飽和動作 | 監視、FW取得、再接続、履歴抽出、通常EL操作を同時実行する最大条件は何か。予算超過時に何を制限し、どのG側期限を守るか。 | 性能・ネットワーク・G側設計<br/>G3（提案） |
| [OQ-R6-15-01](../chapters/15_Deployment_Isolation.md#oq-r6-15-01)<br/>15.9.1 G側実装と共有資源の依存表 | GW_MANAGEDのG側を実際にどこへ配置するか。H側停止・更新に共倒れする資源は何か。独立通常チャネルを採用するなら非迂回を何で確認するか。 | HW・OS・G側・既存製品担当<br/>G1（提案） |
| [OQ-R6-15-02](../chapters/15_Deployment_Isolation.md#oq-r6-15-02)<br/>15.9.2 非干渉評価の範囲と根拠文書 | 非干渉を説明する入力・負荷・故障条件と比較Baselineは何か。共有ルータ・電源・OS変更をどの評価へ含め、誰が判断するか。 | 品質・認証担当・G側設計<br/>G3（提案） |
| [OQ-R6-16-01](../chapters/16_Certification_Change.md#oq-r6-16-01)<br/>16.10.1 文書版・条項・要求・証拠の対応 | 対象製品の規格・制度・地域・適用版・条項は何か。採用、対象外、未確認を誰がどの資料で判断し、SYS要求と証拠をどう対応付けるか。 | 品質・認証・製品企画<br/>G1（提案） |
| [OQ-R6-16-02](../chapters/16_Certification_Change.md#oq-r6-16-02)<br/>16.10.2 変更手続きと社内リリース判定 | H/G、機器FW、ルータ条件、外部API変更をどの基準で分類するか。メーカー・JET等への相談要否と製品リリースの承認者・必要証拠は何か。 | 品質保証・認証申請主体・リリース担当<br/>G4（提案） |
| [OQ-R6-17-01](../chapters/17_Verification.md#oq-r6-17-01)<br/>17.10.1 全要求の検証方法と受入プロファイル | 既存69試験と追加項目を、どの構成と数値で判定するか。試験以外の確認方法を含め、要求ごとの合否基準と評価責任者は誰か。 | 品質保証・試験設計・要求責任者<br/>G3（提案） |
| [OQ-R6-17-02](../chapters/17_Verification.md#oq-r6-17-02)<br/>17.10.2 利用者目的に対するValidation | 自家消費、充電期限、快適性、監視・操作について、どの住宅条件とシナリオで利用目的の達成を確認するか。未達や制限の説明が適切なことをどう判定するか。 | 製品企画・利用者代表・QA<br/>G3（提案） |
| [OQ-R6-17-03](../chapters/17_Verification.md#oq-r6-17-03)<br/>17.10.3 補完項目の評価配賦と適用除外 | 新設章の各項を試験、解析、文書検査のどれで確認するか。社外評価・施工確認・寿命根拠の担当と対象外承認をどう定めるか。 | QA・製品安全・製造/施工担当<br/>G3（提案） |
| [OQ-R6-18-01](../chapters/18_Migration.md#oq-r6-18-01)<br/>18.10.1 As-Is確認と新旧製品への機能配賦 | As-Isのどの機能・通信・設定・挙動を維持するか。Legacyへ戻せない機能や、未確認の持越し項目をどの製品で対象外にするか。 | 既存製品・移行設計・製品企画<br/>G1（提案） |
| [OQ-R6-18-02](../chapters/18_Migration.md#oq-r6-18-02)<br/>18.10.2 版互換・設定移行・旧経路停止 | どの新旧版の組合せとデータ移行をサポートするか。旧Pollerと新経路の書込権移譲、旧R3 mode設定、切戻し時の適合をどう確認するか。 | 移行・更新・クラウド/機器IF設計<br/>G2（提案） |
| [OQ-R6-19-01](../chapters/19_Open_Issues_Sources.md#oq-r6-19-01)<br/>19.10.1 上位USDMと双方向トレーサビリティ | 正式USDMの正本・IDは何か。124件のSYSと今回の補完項目を誰が要求へ対応付け、重複・不足・対象外を承認するか。 | 要求責任者・製品承認者<br/>G0（提案） |
| [OQ-R6-19-02](../chapters/19_Open_Issues_Sources.md#oq-r6-19-02)<br/>19.10.2 OQの責任者・期限・決定ゲート | 各OQの実担当者、回答期限、提案G0〜G4の採否と正式レビュー日をどう定めるか。未決のまま許される作業と停止する判断はどこか。 | PM・要求責任者・各領域担当<br/>G0（提案） |
| [OQ-R6-19-03](../chapters/19_Open_Issues_Sources.md#oq-r6-19-03)<br/>19.10.3 現行仕様と履歴の意味的整合 | 第4.5節の明示補正以外に、履歴由来の構成・用語・保証が現行方針と競合していないか。誰が意味的整合レビューを完了判定するか。 | システム設計・レビュー担当<br/>G1（提案） |
| [OQ-R6-20-01](../chapters/20_Northbound_Monitoring_FW.md#oq-r6-20-01)<br/>20.22.1 上位プロトコルとGW内部機能の公開一覧 | 上位管理が読み書きする実項目と内部操作はどれか。プロトコル、公開schema、役割権限、完了通知・エラーをどう固定するか。 | クラウド/GW IF・セキュリティ設計<br/>G2（提案） |
| [OQ-R6-20-02](../chapters/20_Northbound_Monitoring_FW.md#oq-r6-20-02)<br/>20.23.1 画面・表示項目・対応端末・操作確認 | 宅内Web・スマートフォン・本体表示で提供する画面と項目は何か。対応端末、更新周期、色以外の区別、重要操作確認、多言語等の適用をどう決めるか。 | UI/UX・製品企画・QA<br/>G2（提案） |
| [OQ-R6-20-03](../chapters/20_Northbound_Monitoring_FW.md#oq-r6-20-03)<br/>20.23.2 警報・通知・確認・抑止・解除 | 通信断、出力制限、Unknown、更新失敗、保存異常等をどの警報として誰へ通知するか。確認・抑止・再通知・解除の条件と優先順位は何か。 | 運用・UI・故障設計<br/>G2（提案） |
| [OQ-R6-20-04](../chapters/20_Northbound_Monitoring_FW.md#oq-r6-20-04)<br/>20.22.2 FW対象・配信・適用・互換・復旧 | FW配信が扱う対象はH側のみか、独立G保守を含む別配布か。画像形式・検証・適用条件・旧版復帰と各画面の成功判定をどう定めるか。 | FW更新・セキュリティ・運用設計<br/>G2（提案） |
| [OQ-R6-20-05](../chapters/20_Northbound_Monitoring_FW.md#oq-r6-20-05)<br/>20.22.3 オフライン・通知・認可失効の契約 | 上位断中にどの要求を保留し、何時まで同一要求と判断するか。オフライン認可の寿命と、アプリが表示できる過去状態の条件は何か。 | クラウド・アプリ・セキュリティ<br/>G2（提案） |
| [OQ-R6-21-01](../chapters/21_Grid_Connection_Selection.md#oq-r6-21-01)<br/>21.13.1 機種別取得主体・公開状態・実経路 | EL接続PCSの自律取得能力・プロトコル・資格情報の管理仕様は何か。RS-485のGW管理と併せて、どの型式/版で実経路・公開状態を確認できるか。 | PCSメーカー・G側・ネットワーク設計<br/>G1（提案） |
| [OQ-R6-21-02](../chapters/21_Grid_Connection_Selection.md#oq-r6-21-02)<br/>21.13.2 施工・保守の構成変更と故障時復旧 | 構成変更をどの施工・保守手順で認可し、新旧主体の停止/適用を何で確認するか。中断時の保持状態・時間条件・ロールバック条件は何か。 | 施工・G側・認証/保守担当<br/>G3（提案） |
| [OQ-R6-22-01](../chapters/22_Physical_Electrical_Installation.md#oq-r6-22-01)<br/>22.1.1 電源入力・定格・許容変動 | GWの電源方式、定格・許容変動・最大電流/消費電力は何か。外付け電源、接地、接続保護をどのHW仕様に委ねるか。 | HW・電源・製品安全担当<br/>G1（提案） |
| [OQ-R6-22-02](../chapters/22_Physical_Electrical_Installation.md#oq-r6-22-02)<br/>22.1.2 投入・瞬断・電圧低下・復電・停止 | 瞬断・電圧低下・復電時にH側/G側/PCS指令/保存データをどう扱うか。独立電源や保持機能は存在するか、どこまで保証するか。 | HW・起動復旧・G側設計<br/>G1（提案） |
| [OQ-R6-22-03](../chapters/22_Physical_Electrical_Installation.md#oq-r6-22-03)<br/>22.2.1 端子・コネクタ・ケーブル・USB | RS-485、LAN、USB等の実コネクタと電気・配線条件は何か。USB給電・接続可能機器、RS-485終端・接地等はどの規範資料に従うか。 | HW・通信・機構設計<br/>G1（提案） |
| [OQ-R6-22-04](../chapters/22_Physical_Electrical_Installation.md#oq-r6-22-04)<br/>22.3.1 外形・取付・放熱・保守空間 | 外形、質量、取付方法・姿勢、放熱/保守空間、アンテナ・設置場所の制約は何か。既存筐体仕様のどこを参照するか。 | 機構・HW・施工設計<br/>G1（提案） |
| [OQ-R6-22-05](../chapters/22_Physical_Electrical_Installation.md#oq-r6-22-05)<br/>22.3.2 表示器・LED・ボタン・ラベル | GWにあるLED、ボタン、表示器、ラベルは何か。状態表示とボタン操作は何を意味し、工場初期化やG側再起動へどう影響するか。 | 機構・UI・製品安全・製造<br/>G2（提案） |
| [OQ-R6-23-01](../chapters/23_Environment_EMC_Transport.md#oq-r6-23-01)<br/>23.1.1 温湿度・結露・標高・汚損等の適用 | 動作・保管の温湿度や結露条件は何か。標高・汚損等を適用対象にするか。H/G最大負荷と同居条件で何を保証するか。 | HW・環境試験・製品企画<br/>G1（提案） |
| [OQ-R6-23-02](../chapters/23_Environment_EMC_Transport.md#oq-r6-23-02)<br/>23.1.2 屋外・防塵防水・日射・腐食・放熱 | 屋外設置を正式採用するか。防塵防水、日射、雨水、腐食等の必要条件と、配線・筐体開閉時の制限は何か。 | 機構・製品企画・安全/環境担当<br/>G1（提案） |
| [OQ-R6-23-03](../chapters/23_Environment_EMC_Transport.md#oq-r6-23-03)<br/>23.2.1 EMC・ESD・サージ等の評価対象 | 各ポート・設置条件でEMC、静電気、サージ等のどの試験が必要か。通信停止・reset・制御への影響にどの性能判定基準を用いるか。 | EMC評価・HW・認証担当<br/>G3（提案） |
| [OQ-R6-23-04](../chapters/23_Environment_EMC_Transport.md#oq-r6-23-04)<br/>23.3.1 振動・衝撃・保管・輸送後受入 | 輸送・保管で想定する荷姿・期間・振動/衝撃/環境条件は何か。輸送後に何が維持されれば合格とするか。 | 機構・物流・製造品質<br/>G3（提案） |
| [OQ-R6-24-01](../chapters/24_Product_Remote_Safety.md#oq-r6-24-01)<br/>24.1.1 GW・PCS・負荷・利用者の危険源一覧 | GW自身と接続PCS/空調/給湯を含め、想定危険源・予見される誤使用は何か。安全責任と適用する評価方法・規格は誰が決定するか。 | 製品安全・HW・機器メーカー<br/>G1（提案） |
| [OQ-R6-24-02](../chapters/24_Product_Remote_Safety.md#oq-r6-24-02)<br/>24.2.1 故障・誤操作・通信断時の安全状態 | 各機器・操作で危険を避ける状態は何か。全停止が不適切な場合を含め、通信断・H停止・再起動後にどの制限と復帰条件を使うか。 | 製品安全・制御・PCS/負荷メーカー<br/>G2（提案） |
| [OQ-R6-24-03](../chapters/24_Product_Remote_Safety.md#oq-r6-24-03)<br/>24.2.2 遠隔操作・登録・変更の誤り防止 | 誤った住宅/機器への遠隔操作、計測点誤対応、設定復元後の意図しない再開を何で防ぐか。ローカル確認が必要な操作はどれか。 | 製品安全・UX・施工・設定設計<br/>G2（提案） |
| [OQ-R6-24-04](../chapters/24_Product_Remote_Safety.md#oq-r6-24-04)<br/>24.3.1 安全検証・注意表示・残留リスク承認 | どの安全根拠をメーカー資料と社内試験で示すか。残留リスクは誰が承認し、利用者・施工者に何を通知するか。 | 製品安全責任者・QA・製品企画<br/>G4（提案） |
| [OQ-R6-25-01](../chapters/25_Reliability_Availability_Maintainability.md#oq-r6-25-01)<br/>25.1.1 可用性・許容停止・復旧・データ損失 | H側更新、クラウド断、WAN断、G側故障別に、機能停止と復旧・データ損失をどの範囲まで許容するか。計画停止や外部要因をどう区分するか。 | 製品企画・信頼性・運用<br/>G3（提案） |
| [OQ-R6-25-02](../chapters/25_Reliability_Availability_Maintainability.md#oq-r6-25-02)<br/>25.1.2 連続稼働・劣化・資源枯渇 | 連続稼働と故障/劣化の品質を何の指標で評価するか。最大負荷・再接続を含む期間、資源増加の合否、計画再起動の許否は何か。 | 信頼性・組込みQA<br/>G3（提案） |
| [OQ-R6-25-03](../chapters/25_Reliability_Availability_Maintainability.md#oq-r6-25-03)<br/>25.2.1 故障切分けと許可保守 | 現地/リモートでどの故障を切り分け、何を交換可能にするか。保守担当が得られる情報・権限、復旧目標、保守後の確認範囲は何か。 | 保守運用・品質・セキュリティ<br/>G3（提案） |
| [OQ-R6-25-04](../chapters/25_Reliability_Availability_Maintainability.md#oq-r6-25-04)<br/>25.3.1 使用寿命・書込み寿命・消耗部品 | 目標使用期間と負荷は何か。採用ストレージ等の耐久根拠、計測/ログ/更新の書込予算、交換が必要な部品と期限は何か。 | HW・保存設計・製品企画<br/>G3（提案） |
| [OQ-R6-26-01](../chapters/26_Manufacturing_Commissioning_Retirement.md#oq-r6-26-01)<br/>26.1.1 個体識別・鍵投入・製造モード | 個体IDと鍵/証明書をどの工程で投入し、再作業・不良品・重複をどう扱うか。出荷時に無効にする製造/開発機能と確認方法は何か。 | 製造技術・セキュリティ・品質<br/>G2（提案） |
| [OQ-R6-26-02](../chapters/26_Manufacturing_Commissioning_Retirement.md#oq-r6-26-02)<br/>26.1.2 出荷状態・検査・校正・梱包 | 出荷時の設定、運転可否、搭載FW・鍵、試験モード閉鎖を何で検査するか。GWが校正責任を持つ量はあるか。ラベル・付属品は何か。 | 製造品質・HW・起動設計<br/>G3（提案） |
| [OQ-R6-26-03](../chapters/26_Manufacturing_Commissioning_Retirement.md#oq-r6-26-03)<br/>26.2.1 ネットワーク・機器・計測点の初期設定 | 施工者はどの順序で住宅・GW・機器・計測点を登録するか。EL自律取得/RS-485 GW管理とルータ経路をどう確認し、未完了時に何を禁止するか。 | 施工・ネットワーク・機器担当<br/>G2（提案） |
| [OQ-R6-26-04](../chapters/26_Manufacturing_Commissioning_Retirement.md#oq-r6-26-04)<br/>26.2.2 試運転・利用者引渡し・教育 | 現地試運転では何を確認し、どの記録で利用開始を許すか。非公開のPCS状態や通信断時制限を利用者へどう説明し、引渡しを確認するか。 | 施工・製品企画・QA<br/>G4（提案） |
| [OQ-R6-26-05](../chapters/26_Manufacturing_Commissioning_Retirement.md#oq-r6-26-05)<br/>26.3.1 本体/機器交換と所有者変更 | GW/PCS/計測器交換、移設、所有者変更で、何のIDとデータを継承し何を失効させるか。G側構成・資格の再設定と検収は誰が行うか。 | 保守・データ・セキュリティ・認証担当<br/>G3（提案） |
| [OQ-R6-26-06](../chapters/26_Manufacturing_Commissioning_Retirement.md#oq-r6-26-06)<br/>26.4.1 秘密・履歴の消去と廃止状態 | 廃棄・返却でどの秘密・履歴・所属情報を消すか。起動不能やオフラインで消去/失効ができない場合の隔離・確認・責任は何か。 | 保守運用・セキュリティ・プライバシー担当<br/>G4（提案） |
| [OQ-R6-26-07](../chapters/26_Manufacturing_Commissioning_Retirement.md#oq-r6-26-07)<br/>26.4.2 支援期間・クラウド終了後の機能 | 製品支援とクラウド/FW配信をいつまで継続するか。終了後に残すローカル機能と出力制御の条件、利用者周知・移行手段は何か。 | 製品企画・サービス運用・セキュリティ<br/>G4（提案） |
| [OQ-R6-27-01](../chapters/27_Security_Privacy_Lifecycle.md#oq-r6-27-01)<br/>27.1.1 脅威分析と要求・検証の対応 | どの資産と脅威を評価対象にするか。宅内/直接無線/上位/EL/RS-485/製造/保守の入口ごとに、対策と検証と残留リスクを誰が承認するか。 | セキュリティ・システム・品質<br/>G1（提案） |
| [OQ-R6-27-02](../chapters/27_Security_Privacy_Lifecycle.md#oq-r6-27-02)<br/>27.2.1 生成・配布・更新・失効・漏えい復旧 | 各資格情報の生成者・保存先・寿命・更新・失効・漏えい復旧をどう定めるか。時刻無効・上位断中の検証とG側資格の独立管理はどうするか。 | セキュリティ・製造・運用<br/>G2（提案） |
| [OQ-R6-27-03](../chapters/27_Security_Privacy_Lifecycle.md#oq-r6-27-03)<br/>27.2.2 通信保護・Webセッション・機器混在 | 各IFの暗号・認証・接続先識別・セッション方式を何にするか。従来EL機器と認証対応機器の許可操作、復号後の文脈保持をどう規定するか。 | セキュリティ・Web・機器IF設計<br/>G2（提案） |
| [OQ-R6-27-04](../chapters/27_Security_Privacy_Lifecycle.md#oq-r6-27-04)<br/>27.3.1 保守経路・製造アクセス・更新認証 | 量産機で残す保守・開発経路は何か。どの条件で一時有効化し、操作範囲・監査・自動無効化をどう制約するか。FW署名検証の失敗時は何を許すか。 | セキュリティ・製造・保守設計<br/>G2（提案） |
| [OQ-R6-27-05](../chapters/27_Security_Privacy_Lifecycle.md#oq-r6-27-05)<br/>27.3.2 SBOM・脆弱性対応と機器の支援機能 | SBOMや脆弱性対応でGWが提供する識別・診断・更新状態は何か。組織の受付・対応期限・承認と、機器の機能をどの文書へ分担するか。 | セキュリティ運用・リリース・製品企画<br/>G4（提案） |
| [OQ-R6-27-06](../chapters/27_Security_Privacy_Lifecycle.md#oq-r6-27-06)<br/>27.4.1 個人/住宅データの収集・利用・公開・消去 | 収集する住宅・利用者データの目的・公開先・保持期間は何か。所有者変更、端末紛失、修理、廃棄での消去・失効と必要な通知をどう規定するか。 | プライバシー・製品運用・セキュリティ<br/>G2（提案） |

## 既存TBD 48件との対応

| 既存ID | 既存の未決内容 | 具体化するR6 OQ |
|---|---|---|
| TBD-001 | 初期接続するPV・蓄電池・V2H・燃料電池の型式とFW | [OQ-R6-04-02](../chapters/04_Configurations_Profiles.md#oq-r6-04-02) / [OQ-R6-08-01](../chapters/08_Advanced_EMS_Loads.md#oq-r6-08-01) / [OQ-R6-08-03](../chapters/08_Advanced_EMS_Loads.md#oq-r6-08-03) |
| TBD-002 | 各機器の通常操作が出力制御を迂回しないか | [OQ-R6-03-02](../chapters/03_Responsibilities.md#oq-r6-03-02) / [OQ-R6-10-02](../chapters/10_Grid_Protection.md#oq-r6-10-02) / [OQ-R6-24-02](../chapters/24_Product_Remote_Safety.md#oq-r6-24-02) |
| TBD-003 | 電力会社の適用方式・容量基準・対象設備範囲 | [OQ-R6-10-01](../chapters/10_Grid_Protection.md#oq-r6-10-01) / [OQ-R6-11-01](../chapters/11_Power_Constraints.md#oq-r6-11-01) |
| TBD-004 | JET登録構成・変更申請主体・適用版 | [OQ-R6-10-01](../chapters/10_Grid_Protection.md#oq-r6-10-01) / [OQ-R6-16-01](../chapters/16_Certification_Change.md#oq-r6-16-01) |
| TBD-005 | G側をPCS外部へ新設する必要性 | [OQ-R6-11-02](../chapters/11_Power_Constraints.md#oq-r6-11-02) |
| TBD-006 | 系統制御用CT・計測範囲・故障時動作 | [OQ-R6-09-01](../chapters/09_Measurement_Data.md#oq-r6-09-01) / [OQ-R6-10-02](../chapters/10_Grid_Protection.md#oq-r6-10-02) / [OQ-R6-11-01](../chapters/11_Power_Constraints.md#oq-r6-11-01) |
| TBD-007 | HEMS停止時の通常要求保持・失効 | [OQ-R6-05-01](../chapters/05_Control_Contracts.md#oq-r6-05-01) / [OQ-R6-08-03](../chapters/08_Advanced_EMS_Loads.md#oq-r6-08-03) / [OQ-R6-13-02](../chapters/13_Fault_Recovery_OTA.md#oq-r6-13-02) / [OQ-R6-24-02](../chapters/24_Product_Remote_Safety.md#oq-r6-24-02) |
| TBD-008 | 各操作の最小更新間隔・実応答 | [OQ-R6-05-02](../chapters/05_Control_Contracts.md#oq-r6-05-02) / [OQ-R6-07-02](../chapters/07_DER_Connections.md#oq-r6-07-02) |
| TBD-009 | 複数クラウド・本体UI・純正アプリの競合 | [OQ-R6-05-01](../chapters/05_Control_Contracts.md#oq-r6-05-01) / [OQ-R6-08-03](../chapters/08_Advanced_EMS_Loads.md#oq-r6-08-03) |
| TBD-010 | As-Isの実際の権威・ワークフロー所有者・迂回経路 | [OQ-R6-03-01](../chapters/03_Responsibilities.md#oq-r6-03-01) / [OQ-R6-04-01](../chapters/04_Configurations_Profiles.md#oq-r6-04-01) / [OQ-R6-18-01](../chapters/18_Migration.md#oq-r6-18-01) |
| TBD-011 | HEMSとG側で共有するCPU・NIC・電源・reset等 | [OQ-R6-03-02](../chapters/03_Responsibilities.md#oq-r6-03-02) / [OQ-R6-14-02](../chapters/14_Performance_Security.md#oq-r6-14-02) / [OQ-R6-15-01](../chapters/15_Deployment_Isolation.md#oq-r6-15-01) / [OQ-R6-22-02](../chapters/22_Physical_Electrical_Installation.md#oq-r6-22-02) / [OQ-R6-23-01](../chapters/23_Environment_EMC_Transport.md#oq-r6-23-01) / [OQ-R6-23-03](../chapters/23_Environment_EMC_Transport.md#oq-r6-23-03) |
| TBD-012 | 認証・暗号化対応機器と従来機器の混在方式 | [OQ-R6-07-03](../chapters/07_DER_Connections.md#oq-r6-07-03) / [OQ-R6-27-01](../chapters/27_Security_Privacy_Lifecycle.md#oq-r6-27-01) / [OQ-R6-27-03](../chapters/27_Security_Privacy_Lifecycle.md#oq-r6-27-03) |
| TBD-013 | JETへ提出する非影響説明と必要試験の範囲 | [OQ-R6-15-02](../chapters/15_Deployment_Isolation.md#oq-r6-15-02) / [OQ-R6-16-02](../chapters/16_Certification_Change.md#oq-r6-16-02) |
| TBD-014 | 運用ログ保持期間・個人情報・障害解析アクセス | [OQ-R6-09-02](../chapters/09_Measurement_Data.md#oq-r6-09-02) / [OQ-R6-09-03](../chapters/09_Measurement_Data.md#oq-r6-09-03) / [OQ-R6-25-03](../chapters/25_Reliability_Availability_Maintainability.md#oq-r6-25-03) / [OQ-R6-26-06](../chapters/26_Manufacturing_Commissioning_Retirement.md#oq-r6-26-06) / [OQ-R6-27-06](../chapters/27_Security_Privacy_Lifecycle.md#oq-r6-27-06) |
| SYS-TBD-001 | 既存RS-485のroute_role・必須系統通信・全書込み元 | [OQ-R6-03-01](../chapters/03_Responsibilities.md#oq-r6-03-01) / [OQ-R6-07-01](../chapters/07_DER_Connections.md#oq-r6-07-01) |
| SYS-TBD-002 | RS-485の型式別プロトコル・操作・応答意味・タイミング | [OQ-R6-07-01](../chapters/07_DER_Connections.md#oq-r6-07-01) / [OQ-R6-22-03](../chapters/22_Physical_Electrical_Installation.md#oq-r6-22-03) |
| SYS-TBD-003 | RS-485 GW管理構成のG側独立性が現行実装で成立するか | [OQ-R6-10-02](../chapters/10_Grid_Protection.md#oq-r6-10-02) / [OQ-R6-15-01](../chapters/15_Deployment_Isolation.md#oq-r6-15-01) |
| SYS-TBD-004 | GWのECHONET Lite Device側公開と実資源の対応 | [OQ-R6-04-03](../chapters/04_Configurations_Profiles.md#oq-r6-04-03) / [OQ-R6-07-02](../chapters/07_DER_Connections.md#oq-r6-07-02) |
| SYS-TBD-005 | 自律HEMS無効時の既存機能維持と適用構成 | [OQ-R6-01-02](../chapters/01_Scope_Baseline.md#oq-r6-01-02) / [OQ-R6-04-01](../chapters/04_Configurations_Profiles.md#oq-r6-04-01) / [OQ-R6-08-01](../chapters/08_Advanced_EMS_Loads.md#oq-r6-08-01) / [OQ-R6-12-01](../chapters/12_Configuration_Lifecycle.md#oq-r6-12-01) / [OQ-R6-17-02](../chapters/17_Verification.md#oq-r6-17-02) / [OQ-R6-18-01](../chapters/18_Migration.md#oq-r6-18-01) |
| SYS-TBD-006 | RS-485／ECHONET Lite混在の資源・周期・最大台数 | [OQ-R6-04-02](../chapters/04_Configurations_Profiles.md#oq-r6-04-02) / [OQ-R6-07-03](../chapters/07_DER_Connections.md#oq-r6-07-03) / [OQ-R6-08-02](../chapters/08_Advanced_EMS_Loads.md#oq-r6-08-02) / [OQ-R6-14-01](../chapters/14_Performance_Security.md#oq-r6-14-01) / [OQ-R6-17-01](../chapters/17_Verification.md#oq-r6-17-01) |
| SYS-TBD-007 | 複数経路の同一性と経路切替を採用する範囲 | [OQ-R6-04-03](../chapters/04_Configurations_Profiles.md#oq-r6-04-03) / [OQ-R6-18-02](../chapters/18_Migration.md#oq-r6-18-02) |
| SYS-TBD-008 | 結果Unknownの保持期間・再確認・終端・利用者通知 | [OQ-R6-05-02](../chapters/05_Control_Contracts.md#oq-r6-05-02) / [OQ-R6-13-01](../chapters/13_Fault_Recovery_OTA.md#oq-r6-13-01) / [OQ-R6-20-03](../chapters/20_Northbound_Monitoring_FW.md#oq-r6-20-03) / [OQ-R6-24-02](../chapters/24_Product_Remote_Safety.md#oq-r6-24-02) |
| SYS-TBD-009 | 通常設定変更の反映状態・保留期限・緊急復旧契約 | [OQ-R6-06-02](../chapters/06_Usecases.md#oq-r6-06-02) / [OQ-R6-12-02](../chapters/12_Configuration_Lifecycle.md#oq-r6-12-02) / [OQ-R6-12-03](../chapters/12_Configuration_Lifecycle.md#oq-r6-12-03) |
| SYS-TBD-010 | 長期保存・制度・JC-STAR等の持越し要求の適用範囲 | [OQ-R6-07-03](../chapters/07_DER_Connections.md#oq-r6-07-03) / [OQ-R6-08-01](../chapters/08_Advanced_EMS_Loads.md#oq-r6-08-01) / [OQ-R6-09-01](../chapters/09_Measurement_Data.md#oq-r6-09-01) / [OQ-R6-09-02](../chapters/09_Measurement_Data.md#oq-r6-09-02) / [OQ-R6-16-01](../chapters/16_Certification_Change.md#oq-r6-16-01) / [OQ-R6-18-01](../chapters/18_Migration.md#oq-r6-18-01) / [OQ-R6-26-07](../chapters/26_Manufacturing_Commissioning_Retirement.md#oq-r6-26-07) / [OQ-R6-27-01](../chapters/27_Security_Privacy_Lifecycle.md#oq-r6-27-01) / [OQ-R6-27-05](../chapters/27_Security_Privacy_Lifecycle.md#oq-r6-27-05) |
| SYS-TBD-011 | 正式USDMとのID対応・製品承認者 | [OQ-R6-01-02](../chapters/01_Scope_Baseline.md#oq-r6-01-02) / [OQ-R6-01-04](../chapters/01_Scope_Baseline.md#oq-r6-01-04) / [OQ-R6-04-01](../chapters/04_Configurations_Profiles.md#oq-r6-04-01) / [OQ-R6-06-01](../chapters/06_Usecases.md#oq-r6-06-01) / [OQ-R6-17-01](../chapters/17_Verification.md#oq-r6-17-01) / [OQ-R6-17-02](../chapters/17_Verification.md#oq-r6-17-02) / [OQ-R6-19-01](../chapters/19_Open_Issues_Sources.md#oq-r6-19-01) / [OQ-R6-19-02](../chapters/19_Open_Issues_Sources.md#oq-r6-19-02) |
| SYS-TBD-012 | 上位管理・FW配信の物理配置、事業主体、役割・運用責任 | [OQ-R6-01-01](../chapters/01_Scope_Baseline.md#oq-r6-01-01) / [OQ-R6-02-01](../chapters/02_System_Context.md#oq-r6-02-01) / [OQ-R6-26-07](../chapters/26_Manufacturing_Commissioning_Retirement.md#oq-r6-26-07) |
| SYS-TBD-013 | 上位接続プロトコル・接続開始方向・FQDN/ポート/IPv4/IPv6 | [OQ-R6-20-01](../chapters/20_Northbound_Monitoring_FW.md#oq-r6-20-01) / [OQ-R6-27-03](../chapters/27_Security_Privacy_Lifecycle.md#oq-r6-27-03) |
| SYS-TBD-014 | 直接無線方式・ルータ接続・AP/STA同時能力と切替 | [OQ-R6-02-02](../chapters/02_System_Context.md#oq-r6-02-02) |
| SYS-TBD-015 | Web資産の配置・ローカル到達・認証・TLS・オフライン利用 | [OQ-R6-02-02](../chapters/02_System_Context.md#oq-r6-02-02) / [OQ-R6-20-02](../chapters/20_Northbound_Monitoring_FW.md#oq-r6-20-02) / [OQ-R6-27-03](../chapters/27_Security_Privacy_Lifecycle.md#oq-r6-27-03) |
| SYS-TBD-016 | 利用者・上位サービス認証、所属・委譲・失効の契約 | [OQ-R6-01-01](../chapters/01_Scope_Baseline.md#oq-r6-01-01) / [OQ-R6-20-05](../chapters/20_Northbound_Monitoring_FW.md#oq-r6-20-05) / [OQ-R6-26-05](../chapters/26_Manufacturing_Commissioning_Retirement.md#oq-r6-26-05) / [OQ-R6-26-06](../chapters/26_Manufacturing_Commissioning_Retirement.md#oq-r6-26-06) / [OQ-R6-27-02](../chapters/27_Security_Privacy_Lifecycle.md#oq-r6-27-02) / [OQ-R6-27-06](../chapters/27_Security_Privacy_Lifecycle.md#oq-r6-27-06) |
| SYS-TBD-017 | GW内部操作・設定・情報の公開可能な実項目 | [OQ-R6-12-02](../chapters/12_Configuration_Lifecycle.md#oq-r6-12-02) / [OQ-R6-20-01](../chapters/20_Northbound_Monitoring_FW.md#oq-r6-20-01) / [OQ-R6-22-05](../chapters/22_Physical_Electrical_Installation.md#oq-r6-22-05) / [OQ-R6-24-03](../chapters/24_Product_Remote_Safety.md#oq-r6-24-03) / [OQ-R6-25-03](../chapters/25_Reliability_Availability_Maintainability.md#oq-r6-25-03) / [OQ-R6-26-02](../chapters/26_Manufacturing_Commissioning_Retirement.md#oq-r6-26-02) / [OQ-R6-27-04](../chapters/27_Security_Privacy_Lifecycle.md#oq-r6-27-04) |
| SYS-TBD-018 | FW更新対象・承認/署名・画像検証・適用/復旧方式 | [OQ-R6-06-02](../chapters/06_Usecases.md#oq-r6-06-02) / [OQ-R6-12-04](../chapters/12_Configuration_Lifecycle.md#oq-r6-12-04) / [OQ-R6-13-02](../chapters/13_Fault_Recovery_OTA.md#oq-r6-13-02) / [OQ-R6-20-04](../chapters/20_Northbound_Monitoring_FW.md#oq-r6-20-04) / [OQ-R6-27-02](../chapters/27_Security_Privacy_Lifecycle.md#oq-r6-27-02) / [OQ-R6-27-04](../chapters/27_Security_Privacy_Lifecycle.md#oq-r6-27-04) |
| SYS-TBD-019 | クラウド保存・イベント保持・要求キュー・再接続方針 | [OQ-R6-09-03](../chapters/09_Measurement_Data.md#oq-r6-09-03) / [OQ-R6-20-05](../chapters/20_Northbound_Monitoring_FW.md#oq-r6-20-05) |
| SYS-TBD-020 | 監視/操作/更新の数値SLAと上限 | [OQ-R6-14-01](../chapters/14_Performance_Security.md#oq-r6-14-01) / [OQ-R6-25-02](../chapters/25_Reliability_Availability_Maintainability.md#oq-r6-25-02) |
| SYS-TBD-021 | 通信設定で到達性を失う場合の確認・復旧条件 | [OQ-R6-12-03](../chapters/12_Configuration_Lifecycle.md#oq-r6-12-03) |
| SYS-TBD-022 | リモートアプリの実装形態・通知・オフライン閲覧・ローカル切替 | [OQ-R6-20-02](../chapters/20_Northbound_Monitoring_FW.md#oq-r6-20-02) / [OQ-R6-20-03](../chapters/20_Northbound_Monitoring_FW.md#oq-r6-20-03) / [OQ-R6-20-05](../chapters/20_Northbound_Monitoring_FW.md#oq-r6-20-05) |
| SYS-TBD-023 | サービス/Web/API/FW/アプリの互換とリリース・データ運用 | [OQ-R6-09-03](../chapters/09_Measurement_Data.md#oq-r6-09-03) / [OQ-R6-12-04](../chapters/12_Configuration_Lifecycle.md#oq-r6-12-04) / [OQ-R6-16-02](../chapters/16_Certification_Change.md#oq-r6-16-02) / [OQ-R6-18-02](../chapters/18_Migration.md#oq-r6-18-02) / [OQ-R6-20-04](../chapters/20_Northbound_Monitoring_FW.md#oq-r6-20-04) / [OQ-R6-26-05](../chapters/26_Manufacturing_Commissioning_Retirement.md#oq-r6-26-05) / [OQ-R6-26-07](../chapters/26_Manufacturing_Commissioning_Retirement.md#oq-r6-26-07) / [OQ-R6-27-05](../chapters/27_Security_Privacy_Lifecycle.md#oq-r6-27-05) / [OQ-R6-27-06](../chapters/27_Security_Privacy_Lifecycle.md#oq-r6-27-06) |
| SYS-TBD-024 | R4のEL自律取得／RS-485 GW管理に対応する型式・HW/FW | [OQ-R6-04-02](../chapters/04_Configurations_Profiles.md#oq-r6-04-02) / [OQ-R6-21-01](../chapters/21_Grid_Connection_Selection.md#oq-r6-21-01) |
| SYS-TBD-025 | GW_MANAGEDのG側実配置と必須通信・計測の独立性 | [OQ-R6-03-02](../chapters/03_Responsibilities.md#oq-r6-03-02) / [OQ-R6-12-01](../chapters/12_Configuration_Lifecycle.md#oq-r6-12-01) / [OQ-R6-15-01](../chapters/15_Deployment_Isolation.md#oq-r6-15-01) |
| SYS-TBD-026 | 接続構成に制約された施工・保守変更の認可と復旧 | [OQ-R6-12-02](../chapters/12_Configuration_Lifecycle.md#oq-r6-12-02) / [OQ-R6-21-02](../chapters/21_Grid_Connection_Selection.md#oq-r6-21-02) / [OQ-R6-26-03](../chapters/26_Manufacturing_Commissioning_Retirement.md#oq-r6-26-03) |
| SYS-TBD-027 | 方式ごとの対象登録・認証構成・切替手続き | [OQ-R6-16-01](../chapters/16_Certification_Change.md#oq-r6-16-01) / [OQ-R6-16-02](../chapters/16_Certification_Change.md#oq-r6-16-02) / [OQ-R6-21-02](../chapters/21_Grid_Connection_Selection.md#oq-r6-21-02) / [OQ-R6-26-04](../chapters/26_Manufacturing_Commissioning_Retirement.md#oq-r6-26-04) |
| SYS-TBD-028 | 保持・時刻・必須通信・切替の具体数値 | [OQ-R6-21-02](../chapters/21_Grid_Connection_Selection.md#oq-r6-21-02) |
| SYS-TBD-029 | PCS側公開情報と各画面に出せる方式・適用状態 | [OQ-R6-20-03](../chapters/20_Northbound_Monitoring_FW.md#oq-r6-20-03) / [OQ-R6-21-01](../chapters/21_Grid_Connection_Selection.md#oq-r6-21-01) / [OQ-R6-26-04](../chapters/26_Manufacturing_Commissioning_Retirement.md#oq-r6-26-04) |
| SYS-TBD-030 | 複数scopeでの二方式混在と共通連系点制約 | [OQ-R6-11-02](../chapters/11_Power_Constraints.md#oq-r6-11-02) |
| SYS-TBD-031 | ルータ–GW／EL接続PCSの有線無線・LAN分離・アドレス・発見条件 | [OQ-R6-02-01](../chapters/02_System_Context.md#oq-r6-02-01) / [OQ-R6-26-03](../chapters/26_Manufacturing_Commissioning_Retirement.md#oq-r6-26-03) |
| SYS-TBD-032 | 共有ルータ故障・帯域競合と各取得主体の縮退条件 | [OQ-R6-06-02](../chapters/06_Usecases.md#oq-r6-06-02) / [OQ-R6-13-01](../chapters/13_Fault_Recovery_OTA.md#oq-r6-13-01) / [OQ-R6-14-02](../chapters/14_Performance_Security.md#oq-r6-14-02) / [OQ-R6-15-02](../chapters/15_Deployment_Isolation.md#oq-r6-15-02) |
| SYS-TBD-033 | EL接続PCSのサーバ取得プロトコル・資格・公開情報 | [OQ-R6-21-01](../chapters/21_Grid_Connection_Selection.md#oq-r6-21-01) |
| SYS-TBD-034 | 両IF PCS・仮想EL公開・既設R3設定の対応付けと移行 | [OQ-R6-04-03](../chapters/04_Configurations_Profiles.md#oq-r6-04-03) / [OQ-R6-12-04](../chapters/12_Configuration_Lifecycle.md#oq-r6-12-04) / [OQ-R6-18-02](../chapters/18_Migration.md#oq-r6-18-02) / [OQ-R6-24-03](../chapters/24_Product_Remote_Safety.md#oq-r6-24-03) / [OQ-R6-26-03](../chapters/26_Manufacturing_Commissioning_Retirement.md#oq-r6-26-03) / [OQ-R6-26-05](../chapters/26_Manufacturing_Commissioning_Retirement.md#oq-r6-26-05) |

## 既存パラメータ50件との対応

| 既存ID | 既存の未決内容 | 具体化するR6 OQ |
|---|---|---|
| PAR-PLAN-01 | 計画演算周期・期限 | [OQ-R6-08-02](../chapters/08_Advanced_EMS_Loads.md#oq-r6-08-02) / [OQ-R6-14-01](../chapters/14_Performance_Security.md#oq-r6-14-01) |
| PAR-MEAS-01 | 取得周期と機器内更新周期 | [OQ-R6-09-01](../chapters/09_Measurement_Data.md#oq-r6-09-01) |
| PAR-MEAS-02 | 制御に用いる最大鮮度 | [OQ-R6-08-02](../chapters/08_Advanced_EMS_Loads.md#oq-r6-08-02) / [OQ-R6-09-01](../chapters/09_Measurement_Data.md#oq-r6-09-01) |
| PAR-CMD-01 | 最小設定更新間隔 | [OQ-R6-14-01](../chapters/14_Performance_Security.md#oq-r6-14-01) |
| PAR-CMD-02 | 最大バースト・同時要求 | [OQ-R6-14-01](../chapters/14_Performance_Security.md#oq-r6-14-01) |
| PAR-CMD-03 | 応答期限 | [OQ-R6-07-01](../chapters/07_DER_Connections.md#oq-r6-07-01) |
| PAR-CMD-04 | 再試行回数・間隔 | [OQ-R6-13-01](../chapters/13_Fault_Recovery_OTA.md#oq-r6-13-01) |
| PAR-RESULT-01 | 達成確認窓・許容差 | [OQ-R6-05-02](../chapters/05_Control_Contracts.md#oq-r6-05-02) |
| PAR-RESULT-02 | Unknownの再確認期限・保持 | [OQ-R6-05-02](../chapters/05_Control_Contracts.md#oq-r6-05-02) |
| PAR-AUTH-01 | Lease・冪等情報の期間 | [OQ-R6-05-01](../chapters/05_Control_Contracts.md#oq-r6-05-01) |
| PAR-RS-01 | 接続条件・局数 | [OQ-R6-07-01](../chapters/07_DER_Connections.md#oq-r6-07-01) / [OQ-R6-22-03](../chapters/22_Physical_Electrical_Installation.md#oq-r6-22-03) |
| PAR-RS-02 | 制御・監視・必須通信のバス予算 | [OQ-R6-07-01](../chapters/07_DER_Connections.md#oq-r6-07-01) |
| PAR-EL-01 | 接続台数・探索・取得予算 | [OQ-R6-07-02](../chapters/07_DER_Connections.md#oq-r6-07-02) |
| PAR-GRID-01 | スケジュール取得・適用・有効期限 | [OQ-R6-10-01](../chapters/10_Grid_Protection.md#oq-r6-10-01) |
| PAR-GRID-02 | G側必須通信異常時動作・時間 | [OQ-R6-10-01](../chapters/10_Grid_Protection.md#oq-r6-10-01) / [OQ-R6-25-01](../chapters/25_Reliability_Availability_Maintainability.md#oq-r6-25-01) |
| PAR-GRID-03 | 系統連系保護の条件・動作時間 | [OQ-R6-10-02](../chapters/10_Grid_Protection.md#oq-r6-10-02) |
| PAR-GRID-04 | 過渡応答・許容差・評価窓 | [OQ-R6-11-02](../chapters/11_Power_Constraints.md#oq-r6-11-02) |
| PAR-GRID-05 | 制約の容量基準・対象scope | [OQ-R6-11-01](../chapters/11_Power_Constraints.md#oq-r6-11-01) |
| PAR-CFG-01 | 設定反映状態・保留期限 | [OQ-R6-12-01](../chapters/12_Configuration_Lifecycle.md#oq-r6-12-01) / [OQ-R6-12-03](../chapters/12_Configuration_Lifecycle.md#oq-r6-12-03) |
| PAR-DATA-01 | 短期・長期・監査の保持期間 | [OQ-R6-09-02](../chapters/09_Measurement_Data.md#oq-r6-09-02) |
| PAR-DATA-02 | 保存粒度・容量・書込み予算 | [OQ-R6-09-02](../chapters/09_Measurement_Data.md#oq-r6-09-02) / [OQ-R6-22-02](../chapters/22_Physical_Electrical_Installation.md#oq-r6-22-02) / [OQ-R6-25-01](../chapters/25_Reliability_Availability_Maintainability.md#oq-r6-25-01) / [OQ-R6-25-04](../chapters/25_Reliability_Availability_Maintainability.md#oq-r6-25-04) |
| PAR-ISO-01 | CPU・メモリ・キュー・帯域予算 | [OQ-R6-03-02](../chapters/03_Responsibilities.md#oq-r6-03-02) / [OQ-R6-14-02](../chapters/14_Performance_Security.md#oq-r6-14-02) / [OQ-R6-25-02](../chapters/25_Reliability_Availability_Maintainability.md#oq-r6-25-02) |
| PAR-ENV-01 | 温度・電源・reset・設置条件 | [OQ-R6-22-01](../chapters/22_Physical_Electrical_Installation.md#oq-r6-22-01) / [OQ-R6-22-02](../chapters/22_Physical_Electrical_Installation.md#oq-r6-22-02) / [OQ-R6-22-03](../chapters/22_Physical_Electrical_Installation.md#oq-r6-22-03) / [OQ-R6-22-04](../chapters/22_Physical_Electrical_Installation.md#oq-r6-22-04) / [OQ-R6-22-05](../chapters/22_Physical_Electrical_Installation.md#oq-r6-22-05) / [OQ-R6-23-01](../chapters/23_Environment_EMC_Transport.md#oq-r6-23-01) / [OQ-R6-23-02](../chapters/23_Environment_EMC_Transport.md#oq-r6-23-02) / [OQ-R6-23-03](../chapters/23_Environment_EMC_Transport.md#oq-r6-23-03) / [OQ-R6-23-04](../chapters/23_Environment_EMC_Transport.md#oq-r6-23-04) / [OQ-R6-26-02](../chapters/26_Manufacturing_Commissioning_Retirement.md#oq-r6-26-02) |
| PAR-SEC-01 | 認証・暗号化・資格情報・保守許可 | [OQ-R6-27-01](../chapters/27_Security_Privacy_Lifecycle.md#oq-r6-27-01) / [OQ-R6-27-03](../chapters/27_Security_Privacy_Lifecycle.md#oq-r6-27-03) |
| PAR-UP-01 | 上位要求・イベント・再接続の頻度とburst | [OQ-R6-20-01](../chapters/20_Northbound_Monitoring_FW.md#oq-r6-20-01) |
| PAR-UP-02 | オフライン要求のTTLと保留上限 | [OQ-R6-20-01](../chapters/20_Northbound_Monitoring_FW.md#oq-r6-20-01) |
| PAR-UP-03 | 重複排除・結果照会の保持期間 | [OQ-R6-20-01](../chapters/20_Northbound_Monitoring_FW.md#oq-r6-20-01) |
| PAR-UP-04 | 監視取得・報告・画面更新周期と鮮度 | [OQ-R6-20-02](../chapters/20_Northbound_Monitoring_FW.md#oq-r6-20-02) |
| PAR-UP-05 | Web/アプリの同時セッション数・認可寿命 | [OQ-R6-20-02](../chapters/20_Northbound_Monitoring_FW.md#oq-r6-20-02) |
| PAR-UP-06 | 履歴/診断のページサイズ・容量・同時Job上限 | [OQ-R6-09-03](../chapters/09_Measurement_Data.md#oq-r6-09-03) |
| PAR-UP-07 | イベント保存量・監査優先度・再同期窓 | [OQ-R6-09-03](../chapters/09_Measurement_Data.md#oq-r6-09-03) |
| PAR-UP-08 | 直接無線の稼働条件・有効時間・接続数 | [OQ-R6-02-02](../chapters/02_System_Context.md#oq-r6-02-02) |
| PAR-UP-09 | ネットワーク変更の確認期限・復旧猶予 | [OQ-R6-12-03](../chapters/12_Configuration_Lifecycle.md#oq-r6-12-03) |
| PAR-UP-10 | FW画像/一時保存/復旧領域の必要容量 | [OQ-R6-13-02](../chapters/13_Fault_Recovery_OTA.md#oq-r6-13-02) / [OQ-R6-20-04](../chapters/20_Northbound_Monitoring_FW.md#oq-r6-20-04) / [OQ-R6-25-04](../chapters/25_Reliability_Availability_Maintainability.md#oq-r6-25-04) |
| PAR-UP-11 | FW転送帯域・再試行・CPU予算 | [OQ-R6-14-02](../chapters/14_Performance_Security.md#oq-r6-14-02) |
| PAR-UP-12 | FW適用・起動・稼働確認・復旧期限 | [OQ-R6-13-02](../chapters/13_Fault_Recovery_OTA.md#oq-r6-13-02) / [OQ-R6-20-04](../chapters/20_Northbound_Monitoring_FW.md#oq-r6-20-04) / [OQ-R6-25-01](../chapters/25_Reliability_Availability_Maintainability.md#oq-r6-25-01) |
| PAR-UP-13 | 高影響内部Jobの期限・並行実行・取消し条件 | [OQ-R6-20-01](../chapters/20_Northbound_Monitoring_FW.md#oq-r6-20-01) |
| PAR-UP-14 | オフライン認可・失効伝達・所有者変更の期限 | [OQ-R6-20-05](../chapters/20_Northbound_Monitoring_FW.md#oq-r6-20-05) / [OQ-R6-27-02](../chapters/27_Security_Privacy_Lifecycle.md#oq-r6-27-02) |
| PAR-UP-15 | TLS/鍵/接続先識別/ローカル名前解決プロファイル | [OQ-R6-27-02](../chapters/27_Security_Privacy_Lifecycle.md#oq-r6-27-02) |
| PAR-UP-16 | GW/Web/API/クラウド/アプリの互換範囲 | [OQ-R6-18-02](../chapters/18_Migration.md#oq-r6-18-02) |
| PAR-GSEL-01 | 方式切替準備・旧主体停止確認・適用確認の各期限 | [OQ-R6-21-02](../chapters/21_Grid_Connection_Selection.md#oq-r6-21-02) |
| PAR-GSEL-02 | スケジュール保持・期限・時刻許容差 | [OQ-R6-10-01](../chapters/10_Grid_Protection.md#oq-r6-10-01) |
| PAR-GSEL-03 | G側PCS指示・監視周期と通信断時動作条件 | [OQ-R6-10-02](../chapters/10_Grid_Protection.md#oq-r6-10-02) |
| PAR-GSEL-04 | 切替中の制約保持・必要停止・復旧条件 | [OQ-R6-21-02](../chapters/21_Grid_Connection_Selection.md#oq-r6-21-02) |
| PAR-GSEL-05 | GW G側のCPU・通信・保存・バス負荷上限 | [OQ-R6-15-02](../chapters/15_Deployment_Isolation.md#oq-r6-15-02) |
| PAR-GSEL-06 | 方式・適用状態の公開項目と最大観測経過時間 | [OQ-R6-21-01](../chapters/21_Grid_Connection_Selection.md#oq-r6-21-01) |
| PAR-GNET-01 | 宅内ルータ経路の必須LAN/WAN・名前解決・アドレス条件 | [OQ-R6-02-01](../chapters/02_System_Context.md#oq-r6-02-01) |
| PAR-GNET-02 | 取得経路断の検出・再接続・再取得条件 | [OQ-R6-13-01](../chapters/13_Fault_Recovery_OTA.md#oq-r6-13-01) |
| PAR-GNET-03 | FW・監視の送信量／並行数と取得通信の共存予算 | [OQ-R6-14-02](../chapters/14_Performance_Security.md#oq-r6-14-02) |
| PAR-GNET-04 | PCS独立取得状態の公開項目と鮮度・不明判定 | [OQ-R6-21-01](../chapters/21_Grid_Connection_Selection.md#oq-r6-21-01) |

<!-- R6:OPEN_QUESTIONS -->
<a id="oq-list-appendices-open-question-register-md"></a>
## Open Questions — 本ノートを完成させるための未決事項

本ノートに関係する質問を、下表の正本章で管理する。同じ質問を別IDで重複起票せず、回答・採用値・決定記録を参照元にも反映する。履歴本文は当時の状態であり、現在の未決事項が解消した証拠にはしない。

| Open Question・正本章 | 具体的に不足する判断 | 解消時に必要な成果物 |
|---|---|---|
| [OQ-R6-19-02](../chapters/19_Open_Issues_Sources.md#oq-r6-19-02) | 各OQの実担当者、回答期限、提案G0〜G4の採否と正式レビュー日をどう定めるか。未決のまま許される作業と停止する判断はどこか。 | OQへ担当・期限・決定者を記入し、回答→根拠確認→承認→本文/台帳/テスト反映の閉鎖手順を合意する。 |
| [OQ-R6-19-01](../chapters/19_Open_Issues_Sources.md#oq-r6-19-01) | 正式USDMの正本・IDは何か。124件のSYSと今回の補完項目を誰が要求へ対応付け、重複・不足・対象外を承認するか。 | USDM→機能→SYS/補完項目→設計→検証の対応を版付きで完成し、未記入を適合扱いしない。 |

担当者・期限・状態はリンク先を正本とする。新たな数値や認証判断を本参照表だけで確定しない。
