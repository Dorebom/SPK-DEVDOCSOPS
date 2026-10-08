---
schema: spkgw.governance-note/v1
document_id: STD-GOV-003
project: SPK-GW_HEMS
document_type: STANDARD
revision: 1.2.0
status: DRAFT_FOR_REVIEW
title: 文書TraceID・項目TraceID・工程略称・版付き追跡
owner: null
document_trace_id: DTR-SPKGW-GOV-000010
item_trace_ids: []
thread_id: THR-SPKGW-GOV-000001
related_thread_ids: []
trace_contract: spkgw.lifecycle-tags/v2
phase_ids: []
phase_scope: UNASSIGNED
activity_type: UNSPECIFIED
created_on: '2026-10-08'
updated_on: '2026-10-08'
classification: INTERNAL
source_baseline: BL-R9-0001
related_ids: []
---

# 文書TraceID・項目TraceID・工程略称・版付き追跡

## 1. 今回の区別

**文書を追うDocument TraceIDと、開発工程の個別項目を追うItem TraceIDを別の名前空間とする。** R11の「同じテーマに同じtrace_idを付ける」だけの方式を、項目の追跡として使わない。

| 単位 | 属性 | 命名例 | 何を識別するか |
|---|---|---|---|
| 文書 | `document_trace_id` | `DTR-SPKGW-SPEC-000001` | 一冊の仕様書、一つの独立MD、会議録、Word/Excel原本等の論理的文書 |
| 項目 | `item_trace_id` | `ITR-SPKGW-REQ-000001` | 一つの要求、設計判断、関数の実装、試験ケース、会議議題、規格条項等 |
| テーマ（任意） | `thread_id` | `THR-SPKGW-GOV-000001` | 複数項目を束ねる開発目的。文書／項目IDの代わりにしない |
| 既存識別子 | `document_id` / `native_ids` | `STD-GOV-003`、`SYS-RESP-001` | 原文・既存台帳の番号。保持して新Traceへ対応付ける |
| 版付き位置 | `document_version_id` / `node_id` | `DTR-…_V_1_2_0` / `ITR-…_V_1` | 比較・根拠・証拠が指す特定版 |

DTR=Document Trace、ITR=Item Trace、THR=Thread。文書状態と項目の状態、レビュー・承認・試験実施は独立。文書を承認しても、その文書に掲載した未実施試験がPASSになったとは扱わない。

## 2. 命名規則

`DTR-SPKGW-<文書種別>-<6桁連番>`、`ITR-SPKGW-<項目種別>-<6桁連番>`、`THR-SPKGW-<テーマ略称>-<6桁連番>`とする。英大文字・数字・ハイフンを使い、連番は名前空間内で一意に採番する。番号は通し順であり工程順ではない。タイトル、ファイル名、章番号をIDへ含めない。

文書種別はGOV／SPEC／REGISTER／REFERENCE／TASK／TEMPLATE／CODE等。項目種別は次の例から選び、種別辞書を変更管理する。

| 対象項目 | コード例 |
|---|---|
| 企画目的・要求分析・要求 | CONCEPT / REQAN / REQ |
| システム・アーキテクチャ・構造・詳細設計 | SYSDES / ARCH / BASIC / DETAIL |
| 関数・コード変更単位 | CODE |
| 単体・結合・機能・非機能試験ケース | UT / IT / ST / NFT |
| 段階未確定の既存試験 | TEST（試験レベルは未割当のまま） |
| 実行結果・妥当性確認 | RESULT / VALID |
| リリース準備・配布・導入 | RELPREP / RELEASE / DEPLOY |
| 運用事象・障害・改善 | OPS / INCIDENT / IMPROVE |
| 調査観点・会議議題・決定・原資料条項 | RES / AGENDA / DEC / REF |
| 作業・機能群・未決質問 | TASK / SFUNC / GFUNC / QUESTION |

**種別接頭辞は採番時の識別であり、「現在どの工程で使われているか」は`phase_ids`で持つ。** REQ項目を実装・試験・保守で参照してもCODEやTESTへ改名しない。要求とそれを実現する設計・コード・試験はそれぞれ別ITRで結ぶ。

同じ意味の項目を別のMDへ移してもITRを維持する。文書の分割／統合は新DTRと旧文書の関係、項目の分割／統合は新ITRと旧項目のrefines/derives_from等を明示する。異なる項目に旧IDを再利用しない。

## 3. 文書と項目の関係

```text
DTR: 要求仕様書 @版A
  ├─ ITR: 要求1 @版1
  └─ ITR: 要求2 @版1

DTR: アーキテクチャ設計書 @版B
  └─ ITR: 設計1 @版2 ──refines──→ ITR: 要求1 @版1

DTR: コードファイル（又はコード索引）@固定commit
  └─ ITR: 実装1 @commit ──implements──→ ITR: 設計1 @版2

DTR: 単体試験仕様書 @版C
  └─ ITR: UTケース1 @版1 ──verifies──→ ITR: 要求1／実装1

DTR: 実行記録 @run
  └─ ITR: 試験結果1 @run ──result_of──→ ITR: UTケース1 @版1
```

