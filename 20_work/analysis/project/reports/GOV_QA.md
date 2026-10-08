---
schema: spkgw.governance-note/v1
document_id: GOV-20-work-analysis-project-reports-GOV-QA
project: SPK-GW_HEMS
document_type: REPORT
revision: 1.0.0
status: GENERATED
title: R10 ガバナンス追加 検証記録
owner: null
trace_id: TRC-SPKGW-000001
created_on: '2026-10-08'
updated_on: '2026-10-08'
classification: INTERNAL
source_baseline: BL-R9-0001
related_ids: []
---

# R10 ガバナンス追加 検証記録

## 実行結果

| 検査 | 結果 | 範囲 |
|---|---|---|
| 管理機能合成回帰 | 44件 PASS | FrontMatter、TASK、Trace、依存、証拠、受入、工数・費用・予算集計 |
| 既存R9回帰の再実行 | 47件 PASS | 原資料抽出・マージ判断・USDM・生成・承認・公開の既存契約 |
| R9現行文書検証 | PASS | 44章・124要求・69試験・91OQ、参照と生成鮮度 |
| 原本監査 | PASS | R8-FIX001元ZIP・展開324ファイルと補修済み原本 |
| 追加前後の保存比較 | PASS | 既存current/選択release/受領原本/既存ツール・schemas/既存STD本文を保持 |

入力R9の実ファイル数：495。ルートManifestの再生成、ルートREADME.mdとpackage_info.jsonの変更を除き、全既存ファイルはバイト不変。製品文書CURRENT.jsonはBL-R9-0001を指したまま。

## 合成テストの主な内容

欠落・重複FrontMatter、型不正、存在しないTrace/要求/Actor、依存循環、Owner/見積/着手判断のない実行状態、証拠なしDONE、AIによる人の受入代行、証拠hash改変、パス逸脱、summary二重計上、同一原票二重計上、異通貨・異税基準、発注超過、ETCの発注残不足、正確なdecimal計算、原価取消、未締め時のEAC抑止、分母固定進捗、新TASK追加、EXE逆リンクを確認した。

試験の例：AC=100、未履行発注残=200、OCを含むETC=400のときEAC=500。700と二重計上しない。これらはSYNTHETIC_ONLYであり、実プロジェクトの予算や実績ではない。

## 初期データ

導入準備4TASKはPROPOSED。Actor未割当、基準計画・予算なし、実績締め未確認。EAC/VACと成果進捗はnull。記録額0を実費0とは表示しない。既存全作業の棚卸し・実予算移行は未実施。

## 再現

```powershell
python -m pip install -r .\00_governance\requirements.txt
python -m unittest discover -s .\tools\tests -p test_governance.py -v
python -m unittest discover -s .\tools\tests -p test_specflow.py -v
python .\tools\govcheck.py validate
python .\tools\specflow.py validate
```

## 証拠

[管理テストログ](governance_unittest.log) ／ [R9回帰ログ](r9_regression_unittest.log) ／ [保存比較](R9_R10_Preservation.json) ／ [管理検証](Governance_Validation.json) ／ [初期集計](Management_Initial_Report.json) ／ [R9文書検証](R9_Model_Validation.json) ／ [原本監査](R9_Original_Audit.json) ／ [リンク検査](Governance_Links.json)

## 限界

実行環境はLinux/Python。Windows、共有ストレージ、実停電、Git/IDEの承認設定、実人事・会計・購買との照合、製品実機・安全・認証評価は未実施。ツールは全STDの強制・完全な認可エンジン・スケジュール最適化・EVM・為替換算・自動発注を実装していない。JSONの承認Actorは本人認証の証拠ではない。

## Open Questions

[ガバナンス未決事項](../../../../00_governance/Open_Questions.md)の実担当・予算・締め・運用環境を確定する。
