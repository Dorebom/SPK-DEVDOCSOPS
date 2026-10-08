---
schema: spkgw.governance-note/v1
document_id: STD-GOV-002
project: SPK-GW_HEMS
document_type: STANDARD
revision: 1.2.0
status: DRAFT_FOR_REVIEW
title: FrontMatter・文書IDと項目ID・工程属性
owner: null
document_trace_id: DTR-SPKGW-GOV-000009
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

# FrontMatter・文書IDと項目ID・工程属性

## 1. 文書のヘッダ

UTF-8、LF、先頭YAML FrontMatter1回、キー重複禁止。ID・日付・版・状態は文字列。未確定数値はnullであり0・無制限ではない。

```yaml
schema: "spkgw.governance-note/v1"
document_id: "STD-GOV-003"      # 従来の文書識別子を保持
document_trace_id: "DTR-SPKGW-GOV-000003"
item_trace_ids: []               # 文書が所有する項目のみ。全参照項目は含めない
thread_id: "THR-SPKGW-GOV-000001" # テーマ。文書IDでも項目IDでもない
related_thread_ids: []
trace_contract: "spkgw.lifecycle-tags/v2"
phase_ids: ["SYSDES", "ARCH"]
phase_scope: "CROSS_PHASE"
activity_type: "REVIEW"
revision: "1.2.0"
status: "DRAFT_FOR_REVIEW"
```

これは必須共通属性の一部を示す例。実ノートはproject/document_type/title/owner/created_on/updated_on/classification/source_baseline/related_idsも持つ。正式フィールドは[共通schema](schemas/frontmatter.schema.json)、[Task schema](schemas/task.schema.json)に従う。

## 2. 項目のIDは項目ごとに付ける

1文書に要求1・要求2があれば異なるITR。本文の項目又は構造化データのレコードを、trace_graphのnodeで文書版＋selectorへ結ぶ。1つのFrontMatter.trace_idを全項目に流用しない。

文書の一覧と、要求・設計・コード・試験等の項目一覧は別の索引で管理する。章・別冊への移動、見出し番号の変更だけではITRを変更しない。文書revisionと項目revisionも別であり、新版文書に旧版で不変の項目があってよい。

## 3. TASKとその他のノート

TASKはtask_id=document_id（既存ルール）に加え、文書DTRとTASK項目ITRを持つ。タスク自身のphaseとphase_ids、活動activity_type、状態state、工数・受入条件等は従来どおり保持する。`status`はノートの文書状態、`state`は作業状態であり同一にしない。

会議録DTRの下に議題ITR、調査ノートDTRの下に調査観点・結論ITRを置く。関連SYS/ITRはリンク先であり、会議録がその要件を新規に所有するとはしない。

## 4. 互換と原資料

旧document_idとSYS/OQ等のnative IDは維持する。旧テーマtrace_idはTHRへ移行し、編集ノートではthread_idへ明示改名。製品ランタイムログのtrace_idは対象外。選択済みcanonical、旧Word/Excel・規格原本、履歴へFrontMatterを後付けしない。文書版と項目所在をsidecarで登録する。

旧データのCONTROL.traces及び実行原票trace_idはTHRの互換欄。旧IDはtrace_aliasesの指定型で解決する。DTRとITRを同じものとするfallbackを置かない。テンプレートのID欄はnull/空配列であり実文書へコピーする際に採番する。

## 5. 検査・正本

tracecheckは文書hashと項目selectorを検査。govcheckは共通属性、TASK、認可記録、実績を検査。要件本文はcanonicalの元台帳、項目関係はtrace_graph、集計は生成ビュー。二つの正本を編集して同じ値を手動維持する運用にしない。

## Open Questions

実担当・実成果・運用環境は[管理OQ](Open_Questions.md)で確定する。製品要求・工程完了の承認ではない。
