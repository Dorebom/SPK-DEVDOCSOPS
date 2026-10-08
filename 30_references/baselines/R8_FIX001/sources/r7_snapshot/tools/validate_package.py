#!/usr/bin/env python3
"""R7 document-only QA. Does not run system/device tests or grant permissions.

With --refresh-manifest: write measured QA then refresh package hashes.
Without flag: validate the existing package and its manifest without writing.
Optional markdown-it-py improves Markdown parsing; a stdlib fallback is used.
"""
from __future__ import annotations
import argparse, collections, hashlib, json, re
from pathlib import Path
from urllib.parse import unquote, urlsplit
from zipfile import ZipFile
ROOT=Path(__file__).resolve().parents[1]
def load(p):return json.loads((ROOT/p).read_text(encoding='utf-8'))
def sha(b):return hashlib.sha256(b).hexdigest()
def allfiles():return sorted(p for p in ROOT.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p != ROOT/'MANIFEST_SHA256.txt')
def slug(s):
 s=re.sub(r'\[([^\]]+)\]\([^)]*\)',r'\1',s)
 return re.sub(r'[^\w\-\s]','',s.lower()).replace(' ','-')
def anchors(text):
 out=set(re.findall(r'<a\s+id="([^"]+)"',text));count=collections.Counter()
 for h in re.findall(r'^#{1,6}\s+(.+)$',text,re.M):
  a=slug(h);i=count[a];count[a]+=1;out.add(a if i==0 else f'{a}-{i}')
 return out

