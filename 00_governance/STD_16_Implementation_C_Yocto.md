---
schema: spkgw.governance-note/v1
document_id: STD-GOV-016
project: SPK-GW_HEMS
document_type: STANDARD
revision: 1.3.0
status: DRAFT_FOR_REVIEW
title: 実装・C／Yocto・変更差分
owner: null
document_trace_id: DTR-SPKGW-GOV-000029
item_trace_ids:
- ITR-SPKGW-IMPROVE-000019
- ITR-SPKGW-IMPROVE-000020
- ITR-SPKGW-IMPROVE-000021
thread_id: THR-SPKGW-GOV-000001
related_thread_ids: []
trace_contract: spkgw.lifecycle-tags/v2
phase_ids:
- IMPL
- UT
- IT
phase_scope: CROSS_PHASE
activity_type: UNSPECIFIED
created_on: '2026-10-08'
updated_on: '2026-10-08'
classification: INTERNAL
source_baseline: BL-R9-0001
related_ids: []
---

# 実装・C／Yocto・変更差分

採用した言語・製品構成と既存コーディング規約を優先し、変更箇所と波及先へ適用する確認標準。全旧コードの是正を一件の完了条件へ無断追加しない。

## 1. 着手・差分・確認範囲

<a id="aim-19"></a>
### AIM-19 — 最小で再現可能な差分を作る

TASK、対象構成、固定入力版、受入条件、作業認可と影響区分を確認する。作業前のbranch・commit・dirty差分を残し、人／別Actorの編集を消さない。必要なら分離されたworktree等を使うが、実リポジトリ設定を無断変更しない。

要求に無関係な整形・一括改名・依存更新・構造変更を同じ差分へ混ぜない。API・関数・設定キーが実在するか対象版で確認する。生成物は生成元と再生成手順から変更する。実機・外部サービスへ作用する操作はその環境の認可を確認する。

実装項目はITR-CODE等として設計・要求のITRへimplementsで結び、文書DTRを試験端点の代用にしない。ソースファイル全てへコメントIDを一括挿入する要求ではない。

## 2. Cを中心とする変更レビュー

<a id="aim-20"></a>
### AIM-20 — メモリ・数値・並行・資源・状態

| 観点 | 確認項目 |
|---|---|
| メモリ | 長さ・配列境界、所有者、寿命、解放経路 |
| 数値・型 | 単位、範囲、符号、変換、桁溢れ境界 |
| 文字列・入力 | 終端、最大長、形式、不正・欠損値 |
| エラー | 戻り値、部分成功、資源解放、呼出元への結果 |
| 並行処理 | 共有状態、排他・直列化、順序、停止競合 |
| 時間 | 時計、単位、周期・期限、timeout、遅延後動作 |
| 資源 | メモリ・記述子・キュー上限と枯渇時 |
| 状態 | 初期化、再初期化、通信断、再起動・復帰 |
| 互換 | 対象コンパイラ・構成、IF、永続データ |

変更関連のコンパイラ警告は原因を確認し、単に抑制して問題を隠さない。エラー経路が制御権・認証・G側制約を迂回しないことを確認する。ログは対象ITR/要求ID・状態・相関を含めつつ秘密を出さない。コメントは意図・制約・非自明な理由へ絞る。既存の静的解析・書式確認を必要範囲で使う。本表は内部の確認規則で、MISRA等への適合宣言ではない。

## 3. Yocto・ビルド・構成と引渡し

<a id="aim-21"></a>
### AIM-21 — ビルド対象・構成差・回帰の引渡し

ソースだけでなくlayer/recipe/patch/依存版/MACHINE/DISTRO/設定・サービス・ツールチェーンを対象イメージへ結ぶ。ホストbuild、対象向けbuild、対象上の実行を区別し、一構成の成功を全構成へ一般化しない。具体コマンドは実リポジトリの手順を参照し、ダミーコマンドを実行しない。

変更した構成情報・依存・SBOM参照、ライセンス・更新責任をSTD-GOV-011/017へつなぐ。秘密をソース・build設定・生成物・commit・ログへ含めない。

要求／設計／コードの差異、異常系・回帰の実行／未実行、対象外、debug設定や暫定値の残留、自己レビューの範囲を最終差分から確認する。原因不明のFAILを試験弱体化で消さない。実装報告は変更内容、入力・候補版、実行者・環境・コマンド・証拠、残課題、次の判断。受入条件がそろっても未受入ならIN_REVIEWへ提出し、勝手にDONEへしない。

## Open Questions

実ビルド手順、target matrix、CIチェック、実機予約、既存コーディング規約は[適用プロファイル](PROJECT_PROFILE.md)と対象TASKで確定する。コード・実機は今回未提供、実装変更を実施したという記録ではない。

本版の追補・新設部分は[選択統合記録](AI_STD_Integration.md)から原文位置・採否・差分を追跡できる。添付の旧状態・旧保管先・旧ID体系を現行へ併設しない。
