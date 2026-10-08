---
title: "全体責務配分・電力制約・保護"
document_id: "SPKGW-SYS-I-07"
revision: "R8"
updated: 2026-10-07
status: DRAFT_FOR_REVIEW
part: "I"
---

<a id="i-07"></a>
# I-07 全体責務配分・電力制約・保護

[全体MOCへ](../../00_MOC.md#part-i)

**本章の対象：** 全体の責任境界、出力制御と保護、連系点・変換グループ・計測範囲。

**記載区分：** 既存R7の有効な記述とR6補完項を再配置。章構成・読み分けの案以外に、新しい実装・権限・数値・適合を確定していない。旧版に由来する具体値や規格参照は当時の確認範囲を引き継ぐ。

## 本章の責務と他章との境界

通常運転要求の調停、遠隔出力制御のスケジュール適用、PCS等の系統連系保護を別責務にする。GW内H/G、PCS内、外部サービスという実装配賦は、この全体契約の実現先である。認証範囲は筐体や章の境界だけでは決まらない。

連系点・変換グループの全体制約と、個別PCSへの命令を区別する。必要な機器・計測・強制経路は構成ごとに確認し、H側の最適化だけを全体適合の唯一の根拠にしない。


<a id="legacy-2-4"></a>
## I-07.1 独立する制御責務

**移行元：** [R7旧2.4節](../../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/02_System_Context.md)。

| 経路 | 適用責務 | H側の役割 |
|---|---|---|
| 通常運転 | 受付 → 必要ならEMS → Arbiter → Orchestrator → DPC/FLC → Adapter／固定通常受付 | 制御要求・結果・観測 |
| EL接続PCSの出力制御 | PCS内の取得・時刻・保存・適用 → 機器制約 | 読取可能情報だけを参照。代理取得・適用しない |
| RS-485接続PCSの出力制御 | GW G側の取得・管理・適用 → RS-485 → PCS | 固定された通常要求・読取コピーだけ |
| 系統連系保護 | 必要な独立計測 → 機器側保護・解列・規定復帰 | 保護の承認を行わない |

<a id="legacy-10-1"></a>
## I-07.2 本章の適用範囲

**移行元：** [R7旧10.1節](../../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/10_Grid_Protection.md)。

本章は二方式共通の出力制御契約を定義する。PCS_DIRECTではPCS内の出力制御機能への依存仕様、GW_MANAGEDではGWのG側の取得・保存・時刻管理・適用・PCS指示への実装要求へ配賦する。PCS保護は両方式で独立する。GW_MANAGEDは単なるスケジュールの透過中継ではない。標準H側のArbiter／Orchestratorを出力制御の成立経路にしない。

数値・認証適用は添付の公開資料確認を引き継ぐが、今回原本を再確認していない。対象一般送配電事業者、契約、伝送仕様、機器・試験プロファイルの適用値を確定するまで、周期、出力変化条件、停止時間等を決め打ちしない。

<a id="legacy-10-3"></a>
## I-07.3 最終制約と保護

**移行元：** [R7旧10.3節](../../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/10_Grid_Protection.md)。

機器側運転制御は通常要求と系統・機器制約を整合し、許容される運転を実行する。系統連系保護は必要な独立計測に基づき、HEMSの計画計算、Arbiter許可、クラウド応答を待たずに動作する。

保護の停止・解列と遠隔出力制御のスケジュール実行は、評価する時間条件・状態遷移を別に定義する。再連系や保護復帰を通常モードAPIで強制解除できる形にしない。

<a id="legacy-10-6"></a>
## I-07.4 配置によって変わる正本と責任

**移行元：** [R7旧10.6節](../../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/10_Grid_Protection.md)。

| 責務 | PCS_DIRECT | GW_MANAGED |
|---|---|---|
| サーバ接続・対象確認 | PCS内の出力制御機能 | GWのG側 |
| スケジュール正本・履歴・時刻 | PCS側 | GWのG側 |
| スケジュールから適用制約を決定 | PCS側 | GWのG側 |
| PCSへの制約・指令の適用 | PCS内部経路 | GW G側→確認済みPCS接続経路 |
| 機器状態・実出力の監視 | PCS内、公開情報をGWで参照 | 必要監視はG側で維持、H側へコピー |
| 通常エネマネ・上位／UI操作 | GW H側 | GW H側 |
| 電気的な保護・解列等 | PCS等の確認対象保護機能 | PCS等の確認対象保護機能 |

GW_MANAGEDでGWが算出するのは採用プロファイルの制約／指令であり、PCSの高速制御・保護をLinux HEMSへ移す意味ではない。設定値ACKだけで実出力適合としない。複数PCSに対する配分が必要ならG側の責務としてscope・容量根拠・過渡条件を定義する。

独立性の主張対象はH側の停止・更新である。GW全体喪失時にGWのG側が動き続けるとは主張せず、PCS側の必須通信断時動作と復帰を確認する。[第21章](I-05_Configurations.md#i-05)の選択・切替・障害表を適用する。

<a id="legacy-10-7"></a>
## I-07.5 宅内ルータ必須と対象限定

**移行元：** [R7旧10.7節](../../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/10_Grid_Protection.md)。

全取得要求・応答は宅内ルータ経由。PCS_DIRECTはEL接続PCSの自律取得、GW_MANAGEDはRS-485接続PCSのGW取得・管理である。ルータはスケジュール保存・適用を担わない。上位サーバ不通、WAN断、ルータ全停止、LAN片側断、RS-485必須断を区別し、保存情報の期限・時刻・必要計測に従って同じ方式の規定動作を続ける。

<a id="legacy-10-8-2"></a>
<a id="slot-r6-10-02"></a>
## I-07.6 通常API非迂回・保護・復帰の確認

**移行元：** [R7旧10.8.2節](../../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/10_Grid_Protection.md)。

**補完項目ID：** `SLOT-R6-10-02`。**対応観点：** C17, C26（[レビューA1](../../../../../30_references/baselines/R8_FIX001/sources/review/R5_Coverage_Review_A1.md)）。

R5の既存原則は保持するが、この項の全対象・具体条件・規範参照は未確定。

**本項に記載する仕様項目：**

- 許可通常モードと禁止操作。
- 制約強制・独立計測・保護の主体。
- H停止/G停止/WAN断時の成立条件。

**本項の完成判定：** メーカー説明・機能分担・許可操作・適用評価の記録をそろえ、必要な受入条件を[旧17章の再配置先](../../appendices/Chapter_Migration_Map.md#old-ch-17)へ配賦する。

**具体的な不足：** [OQ-R6-10-02](I-07_Responsibilities_Constraints.md#oq-r6-10-02)。採用値・参照版・対象外理由は回答後に本項又は版指定の規範別冊へ反映する。

<a id="legacy-11-1"></a>
## I-07.7 制約のscope

**移行元：** [R7旧11.1節](../../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/11_Power_Constraints.md)。

添付の電力モデルを継承する。以下は設計・計画のモデルであり、接続契約や機器試験の代替ではない。

| scope | 対象 |
|---|---|
| RESOURCE | 特定蓄電池等の操作・状態依存の能力範囲 |
| CONVERSION_GROUP | Hybrid PCSの共通AC容量、同時動作、排他モード |
| CONNECTION_POINT | 住宅・発電所の連系点における電力等 |
| PROTECTION_DOMAIN | 保護停止・解列が作用する設備範囲 |

各制約にquantity、単位・符号、scope、容量基準、有効時間、enforcement_ownerを持たせる。未知の分母を機器定格で置換せず、すべてを「抑制率×PCS定格」に正規化しない。

<a id="legacy-11-2"></a>
## I-07.8 電力収支

**移行元：** [R7旧11.2節](../../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/11_Power_Constraints.md)。

同じAC基準点へそろえ、DERからACバスへ出る電力を正、蓄電池・V2Hの充電を負、負荷消費を正の大きさとする。

$$
p_{\mathrm{PCC}}(t)=\sum_{i\in\mathcal D}p_i(t)-p_{\mathrm{load}}(t)
$$

$$
p_{\mathrm{export}}=\max(p_{\mathrm{PCC}},0),\qquad
p_{\mathrm{import}}=\max(-p_{\mathrm{PCC}},0)
$$

集合Dは重複しない実電力経路に対応付ける。同じHybrid PCSのPV、蓄電池、PCS総出力を同時加算しない。AC/DCや損失の基準が異なる場合、変換の根拠と品質を明示する。RS-485とECHONET Liteの取得値であることより、計測範囲が重要である。

<a id="legacy-11-3"></a>
## I-07.9 機器能力と計画制約

**移行元：** [R7旧11.3節](../../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/11_Power_Constraints.md)。

$$
p_i^{\min}(x_i)\le p_i\le p_i^{\max}(x_i),\qquad
p_i^2+q_i^2\le S_i^2
$$

$$
-\bar p_{\mathrm{import}}\le p_{\mathrm{PCC}}\le\bar p_{\mathrm{export}}
$$

Qを操作できない機器ではQを自由な制御変数にしない。SoC、温度、接続、運転モード、共通変換容量等を条件として扱う。同じ量・同じscopeの上限制約以外を一つのminに押し込めない。

<a id="legacy-11-4"></a>
## I-07.10 複数メーカー・複数PCS

**移行元：** [R7旧11.4節](../../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/11_Power_Constraints.md)。

複数PCSが同一連系点の制約を共有する場合、どの機器又はサイト装置が独立計測と強制経路を持つかを特定する。各PCSに同じ上限を設定するだけで合計上限を満たすとはしない。

全体制約を強制できない構成では、確認済みサイト制御の導入、適用方式が認める保守的な上限配分、組合せをサポート外とする方法を比較する。いずれを採るかは未確定。HEMS計画や負荷継続にだけ依存する案を、本分離目標の成立構成として採用しない。

<a id="legacy-11-5"></a>
## I-07.11 過渡と評価

**移行元：** [R7旧11.5節](../../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/11_Power_Constraints.md)。

測定、通信、設定、物理応答、出力変化条件に遅延がある。すべての瞬間で厳密な静的上限を維持すると断定せず、適用プロファイルPiの評価窓・応答・許容差・異常時動作に対して適合を判定する。

$$
\operatorname{Conforms}_{\Pi}
\bigl(p_{\mathrm{PCC}}(\cdot),u_{\mathrm{grid}}(\cdot),x(\cdot)\bigr)
$$

計画余裕mを使う場合も値と根拠は未確定である。余裕だけで負荷遮断やEV離脱への適合を保証しない。保護動作の時間条件へ遠隔出力制御用のランプ条件を流用しない。

<a id="legacy-11-6"></a>
## I-07.12 混在する取得主体と共有連系点

**移行元：** [R7旧11.6節](../../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/11_Power_Constraints.md)。

同一宅内ルータ上のEL自律取得PCSと、RS-485を介するGW管理PCSが共通連系点を持つ場合も、ルータやH側EMSを合算制約の唯一の強制主体にしない。対象scope・容量分配・最終強制の成立を機器別に確認し、未成立な混在を製品対応済みとしない。

<a id="legacy-11-7-1"></a>
<a id="slot-r6-11-01"></a>
## I-07.13 基準点・容量・変換グループの対応

**移行元：** [R7旧11.7.1節](../../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/11_Power_Constraints.md)。

**補完項目ID：** `SLOT-R6-11-01`。**対応観点：** C14, C17（[レビューA1](../../../../../30_references/baselines/R8_FIX001/sources/review/R5_Coverage_Review_A1.md)）。

R5の既存原則は保持するが、この項の全対象・具体条件・規範参照は未確定。

**本項に記載する仕様項目：**

- 物理配線・計測点・AC/DC。
- 機器定格/契約容量/PCS共用容量。
- 量・符号・scope・損失。

**本項の完成判定：** 配線図、制約表、データ辞書を同じ資源ID・基準点で突合し、合算/非合算の対象を確定する。

**具体的な不足：** [OQ-R6-11-01](I-07_Responsibilities_Constraints.md#oq-r6-11-01)。採用値・参照版・対象外理由は回答後に本項又は版指定の規範別冊へ反映する。

<a id="legacy-11-7-2"></a>
<a id="slot-r6-11-02"></a>
## I-07.14 混在設備・過渡・実出力の合否

**移行元：** [R7旧11.7.2節](../../../../../30_references/baselines/R8_FIX001/sources/r7_snapshot/chapters/11_Power_Constraints.md)。

**補完項目ID：** `SLOT-R6-11-02`。**対応観点：** C17, C22, C32（[レビューA1](../../../../../30_references/baselines/R8_FIX001/sources/review/R5_Coverage_Review_A1.md)）。

R5の既存原則は保持するが、この項の全対象・具体条件・規範参照は未確定。

**本項に記載する仕様項目：**

- 複数PCS・取得主体・連系点全体。
- 負荷離脱・通信遅延・応動。
- 許容差・評価窓・独立強制。

**本項の完成判定：** 混在構成の成立/非対応表、過渡評価プロファイル、必要な計測・強制経路を確定する。

**具体的な不足：** [OQ-R6-11-02](I-07_Responsibilities_Constraints.md#oq-r6-11-02)。採用値・参照版・対象外理由は回答後に本項又は版指定の規範別冊へ反映する。


<a id="open-questions"></a>
## Open Questions — 本ノートの完成に必要な確認

以下が本章で回答を管理する質問。関連台帳は参照ビューであり、承認や数値を二重管理しない。

<a id="oq-r6-10-02"></a>
### OQ-R6-10-02 — 通常API非迂回・保護・復帰の確認

**対象項：** [SLOT-R6-10-02](I-07_Responsibilities_Constraints.md#slot-r6-10-02)。状態：**OPEN**。

**質問：** 対象PCSの通常操作で出力制約や保護を上書きできない根拠は何か。独立計測・保護復帰・必要通信を誰が担い、H停止時に何を維持するか。

**必要資料・完了条件：** メーカー説明・機能分担・許可操作・適用評価の記録をそろえ、必要な受入条件を[旧17章の再配置先](../../appendices/Chapter_Migration_Map.md#old-ch-17)へ配賦する。

**決定担当：** 未割当（候補：PCSメーカー・G側・安全設計）。承認者：未定。

**確定時点：** G1 — 該当する構造・HW・安全・セキュリティ境界の設計固定前（提案）。回答期限：未定。

**未解決時の制約：** 「通常API非迂回・保護・復帰の確認」を対象構成の確定保証・実装受入根拠として使用しない。

**関連する既存ID：** TBD-002, TBD-006, SYS-TBD-003, PAR-GRID-03, PAR-GSEL-03。

**回答：** 未記入。**決定記録：** 未記入。

<a id="oq-r6-11-01"></a>
### OQ-R6-11-01 — 基準点・容量・変換グループの対応

**対象項：** [SLOT-R6-11-01](I-07_Responsibilities_Constraints.md#slot-r6-11-01)。状態：**OPEN**。

**質問：** 制約と計測の基準点はどこか。PV/蓄電池/Hybrid PCSの共有容量と契約容量をどの配線図・機器仕様へ対応付けるか。

**必要資料・完了条件：** 配線図、制約表、データ辞書を同じ資源ID・基準点で突合し、合算/非合算の対象を確定する。

**決定担当：** 未割当（候補：電力・計測・施工設計）。承認者：未定。

**確定時点：** G1 — 該当する構造・HW・安全・セキュリティ境界の設計固定前（提案）。回答期限：未定。

**未解決時の制約：** 「基準点・容量・変換グループの対応」を対象構成の確定保証・実装受入根拠として使用しない。

**関連する既存ID：** TBD-003, TBD-006, PAR-GRID-05。

**回答：** 未記入。**決定記録：** 未記入。

<a id="oq-r6-11-02"></a>
### OQ-R6-11-02 — 混在設備・過渡・実出力の合否

**対象項：** [SLOT-R6-11-02](I-07_Responsibilities_Constraints.md#slot-r6-11-02)。状態：**OPEN**。

**質問：** 異なる取得主体のPCSが同じ連系点にある場合、誰が全体制約を強制するか。負荷急変時に使う評価窓・許容差・応答条件と対応外組合せは何か。

**必要資料・完了条件：** 混在構成の成立/非対応表、過渡評価プロファイル、必要な計測・強制経路を確定する。

**決定担当：** 未割当（候補：電力制御・PCSメーカー・評価担当）。承認者：未定。

**確定時点：** G3 — 該当する受入／適合性評価の実施前（提案）。回答期限：未定。

**未解決時の制約：** 「混在設備・過渡・実出力の合否」を対象構成の確定保証・実装受入根拠として使用しない。

**関連する既存ID：** SYS-TBD-030, TBD-005, PAR-GRID-04。

**回答：** 未記入。**決定記録：** 未記入。
