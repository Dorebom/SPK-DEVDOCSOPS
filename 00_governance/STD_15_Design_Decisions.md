---
schema: spkgw.governance-note/v1
document_id: STD-GOV-015
project: SPK-GW_HEMS
document_type: STANDARD
revision: 1.3.0
status: DRAFT_FOR_REVIEW
title: 設計・設計判断
owner: null
document_trace_id: DTR-SPKGW-GOV-000028
item_trace_ids:
- ITR-SPKGW-IMPROVE-000016
- ITR-SPKGW-IMPROVE-000017
- ITR-SPKGW-IMPROVE-000018
thread_id: THR-SPKGW-GOV-000001
related_thread_ids: []
trace_contract: spkgw.lifecycle-tags/v2
phase_ids:
- SYSDES
- ARCH
- BASIC
- DETAIL
phase_scope: CROSS_PHASE
activity_type: UNSPECIFIED
created_on: '2026-10-08'
updated_on: '2026-10-08'
classification: INTERNAL
source_baseline: BL-R9-0001
related_ids: []
---

# 設計・設計判断

既存設計を正本にし、変更に必要な説明を追加する。すべての変更で独立した詳細設計書を要求しない。

## 1. 設計の記録単位

<a id="aim-16"></a>
### AIM-16 — 七つの確認と論理・実配置の分離

責務、配置、契約、状態、競合、不変条件、確認方法の七点を、関連する変更に対して説明する。R0は差分と確認、R1は既存設計を参照した必要な判断、R2は境界・代替案・リスク・必要評価を明確にする。変更量で分類せず、不要な比較案・文書を捏造しない。

| 層・観点 | 記録 |
|---|---|
| 論理責務 | Usecase、Arbiter、Orchestrator、DPC/FLC、Measurement等 |
| 実装単位 | 実在するモジュール、API、構造体、主関数・コードITR |
| 実配置 | 実在するプロセス、HW/SW、権限・障害境界 |
| 実行文脈 | スレッド、イベントループ、周期、コールバック・割込み等 |

レイヤ名だけでCore集約・プロセス分離を断定しない。As-Isは調査した事実、To-Beは提案・採用状態を示し、分散責務を消した現状図にしない。移行中の二経路と切替条件、未commit／他Actor作業への影響も識別する。

## 2. 境界・状態・時間の契約

<a id="aim-17"></a>
### AIM-17 — 状態所有・競合・非同期結果の設計

入出力、単位・範囲・欠測・古い値、成功／失敗、受理／処理完了／実機反映、timeout・retry・重複・遅延応答を定義する。状態には所有者、読書き主体、有効な更新経路、排他・直列化と復帰を付ける。Blackboard・Mediator・RPCでも希望値・保存値・有効値を混同しない。

| 現在状態 | 入力／条件 | 判定・作用／参照要求 | 次状態 | 観測・試験ITR |
|---|---|---|---|---|
| 記入する実状態 | 設定／制御／通信断等 | 採用規則と今回差分 | 実状態 | 参照と未確定条件 |

高優先度処理中の通常設定変更と、認可された重大故障対応を別契約にする。安全そうというAI推測で優先度・停止規則を追加しない。

周期・起点・許容遅延・打切り・遅延後動作、キュー上限・溢れ、全体の待ち時間と必須通信への波及を確認する。一部1秒要求を全経路へ拡張しない。PCS自律取得とGW管理、ルータ経由、H停止とGW全停止、認証・暗号混在は既存構成に従う。構造上の分離だけでJET等の再評価不要を断定しない。

## 3. 設計判断と実装への引渡し

<a id="aim-18"></a>
### AIM-18 — 選択理由・反証・引渡し条件

複数案が実質的にある場合、採用案・比較案・選択理由・残存リスクを記録する。判断を左右する観点へ絞り、小修正に架空の代替案を追加しない。AI提案は要求・現コード・測定と照合するまで提案。

レビューは要求への一致、故障・競合・検証可能性を見て、対象DTR/ITR版・観点・指摘根拠を残す。実装中に設計から逸脱したら、必要な設計判断を更新し、コードに合わせて受入条件を無断変更しない。設計案採用、実装受入、文書Baseline、製品配布を分ける。

未確認事項のうち、固定しないと実装できないものと、仮定を明示した分離試作で調べるものを分ける。試作PASSを量産・実機・認証の証拠へ読み替えない。

## Open Questions

[Design Note](templates/Design_Note.md)に、実対象・入力・状態・タイミング・承認者・専門評価の不足を記す。設計の具体配置・全機種適合は今回未確定。

本版の追補・新設部分は[選択統合記録](AI_STD_Integration.md)から原文位置・採否・差分を追跡できる。添付の旧状態・旧保管先・旧ID体系を現行へ併設しない。
