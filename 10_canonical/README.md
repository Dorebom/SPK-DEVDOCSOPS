# 正本の選択

CURRENT.jsonが指すreleases配下の一式だけを現行として読む。各snapshotの00_MOC.mdが仕様書の入口。選択後のsnapshotは直接編集せず、draftへ複製して再採用する。

`python tools/specflow.py current` をワークスペース直下から実行すると、hash検査済みの現行MOCパスを返す。

受領原本・未承認の分析や草案はここへ置かない。正本に保持された未確定要求はDRAFT状態のままであり、採用・製品承認の別を保つ。

## Open Questions

OS権限、共有ストレージ、実際の公開担当と承認保管は[文書管理STD](../00_governance/STD_Import_Merge.md)と現行OQで具体化する。
