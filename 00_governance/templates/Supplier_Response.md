---
schema: spkgw.governance-note/v1
document_id: TPL-GOV-SUPPLIER
project: SPK-GW_HEMS
document_type: TEMPLATE
revision: 1.3.0
status: TEMPLATE
title: 委託先技術回答・受入確認
owner: null
document_trace_id: DTR-SPKGW-TEMPLATE-000017
item_trace_ids: []
thread_id: THR-SPKGW-GOV-000001
related_thread_ids: []
trace_contract: spkgw.lifecycle-tags/v2
phase_ids:
- REQSPEC
- DETAIL
- OPS
phase_scope: CROSS_PHASE
activity_type: UNSPECIFIED
created_on: '2026-10-08'
updated_on: '2026-10-08'
classification: INTERNAL
source_baseline: BL-R9-0001
related_ids: []
---

# 委託先技術回答・受入確認

## 1. 対象と正本参照
| 項目 | 記入 |
|---|---|
| TASK／DTR／ITR／THR | 未記入。登録IDを参照し、原文のIDを削除しない |
| 入力文書版・基準commit・対象機種・FW・接続 | 未記入 |
| 未commit差分・対象外・実行認可 | 未記入 |
| 作成者・確認者・日時 | 未記入。本人・承認を推測しない |

本ファイルは未記入テンプレート。コピー時は新DTR・native ID・実際の配置リンクを設定し、状態を実記録に合わせる。記録が不要な小変更は既存TASK内へ必要項目を記載してよい。費用・TASK state・製品採用状態の第二正本にしない。

## 2. 最小回答項目
| 項目 | 回答／既存資料の版と位置 |
|---|---|
| 対象製品・変更前後版・ビルド／配布物 | 未記入 |
| 変更内容・理由・影響範囲・根拠 | 未記入 |
| 処理・入出力・状態・異常処理の設計 | 未記入 |
| リスク・発生条件・対策・残留制限 | 未記入 |
| 検証条件・期待値・観測・ログ・未実施 | 未記入 |
| 更新／復旧・他機種・保守継続の扱い | 未記入 |

## 3. 脆弱性時の追補
識別情報／CVE等・情報源、部品版・patch/backport、製品での利用・到達性・攻撃条件、該当／非該当／調査中の根拠、暫定措置、修正物・提供見込：未記入。通常変更で非該当なら理由を記録する。

## 4. 問い合わせと自社判断
委託先回答者・自社窓口、依頼・一次／確定回答予定、未回答、利用権・機密区分：未記入。回答期日の具体値は契約・製品運用に従い確定する。

自社が照合した版・実物・試験・不足、判断者・日時・根拠DEC/EVD：未記入。判定はレビュー記録に保持しTASKのDONEを別欄へ複製しない。委託先の確認済みを自社PASSへ自動転記しない。

根拠：[セキュリティ・委託先STD](../STD_17_Security_Supplier.md)。IPA／JETの公式様式ではない。

## Open Questions
未回答の判断・数値・対象版・担当・確定期限を記入する。未記入を承認済み・合格・0に置換しない。[統合方針](../AI_STD_Integration.md)を参照。
