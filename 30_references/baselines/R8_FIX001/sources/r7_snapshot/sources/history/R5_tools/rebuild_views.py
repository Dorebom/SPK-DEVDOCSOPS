#!/usr/bin/env python3
"""Regenerate Markdown register views and the integrated system specification."""
from pathlib import Path
import json, re, textwrap
ROOT=Path(__file__).resolve().parents[1]
def write(rel,text):
    p=ROOT/rel; p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(textwrap.dedent(text).strip()+'\n',encoding='utf-8')
def rows_for(text,pattern):
    return [[c.strip() for c in line.strip().strip('|').split('|')]
            for line in text.splitlines() if re.match(r'^\| '+pattern+r' \|',line)]
index=json.loads((ROOT/'data/document_index.json').read_text(encoding='utf-8'))
chapters=index['chapters']
reqs=json.loads((ROOT/'data/requirements.json').read_text(encoding='utf-8'))['requirements']
source_tests=json.loads((ROOT/'data/test_catalog.json').read_text(encoding='utf-8'))['tests']
issues=json.loads((ROOT/'data/open_issues.json').read_text(encoding='utf-8'))['issues']
params=json.loads((ROOT/'data/parameters.json').read_text(encoding='utf-8'))['parameters']
source_text=(ROOT/'sources/architecture/10_Requirements_Tests.md').read_text(encoding='utf-8')
source_dec=(ROOT/'sources/architecture/11_Migration_Decisions.md').read_text(encoding='utf-8')
arch_rows=rows_for(source_text,r'ARCH-\d{3}')
dec_rows=rows_for(source_dec,r'DEC-\d{3}')
for t in source_tests:
    t['system_requirement_ids']=[r['id'] for r in reqs if t['id'] in r['verification_ids']]
test_register=json.loads((ROOT/'data/test_catalog.json').read_text(encoding='utf-8'))
test_register['tests']=source_tests
write('data/test_catalog.json',json.dumps(test_register,ensure_ascii=False,indent=2))

# Generate reviewable Markdown views of the registers.
chapter_by_num={c['number']:c for c in chapters}
def chlink(n):
    c=chapter_by_num[n]
    return f"[第{n:02d}章](../chapters/{c['file']}#ch-{n:02d})"

catalog=['# 要求カタログ — SYS要求のレビュー用ビュー','',
'原子要求の管理用正本は[data/requirements.json](../data/requirements.json)。本ファイルは同データから生成する。章本文は責務・動作・例外の説明を補う。原典判断は履歴保持し、R4でのルータ必須・機器接続別限定を[R4判断差分](R4_Decision_Changes.md)へ記録する。機器・実装・認証承認とは分ける。',
'',f'要求件数：**{len(reqs)}件**。全件DRAFT_FOR_REVIEW。原典ARCH対応24件と追加具体化要求を区別する。正式USDM IDは全件未対応として明示している。','']
for r in reqs:
    aid=', '.join(r['source_arch_ids']) or '追加具体化（原典ARCHの上書きなし）'
    vids=', '.join(r['verification_ids']) or '文書・契約レビュー'
    catalog += [f"## {r['id']} — {r['title']}",'',r['requirement'],'',
                f"**対象章：** {chlink(r['chapter'])}　**配賦：** {r['allocation']}",
                f"**根拠：** {r['basis']} / {', '.join(r['source_ids'])}　**原典：** {aid}",
                f"**検証：** {vids}。レビュー補足：{r['verification_review']}。",
                '**状態：** DRAFT_FOR_REVIEW。実装・試験・正式USDM対応の完了を示さない。','']
write('appendices/Requirements_Catalog.md','\n'.join(catalog))

trace=['# 原典要求・システム仕様・試験の対応','',
'原典[10_Requirements_Tests.md](../sources/architecture/10_Requirements_Tests.md)のARCH番号と意味を保持する。下表は要求の継承・展開状況であり、試験合格・認証承認の対応表ではない。','',
'| 原典ARCH | 原典の要求案 | SYS要求 | 主な章 | 検証 |',
'|---|---|---|---|---|']
for aid,orig,method in arch_rows:
    rr=[r for r in reqs if aid in r['source_arch_ids']]
    trace.append(f"| {aid} | {orig} | {', '.join(r['id'] for r in rr)} | {', '.join(chlink(r['chapter']) for r in rr)} | {method} |")
