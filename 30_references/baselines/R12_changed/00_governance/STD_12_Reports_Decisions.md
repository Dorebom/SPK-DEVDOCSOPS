---
schema: spkgw.governance-note/v1
document_id: STD-GOV-012
project: SPK-GW_HEMS
document_type: STANDARD
revision: 1.2.0
status: DRAFT_FOR_REVIEW
title: 進捗会議・日報週報・意思決定
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
document_trace_id: DTR-SPKGW-GOV-000019
item_trace_ids: []
---

# 進捗会議・日報週報・意思決定

## 1. 報告は管理正本から生成する
TASKの状態、control.jsonの実績・見通し、承認したPLN/BUDから集計する。報告書のパーセントや合計だけを手で直さない。期間・締め日時・入力hash・計画版・集計除外を明記する。過去レポートを同名上書きせず、訂正時は新報告IDへ置換関係を付ける。

## 2. 最小報告項目
成果として受入済みのもの、未完了・レビュー待ち・BLOCKED、基準との差、残工数・予測完了、追加・取消し、AC/OC/ETC/EAC/VAC、未計上・未確定・承認待ち、主なリスク、必要な決定、次の作業を示す。数字がない時はNOT_AVAILABLEを明示する。
人件費、AI費用、委託費、設備費等の内訳と課税・通貨基準を示す。実績額に請求到着分しか含まれない場合は、発生原価全体ではないと注記する。

## 3. 会議からタスクへ
会議そのものをMANAGEMENT/LOE又は明示成果のTASKにする。議事は議題・参加Actor・根拠・決定・保留・担当・期限・TASK/OQを記録する。「検討します」だけで終了しない。決定はDECとして対象版・権限範囲・理由を持ち、TASKのDONEとは別に管理する。

## 4. 配信と秘匿
原価単価・委託契約・個人情報を全開発者へ一律公開しない。公開範囲に応じた派生レポートを生成し、元記録へ限定アクセスを維持する。このパッケージはメール送信や周期実行を自動設定していない。

## 5. 入力締め
週次・月次の締め対象と担当を明示し、未入力件数を出す。締め済み期間の変更には訂正理由が必要。予定だけの作業を実績へ移すこと、テスト用データを実運営へ足すことは禁止。

## 6. R11：会議・調査の工程横断記録
会議をMANAGEMENTに固定せず、phase_ids=SYSDES/ARCH等とactivity_type=MEETINGを組み合わせる。会議TASKの工数管理と会議録MTGの内容管理を分ける。複数テーマなら議題AGENDAごとにTrace・入力版・検討内容・決定・保留・派生TASK・OQ・担当・期限を記す。

調査RESは調査目的、対象工程、原資料のID／版／位置、事実・解釈・仮説、結論、影響する要件／設計／試験、次作業を持つ。採用しない結果も根拠として保存する。

週次会議は複数Traceを一覧で扱ってよいが、「報告した」ことを各設計・試験の受入済みとしない。[会議テンプレート](templates/Meeting.md)、[調査テンプレート](templates/Research.md)を使用する。

## R12：文書と項目の識別

文書は`document_trace_id`（DTR）、個別項目は`item_trace_id`（ITR）、目的の束ねは任意の`thread_id`（THR）。本文中の旧「Trace」が作業相関を表す場合はTHRを指す。[TraceID標準](STD_03_TraceID.md)に従い、文書リンクを項目の実装・検証リンクの代わりにしない。工程は英字略称、担当未確定はUNASSIGNED。

## Open Questions

担当・実予算・承認閾値・運用環境の未決は [GOV Open Questions](Open_Questions.md) を参照する。本文の運用案は、未確定の製品仕様や支出の承認を代行しない。
