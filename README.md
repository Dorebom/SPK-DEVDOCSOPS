# SPK-GW_HEMS ワークスペース R13 — AI_STDの選択統合

[MOC](00_governance/00_MOC.md)／[今回の採否記録](00_governance/AI_STD_Integration.md)／[プロジェクト索引](00_governance/PROJECT_PROFILE.md)／[AI入口ガイド](00_governance/Tool_Copilot.md)／[R13検証結果](20_work/analysis/project/reports/AI_STD_R13_QA.md)

現行製品文書はBL-R9-0001のまま。R13は管理標準と入力例の追補で、元R12のタスク・原価・版・Trace識別を維持する。新しい5STD、6テンプレート、6補助AI入口と26規則群の出典・適合化を記録した。

実利用前の環境確認はNOT_RUN。未知の製品数値・権限・担当・合格を補完していない。以下のR12説明は既存機能の履歴・利用参考であり、現在の改訂情報は上記のリンクを優先する。

---

# SPK-GW_HEMS ワークスペース R12 — 文書／項目TraceIDと工程略称

**選択済み製品仕様はBL-R9-0001のままです。** R12はガバナンスと追跡管理の変更です。

[ガバナンスMOC](00_governance/00_MOC.md) ／ [TraceID標準](00_governance/STD_03_TraceID.md) ／ [操作ガイド](00_governance/Tool_Traceability.md) ／ [文書・項目索引](20_work/analysis/project/reports/TRACE_INDEX.md)

原資料30_references → 分析20_work/analysis → 草案20_work/drafts → 検証・承認済みの文書Baseline10_canonical、という分離は維持。原本・現在の製品Baselineへ一括でFrontMatterを付与しません。

DTRは文書、ITRは一つの要求／設計／試験等、THRは任意テーマ。CONCEPT/REQAN/REQSPEC/SYSDES/ARCH/BASIC/DETAIL/IMPL/UT/IT/ST/NFT/VALID/RELPREP/RELEASE/OPS/IMPROVEを工程コードに使います。

```powershell
python .\tools\govcheck.py validate
python .\tools\tracecheck.py validate
python .\tools\tracecheck.py resolve --id SYS-RESP-001 --namespace item
python .\tools\specflow.py validate
```

## Open Questions

実担当、既存テストの段階、実コードやOffice条項の対応、Windows運用は[管理OQ](00_governance/Open_Questions.md)で確認する。
