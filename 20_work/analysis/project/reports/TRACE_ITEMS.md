# R13 Trace索引（生成ビュー）

文書DTRと項目ITRを区別。既存IDを保持し、旧文書版はスナップショット参照。review=nullは未確認であり採用/合格ではない。


| ITR／版 | native ID | 項目 | 所在 |
|---|---|---|---|
| ITR-SPKGW-TASK-000001 / 1.2.0 | TASK-SPKGW-000001 | 開発管理の担当・承認分掌と標準の採用範囲を決める | [原文](../../../../20_work/drafts/project/tasks/TASK-SPKGW-000001.md#task-spkgw-000001) |
| ITR-SPKGW-TASK-000002 / 1.2.0 | TASK-SPKGW-000002 | 既存開発作業を棚卸ししWBSと基準計画を作る | [原文](../../../../20_work/drafts/project/tasks/TASK-SPKGW-000002.md#task-spkgw-000002) |
| ITR-SPKGW-TASK-000003 / 1.2.0 | TASK-SPKGW-000003 | 予算・単価・実績収集・発注管理の基準を決める | [原文](../../../../20_work/drafts/project/tasks/TASK-SPKGW-000003.md#task-spkgw-000003) |
| ITR-SPKGW-TASK-000004 / 1.2.0 | TASK-SPKGW-000004 | Windowsと実運用環境でガバナンスツールを確認する | [原文](../../../../20_work/drafts/project/tasks/TASK-SPKGW-000004.md#task-spkgw-000004) |
| ITR-SPKGW-REQ-000001 / 1 | SYS-RESP-001 | DER実行責務の名称 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000002 / 1 | SYS-GRID-001 | 独立した出力制御経路 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000003 / 1 | SYS-GRID-002 | 独立した系統連系保護 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000004 / 1 | SYS-BOUND-001 | 通常APIの禁止操作 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000005 / 1 | SYS-GRID-003 | 必須計測・時刻・保存の独立性 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000006 / 1 | SYS-AUTH-001 | 資源と変換グループの権威 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000007 / 1 | SYS-AUTH-002 | 最後の送信境界の再検査 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000008 / 1 | SYS-ORCH-001 | ワークフローと補償の所有 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000009 / 1 | SYS-ADAPT-001 | Adapterの政策非所有 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000010 / 1 | SYS-CAP-001 | 機器別の実能力 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000011 / 1 | SYS-RESULT-001 | 受理と達成の区別 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000012 / 1 | SYS-TOPO-001 | 制約scopeの分離 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000013 / 1 | SYS-CONST-001 | 古い制約コピー | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000014 / 1 | SYS-CONST-002 | 負荷急変時の制約成立 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000015 / 1 | SYS-ISO-001 | 実行資源非干渉 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000016 / 1 | SYS-OTA-001 | 更新と書込み権限の分離 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000017 / 1 | SYS-OTA-002 | 復帰後の再照合 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000018 / 1 | SYS-EXPIRY-001 | 機器内保持と利用者期限 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000019 / 1 | SYS-COEX-001 | 別操作元との共存 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000020 / 1 | SYS-CERT-001 | 認証・接続・版の構成台帳 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000021 / 1 | SYS-ISO-002 | 共通原因の評価 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000022 / 1 | SYS-CHG-001 | 通常更新の前提確認 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000023 / 1 | SYS-TIME-001 | 保護と出力制御の時間分離 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000024 / 1 | SYS-LOG-001 | 相関を持つ証跡 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000025 / 1 | SYS-SCOPE-001 | 製品と接続依存の範囲 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000026 / 1 | SYS-DEPLOY-001 | 接続種別に制約された二方式の配備 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000027 / 1 | SYS-REQ-001 | 要求経路の統一 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000028 / 1 | SYS-RS-001 | RS-485既存機能の独立扱い | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000029 / 1 | SYS-RS-002 | RS-485通信仕様プロファイル | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000030 / 1 | SYS-RS-003 | RS-485通信役割の台帳 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000031 / 1 | SYS-RS-004 | 方式名で配置を決めない | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000032 / 1 | SYS-RS-005 | 生電文の迂回防止 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000033 / 1 | SYS-RS-006 | 共有バス負荷と読出し | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000034 / 1 | SYS-SEM-001 | 経路間の意味同等性 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000035 / 1 | SYS-EL-001 | Controller／Device役割の区別 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000036 / 1 | SYS-EL-002 | 公開応答の意味 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000037 / 1 | SYS-ROUTE-001 | 経路同一性と切替 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000038 / 1 | SYS-CAP-002 | UNKNOWNの限定運転 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000039 / 1 | SYS-RESULT-002 | 原因不明の保持 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000040 / 1 | SYS-RESULT-003 | 値の段階分離 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000041 / 1 | SYS-RETRY-001 | 再送と再計画の責任 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000042 / 1 | SYS-LOAD-001 | 負荷実行とDER実行 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000043 / 1 | SYS-EMS-001 | 利用可能能力での計画 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000044 / 1 | SYS-MEAS-001 | 観測基準と品質 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000045 / 1 | SYS-MEAS-002 | 経路・オブジェクトの二重計上防止 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000046 / 1 | SYS-DATA-001 | 用途別保存 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000047 / 1 | SYS-DATA-002 | 欠測を含む抽出 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000048 / 1 | SYS-CFG-001 | 運転調停と設定調停の分離 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000049 / 1 | SYS-CFG-002 | 通常変更と緊急復旧 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000050 / 1 | SYS-CFG-003 | 復元境界 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000051 / 1 | SYS-PERF-001 | 操作ごとの時間契約 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000052 / 1 | SYS-PERF-002 | 有限な資源上限 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000053 / 1 | SYS-SEC-001 | 接続セキュリティ文脈 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000054 / 1 | SYS-SEC-002 | 評価体系の分離 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000055 / 1 | SYS-FAULT-001 | 通信断位置の区別 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000056 / 1 | SYS-CERT-002 | 試験免除の非保証 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000057 / 1 | SYS-MIG-001 | 既存経路の棚卸し | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000058 / 1 | SYS-MIG-002 | Legacy適用差 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000059 / 1 | SYS-BASE-001 | ドラフトと評価状態 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000060 / 1 | SYS-VERIFY-001 | 検証条件と証拠 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000061 / 1 | SYS-CTX-001 | 外部役割の分離 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000062 / 1 | SYS-CTX-002 | GWと外部サービスの保証境界 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000063 / 1 | SYS-NORTH-001 | 用途別Usecaseへの振分け | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000064 / 1 | SYS-NORTH-002 | 操作者と配送主体の認可 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000065 / 1 | SYS-NORTH-003 | オフライン要求の有限性 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000066 / 1 | SYS-NORTH-004 | 重複排除と結果照合 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000067 / 1 | SYS-NORTH-005 | 有限な監視・診断負荷 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000068 / 1 | SYS-NORTH-006 | イベントの欠落と再同期 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000069 / 1 | SYS-NORTH-007 | チャネル非依存の操作権限と監査 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000070 / 1 | SYS-CFG-004 | 設定世代の競合検査 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000071 / 1 | SYS-CFG-005 | 希望・保存・有効設定の分離 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000072 / 1 | SYS-CFG-006 | ネットワーク設定の到達性確認 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000073 / 1 | SYS-GWOP-001 | 内部機能操作の許可リスト | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000074 / 1 | SYS-GWOP-002 | 高影響操作と変更の排他 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000075 / 1 | SYS-UI-001 | 直接無線の宅内Web UI | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000076 / 1 | SYS-UI-002 | ルータ経由の宅内Web UI | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000077 / 1 | SYS-UI-003 | 直接接続とWANの独立した可用性 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000078 / 1 | SYS-UI-004 | クラウド非依存のローカル利用 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000079 / 1 | SYS-UI-005 | Web境界と互換性 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000080 / 1 | SYS-APP-001 | クラウド経由リモートアプリ | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000081 / 1 | SYS-APP-002 | 受付段階と鮮度の表示 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000082 / 1 | SYS-APP-003 | 所属変更と資格失効 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000083 / 1 | SYS-FW-001 | 配信と承認と適用の分離 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000084 / 1 | SYS-FW-002 | 配布物の対象・完全性・系列確認 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000085 / 1 | SYS-FW-003 | H/G更新権限と認可復旧 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000086 / 1 | SYS-FW-004 | 更新段階と永続復旧情報 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000087 / 1 | SYS-FW-005 | 配信障害と更新転送負荷の限定 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000088 / 1 | SYS-STATE-001 | 内部情報の選択的公開 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000089 / 1 | SYS-STATE-002 | 観測とクラウドコピーの区別 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000090 / 1 | SYS-SVC-001 | サービス・UI・FW互換性の管理 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000091 / 1 | SYS-ISO-003 | 外部接続追加時の共有影響 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000092 / 1 | SYS-CHG-002 | クラウド・UI変更の非影響判定 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000093 / 1 | SYS-GSEL-001 | 機器接続別の取得・適用契約 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000094 / 1 | SYS-GSEL-002 | 確認済み構成からの選択 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000095 / 1 | SYS-GSEL-003 | scopeと適用主体の一意性 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000096 / 1 | SYS-GSEL-004 | 通常要求経路の非迂回 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000097 / 1 | SYS-GSEL-005 | GW管理方式のH側非依存 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000098 / 1 | SYS-GSEL-006 | 正本と資格情報の領域分離 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000099 / 1 | SYS-GSEL-007 | 適用条件内の施工保守による構成変更 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000100 / 1 | SYS-GSEL-008 | 制約を維持する引継ぎ | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000101 / 1 | SYS-GSEL-009 | 古い経路と残留指令の無効化 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000102 / 1 | SYS-GSEL-010 | 自動方式切替の非採用 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000103 / 1 | SYS-GSEL-011 | H停止とGW全体喪失の区別 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000104 / 1 | SYS-GSEL-012 | 共用PCS通信の所有 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000105 / 1 | SYS-GSEL-013 | 表示状態と実適用の分離 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000106 / 1 | SYS-GSEL-014 | 非公開状態の扱い | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000107 / 1 | SYS-GSEL-015 | H更新と方式bindingの不変 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000108 / 1 | SYS-GSEL-016 | 方式別の認証構成評価 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000109 / 1 | SYS-GSEL-017 | 共有scopeの全体制約 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000110 / 1 | SYS-GSEL-018 | 切替中断時の永続復旧 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000111 / 1 | SYS-GSEL-019 | 機器交換と再登録 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000112 / 1 | SYS-GSEL-020 | 選択と適用結果の監査 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000113 / 1 | SYS-GNET-001 | 宅内ルータ必須経路 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000114 / 1 | SYS-GNET-002 | PCS自律取得の対象限定 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000115 / 1 | SYS-GNET-003 | RS-485のGW管理経路 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000116 / 1 | SYS-GNET-004 | 通常EL通信と出力制御サーバ通信の分離 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000117 / 1 | SYS-GNET-005 | ルータ共有障害と保持動作 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000118 / 1 | SYS-GNET-006 | ルータ混雑と変更影響 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000119 / 1 | SYS-GNET-007 | 経路別の可観測性 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000120 / 1 | SYS-GNET-008 | 旧方式設定の再評価 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000121 / 1 | SYS-GNET-009 | 混在構成の独立所有 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000122 / 1 | SYS-GNET-010 | 直接Web接続の非代替 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000123 / 1 | SYS-GNET-011 | 経路を含む変更証拠 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-REQ-000124 / 1 | SYS-GNET-012 | 多重IF・仮想機器の分類 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/requirements.json) |
| ITR-SPKGW-SFUNC-000001 / 1 | S-FN-001 | エネルギー・設備状態の把握 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/function_catalog.json) |
| ITR-SPKGW-SFUNC-000002 / 1 | S-FN-002 | 宅内モニタリング・操作 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/function_catalog.json) |
| ITR-SPKGW-SFUNC-000003 / 1 | S-FN-003 | リモートモニタリング・操作 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/function_catalog.json) |
| ITR-SPKGW-SFUNC-000004 / 1 | S-FN-004 | PV・蓄電池等の通常運転 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/function_catalog.json) |
| ITR-SPKGW-SFUNC-000005 / 1 | S-FN-005 | 空調・給湯等の負荷操作 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/function_catalog.json) |
| ITR-SPKGW-SFUNC-000006 / 1 | S-FN-006 | 高度エネマネ運転計画 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/function_catalog.json) |
| ITR-SPKGW-SFUNC-000007 / 1 | S-FN-007 | 計画評価・再計画 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/function_catalog.json) |
| ITR-SPKGW-SFUNC-000008 / 1 | S-FN-008 | 設備登録・接続構成管理 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/function_catalog.json) |
| ITR-SPKGW-SFUNC-000009 / 1 | S-FN-009 | 設定変更・保存・復元 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/function_catalog.json) |
| ITR-SPKGW-SFUNC-000010 / 1 | S-FN-010 | GW内部機能の操作 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/function_catalog.json) |
| ITR-SPKGW-SFUNC-000011 / 1 | S-FN-011 | FW配信・適用・復旧 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/function_catalog.json) |
| ITR-SPKGW-SFUNC-000012 / 1 | S-FN-012 | RS-485 PCSの遠隔出力制御 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/function_catalog.json) |
| ITR-SPKGW-SFUNC-000013 / 1 | S-FN-013 | EL接続PCSの自律出力制御 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/function_catalog.json) |
| ITR-SPKGW-SFUNC-000014 / 1 | S-FN-014 | PCS側の系統連系保護 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/function_catalog.json) |
| ITR-SPKGW-SFUNC-000015 / 1 | S-FN-015 | 競合・通信断・停止・復旧の協調 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/function_catalog.json) |
| ITR-SPKGW-SFUNC-000016 / 1 | S-FN-016 | 警報・通知・診断 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/function_catalog.json) |
| ITR-SPKGW-SFUNC-000017 / 1 | S-FN-017 | 履歴の保存・提出・利用 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/function_catalog.json) |
| ITR-SPKGW-SFUNC-000018 / 1 | S-FN-018 | 外部HEMSとの機器公開連携 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/function_catalog.json) |
| ITR-SPKGW-SFUNC-000019 / 1 | S-FN-019 | 利用者識別・権限・所属管理 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/function_catalog.json) |
| ITR-SPKGW-SFUNC-000020 / 1 | S-FN-020 | 製造・施工・保守・交換・廃棄支援 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/function_catalog.json) |
| ITR-SPKGW-SFUNC-000021 / 1 | S-FN-021 | 通信・周辺機器の構成と復旧 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/function_catalog.json) |
| ITR-SPKGW-GFUNC-000001 / 1 | GW-FN-001 | 要求受付・認証認可・用途別振分け | [原文](../../../../10_canonical/releases/BL-R9-0001/data/function_catalog.json) |
| ITR-SPKGW-GFUNC-000002 / 1 | GW-FN-002 | 通常制御権・競合調停 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/function_catalog.json) |
| ITR-SPKGW-GFUNC-000003 / 1 | GW-FN-003 | 複数機器の実行進行・補償 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/function_catalog.json) |
| ITR-SPKGW-GFUNC-000004 / 1 | GW-FN-004 | DERの通常操作・達成確認 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/function_catalog.json) |
| ITR-SPKGW-GFUNC-000005 / 1 | GW-FN-005 | 空調・給湯等の負荷操作 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/function_catalog.json) |
| ITR-SPKGW-GFUNC-000006 / 1 | GW-FN-006 | 高度エネマネの計画生成 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/function_catalog.json) |
| ITR-SPKGW-GFUNC-000007 / 1 | GW-FN-007 | 実績評価・再計画・入力不足時縮退 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/function_catalog.json) |
| ITR-SPKGW-GFUNC-000008 / 1 | GW-FN-008 | 計測・状態の取得正規化 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/function_catalog.json) |
| ITR-SPKGW-GFUNC-000009 / 1 | GW-FN-009 | 履歴保存・抽出・上位同期 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/function_catalog.json) |
| ITR-SPKGW-GFUNC-000010 / 1 | GW-FN-010 | 機器探索・登録・識別・能力管理 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/function_catalog.json) |
| ITR-SPKGW-GFUNC-000011 / 1 | GW-FN-011 | RS-485 PCS通常操作・状態通信 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/function_catalog.json) |
| ITR-SPKGW-GFUNC-000012 / 1 | GW-FN-012 | ECHONET Lite Controller | [原文](../../../../10_canonical/releases/BL-R9-0001/data/function_catalog.json) |
| ITR-SPKGW-GFUNC-000013 / 1 | GW-FN-013 | ECHONET Lite Device側公開 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/function_catalog.json) |
| ITR-SPKGW-GFUNC-000014 / 1 | GW-FN-014 | GW G側スケジュール取得・管理 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/function_catalog.json) |
| ITR-SPKGW-GFUNC-000015 / 1 | GW-FN-015 | GW G側の出力制御指示・必須監視 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/function_catalog.json) |
| ITR-SPKGW-GFUNC-000016 / 1 | GW-FN-016 | PCS側の出力制御・保護状態の参照 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/function_catalog.json) |
| ITR-SPKGW-GFUNC-000017 / 1 | GW-FN-017 | 上位管理・監視サーバ接続 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/function_catalog.json) |
| ITR-SPKGW-GFUNC-000018 / 1 | GW-FN-018 | 宅内Web UI提供・ローカルAPI | [原文](../../../../10_canonical/releases/BL-R9-0001/data/function_catalog.json) |
| ITR-SPKGW-GFUNC-000019 / 1 | GW-FN-019 | リモートアプリ用状態・結果連携 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/function_catalog.json) |
| ITR-SPKGW-GFUNC-000020 / 1 | GW-FN-020 | 設定管理・変更調停 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/function_catalog.json) |
| ITR-SPKGW-GFUNC-000021 / 1 | GW-FN-021 | ネットワーク設定の変更・到達性復旧 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/function_catalog.json) |
| ITR-SPKGW-GFUNC-000022 / 1 | GW-FN-022 | 内部機能操作・ライフサイクルJob | [原文](../../../../10_canonical/releases/BL-R9-0001/data/function_catalog.json) |
| ITR-SPKGW-GFUNC-000023 / 1 | GW-FN-023 | FW取得・配布物検証 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/function_catalog.json) |
| ITR-SPKGW-GFUNC-000024 / 1 | GW-FN-024 | FW適用・稼働確認・復旧 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/function_catalog.json) |
| ITR-SPKGW-GFUNC-000025 / 1 | GW-FN-025 | 警報・監査・診断情報の公開 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/function_catalog.json) |
| ITR-SPKGW-GFUNC-000026 / 1 | GW-FN-026 | 故障検出・再接続・結果再照合 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/function_catalog.json) |
| ITR-SPKGW-GFUNC-000027 / 1 | GW-FN-027 | 資格情報・所属・失効・認可の管理 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/function_catalog.json) |
| ITR-SPKGW-GFUNC-000028 / 1 | GW-FN-028 | H/G境界の限定操作・不正入力拒否 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/function_catalog.json) |
| ITR-SPKGW-GFUNC-000029 / 1 | GW-FN-029 | 製造初期化・施工・試運転の機器側支援 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/function_catalog.json) |
| ITR-SPKGW-GFUNC-000030 / 1 | GW-FN-030 | バックアップ・初期化・交換・消去 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/function_catalog.json) |
| ITR-SPKGW-GFUNC-000031 / 1 | GW-FN-031 | 複数通信・USB等の接続管理 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/function_catalog.json) |
| ITR-SPKGW-GFUNC-000032 / 1 | GW-FN-032 | 起動・停止・操作開始条件の管理 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/function_catalog.json) |
| ITR-SPKGW-TEST-000001 / 1 | T01 | HEMS停止・プロセスkill・再起動・物理切離し | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000002 / 1 | T02 | 電力会社通信断、保存済みスケジュール、有効期限境界 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000003 / 1 | T03 | HEMS高負荷中に系統異常を模擬 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000004 / 1 | T04 | HEMS資格情報・OTA経路からG側設定／FWへの書込みを試行 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000005 / 1 | T05 | 過大値、負値、未対応モード、破損電文、旧版、最大頻度 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000006 / 1 | T06 | HEMS時計異常、計測停止、G側時計／保存異常を個別注入 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000007 / 1 | T07 | 権威交代直前の送信待ち、Lease失効、旧応答到来 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000008 / 1 | T08 | 同じHybrid PCSの複数EOJへ競合要求 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000009 / 1 | T09 | 複数機器計画の一部のみ受理・実行 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000010 / 1 | T10 | 未対応プロパティ・機器版変更・Capability欠損 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000011 / 1 | T11 | 高頻度の計画変更を入力 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000012 / 1 | T12 | Set受理後に出力未達、応答だけ消失、計測だけ消失 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000013 / 1 | T13 | PV＋蓄電池＋V2H、負荷遮断、EV離脱、変換器制限 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000014 / 1 | T14 | HEMS参照用制約が古い・不明・取得不能 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000015 / 1 | T15 | CPU最大負荷、メモリ圧迫、帯域集中、温度・電源条件 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000016 / 1 | T16 | OTA中断、H側watchdog、ロールバック、電源断復帰 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000017 / 1 | T17 | HEMS停止時に実機が最後の通常要求を保持 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000018 / 1 | T18 | 本体操作・メーカークラウドとの同時操作 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000019 / 1 | T19 | リリース前後の構成・依存・要求・結果を照合 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000020 / 1 | SYS-T01 | 既存RS-485通常制御・監視とHEMS無効／停止／再起動の回帰 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000021 / 1 | SYS-T02 | 両経路の同一意味操作、目標／上限差、符号・単位・未対応・丸め | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000022 / 1 | SYS-T03 | GWのController／Device共存、外部HEMS→RS-485、自己公開・重複検出 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000023 / 1 | SYS-T04 | RS-485＋ECHONET Liteの混在、最大台数・要求集中・計測の重複 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000024 / 1 | SYS-T05 | route_roleを確定したRS-485の通常リンク断／G必須通信断／共有サービス再起動 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000025 / 1 | SYS-T06 | 高優先度実行中の通常設定、緊急復旧、部分反映、旧設定リストア | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000026 / 1 | SYS-T07 | 同一物理設備の二経路、装置交換、採用する場合の経路切替 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000027 / 1 | SYS-T08 | 欠測、時刻異常、積算リセット、機器交換、保存飽和、データ抽出 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000028 / 1 | SYS-T09 | 認証・暗号化機器と従来機器の混在、復号後の共通処理、経路切替 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000029 / 1 | SYS-T10 | 全体目標・直接要求・自律HEMS、DERとFlexible Loadの混合実行 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000030 / 1 | SYS-T11 | 外部サーバ役割と5操作種別の配送を全接続経路で照合 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000031 / 1 | SYS-T12 | 直接無線で端末を接続しWAN・外部DNS・CDN・上位認証接続を遮断 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000032 / 1 | SYS-T13 | ルータ経由監視、端末隔離、別セグメント、AP/STA切替、到達先変更 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000033 / 1 | SYS-T14 | リモートアプリの利用者・住宅・GW・ロール違い、所属失効 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000034 / 1 | SYS-T15 | ローカルと上位が同じ基準設定世代で競合し、一部反映を遅延・失敗 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000035 / 1 | SYS-T16 | 上位保留要求の期限切れ・重複・逆順・同一キー異内容・再認可 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000036 / 1 | SYS-T17 | GW内部再探索・H側再起動・停止と設定/FWの競合、未許可操作 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000037 / 1 | SYS-T18 | 多数のWeb/アプリ監視とFresh Read・履歴・診断・FW取得を同時最大実行 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000038 / 1 | SYS-T19 | FWの署名/真正性不適合、改変、別機種・領域・依存版・旧系列を入力 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000039 / 1 | SYS-T20 | FW取得・適用・起動・稼働確認の各段階で通信断・中断・電断・並行再起動 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000040 / 1 | SYS-T21 | クラウドACKのみ、GW受理のみ、実機受理後未達、観測欠損、通知逆転 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000041 / 1 | SYS-T22 | SSID/IP/route/上位接続先変更で応答経路を断ち、共用G側依存も照合 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000042 / 1 | SYS-T23 | 直接AP/LANで未認可Webアクセス、CSRF/Origin/Host悪用、診断秘密混入を試験環境で検証 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000043 / 1 | SYS-T24 | 上位管理サービス停止・WAN断・再接続と操作期限境界 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000044 / 1 | SYS-T25 | FW配信サービスのみ停止、低速化、容量不足、再接続集中 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000045 / 1 | SYS-T26 | 所有者変更・GW再登録の後、旧アプリ/ローカル資格/保留要求で操作 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000046 / 1 | SYS-T27 | GW/Web/API/クラウド/アプリ版を混在させ、クラウド要求頻度や共通OSを変更 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000047 / 1 | SYS-T28 | イベントバッファあふれ・GW再起動・順序逆転・再同期と旧希望設定復元 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000048 / 1 | SYS-T29 | EL接続PCSが宅内ルータ経由で自律取得・適用中にGW通常操作・H停止・GW全停止を分けて実施 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000049 / 1 | SYS-T30 | RS-485接続PCSに対しGW G側が宅内ルータ経由で取得・保存・適用・指示し、H側を停止 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000050 / 1 | SYS-T31 | R4適用表外の組合せ、未選択・未対応PCS・不一致FW・旧世代・認可不足で有効化要求 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000051 / 1 | SYS-T32 | 同一scopeへPCS_DIRECTとGW_MANAGEDを同時有効化し、旧経路遅延指示も注入 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000052 / 1 | SYS-T33 | R4適用表を満たす初期配備又は承認済み機器・接続構成変更を実施 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000053 / 1 | SYS-T34 | 準備・旧主体停止・新主体有効化の各境界で通信断・電断・確認応答喪失 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000054 / 1 | SYS-T35 | PCS_DIRECT／GW_MANAGEDでH限定停止とGW全筐体停止を分けて注入 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000055 / 1 | SYS-T36 | 両方式でサーバ通信断・保持期限境界・時刻異常・監視断を注入 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000056 / 1 | SYS-T37 | H側OTA／一般バックアップ復元／初期化に古い方式bindingやG設定を混入 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000057 / 1 | SYS-T38 | Web／クラウド／アプリへ方式・適用情報を配信し、PCS非公開・古いコピー・切替途中を含める | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000058 / 1 | SYS-T39 | GW管理のRS-485必須経路に通常Set・読出し負荷を集中し、共有ルータにFW転送負荷を加える | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000059 / 1 | SYS-T40 | 二方式間変更、H/Gの各更新、共有driver／reset変更で構成・認証証拠を照合 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000060 / 1 | SYS-T41 | 独立scopeと共有PCS／共通連系点で二方式を混在させ容量配分・負荷離脱を試験 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000061 / 1 | SYS-T42 | 切替未完了中の再起動、GW／PCS交換、旧資格・旧binding・遅延応答の復元 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000062 / 1 | SYS-T43 | EL接続PCSの取得要求・応答とGWからの通常EL通信を別に追跡しGWを停止 | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000063 / 1 | SYS-T44 | RS-485 PCSのGW取得・適用・応答経路を追跡する | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000064 / 1 | SYS-T45 | 機器接続種別・mode・ルータ経路・取得能力を不整合にした構成を検査する | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000065 / 1 | SYS-T46 | WANのみ断、ルータ全停止、PCS側だけのLAN断を個別に注入し保持期限境界を通す | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000066 / 1 | SYS-T47 | FW取得・監視集中・ルータ設定変更・GW直接Webモード変更を行う | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000067 / 1 | SYS-T48 | H限定停止、GW全電断、ルータ電断、RS-485断を個別に注入する | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000068 / 1 | SYS-T49 | GW WAN正常だがPCSサーバ取得不能、EL応答正常だがPCS情報非公開等を組み合わせる | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-TEST-000069 / 1 | SYS-T50 | R3設定復元、GW仮想ELオブジェクト、両IF PCS、同一scope二重登録を評価する | [原文](../../../../10_canonical/releases/BL-R9-0001/data/test_catalog.json) |
| ITR-SPKGW-QUESTION-000001 / 1 | OQ-R6-01-01 | 利用者・施工者・運用者・保守者の役割 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/I_System/I-02_Actors_Roles.md#oq-r6-01-01) |
| ITR-SPKGW-QUESTION-000002 / 1 | OQ-R6-01-02 | 製品価値と対象外の判定 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/I_System/I-01_Purpose_Scope.md#oq-r6-01-02) |
| ITR-SPKGW-QUESTION-000003 / 1 | OQ-R6-01-03 | 用語・略語・数値表記 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/I_System/I-01_Purpose_Scope.md#oq-r6-01-03) |
| ITR-SPKGW-QUESTION-000004 / 1 | OQ-R6-01-04 | 規範別冊の版と仕様完成条件 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/I_System/I-01_Purpose_Scope.md#oq-r6-01-04) |
| ITR-SPKGW-QUESTION-000005 / 1 | OQ-R6-02-01 | 実ネットワークと接続先の実体 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/I_System/I-04_System_Context.md#oq-r6-02-01) |
| ITR-SPKGW-QUESTION-000006 / 1 | OQ-R6-02-02 | 宅内直接Webとルータ接続の成立条件 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/I_System/I-04_System_Context.md#oq-r6-02-02) |
| ITR-SPKGW-QUESTION-000007 / 1 | OQ-R6-03-01 | 実装配賦・状態所有者一覧 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/II_GW/II-01_GW_Architecture.md#oq-r6-03-01) |
| ITR-SPKGW-QUESTION-000008 / 1 | OQ-R6-03-02 | H内・H/G境界契約の具体項目 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/III_Interfaces/III-01_Boundary_Contracts.md#oq-r6-03-02) |
| ITR-SPKGW-QUESTION-000009 / 1 | OQ-R6-04-01 | 既存・追加・変更・廃止機能の母集団 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/II_GW/II-02_GW_Functions.md#oq-r6-04-01) |
| ITR-SPKGW-QUESTION-000010 / 1 | OQ-R6-04-02 | 機器・ソフトウェア・接続の対応組合せ | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/I_System/I-05_Configurations.md#oq-r6-04-02) |
| ITR-SPKGW-QUESTION-000011 / 1 | OQ-R6-04-03 | 探索・登録・解除・交換・同一性 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/II_GW/II-06_Device_Management.md#oq-r6-04-03) |
| ITR-SPKGW-QUESTION-000012 / 1 | OQ-R6-05-01 | 優先関係・同順位・取消し・並行実行 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/II_GW/II-03_Control_Execution.md#oq-r6-05-01) |
| ITR-SPKGW-QUESTION-000013 / 1 | OQ-R6-05-02 | 結果・確認窓・不明状態の終端 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/II_GW/II-03_Control_Execution.md#oq-r6-05-02) |
| ITR-SPKGW-QUESTION-000014 / 1 | OQ-R6-06-01 | 機能とUCの双方向対応 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/I_System/I-06_Usecases.md#oq-r6-06-01) |
| ITR-SPKGW-QUESTION-000015 / 1 | OQ-R6-06-02 | 横断条件・同時事象・利用場面 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/I_System/I-06_Usecases.md#oq-r6-06-02) |
| ITR-SPKGW-QUESTION-000016 / 1 | OQ-R6-07-01 | RS-485電文・接続条件・送信所有権 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/III_Interfaces/III-07_RS485_PCS.md#oq-r6-07-01) |
| ITR-SPKGW-QUESTION-000017 / 1 | OQ-R6-07-02 | ECHONET Lite Controller/Deviceの対象能力 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/III_Interfaces/III-06_ECHONET_Lite.md#oq-r6-07-02) |
| ITR-SPKGW-QUESTION-000018 / 1 | OQ-R6-07-03 | IPv4/IPv6・Wi-SUN・USB等の持越し要求 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/III_Interfaces/III-09_Network_Peripherals.md#oq-r6-07-03) |
| ITR-SPKGW-QUESTION-000019 / 1 | OQ-R6-08-01 | 高度エネマネ戦略の採否・適用・解除 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/II_GW/II-05_Advanced_EMS.md#oq-r6-08-01) |
| ITR-SPKGW-QUESTION-000020 / 1 | OQ-R6-08-02 | 予測・計画・目標未達の扱い | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/II_GW/II-05_Advanced_EMS.md#oq-r6-08-02) |
| ITR-SPKGW-QUESTION-000021 / 1 | OQ-R6-08-03 | DER/負荷の個別操作と快適性条件 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/II_GW/II-04_DER_Load_Control.md#oq-r6-08-03) |
| ITR-SPKGW-QUESTION-000022 / 1 | OQ-R6-09-01 | 実項目・型・単位・品質・計測点 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/II_GW/II-07_Measurement_Data.md#oq-r6-09-01) |
| ITR-SPKGW-QUESTION-000023 / 1 | OQ-R6-09-02 | 保存容量・集計・電断時完全性 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/IV_Quality/IV-08_Data_Log_UI_Quality.md#oq-r6-09-02) |
| ITR-SPKGW-QUESTION-000024 / 1 | OQ-R6-09-03 | 上位同期・履歴エクスポート・削除 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/II_GW/II-07_Measurement_Data.md#oq-r6-09-03) |
| ITR-SPKGW-QUESTION-000025 / 1 | OQ-R6-10-01 | エリア・契約・スケジュール仕様の版 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/V_Lifecycle/V-04_Compliance.md#oq-r6-10-01) |
| ITR-SPKGW-QUESTION-000026 / 1 | OQ-R6-10-02 | 通常API非迂回・保護・復帰の確認 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/I_System/I-07_Responsibilities_Constraints.md#oq-r6-10-02) |
| ITR-SPKGW-QUESTION-000027 / 1 | OQ-R6-11-01 | 基準点・容量・変換グループの対応 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/I_System/I-07_Responsibilities_Constraints.md#oq-r6-11-01) |
| ITR-SPKGW-QUESTION-000028 / 1 | OQ-R6-11-02 | 混在設備・過渡・実出力の合否 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/I_System/I-07_Responsibilities_Constraints.md#oq-r6-11-02) |
| ITR-SPKGW-QUESTION-000029 / 1 | OQ-R6-12-01 | 起動完了・未登録・縮退・停止 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/II_GW/II-09_Settings_Lifecycle.md#oq-r6-12-01) |
| ITR-SPKGW-QUESTION-000030 / 1 | OQ-R6-12-02 | 設定キー・型・範囲・既定値・権限 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/II_GW/II-09_Settings_Lifecycle.md#oq-r6-12-02) |
| ITR-SPKGW-QUESTION-000031 / 1 | OQ-R6-12-03 | 同時変更・部分反映・緊急変更 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/II_GW/II-09_Settings_Lifecycle.md#oq-r6-12-03) |
| ITR-SPKGW-QUESTION-000032 / 1 | OQ-R6-12-04 | バックアップ・工場初期化・移行 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/II_GW/II-09_Settings_Lifecycle.md#oq-r6-12-04) |
| ITR-SPKGW-QUESTION-000033 / 1 | OQ-R6-13-01 | 検出閾値・重大度・復帰・再発 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/II_GW/II-10_Fault_Alarm_Diagnostics.md#oq-r6-13-01) |
| ITR-SPKGW-QUESTION-000034 / 1 | OQ-R6-13-02 | 更新中断・起動不能・実機残留要求 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/II_GW/II-11_Firmware_Update.md#oq-r6-13-02) |
| ITR-SPKGW-QUESTION-000035 / 1 | OQ-R6-14-01 | 機能別の時間・精度・容量プロファイル | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/IV_Quality/IV-01_Performance_Capacity.md#oq-r6-14-01) |
| ITR-SPKGW-QUESTION-000036 / 1 | OQ-R6-14-02 | 同時最大負荷・上限・飽和動作 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/IV_Quality/IV-01_Performance_Capacity.md#oq-r6-14-02) |
| ITR-SPKGW-QUESTION-000037 / 1 | OQ-R6-15-01 | G側実装と共有資源の依存表 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/II_GW/II-01_GW_Architecture.md#oq-r6-15-01) |
| ITR-SPKGW-QUESTION-000038 / 1 | OQ-R6-15-02 | 非干渉評価の範囲と根拠文書 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/IV_Quality/IV-07_Isolation_Shared_Resources.md#oq-r6-15-02) |
| ITR-SPKGW-QUESTION-000039 / 1 | OQ-R6-16-01 | 文書版・条項・要求・証拠の対応 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/V_Lifecycle/V-04_Compliance.md#oq-r6-16-01) |
| ITR-SPKGW-QUESTION-000040 / 1 | OQ-R6-16-02 | 変更手続きと社内リリース判定 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/V_Lifecycle/V-05_Change_Migration_Release.md#oq-r6-16-02) |
| ITR-SPKGW-QUESTION-000041 / 1 | OQ-R6-17-01 | 全要求の検証方法と受入プロファイル | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/V_Lifecycle/V-06_Verification_Validation.md#oq-r6-17-01) |
| ITR-SPKGW-QUESTION-000042 / 1 | OQ-R6-17-02 | 利用者目的に対するValidation | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/V_Lifecycle/V-06_Verification_Validation.md#oq-r6-17-02) |
| ITR-SPKGW-QUESTION-000043 / 1 | OQ-R6-17-03 | 補完項目の評価配賦と適用除外 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/V_Lifecycle/V-06_Verification_Validation.md#oq-r6-17-03) |
| ITR-SPKGW-QUESTION-000044 / 1 | OQ-R6-18-01 | As-Is確認と新旧製品への機能配賦 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/V_Lifecycle/V-05_Change_Migration_Release.md#oq-r6-18-01) |
| ITR-SPKGW-QUESTION-000045 / 1 | OQ-R6-18-02 | 版互換・設定移行・旧経路停止 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/V_Lifecycle/V-05_Change_Migration_Release.md#oq-r6-18-02) |
| ITR-SPKGW-QUESTION-000046 / 1 | OQ-R6-19-01 | 上位USDMと双方向トレーサビリティ | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/V_Lifecycle/V-07_Trace_Open_Questions.md#oq-r6-19-01) |
| ITR-SPKGW-QUESTION-000047 / 1 | OQ-R6-19-02 | OQの責任者・期限・決定ゲート | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/V_Lifecycle/V-07_Trace_Open_Questions.md#oq-r6-19-02) |
| ITR-SPKGW-QUESTION-000048 / 1 | OQ-R6-19-03 | 現行仕様と履歴の意味的整合 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/V_Lifecycle/V-05_Change_Migration_Release.md#oq-r6-19-03) |
| ITR-SPKGW-QUESTION-000049 / 1 | OQ-R6-20-01 | 上位プロトコルとGW内部機能の公開一覧 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/III_Interfaces/III-02_Cloud_GW.md#oq-r6-20-01) |
| ITR-SPKGW-QUESTION-000050 / 1 | OQ-R6-20-02 | 画面・表示項目・対応端末・操作確認 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/IV_Quality/IV-08_Data_Log_UI_Quality.md#oq-r6-20-02) |
| ITR-SPKGW-QUESTION-000051 / 1 | OQ-R6-20-03 | 警報・通知・確認・抑止・解除 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/II_GW/II-10_Fault_Alarm_Diagnostics.md#oq-r6-20-03) |
| ITR-SPKGW-QUESTION-000052 / 1 | OQ-R6-20-04 | FW対象・配信・適用・互換・復旧 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/II_GW/II-11_Firmware_Update.md#oq-r6-20-04) |
| ITR-SPKGW-QUESTION-000053 / 1 | OQ-R6-20-05 | オフライン・通知・認可失効の契約 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/III_Interfaces/III-02_Cloud_GW.md#oq-r6-20-05) |
| ITR-SPKGW-QUESTION-000054 / 1 | OQ-R6-21-01 | 機種別取得主体・公開状態・実経路 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/I_System/I-05_Configurations.md#oq-r6-21-01) |
| ITR-SPKGW-QUESTION-000055 / 1 | OQ-R6-21-02 | 施工・保守の構成変更と故障時復旧 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/V_Lifecycle/V-02_Commissioning_Handover.md#oq-r6-21-02) |
| ITR-SPKGW-QUESTION-000056 / 1 | OQ-R6-22-01 | 電源入力・定格・許容変動 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/IV_Quality/IV-05_Physical_Electrical.md#oq-r6-22-01) |
| ITR-SPKGW-QUESTION-000057 / 1 | OQ-R6-22-02 | 投入・瞬断・電圧低下・復電・停止 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/IV_Quality/IV-05_Physical_Electrical.md#oq-r6-22-02) |
| ITR-SPKGW-QUESTION-000058 / 1 | OQ-R6-22-03 | 端子・コネクタ・ケーブル・USB | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/IV_Quality/IV-05_Physical_Electrical.md#oq-r6-22-03) |
| ITR-SPKGW-QUESTION-000059 / 1 | OQ-R6-22-04 | 外形・取付・放熱・保守空間 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/IV_Quality/IV-05_Physical_Electrical.md#oq-r6-22-04) |
| ITR-SPKGW-QUESTION-000060 / 1 | OQ-R6-22-05 | 表示器・LED・ボタン・ラベル | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/IV_Quality/IV-05_Physical_Electrical.md#oq-r6-22-05) |
| ITR-SPKGW-QUESTION-000061 / 1 | OQ-R6-23-01 | 温湿度・結露・標高・汚損等の適用 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/IV_Quality/IV-06_Environment_EMC.md#oq-r6-23-01) |
| ITR-SPKGW-QUESTION-000062 / 1 | OQ-R6-23-02 | 屋外・防塵防水・日射・腐食・放熱 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/IV_Quality/IV-06_Environment_EMC.md#oq-r6-23-02) |
| ITR-SPKGW-QUESTION-000063 / 1 | OQ-R6-23-03 | EMC・ESD・サージ等の評価対象 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/IV_Quality/IV-06_Environment_EMC.md#oq-r6-23-03) |
| ITR-SPKGW-QUESTION-000064 / 1 | OQ-R6-23-04 | 振動・衝撃・保管・輸送後受入 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/IV_Quality/IV-06_Environment_EMC.md#oq-r6-23-04) |
| ITR-SPKGW-QUESTION-000065 / 1 | OQ-R6-24-01 | GW・PCS・負荷・利用者の危険源一覧 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/IV_Quality/IV-04_Product_Safety.md#oq-r6-24-01) |
| ITR-SPKGW-QUESTION-000066 / 1 | OQ-R6-24-02 | 故障・誤操作・通信断時の安全状態 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/IV_Quality/IV-04_Product_Safety.md#oq-r6-24-02) |
| ITR-SPKGW-QUESTION-000067 / 1 | OQ-R6-24-03 | 遠隔操作・登録・変更の誤り防止 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/IV_Quality/IV-04_Product_Safety.md#oq-r6-24-03) |
| ITR-SPKGW-QUESTION-000068 / 1 | OQ-R6-24-04 | 安全検証・注意表示・残留リスク承認 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/IV_Quality/IV-04_Product_Safety.md#oq-r6-24-04) |
| ITR-SPKGW-QUESTION-000069 / 1 | OQ-R6-25-01 | 可用性・許容停止・復旧・データ損失 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/IV_Quality/IV-02_Reliability_Availability.md#oq-r6-25-01) |
| ITR-SPKGW-QUESTION-000070 / 1 | OQ-R6-25-02 | 連続稼働・劣化・資源枯渇 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/IV_Quality/IV-02_Reliability_Availability.md#oq-r6-25-02) |
| ITR-SPKGW-QUESTION-000071 / 1 | OQ-R6-25-03 | 故障切分けと許可保守 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/IV_Quality/IV-02_Reliability_Availability.md#oq-r6-25-03) |
| ITR-SPKGW-QUESTION-000072 / 1 | OQ-R6-25-04 | 使用寿命・書込み寿命・消耗部品 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/IV_Quality/IV-02_Reliability_Availability.md#oq-r6-25-04) |
| ITR-SPKGW-QUESTION-000073 / 1 | OQ-R6-26-01 | 個体識別・鍵投入・製造モード | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/V_Lifecycle/V-01_Manufacturing_Shipping.md#oq-r6-26-01) |
| ITR-SPKGW-QUESTION-000074 / 1 | OQ-R6-26-02 | 出荷状態・検査・校正・梱包 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/V_Lifecycle/V-01_Manufacturing_Shipping.md#oq-r6-26-02) |
| ITR-SPKGW-QUESTION-000075 / 1 | OQ-R6-26-03 | ネットワーク・機器・計測点の初期設定 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/V_Lifecycle/V-02_Commissioning_Handover.md#oq-r6-26-03) |
| ITR-SPKGW-QUESTION-000076 / 1 | OQ-R6-26-04 | 試運転・利用者引渡し・教育 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/V_Lifecycle/V-02_Commissioning_Handover.md#oq-r6-26-04) |
| ITR-SPKGW-QUESTION-000077 / 1 | OQ-R6-26-05 | 本体/機器交換と所有者変更 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/V_Lifecycle/V-03_Maintenance_Retirement.md#oq-r6-26-05) |
| ITR-SPKGW-QUESTION-000078 / 1 | OQ-R6-26-06 | 秘密・履歴の消去と廃止状態 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/V_Lifecycle/V-03_Maintenance_Retirement.md#oq-r6-26-06) |
| ITR-SPKGW-QUESTION-000079 / 1 | OQ-R6-26-07 | 支援期間・クラウド終了後の機能 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/V_Lifecycle/V-03_Maintenance_Retirement.md#oq-r6-26-07) |
| ITR-SPKGW-QUESTION-000080 / 1 | OQ-R6-27-01 | 脅威分析と要求・検証の対応 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/IV_Quality/IV-03_Security_Privacy.md#oq-r6-27-01) |
| ITR-SPKGW-QUESTION-000081 / 1 | OQ-R6-27-02 | 生成・配布・更新・失効・漏えい復旧 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/IV_Quality/IV-03_Security_Privacy.md#oq-r6-27-02) |
| ITR-SPKGW-QUESTION-000082 / 1 | OQ-R6-27-03 | 通信保護・Webセッション・機器混在 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/IV_Quality/IV-03_Security_Privacy.md#oq-r6-27-03) |
| ITR-SPKGW-QUESTION-000083 / 1 | OQ-R6-27-04 | 保守経路・製造アクセス・更新認証 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/IV_Quality/IV-03_Security_Privacy.md#oq-r6-27-04) |
| ITR-SPKGW-QUESTION-000084 / 1 | OQ-R6-27-05 | SBOM・脆弱性対応と機器の支援機能 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/V_Lifecycle/V-03_Maintenance_Retirement.md#oq-r6-27-05) |
| ITR-SPKGW-QUESTION-000085 / 1 | OQ-R6-27-06 | 個人/住宅データの収集・利用・公開・消去 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/IV_Quality/IV-03_Security_Privacy.md#oq-r6-27-06) |
| ITR-SPKGW-QUESTION-000086 / 1 | OQ-R9-IMP-01 | 原資料の責任・承認版・対象製品 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/V_Lifecycle/V-07_Trace_Open_Questions.md#oq-r9-imp-01) |
| ITR-SPKGW-QUESTION-000087 / 1 | OQ-R9-IMP-02 | 実資料による抽出の対応範囲 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/V_Lifecycle/V-07_Trace_Open_Questions.md#oq-r9-imp-02) |
| ITR-SPKGW-QUESTION-000088 / 1 | OQ-R9-IMP-03 | 適用条件付きマージの実承認者 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/V_Lifecycle/V-05_Change_Migration_Release.md#oq-r9-imp-03) |
| ITR-SPKGW-QUESTION-000089 / 1 | OQ-R9-IMP-04 | 正式USDM形式と意味の確認 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/V_Lifecycle/V-07_Trace_Open_Questions.md#oq-r9-imp-04) |
| ITR-SPKGW-QUESTION-000090 / 1 | OQ-R9-IMP-05 | 実環境の公開・権限制御・障害復旧 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/V_Lifecycle/V-07_Trace_Open_Questions.md#oq-r9-imp-05) |
| ITR-SPKGW-QUESTION-000091 / 1 | OQ-R9-IMP-06 | 取り込みパイロットの受入と規模 | [原文](../../../../10_canonical/releases/BL-R9-0001/chapters/V_Lifecycle/V-06_Verification_Validation.md#oq-r9-imp-06) |
| ITR-SPKGW-REF-000001 / 1 | AISTD1-FRAG-000001 | AIM-01 原文位置 | [原文](../../../../20_work/analysis/project/ai_std_integration/source_fragments.json) |
| ITR-SPKGW-IMPROVE-000001 / 1.3.0 | AIM-01 | 有効な認可・正本・独立性 | [原文](../../../../00_governance/STD_01_Authority_Ownership.md#aim-01) |
| ITR-SPKGW-REF-000002 / 1 | AISTD1-FRAG-000002 | AIM-02 原文位置 | [原文](../../../../20_work/analysis/project/ai_std_integration/source_fragments.json) |
| ITR-SPKGW-IMPROVE-000002 / 1.3.0 | AIM-02 | 作業・並列・引継ぎの最小記録 | [原文](../../../../00_governance/STD_04_Task_WBS.md#aim-02) |
| ITR-SPKGW-REF-000003 / 1 | AISTD1-FRAG-000003 | AIM-03 原文位置 | [原文](../../../../20_work/analysis/project/ai_std_integration/source_fragments.json) |
| ITR-SPKGW-IMPROVE-000003 / 1.3.0 | AIM-03 | 旧タスク状態を現行へ併設しない | [原文](../../../../00_governance/STD_04_Task_WBS.md#aim-03) |
| ITR-SPKGW-REF-000004 / 1 | AISTD1-FRAG-000004 | AIM-04 原文位置 | [原文](../../../../20_work/analysis/project/ai_std_integration/source_fragments.json) |
| ITR-SPKGW-IMPROVE-000004 / 1.3.0 | AIM-04 | 実行証拠・異常系・自己レビュー | [原文](../../../../00_governance/STD_06_Execution_Review_Evidence.md#aim-04) |
| ITR-SPKGW-REF-000005 / 1 | AISTD1-FRAG-000005 | AIM-05 原文位置 | [原文](../../../../20_work/analysis/project/ai_std_integration/source_fragments.json) |
| ITR-SPKGW-IMPROVE-000005 / 1.3.0 | AIM-05 | 結果語彙と周期測定の境界 | [原文](../../../../00_governance/STD_06_Execution_Review_Evidence.md#aim-05) |
| ITR-SPKGW-REF-000006 / 1 | AISTD1-FRAG-000006 | AIM-06 原文位置 | [原文](../../../../20_work/analysis/project/ai_std_integration/source_fragments.json) |
| ITR-SPKGW-IMPROVE-000006 / 1.3.0 | AIM-06 | 同一時点の旧新分母比較と未受入量 | [原文](../../../../00_governance/STD_07_Progress_Schedule.md#aim-06) |
| ITR-SPKGW-REF-000007 / 1 | AISTD1-FRAG-000007 | AIM-07 原文位置 | [原文](../../../../20_work/analysis/project/ai_std_integration/source_fragments.json) |
| ITR-SPKGW-IMPROVE-000007 / 1.3.0 | AIM-07 | 実費・配賦・推定を区別する | [原文](../../../../00_governance/STD_08_Budget_Cost.md#aim-07) |
| ITR-SPKGW-REF-000008 / 1 | AISTD1-FRAG-000008 | AIM-08 原文位置 | [原文](../../../../20_work/analysis/project/ai_std_integration/source_fragments.json) |
| ITR-SPKGW-IMPROVE-000008 / 1.3.0 | AIM-08 | R0／R1／R2は作業影響の補助分類 | [原文](../../../../00_governance/STD_09_Change_Risk.md#aim-08) |
| ITR-SPKGW-REF-000009 / 1 | AISTD1-FRAG-000009 | AIM-09 原文位置 | [原文](../../../../20_work/analysis/project/ai_std_integration/source_fragments.json) |
| ITR-SPKGW-IMPROVE-000009 / 1.3.0 | AIM-09 | 例外・緊急対応を限定する | [原文](../../../../00_governance/STD_09_Change_Risk.md#aim-09) |
| ITR-SPKGW-REF-000010 / 1 | AISTD1-FRAG-000010 | AIM-10 原文位置 | [原文](../../../../20_work/analysis/project/ai_std_integration/source_fragments.json) |
| ITR-SPKGW-IMPROVE-000010 / 1.3.0 | AIM-10 | 指示ファイルは入口であり強制制御ではない | [原文](../../../../00_governance/STD_10_AI_Collaboration.md#aim-10) |
| ITR-SPKGW-REF-000011 / 1 | AISTD1-FRAG-000011 | AIM-11 原文位置 | [原文](../../../../20_work/analysis/project/ai_std_integration/source_fragments.json) |
| ITR-SPKGW-IMPROVE-000011 / 1.3.0 | AIM-11 | ソース・ビルド・配布物・証拠を同一候補へ結ぶ | [原文](../../../../00_governance/STD_11_Release_Baselines.md#aim-11) |
| ITR-SPKGW-REF-000012 / 1 | AISTD1-FRAG-000012 | AIM-12 原文位置 | [原文](../../../../20_work/analysis/project/ai_std_integration/source_fragments.json) |
| ITR-SPKGW-IMPROVE-000012 / 1.3.0 | AIM-12 | 会話の報告と正本更新を区別する | [原文](../../../../00_governance/STD_12_Reports_Decisions.md#aim-12) |
| ITR-SPKGW-REF-000013 / 1 | AISTD1-FRAG-000013 | AIM-13 原文位置 | [原文](../../../../20_work/analysis/project/ai_std_integration/source_fragments.json) |
| ITR-SPKGW-IMPROVE-000013 / 1.3.0 | AIM-13 | 六つの質問と適用範囲 | [原文](../../../../00_governance/STD_14_Requirements_Change_Impact.md#aim-13) |
| ITR-SPKGW-REF-000014 / 1 | AISTD1-FRAG-000014 | AIM-14 原文位置 | [原文](../../../../20_work/analysis/project/ai_std_integration/source_fragments.json) |
| ITR-SPKGW-IMPROVE-000014 / 1.3.0 | AIM-14 | 観測可能な要求と根拠の区別 | [原文](../../../../00_governance/STD_14_Requirements_Change_Impact.md#aim-14) |
| ITR-SPKGW-REF-000015 / 1 | AISTD1-FRAG-000015 | AIM-15 原文位置 | [原文](../../../../20_work/analysis/project/ai_std_integration/source_fragments.json) |
| ITR-SPKGW-IMPROVE-000015 / 1.3.0 | AIM-15 | 実行経路と外部依存まで追う | [原文](../../../../00_governance/STD_14_Requirements_Change_Impact.md#aim-15) |
| ITR-SPKGW-REF-000016 / 1 | AISTD1-FRAG-000016 | AIM-16 原文位置 | [原文](../../../../20_work/analysis/project/ai_std_integration/source_fragments.json) |
| ITR-SPKGW-IMPROVE-000016 / 1.3.0 | AIM-16 | 七つの確認と論理・実配置の分離 | [原文](../../../../00_governance/STD_15_Design_Decisions.md#aim-16) |
| ITR-SPKGW-REF-000017 / 1 | AISTD1-FRAG-000017 | AIM-17 原文位置 | [原文](../../../../20_work/analysis/project/ai_std_integration/source_fragments.json) |
| ITR-SPKGW-IMPROVE-000017 / 1.3.0 | AIM-17 | 状態所有・競合・非同期結果の設計 | [原文](../../../../00_governance/STD_15_Design_Decisions.md#aim-17) |
| ITR-SPKGW-REF-000018 / 1 | AISTD1-FRAG-000018 | AIM-18 原文位置 | [原文](../../../../20_work/analysis/project/ai_std_integration/source_fragments.json) |
| ITR-SPKGW-IMPROVE-000018 / 1.3.0 | AIM-18 | 選択理由・反証・引渡し条件 | [原文](../../../../00_governance/STD_15_Design_Decisions.md#aim-18) |
| ITR-SPKGW-REF-000019 / 1 | AISTD1-FRAG-000019 | AIM-19 原文位置 | [原文](../../../../20_work/analysis/project/ai_std_integration/source_fragments.json) |
| ITR-SPKGW-IMPROVE-000019 / 1.3.0 | AIM-19 | 最小で再現可能な差分を作る | [原文](../../../../00_governance/STD_16_Implementation_C_Yocto.md#aim-19) |
| ITR-SPKGW-REF-000020 / 1 | AISTD1-FRAG-000020 | AIM-20 原文位置 | [原文](../../../../20_work/analysis/project/ai_std_integration/source_fragments.json) |
| ITR-SPKGW-IMPROVE-000020 / 1.3.0 | AIM-20 | メモリ・数値・並行・資源・状態 | [原文](../../../../00_governance/STD_16_Implementation_C_Yocto.md#aim-20) |
| ITR-SPKGW-REF-000021 / 1 | AISTD1-FRAG-000021 | AIM-21 原文位置 | [原文](../../../../20_work/analysis/project/ai_std_integration/source_fragments.json) |
| ITR-SPKGW-IMPROVE-000021 / 1.3.0 | AIM-21 | ビルド対象・構成差・回帰の引渡し | [原文](../../../../00_governance/STD_16_Implementation_C_Yocto.md#aim-21) |
| ITR-SPKGW-REF-000022 / 1 | AISTD1-FRAG-000022 | AIM-22 原文位置 | [原文](../../../../20_work/analysis/project/ai_std_integration/source_fragments.json) |
| ITR-SPKGW-IMPROVE-000022 / 1.3.0 | AIM-22 | 必要最小限の入力と脅威確認 | [原文](../../../../00_governance/STD_17_Security_Supplier.md#aim-22) |
| ITR-SPKGW-REF-000023 / 1 | AISTD1-FRAG-000023 | AIM-23 原文位置 | [原文](../../../../20_work/analysis/project/ai_std_integration/source_fragments.json) |
| ITR-SPKGW-IMPROVE-000023 / 1.3.0 | AIM-23 | 脆弱性対応と部品情報 | [原文](../../../../00_governance/STD_17_Security_Supplier.md#aim-23) |
| ITR-SPKGW-REF-000024 / 1 | AISTD1-FRAG-000024 | AIM-24 原文位置 | [原文](../../../../20_work/analysis/project/ai_std_integration/source_fragments.json) |
| ITR-SPKGW-IMPROVE-000024 / 1.3.0 | AIM-24 | ブラックボックスを推測で補わない | [原文](../../../../00_governance/STD_17_Security_Supplier.md#aim-24) |
| ITR-SPKGW-REF-000025 / 1 | AISTD1-FRAG-000025 | AIM-25 原文位置 | [原文](../../../../20_work/analysis/project/ai_std_integration/source_fragments.json) |
| ITR-SPKGW-IMPROVE-000025 / 1.3.0 | AIM-25 | 分母・時点・欠測・比較条件 | [原文](../../../../00_governance/STD_18_AI_Measurement_Improvement.md#aim-25) |
| ITR-SPKGW-REF-000026 / 1 | AISTD1-FRAG-000026 | AIM-26 原文位置 | [原文](../../../../20_work/analysis/project/ai_std_integration/source_fragments.json) |
| ITR-SPKGW-IMPROVE-000026 / 1.3.0 | AIM-26 | 軽量な協働記録と将来接続 | [原文](../../../../00_governance/STD_18_AI_Measurement_Improvement.md#aim-26) |
| ITR-SPKGW-QUESTION-000092 / 1 | OQ-GOV-AISTD-01 | AI入口ファイルの適用環境 | [原文](../../../../00_governance/Open_Questions.md#oq-gov-aistd-01) |
| ITR-SPKGW-QUESTION-000093 / 1 | OQ-GOV-AISTD-02 | 委託・脆弱性対応の契約値 | [原文](../../../../00_governance/Open_Questions.md#oq-gov-aistd-02) |
| ITR-SPKGW-QUESTION-000094 / 1 | OQ-GOV-AISTD-03 | 測定・WIP・観測費用の運用値 | [原文](../../../../00_governance/Open_Questions.md#oq-gov-aistd-03) |
