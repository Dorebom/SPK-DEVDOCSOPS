# 抽出・分析・照合・採用判断

importsは原本の抽出結果、reviewsは原文対照、draft_recordsは解釈候補とマージ判断、comparisonsは改版差分候補、approvalsは採用要求・承認記録、verificationは文書ツールの検査証拠。

結果は正本へ自動昇格しない。採用時は対象断片・確認・判断を候補内のimport_provenance.jsonへ固定し、選択Baselineが作業フォルダに依存しないようにする。

## Open Questions

実資料の対照担当・残オブジェクトの完了判定は[STD](../../00_governance/STD_Import_Merge.md)とOQで確定する。
