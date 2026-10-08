# R2で補助参照した外部一次資料

確認日：2026-10-06。R1及び原典のJET／ECHONET Lite／一般送配電事業者資料は今回再検証していない。以下はFW機能の具体化に際して参照した**補助的な設計資料**であり、SPK-GWの採用規格・実装・適合宣言ではない。SUIT、特定署名形式、HTTP／MQTT等の採用を決めるものではない。

## EXT-FW-01 — RFC 9019

IETF / RFC Editor, *A Firmware Update Architecture for Internet of Things*, April 2021, Informational。
原本：<https://www.rfc-editor.org/rfc/rfc9019.html>
参照範囲：役割・機能の分担、ファームウェア画像とマニフェスト、更新の認証・完全性、復旧。
R2では「配信する主体／配信物を承認する主体／機器で適用判断する主体を区別する」「配送成功を更新成功としない」という設計提案の参考に用いる。

## EXT-FW-02 — RFC 9124

IETF / RFC Editor, *A Manifest Information Model for Firmware Updates in Internet of Things (IoT) Devices*, January 2022, Informational。
原本：<https://www.rfc-editor.org/rfc/rfc9124.html>
参照範囲：マニフェストの情報モデル、対象機器・コンポーネント、ダイジェスト、更新系列・互換性等の検査。
R2のFW対象領域、モデル・HW／SW互換、許可された版系列、真正性と完全性検査の項目を具体化する参考。各フィールド名は独自仕様案である。

ローカルWeb UIの具体的TLS／証明書配布、ブラウザ対応表、クラウド製品、認証基盤は選定していない。JETの新しい免除条件を外部調査で追加していない。
