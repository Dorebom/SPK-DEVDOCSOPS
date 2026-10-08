# R9 ツール操作ガイド

すべてワークスペース直下で実行する。Python 3.11以上、jsonschema 4.26.0を使用。Office/マクロ/外部ネットワーク呼出しは行わない。

## 1. 現行と原本を確認

```powershell
python -m pip install -r .\tools\requirements.txt
python .\tools\specflow.py current
python .\tools\specflow.py audit-baseline
python .\tools\specflow.py validate
```

CURRENTのhashが不一致なら、正本を直接修正して辻褄を合わせず原本又は採用記録から復旧する。

## 2. 原資料の登録・抽出

```powershell
$Registered = python .\tools\specflow.py register --file "C:\specs\PCS_Protocol.docx" --document-id LEGACY-PCS --revision 1.0 --basis AS_IS | ConvertFrom-Json
$SourceId = $Registered.source.source_id
$Extracted = python .\tools\specflow.py extract --source $SourceId | ConvertFrom-Json
$RunId = $Extracted.run_id
```

結果は30_references/source_register.jsonとanalysis/imports/<RunId>に保存する。原資料のSOURCE_APPROVEDは原本の承認証拠を確認して別途登録する。registerの既定はUNVERIFIED。

## 3. 草案作成と原文対照

```powershell
python .\tools\specflow.py new-draft --id DR-001
python .\tools\specflow.py review-fragment --run $RunId --fragment "FRAG-実ID" --by "実担当者" --note "表ヘッダ・単位・対象FW・注記を原本と対照した記録"
```

草案の編集先は20_work/drafts/DR-001。analysis内の抽出原文を直接書き換えない。図・table mergeなど断片外の文脈を確認してreview_noteに記録する。

## 4. 解釈候補と採否

templates/scope.example.jsonをコピーして対象条件を記入する。コマンドの`--scope-file`に渡す。数値例は製品値ではない。

```powershell
python .\tools\specflow.py candidate --draft DR-001 --id CAND-001 --run $RunId --fragment "FRAG-実ID" --target-kind SYS --target SYS-IMPORT-001 --interpretation "原文から確認した仕様の解釈" --classification ADDITION --scope-file .\20_work\analysis\scope.json
python .\tools\specflow.py decide --draft DR-001 --candidate CAND-001 --action ADOPT --by "実承認担当" --rationale "対象版と既存要求の重複・競合を確認した根拠"
```

分類はEQUAL/ADDITION/DETAIL/SCOPE_VARIANT/CONFLICT/OBSOLETE/INSUFFICIENT/UNCLASSIFIED。CONFLICTは`--resolution`で解決根拠を記録するまでADOPT不可。DEFER/REJECT/REFERENCE_ONLYはcanonicalへ本文を追加しない。

## 5. SYS/USDMレコードへの反映

templates/requirement.example.json又はusdm.example.jsonを作業へコピーし、ID、実本文、source_ids、章、適用、検証を記入する。既存SYSと重複していれば新IDを増やさず詳細化又は出典追加を検討する。

```powershell
python .\tools\specflow.py apply-record --draft DR-001 --candidate CAND-001 --record .\20_work\analysis\SYS-IMPORT-001.json
python .\tools\specflow.py validate --draft DR-001 --no-freshness
```

apply-recordは草案だけを変更する。要求→試験を追加した場合はtest_catalog.jsonの逆向き対応も更新する。機能、IF、設定、データ辞書、本文、OQの関連箇所は草案で明示編集し、別冊の矛盾をレビューする。自動生成部分はprepareで更新する。

## 6. 一式生成・検査・承認

```powershell
python .\tools\specflow.py prepare --draft DR-001
```

成功するとPREP-*候補とanalysis/approvals/DR-001.request.jsonが作られる。analysis/draft_records/<草案ID>.diff.jsonの全変更ファイル・旧新hashと、原資料・マージ判断、適用条件、OQ、禁止経路への影響、検証報告を確認する。

承認者がrequest.jsonを別名のapproval.jsonへコピーし、decisionをAPPROVE_DOCUMENT_BASELINE、approved_by/approved_at/rationaleを実記録で記入する。候補hash・元Baselinehash・toolhashを書き換えない。product_requirements_approvedはfalseのまま。これは文書Baselineの選択承認であり全製品要求の承認ではない。

```powershell
python .\tools\specflow.py publish --draft DR-001 --approval .\20_work\analysis\approvals\DR-001.approval.json
python .\tools\specflow.py current
python .\tools\specflow.py validate
```

公開済みの同候補を再実行しても二重追加せずALREADY_SELECTED。元Baselineが変わった場合はSTALE_BASEで停止するので、新しい草案で差分を再レビューする。元hashだけ更新して強行しない。

## 7. 再取り込み・旧形式

同じregister/extractの再実行は既存IDを返す。原資料改版又は抽出器変更は新runを作り、`compare-runs --old RUN-... --new RUN-...`で位置変更/同一文字/削除候補を確認する。既存採用IDを無断削除しない。

```powershell
python .\tools\specflow.py coverage --run $RunId
```

coverageは断片ごとの未分類・レビュー中・判断記録・現行Baseline採用の別と、未処理オブジェクトを出す。ADOPTの判断記録だけでは正本へ採用済みと表示しない。資料全体の受入・意味の完全性は自動認定しない。

旧.doc/.xlsは登録後BLOCKED_MANUALとする。原本を残して認可された別変換を行い、変換後ファイルは別source_idで登録・関連付ける。

## 8. 失敗・ロック・旧版への戻し

生成失敗時はCURRENTと選択済みsnapshotを維持する。publishのCURRENT切替前に止まると未選択releaseが残り得るが現行は変わらない。履歴を先に削除しない。

.workspace.lockが残った場合はPIDと運用記録を確認し、実行中writerがないことを確認した担当者だけが除去する。自動的にロックを破らない。承認済み旧snapshotを再選択する復旧は、単なる「最新フォルダ名」ではなく記録されたhashと理由を検証して実施する。自動rollbackコマンドは今回未実装。

## Open Questions

実原資料と正式担当者、外部USDM形式、Windows/共有ストレージ・実停電、Git/署名承認を含む運用はOQ-R9-IMP-01〜06で確認する。
