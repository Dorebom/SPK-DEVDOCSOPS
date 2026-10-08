# R7 文書QA

**検査結果：PASS（文書整合性のみ）**。実機・性能・安全・認証・認可の承認ではない。

## 実行した検査

| 検査 | 結果 |
|---|---|
| parts | 5 |
| chapters | 27 |
| appendices | 33 |
| system_function_groups | 21 |
| gw_function_groups | 32 |
| existing_requirements | 124 |
| existing_open_questions | 85 |
| role_types | 4 |
| proposed_operation_groups | 13 |
| configuration_patterns | 3 |
| r6_inventory_rows_linked | 21 |
| requirements_crosswalk_rows | 124 |
| r6_appendices_preserved | 29 |
| r6_detailed_chapters_preserved | 27 |
| r6_core_data_files_preserved | 10 |
| r6_diagram_files_preserved | 7 |
| r6_source_files_preserved | 51 |
| r6_input_sha256 | 6347adb1111e5b55562d9c650fad7596f0e24651dc2f4bb745e50f6fc18be9e3 |
| managed_json_files_parsed | 40 |
| current_markdown_notes | 71 |
| all_current_notes_have_trailing_oq | True |
| link_parser | markdown-it-py |
| local_links_checked | 7072 |
| external_links_not_revalidated | 8 |
| integrated_function_definitions | 53 |
| integrated_original_oq_definitions | 85 |

## 検査範囲の限界

機能一覧の根拠リンク・相互対応・ID・原本保持・リンク・形式を検査した。機能採否、既存実装全量の網羅、性能数値、権限付与、対応機器、JETその他認証の妥当性を合格にしたものではない。R5からの図は不変で、新規描画はしていない。

## 再実行

`python tools/rebuild_views.py` の後、レビュー済みの編集に対して `python tools/validate_package.py --refresh-manifest` を実行し、最後に `python tools/validate_package.py` で不変性を確認する。

## Open Questions — 仕様・検証の完成条件

[OQ-R6-17-01](chapters/17_Verification.md#oq-r6-17-01)：実構成・閾値・受入条件と評価責任者を確定する。[OQ-R6-04-01](chapters/04_Configurations_Profiles.md#oq-r6-04-01)：既存全機能と採用範囲を確認する。[OQ-R6-01-01](chapters/01_Scope_Baseline.md#oq-r6-01-01)：4種類の名前以外の権限・委譲等を確定する。
