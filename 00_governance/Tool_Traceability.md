---
schema: spkgw.governance-note/v1
document_id: GOV-TOOL-TRACE-001
project: SPK-GW_HEMS
document_type: REPORT
revision: 1.2.0
status: DRAFT_FOR_REVIEW
title: 文書・項目・工程のTrace運用ガイド
owner: null
document_trace_id: DTR-SPKGW-GOV-000024
item_trace_ids: []
thread_id: THR-SPKGW-GOV-000001
related_thread_ids: []
trace_contract: spkgw.lifecycle-tags/v2
phase_ids: []
phase_scope: UNASSIGNED
activity_type: UNSPECIFIED
created_on: '2026-10-08'
updated_on: '2026-10-08'
classification: INTERNAL
source_baseline: BL-R9-0001
related_ids: []
---

# 文書・項目・工程のTrace運用ガイド

## 1. 正本

`20_work/analysis/project/trace_graph.json`のdocumentsは文書版（DTR）、nodesは項目版（ITR）、edgesは項目間、document_edgesは文書間の関係。profilesは任意のテーマ（THR）の工程計画。`control.json.traces`はTHR宣言の互換保管欄。本文・要求・費用をグラフへ複製しない。

IDは原本ファイルへ埋め込む必要はない。編集可能なガバナンスノートはFrontMatter、選択済みcanonicalと原資料はsidecarで対応する。文書一覧と項目一覧は[索引](../20_work/analysis/project/reports/TRACE_INDEX.md)を参照。

## 2. 検査と検索

```powershell
python -m pip install -r .\00_governance\requirements.txt
python .\tools\govcheck.py validate
python .\tools\tracecheck.py validate
python .\tools\tracecheck.py resolve --id SYS-RESP-001 --namespace item
python .\tools\tracecheck.py resolve --id ITR-SPKGW-REQ-000001
python .\tools\tracecheck.py document --id DTR-SPKGW-REGISTER-000001
python .\tools\tracecheck.py report --thread THR-SPKGW-GOV-000001
python .\tools\specflow.py validate
```

DTRの例は実際の索引から選ぶ。resolveは一意でなければ複数候補を返し、勝手に最新を選ばない。同じ文字列が旧文書IDと旧項目IDにあるTASK等ではnamespaceを指定する。`--trace`は旧CLIとの互換で、値はテーマTHRとしてだけ解決する。

report --require-linkedは不足時に終了コード2。validate PASSは形式・ローカル根拠確認であり、未割当やレビュー未了を完成に変えない。

## 3. 新規TASK

```powershell
python .\tools\govcheck.py new-task `
  --title "既存試験ケースを検証レベルへ対応付ける" `
  --thread THR-SPKGW-GOV-000001 `
  --wbs WBS-SPKGW-BOOT `
  --phase IMPROVE `
  --activity PROCESS_IMPROVEMENT
```

TASK IDに加え、当該タスクノートDTRとタスク項目ITRを採番し、グラフへ同時登録する。PROPOSEDとして作るのみで、着手・受入を代行しない。例外検出時は書込みを戻すが、実停電・共有FSでの完全な複数ファイルトランザクションを保証しない。Git・単一writer運用を併用する。

## 4. 項目と文書の改訂

文書は同じDTRの新revision、項目は同じITRの新revision/nodeを追加する。新しいnodeに新しい文書版とlocatorを指定し、旧node・旧reviewは保持する。元ファイルを同じ版で黙って上書きするとhash検査が失敗する。履歴版の実体も不変パスに保存する。文書の切り出し先が変わるだけなら項目ITRを再採番しない。

1項目を別冊にも表示する場合はoccurrences（VIEW）を追加する。旧SYS/native IDはnative_idsに保持。原本にない理由やrelationの確認者を生成しない。

## 5. 影響分析

```powershell
# resolveの結果にある版付きnode_idを指定する。
python .\tools\tracecheck.py impact --node ITR-SPKGW-REQ-000001_V_1
```

項目を起点にedgesの逆方向で再レビュー候補を探す。文書同士のreferences/generated_fromは技術的依存へ自動変換しない。未登録の関係・内容上の影響を見落とす可能性を残し、判断は人が行う。

## 6. Word/Excel・規格・コードへの適用

R9 specflowのregister/extractで原本hash、run、fragmentを確保し、DTRから原資料版、ITR-REFからローカル抽出JSONのfragmentへ結び付ける。selectorは`json:/…`又は`anchor:…`の実在を検査する。XML要素・セル番地・symbolは抽出記録内で保持する。元Officeを編集せず、マクロ・外部リンクを実行しない。GitのbranchやHEADを根拠にせず固定commitのローカル照合記録を使う。

## 7. 保存と検査範囲

validate/report/resolve/document/impactは読取専用。現行管理ノートを改訂したらDTR版の追加とlocator更新が必要。文書のhash一致、項目所在、型付き端点、ID一意性、既存native ID、工程略称を検査する。関係の意味、本人認証、規格適合、試験PASSの妥当性は自動承認しない。

古いR11のgraph v1は互換読出しのみで文書/項目分離の保証対象外。現行graphはv2で、DTRをimplementsやverifiesの端点に使うと拒否する。R9のprepare済み未公開候補はツールhash変更のため再prepare・再承認が必要。選択済みBL-R9-0001は変更しない。

## Open Questions

実担当・実成果・運用環境は[管理OQ](Open_Questions.md)で確定する。製品要求・工程完了の承認ではない。
