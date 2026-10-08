---
schema: spkgw.governance-note/v1
document_id: STD-GOV-006
project: SPK-GW_HEMS
document_type: STANDARD
revision: 1.1.0
status: DRAFT_FOR_REVIEW
title: 実行・レビュー・証拠・受入の記録
owner: null
trace_id: TRC-SPKGW-000001
created_on: '2026-10-08'
updated_on: '2026-10-08'
classification: INTERNAL
source_baseline: BL-R9-0001
related_ids: []
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

## Open Questions

担当・実予算・承認閾値・運用環境の未決は [GOV Open Questions](Open_Questions.md) を参照する。本文の運用案は、未確定の製品仕様や支出の承認を代行しない。
