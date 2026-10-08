---
schema: spkgw.governance-note/v1
document_id: STD-GOV-002
project: SPK-GW_HEMS
document_type: STANDARD
revision: 1.1.0
status: DRAFT_FOR_REVIEW
title: FrontMatter・ノート属性・編集規則
owner: null
trace_id: TRC-SPKGW-000001
created_on: '2026-10-08'
updated_on: '2026-10-08'
classification: INTERNAL
source_baseline: BL-R9-0001
related_ids: []
---

# FrontMatter・ノート属性・編集規則

## 1. 新規ノートの共通ヘッダ
YAML FrontMatterをファイル先頭に1回だけ置く。UTF-8、LF、キー重複禁止。YAMLの暗黙型を避け、日付・ID・状態・版は引用付き文字列として保存する。数値未確認はnullであり、0や空文字にしない。
```yaml
schema: spkgw.governance-note/v1
document_id: TASK-SPKGW-000001
project: SPK-GW_HEMS
document_type: TASK
revision: 1.0.0
status: DRAFT_FOR_REVIEW
title: 原資料の対象版を確認する
owner: null
trace_id: TRC-SPKGW-000001
created_on: "2026-10-08"
updated_on: "2026-10-08"
classification: INTERNAL
source_baseline: BL-R9-0001
related_ids: []
```
| キー | 意味・規則 |
|---|---|
| schema | FrontMatterの構造版。文書revisionと別 |
| document_id | ノート不変ID。ファイル名や章番号で再採番しない |
| document_type | STANDARD/MOC/TEMPLATE/TASK/PLAN/RISK/CHANGE/DECISION/REPORT/RUN/BUDGET/EVIDENCE |
| status | 文書の審査状態。DRAFT_FOR_REVIEW/IN_REVIEW/APPROVED/SUPERSEDED/WITHDRAWN/TEMPLATE/GENERATED |
| owner | Actor ID又はnull。人物名の文字列だけで権限付与しない |
| trace_id | 作業連鎖の主相関ID。要件IDや通信ランタイムIDとは別 |
| source_baseline | 作業を開始した文書Baseline ID。作業中に自動で最新版へ置換しない |
| related_ids | 関連STD・要求・IF・OQ等。不明IDを捏造しない |
| created_on / updated_on | ISO日付文字列。実行時刻は実行記録にタイムゾーン付きで記す |
| classification | PUBLIC/INTERNAL/CONFIDENTIAL/RESTRICTED。実アクセス制御を併用 |
ノートstatus=APPROVEDとタスクstate=DONEは独立。新規作成日は作成日であって、過去の作業開始日時を推定して埋めない。

## 2. TASK固有項目
TASKはtask_id=document_id、state、kind、phase、priority、wbs_id、milestone_id、parent_task_id、depends_on、assignees、reviewers、linked_ids、artifacts、acceptance_criteria、estimate_hours、remaining_hours、forecast_finish、baseline_plan_id、approval_refs、run_ids、evidence_ids、acceptanceを持つ。具体値と列挙は [Taskテンプレート](templates/Task.md) と [スキーマ](schemas/task.schema.json) を正本とする。
工数実績、金額実績、承認済み予算はヘッダへ複製しない。control.jsonのIDを参照する。FrontMatterの属性を変えたらrevision・updated_onと変更理由を更新する。

## 3. 記述本文の共通要素
目的／背景、範囲内・範囲外、入力と版、実施内容、完了条件、成果物、検証結果、リスク、残作業、Open Questionsを分ける。予定・結果・推測を混ぜない。ログ貼付けだけで要求や結論の根拠を省略しない。

## 4. 既存文書との互換
R9のcanonical_ownership.json、既存document_id、SYS-*、OQ-*、run_id、trace_links.jsonは維持する。新FrontMatterは管理ノートへ適用し、選択済みBL-R9-0001へ一括付与しない。00_governanceの既存4ノートはlegacy_documents.jsonで移行対象を識別し、未改版のまま参照可能にする。生成ビューへの追記は禁止。旧Word/Excel原本や30_referencesの歴史資料へFrontMatterを付けて原本hashを壊さない。

## 5. 検査と移行
新規STD、テンプレート、TASKはgovcheckの対象。テンプレートは値未記入を認めるが、コピー後の実TASKは状態に応じて必須を強める。全旧製品文書を検査対象へ追加する時は、除外根拠・対応表・移行タスクを明示する。

## 6. R11：工程横断Traceの追加属性
既存`trace_id`は主テーマのIDとして継承する。新規TASK・会議・調査ノートは`trace_contract: spkgw.lifecycle-tags/v1`を付け、次を記す。全原資料や選択済み正本へ一括追記しない。

```yaml
trace_contract: "spkgw.lifecycle-tags/v1"
trace_id: "TRC-SPKGW-000001"
related_trace_ids: []
phase: "P04"
phase_ids: ["P04", "P05"]
phase_scope: "CROSS_PHASE"
activity_type: "RESEARCH"
```

主trace_idを関連リストへ重複登録しない。phaseは主工程又はUNASSIGNED/CROSS_CUTTING、phase_idsは関係する17工程、phase_scopeはPHASE_SPECIFIC/CROSS_PHASE/UNASSIGNED。P番号を使った主工程はphase_idsにも含める。未割当のPROPOSEDは空phase_idsを許すが、そのまま新規契約のTASKをREADY以降へ進めない。会議・調査のphase_idsとactivity_typeは別分類。

文書全体の所属に加え、複数議題・複数要求を含む文書は版付きnodeと関係で細分化する。FrontMatterのrelated_idsは索引であり、正式なderives_from/verifies等の型付き関係を代替しない。

## Open Questions

担当・実予算・承認閾値・運用環境の未決は [GOV Open Questions](Open_Questions.md) を参照する。本文の運用案は、未確定の製品仕様や支出の承認を代行しない。
