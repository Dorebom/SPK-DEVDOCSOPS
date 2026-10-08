---
schema: spkgw.governance-note/v1
document_id: STD-GOV-003
project: SPK-GW_HEMS
document_type: STANDARD
revision: 1.1.0
status: DRAFT_FOR_REVIEW
title: TraceID・17工程・成果物／判断のライフサイクル追跡
owner: null
trace_id: TRC-SPKGW-000001
created_on: '2026-10-08'
updated_on: '2026-10-08'
classification: INTERNAL
source_baseline: BL-R9-0001
related_ids: []
---

# TraceID・17工程・成果物／判断のライフサイクル追跡

## 1. TraceIDの定義と適用範囲
**TraceIDは、ある開発目的・機能・課題・改善テーマのライフサイクルを、企画から運用・振り返りまで継続して束ねる安定IDである。** 単発TASK、実行EXE、個別要件SYS、ファイル名、工程番号、製品ランタイムの通信trace_idではない。

ユーザーの17工程は[工程標準](STD_05_Process_Gates.md)と[lifecycle_profile.json](lifecycle_profile.json)で管理する。**工程が変わる、担当が替わる、草案を正本へ採用する、リリースされる、保守へ移る、という理由だけではTraceIDを変更しない。** 全プロジェクトの全機能を1つの巨大なTraceへ押し込めることも避ける。

## 2. IDと版を分ける
| 対象 | 識別 | 規則 |
|---|---|---|
| 継続テーマ | `TRC-SPKGW-*` | 目的・範囲を持つ。工程移行時に再採番しない |
| 作業 | `TASK-*` | 作業状態、担当、工数の正本。1テーマに複数TASK |
| 要求・仕様 | 既存`SYS-*`／USDM／S-FN／GW-FN等 | 既存IDを維持。機能群を要求1件へ強制変換しない |
| 設計・コード・試験等 | 既存成果ID又は新規成果ID | 安定した成果ID＋revision。全ファイルへIDを強制埋込しない |
| 版付き参照 | `node_id` | `artifact_id＋revision`を特定するノード。本文／実体は元の正本に置く |
| 実行・証拠 | `EXE-*`／`EVD-*` | 入力・環境・実行版・結果の証拠。再実行は新ID |
| 会議・調査・議題・決定 | `MTG-*`／`RES-*`／`AGENDA-*`／`DEC-*` | 会議開催、議論、結論、承認、派生作業を同一視しない |
| 変更・障害・改善 | `CHG-*`／既存Issue／改善ID | 元の目的・リリース・導入版へ戻れるようにする |

R10の`control.json.traces`をTraceIDの宣言正本として維持する。新しい`trace_graph.json`は**版付き成果ノード、関係、工程適用計画**の正本であり、要求本文・TASK本文・工数原票を再定義しない。原本・採用済みsnapshotは改変しない。

## 3. 連続性は同じIDだけでは成立しない
```text
企画意図 → 要求分析 → 要求／USDM → システム設計 → アーキテクチャ
 → 構造設計 → 詳細設計 → コード／ビルド
 → 単体・結合・システム・非機能の試験仕様／実行結果
 → 妥当性確認 → リリース準備 → 配布版／導入記録
 → 障害・保守変更 → 振り返り → 改善TASK／次の企画
```
これは**追跡すべき範囲**であり、すべてを直列に実行する指定ではない。テスト設計を先行してよく、工程の反復・並行・差戻しも記録する。試験は直前工程だけでなく、検証する要件・設計・コードへ直接関連付ける。

**TraceIDは集合を探す鍵。型付き関係は何に依存するか。版とhashは何を確認したか。** 三つを組み合わせる。`related_to`と会議の`discusses`だけでは、設計→実装→試験の根拠鎖を満たしたことにしない。

## 4. 関係の向きと意味
すべての依存関係は原則として **下流・依存する項目 → 上流・根拠項目** を向く。

| 関係 | 例 |
|---|---|
| derives_from／refines | 下位要求→原要求、詳細設計→構造設計 |
| allocated_from | GW機能／HW・SW要素要求→全体要求 |
| implements | コードcommit→詳細設計／仕様 |
| verifies | 試験ケース→対象要求／設計／実装 |
| validates | 受入検証→利用者目的・製品要求 |
| result_of | 試験結果→試験ケース／実行、調査結果→調査TASK |
| evidence_for | 証拠→レビュー／判断／対象成果 |
| investigates／discusses | 調査／議題→対象OQ・課題・設計 |
| decides_on／action_from | 決定→対象、派生TASK→決定／会議 |
| includes／deployment_of | リリース→コード／証拠、導入記録→リリース |
| observed_in／fixes | 障害→導入版、修正→障害 |
| supersedes | 新版成果→旧版成果 |

