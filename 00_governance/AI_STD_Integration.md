---
schema: spkgw.governance-note/v1
document_id: GOV-AISTD-INTEGRATION-001
project: SPK-GW_HEMS
document_type: REPORT
revision: 1.3.0
status: DRAFT_FOR_REVIEW
title: AI_STD v1.0.0 選択採用・適合化・保留の記録
owner: null
document_trace_id: DTR-SPKGW-GOV-000035
item_trace_ids: []
thread_id: THR-SPKGW-GOV-000001
related_thread_ids: []
trace_contract: spkgw.lifecycle-tags/v2
phase_ids:
- IMPROVE
phase_scope: PHASE_SPECIFIC
activity_type: UNSPECIFIED
created_on: '2026-10-08'
updated_on: '2026-10-08'
classification: INTERNAL
source_baseline: BL-R9-0001
related_ids: []
---

# AI_STD v1.0.0 選択採用・適合化・保留の記録

## 1. 基準と扱い
本書は添付37ファイルの読み合わせとR12管理方式への適合化の記録。標準の原本は30_references、選択判断と原文断片は20_work/analysis、現行STDは00_governanceに置く。R13の文書追補でありBL-R9-0001を更新しない。

## 2. 採否の原則
採用できる確認観点は既存STD又は新設STDへ配置する。元の語句を黙って別の意味で使わず、以下の差分を明示する。

| 原資料の提案 | R13での扱い | 理由 |
|---|---|---|
| 作業認可と採用・受入の分離 | ADAPTED：既存TASK/DEC/EXE/EVDとspecflowに接続 | 同じ承認の重複取得を減らすが実権限は保持 |
| DRAFT/READY/.../ACCEPTED等 | ADAPTED：現行PROPOSED/READY/.../DONEに対応 | FSMを二重にしない。証拠なしDONE不可 |
| BLOCKEDを試験結果に併記 | NOT_ADOPTED：作業阻害はTASK、試験未実施はNOT_RUN+理由 | 既存結果列挙を維持 |
| baseline_weight等の別ウェイト | NOT_ADOPTED：承認済み基準工数を利用 | 進捗の第二正本を作らない |
| governance/、work/tickets又は外部Issueへの自由配置 | ADAPTED：現行00/10/20/30に固定 | 既存正本とリンクを維持 |
| 半日〜2日、WIP=2、週1件ログ、半年計画 | DEFERRED：実運用で適用値を判断 | 一律の義務・実日程として承認されていない |
| Copilot等の2026-10-07機能説明 | REFERENCE_ONLY | 外部再検証は未実施。現環境確認票で確認 |
| 2実施例の進捗・工数・受入 | REFERENCE_ONLY | 架空例を実績へ計上しない |
| SHIRABE/HIBIKI接続 | REFERENCE_ONLY | 追加ランタイム依存や導入済みを意味しない |
| 元のMANIFEST/PACKAGE_CHECK | 原本として保存 | 元配布の検査でありR13の検査ではない |

