# 旧27章から5部44章への再編対応

旧章を丸ごと複製せず、節／補完項単位で現行所属を1つにする。元本文はsources/r7_snapshotに保存。章番号を含む旧OQ／SLOT IDは識別子として保持し、現在の章番号とは一致させない。

<a id="old-ch-01"></a>
## 旧01章 — 01_Scope_Baseline

元資料：[R7原本（履歴）](../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/01_Scope_Baseline.md)

| 元の節／項 | 現行の章・節 | 取扱い |
|---|---|---|
| 1.1 本書の位置付け | [I-01.1 文書目的・適用範囲・システム境界](../chapters/I_System/I-01_Purpose_Scope.md#legacy-1-1) | 当時の文書管理記述をR8に置換。原文は履歴保持 |
| 1.2 入力と優先関係 | [I-01.2 文書目的・適用範囲・システム境界](../chapters/I_System/I-01_Purpose_Scope.md#legacy-1-2) | 当時の文書管理記述をR8に置換。原文は履歴保持 |
| 1.3 更新の中心 | [I-01.3 文書目的・適用範囲・システム境界](../chapters/I_System/I-01_Purpose_Scope.md#legacy-1-3) | 当時の文書管理記述をR8に置換。原文は履歴保持 |
| 1.4 対象システムと製品境界 | [I-01.4 文書目的・適用範囲・システム境界](../chapters/I_System/I-01_Purpose_Scope.md#legacy-1-4) | 本文・補完項を移行。見出し・参照のみ再編 |
| 1.5 状態・トレーサビリティ | [I-01.5 文書目的・適用範囲・システム境界](../chapters/I_System/I-01_Purpose_Scope.md#legacy-1-5) | 当時の文書管理記述をR8に置換。原文は履歴保持 |
| 1.6 周辺文書との関係 | [I-01.6 文書目的・適用範囲・システム境界](../chapters/I_System/I-01_Purpose_Scope.md#legacy-1-6) | 本文・補完項を移行。見出し・参照のみ再編 |
| 1.7 R2のシステム境界拡張 | [I-01.7 文書目的・適用範囲・システム境界](../chapters/I_System/I-01_Purpose_Scope.md#legacy-1-7) | 当時の文書管理記述をR8に置換。原文は履歴保持 |
| 1.8 R3の優先関係と変更記録 | [I-01.8 文書目的・適用範囲・システム境界](../chapters/I_System/I-01_Purpose_Scope.md#legacy-1-8) | 当時の文書管理記述をR8に置換。原文は履歴保持 |
| 1.9.1 利用者・施工者・運用者・保守者の役割 | [I-02.1 システム利用者・運用概念・利用機能](../chapters/I_System/I-02_Actors_Roles.md#legacy-1-9-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 1.9.2 製品価値と対象外の判定 | [I-01.9 文書目的・適用範囲・システム境界](../chapters/I_System/I-01_Purpose_Scope.md#legacy-1-9-2) | 本文・補完項を移行。見出し・参照のみ再編 |
| 1.10.1 用語・略語・数値表記 | [I-01.10 文書目的・適用範囲・システム境界](../chapters/I_System/I-01_Purpose_Scope.md#legacy-1-10-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 1.10.2 規範別冊の版と仕様完成条件 | [I-01.11 文書目的・適用範囲・システム境界](../chapters/I_System/I-01_Purpose_Scope.md#legacy-1-10-2) | 本文・補完項を移行。見出し・参照のみ再編 |
<a id="old-ch-02"></a>
## 旧02章 — 02_System_Context

元資料：[R7原本（履歴）](../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/02_System_Context.md)

| 元の節／項 | 現行の章・節 | 取扱い |
|---|---|---|
| 2.1 システムコンテキスト：共通宅内ルータを明示 | [I-04.1 システムコンテキスト・ネットワーク接続](../chapters/I_System/I-04_System_Context.md#legacy-2-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 2.2 経路・役割・現在の対応範囲 | [I-04.2 システムコンテキスト・ネットワーク接続](../chapters/I_System/I-04_System_Context.md#legacy-2-2) | 本文・補完項を移行。見出し・参照のみ再編 |
| 2.3 GW内の用途別経路 | [II-01.1 GW論理構成・H/G責務・状態所有者](../chapters/II_GW/II-01_GW_Architecture.md#legacy-2-3) | 本文・補完項を移行。見出し・参照のみ再編 |
| 2.4 独立する制御責務 | [I-07.1 全体責務配分・電力制約・保護](../chapters/I_System/I-07_Responsibilities_Constraints.md#legacy-2-4) | 本文・補完項を移行。見出し・参照のみ再編 |
| 2.5 RS-485経路の確定点と残る設計 | [II-01.2 GW論理構成・H/G責務・状態所有者](../chapters/II_GW/II-01_GW_Architecture.md#legacy-2-5) | 本文・補完項を移行。見出し・参照のみ再編 |
| 2.6 IF・識別子・互換性 | [III-01.1 IF一覧・共通契約・H/G内部境界](../chapters/III_Interfaces/III-01_Boundary_Contracts.md#legacy-2-6) | 本文・補完項を移行。見出し・参照のみ再編 |
| 2.7 ルータ共有の障害範囲 | [I-04.3 システムコンテキスト・ネットワーク接続](../chapters/I_System/I-04_System_Context.md#legacy-2-7) | 本文・補完項を移行。見出し・参照のみ再編 |
| 2.8.1 実ネットワークと接続先の実体 | [I-04.4 システムコンテキスト・ネットワーク接続](../chapters/I_System/I-04_System_Context.md#legacy-2-8-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 2.8.2 宅内直接Webとルータ接続の成立条件 | [I-04.5 システムコンテキスト・ネットワーク接続](../chapters/I_System/I-04_System_Context.md#legacy-2-8-2) | 本文・補完項を移行。見出し・参照のみ再編 |
<a id="old-ch-03"></a>
## 旧03章 — 03_Responsibilities

元資料：[R7原本（履歴）](../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/03_Responsibilities.md)

| 元の節／項 | 現行の章・節 | 取扱い |
|---|---|---|
| 3.1 責務契約 | [II-01.3 GW論理構成・H/G責務・状態所有者](../chapters/II_GW/II-01_GW_Architecture.md#legacy-3-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 3.2 状態の正本 | [II-01.4 GW論理構成・H/G責務・状態所有者](../chapters/II_GW/II-01_GW_Architecture.md#legacy-3-2) | 本文・補完項を移行。見出し・参照のみ再編 |
| 3.3 一意性と分散配置 | [II-01.5 GW論理構成・H/G責務・状態所有者](../chapters/II_GW/II-01_GW_Architecture.md#legacy-3-3) | 本文・補完項を移行。見出し・参照のみ再編 |
| 3.4 Blackboard・既存構造 | [II-01.6 GW論理構成・H/G責務・状態所有者](../chapters/II_GW/II-01_GW_Architecture.md#legacy-3-4) | 本文・補完項を移行。見出し・参照のみ再編 |
| 3.5 設定調停との区別 | [II-01.7 GW論理構成・H/G責務・状態所有者](../chapters/II_GW/II-01_GW_Architecture.md#legacy-3-5) | 本文・補完項を移行。見出し・参照のみ再編 |
| 3.6 R2追加：北向き管理の論理責務と状態正本 | [II-01.8 GW論理構成・H/G責務・状態所有者](../chapters/II_GW/II-01_GW_Architecture.md#legacy-3-6) | 本文・補完項を移行。見出し・参照のみ再編 |
| 3.7 R3導入・R4適用：出力制御所有者の選択 | [II-01.9 GW論理構成・H/G責務・状態所有者](../chapters/II_GW/II-01_GW_Architecture.md#legacy-3-7) | 本文・補完項を移行。見出し・参照のみ再編 |
| 3.8 R4：宅内ルータの責務と取得所有者 | [I-04.6 システムコンテキスト・ネットワーク接続](../chapters/I_System/I-04_System_Context.md#legacy-3-8) | 本文・補完項を移行。見出し・参照のみ再編 |
| 3.9 R5：通常EL通信の共通窓口と意味的担当 | [II-01.10 GW論理構成・H/G責務・状態所有者](../chapters/II_GW/II-01_GW_Architecture.md#legacy-3-9) | 本文・補完項を移行。見出し・参照のみ再編 |
| 3.10.1 実装配賦・状態所有者一覧 | [II-01.11 GW論理構成・H/G責務・状態所有者](../chapters/II_GW/II-01_GW_Architecture.md#legacy-3-10-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 3.10.2 H内・H/G境界契約の具体項目 | [III-01.2 IF一覧・共通契約・H/G内部境界](../chapters/III_Interfaces/III-01_Boundary_Contracts.md#legacy-3-10-2) | 本文・補完項を移行。見出し・参照のみ再編 |
<a id="old-ch-04"></a>
## 旧04章 — 04_Configurations_Profiles

元資料：[R7原本（履歴）](../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/04_Configurations_Profiles.md)

| 元の節／項 | 現行の章・節 | 取扱い |
|---|---|---|
| 4.1 分類軸を分離する | [I-05.1 機器構成パターン・機能適用条件](../chapters/I_System/I-05_Configurations.md#legacy-4-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 4.2 機器群と責務 | [I-05.2 機器構成パターン・機能適用条件](../chapters/I_System/I-05_Configurations.md#legacy-4-2) | 本文・補完項を移行。見出し・参照のみ再編 |
| 4.3 識別と共有資源 | [I-05.3 機器構成パターン・機能適用条件](../chapters/I_System/I-05_Configurations.md#legacy-4-3) | 本文・補完項を移行。見出し・参照のみ再編 |
| 4.4 接続プロファイルの最小内容 | [I-05.4 機器構成パターン・機能適用条件](../chapters/I_System/I-05_Configurations.md#legacy-4-4) | 本文・補完項を移行。見出し・参照のみ再編 |
| 4.5 RS-485経路の分類：本書の具体化案 | [III-07.1 RS-485 PCSインターフェース](../chapters/III_Interfaces/III-07_RS485_PCS.md#legacy-4-5) | 本文・補完項を移行。見出し・参照のみ再編 |
| 4.6 適用判定と不足情報 | [I-05.5 機器構成パターン・機能適用条件](../chapters/I_System/I-05_Configurations.md#legacy-4-6) | 本文・補完項を移行。見出し・参照のみ再編 |
| 4.7 R2追加：接続・サービス適用プロファイル | [I-05.6 機器構成パターン・機能適用条件](../chapters/I_System/I-05_Configurations.md#legacy-4-7) | 本文・補完項を移行。見出し・参照のみ再編 |
| 4.8 R3導入・R4適用：出力制御接続プロファイル | [I-05.7 機器構成パターン・機能適用条件](../chapters/I_System/I-05_Configurations.md#legacy-4-8) | 本文・補完項を移行。見出し・参照のみ再編 |
| 4.9 R4：物理機器と多重IFの分類 | [I-05.8 機器構成パターン・機能適用条件](../chapters/I_System/I-05_Configurations.md#legacy-4-9) | 本文・補完項を移行。見出し・参照のみ再編 |
| 4.10.1 既存・追加・変更・廃止機能の母集団 | [II-02.1 SPK-GW製品の機能（要件）一覧](../chapters/II_GW/II-02_GW_Functions.md#legacy-4-10-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 4.10.2 機器・ソフトウェア・接続の対応組合せ | [I-05.9 機器構成パターン・機能適用条件](../chapters/I_System/I-05_Configurations.md#legacy-4-10-2) | 本文・補完項を移行。見出し・参照のみ再編 |
| 4.11.1 探索・登録・解除・交換・同一性 | [II-06.1 機器探索・登録・識別・Capability管理](../chapters/II_GW/II-06_Device_Management.md#legacy-4-11-1) | 本文・補完項を移行。見出し・参照のみ再編 |
<a id="old-ch-05"></a>
## 旧05章 — 05_Control_Contracts

元資料：[R7原本（履歴）](../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/05_Control_Contracts.md)

| 元の節／項 | 現行の章・節 | 取扱い |
|---|---|---|
| 5.1 意味論を固定する | [II-03.1 要求受付・通常制御権・実行調整](../chapters/II_GW/II-03_Control_Execution.md#legacy-5-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 5.2 操作の区別 | [II-03.2 要求受付・通常制御権・実行調整](../chapters/II_GW/II-03_Control_Execution.md#legacy-5-2) | 本文・補完項を移行。見出し・参照のみ再編 |
| 5.3 権威・期限と送信境界 | [II-03.3 要求受付・通常制御権・実行調整](../chapters/II_GW/II-03_Control_Execution.md#legacy-5-3) | 本文・補完項を移行。見出し・参照のみ再編 |
| 5.4 実行状態 | [II-03.4 要求受付・通常制御権・実行調整](../chapters/II_GW/II-03_Control_Execution.md#legacy-5-4) | 本文・補完項を移行。見出し・参照のみ再編 |
| 5.5 要求と観測の対応：追加の具体化案 | [II-03.5 要求受付・通常制御権・実行調整](../chapters/II_GW/II-03_Control_Execution.md#legacy-5-5) | 本文・補完項を移行。見出し・参照のみ再編 |
| 5.9 R2追加：上位公開Envelopeと経路区分 | [III-01.3 IF一覧・共通契約・H/G内部境界](../chapters/III_Interfaces/III-01_Boundary_Contracts.md#legacy-5-9) | 本文・補完項を移行。見出し・参照のみ再編 |
| 5.10 R3導入・R4適用：通常権威と系統構成世代の分離 | [III-01.4 IF一覧・共通契約・H/G内部境界](../chapters/III_Interfaces/III-01_Boundary_Contracts.md#legacy-5-10) | 本文・補完項を移行。見出し・参照のみ再編 |
| 5.11.1 優先関係・同順位・取消し・並行実行 | [II-03.6 要求受付・通常制御権・実行調整](../chapters/II_GW/II-03_Control_Execution.md#legacy-5-11-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 5.11.2 結果・確認窓・不明状態の終端 | [II-03.7 要求受付・通常制御権・実行調整](../chapters/II_GW/II-03_Control_Execution.md#legacy-5-11-2) | 本文・補完項を移行。見出し・参照のみ再編 |
<a id="old-ch-06"></a>
## 旧06章 — 06_Usecases

元資料：[R7原本（履歴）](../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/06_Usecases.md)

| 元の節／項 | 現行の章・節 | 取扱い |
|---|---|---|
| 6.1 原典UCの継承 | [I-06.1 システムユースケース・横断振る舞い](../chapters/I_System/I-06_Usecases.md#legacy-6-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 6.2 UC-04：通常操作と出力制御の同時実行 | [I-06.2 システムユースケース・横断振る舞い](../chapters/I_System/I-06_Usecases.md#legacy-6-2) | 本文・補完項を移行。見出し・参照のみ再編 |
| 6.3 本書で追加したUC：USER_CONTEXT_DERIVED／SYSTEM_SPEC_PROPOSAL | [I-06.3 システムユースケース・横断振る舞い](../chapters/I_System/I-06_Usecases.md#legacy-6-3) | 本文・補完項を移行。見出し・参照のみ再編 |
| 6.4 部分失敗と補償 | [II-03.8 要求受付・通常制御権・実行調整](../chapters/II_GW/II-03_Control_Execution.md#legacy-6-4) | 本文・補完項を移行。見出し・参照のみ再編 |
| 6.5 ユースケース記述の完成条件 | [I-06.4 システムユースケース・横断振る舞い](../chapters/I_System/I-06_Usecases.md#legacy-6-5) | 本文・補完項を移行。見出し・参照のみ再編 |
| 6.6 R2追加：上位サービス・UIのユースケース | [I-06.5 システムユースケース・横断振る舞い](../chapters/I_System/I-06_Usecases.md#legacy-6-6) | 本文・補完項を移行。見出し・参照のみ再編 |
| 6.9 R3追加ユースケースの所在 | [I-06.6 システムユースケース・横断振る舞い](../chapters/I_System/I-06_Usecases.md#legacy-6-9) | 本文・補完項を移行。見出し・参照のみ再編 |
| 6.10 R4：ルータを含む取得の往復 | [I-06.7 システムユースケース・横断振る舞い](../chapters/I_System/I-06_Usecases.md#legacy-6-10) | 本文・補完項を移行。見出し・参照のみ再編 |
| 6.11.1 機能とUCの双方向対応 | [I-06.8 システムユースケース・横断振る舞い](../chapters/I_System/I-06_Usecases.md#legacy-6-11-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 6.11.2 横断条件・同時事象・利用場面 | [I-06.9 システムユースケース・横断振る舞い](../chapters/I_System/I-06_Usecases.md#legacy-6-11-2) | 本文・補完項を移行。見出し・参照のみ再編 |
<a id="old-ch-07"></a>
## 旧07章 — 07_DER_Connections

元資料：[R7原本（履歴）](../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/07_DER_Connections.md)

| 元の節／項 | 現行の章・節 | 取扱い |
|---|---|---|
| 7.1 共通実行契約 | [II-04.1 DER制御・負荷制御・結果確認](../chapters/II_GW/II-04_DER_Load_Control.md#legacy-7-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 7.2 RS-485接続PCS：既存機能からの具体化 | [III-07.2 RS-485 PCSインターフェース](../chapters/III_Interfaces/III-07_RS485_PCS.md#legacy-7-2) | 本文・補完項を移行。見出し・参照のみ再編 |
| 7.3 ECHONET Lite接続：他社機器のController側 | [III-06.1 ECHONET Lite Controller／Deviceインターフェース](../chapters/III_Interfaces/III-06_ECHONET_Lite.md#legacy-7-3) | 本文・補完項を移行。見出し・参照のみ再編 |
| 7.4 外部HEMSに対するGWのDevice側：持越し要求 | [III-06.2 ECHONET Lite Controller／Deviceインターフェース](../chapters/III_Interfaces/III-06_ECHONET_Lite.md#legacy-7-4) | 本文・補完項を移行。見出し・参照のみ再編 |
| 7.5 経路切替・透過性の限界 | [II-04.2 DER制御・負荷制御・結果確認](../chapters/II_GW/II-04_DER_Load_Control.md#legacy-7-5) | 本文・補完項を移行。見出し・参照のみ再編 |
| 7.9 R3導入・R4適用：通常機器接続と系統制御接続の別契約 | [III-06.3 ECHONET Lite Controller／Deviceインターフェース](../chapters/III_Interfaces/III-06_ECHONET_Lite.md#legacy-7-9) | 本文・補完項を移行。見出し・参照のみ再編 |
| 7.10 R4：ELサーバ取得と通常操作は別契約 | [III-06.4 ECHONET Lite Controller／Deviceインターフェース](../chapters/III_Interfaces/III-06_ECHONET_Lite.md#legacy-7-10) | 本文・補完項を移行。見出し・参照のみ再編 |
| 7.11 R5：Controller側の接続を全対象へ明示 | [III-06.5 ECHONET Lite Controller／Deviceインターフェース](../chapters/III_Interfaces/III-06_ECHONET_Lite.md#legacy-7-11) | 本文・補完項を移行。見出し・参照のみ再編 |
| 7.12.1 RS-485電文・接続条件・送信所有権 | [III-07.3 RS-485 PCSインターフェース](../chapters/III_Interfaces/III-07_RS485_PCS.md#legacy-7-12-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 7.12.2 ECHONET Lite Controller/Deviceの対象能力 | [III-06.6 ECHONET Lite Controller／Deviceインターフェース](../chapters/III_Interfaces/III-06_ECHONET_Lite.md#legacy-7-12-2) | 本文・補完項を移行。見出し・参照のみ再編 |
| 7.12.3 IPv4/IPv6・Wi-SUN・USB等の持越し要求 | [III-09.1 ネットワーク・無線・USB等の接続プロファイル](../chapters/III_Interfaces/III-09_Network_Peripherals.md#legacy-7-12-3) | 本文・補完項を移行。見出し・参照のみ再編 |
<a id="old-ch-08"></a>
## 旧08章 — 08_Advanced_EMS_Loads

元資料：[R7原本（履歴）](../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/08_Advanced_EMS_Loads.md)

| 元の節／項 | 現行の章・節 | 取扱い |
|---|---|---|
| 8.1 高度エネマネの範囲 | [II-05.1 高度エネルギーマネジメント](../chapters/II_GW/II-05_Advanced_EMS.md#legacy-8-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 8.2 機能分類→機能→振る舞い | [II-05.2 高度エネルギーマネジメント](../chapters/II_GW/II-05_Advanced_EMS.md#legacy-8-2) | 本文・補完項を移行。見出し・参照のみ再編 |
| 8.3 Flexible Loadの独立性 | [II-04.3 DER制御・負荷制御・結果確認](../chapters/II_GW/II-04_DER_Load_Control.md#legacy-8-3) | 本文・補完項を移行。見出し・参照のみ再編 |
| 8.4 入力不足と機能利用可否 | [II-05.3 高度エネルギーマネジメント](../chapters/II_GW/II-05_Advanced_EMS.md#legacy-8-4) | 本文・補完項を移行。見出し・参照のみ再編 |
| 8.5 系統制約を考慮する計画 | [II-05.4 高度エネルギーマネジメント](../chapters/II_GW/II-05_Advanced_EMS.md#legacy-8-5) | 本文・補完項を移行。見出し・参照のみ再編 |
| 8.6.1 高度エネマネ戦略の採否・適用・解除 | [II-05.5 高度エネルギーマネジメント](../chapters/II_GW/II-05_Advanced_EMS.md#legacy-8-6-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 8.6.2 予測・計画・目標未達の扱い | [II-05.6 高度エネルギーマネジメント](../chapters/II_GW/II-05_Advanced_EMS.md#legacy-8-6-2) | 本文・補完項を移行。見出し・参照のみ再編 |
| 8.6.3 DER/負荷の個別操作と快適性条件 | [II-04.4 DER制御・負荷制御・結果確認](../chapters/II_GW/II-04_DER_Load_Control.md#legacy-8-6-3) | 本文・補完項を移行。見出し・参照のみ再編 |
<a id="old-ch-09"></a>
## 旧09章 — 09_Measurement_Data

元資料：[R7原本（履歴）](../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/09_Measurement_Data.md)

| 元の節／項 | 現行の章・節 | 取扱い |
|---|---|---|
| 9.1 計測の意味と正本 | [II-07.1 計測・状態・履歴・データ公開機能](../chapters/II_GW/II-07_Measurement_Data.md#legacy-9-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 9.2 二重計上と未取得 | [II-07.2 計測・状態・履歴・データ公開機能](../chapters/II_GW/II-07_Measurement_Data.md#legacy-9-2) | 本文・補完項を移行。見出し・参照のみ再編 |
| 9.3 保存区分：先行検討からの持越しを具体化した案 | [II-07.3 計測・状態・履歴・データ公開機能](../chapters/II_GW/II-07_Measurement_Data.md#legacy-9-3) | 本文・補完項を移行。見出し・参照のみ再編 |
| 9.4 制御・監査記録 | [IV-08.1 データ完全性・ログ・UI品質](../chapters/IV_Quality/IV-08_Data_Log_UI_Quality.md#legacy-9-4) | 本文・補完項を移行。見出し・参照のみ再編 |
| 9.5 データ抽出と診断 | [II-07.4 計測・状態・履歴・データ公開機能](../chapters/II_GW/II-07_Measurement_Data.md#legacy-9-5) | 本文・補完項を移行。見出し・参照のみ再編 |
| 9.6 R2追加：上位公開・同期・監視負荷 | [II-07.5 計測・状態・履歴・データ公開機能](../chapters/II_GW/II-07_Measurement_Data.md#legacy-9-6) | 本文・補完項を移行。見出し・参照のみ再編 |
| 9.9 R3導入・R4適用：方式・適用状態の公開 | [II-07.6 計測・状態・履歴・データ公開機能](../chapters/II_GW/II-07_Measurement_Data.md#legacy-9-9) | 本文・補完項を移行。見出し・参照のみ再編 |
| 9.10 R4：ネットワーク状態の非推移性 | [II-07.7 計測・状態・履歴・データ公開機能](../chapters/II_GW/II-07_Measurement_Data.md#legacy-9-10) | 本文・補完項を移行。見出し・参照のみ再編 |
| 9.11 R5：計測器と他機器の観測戻り | [II-07.8 計測・状態・履歴・データ公開機能](../chapters/II_GW/II-07_Measurement_Data.md#legacy-9-11) | 本文・補完項を移行。見出し・参照のみ再編 |
| 9.12.1 実項目・型・単位・品質・計測点 | [II-07.9 計測・状態・履歴・データ公開機能](../chapters/II_GW/II-07_Measurement_Data.md#legacy-9-12-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 9.13.1 保存容量・集計・電断時完全性 | [IV-08.2 データ完全性・ログ・UI品質](../chapters/IV_Quality/IV-08_Data_Log_UI_Quality.md#legacy-9-13-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 9.13.2 上位同期・履歴エクスポート・削除 | [II-07.10 計測・状態・履歴・データ公開機能](../chapters/II_GW/II-07_Measurement_Data.md#legacy-9-13-2) | 本文・補完項を移行。見出し・参照のみ再編 |
<a id="old-ch-10"></a>
## 旧10章 — 10_Grid_Protection

元資料：[R7原本（履歴）](../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/10_Grid_Protection.md)

| 元の節／項 | 現行の章・節 | 取扱い |
|---|---|---|
| 10.1 本章の適用範囲 | [I-07.2 全体責務配分・電力制約・保護](../chapters/I_System/I-07_Responsibilities_Constraints.md#legacy-10-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 10.2 出力制御ユニットの契約 | [II-08.1 GW G側の出力制御機能](../chapters/II_GW/II-08_GW_Grid_Control.md#legacy-10-2) | 本文・補完項を移行。見出し・参照のみ再編 |
| 10.3 最終制約と保護 | [I-07.3 全体責務配分・電力制約・保護](../chapters/I_System/I-07_Responsibilities_Constraints.md#legacy-10-3) | 本文・補完項を移行。見出し・参照のみ再編 |
| 10.4 四つの通信・観測障害を区別する | [I-08.1 システム状態・可用機能・成立条件](../chapters/I_System/I-08_System_States.md#legacy-10-4) | 本文・補完項を移行。見出し・参照のみ再編 |
| 10.5 HEMS停止と通常要求の残留 | [I-08.2 システム状態・可用機能・成立条件](../chapters/I_System/I-08_System_States.md#legacy-10-5) | 本文・補完項を移行。見出し・参照のみ再編 |
| 10.6 R3導入・R4適用：配置によって変わる正本と責任 | [I-07.4 全体責務配分・電力制約・保護](../chapters/I_System/I-07_Responsibilities_Constraints.md#legacy-10-6) | 本文・補完項を移行。見出し・参照のみ再編 |
| 10.7 R4：宅内ルータ必須と対象限定 | [I-07.5 全体責務配分・電力制約・保護](../chapters/I_System/I-07_Responsibilities_Constraints.md#legacy-10-7) | 本文・補完項を移行。見出し・参照のみ再編 |
| 10.8.1 エリア・契約・スケジュール仕様の版 | [V-04.1 適用規格・制度・認証構成](../chapters/V_Lifecycle/V-04_Compliance.md#legacy-10-8-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 10.8.2 通常API非迂回・保護・復帰の確認 | [I-07.6 全体責務配分・電力制約・保護](../chapters/I_System/I-07_Responsibilities_Constraints.md#legacy-10-8-2) | 本文・補完項を移行。見出し・参照のみ再編 |
<a id="old-ch-11"></a>
## 旧11章 — 11_Power_Constraints

元資料：[R7原本（履歴）](../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/11_Power_Constraints.md)

| 元の節／項 | 現行の章・節 | 取扱い |
|---|---|---|
| 11.1 制約のscope | [I-07.7 全体責務配分・電力制約・保護](../chapters/I_System/I-07_Responsibilities_Constraints.md#legacy-11-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 11.2 電力収支 | [I-07.8 全体責務配分・電力制約・保護](../chapters/I_System/I-07_Responsibilities_Constraints.md#legacy-11-2) | 本文・補完項を移行。見出し・参照のみ再編 |
| 11.3 機器能力と計画制約 | [I-07.9 全体責務配分・電力制約・保護](../chapters/I_System/I-07_Responsibilities_Constraints.md#legacy-11-3) | 本文・補完項を移行。見出し・参照のみ再編 |
| 11.4 複数メーカー・複数PCS | [I-07.10 全体責務配分・電力制約・保護](../chapters/I_System/I-07_Responsibilities_Constraints.md#legacy-11-4) | 本文・補完項を移行。見出し・参照のみ再編 |
| 11.5 過渡と評価 | [I-07.11 全体責務配分・電力制約・保護](../chapters/I_System/I-07_Responsibilities_Constraints.md#legacy-11-5) | 本文・補完項を移行。見出し・参照のみ再編 |
| 11.6 R4：混在する取得主体と共有連系点 | [I-07.12 全体責務配分・電力制約・保護](../chapters/I_System/I-07_Responsibilities_Constraints.md#legacy-11-6) | 本文・補完項を移行。見出し・参照のみ再編 |
| 11.7.1 基準点・容量・変換グループの対応 | [I-07.13 全体責務配分・電力制約・保護](../chapters/I_System/I-07_Responsibilities_Constraints.md#legacy-11-7-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 11.7.2 混在設備・過渡・実出力の合否 | [I-07.14 全体責務配分・電力制約・保護](../chapters/I_System/I-07_Responsibilities_Constraints.md#legacy-11-7-2) | 本文・補完項を移行。見出し・参照のみ再編 |
<a id="old-ch-12"></a>
## 旧12章 — 12_Configuration_Lifecycle

元資料：[R7原本（履歴）](../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/12_Configuration_Lifecycle.md)

| 元の節／項 | 現行の章・節 | 取扱い |
|---|---|---|
| 12.1 状態軸 | [II-09.1 設定・起動停止・内部機能操作](../chapters/II_GW/II-09_Settings_Lifecycle.md#legacy-12-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 12.2 設定の領域分離 | [II-09.2 設定・起動停止・内部機能操作](../chapters/II_GW/II-09_Settings_Lifecycle.md#legacy-12-2) | 本文・補完項を移行。見出し・参照のみ再編 |
| 12.3 通常設定変更の振る舞い：本書の具体化案 | [II-09.3 設定・起動停止・内部機能操作](../chapters/II_GW/II-09_Settings_Lifecycle.md#legacy-12-3) | 本文・補完項を移行。見出し・参照のみ再編 |
| 12.4 バックアップ・リストア | [II-09.4 設定・起動停止・内部機能操作](../chapters/II_GW/II-09_Settings_Lifecycle.md#legacy-12-4) | 本文・補完項を移行。見出し・参照のみ再編 |
| 12.5 R2追加：複数チャネルの設定変更 | [II-09.5 設定・起動停止・内部機能操作](../chapters/II_GW/II-09_Settings_Lifecycle.md#legacy-12-5) | 本文・補完項を移行。見出し・参照のみ再編 |
| 12.6 R3導入・R4適用：方式選択は系統構成変更 | [V-02.1 施工・初期設定・試運転・引渡し](../chapters/V_Lifecycle/V-02_Commissioning_Handover.md#legacy-12-6) | 本文・補完項を移行。見出し・参照のみ再編 |
| 12.7 R4：ルータ接続と構成変更の制限 | [V-02.2 施工・初期設定・試運転・引渡し](../chapters/V_Lifecycle/V-02_Commissioning_Handover.md#legacy-12-7) | 本文・補完項を移行。見出し・参照のみ再編 |
| 12.8.1 起動完了・未登録・縮退・停止 | [II-09.6 設定・起動停止・内部機能操作](../chapters/II_GW/II-09_Settings_Lifecycle.md#legacy-12-8-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 12.9.1 設定キー・型・範囲・既定値・権限 | [II-09.7 設定・起動停止・内部機能操作](../chapters/II_GW/II-09_Settings_Lifecycle.md#legacy-12-9-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 12.9.2 同時変更・部分反映・緊急変更 | [II-09.8 設定・起動停止・内部機能操作](../chapters/II_GW/II-09_Settings_Lifecycle.md#legacy-12-9-2) | 本文・補完項を移行。見出し・参照のみ再編 |
| 12.9.3 バックアップ・工場初期化・移行 | [II-09.9 設定・起動停止・内部機能操作](../chapters/II_GW/II-09_Settings_Lifecycle.md#legacy-12-9-3) | 本文・補完項を移行。見出し・参照のみ再編 |
<a id="old-ch-13"></a>
## 旧13章 — 13_Fault_Recovery_OTA

元資料：[R7原本（履歴）](../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/13_Fault_Recovery_OTA.md)

| 元の節／項 | 現行の章・節 | 取扱い |
|---|---|---|
| 13.1 障害分類 | [II-10.1 障害検出・縮退復旧・警報診断機能](../chapters/II_GW/II-10_Fault_Alarm_Diagnostics.md#legacy-13-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 13.2 再試行と結果不明 | [II-10.2 障害検出・縮退復旧・警報診断機能](../chapters/II_GW/II-10_Fault_Alarm_Diagnostics.md#legacy-13-2) | 本文・補完項を移行。見出し・参照のみ再編 |
| 13.3 通常のOTA | [II-11.1 FW取得・検証・適用・復旧機能](../chapters/II_GW/II-11_Firmware_Update.md#legacy-13-3) | 本文・補完項を移行。見出し・参照のみ再編 |
| 13.4 機器内残留要求 | [II-10.3 障害検出・縮退復旧・警報診断機能](../chapters/II_GW/II-10_Fault_Alarm_Diagnostics.md#legacy-13-4) | 本文・補完項を移行。見出し・参照のみ再編 |
| 13.5 外部操作元との共存 | [II-10.4 障害検出・縮退復旧・警報診断機能](../chapters/II_GW/II-10_Fault_Alarm_Diagnostics.md#legacy-13-5) | 本文・補完項を移行。見出し・参照のみ再編 |
| 13.6 R2追加：上位・配信・Web・アプリを別故障にする | [II-10.5 障害検出・縮退復旧・警報診断機能](../chapters/II_GW/II-10_Fault_Alarm_Diagnostics.md#legacy-13-6) | 本文・補完項を移行。見出し・参照のみ再編 |
| 13.7 R3導入・R4適用：HEMS停止とGW全体停止の区別 | [I-08.3 システム状態・可用機能・成立条件](../chapters/I_System/I-08_System_States.md#legacy-13-7) | 本文・補完項を移行。見出し・参照のみ再編 |
| 13.8 R4：共有ルータ・WAN・LANの障害 | [I-08.4 システム状態・可用機能・成立条件](../chapters/I_System/I-08_System_States.md#legacy-13-8) | 本文・補完項を移行。見出し・参照のみ再編 |
| 13.9.1 検出閾値・重大度・復帰・再発 | [II-10.6 障害検出・縮退復旧・警報診断機能](../chapters/II_GW/II-10_Fault_Alarm_Diagnostics.md#legacy-13-9-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 13.9.2 更新中断・起動不能・実機残留要求 | [II-11.2 FW取得・検証・適用・復旧機能](../chapters/II_GW/II-11_Firmware_Update.md#legacy-13-9-2) | 本文・補完項を移行。見出し・参照のみ再編 |
<a id="old-ch-14"></a>
## 旧14章 — 14_Performance_Security

元資料：[R7原本（履歴）](../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/14_Performance_Security.md)

| 元の節／項 | 現行の章・節 | 取扱い |
|---|---|---|
| 14.1 周期と期限を分ける | [IV-01.1 性能・時間・精度・容量](../chapters/IV_Quality/IV-01_Performance_Capacity.md#legacy-14-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 14.2 性能の保証条件 | [IV-01.2 性能・時間・精度・容量](../chapters/IV_Quality/IV-01_Performance_Capacity.md#legacy-14-2) | 本文・補完項を移行。見出し・参照のみ再編 |
| 14.3 セキュリティ文脈 | [IV-03.1 セキュリティ・プライバシー](../chapters/IV_Quality/IV-03_Security_Privacy.md#legacy-14-3) | 本文・補完項を移行。見出し・参照のみ再編 |
| 14.4 JC-STAR・制度・製品運用との接続 | [IV-03.2 セキュリティ・プライバシー](../chapters/IV_Quality/IV-03_Security_Privacy.md#legacy-14-4) | 本文・補完項を移行。見出し・参照のみ再編 |
| 14.5 R2追加：上位・Web・FWの信頼境界と資源予算 | [IV-03.3 セキュリティ・プライバシー](../chapters/IV_Quality/IV-03_Security_Privacy.md#legacy-14-5) | 本文・補完項を移行。見出し・参照のみ再編 |
| 14.9 R3導入・R4適用：GW管理方式の資源と資格情報 | [IV-01.3 性能・時間・精度・容量](../chapters/IV_Quality/IV-01_Performance_Capacity.md#legacy-14-9) | 本文・補完項を移行。見出し・参照のみ再編 |
| 14.10 R4：ルータ共用の負荷と不明条件 | [IV-01.4 性能・時間・精度・容量](../chapters/IV_Quality/IV-01_Performance_Capacity.md#legacy-14-10) | 本文・補完項を移行。見出し・参照のみ再編 |
| 14.11.1 機能別の時間・精度・容量プロファイル | [IV-01.5 性能・時間・精度・容量](../chapters/IV_Quality/IV-01_Performance_Capacity.md#legacy-14-11-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 14.11.2 同時最大負荷・上限・飽和動作 | [IV-01.6 性能・時間・精度・容量](../chapters/IV_Quality/IV-01_Performance_Capacity.md#legacy-14-11-2) | 本文・補完項を移行。見出し・参照のみ再編 |
<a id="old-ch-15"></a>
## 旧15章 — 15_Deployment_Isolation

元資料：[R7原本（履歴）](../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/15_Deployment_Isolation.md)

| 元の節／項 | 現行の章・節 | 取扱い |
|---|---|---|
| 15.1 接続方式と実行配置を分ける | [II-01.12 GW論理構成・H/G責務・状態所有者](../chapters/II_GW/II-01_GW_Architecture.md#legacy-15-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 15.2 Certification Isolation Boundary | [IV-07.1 非干渉・認証影響分離・共有資源制約](../chapters/IV_Quality/IV-07_Isolation_Shared_Resources.md#legacy-15-2) | 本文・補完項を移行。見出し・参照のみ再編 |
| 15.3 共有資源 | [IV-07.2 非干渉・認証影響分離・共有資源制約](../chapters/IV_Quality/IV-07_Isolation_Shared_Resources.md#legacy-15-3) | 本文・補完項を移行。見出し・参照のみ再編 |
| 15.4 RS-485の配置判断 | [II-01.13 GW論理構成・H/G責務・状態所有者](../chapters/II_GW/II-01_GW_Architecture.md#legacy-15-4) | 本文・補完項を移行。見出し・参照のみ再編 |
| 15.5 配置を固定するレビュー条件 | [II-01.14 GW論理構成・H/G責務・状態所有者](../chapters/II_GW/II-01_GW_Architecture.md#legacy-15-5) | 本文・補完項を移行。見出し・参照のみ再編 |
| 15.6 R2追加：外部管理機能からの非干渉 | [IV-07.3 非干渉・認証影響分離・共有資源制約](../chapters/IV_Quality/IV-07_Isolation_Shared_Resources.md#legacy-15-6) | 本文・補完項を移行。見出し・参照のみ再編 |
| 15.7 GW_MANAGEDのPCS送信所有者 | [II-01.15 GW論理構成・H/G責務・状態所有者](../chapters/II_GW/II-01_GW_Architecture.md#legacy-15-7) | 本文・補完項を移行。見出し・参照のみ再編 |
| 15.8 R4：共通ルータは独立性の除外ではない | [IV-07.4 非干渉・認証影響分離・共有資源制約](../chapters/IV_Quality/IV-07_Isolation_Shared_Resources.md#legacy-15-8) | 本文・補完項を移行。見出し・参照のみ再編 |
| 15.9.1 G側実装と共有資源の依存表 | [II-01.16 GW論理構成・H/G責務・状態所有者](../chapters/II_GW/II-01_GW_Architecture.md#legacy-15-9-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 15.9.2 非干渉評価の範囲と根拠文書 | [IV-07.5 非干渉・認証影響分離・共有資源制約](../chapters/IV_Quality/IV-07_Isolation_Shared_Resources.md#legacy-15-9-2) | 本文・補完項を移行。見出し・参照のみ再編 |
<a id="old-ch-16"></a>
## 旧16章 — 16_Certification_Change

元資料：[R7原本（履歴）](../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/16_Certification_Change.md)

| 元の節／項 | 現行の章・節 | 取扱い |
|---|---|---|
| 16.1 目標と保証の限界 | [V-04.2 適用規格・制度・認証構成](../chapters/V_Lifecycle/V-04_Compliance.md#legacy-16-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 16.2 認証構成台帳 | [V-04.3 適用規格・制度・認証構成](../chapters/V_Lifecycle/V-04_Compliance.md#legacy-16-2) | 本文・補完項を移行。見出し・参照のみ再編 |
| 16.3 社内の変更分類案 | [V-05.1 変更影響・互換性・移行・リリース](../chapters/V_Lifecycle/V-05_Change_Migration_Release.md#legacy-16-3) | 本文・補完項を移行。見出し・参照のみ再編 |
| 16.4 非干渉の確認条件 | [V-05.2 変更影響・互換性・移行・リリース](../chapters/V_Lifecycle/V-05_Change_Migration_Release.md#legacy-16-4) | 本文・補完項を移行。見出し・参照のみ再編 |
| 16.5 三つの承認を分ける | [V-05.3 変更影響・互換性・移行・リリース](../chapters/V_Lifecycle/V-05_Change_Migration_Release.md#legacy-16-5) | 本文・補完項を移行。見出し・参照のみ再編 |
| 16.7 R2追加：クラウド・UI・FW配信の変更も対象条件を確認 | [V-05.4 変更影響・互換性・移行・リリース](../chapters/V_Lifecycle/V-05_Change_Migration_Release.md#legacy-16-7) | 本文・補完項を移行。見出し・参照のみ再編 |
| 16.8 R3導入・R4適用：方式ごとの構成評価と切替 | [V-04.4 適用規格・制度・認証構成](../chapters/V_Lifecycle/V-04_Compliance.md#legacy-16-8) | 本文・補完項を移行。見出し・参照のみ再編 |
| 16.9 R4：ルータを含む影響証拠 | [V-05.5 変更影響・互換性・移行・リリース](../chapters/V_Lifecycle/V-05_Change_Migration_Release.md#legacy-16-9) | 本文・補完項を移行。見出し・参照のみ再編 |
| 16.10.1 文書版・条項・要求・証拠の対応 | [V-04.5 適用規格・制度・認証構成](../chapters/V_Lifecycle/V-04_Compliance.md#legacy-16-10-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 16.10.2 変更手続きと社内リリース判定 | [V-05.6 変更影響・互換性・移行・リリース](../chapters/V_Lifecycle/V-05_Change_Migration_Release.md#legacy-16-10-2) | 本文・補完項を移行。見出し・参照のみ再編 |
<a id="old-ch-17"></a>
## 旧17章 — 17_Verification

元資料：[R7原本（履歴）](../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/17_Verification.md)

| 元の節／項 | 現行の章・節 | 取扱い |
|---|---|---|
| 17.1 検証の区分 | [V-06.1 検証・妥当性確認・受入](../chapters/V_Lifecycle/V-06_Verification_Validation.md#legacy-17-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 17.2 原典IDの保持と拡張 | [V-06.2 検証・妥当性確認・受入](../chapters/V_Lifecycle/V-06_Verification_Validation.md#legacy-17-2) | 本文・補完項を移行。見出し・参照のみ再編 |
| 17.3 受入プロファイルが揃うまでの扱い | [V-06.3 検証・妥当性確認・受入](../chapters/V_Lifecycle/V-06_Verification_Validation.md#legacy-17-3) | 本文・補完項を移行。見出し・参照のみ再編 |
| 17.4 優先して成立を確認する試験 | [V-06.4 検証・妥当性確認・受入](../chapters/V_Lifecycle/V-06_Verification_Validation.md#legacy-17-4) | 本文・補完項を移行。見出し・参照のみ再編 |
| 17.5 POCの位置付け | [V-06.5 検証・妥当性確認・受入](../chapters/V_Lifecycle/V-06_Verification_Validation.md#legacy-17-5) | 本文・補完項を移行。見出し・参照のみ再編 |
| 17.6 リリース受入 | [V-06.6 検証・妥当性確認・受入](../chapters/V_Lifecycle/V-06_Verification_Validation.md#legacy-17-6) | 本文・補完項を移行。見出し・参照のみ再編 |
| 17.7 R2追加：上位・宅内・アプリ・FWの統合受入 | [V-06.7 検証・妥当性確認・受入](../chapters/V_Lifecycle/V-06_Verification_Validation.md#legacy-17-7) | 本文・補完項を移行。見出し・参照のみ再編 |
| 17.8 R3導入・R4適用：二方式の検証範囲 | [V-06.8 検証・妥当性確認・受入](../chapters/V_Lifecycle/V-06_Verification_Validation.md#legacy-17-8) | 本文・補完項を移行。見出し・参照のみ再編 |
| 17.9 R4：R4経路・機器限定の検証 | [V-06.9 検証・妥当性確認・受入](../chapters/V_Lifecycle/V-06_Verification_Validation.md#legacy-17-9) | 本文・補完項を移行。見出し・参照のみ再編 |
| 17.10.1 全要求の検証方法と受入プロファイル | [V-06.10 検証・妥当性確認・受入](../chapters/V_Lifecycle/V-06_Verification_Validation.md#legacy-17-10-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 17.10.2 利用者目的に対するValidation | [V-06.11 検証・妥当性確認・受入](../chapters/V_Lifecycle/V-06_Verification_Validation.md#legacy-17-10-2) | 本文・補完項を移行。見出し・参照のみ再編 |
| 17.10.3 補完項目の評価配賦と適用除外 | [V-06.12 検証・妥当性確認・受入](../chapters/V_Lifecycle/V-06_Verification_Validation.md#legacy-17-10-3) | 本文・補完項を移行。見出し・参照のみ再編 |
<a id="old-ch-18"></a>
## 旧18章 — 18_Migration

元資料：[R7原本（履歴）](../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/18_Migration.md)

| 元の節／項 | 現行の章・節 | 取扱い |
|---|---|---|
| 18.1 今回わかっていること | [V-05.7 変更影響・互換性・移行・リリース](../chapters/V_Lifecycle/V-05_Change_Migration_Release.md#legacy-18-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 18.2 先行仕様案からの主要な改訂 | [V-05.8 変更影響・互換性・移行・リリース](../chapters/V_Lifecycle/V-05_Change_Migration_Release.md#legacy-18-2) | 本文・補完項を移行。見出し・参照のみ再編 |
| 18.3 移行の順序 | [V-05.9 変更影響・互換性・移行・リリース](../chapters/V_Lifecycle/V-05_Change_Migration_Release.md#legacy-18-3) | 本文・補完項を移行。見出し・参照のみ再編 |
| 18.4 LegacyとNext | [V-05.10 変更影響・互換性・移行・リリース](../chapters/V_Lifecycle/V-05_Change_Migration_Release.md#legacy-18-4) | 本文・補完項を移行。見出し・参照のみ再編 |
| 18.5 R2追加：既存上位APIと画面の移行 | [V-05.11 変更影響・互換性・移行・リリース](../chapters/V_Lifecycle/V-05_Change_Migration_Release.md#legacy-18-5) | 本文・補完項を移行。見出し・参照のみ再編 |
| 18.8 R3導入・R4適用：既設構成へ両方式を導入する際の手順 | [V-05.12 変更影響・互換性・移行・リリース](../chapters/V_Lifecycle/V-05_Change_Migration_Release.md#legacy-18-8) | 本文・補完項を移行。見出し・参照のみ再編 |
| 18.9 R4：R3の汎用modeからR4へ | [V-05.13 変更影響・互換性・移行・リリース](../chapters/V_Lifecycle/V-05_Change_Migration_Release.md#legacy-18-9) | 本文・補完項を移行。見出し・参照のみ再編 |
| 18.10.1 As-Is確認と新旧製品への機能配賦 | [V-05.14 変更影響・互換性・移行・リリース](../chapters/V_Lifecycle/V-05_Change_Migration_Release.md#legacy-18-10-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 18.10.2 版互換・設定移行・旧経路停止 | [V-05.15 変更影響・互換性・移行・リリース](../chapters/V_Lifecycle/V-05_Change_Migration_Release.md#legacy-18-10-2) | 本文・補完項を移行。見出し・参照のみ再編 |
<a id="old-ch-19"></a>
## 旧19章 — 19_Open_Issues_Sources

元資料：[R7原本（履歴）](../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/19_Open_Issues_Sources.md)

| 元の節／項 | 現行の章・節 | 取扱い |
|---|---|---|
| 19.1 判断状態の維持 | [V-07.1 要求トレース・仕様完成・Open Question管理](../chapters/V_Lifecycle/V-07_Trace_Open_Questions.md#legacy-19-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 19.2 レビューの優先順 | [V-07.2 要求トレース・仕様完成・Open Question管理](../chapters/V_Lifecycle/V-07_Trace_Open_Questions.md#legacy-19-2) | 本文・補完項を移行。見出し・参照のみ再編 |
| 19.3 根拠索引 | [V-07.3 要求トレース・仕様完成・Open Question管理](../chapters/V_Lifecycle/V-07_Trace_Open_Questions.md#legacy-19-3) | 本文・補完項を移行。見出し・参照のみ再編 |
| 19.4 今回の完了範囲 | [V-07.4 要求トレース・仕様完成・Open Question管理](../chapters/V_Lifecycle/V-07_Trace_Open_Questions.md#legacy-19-4) | 当時の文書管理記述をR8に置換。原文は履歴保持 |
| 19.5 R2追加の出典・検討状態 | [V-07.5 要求トレース・仕様完成・Open Question管理](../chapters/V_Lifecycle/V-07_Trace_Open_Questions.md#legacy-19-5) | 本文・補完項を移行。見出し・参照のみ再編 |
| 19.8 R3入力・判断差分（履歴） | [V-07.6 要求トレース・仕様完成・Open Question管理](../chapters/V_Lifecycle/V-07_Trace_Open_Questions.md#legacy-19-8) | 本文・補完項を移行。見出し・参照のみ再編 |
| 19.9 R4：原典優先と確認範囲 | [V-07.7 要求トレース・仕様完成・Open Question管理](../chapters/V_Lifecycle/V-07_Trace_Open_Questions.md#legacy-19-9) | 本文・補完項を移行。見出し・参照のみ再編 |
| 19.10.1 上位USDMと双方向トレーサビリティ | [V-07.8 要求トレース・仕様完成・Open Question管理](../chapters/V_Lifecycle/V-07_Trace_Open_Questions.md#legacy-19-10-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 19.10.2 OQの責任者・期限・決定ゲート | [V-07.9 要求トレース・仕様完成・Open Question管理](../chapters/V_Lifecycle/V-07_Trace_Open_Questions.md#legacy-19-10-2) | 本文・補完項を移行。見出し・参照のみ再編 |
| 19.10.3 現行仕様と履歴の意味的整合 | [V-05.16 変更影響・互換性・移行・リリース](../chapters/V_Lifecycle/V-05_Change_Migration_Release.md#legacy-19-10-3) | 本文・補完項を移行。見出し・参照のみ再編 |
<a id="old-ch-20"></a>
## 旧20章 — 20_Northbound_Monitoring_FW

元資料：[R7原本（履歴）](../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/20_Northbound_Monitoring_FW.md)

| 元の節／項 | 現行の章・節 | 取扱い |
|---|---|---|
| 20.1 上位サービスの責務と操作種別 | [III-02.1 上位管理・監視サーバ—GWインターフェース](../chapters/III_Interfaces/III-02_Cloud_GW.md#legacy-20-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 20.2 上位サーバとの境界契約 | [III-02.2 上位管理・監視サーバ—GWインターフェース](../chapters/III_Interfaces/III-02_Cloud_GW.md#legacy-20-2) | 本文・補完項を移行。見出し・参照のみ再編 |
| 20.3 宅内Web UI：直接接続とルータ経由 | [III-04.1 宅内Web UI—GWインターフェース](../chapters/III_Interfaces/III-04_Local_Web.md#legacy-20-3) | 本文・補完項を移行。見出し・参照のみ再編 |
| 20.4 リモート監視・操作アプリ | [III-05.1 スマートフォンアプリ—クラウド連携](../chapters/III_Interfaces/III-05_Remote_App.md#legacy-20-4) | 本文・補完項を移行。見出し・参照のみ再編 |
| 20.5 クラウド・GW・実機の結果を分ける | [III-02.3 上位管理・監視サーバ—GWインターフェース](../chapters/III_Interfaces/III-02_Cloud_GW.md#legacy-20-5) | 本文・補完項を移行。見出し・参照のみ再編 |
| 20.6 設定変更：クラウドとローカルの同時操作 | [II-09.10 設定・起動停止・内部機能操作](../chapters/II_GW/II-09_Settings_Lifecycle.md#legacy-20-6) | 本文・補完項を移行。見出し・参照のみ再編 |
| 20.7 ネットワーク設定変更と到達性 | [II-09.11 設定・起動停止・内部機能操作](../chapters/II_GW/II-09_Settings_Lifecycle.md#legacy-20-7) | 本文・補完項を移行。見出し・参照のみ再編 |
| 20.8 GW内部機能への操作 | [II-09.12 設定・起動停止・内部機能操作](../chapters/II_GW/II-09_Settings_Lifecycle.md#legacy-20-8) | 本文・補完項を移行。見出し・参照のみ再編 |
| 20.9 内部情報・状態の公開View | [II-07.11 計測・状態・履歴・データ公開機能](../chapters/II_GW/II-07_Measurement_Data.md#legacy-20-9) | 本文・補完項を移行。見出し・参照のみ再編 |
| 20.10 オフライン・再送・所有者変更 | [III-02.4 上位管理・監視サーバ—GWインターフェース](../chapters/III_Interfaces/III-02_Cloud_GW.md#legacy-20-10) | 本文・補完項を移行。見出し・参照のみ再編 |
| 20.11 FW配信・更新の責任を分ける | [II-11.3 FW取得・検証・適用・復旧機能](../chapters/II_GW/II-11_Firmware_Update.md#legacy-20-11) | 本文・補完項を移行。見出し・参照のみ再編 |
| 20.12 FW更新の状態と障害 | [II-11.4 FW取得・検証・適用・復旧機能](../chapters/II_GW/II-11_Firmware_Update.md#legacy-20-12) | 本文・補完項を移行。見出し・参照のみ再編 |
| 20.13 代表ユースケース | [I-06.10 システムユースケース・横断振る舞い](../chapters/I_System/I-06_Usecases.md#legacy-20-13) | 本文・補完項を移行。見出し・参照のみ再編 |
| 20.14 障害・利用可能性マトリクス | [I-08.5 システム状態・可用機能・成立条件](../chapters/I_System/I-08_System_States.md#legacy-20-14) | 本文・補完項を移行。見出し・参照のみ再編 |
| 20.15 仕様を確定させる入口 | [III-02.5 上位管理・監視サーバ—GWインターフェース](../chapters/III_Interfaces/III-02_Cloud_GW.md#legacy-20-15) | 本文・補完項を移行。見出し・参照のみ再編 |
| 20.19 R3導入・R4適用：方式選択状態の監視と保守境界 | [III-02.6 上位管理・監視サーバ—GWインターフェース](../chapters/III_Interfaces/III-02_Cloud_GW.md#legacy-20-19) | 本文・補完項を移行。見出し・参照のみ再編 |
| 20.20 R3導入・R4適用：更新・復元・無線変更と方式 | [II-11.5 FW取得・検証・適用・復旧機能](../chapters/II_GW/II-11_Firmware_Update.md#legacy-20-20) | 本文・補完項を移行。見出し・参照のみ再編 |
| 20.21 R4：全取得通信のルータ経由化と画面表示 | [III-02.7 上位管理・監視サーバ—GWインターフェース](../chapters/III_Interfaces/III-02_Cloud_GW.md#legacy-20-21) | 本文・補完項を移行。見出し・参照のみ再編 |
| 20.22.1 上位プロトコルとGW内部機能の公開一覧 | [III-02.8 上位管理・監視サーバ—GWインターフェース](../chapters/III_Interfaces/III-02_Cloud_GW.md#legacy-20-22-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 20.22.2 FW対象・配信・適用・互換・復旧 | [II-11.6 FW取得・検証・適用・復旧機能](../chapters/II_GW/II-11_Firmware_Update.md#legacy-20-22-2) | 本文・補完項を移行。見出し・参照のみ再編 |
| 20.22.3 オフライン・通知・認可失効の契約 | [III-02.9 上位管理・監視サーバ—GWインターフェース](../chapters/III_Interfaces/III-02_Cloud_GW.md#legacy-20-22-3) | 本文・補完項を移行。見出し・参照のみ再編 |
| 20.23.1 画面・表示項目・対応端末・操作確認 | [IV-08.3 データ完全性・ログ・UI品質](../chapters/IV_Quality/IV-08_Data_Log_UI_Quality.md#legacy-20-23-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 20.23.2 警報・通知・確認・抑止・解除 | [II-10.7 障害検出・縮退復旧・警報診断機能](../chapters/II_GW/II-10_Fault_Alarm_Diagnostics.md#legacy-20-23-2) | 本文・補完項を移行。見出し・参照のみ再編 |
<a id="old-ch-21"></a>
## 旧21章 — 21_Grid_Connection_Selection

元資料：[R7原本（履歴）](../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/21_Grid_Connection_Selection.md)

| 元の節／項 | 現行の章・節 | 取扱い |
|---|---|---|
| 21.1 変更後の適用表 | [I-05.10 機器構成パターン・機能適用条件](../chapters/I_System/I-05_Configurations.md#legacy-21-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 21.2 EL接続PCSの自律取得と通常EL通信 | [III-08.1 出力制御サーバ—取得クライアントインターフェース](../chapters/III_Interfaces/III-08_Utility_Server.md#legacy-21-2) | 本文・補完項を移行。見出し・参照のみ再編 |
| 21.3 RS-485接続PCSのGW管理 | [II-08.2 GW G側の出力制御機能](../chapters/II_GW/II-08_GW_Grid_Control.md#legacy-21-3) | 本文・補完項を移行。見出し・参照のみ再編 |
| 21.4 選択単位・混在・一意性 | [I-05.11 機器構成パターン・機能適用条件](../chapters/I_System/I-05_Configurations.md#legacy-21-4) | 本文・補完項を移行。見出し・参照のみ再編 |
| 21.5 設定・経路・状態のモデル | [I-05.12 機器構成パターン・機能適用条件](../chapters/I_System/I-05_Configurations.md#legacy-21-5) | 本文・補完項を移行。見出し・参照のみ再編 |
| 21.6 SYS-UC-25：施工・保守での対応構成の選択・変更 | [V-02.3 施工・初期設定・試運転・引渡し](../chapters/V_Lifecycle/V-02_Commissioning_Handover.md#legacy-21-6) | 本文・補完項を移行。見出し・参照のみ再編 |
| 21.7 構成の有効化・復旧状態 | [V-02.4 施工・初期設定・試運転・引渡し](../chapters/V_Lifecycle/V-02_Commissioning_Handover.md#legacy-21-7) | 本文・補完項を移行。見出し・参照のみ再編 |
| 21.8 障害マトリクス：ルータとGWを分ける | [I-08.6 システム状態・可用機能・成立条件](../chapters/I_System/I-08_System_States.md#legacy-21-8) | 本文・補完項を移行。見出し・参照のみ再編 |
| 21.9 共有ルータと認証影響の扱い | [IV-07.6 非干渉・認証影響分離・共有資源制約](../chapters/IV_Quality/IV-07_Isolation_Shared_Resources.md#legacy-21-9) | 本文・補完項を移行。見出し・参照のみ再編 |
| 21.10 上位・Web・アプリへの表示 | [II-07.12 計測・状態・履歴・データ公開機能](../chapters/II_GW/II-07_Measurement_Data.md#legacy-21-10) | 本文・補完項を移行。見出し・参照のみ再編 |
| 21.11 試験と静的モデルの範囲 | [V-06.13 検証・妥当性確認・受入](../chapters/V_Lifecycle/V-06_Verification_Validation.md#legacy-21-11) | 本文・補完項を移行。見出し・参照のみ再編 |
| 21.12 未確定事項・導入条件 | [I-05.13 機器構成パターン・機能適用条件](../chapters/I_System/I-05_Configurations.md#legacy-21-12) | 本文・補完項を移行。見出し・参照のみ再編 |
| 21.13.1 機種別取得主体・公開状態・実経路 | [I-05.14 機器構成パターン・機能適用条件](../chapters/I_System/I-05_Configurations.md#legacy-21-13-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 21.13.2 施工・保守の構成変更と故障時復旧 | [V-02.5 施工・初期設定・試運転・引渡し](../chapters/V_Lifecycle/V-02_Commissioning_Handover.md#legacy-21-13-2) | 本文・補完項を移行。見出し・参照のみ再編 |
<a id="old-ch-22"></a>
## 旧22章 — 22_Physical_Electrical_Installation

元資料：[R7原本（履歴）](../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/22_Physical_Electrical_Installation.md)

| 元の節／項 | 現行の章・節 | 取扱い |
|---|---|---|
| 22.1.1 電源入力・定格・許容変動 | [IV-05.1 物理・電気・機構・設置条件](../chapters/IV_Quality/IV-05_Physical_Electrical.md#legacy-22-1-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 22.1.2 投入・瞬断・電圧低下・復電・停止 | [IV-05.2 物理・電気・機構・設置条件](../chapters/IV_Quality/IV-05_Physical_Electrical.md#legacy-22-1-2) | 本文・補完項を移行。見出し・参照のみ再編 |
| 22.2.1 端子・コネクタ・ケーブル・USB | [IV-05.3 物理・電気・機構・設置条件](../chapters/IV_Quality/IV-05_Physical_Electrical.md#legacy-22-2-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 22.3.1 外形・取付・放熱・保守空間 | [IV-05.4 物理・電気・機構・設置条件](../chapters/IV_Quality/IV-05_Physical_Electrical.md#legacy-22-3-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 22.3.2 表示器・LED・ボタン・ラベル | [IV-05.5 物理・電気・機構・設置条件](../chapters/IV_Quality/IV-05_Physical_Electrical.md#legacy-22-3-2) | 本文・補完項を移行。見出し・参照のみ再編 |
<a id="old-ch-23"></a>
## 旧23章 — 23_Environment_EMC_Transport

元資料：[R7原本（履歴）](../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/23_Environment_EMC_Transport.md)

| 元の節／項 | 現行の章・節 | 取扱い |
|---|---|---|
| 23.1.1 温湿度・結露・標高・汚損等の適用 | [IV-06.1 環境・EMC・静電気・輸送保管](../chapters/IV_Quality/IV-06_Environment_EMC.md#legacy-23-1-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 23.1.2 屋外・防塵防水・日射・腐食・放熱 | [IV-06.2 環境・EMC・静電気・輸送保管](../chapters/IV_Quality/IV-06_Environment_EMC.md#legacy-23-1-2) | 本文・補完項を移行。見出し・参照のみ再編 |
| 23.2.1 EMC・ESD・サージ等の評価対象 | [IV-06.3 環境・EMC・静電気・輸送保管](../chapters/IV_Quality/IV-06_Environment_EMC.md#legacy-23-2-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 23.3.1 振動・衝撃・保管・輸送後受入 | [IV-06.4 環境・EMC・静電気・輸送保管](../chapters/IV_Quality/IV-06_Environment_EMC.md#legacy-23-3-1) | 本文・補完項を移行。見出し・参照のみ再編 |
<a id="old-ch-24"></a>
## 旧24章 — 24_Product_Remote_Safety

元資料：[R7原本（履歴）](../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/24_Product_Remote_Safety.md)

| 元の節／項 | 現行の章・節 | 取扱い |
|---|---|---|
| 24.1.1 GW・PCS・負荷・利用者の危険源一覧 | [IV-04.1 製品安全・遠隔操作安全](../chapters/IV_Quality/IV-04_Product_Safety.md#legacy-24-1-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 24.2.1 故障・誤操作・通信断時の安全状態 | [IV-04.2 製品安全・遠隔操作安全](../chapters/IV_Quality/IV-04_Product_Safety.md#legacy-24-2-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 24.2.2 遠隔操作・登録・変更の誤り防止 | [IV-04.3 製品安全・遠隔操作安全](../chapters/IV_Quality/IV-04_Product_Safety.md#legacy-24-2-2) | 本文・補完項を移行。見出し・参照のみ再編 |
| 24.3.1 安全検証・注意表示・残留リスク承認 | [IV-04.4 製品安全・遠隔操作安全](../chapters/IV_Quality/IV-04_Product_Safety.md#legacy-24-3-1) | 本文・補完項を移行。見出し・参照のみ再編 |
<a id="old-ch-25"></a>
## 旧25章 — 25_Reliability_Availability_Maintainability

元資料：[R7原本（履歴）](../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/25_Reliability_Availability_Maintainability.md)

| 元の節／項 | 現行の章・節 | 取扱い |
|---|---|---|
| 25.1.1 可用性・許容停止・復旧・データ損失 | [IV-02.1 信頼性・可用性・保守性・耐久性](../chapters/IV_Quality/IV-02_Reliability_Availability.md#legacy-25-1-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 25.1.2 連続稼働・劣化・資源枯渇 | [IV-02.2 信頼性・可用性・保守性・耐久性](../chapters/IV_Quality/IV-02_Reliability_Availability.md#legacy-25-1-2) | 本文・補完項を移行。見出し・参照のみ再編 |
| 25.2.1 故障切分けと許可保守 | [IV-02.3 信頼性・可用性・保守性・耐久性](../chapters/IV_Quality/IV-02_Reliability_Availability.md#legacy-25-2-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 25.3.1 使用寿命・書込み寿命・消耗部品 | [IV-02.4 信頼性・可用性・保守性・耐久性](../chapters/IV_Quality/IV-02_Reliability_Availability.md#legacy-25-3-1) | 本文・補完項を移行。見出し・参照のみ再編 |
<a id="old-ch-26"></a>
## 旧26章 — 26_Manufacturing_Commissioning_Retirement

元資料：[R7原本（履歴）](../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/26_Manufacturing_Commissioning_Retirement.md)

| 元の節／項 | 現行の章・節 | 取扱い |
|---|---|---|
| 26.1.1 個体識別・鍵投入・製造モード | [V-01.1 製造・初期書込み・出荷](../chapters/V_Lifecycle/V-01_Manufacturing_Shipping.md#legacy-26-1-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 26.1.2 出荷状態・検査・校正・梱包 | [V-01.2 製造・初期書込み・出荷](../chapters/V_Lifecycle/V-01_Manufacturing_Shipping.md#legacy-26-1-2) | 本文・補完項を移行。見出し・参照のみ再編 |
| 26.2.1 ネットワーク・機器・計測点の初期設定 | [V-02.6 施工・初期設定・試運転・引渡し](../chapters/V_Lifecycle/V-02_Commissioning_Handover.md#legacy-26-2-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 26.2.2 試運転・利用者引渡し・教育 | [V-02.7 施工・初期設定・試運転・引渡し](../chapters/V_Lifecycle/V-02_Commissioning_Handover.md#legacy-26-2-2) | 本文・補完項を移行。見出し・参照のみ再編 |
| 26.3.1 本体/機器交換と所有者変更 | [V-03.1 運用保守・修理交換・廃棄・サービス終了](../chapters/V_Lifecycle/V-03_Maintenance_Retirement.md#legacy-26-3-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 26.4.1 秘密・履歴の消去と廃止状態 | [V-03.2 運用保守・修理交換・廃棄・サービス終了](../chapters/V_Lifecycle/V-03_Maintenance_Retirement.md#legacy-26-4-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 26.4.2 支援期間・クラウド終了後の機能 | [V-03.3 運用保守・修理交換・廃棄・サービス終了](../chapters/V_Lifecycle/V-03_Maintenance_Retirement.md#legacy-26-4-2) | 本文・補完項を移行。見出し・参照のみ再編 |
<a id="old-ch-27"></a>
## 旧27章 — 27_Security_Privacy_Lifecycle

元資料：[R7原本（履歴）](../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/27_Security_Privacy_Lifecycle.md)

| 元の節／項 | 現行の章・節 | 取扱い |
|---|---|---|
| 27.1.1 脅威分析と要求・検証の対応 | [IV-03.4 セキュリティ・プライバシー](../chapters/IV_Quality/IV-03_Security_Privacy.md#legacy-27-1-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 27.2.1 生成・配布・更新・失効・漏えい復旧 | [IV-03.5 セキュリティ・プライバシー](../chapters/IV_Quality/IV-03_Security_Privacy.md#legacy-27-2-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 27.2.2 通信保護・Webセッション・機器混在 | [IV-03.6 セキュリティ・プライバシー](../chapters/IV_Quality/IV-03_Security_Privacy.md#legacy-27-2-2) | 本文・補完項を移行。見出し・参照のみ再編 |
| 27.3.1 保守経路・製造アクセス・更新認証 | [IV-03.7 セキュリティ・プライバシー](../chapters/IV_Quality/IV-03_Security_Privacy.md#legacy-27-3-1) | 本文・補完項を移行。見出し・参照のみ再編 |
| 27.3.2 SBOM・脆弱性対応と機器の支援機能 | [V-03.4 運用保守・修理交換・廃棄・サービス終了](../chapters/V_Lifecycle/V-03_Maintenance_Retirement.md#legacy-27-3-2) | 本文・補完項を移行。見出し・参照のみ再編 |
| 27.4.1 個人/住宅データの収集・利用・公開・消去 | [IV-03.8 セキュリティ・プライバシー](../chapters/IV_Quality/IV-03_Security_Privacy.md#legacy-27-4-1) | 本文・補完項を移行。見出し・参照のみ再編 |


<a id="open-questions"></a>
## Open Questions — 本ノートの完成に必要な確認


### 他章で回答する関連質問

| OQ・正本章 | 残る判断 | 完了条件 |
|---|---|---|
| [OQ-R6-19-03](../chapters/V_Lifecycle/V-05_Change_Migration_Release.md#oq-r6-19-03) | 第4.5節の明示補正以外に、履歴由来の構成・用語・保証が現行方針と競合していないか。誰が意味的整合レビューを完了判定するか。 | 現行章をR5の接続・責務・用語と突合し、差分記録を承認する。リンク検査だけで意味的合格にしない。 |
