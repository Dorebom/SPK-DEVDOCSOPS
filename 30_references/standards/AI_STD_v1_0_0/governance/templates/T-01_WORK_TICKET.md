---
template_id: T-01
ticket_id: TASK-XXXX
title: 記入する
state: DRAFT
impediment: NONE
risk_class: UNCLASSIFIED
owner: UNSET
base_revision: UNSET
candidate_revision: UNSET
baseline_id: UNSET
baseline_weight: UNSET
task_authorized_by: UNSET
task_authorization_ref: UNSET
updated_at: UNSET
---

# TASK-XXXX 作業チケット

> 未記入テンプレート。通常は `work/tickets/` にコピーし、実際の値で記入する。R0/R1はこの1ファイルに必要項目を集約してよい。既存Issueが正本なら各見出しをIssue本文へ移す。参照パスはプロジェクトルート基準で記録する。

`candidate_revision` は今回の候補を識別する版であり、検証・評価・受入で同じ対象を照合する。作業途中の検証が別版を対象とした場合は、その版を個別の実行記録に残す。`base_revision` は変更前のソース等の基準版、`baseline_id` は計画基準のIDである。

## 1. 目的・範囲・受入条件

| 項目 | 記入 |
| --- | --- |
| 作業種別 | 調査／要求／設計／実装／試験／保守／進捗更新 |
| 対象製品・HW・FW/SW | UNSET |
| 解決する問題・得たい成果 | UNSET |
| 変更対象・非対象 | UNSET |
| リスク分類と理由 | R0/R1/R2を選択、理由を記入 |
| 参照する要求・仕様・設計と版 | UNSET |
| 認可された作業範囲 | UNSET |
| 作業認可の根拠 | 指示、Issue、会議記録等の実在参照 |
| 受入責任者 | UNSET |

| AC-ID | 受入条件（観測可能な条件） | 検証方法・実施環境 | 結果・証跡 |
| --- | --- | --- | --- |
| AC-01 | UNSET | UNSET | NOT_RUN |

## 2. 作業計画

| 順 | 実施内容・成果 | 担当 | 依存・前提 | 見積り・予定 |
| --- | --- | --- | --- | --- |
| 1 | UNSET | UNSET | UNSET | UNSET |

`baseline_weight` は採用済み計画の値を転記する。実績に合わせて書き換えない。期日・優先順位を変える提案は判断記録へ分ける。

## 3. 差分・影響・設計メモ

| 変更対象 | 変更前→変更後 | 影響する要求・I/F・状態・データ | 対策・確認 |
| --- | --- | --- | --- |
| UNSET | UNSET | UNSET | UNSET |

影響があるときだけ `T-02`、`T-03` または既存設計書を参照して詳細化する。影響なしなら、調査した範囲と根拠を1〜数行で記す。

## 4. 実行記録

| 日時・担当 | 実施したこと | 対象版・成果物 | 観測した結果・証跡 |
| --- | --- | --- | --- |
| UNSET | UNSET | UNSET | UNSET |

時間を測る場合は人の作業時間、AI実行時間、待ち時間を区別する。機密や会話全文を無条件に貼り付けない。

## 5. 検証・レビュー

| 検証ID／観点 | コマンドまたは手順 | 期待値 | 実際の結果 | 結果区分 | 証跡・対象版 |
| --- | --- | --- | --- | --- | --- |
| UNSET | UNSET | UNSET | 未実施 | NOT_RUN | UNSET |

結果区分は `PASS / FAIL / NOT_RUN / BLOCKED / INCONCLUSIVE`。レビュー指摘は未解決/修正済み/採用しない理由が分かる形で記録する。詳しい結果は `T-04` に分けて参照してよい。

## 6. 現在地・阻害・次の行動

| 項目 | 記入 |
| --- | --- |
| state / impediment | ヘッダと一致させる |
| 事実として完了したこと | UNSET |
| 残作業 | UNSET |
| 阻害理由・発生日時 | NONE または実際の値 |
| 解除担当・次回確認 | UNSET |
| 完了予測・幅・前提 | UNSET |
| 判断待ち・選択肢・推奨 | NONE または判断記録参照 |
| 次に行う1〜3手順 | UNSET |

## 7. 受入記録

| 項目 | 記入 |
| --- | --- |
| accept_decision | PENDING / ACCEPT / CHANGES_REQUESTED |
| accepted_by | UNSET：実際に判断した人 |
| accepted_at | UNSET |
| acceptance_ref | UNSET：実在する判断記録 |
| candidate_revision | UNSET：判断対象の版 |
| 根拠・残課題の扱い | UNSET |

AIは根拠のある人の判断を転記できる。AI自身の「完了しました」はACCEPTの根拠にならない。ACCEPTEDにするには、STD-07の受入条件を満たす。

## 8. 引継ぎ

- 読む順番と正本：UNSET
- 基準版・現在版・未コミット差分：UNSET
- 実行済み検証／未実施検証：UNSET
- 未解決・変更してはいけない境界：UNSET
- 次の担当と次の手順：UNSET

## 参照

- [STD-03 作業管理](../../governance/STD/STD-03_WORK_CONTROL.md)
- [STD-07 検証と受入](../../governance/STD/STD-07_VERIFICATION_AND_ACCEPTANCE.md)
- [STD-08 進捗管理](../../governance/STD/STD-08_PROGRESS_MANAGEMENT.md)
