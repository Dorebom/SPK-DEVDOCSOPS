---
schema: spkgw.governance-note/v1
document_id: STD-GOV-012
project: SPK-GW_HEMS
document_type: STANDARD
revision: 1.0.0
status: DRAFT_FOR_REVIEW
title: 進捗会議・日報週報・意思決定
owner: null
trace_id: TRC-SPKGW-000001
created_on: '2026-10-08'
updated_on: '2026-10-08'
classification: INTERNAL
source_baseline: BL-R9-0001
related_ids: []
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

## Open Questions

担当・実予算・承認閾値・運用環境の未決は [GOV Open Questions](Open_Questions.md) を参照する。本文の運用案は、未確定の製品仕様や支出の承認を代行しない。
