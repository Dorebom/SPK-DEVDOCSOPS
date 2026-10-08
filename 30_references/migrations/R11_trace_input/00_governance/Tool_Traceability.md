---
schema: spkgw.governance-note/v1
document_id: GOV-TOOL-TRACE-001
project: SPK-GW_HEMS
document_type: REPORT
revision: 1.1.0
status: DRAFT_FOR_REVIEW
title: Trace運用・17工程の記録確認ガイド
owner: null
trace_id: TRC-SPKGW-000001
created_on: '2026-10-08'
updated_on: '2026-10-08'
classification: INTERNAL
source_baseline: BL-R9-0001
related_ids: []
---

# Trace運用・17工程の記録確認ガイド

## 1. 利用する正本
| 情報 | 正本 |
|---|---|
| 17工程・作業種別・関係型 | `00_governance/lifecycle_profile.json` |
| TraceIDの宣言・工数・実行等 | `20_work/analysis/project/control.json` |
| TASK・主/関連Trace・工程 | `20_work/drafts/project/tasks/*.md` |
| 版付き成果・関係・工程適用表 | `20_work/analysis/project/trace_graph.json` |
| 仕様のSYS/USDM関係 | 選択Baselineの`data/trace_links.json`（既存R9） |

lifecycleのgraphは開発成果の版付き追跡用であり、R9のSYS/USDM採用関係を上書きするものではない。要求は原本ID・版へ参照し、同じ要求本文をgraphへ複製しない。会議や調査の草案はdrafts/project/meetings又はresearch、確定した実施記録・照合証拠はanalysis/project/records又はevidence、外部原資料は30_referencesへ配置する。新規成果の現行採用は既存の承認方式による。

## 2. 最初の検査
ワークスペース直下で実行する。

```powershell
python -m pip install -r .\00_governance\requirements.txt
python .\tools\govcheck.py validate
python .\tools\tracecheck.py validate
python .\tools\tracecheck.py report --trace TRC-SPKGW-000001
python .\tools\specflow.py validate
```

初期レジストリは既存ガバナンスTrace1件、17工程すべてTBD、成果node/edgeは未登録。実プロジェクトの移行済み・工程完了とはしていない。R10の4候補TASKは旧工程分類のまま保持し、TASK_NOT_IN_ARTIFACT_GRAPH等を警告する。

`validate`のPASSは形式・参照検査の成功であり、未入力の台帳が完成している意味ではない。`report`のrecord_chain_ready=falseを隠さない。

## 3. 新規TASKの作成
既存ガバナンス導入Traceの例：

```powershell
python .\tools\govcheck.py new-task `
  --title "Trace運用の既存作業を棚卸しする" `
  --trace TRC-SPKGW-000001 `
  --wbs WBS-SPKGW-BOOT `
  --phase P17 `
  --activity PROCESS_IMPROVEMENT
