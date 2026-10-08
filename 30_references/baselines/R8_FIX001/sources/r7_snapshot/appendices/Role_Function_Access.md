# 利用者別機能・操作権限仕様（規範別冊候補）

文書ID：`SPKGW-ANNEX-ACCESS`。版：`R7-DRAFT`。**4利用者の名称はユーザー確定。以下の権限マトリクスは提案であり、実行認可として使用しない。** 正本候補は [role_access_r7.json](../data/role_access_r7.json)。承認済み権限欄はすべてnullのまま。

## 1. 本編と別冊に何を書くか

本編Iには4分類・目的・利用場面・機能群別概要、本編IIにはGWが実施する認可・拒否・状態検査、本編IIIにはIFの認証・認可文脈、本編IVには最小権限・環境分離・監査等を記載する。この別冊が操作単位の詳細表を所有する。利用者マニュアル・施工保守手順・開発手順には具体操作を展開し、権限の新設は手順書側で行わない。

版・適用製品・承認・変更影響を持つ規範別冊として本体仕様の一部にする。単なる参考添付にしない。秘匿性の高い保守の具体手順は配布先を限定してよいが、禁止操作・認可境界まで本体から消さない。

## 2. 4利用者

| 利用者分類（確定） | 役割範囲の案（権限は未承認） |
|---|---|
| ユーザ | 所有・利用する住宅の監視、許可された通常運転・利用者設定 |
| メンテナンス | 委託された設備の施工・点検・診断・許可された復旧 |
| メーカー | 製品個体・リリース・配信・承認された保守の管理 |
| 開発者 | 開発・試験環境の検証と、別途認可された限定診断 |

ロールをユーザ＜メンテナンス＜メーカー＜開発者という単純な包含関係にしない。「メーカー」は全住宅への恒久アクセス、「開発者」は量産機の自由な操作を意味しない。製造・施工・運用の担当がどのロールを取るかは職務と委任で確定する。人の兼任・ロール切替、同一セッションでの併用、職務分離は未決。

## 3. 操作単位の権限マトリクス案

全セルは**レビュー案**。既存仕様の通常API非迂回原則を除き、新しい許可・禁止の採用を確定していない。空欄／nullは許可ではない。

