---
title: "設計判断・未確定事項・出典・レビュー"
document_id: "SPKGW-SYS-R6-19"
revision: "R6"
updated: 2026-10-06
status: DRAFT_FOR_REVIEW
source_baseline: "System_Spec_R5 + Coverage_Review_A1 + CTX-R6"
---

<a id="ch-19"></a>
# 19. 設計判断・未確定事項・出典・レビュー

根拠：[11_Migration_Decisions.md](../sources/architecture/11_Migration_Decisions.md) ／ [12_Sources.md](../sources/architecture/12_Sources.md) ／ [10_Requirements_Tests.md](../sources/architecture/10_Requirements_Tests.md)。ユーザー明示事項・本書の具体化案は本文で区別する。

## 19.1 判断状態の維持

原典DEC-001〜010を[未確定事項・判断台帳](../appendices/Open_Issues.md)へ保持する。命名と非影響構造の目標はユーザー合意・目標であり、案Aの実機成立、別CPU、全機器対応、JET試験免除が承認されたことにはしない。

原典TBD-001〜014もIDを維持する。RS-485役割・IF、既存Device公開、数値保証、未知結果の終端等はSYS-TBD-*へ追加し、原典の未決事項の意味を置き換えない。

## 19.2 レビューの優先順

最初に、RS-485既存経路の役割、対象PCS型式と非迂回、連系点・変換グループ、配置案A／Bの成立条件を確認する。続いて通常権威・workflow owner・プロファイル・時間条件を決める。

本書では担当者名を推測せず、役割単位の確認先と完了条件を示す。未確定パラメータは[Parameter Register](../appendices/Parameter_Register.md)に集約し、レビューで確定値・根拠・適用構成・確認者を記録する。

## 19.3 根拠索引

| 識別 | 同梱する原典 | 本書での主な用途 |
|---|---|---|
| A01 | [01_Architecture](../sources/architecture/01_Architecture.md) | 二経路、通常要求、案A優先、認証影響分離境界 |
| A02 | [02_Responsibilities](../sources/architecture/02_Responsibilities.md) | レイヤー、責務、正本、権威・workflow owner |
| A03 | [03_Command_Flows](../sources/architecture/03_Command_Flows.md) | UC-01〜07、機器結果、再計画、OTA |
| A04 | [04_JET_Isolation](../sources/architecture/04_JET_Isolation.md) | 変更・非干渉、先行説明の補正、証跡 |
| A05 | [05_Device_Classes](../sources/architecture/05_Device_Classes.md) | 四軸分類、group/PCC、初期機器候補 |
| A06 | [06_Contracts](../sources/architecture/06_Contracts.md) | 要求・権威・Capability・結果・期限 |
| A07 | [07_Power_Constraints](../sources/architecture/07_Power_Constraints.md) | 電力基準、scope、複数PCS、過渡 |
| A08 | [08_Deployment_Failures_OTA](../sources/architecture/08_Deployment_Failures_OTA.md) | 配置案、通信断、共通原因、更新、セキュリティ |
| A09 | [09_Risks_Alternatives](../sources/architecture/09_Risks_Alternatives.md) | 制約、非対応、固定APIの限界、外部操作元 |
| A10 | [10_Requirements_Tests](../sources/architecture/10_Requirements_Tests.md) | ARCH-001〜024、T01〜T19、検証レベル |
| A11 | [11_Migration_Decisions](../sources/architecture/11_Migration_Decisions.md) | DEC、TBD、既存調査の限界、移行 |
| A12 | [12_Sources](../sources/architecture/12_Sources.md) | 原典S/P/C、確認範囲・未確認・先行説明補正 |
| CTX | [ユーザー明示接続前提](../sources/USER_CONTEXT.md) | RS-485直結PCS、ECHONET Lite他社機器、既存会話の持越し |
| SP | R1で導入したシステム仕様案（R2へ継承） | 追加した台帳方式、SYS-ID、パラメータ表、接続具体化案 |

外部資料のURL・確認箇所は原典A12に保持する。今回独自に最新規格一覧や新しい免除根拠を追加していない。A12にある「未確認」を適用確認済みに変更しない。

## 19.4 今回の完了範囲

完了対象は、添付に整合するシステム仕様のドラフト作成、RS-485等の前提追加、要求・試験・未確定事項の対応、文書・ZIP整合性の検査である。既存ソフトの修正、実機結合、HIL、JET判断、正式設計承認、元アーキテクチャの更新は実施していない。

分割章とdataの管理用正本を修正した後は、統合ビューと表を再生成する。90_All_In_One.mdは生成ビューであり、入力アーキテクチャの90_All_In_One.mdとは別のシステム仕様書である。

## 19.5 R2追加の出典・検討状態

