# R13：AI_STD選択統合の検証報告

検査対象：SPK-GW_HEMS_Workspace_20261008_R13。日付：2026-10-08。
**文書の選択統合・構造・保存・合成回帰の検査であり、標準の全項目自動強制、実機・実会計・認証・本人確認の検査ではない。**

## 1. 反映範囲
添付AI_STD v1.0.0の37ファイルを原本保存。26規則群を現行R12の契約へ適合化し、既存STDに追補、STD-GOV-014〜018を新設。6テンプレートと6任意AI入口を追加した。原資料の状態・ID・フォルダ・進捗ウェイト・固定WIP/頻度・実施例の数値を現行管理原票に採用しない。

## 2. 実行した検査
| 検査 | 実測結果 |
|---|---|
| govcheck validate | PASS。4候補TASK・未承認計画/予算・実績未確認の警告を保持 |
| tracecheck validate | PASS。217論理文書／239文書版、396項目、767項目関係 |
| specflow validate | PASS。5部44章／124要求／69試験／91製品OQの既存Baselineを維持 |
| audit-baseline | PASS。R8-FIX001 ZIPと324原本ファイルが一致 |
| verify_ai_std_integration | PASS。37原本・26規則・原文範囲・旧版保存・旧項目/関係・原票/ツール保存 |
| 既存governance回帰 | 45件PASS |
| 既存specflow回帰 | 47件PASS |
| 既存文書/項目ID回帰 | 35件PASS |
| 既存17工程Trace回帰 | 40件PASS |
| 新規統合の異常系・保存検査 | 21件PASS |
| **重複を除く合成回帰合計** | **188件PASS、失敗0、skip0** |

初回の一括テスト呼出しはspecflow第16ケース中にツール実行時間制限で中断した。中断前の完了60ケースを確認し、第16以降を分割して完走した。Trace75件、新規統合21件も実行した。中断した呼出し全体をPASSとせず、`all_test_results.json`で各ケースの完了を重複排除して集計した。新規統合21件は最終文書ハッシュ更新後にも再実行しPASS。これは実環境の製品試験69件の実行ではない。

65現行Markdown（ガバナンス・補助AI入口・README・Trace索引）の982相対リンクを検査し、参照先・確認対象アンカーの欠落0を確認。原資料・旧版は当時のバイトを保存し、現行のリンクへ無断書換えしない。選択済みシステム本文の生成鮮度・参照はspecflowの検査範囲。

## 3. 追加検査の21ケース

| ケース | 結果 |
|---|---|
| `test_01_current_integration` | PASS |
| `test_02_missing_original` | PASS |
| `test_03_original_tampering` | PASS |
| `test_04_missing_target` | PASS |
| `test_05_wrong_excerpt` | PASS |
| `test_06_invalid_source_range` | PASS |
| `test_07_missing_rule_anchor` | PASS |
| `test_08_duplicate_rule` | PASS |
| `test_09_invalid_source_document` | PASS |
| `test_10_canonical_tampering` | PASS |
| `test_11_actual_task_tampering` | PASS |
| `test_12_existing_tool_tampering` | PASS |
| `test_13_citation_is_not_implements` | PASS |
| `test_14_existing_item_unchanged` | PASS |
| `test_15_existing_edges_unchanged` | PASS |
| `test_16_prior_document_snapshot_required` | PASS |
| `test_17_current_revised_document_hash_required` | PASS |
| `test_18_no_old_authority_path` | PASS |
| `test_19_no_implicit_product_approval` | PASS |
| `test_20_previous_source_register_rows_preserved` | PASS |
| `test_21_read_only_audit` | PASS |

## 4. 保存とTrace
製品CURRENT/releases/receipts、管理control.json、4TASK、既存ツール・スキーマ・17工程・aliasesを不変検査した。R12にあった341項目・741項目関係はレコード一致。改訂した22文書はDTRを維持し、旧revisionの原本を30_references/baselines/R12_changedへ保存。新たに26規則・26引用断片・3管理OQ（合計55項目）を追加。

新規関係は26件のcitesでありimplements/verifiesではない。全396項目のreviewは未確認を含み、Traceの接続を工程完了・製品合格としない。既存ルールの意味を変えずに対応できない提案は、選択統合台帳の理由で保留又は参考のみとした。

## 5. 未実施・制約
実GitHub Copilot／VS Codeの読込み・プロンプト起動・権限、製品Cコードの静的解析、Yoctoビルド、Windows／実ネットワーク共有／実停電、PCS・GW実機、委託先受入・会計照合・法規/安全/セキュリティ認証・JET判断は未実施。原資料の2026-10-07付の外部製品機能を今回再検証していない。

`.github`6ファイルは任意入口であり、全STD自動読込み、承認済み変更、権限設定、sandbox、強制検査を実装したものではない。新しい確認票や測定は手動レビューを伴い、既存管理ツールに新指標の自動集計を追加していない。

## 6. 証跡
[ケース別結果](../ai_std_integration/verification/all_test_results.json)／[統合検査](../ai_std_integration/verification/integration_result.json)／[Trace検査](../ai_std_integration/verification/trace_result.json)／[要求・生成鮮度](../ai_std_integration/verification/spec_result.json)／[原本](../ai_std_integration/verification/baseline_result.json)／[ファイル変更](../ai_std_integration/change_inventory.json)／[採否・原文](../ai_std_integration/integration.json)。

最終ZIPのCRC・全ファイルManifestは配布時に別途検査し、配布ZIP自身のハッシュと結果を外付け報告に残す。内部の作成途中QAで、最終ZIPを確認済みとはしない。

## Open Questions
[管理OQ](../../../../00_governance/Open_Questions.md)の実運用・機密・委託・測定条件を確認する。未承認製品数値、人物、予算をテスト合成データで置換しない。
