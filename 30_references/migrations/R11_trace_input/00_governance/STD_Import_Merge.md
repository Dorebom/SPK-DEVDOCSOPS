# STD-IMP-001 既存仕様の取り込み・分析・マージ・USDM接続

版：R9。根拠：ユーザーのCTX-R9とImport/USDM準備性レビューA1。文書管理方式を採用するもので、未確定の製品要求を承認するものではない。

## 1. 保管場所と権威

| 領域 | 置く内容 | 禁止する扱い |
|---|---|---|
| 30_references | 原Word/Excel、承認版情報、原本hash、受領記録、過去Baseline | 原本の数式再計算保存、変更履歴の黙示承認、原文上書き |
| 20_work/analysis | 抽出断片、未処理一覧、原文確認、差分、採否判断、検査報告 | 抽出済みを仕様採用済みとすること |
| 20_work/drafts | SYS/USDM候補、現行の編集コピー、prepare済み一式 | 利用者へ現行として配布、直接の製品設定化 |
| 10_canonical | 現行ポインタ、採用済み文書snapshot、採用証跡 | 原資料や未審査候補の直接貼付け、選択済みsnapshotの編集 |

canonicalは文書Baselineとして採用された内容であり、全レコードがAPPROVEDとは限らない。旧124要求のDRAFT、未回答OQ、未実施試験を維持する。元資料のSOURCE_APPROVEDと、取り込み先製品の採用も別。

## 2. 状態とフロー

```text
受領・原本登録（30_references）
 → 構造抽出（analysis/imports、原文とlocator）
 → 原文対照（analysis/reviews、未取得を明示）
 → 候補・適用条件・競合分類（analysis/draft_records）
 → 採否判断（ADOPT/EQUIVALENT/DEFER/REJECT/REFERENCE_ONLY）
 → 草案のSYS・USDM・IF・設定・本文へ反映（drafts）
 → 全入力検査 → 別候補で全ビュー生成 → 相互検証（prepare）
 → 候補hash・元Baselinehash・toolhashに対する明示承認
 → immutable release保存 → CURRENTの1回置換（publish）
```

原資料からcanonicalへ直結しない。対象が未確認ならUNKNOWN、不採用ならREJECT、抽出できなければBLOCKED_MANUAL、判断できなければ保留。未記載と未取得を混同しない。

## 3. 原資料とlocator

原本版をdocument_id＋業務版＋hashで識別する。ファイルのmtimeや最新ファイル名だけで権威を決めない。原文位置はdocxのXMLパート・段落/表/セルpath、xlsxのパート・シート・セル・式・キャッシュ・結合・非表示・書式、テキストの行範囲を保持する。ページはrendererにより変わるため単独識別子としない。

同一原本・同一抽出器コードの再抽出は同run_idで上書きしない。原本又は抽出器コードの改版は新run_id。セル/段落が動いた時の旧新対応はcompare-runsの候補を人が確認し、同一文字列だけで意味同一と認定しない。

## 4. マージの判断

| 分類 | 判断 |
|---|---|
| EQUAL | 本文は増やさず出典を追加。ただし同一適用条件を確認 |
| ADDITION / DETAIL | 新規又は詳細化。安定ID、親子/要求関係を保持 |
| SCOPE_VARIANT | 型式・FW・構成・基準点・時刻・単位・状態の差を明示 |
| CONFLICT | 両原文を保持。解決記録がない候補のADOPTを拒否 |
| OBSOLETE | 対象時期・製品を保持し、必要ならRETIRED/SUPERSEDED。黙示削除しない |
| INSUFFICIENT / UNCLASSIFIED | 解釈・根拠が不足。OQへ接続し採用を停止 |

既存の承認済みAs-IsとR8の未承認To-Be案は別の対象である。一方を自動優先して他方を消さない。全出力制御取得の宅内ルータ経由、RS-485対象のGW G側責務、EL PCS自身の自律取得、H/G非迂回、4ロールの範囲を取り込み副作用で変更しない。変更が必要なら影響評価を別に記録する。

## 5. 要求・USDM・理由

機能群S-FN/GW-FN、SYS契約、USDM要求/仕様、OQを同一視しない。SYSを保持したまま、spkgw.usdm-model/v1のREQUIREMENT/SPECIFICATION/EXPLANATIONと型付き多対多リンクを作る。既存単数usdm_idは互換欄。新しい多対多関係の正本はtrace_links.json。

理由はORIGINAL、HUMAN_CONFIRMED、HYPOTHESIS、UNKNOWNを区別する。UNKNOWNはtext=null。原文に理由がない時、AIによるもっともらしい説明をORIGINAL又はAPPROVEDへしない。承認済みREQUIREMENTでは理由の根拠又は確認者・承認記録が必要。

本モデルは公式USDM-Schema適合を宣言しない。正式形式へのエクスポータ、既存USDM Excelの自動意味変換は本実装の対象外。原文を保持して中間モデルとSYSをつなぐところまでが今回の実装。

## 6. 反映する正本

自由記述・章末OQはMD。SYS、機能、試験、USDM、型付きリンクは指定JSON。権限/構成詳細は規範別冊MD。自動生成対象はcanonical_ownership.jsonで指定する。未対応の詳細表を機械的に更新済みと見なさず、草案レビューで表/本文/IFとの一致を確認する。

apply-recordはSYS/USDMレコードを対象にした明示採用の補助であり、文章の意味を自動決定しない。その他の機能/IF/パラメータ/本文変更はdraftで編集して参照・型を検証する。新しい要件・理由を人の確認なしに自動生成・採用しない。

## 7. 承認と公開

prepare後の全ファイルhashと元Baselinehash、toolchainhashをapprovalに固定する。PENDING、担当者空欄、別候補の承認、途中の候補改変、古い元Baseline、未解決の取り込み競合、存在しない出典/USDM、空本文・重複ID・型不正を公開前に拒否する。

publishの可視化の確定点はCURRENT.jsonのos.replace。公開先ディレクトリの作成後に停止しても、旧CURRENTが指す一式を維持する。孤立した未選択release/receiptは監査で識別して必要に応じ整理する。CURRENTを更新する前に旧版を削除しない。

これはポインタを一度解決して読む利用者への論理的原子性であり、OS全ファイル操作の一括トランザクション、ネットワーク共有・実停電時の完全耐久性を証明するものではない。選択snapshotを直接編集するツールを併用しない。承認JSONは署名本人認証の代替ではなく、実アクセス制御/Gitレビューを併用する。

## 8. 検証の分離

固定版audit-baselineはR8原本の完全性のみ。通常validateは増減可能な型・ID・参照・双方向関係・OQ閉鎖・生成鮮度を確認。製品機能の妥当性・実装試験・JET判断・実Word/Excel抽出網羅は別の受入である。

## Open Questions

初回R9のV-05/V-06/V-07にOQ-R9-IMP-01〜06を配置した。管理方式は今回採用。実資料、担当者、公式USDM形式、Windows/共有ストレージ、規模条件は未確認。
