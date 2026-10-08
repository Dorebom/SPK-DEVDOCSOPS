---
description: "正本・原資料・作業・実績とDTR/ITRの境界"
applyTo: "00_governance/**,20_work/**,10_canonical/**,30_references/**,.github/**"
---

# 管理記録の更新
[FrontMatter](../../00_governance/STD_02_FrontMatter.md)、[Trace](../../00_governance/STD_03_TraceID.md)、[取り込み標準](../../00_governance/STD_Import_Merge.md)を参照する。

原資料は不変、採用判断は分析、本文候補はdraft、現行選択はCURRENTの指すBaseline。既存IDや原文位置・版を失わせない。AI案・原文・人の確認・正式承認を区別する。現在のTASK stateとcontrol.json原票を正本にし、別のACCEPTED状態・進捗ウェイト・費用実績を追加しない。

文書同士の参照だけで個別項目のimplements/verifiesを作らない。未知のActor・日付・原価・認証承認・USDM理由を補完しない。変更したDTRは旧版を保存し、新版/hashとITRの所在を整合させる。安全な採用・検証の範囲を超えるコマンドをこの指示で許可しない。
