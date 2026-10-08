---
template_id: T-06
title: 基準計画テンプレート
version: 1.0.0
status: DRAFT_FOR_ADOPTION
updated: 2026-10-07
---

# T-06 基準計画テンプレート

> テンプレート版 1.0.0 / 2026-10-07 / DRAFT_FOR_ADOPTION（採用・業務承認前）。
> 基準計画の承認、個々の作業認可、成果受入、リリース承認は別の判断として記録する。
> 空欄や `UNSET` は未確認・未承認を意味する。コピーしただけで計画を有効にしない。

コピー後のメタデータとリンクは実際の配置先に合わせる。対象外は理由、不明事項は確認担当・予定を添える。

## 1. 計画の識別

| 項目 | 記入 |
|---|---|
| `baseline_id` | UNSET |
| 前の `baseline_id` | UNSET（初版ならNONE） |
| プロジェクト・対象リリース | UNSET |
| 計画記録の状態 | DRAFT（DRAFT / APPROVED / SUPERSEDED） |
| 作成日・基準時点・タイムゾーン | UNSET |
| 作成Actor / 人の計画責任者 | UNSET / UNSET |
| 元となる要求・設計・変更記録 | UNSET |
| 正本の種類・場所 | UNSET |
| 関連するコード等の `base_revision` | UNSET（計画IDとは別） |
| `work_calendar` | UNSET |

## 2. 範囲と成立条件

- 達成する成果・マイルストーン：UNSET
- 対象の機能・版・機器・インターフェース：UNSET
- 対象外と、対象外にする根拠：UNSET
- 外部依存、利用可能な環境、人・AIの担当条件：UNSET
- 納期・予算・工数の制約と、承認元：UNSET
- 未確定の前提と、確定しない場合の影響：UNSET

## 3. 分母となる作業集合

重みは正の値とし、計画時に定義する。重複しない末端作業のみを含める。
実績工数や途中の出来高で重みを動かさない。親作業と子作業を同時に合計しない。

- `weight_basis`（相対規模等の定義）：UNSET
- 見積の根拠・前提：UNSET
- 作業集合の凍結時点：UNSET（未承認なら未凍結）
- 分母 $W=\sum_{i\in B}w_i$：UNSET

| 作業ID・作業票参照 | 成果 | `baseline_weight` | 主担当Actor | 人の受入者 | 受入条件・証拠 | 先行・外部依存 | 計画期限 |
|---|---|---:|---|---|---|---|---|
| UNSET | UNSET | UNSET | UNSET | UNSET | UNSET | UNSET | UNSET |

受入条件は [T-01](../../governance/templates/T-01_WORK_TICKET.md) の検証・受入条件へ参照してよい。
「実装完了」「担当者確認」だけにせず、成果物、必須評価、残課題の扱い、人の判断者を特定する。
作業票の `task_authorized_by / task_authorization_ref` が未成立なら、計画に載っていてもREADYとはしない。

## 4. 基準進捗率

$$
P_{accepted}=100\frac{\sum_{i\in B}w_i a_i}{W}
$$

$a_i=1$ は、有効な人の受入記録を持つ `ACCEPTED` の場合のみ。それ以外は0とする。
試験PASS、IN_REVIEW、部分進捗を分子へ加えない。
`CANCELLED` の作業を承認なしで分母から消さない。
必須データ不足や未承認の基準計画しかない場合、正式値は算出不可とする。

## 5. 旧計画からの差分

初版なら `INITIAL` とし、旧新比較は省略可。

- 変更の種類：UNSET（INITIAL / ADD / REMOVE / REWEIGHT / RESCHEDULE / OTHER）
- 変更要求・理由・影響分析の参照：UNSET
- 要求、品質、安全・認証、依存、納期・予算への影響：UNSET
- 代替案と、採用案の理由：UNSET

| 作業ID | 操作 | 旧重み | 新重み | 旧期限 | 新期限案 | 理由・影響 |
|---|---|---:|---:|---|---|---|
| UNSET | UNSET | UNSET | UNSET | UNSET | UNSET | UNSET |

追加は旧重みなし、削除は新重みなしと表記する。実作業の完成を意味する0とは区別する。

## 6. 同一時点での旧新比較

- 共通の観測時点：UNSET
- 受入状態・証拠の情報源：UNSET

| 対象 | 基準ID | 受入済み分子 | 凍結分母 | 進捗率 | 有効性 |
|---|---|---:|---:|---:|---|
| 旧基準 | UNSET | UNSET | UNSET | UNSET | UNSET |
| 新基準案 | UNSET | UNSET | UNSET | UNSET | 未承認 |

比率の変化の説明：UNSET（実際の受入増減と、分母変更の効果を分ける）
旧基準での報告は保存する。新基準承認前に正本の有効 `baseline_id` を切り替えない。

## 7. 人の承認と適用

| 項目 | 記入 |
|---|---|
| `decision` | PENDING（APPROVE / CHANGES_REQUESTED / REJECT / PENDING） |
| 承認する人・役割 | UNSET |
| 承認日時 | UNSET |
| 承認対象となる計画版・参照 | UNSET |
| 承認条件・残る制約 | UNSET |
| 有効化日時 | UNSET |
| 旧基準の保管参照 | UNSET |
| 正本の更新・読戻し確認 | UNSET |

無応答やAIの生成文を人の承認とみなさない。
承認対象を変更した場合は差分を示し、必要な変更承認を得る。

関連：[STD-04](../../governance/STD/STD-04_REQUIREMENTS_AND_CHANGE.md)、[STD-08](../../governance/STD/STD-08_PROGRESS_MANAGEMENT.md)
