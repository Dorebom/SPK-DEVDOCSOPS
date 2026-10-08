# R9 仕様完成の進め方

正本の選択は10_canonical/CURRENT.json。選択済みの内容を直接編集しない。

## 1. 原資料から正本まで

30_references（原本）→20_work/analysis（抽出・原文対照・マージ判断）→20_work/drafts（仕様草案・要求・USDM候補）→prepare（検証済み候補）→明示承認→10_canonical（CURRENT切替）。

既存124 SYSはDRAFT_FOR_REVIEW、69製品試験はNOT_RUNを維持する。フォルダ名で承認状態を推定しない。

## 2. 編集正本

要求はdata/requirements.json、機能はdata/function_catalog.json、試験計画はdata/test_catalog.json、USDM中間モデルはdata/usdm.json、型付きリンクはdata/trace_links.json。質問の回答は各担当章末尾。権限と機種構成の詳細は規範別冊を正本とし、旧JSONスナップショットと二重編集しない。

## 3. 手順

[取り込み標準](../../../00_governance/STD_Import_Merge.md) と [ツール操作](../../../00_governance/Tool_Operations.md) を参照する。

## 4. 完成・未完了の区別

抽出済み、原文対照済み、採用判断済み、文書Baseline選択、製品要求承認、実装済み、実機試験済みを別状態として扱う。採用する詳細値・理由・機種適合・権限は未提示ならOQに残す。

## Open Questions — 本ガイドの適用

[質問台帳](appendices/Open_Question_Register.md)。旧85件の回答は保持し、追加6件は実資料・実運用の確認に限定する。
