---
schema: spkgw.governance-note/v1
document_id: STD-GOV-005
project: SPK-GW_HEMS
document_type: STANDARD
revision: 1.2.0
status: DRAFT_FOR_REVIEW
title: 開発17工程・可読コード・活動種別・判断ゲート
owner: null
document_trace_id: DTR-SPKGW-GOV-000012
item_trace_ids: []
thread_id: THR-SPKGW-GOV-000001
related_thread_ids: []
trace_contract: spkgw.lifecycle-tags/v2
phase_ids: []
phase_scope: UNASSIGNED
activity_type: UNSPECIFIED
created_on: '2026-10-08'
updated_on: '2026-10-08'
classification: INTERNAL
source_baseline: BL-R9-0001
related_ids: []
---

# 開発17工程・可読コード・活動種別・判断ゲート

## 1. 工程コード

数字順ではなく、次の英字コードを記録する。旧P番号との対応は[別名表](trace_aliases.json)に保存する。番号は表示順`order`にだけ利用する。

| 工程略称 | 正式な開発フェーズ | 英語の意味 | 主な内容 |
|---|---|---|---|
| `CONCEPT` | 企画・構想 | Concept | 課題定義、目的、対象ユーザー、事業要求、開発範囲 |
| `REQAN` | 要求分析 | Requirements Analysis | ユーザー要求、ステークホルダー要求、ユースケース、制約整理 |
| `REQSPEC` | 要求仕様策定 | Requirements Specification | 機能要求、非機能要求、外部仕様、受入条件 |
| `SYSDES` | システム設計 | System Design | システム構成、責務分割、HW/SW分割、インターフェース |
| `ARCH` | アーキテクチャ設計 | Architecture | プロセス構成、レイヤ構成、データフロー、通信方式、状態管理 |
| `BASIC` | 基本／構造設計 | Basic / Structural Design | モジュール構成、コンポーネント、API、状態遷移、DB／データモデル |
| `DETAIL` | 詳細設計 | Detailed Design | クラス、関数、アルゴリズム、通信シーケンス、例外処理 |
| `IMPL` | 実装 | Implementation | コーディング、静的解析、コードレビュー |
| `UT` | 単体テスト | Unit Test | 関数・クラス・モジュール単位の検証 |
| `IT` | 結合テスト | Integration Test | モジュール間、プロセス間、通信インターフェースの検証 |
| `ST` | システム／機能テスト | System / Functional Test | システム全体として要求仕様を満たすか確認 |
| `NFT` | 非機能テスト | Non-functional Test | 性能、負荷、耐久性、セキュリティ、障害耐性 |
| `VALID` | 受入・妥当性確認 | Validation | ユーザー要求・製品要求に対するValidation |
| `RELPREP` | リリース準備 | Release Preparation | リリース判定、成果物整理、マニュアル、移行計画 |
| `RELEASE` | リリース／導入 | Release / Deployment | 製品・サービスへの展開、現場導入 |
| `OPS` | 運用・保守 | Operations / Maintenance | 障害対応、監視、改善、アップデート |
| `IMPROVE` | 振り返り・改善 | Improvement / Retrospective | 開発プロセス、品質、設計、組織運営の改善 |


## 2. 工程・文書・項目・活動を分ける

一つの文書DTRに複数工程の項目ITRを収容してよい。REQSPECの項目をIMPL/UT/OPSから参照しても、その要求のITRを改名しない。工程に属する個別項目は各自のITRと版を持ち、項目間のrefines/implements/verifies等で上流とつなぐ。

調査RESEARCH、会議MEETING、レビューREVIEW、プロジェクト管理PROJECT_MANAGEMENT、手戻りREWORK等は`activity_type`。例：SYSDES/ARCHで行うRESEARCH、DETAILのREVIEW、NFT/OPSのMEETING。これらを18番目以降の工程として追加しない。

## 3. 適用・反復・省略

テーマを使う場合、17工程についてAPPLICABLE／NOT_APPLICABLE／TBDを宣言する。対象外は根拠と判断証拠を付ける。工程の反復・並行・戻りを許し、テストは検証対象の要求や設計を直接参照する。会議記録だけで工程の技術的な完了を満たさない。

## 4. ゲートと実績

企画目的、要求の採用、設計受入、コードレビュー、試験結果、利用目的の妥当性、リリース、導入の確認を別の判断として残す。LINKED_RECORDSは形式的に根拠鎖がある状態であり、製品合格・工程承認・進捗100%ではない。工数・予算はleaf TASKの原票で集計し、複数工程へ参照しても重複計上しない。

## 5. 移行

P01等は[旧番号→略称表](trace_aliases.json)へ正確に1対1移行。旧MANAGEMENT等は工程と活動の混同があるため、初期4TASKの工程をUNASSIGNED、活動をPROJECT_MANAGEMENTとして残す。着手前に実担当が該当工程を確定する。過去の作業・実績を行ったことにはしない。

## Open Questions

実担当・実成果・運用環境は[管理OQ](Open_Questions.md)で確定する。製品要求・工程完了の承認ではない。