```

これはPROPOSEDの作成であり実行・承認ではない。実製品の独立テーマは、control.jsonのTrace/WBSに目的と根拠を先に登録して使う。複数Traceには`--related-trace`、複数工程には作成後phase_idsを追記しphase_scope=CROSS_PHASEとする。主P番号をphase_idsから落とさない。

既存TASKのphaseを勝手に17工程へ読み替えない。DISCOVERY、DESIGN、VERIFICATION、MANAGEMENT等の移行候補はSTD-GOV-005にある。R11属性を持つ新規契約TASKは工程・作業種別未定のまま着手できない。旧TASKの着手条件はR10互換のままなので、旧値を使い続ける運用を移行タスクで解消する。

## 4. 成果と関係を登録する
1. control.jsonのTraceを宣言し、trace_graph.jsonのprofilesへ同IDのscopeと17工程のphase_planを記入する。
2. 成果物の安定artifact_idとrevisionを決め、版付きnode_id、kind、主/関連Trace、phase_idsを登録する。
3. 計画中はPLANNED＋locator=null＋review=null。実体ができたらRECORDEDとし、ローカルpath・sha256を記入する。外部コード等は承認された固定commitの参照情報・取得証拠をローカルに残す。外部URLだけで取得確認済みにしない。
4. edgeにfrom_node、to_node、relation、basis、reviewを記入する。向きは依存する側→根拠側。両方向検索のために逆edgeを重複作成しない。
5. 実確認後だけreview=CONFIRMEDにする。reviewerはcontrol.jsonに存在するActor、reviewed_at、rationale、ローカル証拠path/hashが必要。

`review.subject_sha256`は、対象recordからreview・selected・activeを除いたJSONの正規化SHA-256。`tracecheck.subject_hash(record)`が計算する。本文／版／関係を変えたら旧確認は不一致になるため再確認する。hash再計算だけで本人確認・承認したことにはならない。ファイルへの書込み権限・レビュー運用が必要。

selectorを使う場合は`anchor:明示HTMLアンカー`又は`json:/records/0/id`を使う。Markdownの自動見出しアンカー、任意行番号、Git symbolの解釈は本ツールでは検証しない。selectorなしはファイル全体の参照。

[Trace計画テンプレート](templates/Trace_Plan.md)／[JSON記入例](templates/trace_graph.example.json)／[会議](templates/Meeting.md)／[調査](templates/Research.md)。JSON例は記入途中のノード例であり、実製品の承認済み台帳ではない。

## 5. 工程レポート・逆参照
```powershell
python .\tools\tracecheck.py report --trace TRC-SPKGW-000001
python .\tools\tracecheck.py report --trace TRC-SPKGW-000001 --require-linked
```

`--require-linked`は記録鎖未完なら終了コード2。形式異常は1、形式又は指定した記録条件の成功は0。初期台帳の終了コード2は予定どおり。

| 表示 | 意味 |
|---|---|
| TBD | 工程の適用が未定 |
| NOT_APPLICABLE | 根拠・確認記録付きで対象外 |
| REQUIRED_OUTPUTS_UNDEFINED | 必須成果種別が未記入 |
| MISSING／PLANNED_ONLY | 必要記録がない／予定だけ |
| PENDING_REVIEW | 原本はあるが確認未了 |
| GAP | 上流根拠・必要成果・版付きリンクに不足 |
| LINKED_RECORDS | 必要kindの確認済み記録が根拠rootへ接続。製品合格ではない |

selected_unconnected_nodesは技術的根拠鎖から外れるノード。会議はdiscussesでcontext_linked_nodesに入り、技術的なimplements/verifiesの代用にはしない。context_unconnected_nodesには議題等の孤立・未確認を出す。いずれも工数進捗や合格率へ変換しない。

```powershell
# <登録済みnode_id>を実際の値へ置き換える。
python .\tools\tracecheck.py impact --node "<登録済みnode_id>"
```

impactは依存関係の逆向きに到達する再レビュー候補。すべての影響を保証しない。変更した機器条件、計測点、パラメータ、頻度等の意味は人が確認する。

## 6. 保存と変更
本ツールは読取専用。必要なレポートはanalysis/project/reportsへ新しい名前で保存し、同じ報告を無言で上書きしない。入力hashをレポートに含める。台帳を並行編集する場合はGit又は運用ロックで排他し、schema・ID・参照を再検証する。図・報告だけ編集して正本データの問題を隠さない。

R11はスキーマとgovcheckを変更するためtoolchain hashが変わる。旧ツールでprepareした未公開候補は再prepare・再承認が必要。選択済みBL-R9-0001は変更していない。

## 7. 自動化していないこと
実成果の全量自動登録、Word/Excelの意味判断、外部Gitのfetch、課題管理サービスとの同期、機密アクセス制御、確認者本人の認証、管理Baselineの自動採用、費用の多対多配賦、製品・安全・認証の評価は行わない。SYS等を登録したnodeのartifact_idと指定資料中の意味的同一性も、人が原資料で確認する。

## Open Questions
実テーマ・旧TASKの割当、外部成果の保存方式、工程別必須成果、担当と配賦は[Open Questions](Open_Questions.md)のOQ-GOV-TRACE-01〜04で管理する。