同じTraceに所属するだけで自動的に関係を生成しない。関係そのものにID、根拠、確認状態を持つ。[関係型一覧](lifecycle_profile.json)を正本にする。検査器の双方向探索は、逆向きの関係レコードを二重入力することではない。

## 5. 調査・会議・レビューを工程と分ける
`phase_ids`はP01〜P17の工程、`activity_type`はRESEARCH／MEETING／REVIEW等の作業種別。会議は常に管理工程、調査は常に企画工程、という固定配賦にしない。

例：通信方式調査はP04/P05＋RESEARCH、詳細設計レビューはP07＋REVIEW、性能不具合の対策会議はP12/P16＋MEETING。対象が未定の作業はUNASSIGNEDと理由を残し、都合のよい工程へ自動分類しない。

会議録1件が複数テーマを扱う場合、会議の主`trace_id`と`related_trace_ids`を使う。議題別にAGENDA、決定DEC、未決OQ、派生TASKを元の各テーマへ結ぶ。会議録をテーマ数だけ複製せず、開催・参加記録を要件採用や試験合格とみなさない。

## 6. テーマの分岐・共有・統合・保守
同じ目的の修正・再試行・同一機能の保守は既存Traceを維持し、CHG／TASK／EXEのIDで区別する。新たな独立目的が生じた場合だけ新Traceを作り、`split_from`／`follow_up_to`／`merged_from`で旧Traceへつなぐ。旧TraceのID・所属履歴は消さない。

共通ライブラリや共通試験は1つの版付き成果を複数Traceから参照してよい。多対多関係を理由に複数の成果・費用原票を作らない。保守後は旧版の試験結果を新版合格へ引き継がず、変更対象版に対する影響分析と再評価を残す。

## 7. 版・Baseline・根拠・変更影響
ファイルはworkspace相対path＋sha256＋必要なanchor／JSONポインタ、コードはrepository＋固定commit＋path／symbol＋取得した照合証拠、試験は仕様版＋対象ビルド＋環境＋run＋証拠、導入はrelease＋機器／環境の対応で記録する。`HEAD`、`latest`、題名だけを確定参照にしない。

版が変わる場合は旧nodeを保存し、新しいnodeと関係を作る。`selected`は今回の評価範囲で使う版の指定であって、製品の採用承認ではない。新しい要求版に古い試験版を結び直しただけで確認済みにしない。

本版の`impact`は型付き依存から再レビュー候補を列挙する補助。意味上の影響やJET判断を自動確定しない。単一レジストリのselectedは単一評価scope向けで、並行製品版はscope別の台帳スナップショットで評価する。

## 8. 工程ごとの記録確認
各Traceに17工程の適用表を持つ。APPLICABLE／NOT_APPLICABLE／TBDを区別し、NOT_APPLICABLEは理由と確認者・決定証拠が必要。小変更に全工程の作業を強制せず、影響評価で省略根拠を残す。初期状態は17工程すべてTBDで、勝手に完了・対象外にしない。

各工程には必要成果kind、版付き入力・出力、根拠関係、確認記録を指定する。特に試験仕様と結果を分ける。`PLANNED_ONLY`／`PENDING_REVIEW`／`MISSING`／`TBD`／`LINKED_RECORDS`を区別する。**LINKED_RECORDSは追跡記録の形式的成立であり、製品合格・工程承認・進捗100%を意味しない。**

## 9. 工数・予算・完了と区別する
工数・原価の正本はcontrol.jsonの原票とleaf TASK。複数Traceや複数工程の参照は閲覧用の多対多であり、その数だけ金額・成果ウェイトを足さない。テーマ別配賦が必要なら原票IDを保持した配賦比率を定め、合計1を確認する。本版は多対多配賦の自動金額集計を追加しない。

TASK完了、Trace内の各成果の受入、文書Baseline採用、製品リリース、運用継続は別状態。リリース後もTraceを参照可能にし、運用障害・改善・再企画から遡れるようにする。

## 10. 導入・移行と検査範囲
R10の旧phase列挙を削除せず、互換読出しを残す。`DESIGN`→P06/P07、`VERIFICATION`→P09〜P12等は自動推定しない。新規TASKはphase_idsとactivity_typeを記入する。既存4候補TASKは自動再分類せず、移行未了を警告する。

[Trace操作ガイド](Tool_Traceability.md)のvalidate／report／impactで、参照・版・型・関係・工程記録を確認する。既存govcheckとspecflowも実行する。実タスク・実製品成果の全量移行、権限本人確認、関係の内容妥当性は別作業である。

## Open Questions
[管理OQ](Open_Questions.md)のOQ-GOV-TRACE-01〜04を参照。実テーマの粒度・旧工程対応、機密証拠へのアクセス、コード／試験リポジトリ連携、工程別の実受入条件を具体化する。17工程と調査・会議を追う方針自体は回答済み。
