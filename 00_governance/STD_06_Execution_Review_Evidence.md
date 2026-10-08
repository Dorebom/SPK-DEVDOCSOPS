---
schema: spkgw.governance-note/v1
document_id: STD-GOV-006
project: SPK-GW_HEMS
document_type: STANDARD
revision: 1.3.0
status: DRAFT_FOR_REVIEW
title: 実行・レビュー・証拠・受入の記録
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
document_trace_id: DTR-SPKGW-GOV-000013
item_trace_ids:
- ITR-SPKGW-IMPROVE-000004
- ITR-SPKGW-IMPROVE-000005
---

# 実行・レビュー・証拠・受入の記録

## 1. 実行記録
実行ごとにEXE ID、TASK ID、TraceID、Actor、実行役割、開始終了時刻、入力Baseline/commit、対象・環境、指示、ツールと設定、出力、終了コード、結果、残課題を記録する。実行と独立評価は同一記録内でも役割・実施時点を分ける。試験コマンドの終了成功と、製品の合否を混同しない。

## 2. 証拠
EVDはworkspace相対パス・SHA-256・生成EXE・対象版・何を確認できるか・公開範囲を持つ。ログやレポートだけでなく差分、波形、画面、メーカー確認、承認記録も対象。原本改変・秘密漏えいは禁止。秘匿化は派生IDと原本hashを保持する。パス存在だけで受入せず、内容・条件・閾値をレビューする。

## 3. レビュー対象
要求と理由、適用機種、通常制御とG側、状態・障害、影響範囲、コード安全性、証拠の十分性、回帰、原本維持、ライセンス・機密、予定と実績を確認する。AI自身のSELF_REVIEWを独立レビューと表示しない。単独担当の場合はチェックリストによる時点分離レビューと独立性の限界を明示する。

## 4. 判定
試験result=PASS/FAIL/NOT_RUN/NOT_APPLICABLE/INCONCLUSIVE、受入decision=ACCEPT/REWORK/REJECTを別項目にする。NOT_APPLICABLEには理由・対象範囲・判断者が必要。DONEには受入の証拠IDと担当Actorを必須とする。報告書に「動くはず」と書いたことやAI回答を、そのまま実機PASSとしない。

## 5. 再現性と訂正
同じ入力・ツール・条件を復元できる情報を残す。再試行は新EXE、元記録は残す。結果訂正は新記録で置換対象を指定する。単に最新ファイル名だから正しいとしない。証拠移動はパス・対応を更新しhash維持を確認する。

## 6. R11：版付き成果・関係の評価
EXEは同じTraceのTASKを参照し、テスト仕様・対象コードcommit／ビルド・HW／FW・接続構成・実行環境を特定する。試験結果は特定のTEST_CASE／実行ノードへresult_of、TEST_CASEは検証対象へverifiesで結ぶ。レビューは対象版付きノードと根拠を指す。テストPASSの原票が存在しても、新版や別構成の試験結果へ自動転用しない。

tracecheckのCONFIRMEDは追跡関係を確認した記録であり、TASK受入・製品試験合格・署名者本人認証を代替しない。関係を変更したら確認記録を再評価する。

## R12：文書と項目の識別

文書は`document_trace_id`（DTR）、個別項目は`item_trace_id`（ITR）、目的の束ねは任意の`thread_id`（THR）。本文中の旧「Trace」が作業相関を表す場合はTHRを指す。[TraceID標準](STD_03_TraceID.md)に従い、文書リンクを項目の実装・検証リンクの代わりにしない。工程は英字略称、担当未確定はUNASSIGNED。

## R13追補：変更に応じた確認量と反証

<a id="aim-04"></a>
### AIM-04 — 実行証拠・異常系・自己レビュー

変更に関連する正常値・境界値・欠損・不正入力、通信断・遅延応答・重複・順序逆転、停止・復電・復元、設定と運転の競合、資源枯渇・対象外構成を選び、期待結果と対象版・環境へ結び付ける。試験数や変更行数だけで十分性を決めず、不要とする確認には理由又は適用できる既存証拠を示す。

ホストビルド、ターゲット向けビルド、シミュレータ、ターゲット実機の観測を区別する。自分が実行した試験、CI結果を参照した確認、人の報告で未照合のものを別記し、他者のPASSを自分の実行結果へ転記しない。終了コードやCI緑だけで必要試験が実行されたとしない。

基準版でも発生する失敗は比較した版・条件・証拠を残す。合格のために閾値・期待値を弱めたり、根拠なく削除／skipしない。仕様の誤りが疑われる場合は変更判断へ戻す。修正後の再実行は新しいEXE／EVDを作り、元の失敗を残す。

一人開発の別時点・別観点での自己レビューはそのまま記録する。別AIの評価を、必要な専門家・別担当者による審査の代替として偽装しない。
<a id="aim-05"></a>
### AIM-05 — 結果語彙と周期測定の境界

現行の試験resultは`PASS / FAIL / NOT_RUN / NOT_APPLICABLE / INCONCLUSIVE`を維持する。添付の試験BLOCKEDは、未実行ならNOT_RUN＋不足前提・担当・予定、実行したが判定できなければINCONCLUSIVE＋不足観測として扱う。TASKのBLOCKEDとは別である。NOT_APPLICABLEは理由と適用判断が必要。

時間試験は要求周期Tと実測時刻t_kを用いる場合、周期差e_k=(t_k−t_(k−1))−T等で評価できるが、式だけで閾値を確定しない。計測点、時計基準、受理／送出／応答／物理反映、観測窓・許容誤差を確定する。一部の1秒要求を全通信・全機器へ広げない。

本版の追補・新設部分は[選択統合記録](AI_STD_Integration.md)から原文位置・採否・差分を追跡できる。添付の旧状態・旧保管先・旧ID体系を現行へ併設しない。

## Open Questions

担当・実予算・承認閾値・運用環境の未決は [GOV Open Questions](Open_Questions.md) を参照する。本文の運用案は、未確定の製品仕様や支出の承認を代行しない。