trace += ['', '## 検証シナリオと要求の逆引き','',
'原典T01〜T19とSYS-T01〜50を別名前空間で管理する。R1〜R3を継承し、R4で8件を追加、既存5件の条件を明示改訂。作成時は全件NOT_RUN。個別の状態は管理データを参照。受入条件の詳細は[Test Profiles](Test_Profiles.md)を参照。','',
'| 試験ID | 来歴 | 対応SYS要求 | 実行状態 |','|---|---|---|---|']
for t in source_tests:trace.append(f"| {t['id']} | {t['origin']} | {', '.join(t['system_requirement_ids'])} | {t['status']} |")
trace += ['', '## 対応関係の限界','', '本表の全件対応は、要求が書面上どこへ展開されたかを示すだけである。閾値の確定、実装の存在、実機・保護動作、変更手続きの完了は別の証拠を要する。']
write('appendices/Traceability.md','\n'.join(trace))

openmd=['# 判断状態・未確定事項の台帳','',
'管理データ：[data/open_issues.json](../data/open_issues.json)。以下の原典判断は当時の履歴。R4の現在の配置選択方針は[R4判断差分](R4_Decision_Changes.md)で明示変更した。機器・認証の未確認事項は解消していない。','',
'## 原典の設計判断','', '| ID | 内容 | 原典の状態 |','|---|---|---|']
for row in dec_rows:openmd.append('| '+' | '.join(row)+' |')
openmd+=['','## 原典の未確定事項','', '| ID | 未確定事項 | 解消条件・確認先 | 状態 |','|---|---|---|---|']
for x in issues:
    if x['origin']=='SOURCE_INHERITED':openmd.append(f"| {x['id']} | {x['subject']} | {x['resolution']} | OPEN |")
openmd+=['','## 本書で追加した確認事項','', '| ID | 未確定事項 | 解消条件 | 確認担当の役割 | 状態 |','|---|---|---|---|---|']
for x in issues:
    if x['origin']=='SYSTEM_SPEC_ADDITION':openmd.append(f"| {x['id']} | {x['subject']} | {x['resolution']} | {x['owner_role']} | OPEN |")
openmd+=['','## レビューの優先順','',
'最初にSYS-TBD-001〜003、SYS-TBD-024〜034と原典TBD-001〜006を確認する。R4対応表の機器対応・ルータ実経路・G側実配置・構成変更・認証構成が不明なまま、更新非影響や切替完了を確定しない。原典TBD-005は外部化要否の履歴であり、現在は両方式ごとの成立構成を確認する。']
write('appendices/Open_Issues.md','\n'.join(openmd))

pmd=['# パラメータ・受入閾値台帳','',
'全件未確定。`null`は未確定であり、0、無制限、未使用を意味しない。対象構成、根拠文書・版、確認者、決定日を追加して確定する。原典の数値例を製品閾値としてコピーしない。','',
'| ID | パラメータ | 単位／形式 | 適用scope | 確認根拠 | 関連TBD | 値 |','|---|---|---|---|---|---|---|']
for p in params:pmd.append(f"| {p['id']} | {p['name']} | {p['unit']} | {p['scope']} | {p['basis_to_confirm']} | {p['issue_id']} | TBD |")
pmd += ['','## 数値の扱い','',
'1秒は先行ユーザー要求の対象候補であり、送信・達成・全機器共通保証ではない。添付の60秒は特定AIF・操作の説明例、5分は引用元の定義する内部通信異常の例である。いずれも適用文書・実機・経路・版を確認して該当プロファイルへ登録する。今回これらの規格を再検証していない。']
write('appendices/Parameter_Register.md','\n'.join(pmd))

