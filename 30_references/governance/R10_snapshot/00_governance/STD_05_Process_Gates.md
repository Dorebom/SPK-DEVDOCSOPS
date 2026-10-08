---
schema: spkgw.governance-note/v1
document_id: STD-GOV-005
project: SPK-GW_HEMS
document_type: STANDARD
revision: 1.0.0
status: DRAFT_FOR_REVIEW
title: 開発工程・成果物・判断ゲート
owner: null
trace_id: TRC-SPKGW-000001
created_on: '2026-10-08'
updated_on: '2026-10-08'
classification: INTERNAL
source_baseline: BL-R9-0001
related_ids: []
---

# 開発工程・成果物・判断ゲート

## 1. 工程の母集団
| phase | 主な作業・成果物 | 受入・次工程への条件 |
|---|---|---|
| DISCOVERY | 既存調査、原資料棚卸し、対象範囲 | 原文と未取得箇所、適用範囲を明示 |
| REQUIREMENTS | 利用目的、要求、理由、USDM | 理由の出典／仮説を区別、検証可能な仕様との対応 |
| SPECIFICATION | 外部仕様、システム5部、機能・IF・設定・データ | 矛盾・対象外・OQ・構成の扱いを明示 |
| ARCHITECTURE | H/G、責務、トポロジー、非干渉 | 依存と変更境界を評価 |
| DESIGN | 構造・詳細設計、テスト設計 | 要求配賦と設計レビュー |
| IMPLEMENTATION | コード・設定・ビルド | 対象版の再現とレビュー、静的検査 |
| VERIFICATION | 単体・結合・機能・回帰・性能・安全・セキュリティ | 要求・試験条件・判定・証拠を対応 |
| VALIDATION | 利用目的、実機／運用条件 | 受入条件と制約、既知問題 |
| RELEASE | 変更影響、認証判断、署名、配布、復旧 | 製品品質・認証・文書採用・支出の別判断 |
| OPERATIONS | 製造、施工、保守、脆弱性、交換、廃棄 | 対象個体・版・安全・サポート条件 |
| MANAGEMENT | 計画、進捗、会議、予算、調達、リスク | 決定・実績・見通しと担当 |
工程順は反復可能。段階移行・並行作業では許可された前提を明示し、後工程実施で上流要求を自動承認しない。

## 2. ゲート
G0 スコープ・役割・計画／予算基準、G1 要求・仕様の採用範囲、G2 設計・実行許可、G3 証拠に基づく受入、G4 リリース・運用準備を提案する。R9 OQのG0〜G4は旧提案として残す。正式名称・日程・承認者はOQ-GOV-002で確定し、同名だけで同一権限としない。
ゲートには必要成果物、基準版、判定者、FAIL/保留条件、期限付き例外、関連TASKを指定する。全OQが閉じていなくても許される作業と、必須未決が残れば禁止される判断を区別する。

## 3. 別承認境界
技術仕様採用／タスク着手／作業完了／文書Baseline公開／製品リリース／JET等の個別判断／発注・支出／予算変更を混同しない。ドキュメントのcanonical選択は全機能のAPPROVED化ではない。G側や安全試験は専門設備・手続きの下で実施し、このSTDを活線試験の作業許可にしない。

## Open Questions

担当・実予算・承認閾値・運用環境の未決は [GOV Open Questions](Open_Questions.md) を参照する。本文の運用案は、未確定の製品仕様や支出の承認を代行しない。
