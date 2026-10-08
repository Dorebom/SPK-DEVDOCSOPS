---
schema: spkgw.governance-note/v1
document_id: STD-GOV-014
project: SPK-GW_HEMS
document_type: STANDARD
revision: 1.3.0
status: DRAFT_FOR_REVIEW
title: 要求・仕様・変更影響分析
owner: null
document_trace_id: DTR-SPKGW-GOV-000027
item_trace_ids:
- ITR-SPKGW-IMPROVE-000013
- ITR-SPKGW-IMPROVE-000014
- ITR-SPKGW-IMPROVE-000015
thread_id: THR-SPKGW-GOV-000001
related_thread_ids: []
trace_contract: spkgw.lifecycle-tags/v2
phase_ids:
- REQAN
- REQSPEC
phase_scope: CROSS_PHASE
activity_type: UNSPECIFIED
created_on: '2026-10-08'
updated_on: '2026-10-08'
classification: INTERNAL
source_baseline: BL-R9-0001
related_ids: []
---

# 要求・仕様・変更影響分析

原資料STD-04を既存の取り込み標準、SYS/USDM、DTR/ITR、変更TASKへ適合させた追補。製品仕様値や採用機能を新たに決める標準ではない。

## 1. 変更前にそろえる情報

<a id="aim-13"></a>
### AIM-13 — 六つの質問と適用範囲

| 問い | 最低限の記録 |
|---|---|
| 目的 | 誰のどの問題・要求・受入条件に対応するか |
| 現状と変更後 | As-Isの確認事実、To-Beの提案又は採用内容、維持条件 |
| 対象 | 製品/HW/FW/接続方式/機能/通信/状態/対象外 |
| 影響 | 直接変更、呼出元・先、設定・データ・試験への波及と未調査 |
| 確認 | 観測する結果、条件・環境、判定方法・未実施 |
| 判断 | 作業認可、必要な境界変更、担当と確定時点 |

六つの別文書を作る必要はない。小変更はTASK／Change本文から既存のDTR＋版、ITR、Baseline／固定commitへ参照する。原文の「取得日時付きリンク」は取得版・内容hashで固定できる場合だけ根拠にし、latest/HEADを確定版にしない。既存native IDは改番せず、項目を分割する必要があるときだけ新ITRと旧新関係を残す。

## 2. 要求・仕様と未確認事項

<a id="aim-14"></a>
### AIM-14 — 観測可能な要求と根拠の区別

発生条件、責任主体、期待する動作・結果、適用構成、終了・異常・非対象を明示する。受入条件には観測点・判定方法・環境・対象版を付け、曖昧な「安定」「高速」「問題なし」だけにしない。値が未確定ならnull/TBDと確認者候補・必要時点をOQに結ぶ。

要求・理由、仕様（要求を満たす条件・振る舞い）、設計（実現方法）を分ける。仕様は外部公開情報だけに限定せず、R12のPart II/H-G境界等の内部システム契約も含む。原文にない理由は仮説又は不明にし、USDMのORIGINAL/HUMAN_CONFIRMEDへ自動昇格しない。

横断要求を機能ごとにコピーせず、共通のITRを複数設計・試験へ結ぶ。DTR引用だけで個別要求の根拠条項を確認済みにしない。観測済み・未調査・調査したが不明・適用対象外を分け、AIが未確定を実装済みへ変えない。

## 3. 影響分析の最低範囲

<a id="aim-15"></a>
### AIM-15 — 実行経路と外部依存まで追う

| 観点 | 確認するもの |
|---|---|
| 外部振る舞い | 上位、宅内Web、アプリ、外部HEMS、機器の要求・応答・通知 |
| 制御と競合 | 発生源、制御権、期限、設定変更、高優先度処理、停止・再起動 |
| データ | 単位・符号・計測点、範囲・既定値、時刻、保存・移行 |
| 境界 | 公開API、IPC、H/G、レイヤ／プロセス、認証・鍵・保守経路 |
| 通信と資源 | 待ち時間、再送、順序逆転、キュー、共通NIC／ルータ／バス |
| 構成 | HW/FW、As-Is/To-Be、Yocto・依存版、既設／新規 |
| 品質と運営 | 安全・認証、回帰、委託先回答、実機、計画・費用 |

各行は根拠又は理由付き対象外を付ける。検索0件だけで動的登録・生成コード等の影響なしを確定しない。ブラックボックスの内部は推測せず、対象版・差分・影響根拠を委託先へ確認する。

現在の設計条件（全取得は宅内ルータ経由、RS-485 PCSはGW G側が取得・管理・指示、EL接続PCSのみ自律取得、通常H側によるG側迂回禁止、DPC/FLC/Measurement分離、認証・暗号の混在）はチェック対象として参照する。文書取込みを理由に変更しない。変更が必要ならCHGへ分離する。

## 4. 記録先・引渡し

小変更は[Change](templates/Change.md)、詳細化する場合は[Change Impact](templates/Change_Impact.md)を使用する。原文は30_references、抽出・照合は20_work/analysis、改訂本文は20_work/draftsへ置く。現行10_canonicalへ直接追記しない。

## Open Questions

初回採用機能・数値・要求理由・実プロトコル・承認者は既存の製品OQ／管理OQで確定する。本標準の選択統合はそれらの回答ではない。

本版の追補・新設部分は[選択統合記録](AI_STD_Integration.md)から原文位置・採否・差分を追跡できる。添付の旧状態・旧保管先・旧ID体系を現行へ併設しない。