| ID | 資料・用途 | 確定度 |
|---|---|---|
| CTX-R2 | [ユーザーの外部サービス・UI追加要求](../sources/USER_CONTEXT_R2.md) | 構成追加は明示。通信・配置・数値詳細は未提示 |
| SP-R2 | システム仕様R2の追加設計案 | 用途別振分け、ローカル自立、認可、設定世代、FW契約等のドラフト |
| EXT-FW-01／02 | [RFC 9019／9124の補助参照](../sources/R2_External_References.md) | FW役割・配布物検査の設計参考。採用・適合宣言ではない |

R1の60要求は文言・IDを保持し、新規要求を追加する。原典DECとTBD、R1 SYS-TBDも解決済みにはしない。上位プロトコル、無線方式、ローカル認証、具体内部操作、FW対象領域等をSYS-TBD-012〜023へ追加した。

今回実施する検査は文書・JSON・リンク・ID・原典不変・ZIPの整合性であり、原本JET等の再検証・実装・実機・脆弱性診断・正式承認ではない。


## 19.8 R3入力・判断差分（履歴）

CTX-R3：[二方式の選択要求](../sources/USER_CONTEXT_R3.md)。更新基準は[sources/baseline/R2.zip](../sources/baseline/R2.zip)。原典DEC-004（案Aを基準）を現在方針として再適用せず、[R3判断差分](../appendices/R3_Decision_Changes.md)で二方式選択へ置き換えたことを明示する。原典の判断履歴・未確認の機器／認証事実は保持する。

新しい公開規格の調査は本改訂で実施していない。二方式の機能要求はユーザー明示、名称・scope・排他・切替・確認欄は設計提案である。SYS-TBD-024〜030で対応型式、G実装、切替と登録手続き、適用数値、公開情報、共有scopeを確定する。

SP-R3は今回のシステム仕様具体化案を表す内部根拠IDであり、公開規格の番号ではない。

## 19.9 R4：原典優先と確認範囲

[CTX-R4](../sources/USER_CONTEXT_R4.md)が今回の最優先入力。[R3原本](../sources/baseline/R3.zip)の図と方式選択を修正し、[R4判断差分](../appendices/R4_Decision_Changes.md)へ記録する。SYS-TBD-031〜034でネットワーク媒体・ルータ共有障害・PCS独立取得詳細・多重IF／仮想機器移行を確認する。外部規格調査は行っておらず、既存の引用は以前の確認履歴として保持する。

<!-- R6:COMPLETION_ITEMS -->

> **R6の補完範囲：** 以下はレビューA1から追加した章節項の記入枠であり、数値・機種・機能採否・個別規格適用を推定した確定仕様ではない。各項末のリンクから、本章末尾の具体的な質問・必要資料・確定時点を確認できる。

**記入先・関連する規範候補別冊：** [Open Question横断台帳・既存TBDとの対応](../appendices/Open_Question_Register.md) ／ [網羅性34観点とR6章節項・Open Questionの対応](../appendices/Coverage_Completion_Map.md)

## 19.10 要求属性とOpen Questionの解消管理

<a id="slot-r6-19-01"></a>
### 19.10.1 上位USDMと双方向トレーサビリティ

**補完項目ID：** `SLOT-R6-19-01`。**対応観点：** C03, C33（[レビューA1](../sources/review/R5_Coverage_Review_A1.md)）。

R5の既存原則は保持するが、この項の全対象・具体条件・規範参照は未確定。

**本項に記載する仕様項目：**

- 上位要求ID・理由・優先度・配賦。
- SYS/項目/設計/検証の対応。
- 対象外・承認状態・版。

**本項の完成判定：** USDM→機能→SYS/補完項目→設計→検証の対応を版付きで完成し、未記入を適合扱いしない。

