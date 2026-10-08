# SPK-GW_HEMS システム仕様書 R8

**[全体MOCから読む](00_MOC.md)**

ユーザーが指定した5部構成を、1冊のMOCと44章の実本文へ再編したレビュー用ドラフト。R7と同じ版名で上書きせず、R8を現行識別とする。

[統合版](90_All_In_One.md) ／ [再編判断](appendices/R8_Structure_Decisions.md) ／ [旧新章対応](appendices/Chapter_Migration_Map.md) ／ [仕様完成ガイド](01_Completion_Guide.md) ／ [文書QA](DOCUMENT_QA.md)

R7の機能・要求・OQの意味と既存接続条件を引き継ぐ。機能採否、実型式・数値・権限・認証を新たに確定したものではない。章末OQを完成させるための作業入口とする。

履歴はsources/r7_snapshotに隔離する。原本ZIPのハッシュと非ZIP原本の保存範囲はdata/input_manifest.jsonを参照。過去版ZIPの再帰同梱は行わない。


<a id="open-questions"></a>
**配布補修 R8-FIX001（2026-10-08）：** R8の構成・機能・要求は不変。R7由来のハッシュ一覧3ファイルを復元し、ZIPの保存宣言を再検証した。詳細は[補修ログ](REPAIR_LOG_FIX001.txt)および[文書QA](DOCUMENT_QA.md)。

## Open Questions — 本ノートの完成に必要な確認


### 他章で回答する関連質問

| OQ・正本章 | 残る判断 | 完了条件 |
|---|---|---|
| [OQ-R6-19-02](chapters/V_Lifecycle/V-07_Trace_Open_Questions.md#oq-r6-19-02) | 各OQの実担当者、回答期限、提案G0〜G4の採否と正式レビュー日をどう定めるか。未決のまま許される作業と停止する判断はどこか。 | OQへ担当・期限・決定者を記入し、回答→根拠確認→承認→本文/台帳/テスト反映の閉鎖手順を合意する。 |
