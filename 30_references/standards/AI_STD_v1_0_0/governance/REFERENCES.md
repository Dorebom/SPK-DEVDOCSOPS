# 公式情報・作成根拠

確認日：**2026-10-07**。本パッケージの版：1.0.0。

本標準の役割分担、受入条件、記録量、進捗算式、初期運用値は、SPK-GW_HEMS向けの**運用設計案**である。GitHub・IPAから一律に要求される標準として記載していない。外部の製品仕様は以下の一次資料を確認した。

## 1. GitHub・VS Code

| ID | 一次資料 | 本パッケージで参照する点 |
| --- | --- | --- |
| GH-01 | [Adding repository custom instructions for GitHub Copilot](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions) | 共通指示、パス別指示、applyTo、参照の確認 |
| GH-02 | [Support for different types of custom instructions](https://docs.github.com/en/copilot/reference/custom-instructions-support) | 機能・クライアントによる対応差 |
| GH-03 | [About customizing GitHub Copilot responses](https://docs.github.com/en/copilot/concepts/prompting/response-customization?tool=vscode) | 指示の非決定的な適用と、簡潔な文脈 |
| GH-04 | [GitHub Copilot on GitHub.com](https://docs.github.com/en/copilot/concepts/copilot-surfaces/copilot-on-github) | cloud agentの実行環境と利用形態 |
| GH-05 | [About GitHub Copilot code review](https://docs.github.com/en/copilot/concepts/agents/code-review) | レビュー、Copilot approvals、実際の業務判断との区別 |
| GH-06 | [Content exclusion for GitHub Copilot](https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/content-exclusion) | Edit/Agentの非対応など、保護範囲の限界 |
| GH-07 | [About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) | レビュー、必要なチェック、統合の制御 |
| GH-08 | [About rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets) | ブランチ・タグ等への制御。利用可否はプラン・設定による |
| VS-01 | [Use custom instructions in VS Code](https://code.visualstudio.com/docs/agent-customization/custom-instructions) | 指示の配置・適用・読込確認、実行方式による差 |
| VS-02 | [Use prompt files in VS Code](https://code.visualstudio.com/docs/agent-customization/prompt-files) | .prompt.md、手動呼出、Local agentとAgent Hostの差 |
| VS-03 | [Manage approvals and permissions](https://code.visualstudio.com/docs/agents/run/approvals) | 承認と隔離の役割の区別 |
| VS-04 | [Secure AI-assisted development in VS Code](https://code.visualstudio.com/docs/agents/run/security) | 外部入力、情報露出、ワークスペースの信頼 |

### 対応差を確認した箇所

- `governance/STD/` 自体は、全ノートの自動添付や遵守を保証する配置ではない。入口から必要な文書を明示して使う。
- VS Codeのprompt filesは、確認時点でAgent Hostでは未読込、Local agentでは継続利用できると説明されている。そのため同梱3件は任意の補助とする。
- Copilot approvalsの技術的な承認表示と、本STDで指定する受入・計画採用・リリースの判断を区別する。
- Content exclusionの対応範囲を全実行モードへ一般化しない。特に公式本文で非対応とされるEdit/Agentへ、除外済みだから秘密を置いてよいと解釈しない。

これらは確認時点の仕様であり、導入先の利用プラン、VS Codeと拡張の版、選択モード、組織設定は今回未確認。環境変更時は該当する一次資料を確認する。

## 2. セキュリティ制度

| ID | 一次資料 | 参照する点 |
| --- | --- | --- |
| IPA-01 | [IPA セキュリティ要件適合評価及びラベリング制度（JC-STAR）](https://www.ipa.go.jp/security/jc-star/index.html) | 制度の公式入口。対象レベル・基準・申請・変更等の資料確認先 |

STD-10とT-09は自社・委託先間の開発記録を整えるための様式であり、IPA指定様式ではない。JC-STARの個別要件や届出期限を本パッケージから推定しない。JETへの影響も実際の認証範囲と担当者の確認による。

## 3. プロジェクト文脈

この会話で提供された情報に基づき、次を考慮した。

- Windows 11／VS Codeを利用し、Yocto Linux／C主体の既存製品へHEMS機能を追加すること。
- As-IsとTo-Be、既存機能と追加機能を分けて把握すること。
- HEMS側の名称としてDER Power Controllerを使う方向。
- 2026-10-06の方針として、PCS取得方式とGW取得・管理方式を選択肢とし、通信は宅内ルータ経由とすること。PCS自身の直接取得はECHONET LiteのPCSを対象にし、RS-485のPCSはGWが担うこと。
- 一部の1秒制御、認証・暗号対応機器と従来機器の混在、設定変更と制御競合を扱うこと。
- 実案件のAI利用から、品質・手戻り・時間・能力に関するデータを得ること。

上記は今回の標準案を組み立てるための文脈である。既存リポジトリ、現行governance、仕様書・設計書の全内容は未取得のため、導入先の採用済み正本と照合する。SHIRABE専用のJSONプロトコルや実行ランタイムを、GW_HEMSへ自動適用していない。

## 4. 保守の方法

外部機能の変更を見つけたら、影響するSTD-02と入口・プロンプトを対象に見直す。製品要求や日々の作業規則を、外部UI名称の変化だけで一括改訂しない。参照URLと確認日、変更理由、影響した箇所を改訂記録へ残す。