文書レベルのreferences/generated_from/supersedesは`document_edges`、技術項目の関係は`edges`へ記録する。文書同士のリンクを項目間の実装・検証リンクへ自動展開しない。同じ文書内の項目でも実装先・試験先は異なり得る。

同じ項目を本編・別冊・生成ビューに表示する場合、ITRを複製しない。主記載位置を`document_version_id＋locator`、生成表示等を`occurrences`で指定する。記載場所の関係と技術的な依存は別である。

## 4. 17工程は読める略称を使う

工程の定義は[工程標準](STD_05_Process_Gates.md)の一覧を正本とする。P番号は表示順だけに残し、現行の`phase`／`phase_ids`／`phase_plan.phase_id`では使わない。旧P番号は[別名表](trace_aliases.json)で検索・移行できる。既存の曖昧なDESIGN、VERIFICATION、MANAGEMENTは一意に推測せずUNASSIGNEDとする。

**工程の順番はIDではない。工程の並行・反復・省略の根拠管理はR11から維持する。** 少量修正に17工程の実行を強制しない。

## 5. References・Word/Excel・規格・コード

原本は30_referencesで不変保存し、DTRを外付けの文書台帳へ登録する。原本にFrontMatterや新IDを書き込んでhashを変えない。A01等のsource_idはDTRと版の対応に残す。

Wordの表・段落、Excelのシート・セル・注記、規格条項を個別に扱うならITR-…-REFを付ける。DTR＋原本hash＋抽出run/fragment＋位置を結ぶ。条項に書かれた理由とAIの解釈は別記録。**原資料の一冊全体を引用したことと、特定要求の根拠条項を確定したことは別。** 本版の自動移行は原本単位の引用までで、未読のOffice条項を生成しない。

コード項目はrepository＋固定commit＋path＋symbol等をローカルな照合記録へ保持する。branch名/HEAD/latestだけでは固定参照にしない。本ツールのselector実検査はexplicit HTML anchor／JSON pointer。Office・Gitの細粒度位置はR9抽出結果又はローカル証拠JSONへ橋渡しする。外部Gitの自動fetchや実装コードへの一括コメント挿入は行わない。

## 6. 関係型・版・証拠

ITR間は下流→根拠の向きでderives_from/refines/allocated_from/implements/verifies/validates/result_of等を使う。議題はdiscusses、調査はinvestigates、決定はdecides_on、原文引用はcites。関係にも根拠・確認状態・対象版を持たせる。会議開催や文書の存在を実装・検証完了に換算しない。

改訂時は同一ITRの新revision/new nodeを作り、旧nodeと証拠を保持する。文書移動・改訂でITRは変えないが、旧版試験の結果を新版へ無審査で転用しない。`review.subject_sha256`は項目/関係の内容に結び付く。hashの更新だけはレビュー承認ではない。

## 7. R11からの移行

旧`TRC-SPKGW-000001`は文書でも工程項目でもなくガバナンス導入テーマだったため、`THR-SPKGW-GOV-000001`へ移行する。1つの旧TRCを1つの文書ITRへ勝手に変換せず、各文書にDTR、各既存要求・機能・試験・質問・TASKにITRを割り当てる。

現行の管理ノートはFrontMatterを変更。選択済みBL-R9-0001、Word/Excel原本、履歴は変更せず、sidecarで登録する。SYS等の既存IDは保持し、[移行索引](../20_work/analysis/project/reports/TRACE_ITEMS.md)から新ITRと原文を往復できる。

`control.json.traces`／実行記録の旧`trace_id`は互換フィールド名として当面残すが、その値はTHR（テーマ）のみ。現行ノートは`thread_id`を使う。R9の製品ランタイムtrace_id、SYS/USDMのtrace_linksは別契約であり、一括文字置換しない。

## 8. 範囲と未確定

現存資料からのID付与と既存の明示リンク移行は行うが、未作成の詳細設計・コード・実行結果を捏造しない。SYSのREQSPECへの分類は文書整理案、テストのUT/IT/ST/NFT配賦が未確認なら空欄。テーマ・工程の未割当、根拠レビュー未了はレポートへ出す。

## Open Questions

識別の2層化と可読工程は本版に反映。残る実担当・細粒度抽出・既存試験のレベル・実コード/commitの対応は[管理OQ](Open_Questions.md)のOQ-GOV-TRACE-01〜04で管理する。文書・項目登録を工程完了・権限承認・製品合格としない。
