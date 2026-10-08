# R11 Trace・工程管理の検証記録

実施日：2026-10-08。ワークスペースR10を基に、17工程と関連調査・会議のTrace管理を補強した検証。製品機能の受入記録ではない。

## 実測結果

| 検査 | 結果 |
|---|---|
| 新規Trace合成テスト | 40件 PASS |
| 既存ガバナンス回帰 | 44件 PASS |
| 既存specflow回帰 | 47件 PASS |
| 合計 | **131件 PASS** |
| 現行管理データ | govcheck PASS。実担当・予算等の従来未決と旧TASK移行警告あり |
| Trace台帳形式 | PASS。ただし実成果node=0、edge=0、工程適用17件すべてTBD |
| Traceの記録鎖完成 | **false：実テーマ・成果の移行は未実施** |
| 選択済みcanonical | 122ファイルのバイト一致、CURRENTとBL-R9-0001を変更せず |
| 既存30_references | 331ファイルのバイト一致、新CTX・変更前snapshotのみ追加 |
| 既存TASK | 4件バイト一致、未確認の工程再分類なし |
| control.json | バイト一致。実Actor・費用・予算・実行は未追加 |
| 変更前ファイル履歴 | 22件の変更前バイト・変更後hashを台帳と照合 |

## 新規検査の重点

17工程の証拠参照、工程適用未定、N/Aの根拠、複数Traceの共通調査・会議、discussesだけでは技術的根拠にならないこと、要求変更から設計・コード・試験・リリース／導入への逆参照、旧版リンク、空・重複・不明ID、ローカルhash、対象の変更による確認記録の失効、会議孤立、読取専用性を検査した。

schema・relation検査は内容の正当性・Actor本人認証ではない。CONFIRMEDは登録した確認宣言と対象hashの整合であって、署名検証ではない。新規TASKへのR11属性を検査するが、既存R10 TASKは互換であり自動移行していない。

## 再現

```powershell
python -m unittest discover -s .\tools\tests -v
python .\tools\govcheck.py validate
python .\tools\tracecheck.py validate
python .\tools\tracecheck.py report --trace TRC-SPKGW-000001
python .\tools\specflow.py validate
```

入力・テストの詳細：[Summary](R11_Verification_Summary.json)／[Trace tests](R11_Trace_Tests.log)／[Governance tests](R11_Governance_Tests.log)／[Specflow tests](R11_Specflow_Tests.log)／[初期Trace](R11_Trace_Initial_Report.json)。

## 実行環境・限界

Python 3.13.5、PyYAML 6.0.3、jsonschema 4.26.0。Linuxで実行。Windows・共有ストレージ・実停電・外部Git・実プロジェクト全量移行・製品実機・JET評価は未実施。日付・ロール・成果・費用のテストデータは隔離された一時ディレクトリだけに作成した。

## Open Questions

[ガバナンスOQ](../../../../00_governance/Open_Questions.md)の実担当、対象Trace、旧工程対応、実成果・外部証拠、工程別受入条件を解消する。検査PASSだけで未決事項を閉じない。
