---
schema: spkgw.governance-note/v1
document_id: STD-GOV-018
project: SPK-GW_HEMS
document_type: STANDARD
revision: 1.3.0
status: DRAFT_FOR_REVIEW
title: 人・AI協働の測定・改善
owner: null
document_trace_id: DTR-SPKGW-GOV-000031
item_trace_ids:
- ITR-SPKGW-IMPROVE-000025
- ITR-SPKGW-IMPROVE-000026
thread_id: THR-SPKGW-GOV-000001
related_thread_ids: []
trace_contract: spkgw.lifecycle-tags/v2
phase_ids:
- IMPROVE
phase_scope: PHASE_SPECIFIC
activity_type: UNSPECIFIED
created_on: '2026-10-08'
updated_on: '2026-10-08'
classification: INTERNAL
source_baseline: BL-R9-0001
related_ids: []
---

# 人・AI協働の測定・改善

実績・品質・流れ・人の負担から作業契約を改善する。測定ログを新しい進捗／原価の正本にしない。

## 1. 測定する範囲

<a id="aim-25"></a>
### AIM-25 — 分母・時点・欠測・比較条件

どの指標にも期間、集計時点、対象集合、単位、情報源、欠測、算式を付ける。実測・ツール取得・申告・推定を区別し、未取得を0にしない。成果受入・WIP・待ち・手戻り・期限と予測差・品質残課題を候補として、取得できる範囲から始める。

リードタイムをREADY→受入、サイクルタイムを初回着手→受入で観測するときは、両方が待ちを含む経過時間であることを明示する。未受入は集計時点までの滞留として表示し、未完了の値を完成値にしない。実働・AI実行・複数Actor合計・並行・重複待ちを単純加算しない。時刻が取れない場合は精度を落として明示する。

比較は作業種別・規模・入力品質・既存理解・影響区分・担当・確認範囲をそろえる。導入前の実測がなければ改善率を断定せず、失敗・手戻り・人の肩代わり・未受入を除外してAIの速さだけを報告しない。少数例で個人を順位付けしない。

## 2. Capabilityの記録と改善実験

<a id="aim-26"></a>
### AIM-26 — 軽量な協働記録と将来接続

[AI Capability Log](templates/AI_Capability_Log.md)は任意。人・AIの双方について、実際に提供した要求整理・設計・実装・観測・評価・改善、入力・出力版、権限、使用環境の確認済み情報、修正負担、待ち、費用原票参照、成功・失敗条件を残す。

原文の「週1件」や「最初の半年」は参考案であり、固定ノルマ・期限・自動スケジュールにしない。全プロンプト・全会話の収集を受入条件にせず、ログ未作成だけで作業受入を阻害しない。ただし重大な問題・例外の必須記録は省略しない。

改善は観測事実→原因仮説→小さな試行→品質・流れ・負担の比較→継続／変更／中止の根拠を残す。要求・権限・標準・予算等を変えるときは変更判断へ接続する。Capabilityの自己評価から実行権限を拡張しない。

SHIRABE／HIBIKIへの将来接続は参考の位置付けとして保存するが、専用ランタイムや独自プロトコルを現在の必須依存にしない。機密原文の全保存や社外再利用を無断で行わない。

## 3. 正本・計算・実装範囲

工数・費用はcontrol.json、作業stateはTASK、正式進捗とEACはSTD-GOV-007/008を使用する。今回の新しい測定は記録ルールとテンプレートであり、リードタイム・WIP時間・比較効果の自動集計機能をgovcheckへ追加したものではない。

## Open Questions

採用する指標・取得精度・カレンダー・匿名化・保持・共有範囲はOQ-GOV-AISTD-03で確認する。実験結果や生産性向上は未測定。

本版の追補・新設部分は[選択統合記録](AI_STD_Integration.md)から原文位置・採否・差分を追跡できる。添付の旧状態・旧保管先・旧ID体系を現行へ併設しない。
