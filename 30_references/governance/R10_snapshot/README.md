---
schema: spkgw.governance-note/v1
document_id: GOV-README
project: SPK-GW_HEMS
document_type: MOC
revision: 1.0.0
status: DRAFT_FOR_REVIEW
title: SPK-GW_HEMS 開発ワークスペース R10
owner: null
trace_id: TRC-SPKGW-000001
created_on: '2026-10-08'
updated_on: '2026-10-08'
classification: INTERNAL
source_baseline: BL-R9-0001
related_ids: []
---

# SPK-GW_HEMS 開発ワークスペース R10

**開発ガバナンスGOV-1.0.0を追加。製品システム仕様の選択BaselineはBL-R9-0001を変更していません。**

[開発ガバナンスMOC](00_governance/00_MOC.md) ／ [管理ツール操作](00_governance/Tool_Governance.md) ／ [ガバナンス未決事項](00_governance/Open_Questions.md) ／ [追加・保持検査](20_work/analysis/project/reports/GOV_QA.md)

新規の開発標準13本は、FrontMatter・TraceID・全作業タスク・工程・証拠・進捗・予算・変更・AI作業・リリース・報告・検証を扱います。個別の担当、予算、単価、正式期限は未設定。初期4タスクは導入準備の候補で、既存全開発タスクの棚卸しは未実施です。

```powershell
python -m pip install -r .\00_governance\requirements.txt
python .\tools\govcheck.py validate
python .\tools\govcheck.py report
```

既存R9のspecflowは下記のまま利用できます。tools追加によってtoolchain hashが変わるため、旧ツールで作った未公開prepare候補は再prepare・再承認してください。署名・本人認証・購買・量産操作の自動許可は行いません。

---

## 継承したR9の文書管理

# R9文書管理・現行仕様の参照

## 今回の構成

```text
00_governance/              文書作成STD・承認/公開ルール・ツール操作
10_canonical/
  CURRENT.json              現行文書Baselineを指す唯一のポインタ
  releases/BL-R9-0001/       5部44章・単一MOC・正本データ・生成ビュー
  receipts/                 文書Baselineの選択/採用記録
20_work/
  drafts/                   編集草案とprepare後の候補
  analysis/                 抽出断片・原文対照・競合判断・検証結果・承認要求
30_references/
  originals/                原資料そのもの（改変せず保管）
  baselines/R8_FIX001/       R8-FIX001原本の展開コピー（歴史参照・固定版監査用）
  reviews/                  今回採用した取り込みレビューと監査原本
  decisions/                ユーザーによる管理方式の採用記録
  source_register.json      受領文書・版・hash・適用範囲
schemas/                    管理データのJSON Schema
tools/                     コマンドと合成回帰テスト
```

[初回R9の全体MOC](10_canonical/releases/BL-R9-0001/00_MOC.md) ／ [初回統合版](10_canonical/releases/BL-R9-0001/90_All_In_One.md) ／ [操作手順](00_governance/Tool_Operations.md) ／ [変更記録](00_governance/R9_Change_Log.md)

上記リンクは配布時の初回版。以後の現行版は必ず `python tools/specflow.py current` で取得する。CURRENTを1回読んで得た同一snapshotを一連の読取に使用する。草案、旧版、統合版のファイル名や更新時刻だけで正本を選ばない。

## 最初の確認

```powershell
python -m pip install -r .\tools\requirements.txt
python .\tools\specflow.py current
python .\tools\specflow.py audit-baseline
python .\tools\specflow.py validate
python -m unittest discover -s .\tools\tests -v
```

Python 3.11以上。文書ツールの実測環境は同梱QAを参照。Windows11/WSL2での同手順を想定するが、この配布物の実行試験はLinux上であり、Windows・共有ストレージ・停電耐性を実証していない。

## 重要な境界

本版が選択済み正本であることは、全技術要求が承認済みという意味ではない。既存SYS要求124件、製品試験69件、既存OQ85件の状態は維持し、管理・実資料確認のOQ6件を追加した。未提示の旧Word/Excelを本番統合したわけではない。合成テスト値は現行仕様に入れない。

## Open Questions

[現行配布時の質問台帳](10_canonical/releases/BL-R9-0001/appendices/Open_Question_Register.md)。実原資料、正式USDM交換版、担当者、Windows運用・アクセス制御・規模条件を確定する。
