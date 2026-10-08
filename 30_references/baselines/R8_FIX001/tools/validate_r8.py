#!/usr/bin/env python3
"""R8文書の構造・相互参照・IDを検査する。--baseline-checkは継承不変性も確認。実機試験ではない。"""
from __future__ import annotations
import argparse, collections, hashlib, json, re, sys
from pathlib import Path
from urllib.parse import unquote
ROOT=Path(__file__).resolve().parents[1]
LINK=re.compile(r'!?\[[^\]\n]*\]\(([^\s\)]+)(?:\s+"[^"]*")?\)')
EXPLICIT=re.compile(r'<a\s+(?:name|id)=["\']([^"\']+)["\'][^>]*>',re.I)

def load(n):return json.loads((ROOT/n).read_text(encoding='utf-8'))
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def outside_fences(t):
 out=[];inside=False
 for line in t.splitlines():
  if re.match(r'^\s*(```|~~~)',line):inside=not inside;continue
  if not inside:out.append(line)
 return '\n'.join(out),inside

def anchors(t):
 s,_=outside_fences(t);a=set(EXPLICIT.findall(s));seen=collections.Counter()
 for line in s.splitlines():
  m=re.match(r'^#{1,6}\s+(.+?)\s*#*$',line)
  if not m:continue
  v=re.sub(r'!?\[([^]]+)\]\([^)]*\)',r'\1',m[1]);v=re.sub(r'<[^>]+>','',v)
  slug=re.sub(r'[^\w\-\s]','',v.lower());slug=re.sub(r'\s','-',slug)
  k=seen[slug];seen[slug]+=1;a.add(slug+('-'+str(k) if k else ''))
 return a

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--baseline-check',action='store_true');args=ap.parse_args()
 errors=[];checks={};warn=[]
 def check(label,ok,details=None):
  checks[label]={'pass':bool(ok),'details':details}
  if not ok:errors.append({'check':label,'details':details})
 idx=load('data/document_index.json');chs=idx['chapters'];notes=[ROOT/c['path'] for c in chs]
 expected=[8,11,10,8,7];check('five_parts_44_chapters',len(chs)==44 and [len(p['chapters']) for p in idx['parts']]==expected,{'parts':5,'chapters':len(chs),'part_counts':[len(p['chapters']) for p in idx['parts']]})
 check('chapter_paths_exist',all(p.is_file() for p in notes))
 check('no_active_old_parts_or_27_chapter_layout',not (ROOT/'parts').exists() and not list((ROOT/'chapters').glob('*.md')))
 moc=(ROOT/idx['moc']).read_text(encoding='utf-8');check('single_moc_has_all_chapters',all('('+c['path']+')' in moc for c in chs) and len(list(ROOT.glob('*MOC*.md')))==1)
 active=sorted(p for p in ROOT.rglob('*.md') if 'sources' not in p.relative_to(ROOT).parts)
 cache={};local_count=0;external_count=0;link_errors=[];anchor_errors=[];footers=[];fences=[]
 for p in active:
  text=p.read_text(encoding='utf-8');s,unclosed=outside_fences(text)
  if unclosed:fences.append(str(p.relative_to(ROOT)))
  a=EXPLICIT.findall(s);dupes=[x for x,n in collections.Counter(a).items() if n>1]
  if dupes:anchor_errors.append({'file':str(p.relative_to(ROOT)),'anchors':dupes})
  h=list(re.finditer(r'^##\s+(.+)$',s,re.M))
  if not h or not h[-1][1].startswith('Open Questions'):footers.append(str(p.relative_to(ROOT)))
  elif not re.search(r'OQ-R6-|Open_Question_Register\.md',s[h[-1].end():]):footers.append(str(p.relative_to(ROOT)))
  for m in LINK.finditer(s):
   u=unquote(m[1])
   if re.match(r'^[a-zA-Z][\w+.-]*:',u) or u.startswith('//'):external_count+=1;continue
   local_count+=1;v,_,a=u.partition('#');t=(p.parent/v).resolve() if v else p.resolve()
   if not t.exists():link_errors.append({'file':str(p.relative_to(ROOT)),'href':m[1],'error':'MISSING_FILE'});continue
   if a and t.suffix.lower()=='.md':
    if t not in cache:cache[t]=anchors(t.read_text(encoding='utf-8'))
    if a not in cache[t]:link_errors.append({'file':str(p.relative_to(ROOT)),'href':m[1],'error':'MISSING_ANCHOR'})
 check('markdown_links',not link_errors,{'checked_local':local_count,'external_not_fetched':external_count,'errors':link_errors})
 check('unique_explicit_anchors',not anchor_errors,anchor_errors)
 check('all_current_md_end_with_open_questions',not footers,{'files':len(active),'errors':footers})
 check('balanced_fences',not fences,fences)
 # JSON grammar, IDs, and current ownership.
 invalid=[]
 for p in (ROOT/'data').glob('*.json'):
  try:json.loads(p.read_text(encoding='utf-8'))
  except (ValueError,UnicodeError) as e:invalid.append({'file':p.name,'error':str(e)})
 check('json_syntax',not invalid,invalid)
 qs=load('data/completion_items.json')['items'];qb=load('data/open_question_bindings.json')['questions'];qm={q['question_id']:q for q in qs}
 body='\n'.join(p.read_text(encoding='utf-8') for p in notes)
 oqheaders=re.findall(r'^### (OQ-R6-\d\d-\d\d)\s',body,re.M)
 slotanchors=re.findall(r'<a id="(slot-r6-\d\d-\d\d)"></a>',body)
 check('85_unique_oq_owners',len(qb)==len(qs)==len(qm)==len(oqheaders)==len(set(oqheaders))==85)
 check('85_unique_completion_slots',len(slotanchors)==len(set(slotanchors))==85)
 check('question_owner_and_slot_links',all(b['anchor'] in anchors((ROOT/b['owner_note']).read_text()) and b['slot_anchor'] in anchors((ROOT/b['owner_note']).read_text()) and qm[b['id']]['note']==b['owner_note'] for b in qb))
 units=load('data/section_migration.json')['units'];check('259_source_sections_mapped_once',len(units)==259 and len({(u['source'],u['key']) for u in units})==259 and all(body.count('<a id="'+u['anchor']+'"></a>')==1 and u['anchor'] in anchors((ROOT/u['target_path']).read_text()) for u in units),{'source_sections':len(units)})
 fc=load('data/function_catalog.json');ss={f['id']:f for f in fc['system_functions']};gg={f['id']:f for f in fc['gw_functions']};req=load('data/requirements.json')['requirements'];rr={r['id']:r for r in req}
 check('function_catalog_21_and_32',len(ss)==21 and len(gg)==32 and all(f['id'].lower() in body for f in fc['system_functions']+fc['gw_functions']))
 pairs1={(s['id'],g) for s in ss.values() for g in s['gw_function_ids']};pairs2={(s,g['id']) for g in gg.values() for s in g['parent_system_function_ids']}
 check('bidirectional_function_allocation',pairs1==pairs2,{'pairs':len(pairs1),'mismatch':sorted(pairs1^pairs2)})
 check('function_requirement_question_refs',all(set(f['requirement_ids'])<=set(rr) and set(f['open_question_ids'])<=set(qm) and all((ROOT/n).is_file() for n in f['source_notes']) for f in list(ss.values())+list(gg.values())))
 check('requirement_owners_124',len(rr)==124 and all((ROOT/r['primary_note']).is_file() for r in req))
 tests=load('data/test_catalog.json')['tests'];tt={t['id']:t for t in tests}
 check('69_test_refs',len(tt)==69 and all(set(r.get('verification_ids',[]))<=set(tt) for r in req) and all(set(t.get('system_requirement_ids',[]))<=set(rr) for t in tests))
 check('50_parameters_48_issues_16_interfaces',len(load('data/parameters.json')['parameters'])==50 and len(load('data/open_issues.json')['issues'])==48 and len(load('data/external_interfaces.json')['interfaces'])==16)
 cov=load('data/coverage_completion_map.json')['coverage'];check('34_review_dimensions',len(cov)==34 and all(set(x['question_ids'])<=set(qm) for x in cov))
 roles=load('data/role_access_r7.json');cfg=load('data/configuration_patterns_r7.json')
 check('4_named_roles', [r['name'] for r in roles['human_roles']]==['ユーザ','メンテナンス','メーカー','開発者'])
 check('3_inherited_config_patterns', {p['id'] for p in cfg['patterns']}=={'CFG-RS','CFG-EL','CFG-MIX'})
 routes=load('data/grid_network_routes.json')['routes'];check('router_and_fetcher_contract',len(routes)==2 and all('HOME_ROUTER' in p['request_path'] and 'HOME_ROUTER' in p['response_path'] for p in routes) and next(p for p in routes if p['mode']=='PCS_DIRECT')['fetcher']=='PCS_GRID_CLIENT' and next(p for p in routes if p['mode']=='PCS_DIRECT')['gw_in_fetch_path'] is False)
 manifest=load('data/input_manifest.json');snapshot=ROOT/'sources/r7_snapshot';bad=[x['path'] for x in manifest['archived_nonzip_files'] if not (snapshot/x['path']).is_file() or digest(snapshot/x['path'])!=x['sha256']]
 check('175_archived_inputs_unchanged',len(manifest['archived_nonzip_files'])==175 and not bad,bad)
 diagrams=[p for p in (ROOT/'diagrams').iterdir() if p.suffix in ('.mmd','.svg','.png')];check('6_diagram_assets_unchanged',len(diagrams)==6 and all(digest(p)==digest(snapshot/'diagrams'/p.name) for p in diagrams))
 if args.baseline_check:
  old=json.loads((snapshot/'data/requirements.json').read_text())['requirements'];om={r['id']:r for r in old};nav={'chapter','legacy_chapter','primary_note','related_current_notes'}
  dif=[r['id'] for r in req if {k:v for k,v in r.items() if k not in nav}!={k:v for k,v in om[r['id']].items() if k not in nav}]
  check('requirement_semantics_unchanged',not dif,dif)
  oldfc=json.loads((snapshot/'data/function_catalog_r7.json').read_text());nf={'source_notes','legacy_source_notes'}
  dif=[]
  for key in ['system_functions','gw_functions']:
   omf={x['id']:x for x in oldfc[key]}
   for f in fc[key]:
    if {k:v for k,v in f.items() if k not in nf}!={k:v for k,v in omf[f['id']].items() if k not in nf}:dif.append(f['id'])
  check('function_semantics_unchanged',not dif,dif)
  unchanged=['test_catalog.json','parameters.json','open_issues.json','external_interfaces.json','role_access_r7.json','configuration_patterns_r7.json','grid_network_routes.json','grid_connection_profiles.json','echonet_normal_routes.json']
  check('9_baseline_data_files_byte_identical',all(digest(ROOT/'data'/n)==digest(snapshot/'data'/n) for n in unchanged),unchanged)
  check('no_fabricated_test_or_permission_approval',all(t['status']=='NOT_RUN' for t in tests) and all(v is None for p in roles['permissions'] for v in p['approved_permissions'].values()) and all(q['status']=='OPEN' and q['answer'] is None for q in qs))
 # Keep reported scope honest.
 warn=['文書構造・ID・参照・継承データの検査であり、技術仕様の完全性・実装・実機・セキュリティ・JET判断を検証しない。','外部URLは再取得していない。sources配下は保存ハッシュのみ検査し、歴史的リンクの修復はしない。','既存図6資産の不変性を検査した。Mermaid再描画・ネットワーク実測は未実施。']
 report={'revision':'R8','result':'PASS' if not errors else 'FAIL','baseline_check':args.baseline_check,'current_markdown_files':len(active),'local_links':local_count,'checks':checks,'warnings':warn,'errors':errors}
 (ROOT/'data/document_validation_r8.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({'result':report['result'],'checks':len(checks),'current_markdown_files':len(active),'local_links':local_count,'errors':errors},ensure_ascii=False,indent=2))
 return 0 if not errors else 1
if __name__=='__main__':
 try:sys.exit(main())
 except (OSError,ValueError,KeyError) as e:print(f'ERROR: {e}',file=sys.stderr);sys.exit(2)
