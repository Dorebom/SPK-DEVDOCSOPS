---
schema: spkgw.governance-note/v1
document_id: STD-GOV-011
project: SPK-GW_HEMS
document_type: STANDARD
revision: 1.2.0
status: DRAFT_FOR_REVIEW
title: 構成・文書採用・リリース管理
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
document_trace_id: DTR-SPKGW-GOV-000018
item_trace_ids: []
---

# 構成・文書採用・リリース管理

## 1. 三つのBaseline
製品仕様Baseline（BL）、開発計画（PLN）、予算（BUD）は別ID。相互の適用を参照し、CURRENT.jsonを使うR9の文書公開をそのまま維持する。計画・予算は別の承認記録と10_canonical/managementに保存する。マネジメント承認の自動公開ツールは今回追加しない。

## 2. R9との接続
原本登録→抽出→分析→草案→prepare→候補hash承認→publishというSTD-IMP-001を守る。各段階のtask_id/thread_id/execution_idを管理台帳で既存source_id/run_id/fragment_id/candidate_id/prepared hash/receiptへ対応付ける。specflowの既存スキーマに未定義項目を勝手に挿入しない。
既存ツールにはTASKの存在を強制するフックを追加していない。作業IDの記録と手順レビューで補い、CI連携は別タスクで導入する。現在のcontrol.jsonのedgesは管理用であり、specflowのtrace_links.jsonのUSDM対応を置換しない。

## 3. 候補・ツール変更
governance追加によりtools/schemasのハッシュが変わる場合、古いprepare候補はそのままpublishしない。新ツールで再prepare・差分レビュー・承認する。署名・Git保護・アクセス制御を運用で補い、JSONのAPPROVE文字列だけを承認本人の証明にしない。

## 4. リリース受入
対象機種・H/G/PCS/クラウド/アプリ版、SYS/USDM/IF/構成、変更影響、既知問題、試験・証拠、展開・復旧、サポート条件を同一releaseへ結ぶ。H側変更でも共通OS・NIC・電源・reset・送信頻度の影響を評価する。社内PASSをJET判断に読み替えない。

## 5. 保持と削除
現行から参照される原本・証拠・IDは削除しない。非参照ファイルを整理する場合も依存検索・保持期間・責任者・理由を記録する。過去ZIPの再帰的多重同梱を避け、元hashと必要な原本保持を検証する。マニフェスト生成で同名ファイルを除外しない。

## 6. R11：リリースから運用へのTrace継承
リリース→収容する要求／設計／コード／試験の特定版、導入→実配布リリース、障害→該当導入記録、修正→障害、改善→根拠の結果／決定を関連付ける。ファイル名だけで版を表さない。

製品文書のCURRENTは引き続きBL-R9-0001。本R11は作業管理方式の改版であり、製品仕様や管理計画・予算を自動採用しない。Trace台帳はanalysis内の編集正本、レビュー用草案はdrafts、承認時の記録一式はmanagement/baselinesへ保存する。自動採用フックは今回実装しない。

## R12：文書と項目の識別

文書は`document_trace_id`（DTR）、個別項目は`item_trace_id`（ITR）、目的の束ねは任意の`thread_id`（THR）。本文中の旧「Trace」が作業相関を表す場合はTHRを指す。[TraceID標準](STD_03_TraceID.md)に従い、文書リンクを項目の実装・検証リンクの代わりにしない。工程は英字略称、担当未確定はUNASSIGNED。

## Open Questions

担当・実予算・承認閾値・運用環境の未決は [GOV Open Questions](Open_Questions.md) を参照する。本文の運用案は、未確定の製品仕様や支出の承認を代行しない。
