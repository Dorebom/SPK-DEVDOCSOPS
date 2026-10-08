---
schema: spkgw.governance-note/v1
document_id: STD-GOV-004
project: SPK-GW_HEMS
document_type: STANDARD
revision: 1.3.0
status: DRAFT_FOR_REVIEW
title: 全作業タスク・WBS・状態遷移
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
document_trace_id: DTR-SPKGW-GOV-000011
item_trace_ids:
- ITR-SPKGW-IMPROVE-000002
- ITR-SPKGW-IMPROVE-000003
---

# 全作業タスク・WBS・状態遷移

## 1. すべての作業を扱う
調査、会議、要求、USDM、仕様、設計、実装、単体／結合／機能／実機試験、デザインレビュー、独立評価、修正、認証相談、文書取込み、リリース、保守、進捗管理、予算、購買、育成を対象にする。実装チケットだけを母集団にしない。緊急対応は作業IDを先に確保し、困難なら事後登録理由と実記録を残す。細かな事務作業は期間付き定常タスクへ束ねてよいが、実施明細・工数は残す。

## 2. WBS・親子・粒度
WBSは成果物／目的の分解、taskは担当・入力・完了条件・証拠を持つ作業単位。子タスクがある親はsummary=trueとし、工数・金額・完了率を独立に加算しない。親にも実作業がある場合は別leafタスクへ切り出す。1leafは完了条件を観測できる粒度に分割し、巨大な「開発一式」のパーセント更新にしない。
フェーズは作業の分類であり、WBSの所属と同義ではない。調査の結論が「非対応」でも、定義した調査の完了条件を満たせば調査タスクは完了できる。

## 3. 状態と遷移
| state | 意味 | 出口条件 |
|---|---|---|
| PROPOSED | 候補・未着手 | 範囲・Owner・受入条件・入力・見積／制約をそろえる |
| READY | 着手可能 | 未完了の依存タスクなし、権限と作業枠あり |
| IN_PROGRESS | 実作業中 | 実行記録・残工数・課題を更新 |
| BLOCKED | 前提未成立で進めない | 原因、解除条件、担当、次確認日を持つ |
| ON_HOLD | 計画判断で保留 | 再開条件・計画影響・承認を記録 |
| IN_REVIEW | 成果物と検証結果を提出 | 受入又は差戻し。提出は完了ではない |
| DONE | 完了条件を証拠で確認 | 受入Actor・日時・証拠・判定を記録 |
| CANCELLED | 実施取消し | 理由と決定を保持。完了実績へ算入しない |
標準遷移はPROPOSED→READY→IN_PROGRESS→IN_REVIEW→DONE。IN_PROGRESS↔BLOCKED、READY/IN_PROGRESS↔ON_HOLDを許す。レビュー差戻しはIN_REVIEW→IN_PROGRESS。再開はDONEから無言で戻さず、再オープン理由と変更タスクを残す。依存は循環禁止。CANCELLED依存をDONEとみなさず、依存再設計の承認が必要。

## 4. 着手準備（DoR）
Owner1名、実行Actor、対象Baseline、スコープと対象外、参照ID、成果物、検証可能な受入条件、見積工数、依存、リスク、レビュー担当を確認する。見積不能な探索はtimeboxと中間成果を定めた調査タスクに分割する。NULLの予算は無制限ではない。リスクを伴う実機・本番・G側・支出は追加認可が必要。

## 5. 完了（DoD）
全受入条件、対象版付き証拠、レビュー、必要なSYS/USDM/IF/設定/試験/OQの更新、残リスク、実績・残工数が整合したこと。残工数は0。実行PASSと評価SUFFICIENTと採用を区別する。管理タスクは要求IDがない理由とSTD又は決定IDを持てばよい。

## 6. 例外と小作業
誤記修正でも出典・差分・確認結果を残す。軽微作業は共通チケットの子明細で管理可能だが、認証境界・権限・金額・仕様値の変更を軽微と自動分類しない。例外の期限・承認を確認する。

## 7. R11：17工程・関連活動とTrace
TASKは同じTraceのまま工程を分けて作成できる。複数の成果・レビュー基準がある作業は別TASKへ分割するが、工程番号ごとにTraceを新規発行しない。会議／調査／レビューは独立TASK又は期間定常TASKの明細とし、対象工程と要求・設計・課題・決定を結ぶ。

会議録の作成だけで設計の採用を完了扱いにしない。会議の決定はDEC、派生作業はTASK、未決はOQとしてつなぎ、作業・結論・承認の状態を別に管理する。R11新規テンプレートはTrace追加属性を持つ。旧4候補TASKは内容未確認のまま工程移行済みにしない。

## R12：文書と項目の識別

文書は`document_trace_id`（DTR）、個別項目は`item_trace_id`（ITR）、目的の束ねは任意の`thread_id`（THR）。本文中の旧「Trace」が作業相関を表す場合はTHRを指す。[TraceID標準](STD_03_TraceID.md)に従い、文書リンクを項目の実装・検証リンクの代わりにしない。工程は英字略称、担当未確定はUNASSIGNED。

## R13追補：作業票への集約・中断・引継ぎ

<a id="aim-02"></a>
### AIM-02 — 作業・並列・引継ぎの最小記録

小作業は認可済みの親／期間TASKの明細へ束ねてよい。1プロンプト・1ファイルごとのTASKは必須にしない。親子の成果・工数は二重計上しない。作業単位は受入条件で決め、原資料の「半日〜2営業日」は採用済み工数上限にしない。

開始時は基準Baseline／commit、未commit差分、他Actorの変更、編集対象・統合担当・依存を照合する。他者の未完了差分を消さない。再開・担当交代・終了時には、①現状態と認可範囲、②基準と候補版・dirty差分、③変更と証拠、④実施／未実施の検証、⑤判断待ちと解除条件、⑥次に読む資料と1〜3手順を本文に残す。

`READY`等の既存条件は緩和しない。情報不足を解消する調査TASKは、調査そのものの目的・範囲・受入条件で扱う。人・AIが再開時に過去チャットを保持しているとは仮定せず、引継ぎ記録と実体の一致を確認する。
<a id="aim-03"></a>
### AIM-03 — 旧タスク状態を現行へ併設しない

現行stateは`PROPOSED / READY / IN_PROGRESS / BLOCKED / ON_HOLD / IN_REVIEW / DONE / CANCELLED`で維持する。添付の`DRAFT`はPROPOSEDの候補、`ACCEPTED`は有効な受入証拠付きDONEの候補、`CHANGES_REQUESTED`は差戻し記録＋IN_PROGRESSの候補として、人が根拠を確認して取り込む。語だけの自動状態変換はしない。

添付の独立属性`impediment=BLOCKED`は新しい状態正本として導入しない。現行BLOCKEDを使い、直前state・発生時刻・理由・解除担当・次回確認日・復帰先をTASK本文の中断履歴に記録する。部分的に進められるときはstateを実態で判断し、進められない範囲を併記する。

受入後の修正は元の受入・対象版を残して変更TASK／撤回判断へ接続する。記録の訂正と作業の取消しを混同しない。

本版の追補・新設部分は[選択統合記録](AI_STD_Integration.md)から原文位置・採否・差分を追跡できる。添付の旧状態・旧保管先・旧ID体系を現行へ併設しない。

## Open Questions

担当・実予算・承認閾値・運用環境の未決は [GOV Open Questions](Open_Questions.md) を参照する。本文の運用案は、未確定の製品仕様や支出の承認を代行しない。
