---
title: "テンプレート — DER機器・接続・認証プロファイル"
project: SPK-GW_HEMS
version: "1.0"
created: 2026-10-06
updated: 2026-10-06
status: template-unfilled
language: ja
tags: [SPK-GW_HEMS, architecture, HEMS, JET]
---

# テンプレート — DER機器・接続・認証プロファイル

> 未記入テンプレートです。例示したフィールド名はSPK-GWの内部管理案であり、ECHONET Liteの標準データ形式ではありません。

## 1. 物理装置と通信識別

| 項目 | 記入欄 |
|---|---|
| Profile ID / revision | TBD |
| メーカー・型式・ハードウェア版・FW版 | TBD |
| physical_device_id | TBD |
| resource_id | TBD |
| conversion_group_id | TBD |
| connection_point_id | TBD |
| クラス識別子／EOJ／インスタンス | TBD |
| ECHONET Lite版・APPENDIX版・AIF版 | TBD |
| 接続Transport・セキュリティ状態 | TBD |

## 2. 操作能力

| 操作 | 対応 | 許可範囲・単位・符号 | 更新待ち時間 | 実行確認方法 |
|---|---|---|---|---|
| 状態取得 | UNKNOWN | TBD | TBD | TBD |
| 運転モード要求 | UNKNOWN | TBD | TBD | TBD |
| 充放電電力要求 | UNKNOWN | TBD | TBD | TBD |
| PV出力制限要求 | UNKNOWN | TBD | TBD | TBD |
| Q／力率制御 | UNKNOWN | TBD | TBD | TBD |
| 要求の機器側期限 | UNKNOWN | TBD | TBD | TBD |
| 制限理由の取得 | UNKNOWN | TBD | TBD | TBD |

検出したSetプロパティマップ、メーカー資料、実機確認を結びます。`UNKNOWN`を`SUPPORTED`へ自動変換しません。

## 3. トポロジーと制約範囲

計測点、AC／DC基準、共通PCS容量、同時動作可能範囲、排他モード、連系点の合算対象を記載します。

**構成図／記入：TBD**

## 4. 系統・契約上の適用

| 項目 | 記入欄 |
|---|---|
| 一般送配電事業者・接続エリア | TBD |
| 接続契約・設備規模・逆潮流の可否 | TBD |
| 制約種別・容量の根拠 | TBD |
| 制約scope（機器／グループ／連系点） | TBD |
| GridApplicability | UNKNOWN |
| 判定根拠・確認日・確認者 | TBD |
| 自家消費継続・0%時の運転 | TBD |
| 過渡応答・許容差・評価窓 | TBD |

## 5. 認証・強制経路

| 項目 | 記入欄 |
|---|---|
| 認証登録番号・申請主体 | TBD |
| 対象PCS・出力制御装置・計測器 | TBD |
| 対象ソフトウェア識別・組合せ | TBD |
| 通常操作が制約を迂回しない根拠 | TBD |
| 適用試験方法の版 | TBD |
| HEMS停止時に継続するG側機能 | TBD |
| JET／メーカーとの確認記録 | TBD |

## 6. 障害・本体操作・競合

| 条件 | 実機の動作 | HEMSの動作 | 受入可否・根拠 |
|---|---|---|---|
| HEMS通信断 | TBD | TBD | TBD |
| 旧通常要求の保持 | TBD | TBD | TBD |
| 電力会社通信断 | TBD | TBD | TBD |
| G側内部通信断 | TBD | TBD | TBD |
| 計測／時刻異常 | TBD | TBD | TBD |
| 本体操作・純正アプリ操作 | TBD | TBD | TBD |
| HEMS OTA・復帰 | TBD | TBD | TBD |
| EV離脱・負荷急減 | TBD | TBD | TBD |

## 7. サポートする用途と制限

対応する通常運転Usecase、非対応機能、更新周期、未達・不明時の通知、必要な設置条件を記載します。

**記入：TBD**

## 8. 評価状態

**資料確認：TBD**  
**シミュレータ試験：NOT_RUN**  
**実機試験：NOT_RUN**  
**認証構成確認：TBD**  
**製品対応判定：TBD**

参照： [機器分類](../05_Device_Classes.md)／[契約](../06_Contracts.md)／[電力制約](../07_Power_Constraints.md)
