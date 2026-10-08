---
schema: spkgw.governance-note/v1
document_id: STD-GOV-003
project: SPK-GW_HEMS
document_type: STANDARD
revision: 1.0.0
status: DRAFT_FOR_REVIEW
title: ID・TraceID・作業から要求までの追跡
owner: null
trace_id: TRC-SPKGW-000001
created_on: '2026-10-08'
updated_on: '2026-10-08'
classification: INTERNAL
source_baseline: BL-R9-0001
related_ids: []
---

# ID・TraceID・作業から要求までの追跡

## 1. IDを用途で分ける
| 種類 | 例 | 不変条件 |
|---|---|---|
| 作業連鎖 | TRC-SPKGW-000001 | 同じ目的の調査・設計・修正・評価を束ねる。作業再試行で変更しない |
| タスク | TASK-SPKGW-000001 | WBS・担当・期日が変わっても不変 |
| 実行 | EXE-SPKGW-000001 | 再試行・別Actor・別入力では新規 |
| 証拠 | EVD-SPKGW-000001 | ファイルhashと取得範囲を持つ |
| 計画／予算 | PLN-SPKGW-000001 / BUD-SPKGW-000001 | 承認時のスナップショットを固定 |
| 変更／決定 | CHG-SPKGW-000001 / DEC-SPKGW-000001 | 実行・技術・費用の判断範囲を記録 |
| 工数／原価／発注 | EFF-SPKGW-* / CST-SPKGW-* / COM-SPKGW-* | 同じ原票を二重計上しない |
| 要求・機能・質問 | 既存SYS-*、S-FN-*、GW-FN-*、IF-*、OQ-* | 現在の識別子を変更しない |
本TraceIDは開発作業の相関規則であり、W3Cのトレース標準や製品ランタイム通信のtrace_idの実装指定ではない。既存specflowのRUN/FRAG/CAND/BLを改名せず、型付き関係で接続する。

## 2. 採番と並行作業
連番はcontrol.jsonの単一採番担当が確保し、削除後も再利用禁止。複数ブランチでの作業はUUID由来接尾辞を許し、マージ前の重複検査を必須にする。govcheck new-taskはUUID接尾辞を使用する。IDへ担当者名・個人情報・可変章番号を意味として埋め込まない。

## 3. 追跡の基本連鎖
```text
原資料(source_id＋版＋hash＋locator)
  → 抽出断片(run_id / fragment_id)
  → 分析・採否(candidate_id / decision)
  → SYS / USDM / 機能 / IF / OQ
  ↔ TASK → EXE → EVD → レビュー・採用記録
          ↘ EFF / CST / COM → 進捗・予算報告
```
TraceIDだけを付けても因果・要求対応にはならない。related_to / derives_from / implements / verifies / evidence_for / blocked_by / supersedes等の関係、両端ID、根拠を持たせる。一本のTraceへ複数タスク、タスクへ複数Traceの関係を許す。主trace_idと補助edgesを使い、主IDの書換えで履歴を移動しない。

## 4. 参照の強度
TASKのlinked_idsに既存要求等を指定し、artifactsにworkspace相対パスを置く。必要時はanchor又はJSONポインタを加える。EXEは入力Baseline/commit/hash、EVDは実ファイルhashを保持する。ファイル移動時は移動対応を更新し、内容更新時は新証拠又は新revとする。単なる日付・タイトル一致で同一性としない。
source_idは原資料の所在、requirement_idは採用条件、trace_idは作業相関である。相互に代用しない。Git commitは成果の所在であり、実行・レビュー・予算承認の代替ではない。

## 5. 完了・訂正
DONEタスクには少なくとも1証拠と受入記録を紐付ける。存在しないID・原本のない証拠・不一致hashを拒否する。廃止は参照検索と置換関係を残し、参照されるIDを削除しない。訂正の前後を追跡可能にする。

## Open Questions

担当・実予算・承認閾値・運用環境の未決は [GOV Open Questions](Open_Questions.md) を参照する。本文の運用案は、未確定の製品仕様や支出の承認を代行しない。