profiles=['# 試験プロファイルと受入条件','',
'これは未実施の試験計画。原典のT01〜T19を継承し、RS-485等の追加SYS-Tを分ける。実行データ正本：[test_catalog.json](../data/test_catalog.json)。','',
'## すべてのRunに必要な情報','',
'run_id、宅内ルータ構成とFW、往復経路・端点・採用機器接続種別、要求ID、試験ID、対象HW/FW、HEMS/G側版、機器プロファイル、PCS_DIRECT/GW_MANAGED、grid_control_scope_id、G側実配置、grid_control_epoch、切替Job、route_role、配線・計測点、契約・認証適用版、設定、時計基準、初期状態、注入位置・条件、要求系列、観測品質、波形／イベント、閾値・評価窓、結果、評価者を記録する。','',
'数値・プロファイル未確定で判定できないときはINCONCLUSIVE、未実施はNOT_RUN。対象外はNOT_APPLICABLEと根拠を記録する。文書・シミュレータの確認を実機保護の合格としない。','',
'## 原典の試験を実行条件へ展開する際の注意','',
'負の電力値は採用符号で充電の正常値になり得る。T05では負値という形式だけで異常とせず、operation・符号・許可範囲から正常／範囲外を判定する。物理切離しは通常クライアントが任意に切離し可能な構成での試験であり、必須G側通信を切った場合は別注入として扱う。活線・保護試験は専門の安全設備・手順・担当者で行う。','']
for t in source_tests:
    profiles += [f"## {t['id']} — {t['condition']}",'',f"**来歴：** {t['origin']}　**状態：** {t['status']}",'',
                 f"**期待結果：** {t['expected']}。",'',
                 f"**要求：** {', '.join(t['system_requirement_ids'])}",'',
                 '**成立条件：** 対象構成・操作・経路・数値閾値を確定した受入プロファイルへ結び付ける。TBDのまま包括的PASSを付けない。','']
write('appendices/Test_Profiles.md','\n'.join(profiles))




ifdata=json.loads((ROOT/'data/external_interfaces.json').read_text(encoding='utf-8'))['interfaces']
ifview=['# 外部IF・上位契約台帳','',
'R1〜R3の16件を維持し、R4でIF-GRID-01〜03・IF-RS-01・IF-EL-01へルータ経由・機器接続別対応を明示改訂した。論理サービスとTCP接続を一対一に固定せず、用途別責務は[第20章](../chapters/20_Northbound_Monitoring_FW.md#ch-20)による。管理データは[data/external_interfaces.json](../data/external_interfaces.json)。','',
'| ID | 導入 | 契約 | 主体→相手 | 情報・機能 | 条件 |','|---|---|---|---|---|---|']
for f in ifdata:ifview.append(f"| {f['id']} | {f['introduced_revision']} | {f['name']} | {f['actor']}→{f['peer']} | {f['information']} | {f['conditions']} |")
ifview+=['','## 未確定欄','',
'物理配置、通信プロトコル、接続開始側、FQDN/IP・ポート・IPv4/IPv6、暗号・接続先識別、認証と委譲、公開操作・データ、数値制限、期限・再送・重複、結果、障害・復旧、版・互換、監査、試験条件を各プロファイルで確定する。nullは未確定であり、無認証・無制限の意味ではない。', '',
'宅内という接続名だけで管理権限を付けず、IF-MAINT-01を通常上位APIの管理者フラグで有効にしない。FW適用の論理契約を別TCP接続の必須要件と読み替えない。']
ifview += ['', '## R5追補：IF-EL-01の通常機器接続', '',
'IF-EL-01のレコードと許可範囲はR4から変更しない。対象はPCSだけでなく、空調・給湯・計測器等の対応EL機器である。H側のEL Controller → H側LAN接続 → 宅内ルータLAN／AP → 各機器EL IFの往復経路を[第2.1節の拡大図](../chapters/02_System_Context.md#fig-02-01-el)で明示する。DPCはPV・蓄電池等、FLCは空調・給湯等、Measurement／Device Stateは計測・状態・品質を担当する。PCSサーバ取得はIF-GRID-01の別契約であり、通常EL経路へ統合しない。']
write('appendices/External_Interface_Register.md','\n'.join(ifview))