def check():
 errors=[];c={}
 index=load('data/document_index.json');S=load('data/function_catalog_r7.json')['system_functions'];G=load('data/function_catalog_r7.json')['gw_functions']
 reqs=load('data/requirements.json')['requirements'];reqids={r['id'] for r in reqs}
 oqs=load('data/completion_items.json')['items'];oqids={q['question_id'] for q in oqs}
 c.update(parts=len(index['parts']),chapters=len(index['chapters']),appendices=len(index['appendices']),system_function_groups=len(S),gw_function_groups=len(G),existing_requirements=len(reqs),existing_open_questions=len(oqs))
 sids={x['id'] for x in S};gids={x['id'] for x in G}
 if len(sids)!=len(S) or len(gids)!=len(G):errors.append('Duplicate function ID')
 for x in S+G:
  if set(x['requirement_ids'])-reqids:errors.append('Unknown SYS link '+x['id'])
  if set(x['open_question_ids'])-oqids:errors.append('Unknown OQ link '+x['id'])
  for p in x['source_notes']:
   if not (ROOT/p).exists():errors.append('Missing source note '+p)
  if x['implementation_status']!='NOT_VERIFIED':errors.append('Unverified implementation marked otherwise '+x['id'])
 for g in G:
  if not g['parent_system_function_ids'] or set(g['parent_system_function_ids'])-sids:errors.append('Invalid parent '+g['id'])
  for sid in g['parent_system_function_ids']:
   if g['id'] not in next(s for s in S if s['id']==sid)['gw_function_ids']:errors.append('Asymmetric mapping '+g['id'])
 for s in S:
  if set(s['gw_function_ids'])-gids:errors.append('Unknown child '+s['id'])
  for gid in s['gw_function_ids']:
   if s['id'] not in next(g for g in G if g['id']==gid)['parent_system_function_ids']:errors.append('Asymmetric reverse mapping '+s['id'])
 lineage=load('data/function_lineage_r7.json')['rows']
 if {x['r6_inventory_id'] for x in lineage}!={f'FN-DRAFT-{i:02}' for i in range(1,22)}:errors.append('R6 inventory lineage incomplete')
 if any(not x['gw_function_ids'] or set(x['gw_function_ids'])-gids for x in lineage):errors.append('Broken lineage child')
 cross=load('data/requirements_function_crosswalk_r7.json')['rows']
 if len(cross)!=len(reqs) or {x['requirement_id'] for x in cross}!=reqids:errors.append('Requirement crosswalk is incomplete')
 roles=load('data/role_access_r7.json')
 if [x['name'] for x in roles['human_roles']]!=['ユーザ','メンテナンス','メーカー','開発者']:errors.append('Role names differ from user input')
 for x in roles['permissions']:
  if any(v is not None for v in x['approved_permissions'].values()):errors.append('Permission falsely approved '+x['id'])
  if set(x['gw_function_ids'])-gids:errors.append('Unknown permission function '+x['id'])
 config=load('data/configuration_patterns_r7.json')
 if not config['all_grid_server_routes_use_home_router'] or not config['pcs_self_fetch_only_echonet_pcs'] or config['auto_mode_failover']:errors.append('Grid rules changed')
 if any(x['support_status']!='TBD_NOT_APPROVED' for x in config['patterns']):errors.append('Configuration approval invented')
 c.update(role_types=len(roles['human_roles']),proposed_operation_groups=len(roles['permissions']),configuration_patterns=len(config['patterns']),r6_inventory_rows_linked=len(lineage),requirements_crosswalk_rows=len(cross))

 # Compare exact original bytes against authorized R6 archive.
 b=ROOT/'sources/baseline/R6.zip';im=load('data/r7_input_manifest.json')
 if sha(b.read_bytes())!=im['sha256']:errors.append('R6 input SHA mismatch')
 counts=collections.Counter()
 with ZipFile(b) as z:
  if z.testzip():errors.append('R6 archive CRC failure')
  prefix='SPK-GW_HEMS_System_Spec_20261006_R6/'
  strict_data=['requirements.json','test_catalog.json','open_issues.json','parameters.json','external_interfaces.json','completion_items.json','grid_connection_profiles.json','grid_network_routes.json','echonet_normal_routes.json','decision_overrides.json']
  for name in z.namelist():
   if name.endswith('/'):continue
   rel=name[len(prefix):]
   category=None
   if rel.startswith('chapters/'):category='r6_detailed_chapters_preserved'
   elif rel.startswith('appendices/'):category='r6_appendices_preserved'
   elif rel.startswith('sources/'):category='r6_source_files_preserved'
   elif rel.startswith('diagrams/'):category='r6_diagram_files_preserved'
   elif rel in ['data/'+f for f in strict_data]:category='r6_core_data_files_preserved'
   if category:
    counts[category]+=1
    if not (ROOT/rel).exists() or (ROOT/rel).read_bytes()!=z.read(name):errors.append('Unexpected baseline change '+rel)
 c.update(counts)
 c['r6_input_sha256']=im['sha256']
 # Parse managed JSON; old history is preserved, not reinterpreted as current data.
 jfiles=list((ROOT/'data').glob('*.json'))+[ROOT/'package_info.json']
 for p in jfiles:
  try:json.loads(p.read_text(encoding='utf-8'))
  except (ValueError,UnicodeError):errors.append('Invalid JSON '+str(p.relative_to(ROOT)))
 c['managed_json_files_parsed']=len(jfiles)
 docs=sorted(p for p in ROOT.rglob('*.md') if 'sources' not in p.relative_to(ROOT).parts)
 c['current_markdown_notes']=len(docs)
 for p in docs:
  t=p.read_text(encoding='utf-8');heads=re.findall(r'^## (.*)$',t,re.M)
  if not heads or not heads[-1].startswith('Open Questions'):errors.append('Missing trailing OQ '+str(p.relative_to(ROOT)))
  if '\ufffd' in t:errors.append('Replacement character '+str(p.relative_to(ROOT)))
 c['all_current_notes_have_trailing_oq']=not any('trailing OQ' in e for e in errors)
 try:
  from markdown_it import MarkdownIt
  md=MarkdownIt('commonmark').enable('table')
  def walk(ts):
   for x in ts:
    yield x
    if x.children:yield from walk(x.children)
  def links(t):
   for tok in walk(md.parse(t)):
    if tok.type=='link_open':yield tok.attrGet('href')
    elif tok.type=='image':yield tok.attrGet('src')
  c['link_parser']='markdown-it-py'
 except ImportError:
  def links(t):yield from re.findall(r'\[[^\]\n]*\]\(([^)\n]+)\)',re.sub(r'```.*?```','',t,flags=re.S))
  c['link_parser']='stdlib-regex-fallback'
 acache={};local=0;remote=0
 for p in docs:
  for target in links(p.read_text(encoding='utf-8')):
   if not target:continue
   u=urlsplit(target)
   if u.scheme or u.netloc:remote+=1;continue
   local+=1
   dest=(p.parent/unquote(u.path)).resolve() if u.path else p.resolve()
   if not dest.exists():errors.append(f'Missing local target {p.relative_to(ROOT)} -> {target}');continue
   if u.fragment and dest.suffix.lower()=='.md':
    if dest not in acache:acache[dest]=anchors(dest.read_text(encoding='utf-8'))
    if unquote(u.fragment) not in acache[dest]:errors.append(f'Missing anchor {p.relative_to(ROOT)} -> {target}')
 c.update(local_links_checked=local,external_links_not_revalidated=remote)
 allone=(ROOT/'90_All_In_One.md').read_text(encoding='utf-8')
 exp=re.findall(r'<a\s+id="([^"]+)"',allone)
 dup=[a for a,n in collections.Counter(exp).items() if n>1]
 if dup:errors.append('Duplicate integrated anchors '+','.join(dup[:10]))
 for x in S+G:
  if exp.count(x['id'].lower())!=1:errors.append('Missing function definition in integrated view '+x['id'])
 for q in oqids:
  if exp.count(q.lower())!=1:errors.append('Missing/duplicate original OQ in integrated view '+q)
 c['integrated_function_definitions']=len(S)+len(G)
 c['integrated_original_oq_definitions']=len(oqids)
 return dict(schema='spkgw.document-qa/v1',revision='R7',scope='DOCUMENT_ONLY',result='PASS' if not errors else 'FAIL',checks=c,errors=errors,system_tests_run=False,device_tests_run=False,permissions_approved=False,configuration_certified=False)

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--refresh-manifest',action='store_true');args=ap.parse_args()
 result=check()
 if result['errors']:
  print(json.dumps(result,ensure_ascii=False,indent=2));raise SystemExit(1)
 if args.refresh_manifest:
  (ROOT/'data/r7_document_validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
  c=result['checks']
  report=['# R7 文書QA','','**検査結果：PASS（文書整合性のみ）**。実機・性能・安全・認証・認可の承認ではない。','','## 実行した検査','','| 検査 | 結果 |','|---|---|']
  for key,val in c.items():report.append(f'| {key} | {val} |')
  report+=['','## 検査範囲の限界','','機能一覧の根拠リンク・相互対応・ID・原本保持・リンク・形式を検査した。機能採否、既存実装全量の網羅、性能数値、権限付与、対応機器、JETその他認証の妥当性を合格にしたものではない。R5からの図は不変で、新規描画はしていない。','','## 再実行','','`python tools/rebuild_views.py` の後、レビュー済みの編集に対して `python tools/validate_package.py --refresh-manifest` を実行し、最後に `python tools/validate_package.py` で不変性を確認する。','','## Open Questions — 仕様・検証の完成条件','','[OQ-R6-17-01](chapters/17_Verification.md#oq-r6-17-01)：実構成・閾値・受入条件と評価責任者を確定する。[OQ-R6-04-01](chapters/04_Configurations_Profiles.md#oq-r6-04-01)：既存全機能と採用範囲を確認する。[OQ-R6-01-01](chapters/01_Scope_Baseline.md#oq-r6-01-01)：4種類の名前以外の権限・委譲等を確定する。']
  (ROOT/'DOCUMENT_QA.md').write_text('\n'.join(report)+'\n',encoding='utf-8')
  # Recheck counts after writing the actual report. Its fixed outgoing links do not vary.
  result=check()
  if result['errors']:raise ValueError(result['errors'])
  (ROOT/'data/r7_document_validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
  for i,line in enumerate(report):
   for key,val in result['checks'].items():
    if line.startswith(f'| {key} |'):report[i]=f'| {key} | {val} |'
  (ROOT/'DOCUMENT_QA.md').write_text('\n'.join(report)+'\n',encoding='utf-8')
  manifest='\n'.join(sha(p.read_bytes())+'  '+p.relative_to(ROOT).as_posix() for p in allfiles())+'\n'
  (ROOT/'MANIFEST_SHA256.txt').write_text(manifest,encoding='utf-8')
 else:
  mp=ROOT/'MANIFEST_SHA256.txt'
  entries={}
  for line in mp.read_text(encoding='utf-8').splitlines():
   h,rel=line.split('  ',1);entries[rel]=h
  actual={p.relative_to(ROOT).as_posix():sha(p.read_bytes()) for p in allfiles()}
  if entries!=actual:
   diff=sorted(k for k in set(entries)|set(actual) if entries.get(k)!=actual.get(k));raise SystemExit('Manifest mismatch: '+', '.join(diff[:15]))
  result['manifest_verified_files']=len(actual)
 print(json.dumps(result,ensure_ascii=False,indent=2))

if __name__=='__main__':
 try:main()
 except (OSError,ValueError,KeyError,json.JSONDecodeError) as exc:raise SystemExit(f'Validation failed: {exc}')
