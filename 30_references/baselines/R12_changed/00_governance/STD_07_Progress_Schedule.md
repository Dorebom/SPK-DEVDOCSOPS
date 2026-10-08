---
schema: spkgw.governance-note/v1
document_id: STD-GOV-007
project: SPK-GW_HEMS
document_type: STANDARD
revision: 1.2.0
status: DRAFT_FOR_REVIEW
title: 進捗・日程・残作業・報告
owner: null
created_on: '2026-10-08'
updated_on: '2026-10-08'
classification: INTERNAL
source_baseline: BL-R9-0001
related_ids: []
thread_id: THR-SPKGW-GOV-000001
related_thread_ids: []
trace_contract: spkgw.lifecycle-tags/v2
phase_ids: []
phase_scope: UNASSIGNED
activity_type: UNSPECIFIED
document_trace_id: DTR-SPKGW-GOV-000014
item_trace_ids: []
---

# 進捗・日程・残作業・報告

## 1. 進捗を三つに分ける
作業状態（着手・レビュー待ち等）、成果物受入、消費工数／費用を独立管理する。計画期間の経過や予算消化を機能完成率に変換しない。見積がない作業を自動で1時間として集計しない。

## 2. 基準計画と現在見通し
承認時の計画はPLN ID・版・hash・承認証拠を持つ。TASKの見通し・残工数・予測完了日を更新しても、基準計画の開始終了・工数を上書きしない。変更はCHGと新計画版へつなぐ。実績は期間締め日時を明示する。期日未決は未決として件数を出す。

## 3. 成果進捗の集計
初期方式はleafタスクの0/100受入。DONEかつ受入記録ありならp_i=1、その他0。長期タスクは検証可能な子成果へ分割する。レビュー提出だけで90%にしない。
```text
P = Σ(w_i × p_i) / Σ(w_i)
w_i = 承認基準計画に記録した工数ウェイト
```
w_iは現時点の再見積ではない。分母は基準版の対象leaf全体。キャンセルしても無断で分母から除外しない。新規作業は未基準化作業として別表示し、基準改訂で初めて追加する。全weightゼロ又は未承認ならP=NOT_AVAILABLE。
会議・管理等の定常作業（LOE）は消費工数・実施状況を別表示する。0/100成果進捗へ混ぜる場合は、期間ごとの明示成果と完了条件を設定する。現在のgovcheckレポートは成果タスクだけを重み集計し、定常タスクを別件数で示す。

## 4. 実績と見通し
各leafに実績工数、残工数ETC_h、予測完了を持ち、見込総工数=実績+残工数とする。自己申告完了率から残工数を機械的逆算しない。ブロッカー、依存、レビュー待ち、実機予約・認証待ちをクリティカルな条件として表示する。遅延は責任追及のため隠さず、影響と是正案を示す。

## 5. 報告周期の初期案
作業実施日の終了時に状態・EXE・工数・残課題を更新。週次に基準差・クリティカル依存・リスク・EACをレビュー。費用締めは月次に原票と照合する。実際の曜日・締切時刻・許容遅延は未決で、自動通知は設定しない。
報告に対象Baseline、期間、締め日時、入力hash、計画対象数、DONE・BLOCKED・レビュー待ち、未見積・未予算化・入力未完了数を含める。タスク件数完了率は補助表示で、製品完成率と呼ばない。

## 7. R11：工程・Traceから見る進捗
17工程別に成果、未接続成果、未判定適用、未レビュー関係、旧版参照、BLOCKED、残作業を表示する。Trace別の記録網羅率は成果進捗とは別にする。NOT_APPLICABLEは理由と決定を表示し、TBDを分母から消して達成率を上げない。

多工程・多Traceに関係する同じTASKの基準ウェイトと工数を重複計上しない。全体集計はtask_idで一意。テーマ別配賦を別途承認していなければ主Traceで集計するか、金額を伴わない関係ビューとして表示する。

## R12：文書と項目の識別

文書は`document_trace_id`（DTR）、個別項目は`item_trace_id`（ITR）、目的の束ねは任意の`thread_id`（THR）。本文中の旧「Trace」が作業相関を表す場合はTHRを指す。[TraceID標準](STD_03_TraceID.md)に従い、文書リンクを項目の実装・検証リンクの代わりにしない。工程は英字略称、担当未確定はUNASSIGNED。

## Open Questions

担当・実予算・承認閾値・運用環境の未決は [GOV Open Questions](Open_Questions.md) を参照する。本文の運用案は、未確定の製品仕様や支出の承認を代行しない。
