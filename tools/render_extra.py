"""Additional dynamic views. Preserve free-form test guidance and source history."""
from pathlib import Path
import json,os,re
from common import jread, jwrite

def render_extra(root,workspace):
 def write(p,text): (root/p).write_text(text,encoding='utf-8')
 def cell(v):return str(v).replace('|','&#124;').replace('\n','<br/>')
 def link(p,target,label,anchor=''):
  return '['+label+']('+os.path.relpath(root/target,(root/p).parent).replace(os.sep,'/')+('#'+anchor if anchor else '')+')'
 req=jread(root/'data/requirements.json')['requirements'];tests=jread(root/'data/test_catalog.json')['tests'];fc=jread(root/'data/function_catalog.json');qs=jread(root/'data/completion_items.json')['items'];qm={q['question_id']:q for q in qs}
 def footer(p):
  return '\n## Open Questions — 本ビューの完成\n\n'+link(p,qm['OQ-R6-19-01']['note'],'OQ-R6-19-01','oq-r6-19-01')+'：正式USDM・要求対応。'+link(p,qm['OQ-R6-17-01']['note'],'OQ-R6-17-01','oq-r6-17-01')+'：受入条件。\n'
 # Catalog details are generated from tests; introductory cautions remain authored Markdown.
 p='appendices/Test_Profiles.md';old=(root/p).read_text();start=re.search(r'^## (?:T\d+|SYS-T\d+) —',old,re.M)
 prefix=old[:start.start()] if start else '# 試験プロファイルと受入条件\n\n'
 prefix=re.split(r'<!-- GENERATED:|<a id="(?:t[0-9]+|sys-t[0-9]+)"',prefix,maxsplit=1)[0]
 out=prefix+f'<!-- GENERATED: {len(tests)} test records -->\n\n'
 for t in tests:
  out+=f'<a id="{t["id"].lower()}"></a>\n## {t["id"]} — {t["condition"]}\n\n**来歴：** {t["origin"]}　**状態：** {t["status"]}\n\n**期待結果：** {t["expected"]}\n\n**要求：** '+', '.join(t['system_requirement_ids'])+f'\n\n**受入プロファイル：** {t["acceptance_profile"]}。未確定条件を実施済み・合格としない。\n\n'
 write(p,out+footer(p))
 p='appendices/Traceability.md'
 out='# 要求・機能・試験の双方向対応\n\n生成正本：requirements.json、function_catalog.json、test_catalog.json。版固定の原典表は30_referencesのR8原本に保持。\n\n| SYS要求 | 原典ARCH | 全体機能 | GW機能 | 検証 |\n|---|---|---|---|---|\n'
 for r in req:
  ss=[f['id'] for f in fc['system_functions'] if r['id'] in f['requirement_ids']];gg=[f['id']for f in fc['gw_functions']if r['id'] in f['requirement_ids']]
  out+='| '+link(p,'appendices/Requirements_Catalog.md',r['id'],r['id'].lower())+' | '+', '.join(r.get('source_arch_ids',[]))+' | '+', '.join(ss)+' | '+', '.join(gg)+' | '+(', '.join(r['verification_ids']) or r.get('verification_review','未設定'))+' |\n'
 out+='\n## 試験から要求への逆引き\n\n| 試験 | 対応SYS | 状態 |\n|---|---|---|\n'
 for t in tests:out+=f'| {t["id"]} | '+', '.join(t['system_requirement_ids'])+f' | {t["status"]} |\n'
 write(p,out+footer(p))
 p='appendices/Functional_Allocation.md'
 out='# システム全体・GW機能・要求配賦\n\nfunction_catalog.jsonから生成する。機能群は承認済みUSDMの代替ではない。\n\n| 全体機能 | GWへの配賦 | SYS要求 |\n|---|---|---|\n'
 for f in fc['system_functions']:out+=f'| {f["id"]} {f["name"]} | '+', '.join(f['gw_function_ids'])+' | '+', '.join(f['requirement_ids'])+' |\n'
 out+='\n## GWから全体機能への逆引き\n\n| GW機能 | 上位全体機能 | SYS要求 |\n|---|---|---|\n'
 for f in fc['gw_functions']:out+=f'| {f["id"]} {f["name"]} | '+', '.join(f['parent_system_function_ids'])+' | '+', '.join(f['requirement_ids'])+' |\n'
 write(p,out+footer(p))
 # Capture only the sources actually referenced by this baseline, not unrelated later imports.
 prov=jread(root/'data/import_provenance.json');used={v for r in req for v in r['source_ids']}|{t['source_id'] for t in tests}|{f['source_id'] for f in prov['fragments']}|{'CTX-R9','SRC-IMPORT-REVIEW','SRC-BASE-R8-FIX001'}
 registry=jread(workspace/'30_references/source_register.json')['sources'];sources=[s for s in registry if s['source_id'] in used]
 jwrite(root/'data/source_bindings.json',{'schema':'spkgw.source-register/v1','sources':sources})
 p='appendices/Source_Register.md';out='# 原資料台帳 — 当Baselineで参照する原資料\n\n文書の存在・版・バイトを管理する。原文位置の解釈確認や製品採用とは別。継承A/CTX/SP IDは原本の出典粒度を保持し、段落・セル位置を捏造しない。\n\n| 出典ID | 文書版 | 原本 | SHA-256 | 区分・承認 |\n|---|---|---|---|---|\n'
 for s in sources:
  h=os.path.relpath(workspace/s['path'],(root/p).parent).replace(os.sep,'/')
  out+=f'| {s["source_id"]} | {cell(s["revision"])} | [{cell(Path(s["path"]).name)}]({h}) | `{s["sha256"]}` | {s["basis"]} / {s["approval_state"]} |\n'
 write(p,out+footer(p))
 p='appendices/Import_Merge_Decisions.md';out='# 採用済みBaselineに含まれる原資料・マージ判断\n\n20_workの分析・草案は正本から参照しない。採用時に必要な断片・確認・判断をimport_provenance.jsonへ写し、原本は30_referencesに保持する。\n\n'
 if not prov['bindings']:out+='**今回、旧Word/Excelから採用した製品仕様は0件。** 元資料の実体が未提供のため、合成テストの値を製品仕様へ入れていない。\n'
 else:
  out+='| 対象 | 断片 | 判断ID | 採用レコードhash |\n|---|---|---|---|\n'
  for b in prov['bindings']:out+=f'| {b["target_kind"]}:{b["target_id"]} | '+', '.join(b['fragment_ids'])+f' | {b["decision_id"]} | `{b["record_sha256"]}` |\n'
 write(p,out+footer(p))
 p='appendices/USDM_Traceability.md';u=jread(root/'data/usdm.json')['elements'];ls=jread(root/'data/trace_links.json')['links']
 out='# 要求・理由・仕様とUSDM対応\n\nプロジェクト内の中間モデル。AFFORDD公式USDM-Schemaへの適合は宣言しない。正式版を採用する際は変換・往復テストを別途実施する。\n\n'
 if not u:out+='**USDM要素は未登録。** 既存SYSの単数usdm_id=nullを残す。理由を推定で確定しない。正式対応は多対多のtrace_links.jsonで管理する。\n'
 for e in u:
  out+=f'<a id="{e["id"].lower()}"></a>\n## {e["id"]} {e["kind"]}\n\n{e["text"]}\n\n**理由：** {e["reason"]["text"] or "未確認"}（{e["reason"]["state"]}）。**状態：** {e["status"]}。\n\n**上位：** '+', '.join(e['parent_ids'])+'\n\n'
 out+='\n## 型付きリンク\n\n| ID | 起点 | 関係 | 終点 | 確認状態 |\n|---|---|---|---|---|\n'
 for l in ls:out+=f'| {l["id"]} | {l["from"]["kind"]}:{l["from"]["id"]} | {l["relation"]} | {l["to"]["kind"]}:{l["to"]["id"]} | {l["state"]} |\n'
 write(p,out+footer(p))
