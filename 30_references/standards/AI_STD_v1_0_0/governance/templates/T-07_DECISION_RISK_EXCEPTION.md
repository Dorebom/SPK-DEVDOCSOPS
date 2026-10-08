---
template_id: T-07
title: 決定・リスク・課題・例外記録テンプレート
version: 1.0.0
status: DRAFT_FOR_ADOPTION
updated: 2026-10-07
---

# T-07 決定・リスク・課題・例外記録テンプレート

> テンプレート版 1.0.0 / 2026-10-07 / DRAFT_FOR_ADOPTION（採用・業務承認前）。
> 一記録につき種類を一つ選ぶ。関連するリスク・判断・例外は別IDで接続し、該当しない節は省略可。
> `UNSET` や未署名の欄は、承認・解決・受容を意味しない。

コピー後のメタデータとリンクは実際の配置先に合わせる。対象外は理由、不明事項は確認担当・予定を添える。

## 1. 識別と責任

| 項目 | 記入 |
|---|---|
| `record_id` | UNSET |
| `record_type` | UNSET（DECISION / RISK / ISSUE / EXCEPTION） |
| 要約 | UNSET |
| 関連する作業・要求・設計・版 | UNSET |
| 関連する別記録ID | UNSET |
| 発見したActor・発見日時 | UNSET |
| 調査・処置するActor | UNSET |
| 人の責任者 | UNSET |
| 次回確認・必要な判断期限 | UNSET |
| 作業影響区分 | UNSET（R0 / R1 / R2。リスク重大度とは別） |
| 記録の状態 | OPEN |

状態の候補：RISK/ISSUEは `OPEN / IN_REVIEW / CLOSED`、DECISIONは `OPEN / APPROVED / REJECTED / SUPERSEDED`、EXCEPTIONは `OPEN / APPROVED / REJECTED / EXPIRED / CLOSED`。
これらは本記録の状態であり、作業票の状態と混同しない。

## 2. 確認できたこと

- 観測時点・対象環境・対象版：UNSET
- 事実と証拠の参照：UNSET
- 仮説・推定：UNSET
- 未確認・取得できていないもの：UNSET
- 影響する境界・対象：UNSET
- 影響しないと判断した範囲と根拠：UNSET

「未確認」と「影響なし」を区別する。試験結果は PASS / FAIL / NOT_RUN / BLOCKED / INCONCLUSIVE で記す。

## 3. リスクまたは課題

- 起こり得る事象 / 現在起きている問題：UNSET
- 発生条件・到達経路・関連する前提：UNSET
- 影響、起こりやすさ、検知可能性、未知の範囲：UNSET
- 重大度と使用した判定基準：UNSET（不足時はUNKNOWN）
- 対策候補：UNSET
- 採る対策・担当・対応作業ID：UNSET
- 残存する影響、不確実性、監視・復旧方法：UNSET
- リスク受容が必要か、必要なら判断する人：UNSET
- 処置完了・解除・終了の条件：UNSET

## 4. 判断案

| 選択肢 | 具体的な変更・行動 | 利点 | 欠点・残存影響 | 必要な前提・証拠 |
|---|---|---|---|---|
| UNSET | UNSET | UNSET | UNSET | UNSET |

- 推奨案と理由：UNSET
- 判断しない場合の影響：UNSET
- 判断してほしい事項と適用範囲：UNSET
- 既認可内で先に進める作業：UNSET
- 人の判断まで保留する境界：UNSET

## 5. 例外申請

- 逸脱する標準ID・条項と通常要求：UNSET
- 逸脱が必要な理由：UNSET
- 対象製品・版・作業・環境 / 対象外：UNSET
- 開始条件・適用期間：UNSET
- 有効期限または終了イベント：UNSET
- 次回確認日：UNSET
- 代替の確認・制御・監視：UNSET
- 残存リスクと受容が必要な人：UNSET
- 取消条件と復旧・通常手順への復帰方法：UNSET
- 上位要件との整合を確認した根拠：UNSET

本票だけで法令、契約、認証条件、組織の必須規則を免除したとは扱わない。
例外承認前、期限切れ、範囲外、前提変化の場合は該当逸脱を実行しない。

## 6. 人の判断・承認

| 項目 | 記入 |
|---|---|
| 判断 | PENDING（APPROVE / CHANGES_REQUESTED / REJECT / PENDING） |
| 判断の対象 | UNSET（選択肢・残存リスク・例外条件等） |
| 判断する人・役割 | UNSET |
| 判断日時 | UNSET |
| 対象とした案の版・参照 | UNSET |
| 理由・適用条件・有効期限 | UNSET |
| 明示的な判断の参照 | UNSET |

人が複数の役割を兼ねる場合も、その時点で確認した観点を記す。
承認待ち時間：UNSET（レビュー可能な案の提出日時→判断日時、未判断なら観測時点まで）

## 7. 実施・終了確認

- 実施した処置・対象版・実行Actor・日時：UNSET
- 確認した評価結果と証拠：UNSET
- 残る問題・リスクと関連ID：UNSET
- 作業票の阻害解除に必要な条件を満たしたか：UNSET
- 例外の終了・通常手順への復帰確認：UNSET
- 終了確認をした人・日時・根拠：UNSET
- 再開すべき条件：UNSET

試験PASS、本票の終了、作業ACCEPTED、リリースはそれぞれ別の状態・判断とする。

関連：[STD-11](../../governance/STD/STD-11_RISK_AND_EXCEPTIONS.md)、[T-01](../../governance/templates/T-01_WORK_TICKET.md)、[T-02](../../governance/templates/T-02_CHANGE_IMPACT.md)
