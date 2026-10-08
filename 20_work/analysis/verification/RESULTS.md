# R9 文書管理・取り込み基盤の検証結果

日付：2026-10-08。対象：R8-FIX001からR9への文書管理改訂。製品機能試験ではない。

## 結果

文書検査：PASS。原本保存検査：PASS。合成回帰：47件、失敗0件、エラー0件。

| 継承対象 | 結果 |
|---|---|
| SYS要求124件 | レコード全フィールド一致（文書版メタデータはR9） |
| 全体21/GW32機能群 | 機能レコード一致 |
| 既存OQ85件 | 質問・回答・状態・完了条件・既知回答を保持 |
| 追加OQ | 管理と実資料確認6件（合計91件） |
| 9データ台帳 | バイト一致 |
| 図6資産 | SHA-256一致。再描画なし |
| R8原本 | ZIPと展開324ファイル一致、旧Manifest3件を保持 |

構造：5部44章・29別冊。現在の管理対象Markdownローカル参照：7558件。現行USDM要素と新規原資料採用：各0件。

## 合成テスト一覧

| ケース | 結果 | 秒 |
|---|---|---|
| test_01_baseline_integrity_and_freshness | PASS | 1.539 |
| test_02_empty_requirement_rejected | PASS | 0.086 |
| test_03_wrong_status_type_rejected | PASS | 0.081 |
| test_04_duplicate_ids_rejected_before_render | PASS | 0.12 |
| test_05_unknown_source_rejected | PASS | 0.124 |
| test_06_unknown_usdm_rejected | PASS | 0.148 |
| test_07_requirement_test_asymmetry_rejected | PASS | 0.172 |
| test_08_stale_views_rejected | PASS | 0.731 |
| test_09_input_failure_never_changes_canonical | PASS | 0.108 |
| test_10_staged_render_failure_never_changes_canonical | PASS | 0.451 |
| test_11_pending_approval_rejected | PASS | 1.146 |
| test_12_publish_and_idempotent_republication | PASS | 1.819 |
| test_13_failure_before_pointer_retains_selected_baseline | PASS | 2.549 |
| test_14_prepared_tampering_rejected | PASS | 1.373 |
| test_15_wrong_approval_hash_rejected | PASS | 1.121 |
| test_16_stale_parent_baseline_rejected | PASS | 3.077 |
| test_17_original_tampering_detected | PASS | 0.07 |
| test_18_registration_and_extraction_idempotence | PASS | 0.075 |
| test_19_old_binary_format_is_blocked | PASS | 0.074 |
| test_20_docx_nested_table_revision_and_image_inventory | PASS | 0.059 |
| test_21_xlsx_formula_cache_hidden_merge_comments | PASS | 0.055 |
| test_22_unsafe_zip_path_rejected | PASS | 0.055 |
| test_23_dtd_rejected | PASS | 0.054 |
| test_24_unresolved_conflict_cannot_be_adopted | PASS | 0.08 |
| test_25_unreviewed_fragment_cannot_be_applied | PASS | 0.1 |
| test_26_125th_requirement_end_to_end | PASS | 2.529 |
| test_27_unbound_addition_cannot_prepare | PASS | 0.077 |
| test_28_deleting_old_id_is_rejected | PASS | 0.067 |
| test_29_usdm_unknown_reason_not_approved | PASS | 0.206 |
| test_30_usdm_cycle_rejected | PASS | 0.207 |
| test_31_bad_typed_endpoint_rejected | PASS | 0.211 |
| test_32_new_function_groups_have_no_fixed_count | PASS | 0.818 |
| test_33_new_interface_parameter_and_test_no_fixed_count | PASS | 0.851 |
| test_34_new_oq_id_is_not_r6_bound | PASS | 0.859 |
| test_35_compare_revision_detects_move_not_auto_delete | PASS | 0.085 |
| test_36_approved_binding_text_tampering_rejected | PASS | 0.257 |
| test_37_selected_snapshot_direct_edit_detected | PASS | 0.052 |
| test_38_duplicate_json_key_rejected | PASS | 0.045 |
| test_39_path_traversal_draft_rejected | PASS | 0.047 |
| test_40_tool_change_invalidates_approval | PASS | 1.059 |
| test_41_fragment_text_tampering_rejected | PASS | 0.258 |
| test_42_coverage_distinguishes_unclassified_and_selected | PASS | 1.841 |
| test_43_delete_oq_is_blocked_by_change_gate | PASS | 0.077 |
| test_44_preparation_diff_lists_all_modified_files | PASS | 1.073 |
| test_45_usdm_many_to_many_draft_roundtrip | PASS | 1.756 |
| test_46_legacy_source_alias_identity_checked | PASS | 0.096 |
| test_47_moc_cannot_redirect_current_view_to_history | PASS | 0.214 |

## 実行環境と限界

Python 3.13.5、Linux-6.18.44-x86_64-with-glibc2.41、jsonschema 4.26.0。

DOCX/XLSX試験は、入れ子表・変更履歴・数式cache・非表示・結合・コメント等を持つ合成OOXML部品による構造抽出テスト。Officeの描画品質、既存製品帳票の解釈完全性、Windows、共有ストレージ、実停電、実機制御、JET承認、大量資料処理は未検証。

検証済みの公開原子性は「stage生成の例外」「CURRENT置換直前の例外」で、旧選択snapshotと旧pointerが不変であること。全OS/ファイルシステムでの耐久性を保証しない。承認JSONの本人性はOS権限/Git等の実運用で担保する。

## Open Questions

OQ-R9-IMP-01〜06で実原資料・形式・採用者・USDM交換・実運用・規模を確認する。詳細JSONとunittest.logは同じフォルダに保持。