## 3. 26規則群の反映先
| 規則 | 出典（原資料節） | 反映先 | 処置 |
|---|---|---|---|
| AIM-01 有効な認可・正本・独立性 | STD-01_GOVERNANCE：1., 2., 4., 5., 6. | [STD_01_Authority_Ownership.md#aim-01](STD_01_Authority_Ownership.md#aim-01) | ADAPTED |
| AIM-02 作業・並列・引継ぎの最小記録 | STD-03_WORK_CONTROL：1., 2., 4., 5., 6., 7. | [STD_04_Task_WBS.md#aim-02](STD_04_Task_WBS.md#aim-02) | ADAPTED |
| AIM-03 旧タスク状態を現行へ併設しない | STD-03_WORK_CONTROL / STD-08_PROGRESS_MANAGEMENT：3., 7. | [STD_04_Task_WBS.md#aim-03](STD_04_Task_WBS.md#aim-03) | ADAPTED |
| AIM-04 実行証拠・異常系・自己レビュー | STD-07_VERIFICATION_AND_ACCEPTANCE / STD-06_IMPLEMENTATION：2., 3., 4., 5., 6., 7., 8., 9. | [STD_06_Execution_Review_Evidence.md#aim-04](STD_06_Execution_Review_Evidence.md#aim-04) | ADAPTED |
| AIM-05 結果語彙と周期測定の境界 | STD-07_VERIFICATION_AND_ACCEPTANCE：3., 6.2 | [STD_06_Execution_Review_Evidence.md#aim-05](STD_06_Execution_Review_Evidence.md#aim-05) | ADAPTED |
| AIM-06 同一時点の旧新分母比較と未受入量 | STD-08_PROGRESS_MANAGEMENT：5., 6., 7., 8., 9. | [STD_07_Progress_Schedule.md#aim-06](STD_07_Progress_Schedule.md#aim-06) | ADAPTED |
| AIM-07 実費・配賦・推定を区別する | STD-12_MEASUREMENT_AND_IMPROVEMENT：4., 7. | [STD_08_Budget_Cost.md#aim-07](STD_08_Budget_Cost.md#aim-07) | ADAPTED |
| AIM-08 R0／R1／R2は作業影響の補助分類 | STD-01_GOVERNANCE / STD-11_RISK_AND_EXCEPTIONS / STD-04_REQUIREMENTS_AND_CHANGE：3., 4., 5., 7., 8., 9. | [STD_09_Change_Risk.md#aim-08](STD_09_Change_Risk.md#aim-08) | ADAPTED |
| AIM-09 例外・緊急対応を限定する | STD-11_RISK_AND_EXCEPTIONS：2., 6., 7., 8., 9., 10. | [STD_09_Change_Risk.md#aim-09](STD_09_Change_Risk.md#aim-09) | ADAPTED |
| AIM-10 指示ファイルは入口であり強制制御ではない | STD-02_COPILOT_USAGE：1., 2., 3., 4., 6., 7. | [STD_10_AI_Collaboration.md#aim-10](STD_10_AI_Collaboration.md#aim-10) | ADAPTED |
| AIM-11 ソース・ビルド・配布物・証拠を同一候補へ結ぶ | STD-09_CONFIGURATION_AND_RELEASE：1., 2., 3., 4., 5., 6. | [STD_11_Release_Baselines.md#aim-11](STD_11_Release_Baselines.md#aim-11) | ADAPTED |
| AIM-12 会話の報告と正本更新を区別する | STD-08_PROGRESS_MANAGEMENT / STD-12_MEASUREMENT_AND_IMPROVEMENT：9., 10., 2., 3., 4., 11. | [STD_12_Reports_Decisions.md#aim-12](STD_12_Reports_Decisions.md#aim-12) | ADAPTED |
| AIM-13 六つの質問と適用範囲 | STD-04_REQUIREMENTS_AND_CHANGE：1., 2., 3., 4. | [STD_14_Requirements_Change_Impact.md#aim-13](STD_14_Requirements_Change_Impact.md#aim-13) | ADAPTED |
| AIM-14 観測可能な要求と根拠の区別 | STD-04_REQUIREMENTS_AND_CHANGE：5., 5.1, 10. | [STD_14_Requirements_Change_Impact.md#aim-14](STD_14_Requirements_Change_Impact.md#aim-14) | ADAPTED |
| AIM-15 実行経路と外部依存まで追う | STD-04_REQUIREMENTS_AND_CHANGE：6., 7., 8., 9. | [STD_14_Requirements_Change_Impact.md#aim-15](STD_14_Requirements_Change_Impact.md#aim-15) | ADAPTED |
| AIM-16 七つの確認と論理・実配置の分離 | STD-05_DESIGN：1., 2., 3., 4., 5. | [STD_15_Design_Decisions.md#aim-16](STD_15_Design_Decisions.md#aim-16) | ADAPTED |
| AIM-17 状態所有・競合・非同期結果の設計 | STD-05_DESIGN：6., 7., 7.1, 8., 9. | [STD_15_Design_Decisions.md#aim-17](STD_15_Design_Decisions.md#aim-17) | ADAPTED |
| AIM-18 選択理由・反証・引渡し条件 | STD-05_DESIGN：10., 11. | [STD_15_Design_Decisions.md#aim-18](STD_15_Design_Decisions.md#aim-18) | ADAPTED |
| AIM-19 最小で再現可能な差分を作る | STD-06_IMPLEMENTATION：2., 3., 3.1, 4. | [STD_16_Implementation_C_Yocto.md#aim-19](STD_16_Implementation_C_Yocto.md#aim-19) | ADAPTED |
| AIM-20 メモリ・数値・並行・資源・状態 | STD-06_IMPLEMENTATION：5. | [STD_16_Implementation_C_Yocto.md#aim-20](STD_16_Implementation_C_Yocto.md#aim-20) | ADAPTED |
| AIM-21 ビルド対象・構成差・回帰の引渡し | STD-06_IMPLEMENTATION：6., 7., 8., 9., 10. | [STD_16_Implementation_C_Yocto.md#aim-21](STD_16_Implementation_C_Yocto.md#aim-21) | ADAPTED |
| AIM-22 必要最小限の入力と脅威確認 | STD-10_SECURITY_AND_SUPPLIER：1., 2., 3. | [STD_17_Security_Supplier.md#aim-22](STD_17_Security_Supplier.md#aim-22) | ADAPTED |
| AIM-23 脆弱性対応と部品情報 | STD-10_SECURITY_AND_SUPPLIER：4., 5., 7. | [STD_17_Security_Supplier.md#aim-23](STD_17_Security_Supplier.md#aim-23) | ADAPTED |
| AIM-24 ブラックボックスを推測で補わない | STD-10_SECURITY_AND_SUPPLIER：6. | [STD_17_Security_Supplier.md#aim-24](STD_17_Security_Supplier.md#aim-24) | ADAPTED |
| AIM-25 分母・時点・欠測・比較条件 | STD-12_MEASUREMENT_AND_IMPROVEMENT：1., 2., 3., 4., 5., 9. | [STD_18_AI_Measurement_Improvement.md#aim-25](STD_18_AI_Measurement_Improvement.md#aim-25) | ADAPTED |
| AIM-26 軽量な協働記録と将来接続 | STD-12_MEASUREMENT_AND_IMPROVEMENT：6., 7., 8., 10., 11. | [STD_18_AI_Measurement_Improvement.md#aim-26](STD_18_AI_Measurement_Improvement.md#aim-26) | ADAPTED |

## 4. 37入力ファイルの処置
| 原資料 | 処置 | 現行への反映先／理由 |
|---|---|---|
| [.github/copilot-instructions.md](../30_references/standards/AI_STD_v1_0_0/.github/copilot-instructions.md) | ADAPTED_OPTIONAL_ENTRY | [.github/copilot-instructions.md](../.github/copilot-instructions.md)<br/>現行パス・DTR/ITR/THR・状態に翻訳。実IDEの読み込み/権限は未確認。 |
| [.github/instructions/development.instructions.md](../30_references/standards/AI_STD_v1_0_0/.github/instructions/development.instructions.md) | ADAPTED_OPTIONAL_ENTRY | [.github/instructions/development.instructions.md](../.github/instructions/development.instructions.md)<br/>現行パス・DTR/ITR/THR・状態に翻訳。実IDEの読み込み/権限は未確認。 |
| [.github/instructions/governance.instructions.md](../30_references/standards/AI_STD_v1_0_0/.github/instructions/governance.instructions.md) | ADAPTED_OPTIONAL_ENTRY | [.github/instructions/governance.instructions.md](../.github/instructions/governance.instructions.md)<br/>現行パス・DTR/ITR/THR・状態に翻訳。実IDEの読み込み/権限は未確認。 |
| [.github/prompts/progress-update.prompt.md](../30_references/standards/AI_STD_v1_0_0/.github/prompts/progress-update.prompt.md) | ADAPTED_OPTIONAL_ENTRY | [.github/prompts/progress-update.prompt.md](../.github/prompts/progress-update.prompt.md)<br/>現行パス・DTR/ITR/THR・状態に翻訳。実IDEの読み込み/権限は未確認。 |
| [.github/prompts/work-review.prompt.md](../30_references/standards/AI_STD_v1_0_0/.github/prompts/work-review.prompt.md) | ADAPTED_OPTIONAL_ENTRY | [.github/prompts/work-review.prompt.md](../.github/prompts/work-review.prompt.md)<br/>現行パス・DTR/ITR/THR・状態に翻訳。実IDEの読み込み/権限は未確認。 |
| [.github/prompts/work-start.prompt.md](../30_references/standards/AI_STD_v1_0_0/.github/prompts/work-start.prompt.md) | ADAPTED_OPTIONAL_ENTRY | [.github/prompts/work-start.prompt.md](../.github/prompts/work-start.prompt.md)<br/>現行パス・DTR/ITR/THR・状態に翻訳。実IDEの読み込み/権限は未確認。 |
| [MANIFEST_SHA256.txt](../30_references/standards/AI_STD_v1_0_0/MANIFEST_SHA256.txt) | REFERENCE_ONLY | 原配布物の同一性・過去QAとして保持。R13の実検査の代替にしない。 |
| [PACKAGE_CHECK.md](../30_references/standards/AI_STD_v1_0_0/PACKAGE_CHECK.md) | REFERENCE_ONLY | 原配布物の同一性・過去QAとして保持。R13の実検査の代替にしない。 |
| [README_START_HERE.md](../30_references/standards/AI_STD_v1_0_0/README_START_HERE.md) | ADAPTED_NAVIGATION | [00_governance/00_MOC.md](../00_governance/00_MOC.md) / [00_governance/Tool_Copilot.md](../00_governance/Tool_Copilot.md) / [00_governance/Tool_Governance.md](../00_governance/Tool_Governance.md)<br/>現在のツール・記録先を案内。新しい作業FSMを設けない。 |
| [governance/OPERATION_GUIDE.md](../30_references/standards/AI_STD_v1_0_0/governance/OPERATION_GUIDE.md) | ADAPTED_NAVIGATION | [00_governance/00_MOC.md](../00_governance/00_MOC.md) / [00_governance/Tool_Copilot.md](../00_governance/Tool_Copilot.md) / [00_governance/Tool_Governance.md](../00_governance/Tool_Governance.md)<br/>現在のツール・記録先を案内。新しい作業FSMを設けない。 |
| [governance/PROJECT_PROFILE.md](../30_references/standards/AI_STD_v1_0_0/governance/PROJECT_PROFILE.md) | ADAPTED_INDEX | [00_governance/PROJECT_PROFILE.md](../00_governance/PROJECT_PROFILE.md)<br/>既存の正本を案内する索引に変換。実環境・権限・予算・制限値をコピーしない。 |
| [governance/REFERENCES.md](../30_references/standards/AI_STD_v1_0_0/governance/REFERENCES.md) | REFERENCE_ONLY | 引用元と原資料確認時点の記録。現行GitHub/VS Code機能として未検証。今回外部再調査しない。 |
| [governance/STD/STD-00_INDEX.md](../30_references/standards/AI_STD_v1_0_0/governance/STD/STD-00_INDEX.md) | ADAPTED_NAVIGATION | [00_governance/00_MOC.md](../00_governance/00_MOC.md) / [00_governance/Tool_Copilot.md](../00_governance/Tool_Copilot.md) / [00_governance/Tool_Governance.md](../00_governance/Tool_Governance.md)<br/>現在のツール・記録先を案内。新しい作業FSMを設けない。 |
| [governance/STD/STD-01_GOVERNANCE.md](../30_references/standards/AI_STD_v1_0_0/governance/STD/STD-01_GOVERNANCE.md) | PARTIAL_ADAPTATION | [00_governance/STD_01_Authority_Ownership.md](../00_governance/STD_01_Authority_Ownership.md) / [00_governance/STD_09_Change_Risk.md](../00_governance/STD_09_Change_Risk.md)<br/>該当26規則群の必要観点のみ適合化。異なるFSM・ID・計算や外部製品情報は既存契約を優先又は保留。 |
| [governance/STD/STD-02_COPILOT_USAGE.md](../30_references/standards/AI_STD_v1_0_0/governance/STD/STD-02_COPILOT_USAGE.md) | PARTIAL_ADAPTATION | [00_governance/STD_10_AI_Collaboration.md](../00_governance/STD_10_AI_Collaboration.md)<br/>該当26規則群の必要観点のみ適合化。異なるFSM・ID・計算や外部製品情報は既存契約を優先又は保留。 |
| [governance/STD/STD-03_WORK_CONTROL.md](../30_references/standards/AI_STD_v1_0_0/governance/STD/STD-03_WORK_CONTROL.md) | PARTIAL_ADAPTATION | [00_governance/STD_04_Task_WBS.md](../00_governance/STD_04_Task_WBS.md)<br/>該当26規則群の必要観点のみ適合化。異なるFSM・ID・計算や外部製品情報は既存契約を優先又は保留。 |
| [governance/STD/STD-04_REQUIREMENTS_AND_CHANGE.md](../30_references/standards/AI_STD_v1_0_0/governance/STD/STD-04_REQUIREMENTS_AND_CHANGE.md) | PARTIAL_ADAPTATION | [00_governance/STD_09_Change_Risk.md](../00_governance/STD_09_Change_Risk.md) / [00_governance/STD_14_Requirements_Change_Impact.md](../00_governance/STD_14_Requirements_Change_Impact.md)<br/>該当26規則群の必要観点のみ適合化。異なるFSM・ID・計算や外部製品情報は既存契約を優先又は保留。 |
| [governance/STD/STD-05_DESIGN.md](../30_references/standards/AI_STD_v1_0_0/governance/STD/STD-05_DESIGN.md) | PARTIAL_ADAPTATION | [00_governance/STD_15_Design_Decisions.md](../00_governance/STD_15_Design_Decisions.md)<br/>該当26規則群の必要観点のみ適合化。異なるFSM・ID・計算や外部製品情報は既存契約を優先又は保留。 |
| [governance/STD/STD-06_IMPLEMENTATION.md](../30_references/standards/AI_STD_v1_0_0/governance/STD/STD-06_IMPLEMENTATION.md) | PARTIAL_ADAPTATION | [00_governance/STD_06_Execution_Review_Evidence.md](../00_governance/STD_06_Execution_Review_Evidence.md) / [00_governance/STD_16_Implementation_C_Yocto.md](../00_governance/STD_16_Implementation_C_Yocto.md)<br/>該当26規則群の必要観点のみ適合化。異なるFSM・ID・計算や外部製品情報は既存契約を優先又は保留。 |
| [governance/STD/STD-07_VERIFICATION_AND_ACCEPTANCE.md](../30_references/standards/AI_STD_v1_0_0/governance/STD/STD-07_VERIFICATION_AND_ACCEPTANCE.md) | PARTIAL_ADAPTATION | [00_governance/STD_06_Execution_Review_Evidence.md](../00_governance/STD_06_Execution_Review_Evidence.md)<br/>該当26規則群の必要観点のみ適合化。異なるFSM・ID・計算や外部製品情報は既存契約を優先又は保留。 |
| [governance/STD/STD-08_PROGRESS_MANAGEMENT.md](../30_references/standards/AI_STD_v1_0_0/governance/STD/STD-08_PROGRESS_MANAGEMENT.md) | PARTIAL_ADAPTATION | [00_governance/STD_04_Task_WBS.md](../00_governance/STD_04_Task_WBS.md) / [00_governance/STD_07_Progress_Schedule.md](../00_governance/STD_07_Progress_Schedule.md) / [00_governance/STD_12_Reports_Decisions.md](../00_governance/STD_12_Reports_Decisions.md)<br/>該当26規則群の必要観点のみ適合化。異なるFSM・ID・計算や外部製品情報は既存契約を優先又は保留。 |
| [governance/STD/STD-09_CONFIGURATION_AND_RELEASE.md](../30_references/standards/AI_STD_v1_0_0/governance/STD/STD-09_CONFIGURATION_AND_RELEASE.md) | PARTIAL_ADAPTATION | [00_governance/STD_11_Release_Baselines.md](../00_governance/STD_11_Release_Baselines.md)<br/>該当26規則群の必要観点のみ適合化。異なるFSM・ID・計算や外部製品情報は既存契約を優先又は保留。 |
| [governance/STD/STD-10_SECURITY_AND_SUPPLIER.md](../30_references/standards/AI_STD_v1_0_0/governance/STD/STD-10_SECURITY_AND_SUPPLIER.md) | PARTIAL_ADAPTATION | [00_governance/STD_17_Security_Supplier.md](../00_governance/STD_17_Security_Supplier.md)<br/>該当26規則群の必要観点のみ適合化。異なるFSM・ID・計算や外部製品情報は既存契約を優先又は保留。 |
| [governance/STD/STD-11_RISK_AND_EXCEPTIONS.md](../30_references/standards/AI_STD_v1_0_0/governance/STD/STD-11_RISK_AND_EXCEPTIONS.md) | PARTIAL_ADAPTATION | [00_governance/STD_09_Change_Risk.md](../00_governance/STD_09_Change_Risk.md)<br/>該当26規則群の必要観点のみ適合化。異なるFSM・ID・計算や外部製品情報は既存契約を優先又は保留。 |
| [governance/STD/STD-12_MEASUREMENT_AND_IMPROVEMENT.md](../30_references/standards/AI_STD_v1_0_0/governance/STD/STD-12_MEASUREMENT_AND_IMPROVEMENT.md) | PARTIAL_ADAPTATION | [00_governance/STD_08_Budget_Cost.md](../00_governance/STD_08_Budget_Cost.md) / [00_governance/STD_12_Reports_Decisions.md](../00_governance/STD_12_Reports_Decisions.md) / [00_governance/STD_18_AI_Measurement_Improvement.md](../00_governance/STD_18_AI_Measurement_Improvement.md)<br/>該当26規則群の必要観点のみ適合化。異なるFSM・ID・計算や外部製品情報は既存契約を優先又は保留。 |
| [governance/examples/EX-01_WORK_TICKET.md](../30_references/standards/AI_STD_v1_0_0/governance/examples/EX-01_WORK_TICKET.md) | REFERENCE_ONLY | 例示のTASK/工数/進捗は実計画・実績へ登録しない。 |
| [governance/examples/EX-02_PROGRESS_REPORT.md](../30_references/standards/AI_STD_v1_0_0/governance/examples/EX-02_PROGRESS_REPORT.md) | REFERENCE_ONLY | 例示のTASK/工数/進捗は実計画・実績へ登録しない。 |
| [governance/templates/T-01_WORK_TICKET.md](../30_references/standards/AI_STD_v1_0_0/governance/templates/T-01_WORK_TICKET.md) | ADAPTED_TEMPLATE_FIELDS | [00_governance/templates/Task.md](../00_governance/templates/Task.md)<br/>必要な記入項目を既存又は追加テンプレートへ移す。元の状態/ID/頻度/正本は持ち込まない。 |
| [governance/templates/T-02_CHANGE_IMPACT.md](../30_references/standards/AI_STD_v1_0_0/governance/templates/T-02_CHANGE_IMPACT.md) | ADAPTED_TEMPLATE_FIELDS | [00_governance/templates/Change_Impact.md](../00_governance/templates/Change_Impact.md)<br/>必要な記入項目を既存又は追加テンプレートへ移す。元の状態/ID/頻度/正本は持ち込まない。 |
| [governance/templates/T-03_DESIGN_NOTE.md](../30_references/standards/AI_STD_v1_0_0/governance/templates/T-03_DESIGN_NOTE.md) | ADAPTED_TEMPLATE_FIELDS | [00_governance/templates/Design_Note.md](../00_governance/templates/Design_Note.md)<br/>必要な記入項目を既存又は追加テンプレートへ移す。元の状態/ID/頻度/正本は持ち込まない。 |
| [governance/templates/T-04_VERIFICATION_RECORD.md](../30_references/standards/AI_STD_v1_0_0/governance/templates/T-04_VERIFICATION_RECORD.md) | ADAPTED_TEMPLATE_FIELDS | [00_governance/templates/Execution.md](../00_governance/templates/Execution.md) / [00_governance/templates/Review.md](../00_governance/templates/Review.md)<br/>必要な記入項目を既存又は追加テンプレートへ移す。元の状態/ID/頻度/正本は持ち込まない。 |
| [governance/templates/T-05_PROGRESS_REPORT.md](../30_references/standards/AI_STD_v1_0_0/governance/templates/T-05_PROGRESS_REPORT.md) | ADAPTED_TEMPLATE_FIELDS | [00_governance/templates/Weekly_Report.md](../00_governance/templates/Weekly_Report.md)<br/>必要な記入項目を既存又は追加テンプレートへ移す。元の状態/ID/頻度/正本は持ち込まない。 |
| [governance/templates/T-06_PLAN_BASELINE.md](../30_references/standards/AI_STD_v1_0_0/governance/templates/T-06_PLAN_BASELINE.md) | ADAPTED_TEMPLATE_FIELDS | [00_governance/templates/Plan.md](../00_governance/templates/Plan.md)<br/>必要な記入項目を既存又は追加テンプレートへ移す。元の状態/ID/頻度/正本は持ち込まない。 |
| [governance/templates/T-07_DECISION_RISK_EXCEPTION.md](../30_references/standards/AI_STD_v1_0_0/governance/templates/T-07_DECISION_RISK_EXCEPTION.md) | ADAPTED_TEMPLATE_FIELDS | [00_governance/templates/Change.md](../00_governance/templates/Change.md) / [00_governance/templates/Decision.md](../00_governance/templates/Decision.md) / [00_governance/templates/Risk.md](../00_governance/templates/Risk.md)<br/>必要な記入項目を既存又は追加テンプレートへ移す。元の状態/ID/頻度/正本は持ち込まない。 |
| [governance/templates/T-08_RELEASE_RECORD.md](../30_references/standards/AI_STD_v1_0_0/governance/templates/T-08_RELEASE_RECORD.md) | ADAPTED_TEMPLATE_FIELDS | [00_governance/templates/Release.md](../00_governance/templates/Release.md)<br/>必要な記入項目を既存又は追加テンプレートへ移す。元の状態/ID/頻度/正本は持ち込まない。 |
| [governance/templates/T-09_SUPPLIER_RESPONSE.md](../30_references/standards/AI_STD_v1_0_0/governance/templates/T-09_SUPPLIER_RESPONSE.md) | ADAPTED_TEMPLATE_FIELDS | [00_governance/templates/Supplier_Response.md](../00_governance/templates/Supplier_Response.md)<br/>必要な記入項目を既存又は追加テンプレートへ移す。元の状態/ID/頻度/正本は持ち込まない。 |
| [governance/templates/T-10_AI_CAPABILITY_LOG.md](../30_references/standards/AI_STD_v1_0_0/governance/templates/T-10_AI_CAPABILITY_LOG.md) | ADAPTED_TEMPLATE_FIELDS | [00_governance/templates/AI_Capability_Log.md](../00_governance/templates/AI_Capability_Log.md)<br/>必要な記入項目を既存又は追加テンプレートへ移す。元の状態/ID/頻度/正本は持ち込まない。 |

## 5. 正本・Traceの整合
既存のDTR／ITR／THR、可読工程、SYS等native IDを再採番しない。改訂した文書だけ新revisionを追加し、旧文書を30_references/baselines/R12_changedへ保存。26規則のITRと原資料抜粋のITRをcitesで結ぶ。引用関係はimplements/verifiesではなく、review=nullのまま。原本の承認や製品合格を意味しない。

原文断片と採否は[統合データ](../20_work/analysis/project/ai_std_integration/integration.json)、[原文位置](../20_work/analysis/project/ai_std_integration/source_fragments.json)、現在のDTR/ITRは[Trace索引](../20_work/analysis/project/reports/TRACE_INDEX.md)で追う。

## 6. 検証方法と限界
`python tools/verify_ai_std_integration.py`で原本・採否・節の存在・出典位置・旧版・既存Baseline・原票・ツールの維持を確認する。govcheck/tracecheck/specflowと合成回帰を併用する。実クライアント読込み、製品Cビルド、Yocto実行、実機、委託契約、原価照合、独立レビュー、JET判断は今回の実施対象外。[実測報告](../20_work/analysis/project/reports/AI_STD_R13_QA.md)を参照。

## Open Questions
[管理OQ](Open_Questions.md)のOQ-GOV-AISTD-01〜03が未確定条件。原資料を読み込んだことを全条項・全例の採用や実行認可にしない。
