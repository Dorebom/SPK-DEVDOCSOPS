---
title: "要求トレース・仕様完成・Open Question管理"
document_id: "SPKGW-SYS-V-07"
revision: "R8"
updated: 2026-10-07
status: DRAFT_FOR_REVIEW
part: "V"
---

<a id="v-07"></a>
# V-07 要求トレース・仕様完成・Open Question管理

[全体MOCへ](../../00_MOC.md#part-v)

**本章の対象：** SYS・機能・IF・構成・試験とOQ、未決事項の回答・責任・確定時点。

**記載区分：** 既存R7の有効な記述とR6補完項を再配置。章構成・読み分けの案以外に、新しい実装・権限・数値・適合を確定していない。旧版に由来する具体値や規格参照は当時の確認範囲を引き継ぐ。

## 本章の責務と他章との境界

要求・機能・IF・構成・権限・品質・試験・OQをIDで結び、旧章番号をIDとして使用しない。本版は文書分類と正本位置の再編であり、未確定仕様の回答や製品リリース承認ではない。

85件の既存OQは保持する。各質問の記入正本は新しい担当章の末尾1か所、横断台帳・他章は参照とする。4ロール名称は部分回答済みであり、権限・委任・本人確認等は引き続きOPEN。


<a id="legacy-19-1"></a>
## V-07.1 判断状態の維持

**移行元：** [R7旧19.1節](../../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/19_Open_Issues_Sources.md)。

原典DEC-001〜010を[未確定事項・判断台帳](../../appendices/Open_Issues.md)へ保持する。命名と非影響構造の目標はユーザー合意・目標であり、案Aの実機成立、別CPU、全機器対応、JET試験免除が承認されたことにはしない。

原典TBD-001〜014もIDを維持する。RS-485役割・IF、既存Device公開、数値保証、未知結果の終端等はSYS-TBD-*へ追加し、原典の未決事項の意味を置き換えない。

<a id="legacy-19-2"></a>
## V-07.2 レビューの優先順

**移行元：** [R7旧19.2節](../../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/19_Open_Issues_Sources.md)。

最初に、RS-485既存経路の役割、対象PCS型式と非迂回、連系点・変換グループ、配置案A／Bの成立条件を確認する。続いて通常権威・workflow owner・プロファイル・時間条件を決める。

本書では担当者名を推測せず、役割単位の確認先と完了条件を示す。未確定パラメータは[Parameter Register](../../appendices/Parameter_Register.md)に集約し、レビューで確定値・根拠・適用構成・確認者を記録する。

<a id="legacy-19-3"></a>
## V-07.3 根拠索引

**移行元：** [R7旧19.3節](../../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/19_Open_Issues_Sources.md)。

| 識別 | 同梱する原典 | 本書での主な用途 |
|---|---|---|
| A01 | [01_Architecture](../../../../../30_references/baselines/R8_FIX001/sources/architecture/01_Architecture.md) | 二経路、通常要求、案A優先、認証影響分離境界 |
| A02 | [02_Responsibilities](../../../../../30_references/baselines/R8_FIX001/sources/architecture/02_Responsibilities.md) | レイヤー、責務、正本、権威・workflow owner |
| A03 | [03_Command_Flows](../../../../../30_references/baselines/R8_FIX001/sources/architecture/03_Command_Flows.md) | UC-01〜07、機器結果、再計画、OTA |
| A04 | [04_JET_Isolation](../../../../../30_references/baselines/R8_FIX001/sources/architecture/04_JET_Isolation.md) | 変更・非干渉、先行説明の補正、証跡 |
| A05 | [05_Device_Classes](../../../../../30_references/baselines/R8_FIX001/sources/architecture/05_Device_Classes.md) | 四軸分類、group/PCC、初期機器候補 |
| A06 | [06_Contracts](../../../../../30_references/baselines/R8_FIX001/sources/architecture/06_Contracts.md) | 要求・権威・Capability・結果・期限 |
| A07 | [07_Power_Constraints](../../../../../30_references/baselines/R8_FIX001/sources/architecture/07_Power_Constraints.md) | 電力基準、scope、複数PCS、過渡 |
| A08 | [08_Deployment_Failures_OTA](../../../../../30_references/baselines/R8_FIX001/sources/architecture/08_Deployment_Failures_OTA.md) | 配置案、通信断、共通原因、更新、セキュリティ |
| A09 | [09_Risks_Alternatives](../../../../../30_references/baselines/R8_FIX001/sources/architecture/09_Risks_Alternatives.md) | 制約、非対応、固定APIの限界、外部操作元 |
| A10 | [10_Requirements_Tests](../../../../../30_references/baselines/R8_FIX001/sources/architecture/10_Requirements_Tests.md) | ARCH-001〜024、T01〜T19、検証レベル |
| A11 | [11_Migration_Decisions](../../../../../30_references/baselines/R8_FIX001/sources/architecture/11_Migration_Decisions.md) | DEC、TBD、既存調査の限界、移行 |
| A12 | [12_Sources](../../../../../30_references/baselines/R8_FIX001/sources/architecture/12_Sources.md) | 原典S/P/C、確認範囲・未確認・先行説明補正 |
| CTX | [ユーザー明示接続前提](../../../../../30_references/baselines/R8_FIX001/sources/USER_CONTEXT.md) | RS-485直結PCS、ECHONET Lite他社機器、既存会話の持越し |
| SP | R1で導入したシステム仕様案（R2へ継承） | 追加した台帳方式、SYS-ID、パラメータ表、接続具体化案 |

外部資料のURL・確認箇所は原典A12に保持する。今回独自に最新規格一覧や新しい免除根拠を追加していない。A12にある「未確認」を適用確認済みに変更しない。

<a id="legacy-19-4"></a>
## V-07.4 今回の完了範囲

**移行元：** [R7旧19.4節](../../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/19_Open_Issues_Sources.md)。

今回の完了範囲は、5部の単一MOC、44章への本文再配賦、両機能一覧、役割・構成別冊、OQの担当章再割当、参照・データ整合の文書検査である。実装・実機試験・安全／性能／セキュリティ評価・JET判断は未実施。現行QAはDOCUMENT_QA.mdを参照し、過去のQA記録を今回の結果として使用しない。

<a id="legacy-19-5"></a>
## V-07.5 R2追加の出典・検討状態

**移行元：** [R7旧19.5節](../../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/19_Open_Issues_Sources.md)。

| ID | 資料・用途 | 確定度 |
|---|---|---|
| CTX-R2 | [ユーザーの外部サービス・UI追加要求](../../../../../30_references/baselines/R8_FIX001/sources/USER_CONTEXT_R2.md) | 構成追加は明示。通信・配置・数値詳細は未提示 |
| SP-R2 | システム仕様R2の追加設計案 | 用途別振分け、ローカル自立、認可、設定世代、FW契約等のドラフト |
| EXT-FW-01／02 | [RFC 9019／9124の補助参照](../../../../../30_references/baselines/R8_FIX001/sources/R2_External_References.md) | FW役割・配布物検査の設計参考。採用・適合宣言ではない |

R1の60要求は文言・IDを保持し、新規要求を追加する。原典DECとTBD、R1 SYS-TBDも解決済みにはしない。上位プロトコル、無線方式、ローカル認証、具体内部操作、FW対象領域等をSYS-TBD-012〜023へ追加した。

今回実施する検査は文書・JSON・リンク・ID・原典不変・ZIPの整合性であり、原本JET等の再検証・実装・実機・脆弱性診断・正式承認ではない。

<a id="legacy-19-8"></a>
## V-07.6 R3入力・判断差分（履歴）

**移行元：** [R7旧19.8節](../../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/19_Open_Issues_Sources.md)。

CTX-R3：[二方式の選択要求](../../../../../30_references/baselines/R8_FIX001/sources/USER_CONTEXT_R3.md)。更新基準は[sources/baseline/R2.zip](../../data/input_manifest.json)。原典DEC-004（案Aを基準）を現在方針として再適用せず、[R3判断差分](../../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/appendices/R3_Decision_Changes.md)で二方式選択へ置き換えたことを明示する。原典の判断履歴・未確認の機器／認証事実は保持する。

新しい公開規格の調査は本改訂で実施していない。二方式の機能要求はユーザー明示、名称・scope・排他・切替・確認欄は設計提案である。SYS-TBD-024〜030で対応型式、G実装、切替と登録手続き、適用数値、公開情報、共有scopeを確定する。

SP-R3は今回のシステム仕様具体化案を表す内部根拠IDであり、公開規格の番号ではない。

<a id="legacy-19-9"></a>
## V-07.7 原典優先と確認範囲

**移行元：** [R7旧19.9節](../../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/19_Open_Issues_Sources.md)。

[CTX-R4](../../../../../30_references/baselines/R8_FIX001/sources/USER_CONTEXT_R4.md)が今回の最優先入力。[R3原本](../../data/input_manifest.json)の図と方式選択を修正し、[R4判断差分](../../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/appendices/R4_Decision_Changes.md)へ記録する。SYS-TBD-031〜034でネットワーク媒体・ルータ共有障害・PCS独立取得詳細・多重IF／仮想機器移行を確認する。外部規格調査は行っておらず、既存の引用は以前の確認履歴として保持する。

<a id="legacy-19-10-1"></a>
<a id="slot-r6-19-01"></a>
## V-07.8 上位USDMと双方向トレーサビリティ

**移行元：** [R7旧19.10.1節](../../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/19_Open_Issues_Sources.md)。

**補完項目ID：** `SLOT-R6-19-01`。**対応観点：** C03, C33（[レビューA1](../../../../../30_references/baselines/R8_FIX001/sources/review/R5_Coverage_Review_A1.md)）。

R5の既存原則は保持するが、この項の全対象・具体条件・規範参照は未確定。

**本項に記載する仕様項目：**

- 上位要求ID・理由・優先度・配賦。
- SYS/項目/設計/検証の対応。
- 対象外・承認状態・版。

**本項の完成判定：** USDM→機能→SYS/補完項目→設計→検証の対応を版付きで完成し、未記入を適合扱いしない。

**具体的な不足：** [OQ-R6-19-01](V-07_Trace_Open_Questions.md#oq-r6-19-01)。採用値・参照版・対象外理由は回答後に本項又は版指定の規範別冊へ反映する。

<a id="legacy-19-10-2"></a>
<a id="slot-r6-19-02"></a>
## V-07.9 OQの責任者・期限・決定ゲート

**移行元：** [R7旧19.10.2節](../../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/19_Open_Issues_Sources.md)。

**補完項目ID：** `SLOT-R6-19-02`。**対応観点：** C33（[レビューA1](../../../../../30_references/baselines/R8_FIX001/sources/review/R5_Coverage_Review_A1.md)）。

R5の既存原則は保持するが、この項の全対象・具体条件・規範参照は未確定。

**本項に記載する仕様項目：**

- 担当者と協議相手。
- 実日付/相対ゲート/判断待ち依存。
- 回答・根拠・決定・本文反映・再レビュー。

**本項の完成判定：** OQへ担当・期限・決定者を記入し、回答→根拠確認→承認→本文/台帳/テスト反映の閉鎖手順を合意する。

**具体的な不足：** [OQ-R6-19-02](V-07_Trace_Open_Questions.md#oq-r6-19-02)。採用値・参照版・対象外理由は回答後に本項又は版指定の規範別冊へ反映する。


<a id="slot-r9-imp-01"></a>
## V-07.IMP01 原資料の責任・承認版・対象製品

**管理フロー：** 原本を30_references、抽出・分析を20_work/analysis、草案を20_work/drafts、選択済み文書Baselineを10_canonicalに置く。

**本項の具体化：** 取り込む既存Word/Excelの原資料管理者、承認版、As-Is対象型式・FW・製品リリースは何か。原本が複数版ある場合に誰が適用範囲を確定するか。

**完了条件：** 原資料台帳に実文書・版・承認根拠・型式/期間・閲覧制限を登録し、原本hashと対応させる。

[未確認事項 OQ-R9-IMP-01](#oq-r9-imp-01)。

<a id="slot-r9-imp-02"></a>
## V-07.IMP02 実資料による抽出の対応範囲

**管理フロー：** 原本を30_references、抽出・分析を20_work/analysis、草案を20_work/drafts、選択済み文書Baselineを10_canonicalに置く。

**本項の具体化：** 今回の読み取り器で実資料の図・入れ子表・変更履歴・非表示セル・数式・注記をどこまで拾えるか。旧.doc/.xls、暗号化、独自帳票の変換担当と確認方法は何か。

**完了条件：** 代表原資料を受領してXML断片とOffice表示を対照し、未取得・解釈保留を全件処置する。合成XMLテストを実帳票の完全性証拠にしない。

[未確認事項 OQ-R9-IMP-02](#oq-r9-imp-02)。

<a id="slot-r9-imp-04"></a>
## V-07.IMP04 正式USDM形式と意味の確認

**管理フロー：** 原本を30_references、抽出・分析を20_work/analysis、草案を20_work/drafts、選択済み文書Baselineを10_canonicalに置く。

**本項の具体化：** 正式USDMの交換形式・版は何か。今回のspkgw.usdm-model/v1から外部形式への変換対象はどこまでか。既存仕様にない要求理由を誰が確認するか。

**完了条件：** 正式形式の版・変換規則を承認し、ID/階層/理由/条件/状態/多対多リンクの往復テストを実資料で行う。公式Schema適合を未検証で主張しない。

[未確認事項 OQ-R9-IMP-04](#oq-r9-imp-04)。

<a id="slot-r9-imp-05"></a>
## V-07.IMP05 実環境の公開・権限制御・障害復旧

**管理フロー：** 原本を30_references、抽出・分析を20_work/analysis、草案を20_work/drafts、選択済み文書Baselineを10_canonicalに置く。

**本項の具体化：** Windows11/共有ストレージ/Git運用で、誰がCURRENTを更新し、承認証拠を管理するか。ネットワークファイルシステムと実停電での挙動をどう評価するか。

**完了条件：** 実環境でポインタ更新・旧版保持・ロック復旧・アクセス制御を検証する。今回のLinux上の例外注入をWindows停電試験と読み替えない。

[未確認事項 OQ-R9-IMP-05](#oq-r9-imp-05)。

<a id="open-questions"></a>
## Open Questions — 本ノートの完成に必要な確認

以下が本章で回答を管理する質問。関連台帳は参照ビューであり、承認や数値を二重管理しない。

<a id="oq-r6-19-01"></a>
### OQ-R6-19-01 — 上位USDMと双方向トレーサビリティ

**対象項：** [SLOT-R6-19-01](V-07_Trace_Open_Questions.md#slot-r6-19-01)。状態：**OPEN**。

**質問：** 正式USDMの正本・IDは何か。124件のSYSと今回の補完項目を誰が要求へ対応付け、重複・不足・対象外を承認するか。

**必要資料・完了条件：** USDM→機能→SYS/補完項目→設計→検証の対応を版付きで完成し、未記入を適合扱いしない。

**決定担当：** 未割当（候補：要求責任者・製品承認者）。承認者：未定。

**確定時点：** G0 — 製品スコープ・機能採否・要求Baselineの承認前（提案）。回答期限：未定。

**未解決時の制約：** 「上位USDMと双方向トレーサビリティ」を対象構成の確定保証・実装受入根拠として使用しない。

**関連する既存ID：** SYS-TBD-011。

**回答：** 未記入。**決定記録：** 未記入。

<a id="oq-r6-19-02"></a>
### OQ-R6-19-02 — OQの責任者・期限・決定ゲート

**対象項：** [SLOT-R6-19-02](V-07_Trace_Open_Questions.md#slot-r6-19-02)。状態：**OPEN**。

**質問：** 各OQの実担当者、回答期限、提案G0〜G4の採否と正式レビュー日をどう定めるか。未決のまま許される作業と停止する判断はどこか。

**必要資料・完了条件：** OQへ担当・期限・決定者を記入し、回答→根拠確認→承認→本文/台帳/テスト反映の閉鎖手順を合意する。

**決定担当：** 未割当（候補：PM・要求責任者・各領域担当）。承認者：未定。

**確定時点：** G0 — 製品スコープ・機能採否・要求Baselineの承認前（提案）。回答期限：未定。

**未解決時の制約：** 「OQの責任者・期限・決定ゲート」を対象構成の確定保証・実装受入根拠として使用しない。

**関連する既存ID：** SYS-TBD-011。

**回答：** 未記入。**決定記録：** 未記入。


<a id="oq-r9-imp-01"></a>
### OQ-R9-IMP-01 — 原資料の責任・承認版・対象製品

**対象項：** [SLOT-R9-IMP-01](#slot-r9-imp-01)。状態：**OPEN**。

**質問：** 取り込む既存Word/Excelの原資料管理者、承認版、As-Is対象型式・FW・製品リリースは何か。原本が複数版ある場合に誰が適用範囲を確定するか。

**必要資料・完了条件：** 原資料台帳に実文書・版・承認根拠・型式/期間・閲覧制限を登録し、原本hashと対応させる。

**決定担当：** 未割当（候補：文書管理者・既存製品担当）。承認者：未定。

**確定時点：** IMPORT_PILOT — 実資料の採用又は実運用移行前。回答期限：未定。

**未解決時の制約：** 実資料の採用・正式USDM交換・本番の公開運用を未検証で完了扱いにしない。

**関連する既存ID：** OQ-R6-18-01。

**回答：** 未記入。**決定記録：** 未記入。


<a id="oq-r9-imp-02"></a>
### OQ-R9-IMP-02 — 実資料による抽出の対応範囲

**対象項：** [SLOT-R9-IMP-02](#slot-r9-imp-02)。状態：**OPEN**。

**質問：** 今回の読み取り器で実資料の図・入れ子表・変更履歴・非表示セル・数式・注記をどこまで拾えるか。旧.doc/.xls、暗号化、独自帳票の変換担当と確認方法は何か。

**必要資料・完了条件：** 代表原資料を受領してXML断片とOffice表示を対照し、未取得・解釈保留を全件処置する。合成XMLテストを実帳票の完全性証拠にしない。

**決定担当：** 未割当（候補：原資料担当・抽出担当）。承認者：未定。

**確定時点：** IMPORT_PILOT — 実資料の採用又は実運用移行前。回答期限：未定。

**未解決時の制約：** 実資料の採用・正式USDM交換・本番の公開運用を未検証で完了扱いにしない。

**関連する既存ID：** OQ-R6-19-01。

**回答：** 未記入。**決定記録：** 未記入。


<a id="oq-r9-imp-04"></a>
### OQ-R9-IMP-04 — 正式USDM形式と意味の確認

**対象項：** [SLOT-R9-IMP-04](#slot-r9-imp-04)。状態：**OPEN**。

**質問：** 正式USDMの交換形式・版は何か。今回のspkgw.usdm-model/v1から外部形式への変換対象はどこまでか。既存仕様にない要求理由を誰が確認するか。

**必要資料・完了条件：** 正式形式の版・変換規則を承認し、ID/階層/理由/条件/状態/多対多リンクの往復テストを実資料で行う。公式Schema適合を未検証で主張しない。

**決定担当：** 未割当（候補：要求責任者・USDM担当）。承認者：未定。

**確定時点：** IMPORT_PILOT — 実資料の採用又は実運用移行前。回答期限：未定。

**未解決時の制約：** 実資料の採用・正式USDM交換・本番の公開運用を未検証で完了扱いにしない。

**関連する既存ID：** OQ-R6-19-01。

**回答：** 未記入。**決定記録：** 未記入。


<a id="oq-r9-imp-05"></a>
### OQ-R9-IMP-05 — 実環境の公開・権限制御・障害復旧

**対象項：** [SLOT-R9-IMP-05](#slot-r9-imp-05)。状態：**OPEN**。

**質問：** Windows11/共有ストレージ/Git運用で、誰がCURRENTを更新し、承認証拠を管理するか。ネットワークファイルシステムと実停電での挙動をどう評価するか。

**必要資料・完了条件：** 実環境でポインタ更新・旧版保持・ロック復旧・アクセス制御を検証する。今回のLinux上の例外注入をWindows停電試験と読み替えない。

**決定担当：** 未割当（候補：構成管理・開発基盤担当）。承認者：未定。

**確定時点：** IMPORT_PILOT — 実資料の採用又は実運用移行前。回答期限：未定。

**未解決時の制約：** 実資料の採用・正式USDM交換・本番の公開運用を未検証で完了扱いにしない。

**関連する既存ID：** OQ-R6-19-02。

**回答：** 未記入。**決定記録：** 未記入。
