---
template_id: T-10
title: 人・AIのCapabilityログテンプレート
version: 1.0.0
status: DRAFT_FOR_ADOPTION
updated: 2026-10-07
---

# T-10 人・AIのCapabilityログテンプレート

> テンプレート版 1.0.0 / 2026-10-07 / DRAFT_FOR_ADOPTION（採用・業務承認前）。
> 任意の軽量ログ。初期は週1件の代表例を推奨する。全作業への作成を受入条件にしない。
> 人とAIの双方をActorとして記録する。未観測値をゼロや成功に変えない。

コピー後のメタデータとリンクは実際の配置先に合わせる。対象外は理由、不明事項は確認担当・予定を添える。

## 1. 作業と能力

| 項目 | 記入 |
|---|---|
| `capability_log_id` | UNSET |
| 対象期間・観測時点・タイムゾーン | UNSET |
| 作業ID・成果物版 | UNSET |
| 作業種別・相対規模・リスク区分 | UNSET |
| 対象Capability | UNSET（具体的な仕事を記す） |
| 作業認可の参照 | UNSET |
| 人の管理責任者 | UNSET |
| 記録の情報源・欠測 | UNSET |

| Actor ID | `actor_kind` | 提供したCapability | 実行・判断の範囲 | 確認できたツール・環境 |
|---|---|---|---|---|
| UNSET | UNSET（HUMAN / AI） | UNSET | UNSET | UNSET |

Capabilityは要求整理・計画・設計・実装・観測・評価・改善等から、実際に提供したものを記す。
人を承認者だけとして記録せず、人が行った実開発や計画の仕事も含める。
モデル名・バージョンが確認できない場合は `UNKNOWN` とする。

## 2. 入力と出力

- 入力の参照・版・品質・不足：UNSET
- 必要な前提、使用した指示・標準・制約：UNSET
- 実際に実行した作業の範囲：UNSET
- 出力の参照・版：UNSET
- 検証記録と結果：UNSET（PASS / FAIL / NOT_RUN / BLOCKED / INCONCLUSIVE）
- 人の受入判断の参照：UNSET（未受入ならPENDING）
- 残る限界・未確認：UNSET

秘密情報、資格情報、個人情報、長い会話原文を不要に複製しない。許可された参照・要約を優先する。

## 3. 時間・修正・費用

| 指標 | 値・単位 | 実測 / ツール取得 / 申告 / 推定 / 未取得 | 対象区間・取得元・精度 |
|---|---|---|---|
| 人の初回作業工数 | UNSET | UNSET | UNSET |
| 人の評価・確認工数 | UNSET | UNSET | UNSET |
| 人の修正工数 | UNSET | UNSET | UNSET |
| AI実行時間 | UNSET | UNSET | UNSET |
| 修正・再試行の回数 | UNSET | UNSET | UNSET |
| 承認待ち時間 | UNSET | UNSET | UNSET |
| 依存待ち時間 | UNSET | UNSET | UNSET |
| 取得可能な利用費 | UNSET | UNSET | UNSET |

- 時間の定義・カレンダー・重複区間の扱い：UNSET
- 費用の配賦方法、人時単価等の前提：UNSET
- 観測時点で未完了の区間：UNSET

経過時間、人の工数、AI実行時間、並列Actorの合計時間を混ぜない。
定額料金しか分からなければ、個別作業の実課金額を推測で生成しない。

## 4. 条件付きで分かったこと

- 確認できた事実：UNSET
- 効果・失敗原因についての仮説：UNSET
- 人とAIの分担で有効だった条件：UNSET
- 人が補った不足、AIの修正、見逃し・手戻り：UNSET
- 再利用できる入力契約・指示・確認項目：UNSET
- 今回の事例だけでは判断できないこと：UNSET
- 次に小さく試す改善：UNSET

## 5. 改善案の扱い

- 変更したい標準・テンプレート・作業方法：UNSET
- 期待する効果と、悪化させたくない指標：UNSET
- 次の観測対象と比較条件：UNSET
- 既認可内で試せる範囲：UNSET
- 必要な人の変更承認と、その参照：UNSET

このログだけで能力を保証したり、AIの実行権限を増やしたりしない。
SHIRABE/HIBIKIとの将来接続は検討対象として記し、導入済みと仮定しない。
独自JSONや専用ランタイムをこの記録の前提にしない。

関連：[STD-12](../../governance/STD/STD-12_MEASUREMENT_AND_IMPROVEMENT.md)、[T-04](../../governance/templates/T-04_VERIFICATION_RECORD.md)、[T-07](../../governance/templates/T-07_DECISION_RISK_EXCEPTION.md)
