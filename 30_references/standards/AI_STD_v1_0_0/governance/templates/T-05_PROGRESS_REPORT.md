---
template_id: T-05
title: 進捗報告テンプレート
version: 1.0.0
status: DRAFT_FOR_ADOPTION
updated: 2026-10-07
---

# T-05 進捗報告テンプレート

> テンプレート版 1.0.0 / 2026-10-07 / DRAFT_FOR_ADOPTION（採用・業務承認前）。
> このファイル自体は実績報告ではない。`UNSET` を観測値・参照で埋め、未取得は未取得のまま残す。
> 正本から作るスナップショット。週報を第二の作業正本にしない。

コピー後のメタデータとリンクは実際の配置先に合わせる。対象外は理由、不明事項は確認担当・予定を添える。

## 1. 報告条件

| 項目 | 記入 |
|---|---|
| `report_id` | UNSET |
| 対象プロジェクト・範囲 | UNSET |
| 対象期間 | UNSET |
| `as_of`（タイムゾーンを含む） | UNSET |
| 作成Actor / 人の進捗責任者 | UNSET / UNSET |
| `progress_source_of_truth` | UNSET（MARKDOWN / ISSUE_TRACKER） |
| `progress_source_location` | UNSET |
| 情報源の版・コミット・取得時刻 | UNSET |
| 参照した承認済み `baseline_id` | UNSET |
| 取得できなかったデータ・対象外 | UNSET |
| 実測 / 申告 / 推定の区別 | UNSET |

## 2. 今回の判断に必要な要点

- **確認済み事実**：UNSET（作業ID・証拠を添える）
- **仮説・予測**：UNSET（根拠・不確実性を添える）
- **判断待ち**：UNSET（誰が・何を・いつまでに）
- **次に行うこと**：UNSET（認可内の具体的行動）

## 3. 受入済み進捗

| 指標 | 値 | 根拠・留意事項 |
|---|---|---|
| 基準計画の末端作業数 | UNSET | 親子の二重計上を除外 |
| 凍結分母 $\sum w_i$ | UNSET | 重みの定義：UNSET |
| 受入済み分子 $\sum w_i a_i$ | UNSET | 人の有効な受入記録のみ |
| 正式進捗率 $100\sum w_i a_i/\sum w_i$ | 算出不可 | 根拠が揃うまで値を入れない |
| 受入済み件数 / 基準作業数 | UNSET | 参考。重み付き進捗と区別 |
| 計画外作業の件数・影響 | UNSET | 未承認で分母に混ぜない |

| 作業ID | `baseline_weight` | 状態 | `impediment` | `acceptance_ref` | 部分進捗・未実施 | 最終観測・証拠 |
|---|---:|---|---|---|---|---|
| UNSET | UNSET | UNSET | UNSET | UNSET | UNSET | UNSET |

`IN_REVIEW`、テストPASS、実装済みは受入済み分子に入れない。部分進捗を別列に記す。
状態・重み・基準・受入記録の不足があれば、その対象を示して正式値を「算出不可」とする。例外付き受入がある場合は、件数・重み・残条件・例外期限を別記する。

## 4. 基準計画の変更

- 変更の有無：UNSET（NONE / PROPOSED / APPROVED）
- 変更理由、対象要求、追加・削除・重み変更：UNSET
- 変更記録と人の承認参照：UNSET
- 適用時点：UNSET（承認前は未適用）

| 同一観測時点 `as_of` | 基準ID | 分子 | 分母 | 進捗率 | 有効 / 案 |
|---|---|---:|---:|---:|---|
| UNSET | 旧：UNSET | UNSET | UNSET | UNSET | UNSET |
| UNSET | 新：UNSET | UNSET | UNSET | UNSET | UNSET |

変更がなければ `NONE` とし、この比較表は省略可。旧報告は保存する。

## 5. 期限と予測

| 作業・マイルストーン | 承認済み計画期限 | 最新予測・幅 | 予測根拠・前提 | 不確実性 / 必要な判断 |
|---|---|---|---|---|
| UNSET | UNSET | UNSET | UNSET | UNSET |

予測更新で計画期限を上書きしない。納期変更の承認が必要なら判断待ちへ載せる。

## 6. WIP・待ち・手戻り

| 主担当 | WIP / 上限 | BLOCKED数 | 超過理由・解消行動 | 次回確認 |
|---|---|---|---|---|
| UNSET | UNSET | UNSET | UNSET | UNSET |

| 作業ID | 待ち理由・依存先 | 待ち開始 | 経過時間と単位 | 解除条件・担当 | 次の確認 |
|---|---|---|---|---|---|
| UNSET | UNSET | UNSET | UNSET | UNSET | UNSET |

- 人の投入工数：UNSET（実測 / 申告 / 未取得）
- AI実行時間：UNSET（取得元 / 未取得）
- 手戻りの件数・理由・修正工数：UNSET
- ボトルネック候補：UNSET（確認済み原因と仮説を分ける）
- 時間の定義・使用カレンダー・重複待ちの扱い：UNSET

## 7. リスクと判断待ち

| 記録ID | 事実・不足 | 影響 | 次の行動 | 人の責任者 | 判断期限 | 保留する境界 |
|---|---|---|---|---|---|---|
| UNSET | UNSET | UNSET | UNSET | UNSET | UNSET | UNSET |

## 8. 次の期間の作業

| 作業ID | 具体的な次の一手 | 実行Actor | 作業認可参照 | 成果・観測予定 | 依存条件 |
|---|---|---|---|---|---|
| UNSET | UNSET | UNSET | UNSET | UNSET | UNSET |

## 9. 正本への反映確認

| 項目 | 記入 |
|---|---|
| `reflection_status` | UNSET（NOT_NEEDED / APPLIED_VERIFIED / PENDING / FAILED） |
| 反映先・対象ID | UNSET |
| 実際に変更した欄 | UNSET |
| 書込み結果・更新版またはツール実行参照 | UNSET |
| 読戻し確認時刻・内容 | UNSET |
| 未反映差分・次に必要な操作 | UNSET |

`APPLIED_VERIFIED` は書込みと読戻しを確認したときだけ使う。
この報告を会話へ表示しただけの場合、正本更新は `PENDING` または更新不要なら `NOT_NEEDED` とする。
外部通知・送信をしたかは別に記録し、未実施を実施済みにしない。

関連：[STD-08](../../governance/STD/STD-08_PROGRESS_MANAGEMENT.md)、[T-06](../../governance/templates/T-06_PLAN_BASELINE.md)、[T-07](../../governance/templates/T-07_DECISION_RISK_EXCEPTION.md)
