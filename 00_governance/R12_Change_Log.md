---
schema: spkgw.governance-note/v1
document_id: GOV-CHANGE-R12
project: SPK-GW_HEMS
document_type: REPORT
revision: 1.2.0
status: DRAFT_FOR_REVIEW
title: R12変更記録：文書／項目Trace分離と可読工程
owner: null
document_trace_id: DTR-SPKGW-GOV-000006
item_trace_ids: []
thread_id: THR-SPKGW-GOV-000001
related_thread_ids: []
trace_contract: spkgw.lifecycle-tags/v2
phase_ids: []
phase_scope: UNASSIGNED
activity_type: PROJECT_MANAGEMENT
created_on: '2026-10-08'
updated_on: '2026-10-08'
classification: INTERNAL
source_baseline: BL-R9-0001
related_ids: []
---

# R12変更記録：文書／項目Trace分離と可読工程

## 1. 対象

ユーザー指定の2層のTraceと工程可読化を反映。管理版GOV-1.2.0。R11の仕様本体BL-R9-0001、CURRENT、原資料、実予算・実績・受入結果は不変。

## 2. 変更

STD-002/003/005、関連ノート・テンプレート、FrontMatter／TASK／Trace schema、Trace検査と索引を更新。P01〜P17を17の英字コードへ対応。既存TRC-SPKGW-000001はTHR-SPKGW-GOV-000001へ移行する。旧ファイルは30_references/migrations/R11_trace_inputに保存する。

現存文書にDTR、既存SYS・機能・試験・OQ・TASKにITRを付与し、原文位置・版と明示関係を外付け登録する。元要求本文、試験未実施状態、質問回答を変更しない。自動移行した関係にreview=CONFIRMEDを捏造しない。

## 3. 完成と未完成

形式・位置・移行整合の検査と、実成果の妥当性を分ける。細粒度の設計・コード・既存Office条項・UT/IT等の実割当は未確認。保管済み文書を登録したことは設計完成ではない。担当と根拠の確認を管理OQで進める。

## 4. ツール

tracecheckのvalidate/report/impactにresolve/documentを追加。nodeはITR、documentsはDTR。既存theme相関は任意THR。govcheckのnew-taskはタスク文書と項目を採番・登録する。既存R9 specflowは変更しない。

## Open Questions

実担当・実成果・運用環境は[管理OQ](Open_Questions.md)で確定する。製品要求・工程完了の承認ではない。