| 操作ID／操作 | 関連GW機能 | ユーザ | メンテナンス | メーカー | 開発者 |
|---|---|---|---|---|---|
| ACCESS-DRAFT-01 住宅の状態・履歴閲覧 | [GW-FN-008](../parts/II_GW_Product_Specification.md#gw-fn-008)、[GW-FN-009](../parts/II_GW_Product_Specification.md#gw-fn-009)、[GW-FN-018](../parts/II_GW_Product_Specification.md#gw-fn-018)、[GW-FN-019](../parts/II_GW_Product_Specification.md#gw-fn-019) | 自住宅 | 委託対象・必要範囲 | 承認対象・必要範囲 | 試験データ／別途認可 |
| ACCESS-DRAFT-02 通常運転・利用者設定変更 | [GW-FN-001](../parts/II_GW_Product_Specification.md#gw-fn-001)、[GW-FN-004](../parts/II_GW_Product_Specification.md#gw-fn-004)、[GW-FN-005](../parts/II_GW_Product_Specification.md#gw-fn-005)、[GW-FN-006](../parts/II_GW_Product_Specification.md#gw-fn-006)、[GW-FN-020](../parts/II_GW_Product_Specification.md#gw-fn-020) | 範囲限定で候補 | 委託・保守条件付き | 個別委任時のみ候補 | 開発環境のみ候補 |
| ACCESS-DRAFT-03 機器登録・通信設定・試運転 | [GW-FN-010](../parts/II_GW_Product_Specification.md#gw-fn-010)、[GW-FN-021](../parts/II_GW_Product_Specification.md#gw-fn-021)、[GW-FN-029](../parts/II_GW_Product_Specification.md#gw-fn-029) | 案内された初期設定範囲 | 施工権限付き | 製造／正規保守範囲 | 試験環境のみ |
| ACCESS-DRAFT-04 診断ログの取得・出力 | [GW-FN-025](../parts/II_GW_Product_Specification.md#gw-fn-025) | 利用者向け診断のみ | 委託対象・秘密除去 | 承認された解析対象 | 匿名化／試験環境 |
| ACCESS-DRAFT-05 H側サービス再起動・復旧 | [GW-FN-022](../parts/II_GW_Product_Specification.md#gw-fn-022)、[GW-FN-026](../parts/II_GW_Product_Specification.md#gw-fn-026)、[GW-FN-032](../parts/II_GW_Product_Specification.md#gw-fn-032) | 公開済みの限定操作のみ | 保守Job条件付き | 正規保守条件付き | 開発環境のみ |
| ACCESS-DRAFT-06 GW通常FWの適用要求 | [GW-FN-023](../parts/II_GW_Product_Specification.md#gw-fn-023)、[GW-FN-024](../parts/II_GW_Product_Specification.md#gw-fn-024) | 承認済み更新の操作候補 | 承認済み配布物のみ | 管理・承認条件付き | 試験機のみ |
| ACCESS-DRAFT-07 本番FWリリースの承認・配布 | [GW-FN-023](../parts/II_GW_Product_Specification.md#gw-fn-023)、[GW-FN-024](../parts/II_GW_Product_Specification.md#gw-fn-024) | 不可案 | 不可案 | 独立したリリース権限 | 成果物提出のみ候補 |
| ACCESS-DRAFT-08 設定バックアップ・リストア・初期化 | [GW-FN-020](../parts/II_GW_Product_Specification.md#gw-fn-020)、[GW-FN-030](../parts/II_GW_Product_Specification.md#gw-fn-030) | 利用者範囲のみ候補 | 保守範囲・再確認 | 正規保守範囲 | 試験環境のみ |
| ACCESS-DRAFT-09 所有者変更・関連付け・消去 | [GW-FN-027](../parts/II_GW_Product_Specification.md#gw-fn-027)、[GW-FN-030](../parts/II_GW_Product_Specification.md#gw-fn-030) | 本人確認・確認操作付き | 委任と記録付き | 承認された手続きのみ | 本番は原則不可案 |
| ACCESS-DRAFT-10 製造個体ID・資格情報投入 | [GW-FN-027](../parts/II_GW_Product_Specification.md#gw-fn-027)、[GW-FN-029](../parts/II_GW_Product_Specification.md#gw-fn-029) | 不可案 | 通常保守では不可案 | 製造専用権限 | 試験値のみ |
| ACCESS-DRAFT-11 開発診断・試験操作 | [GW-FN-022](../parts/II_GW_Product_Specification.md#gw-fn-022)、[GW-FN-025](../parts/II_GW_Product_Specification.md#gw-fn-025)、[GW-FN-029](../parts/II_GW_Product_Specification.md#gw-fn-029) | 不可案 | 正規診断のみ | 正規診断又は試験設備 | 隔離環境・許可操作 |
| ACCESS-DRAFT-12 系統構成・G側設定・G側FW保守 | [GW-FN-028](../parts/II_GW_Product_Specification.md#gw-fn-028) | 通常経路では不可 | 別経路・追加認可が必要 | 別経路・追加認可が必要 | 通常経路では不可 |
| ACCESS-DRAFT-13 通常APIで系統制約・保護を解除 | [GW-FN-028](../parts/II_GW_Product_Specification.md#gw-fn-028) | 禁止 | 禁止 | 禁止 | 禁止 |

## 4. 条件付き権限

| 操作ID | 追加条件・境界 | 環境 |
|---|---|---|
| ACCESS-DRAFT-01 | 主体と住宅・機器・データのscopeを確認。メーカー／開発者へ全住宅を開放しない | 本番／開発等を個別指定 |
| ACCESS-DRAFT-02 | 本体操作と競合、契約条件、許可操作、現在状態を再確認 | 本番／開発等を個別指定 |
| ACCESS-DRAFT-03 | 電力計測対応・対象機器・変更世代を確認 | 本番／開発等を個別指定 |
| ACCESS-DRAFT-04 | 詳細ログ・住宅情報・資格情報の露出を別分類 | 本番／開発等を個別指定 |
| ACCESS-DRAFT-05 | G側を巻き込む操作をH限定と表示しない | 本番／開発等を個別指定 |
| ACCESS-DRAFT-06 | リリース承認・署名・適用・復旧は異なる責務 | 本番／開発等を個別指定 |
| ACCESS-DRAFT-07 | 開発者とリリース承認者の職務分離可否を決める。GWが署名秘密鍵を持つとはしない | 本番／開発等を個別指定 |
| ACCESS-DRAFT-08 | 所有者・系統設定・資格情報の移行を別確認 | 本番／開発等を個別指定 |
| ACCESS-DRAFT-09 | 旧セッション・待機要求・クラウド関連付けの失効条件を定義 | 本番／開発等を個別指定 |
| ACCESS-DRAFT-10 | 量産機の製造モード閉鎖と秘密取扱いを別定義 | 製造環境又は隔離された試験環境 |
| ACCESS-DRAFT-11 | 開発者ロールを量産機の裏口にしない。shell等の有無自体も未決 | 開発／試験。量産環境の例外は個別認可 |
| ACCESS-DRAFT-12 | 4ロールの上下関係では解禁しない。IF-MAINT-01／IF-GRID-03の適用・資格・変更手続きを別確認 | 本番／開発等を個別指定 |
| ACCESS-DRAFT-13 | 通常操作による迂回禁止は既存仕様。認可済み専用保守の設定変更を一律禁止する意味ではない | 本番／開発等を個別指定 |

判定は「誰」「何の操作」「どの住宅・GW・機器」「どのチャネル」「どの製品状態」「本番・製造・開発のどの環境」「いつまで」「誰の承認・委任か」を含める。GW操作の許可と実行順序・機器制御権の調停は分ける。

通常API経由の保護・出力制御の迂回は4ロールとも許可しない。専用のG側保守はIF-MAINT-01／IF-GRID-03の独立認可・対象・手続きを維持し、通常ロールの文字列だけで有効化しない。

## 5. 完成させる台帳フィールド

`policy_id / function_id / operation_id / target_scope / role / environment / channel / product_state / feature_profile / allowed_or_denied / value_range / delegation / expiry / additional_approval / audit / error_response / verification_id / applicable_document_revision`。

サーバやアプリに表示しないだけでなく、GWのAPI・公開IF・最終操作境界でも強制する。受信時と実行時に古い認可・期限・対象所属を再確認する。機械主体と人の代理権を別々に表現する。

## 6. 既存Open Questionの一部回答

OQ-R6-01-01の「誰が利用するか」のうち4分類の名称は今回の入力で回答済み。具体的権限、本人確認、委譲、兼任、対象範囲、承認者が残るため、質問全体はOPENを維持する。更新根拠は [CTX-R7](../sources/USER_CONTEXT_R7.md) と [部分回答記録](../data/known_answers_r7.json)。


## Open Questions — 本ノートの完成に必要な確認

既存OQの正本は `data/completion_items.json`。本一覧は参照で、別の回答正本を作らない。4利用者の確定事項は `data/known_answers_r7.json` を併読する。承認・数値・適合を未確認で補完しない。

| OQ・正本章 | 具体的な質問／未回答部分 | 必要資料・完了条件 |
|---|---|---|
| [OQ-R6-01-01](../chapters/01_Scope_Baseline.md#oq-r6-01-01) | 【一部回答済み】4分類の名称は今回確定。権限・委譲・環境等は未決。 初回製品で誰が利用・施工・管理・保守するか。各ロールの操作権限、本人確認、委譲と責任をどこまで分けるか。 | ロール×利用局面×操作範囲表を承認し、第20・26・27章へ対応付ける。 |
| [OQ-R6-20-01](../chapters/20_Northbound_Monitoring_FW.md#oq-r6-20-01) | 上位管理が読み書きする実項目と内部操作はどれか。プロトコル、公開schema、役割権限、完了通知・エラーをどう固定するか。 | 16件の論理IFを実契約へ展開し、公開操作台帳を実項目・権限・状態・結果へ対応付ける。 |
| [OQ-R6-27-02](../chapters/27_Security_Privacy_Lifecycle.md#oq-r6-27-02) | 各資格情報の生成者・保存先・寿命・更新・失効・漏えい復旧をどう定めるか。時刻無効・上位断中の検証とG側資格の独立管理はどうするか。 | 鍵/証明書/アカウントのライフサイクル表と失効・復旧試験条件を製造/運用文書へ対応付ける。 |
| [OQ-R6-27-04](../chapters/27_Security_Privacy_Lifecycle.md#oq-r6-27-04) | 量産機で残す保守・開発経路は何か。どの条件で一時有効化し、操作範囲・監査・自動無効化をどう制約するか。FW署名検証の失敗時は何を許すか。 | 保守経路台帳と許可操作/有効化/失効条件を定義し、任意shellやG設定への迂回を防ぐ検証へ結ぶ。 |
| [OQ-R6-27-06](../chapters/27_Security_Privacy_Lifecycle.md#oq-r6-27-06) | 収集する住宅・利用者データの目的・公開先・保持期間は何か。所有者変更、端末紛失、修理、廃棄での消去・失効と必要な通知をどう規定するか。 | データ用途/アクセス/保持/消去表をデータ辞書・ライフサイクル手順へ対応付け、適用要求を担当者が確認する。 |
| [OQ-R6-26-01](../chapters/26_Manufacturing_Commissioning_Retirement.md#oq-r6-26-01) | 個体IDと鍵/証明書をどの工程で投入し、再作業・不良品・重複をどう扱うか。出荷時に無効にする製造/開発機能と確認方法は何か。 | 製造プロファイルに投入主体・識別・秘密管理・再作業・閉鎖条件を記載し、手順書ID/版へ配賦する。 |