# Integrated view: internalize links to included chapters/appendices; retain source/data links.
import os
paths=[ROOT/'chapters'/c['file'] for c in index['chapters']]
paths += [ROOT/'appendices'/a['file'] for a in index['appendices']]
anchors={p.resolve():(f"ch-{c['number']:02d}") for p,c in zip(paths[:len(chapters)],chapters)}
for a in index['appendices']:
    anchors[(ROOT/'appendices'/a['file']).resolve()]='ap-'+Path(a['file']).stem.lower().replace('_','-')
def strip_front(text):
    return re.sub(r'^---\n.*?\n---\n','',text,count=1,flags=re.S).lstrip()
def convert_links(text,src):
    def replace(m):
        label,target=m.groups()
        if target.startswith(('http:','https:','mailto:','#')): return m.group(0)
        base,sep,fragment=target.partition('#')
        abs_path=(src.parent/base).resolve()
        if abs_path in anchors:
            return f'[{label}](#{fragment if sep else anchors[abs_path]})'
        rel=os.path.relpath(abs_path,ROOT).replace(os.sep,'/')
        return f'[{label}]({rel}'+('#'+fragment if sep else '')+')'
    return re.sub(r'\[([^\]\n]+)\]\(([^)\n]+)\)',replace,text)
intro=['---','title: "SPK-GW_HEMS システム仕様書 — 出力制御二方式・上位・宅内・FW統合版"','revision: "R5"','updated: 2026-10-06','status: DRAFT_FOR_REVIEW','source_baseline: "SPK-GW_HEMS_ToBe_v1_0_20261006"','---','',
'# SPK-GW_HEMS システム仕様書 R5','',
'R4を基準に、H側ECHONET Lite Controllerから空調・給湯・計測器・PCSへの通常EL往復経路を第2.1節で明示した。全出力制御サーバ通信の宅内ルータ経由条件は維持する。PCS_DIRECTはECHONET Lite接続PCSの自律取得、GW_MANAGEDはRS-485接続PCSのGW取得・管理・指示に限定する。上位・Web・アプリ・FW配信、通常運転と系統制御の分離は維持する。型式・G側実配置・ネットワーク詳細・構成変更・認証条件・数値は未確定として管理する。**実装・実機試験・認証承認の完了を示さない。**','',
'このファイルは章本文と別冊を連結した生成ビュー。原典・管理データへの参照は同梱ZIP内の相対リンクである。元アーキテクチャの統合ノートではなく、システム仕様の新しい成果物。','',
'## 目次','']
for c in chapters:intro.append(f"- [{c['number']:02d}. {c['title']}](#ch-{c['number']:02d})")
for a in index['appendices']:
    p=(ROOT/'appendices'/a['file']).resolve()
    intro.append(f"- [別冊：{a['title']}](#{anchors[p]})")
combined='\n'.join(intro)+'\n'
for p in paths:
    body=strip_front(p.read_text(encoding='utf-8'))
    anchor=anchors[p.resolve()]
    if f'<a id="{anchor}"></a>' not in body:
        body=f'<a id="{anchor}"></a>\n\n'+body
    combined+='\n---\n\n'+convert_links(body,p)
write('90_All_In_One.md',combined)
print(f"Generated integrated view: {len(chapters)} chapters, {len(index['appendices'])} appendices")