**具体的な不足：** [OQ-R6-19-01](#oq-r6-19-01)。採用値・参照版・対象外理由は回答後に本項又は版指定の規範別冊へ反映する。

<a id="slot-r6-19-02"></a>
### 19.10.2 OQの責任者・期限・決定ゲート

**補完項目ID：** `SLOT-R6-19-02`。**対応観点：** C33（[レビューA1](../sources/review/R5_Coverage_Review_A1.md)）。

R5の既存原則は保持するが、この項の全対象・具体条件・規範参照は未確定。

**本項に記載する仕様項目：**

- 担当者と協議相手。
- 実日付/相対ゲート/判断待ち依存。
- 回答・根拠・決定・本文反映・再レビュー。

**本項の完成判定：** OQへ担当・期限・決定者を記入し、回答→根拠確認→承認→本文/台帳/テスト反映の閉鎖手順を合意する。

**具体的な不足：** [OQ-R6-19-02](#oq-r6-19-02)。採用値・参照版・対象外理由は回答後に本項又は版指定の規範別冊へ反映する。

<a id="slot-r6-19-03"></a>
### 19.10.3 現行仕様と履歴の意味的整合

**補完項目ID：** `SLOT-R6-19-03`。**対応観点：** C03, C34（[レビューA1](../sources/review/R5_Coverage_Review_A1.md)）。

R5の既存原則は保持するが、この項の全対象・具体条件・規範参照は未確定。

**本項に記載する仕様項目：**

- 正本/生成ビュー/履歴の区別。
- 旧構成例・優先順位・用語。
- 変更前後・判断・レビュー範囲。

**本項の完成判定：** 現行章をR5の接続・責務・用語と突合し、差分記録を承認する。リンク検査だけで意味的合格にしない。

**具体的な不足：** [OQ-R6-19-03](#oq-r6-19-03)。採用値・参照版・対象外理由は回答後に本項又は版指定の規範別冊へ反映する。

<!-- R6:OPEN_QUESTIONS -->
<a id="oq-list-chapters-19-open-issues-sources-md"></a>
## Open Questions — 本ノートを完成させるための未決事項

以下は本章の具体的な未決事項。**担当者・回答期限の日付・採用値・承認結果は未確定**である。担当ロールと確定ゲートは提案。回答を得ただけでは閉じず、根拠確認・決定・本文と関連台帳への反映を行う。
全体索引：[Open Question横断台帳](../appendices/Open_Question_Register.md)。各質問の編集正本は[data/completion_items.json](../data/completion_items.json)。

<a id="oq-r6-19-01"></a>
### OQ-R6-19-01 — 上位USDMと双方向トレーサビリティ

**対象項：** [19.10.1 上位USDMと双方向トレーサビリティ](#slot-r6-19-01)

**質問：** 正式USDMの正本・IDは何か。124件のSYSと今回の補完項目を誰が要求へ対応付け、重複・不足・対象外を承認するか。

**必要資料・完了条件：** USDM→機能→SYS/補完項目→設計→検証の対応を版付きで完成し、未記入を適合扱いしない。

**決定担当：** 未割当（候補：要求責任者・製品承認者）。承認者：未定。

**確定時点：** G0＝製品スコープ・機能採否・要求Baselineの承認前（提案）。回答期限の日付：未定。

**未解決時の制約：** 「上位USDMと双方向トレーサビリティ」を対象構成の確定保証・実装受入根拠として使用しない。

**既存ID：** SYS-TBD-011。

**状態：** OPEN。**回答：** 未記入。**決定記録：** 未記入。

<a id="oq-r6-19-02"></a>
### OQ-R6-19-02 — OQの責任者・期限・決定ゲート

**対象項：** [19.10.2 OQの責任者・期限・決定ゲート](#slot-r6-19-02)

**質問：** 各OQの実担当者、回答期限、提案G0〜G4の採否と正式レビュー日をどう定めるか。未決のまま許される作業と停止する判断はどこか。

**必要資料・完了条件：** OQへ担当・期限・決定者を記入し、回答→根拠確認→承認→本文/台帳/テスト反映の閉鎖手順を合意する。

**決定担当：** 未割当（候補：PM・要求責任者・各領域担当）。承認者：未定。

**確定時点：** G0＝製品スコープ・機能採否・要求Baselineの承認前（提案）。回答期限の日付：未定。

**未解決時の制約：** 「OQの責任者・期限・決定ゲート」を対象構成の確定保証・実装受入根拠として使用しない。

**既存ID：** SYS-TBD-011。

**状態：** OPEN。**回答：** 未記入。**決定記録：** 未記入。

<a id="oq-r6-19-03"></a>
### OQ-R6-19-03 — 現行仕様と履歴の意味的整合

**対象項：** [19.10.3 現行仕様と履歴の意味的整合](#slot-r6-19-03)

**質問：** 第4.5節の明示補正以外に、履歴由来の構成・用語・保証が現行方針と競合していないか。誰が意味的整合レビューを完了判定するか。

**必要資料・完了条件：** 現行章をR5の接続・責務・用語と突合し、差分記録を承認する。リンク検査だけで意味的合格にしない。

**決定担当：** 未割当（候補：システム設計・レビュー担当）。承認者：未定。

**確定時点：** G1＝該当するアーキテクチャ・HW・安全境界の設計固定前（提案）。回答期限の日付：未定。

**未解決時の制約：** 「現行仕様と履歴の意味的整合」を対象構成の確定保証・実装受入根拠として使用しない。

**既存ID：** 該当ID未付与。A1の補完指摘から追加した具体化項目。

**状態：** OPEN。**回答：** 未記入。**決定記録：** 未記入。
