# 抽出器の対応範囲・限界

これは抽出実装の契約であり、旧帳票の意味を自動確定するものではない。

| 入力 | 自動取得 | 人の確認・未対応 |
|---|---|---|
| .docx | document/header/footer/footnote/endnote/commentパートの段落、入れ子表のXML位置、原文、削除/挿入文字列、表結合metadata | ページ描画、番号・field・相互参照、図・数式・OLE・altChunk、表見出し/注記の意味、変更履歴の採否 |
| .xlsx | sheet/cell、共有文字列、inline文字列、式とcache、書式ID/定義、結合範囲、非表示、コメント、外部リンクの存在 | 再計算、完全な表示値、ヘッダ/単位の意味、描画/画像/ピボット/テーブルの意味、shared/array formula復元、複雑なコメント関連付け |
| UTF-8 .md/.txt/.csv | 非空行と行番号、直前行 | CSV列/ヘッダの意味、非UTF-8は手動変換 |
| .doc/.xls/.xlsm、画像主体、暗号化 | 原本登録とBLOCKED_MANUAL | 変換又は専用抽出の追加と目視対照。自動マクロ/外部リンク/OCRなし |

抽出結果は常にNEEDS_REVIEW又はBLOCKED_MANUAL。EXTRACTEDは個別断片を文字として取れた意味で、確認済み/採用済みではない。図・数式・変更履歴等の注意をunhandled_objectsとfeaturesに残す。非表示を不要として落とさない。

XML package制限は10,000 entries、展開合計100MiB、XML1個30MiB。安全な処理予算としての初期値であり、製品仕様値ではない。DTD/ENTITY、ZIP危険パス、重複パス、暗号化を拒否。大きな原資料は無制限に広げず、担当者が分割又は限度をレビューする。

## Open Questions

OQ-R9-IMP-02/06：実帳票の対照・件数・性能。合成テストだけでは、既存資料の全ページ/セルの網羅性を保証しない。