# Top-level index and reading guide use current metadata.
info=json.loads((ROOT/'package_info.json').read_text(encoding='utf-8'))
moc=[f"# MOC — SPK-GW_HEMS システム仕様書 {info['revision']}", '',
'状態：DRAFT_FOR_REVIEW。R5は第2.1節のEL接続図修正。[改訂要約](appendices/Change_Summary.md) → [第02章の全体構成](chapters/02_System_Context.md) → [第21章の経路・責務](chapters/21_Grid_Connection_Selection.md) → [R5の図修正](appendices/R5_Diagram_Changes.md)。全体は[統合版](90_All_In_One.md)。','', '## 本編','', '| 章 | 内容 |','|---|---|']
for c in index['chapters']:moc.append(f"| {c['number']:02d} | [{c['title']}](chapters/{c['file']}) |")
moc+=['','## 別冊','', '| 文書 | 用途 |','|---|---|']
for a in index['appendices']:moc.append(f"| [{a['file']}](appendices/{a['file']}) | {a['title']} |")
moc+=['','## 入力と検査','', '[原典MOC](sources/architecture/00_MOC.md) ／ [R1](sources/baseline/R1.zip) ／ [R2](sources/baseline/R2.zip) ／ [R3](sources/baseline/R3.zip) ／ [R4](sources/baseline/R4.zip) ／ [CTX-R5](sources/USER_CONTEXT_R5.md) ／ [文書QA](DOCUMENT_QA.md)。過去の判断・QAは履歴として保持し、現在の適用・実施状態に読み替えない。']
write('00_MOC.md','\n'.join(moc))
readme=[f"# SPK-GW_HEMS システム仕様書 {info['revision']}", '',
'2026-10-06／DRAFT_FOR_REVIEW。R5は第2.1節の通常EL接続を明示する文書改訂。出力制御サーバとの通信は全て宅内ルータ経由。EL接続PCSはGW非経由のPCS自律取得（識別子PCS_DIRECT）、RS-485接続PCSはGW G側管理（GW_MANAGED）。両方式は機器接続構成に応じた選択であり、同一PCSの自由なmode切替ではない。','',
'入口：[第02章](chapters/02_System_Context.md) → [第21章](chapters/21_Grid_Connection_Selection.md) → [R5の図修正](appendices/R5_Diagram_Changes.md)。[統合版](90_All_In_One.md) ／ [MOC](00_MOC.md)。','',
'## 内容','', '| 内容 | 数・状態 |','|---|---|',
f"| 本編・別冊 | {len(chapters)}章・{len(index['appendices'])}別冊 |",
f"| システム要求 | {len(reqs)}件。R4からレコード不変。全件DRAFT |",
f"| システム試験計画 | {len(source_tests)}件。R4からレコード不変。全件NOT_RUN |",
f"| 未確定事項／パラメータ | {len(issues)}件／{len(params)}件。全件OPEN／未設定 |",
f"| 外部IF | {len(ifdata)}件。R4レコードは不変。説明のみ追補 |",
'| 原典・旧版 | sources/architectureとR1〜R4 ZIPを不変保持 |','',
'## 正本と再生成','',
'`chapters/`は本編、`data/`は要求・試験・未確定事項・IF・経路・テンプレート。`python tools/rebuild_views.py`で対応表・統合版・README/MOCを再生成する。個別テンプレートと改訂要約は手編集。data/revision_changes.jsonはR3→R4の履歴として保持する。R5の変更はdata/r5_document_changes.jsonで管理し、decision_overrides.jsonは変更しない。','',
'`python tools/validate_grid_selection.py`は文書モデルと合成データの整合だけを確認する。`python tools/validate_el_routes.py`はR5の図と通常EL経路を検査する。`python tools/validate_package.py`は文書構造・ID・R3→R4履歴・R4からのレコード不変・原典不変・manifestを検査する。編集後は差分をレビューして`python tools/validate_package.py --refresh-manifest`でmanifestを更新する。これらは実機・通信・保護・認証試験ではない。','',
'## 制約','',
'外部規格の再調査は実施していない。原典の公開資料確認は過去の確認履歴として保持する。特定型式、サーバプロトコル、LAN媒体、G側CPU/OS、現地切替、数値は未確定。H/G分離や文書QAからJET試験不要を保証しない。','',
'図は編集可能なMermaidソース。R5で改修した第2.1節の2図のみ構文解析・SVG/PNG描画・目視確認済み。他の図は今回未描画。詳細はDOCUMENT_QAを参照。単体統合版の本編・別冊参照は内部化するが、JSONや原典参照にはZIP内のフォルダ構成が必要。']
write('README.md','\n'.join(readme))
