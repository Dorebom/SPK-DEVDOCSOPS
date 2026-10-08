---
schema: spkgw.governance-note/v1
document_id: STD-GOV-009
project: SPK-GW_HEMS
document_type: STANDARD
revision: 1.2.0
status: DRAFT_FOR_REVIEW
title: 変更・リスク・課題・エスカレーション
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
document_trace_id: DTR-SPKGW-GOV-000016
item_trace_ids: []
---

# 変更・リスク・課題・エスカレーション

## 1. 変更の入口
要求、仕様、設計、実装、IF、対応機器、データ、計画、予算、役割・権限の変更をCHGで識別する。旧新差、理由、対象Baseline、影響ID、代替案、必要試験、費用・日程、判断者・決定を残す。単なる移動・改番でもリンクと意味的整合を検査する。

## 2. 区別する管理対象
OQは未確定の判断、リスクは将来起こり得る事象、課題は現在起きている障害、タスクは解消に向けた作業、決定は権限者による採否。OQを閉じるために必要なTASKを関連付ける。リスク台帳は事象・原因・影響・発生可能性・対応・Owner・残リスクを持つ。根拠のない精密な確率や金額を作らない。

## 3. 再計画
基準計画・予算を残し、CHGの承認後に新しいBaselineを採用する。キャンセルした仕事の既発生原価は消さない。追加作業、手戻り、管理作業を製品機能の完成率から隠さない。途中発見した依存は即時記録して、期限・見積・契約へ反映する。

## 4. エスカレーション
安全・セキュリティ・G側非干渉・原資料改変・本番誤操作は数値閾値を待たず担当へ報告し、許可範囲を越える作業を停止する。予算超過、期日遅延、レビュー待ち、証拠不足の具体閾値・宛先・期限は決定者が設定する。既定の自動承認・自動発注は設けない。
例外は例外ID、範囲、理由、期限、承認、追加監視・復旧・追認作業を持つ。例外が失効したら通常ルールへ戻し、永久例外を作らない。

## 6. R11：全ライフサイクルの変更追跡
変更CHGから元の企画／要求／設計／コード／試験／導入／運用事象を型付き関係で遡れるようにする。既存目的の変更は主Traceを維持し、独立した新目的は新Traceを起こしてfollow_up_to等で接続する。supersedesは履歴の削除を意味しない。

下流影響はグラフの逆参照で候補を出し、通常入力の値域・頻度、機器構成、H/G共有資源など内容面を別にレビューする。Traceが同じことやバイナリ不変だけでJETへの非影響を宣言しない。

## R12：文書と項目の識別

文書は`document_trace_id`（DTR）、個別項目は`item_trace_id`（ITR）、目的の束ねは任意の`thread_id`（THR）。本文中の旧「Trace」が作業相関を表す場合はTHRを指す。[TraceID標準](STD_03_TraceID.md)に従い、文書リンクを項目の実装・検証リンクの代わりにしない。工程は英字略称、担当未確定はUNASSIGNED。

## Open Questions

担当・実予算・承認閾値・運用環境の未決は [GOV Open Questions](Open_Questions.md) を参照する。本文の運用案は、未確定の製品仕様や支出の承認を代行しない。
