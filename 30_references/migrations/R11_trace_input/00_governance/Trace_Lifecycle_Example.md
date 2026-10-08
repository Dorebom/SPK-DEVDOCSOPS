---
schema: spkgw.governance-note/v1
document_id: GOV-TRACE-EXAMPLE-001
project: SPK-GW_HEMS
document_type: REPORT
revision: 1.1.0
status: DRAFT_FOR_REVIEW
title: Traceの全工程・会議・調査・保守への接続例
owner: null
trace_id: TRC-SPKGW-000001
created_on: '2026-10-08'
updated_on: '2026-10-08'
classification: INTERNAL
source_baseline: BL-R9-0001
related_ids: []
---

# Traceの全工程・会議・調査・保守への接続例

## 1. 例示の範囲
以下は「HEMS更新時の既存制御維持」を題材にした**追跡構造の説明例**。実案件の採用要求・実測・完了記録を新設したものではない。TRC-EXAMPLE-AやSYS-EXAMPLE等はこの説明だけの識別子で、運用台帳へ自動登録しない。

## 2. 企画から運用まで
| 工程 | 記録するものの例 | 遡る対象 |
|---|---|---|
| P01 企画・構想 | 更新中の影響を抑える目的・対象住宅 | 原資料・商品課題 |
| P02 要求分析 | 利用者・保守担当の困りごと・制約 | 企画・調査結果 |
| P03 要求仕様策定 | 条件付きの機能維持要求と受入条件 | 利用者要求・USDM理由 |
| P04 システム設計 | GW/PCS/ルータの責務・構成 | システム要求 |
| P05 アーキテクチャ設計 | H/G分離・プロセス・依存 | システム構成・制約 |
| P06 基本／構造設計 | コンポーネント・API・状態 | アーキテクチャ |
| P07 詳細設計 | 異常処理・指令系列・復帰手順 | API・状態契約 |
| P08 実装 | 対象commit、静的解析、コードレビュー | 詳細設計・要求 |
| P09 単体テスト | 試験ケースと対象ビルドの結果 | 関数・状態・要求 |
| P10 結合テスト | 送信所有者・プロセス境界の結果 | IF・構造設計 |
| P11 システム／機能テスト | 更新中の機能維持の確認 | システム要求 |
| P12 非機能テスト | 高負荷・通信断・耐久等の結果 | 性能・信頼性・分離要求 |
| P13 受入・妥当性確認 | 利用場面での受入確認 | 利用目的・製品要求 |
| P14 リリース準備 | 承認・移行・復旧・マニュアル | 要求・試験・既知問題 |
| P15 リリース／導入 | 実配布版・現場構成 | リリース・対象個体 |
| P16 運用・保守 | 障害・診断・修正依頼 | 実導入版・影響機能 |
| P17 振り返り・改善 | 設計／プロセス改善と採否 | 実績・運用事象・会議決定 |

原目的が同じなら主TraceIDはすべて同じ。コード・試験結果・導入記録は個別IDと版を持つ。新しい独立した改善目的は子Traceとして元テーマへfollow_up_to等でつなぐ。

## 3. 関連調査と会議
```text
RES-EXAMPLE-01  通信断時の機器動作を調査（P04/P05, RESEARCH）
  investigates → 要求・OQ・接続仕様
  result_of    → 調査TASK／実行

MTG-EXAMPLE-01  設計レビュー会議（P05/P06, MEETING）
  議題A：TRC-EXAMPLE-Aの通信境界
  議題B：TRC-EXAMPLE-Bの診断機能
  discusses → 対象設計、RESの結果

DEC-EXAMPLE-01
  decides_on → 設計の対象版
TASK-EXAMPLE-CHANGE
  action_from → DEC-EXAMPLE-01
新しい設計版
  derives_from → 確認済み調査結果
  supersedes   → 旧設計版
```

会議録は1つ。各議題で対象Traceと決定・TASK・未決を分ける。参加者の工数は1つの原票として管理し、テーマの数だけ全額計上しない。

## 4. テストのV字対応と更新
試験結果を直前工程だけへリンクしない。TEST_CASE→対象仕様にverifies、TEST_RESULT→ケースにresult_ofを持つ。P13のValidationは企画・利用者要求を確認する。旧版の結果はその対象版を保持し、新版への関連を変えただけでPASSへ転記しない。

## 5. 新版影響の逆引き
ある要求を変更したら、derives_from／implements／verifies等を逆向きにたどり、関連設計・コード・試験・リリース・導入・保守の見直し候補を出す。会議記録の関連も参考として追えるが、そこで議論したことだけでは実装・受入が成立しない。

## Open Questions
実テーマの粒度、実ID・commit／証拠、工程別必須成果は[管理OQ](Open_Questions.md)を参照。ここにある例を実績や承認済み権限として使わない。
