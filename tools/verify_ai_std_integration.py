#!/usr/bin/env python3
"""Read-only R13 selective-integration audit, not enforcement of all normative rules.
Validates source bytes, selected spans, current target anchors, preserved base records,
version transitions and item/document trace bindings. No IDE, network or code execution.
"""
from __future__ import annotations
import argparse,hashlib,json,re,sys,zipfile
from pathlib import Path,PurePosixPath
from common import FlowError,inside
ROOT=Path(__file__).resolve().parents[1]
AREA=Path('20_work/analysis/project/ai_std_integration')
class IntegrationError(FlowError): pass

def digest(p:Path)->str:return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p:Path):
 def pairs(seq):
  out={}
  for k,v in seq:
   if k in out:raise IntegrationError('DUPLICATE_JSON_KEY: '+k)
   out[k]=v
  return out
 return json.loads(p.read_text(encoding='utf-8-sig'),object_pairs_hook=pairs)

def demand(test,code,detail=''):
 if not test:raise IntegrationError(code+(': '+str(detail)if detail else ''))
def validate(root:Path=ROOT)->dict:
 root=root.resolve();i=load(root/AREA/'integration.json');p=load(root/'00_governance/R13_Input_Provenance.json');f=load(root/AREA/'source_fragments.json');g=load(root/'20_work/analysis/project/trace_graph.json');m=load(root/AREA/'trace_adoption_map.json');checks=[]
 demand(i['revision']=='R13','WRONG_INTEGRATION_REVISION')
 demand(i['product_requirements_approved']is False and i['external_claims_reverified']is False,'SCOPE_OVERCLAIM')
 zpath=inside(root,i['source_zip_path']);demand(zpath.is_file()and digest(zpath)==i['source_zip_sha256']==p['input_zip_sha256'],'SOURCE_ZIP_CHANGED')
 inv={x['source_file']:x for x in i['source_inventory']};demand(len(inv)==len(i['source_inventory'])==37,'SOURCE_INVENTORY')
 with zipfile.ZipFile(zpath)as z:
  demand(z.testzip()is None,'SOURCE_CRC')
  entries={}
  for entry in z.infolist():
   if entry.is_dir():continue
   pp=PurePosixPath(entry.filename);demand(not pp.is_absolute()and '..'not in pp.parts and '\\'not in entry.filename,'SOURCE_UNSAFE_PATH')
   rel='/'.join(pp.parts[1:]);demand(rel not in entries,'SOURCE_DUPLICATE_MEMBER');entries[rel]=z.read(entry)
  demand(set(entries)==set(inv),'SOURCE_MEMBERS')
  for rel,x in inv.items():
   q=inside(root,x['path']);demand(q.is_file()and q.read_bytes()==entries[rel]and digest(q)==x['sha256'],'SOURCE_BYTES',rel)
   demand(x['disposition']in ['REFERENCE_ONLY','PARTIAL_ADAPTATION','ADAPTED_OPTIONAL_ENTRY','ADAPTED_TEMPLATE_FIELDS','ADAPTED_INDEX','ADAPTED_NAVIGATION'],'UNKNOWN_DISPOSITION',rel)
   demand(bool(x['reason'].strip()),'EMPTY_DISPOSITION_REASON',rel)
   for t in x['destinations']:demand(inside(root,t).is_file(),'TARGET_MISSING',t)
  manifest=entries['MANIFEST_SHA256.txt'].decode().splitlines();seen=set()
  for line in manifest:
   h,sep,n=line.partition('  ');demand(sep and n in entries and n not in seen and hashlib.sha256(entries[n]).hexdigest()==h,'SOURCE_MANIFEST',line);seen.add(n)
  demand(seen==set(entries)-{'MANIFEST_SHA256.txt'},'SOURCE_MANIFEST_INVENTORY')
 checks.append('source package, 37 original files, 36 original manifest entries, per-file dispositions')
 for path,h in p['protected_files'].items():
  q=inside(root,path);demand(q.is_file()and digest(q)==h,'BASE_PROTECTED_CHANGED',path)
 checks.append('selected product baseline, tasks, control, prior references, tools and schemas unchanged')
 previous={}
 for rel,s in p['previous_registry_snapshots'].items():
  q=inside(root,s['path']);demand(q.is_file()and digest(q)==s['sha256']==p['base_file_hashes'][rel],'BASE_REGISTRY_SNAPSHOT',rel);previous[rel]=load(q)
 oldg=previous['20_work/analysis/project/trace_graph.json'];oldsrc=previous['30_references/source_register.json'];news=load(root/'30_references/source_register.json');sd={x['source_id']:x for x in news['sources']}
 for x in oldsrc['sources']:demand(sd.get(x['source_id'])==x,'PRIOR_SOURCE_ROW_CHANGED',x['source_id'])
 for x in inv.values():demand(sd.get(x['source_id'],{}).get('sha256')==x['sha256']and sd[x['source_id']]['path']==x['path'],'SOURCE_REGISTER_BINDING',x['source_id'])
 oldnodes={n['node_id']:n for n in oldg['nodes']};nodes={n['node_id']:n for n in g['nodes']};edges={e['edge_id']:e for e in g['edges']}
 for k,n in oldnodes.items():demand(nodes.get(k)==n,'OLD_ITEM_CHANGED',k)
 for e in oldg['edges']:demand(edges.get(e['edge_id'])==e,'OLD_ITEM_EDGE_CHANGED',e['edge_id'])
 demand(g['profiles']==oldg['profiles'] and g['trace_relations']==oldg['trace_relations'],'OLD_TRACE_PROFILE_CHANGED')
 checks.append('previous registries stored; existing 341 items and 741 edges preserved exactly')
 docs={d['document_version_id']:d for d in g['documents']};changes={x['old_version_id']:x for x in p['old_document_versions']}
 for old in oldg['documents']:
  new=docs.get(old['document_version_id']);demand(new is not None,'OLD_DOCUMENT_MISSING',old['document_version_id'])
  if old['document_version_id']in changes:
   c=changes[old['document_version_id']];q=inside(root,c['old_path']);demand(q.is_file()and digest(q)==old['sha256']==c['old_sha256'],'OLD_DOCUMENT_BYTES',q)
   expected=dict(old,path=c['old_path'],representation='IMMUTABLE_REFERENCE');demand(new==expected,'OLD_DOCUMENT_METADATA',old['document_version_id'])
   nd=docs.get(c['new_version_id']);demand(nd and nd['document_trace_id']==old['document_trace_id']and nd['sha256']==c['new_sha256']==digest(inside(root,c['path'])),'NEW_DOCUMENT_BINDING',c['path'])
  else:demand(new==old,'UNCHANGED_DOCUMENT_METADATA',old['document_version_id'])
 checks.append('DTR revisions retained; changed current documents have separate immutable R12 versions')
 fr={x['id']:x for x in f['fragments']};rules={x['id']:x for x in i['rules']};maps={x['rule_id']:x for x in m['rule_links']}
 demand(len(rules)==len(i['rules'])==26 and len(fr)==26 and set(maps)==set(rules),'RULE_INVENTORY')
 items={n['item_trace_id']:n for n in g['nodes']if n['selected']}
 for rid,x in rules.items():
  demand(x['normative_status']=='DRAFT_FOR_REVIEW','RULE_STATUS',rid)
  q=inside(root,x['destination']);text=q.read_text();demand(f'id="{x["anchor"]}"'in text,'RULE_ANCHOR',rid)
  frag=fr.get(x['fragment_id']);demand(frag and frag['rule_id']==rid and frag['segments'],'RULE_FRAGMENT',rid)
  for s in frag['segments']:
   src=inside(root,s['source_path']);demand(src.is_file()and digest(src)==s['source_sha256'],'FRAGMENT_SOURCE',rid)
   lines=src.read_text().splitlines();a,b=s['start_line'],s['end_line'];demand(isinstance(a,int)and isinstance(b,int)and 1<=a<=b<=len(lines),'FRAGMENT_RANGE',rid)
   quote='\n'.join(lines[a-1:b]);demand(quote==s['quote']and hashlib.sha256(quote.encode()).hexdigest()==s['quote_sha256'],'FRAGMENT_QUOTE',rid)
   demand(s['document_version_id']in docs and docs[s['document_version_id']]['path']==s['source_path'],'FRAGMENT_DTR',rid)
  mp=maps[rid];n=items.get(mp['rule_item']);sn=items.get(mp['source_item']);demand(n and sn and rid in n['native_ids']and frag['id']in sn['native_ids'],'RULE_ITR',rid)
  demand(n['document_version_id']==mp['document_version_id']and n['locator']['path']==x['destination'],'RULE_LOCATION',rid)
  demand(any(e['from_node']==n['node_id']and e['to_node']==sn['node_id']and e['relation']=='cites'and e['review']is None for e in g['edges']),'RULE_CITATION',rid)
 checks.append('26 adapted rule anchors, exact source spans and item-level cites with no inferred approval')
 for target in i['optional_entry_files']:
  text=inside(root,target).read_text();demand('20_work/drafts'not in target and target.startswith('.github/'),'ENTRY_PATH')
  # Old names may occur in warnings, but paths/new FSM declarations must not be imported as active settings.
  demand('work/tickets'not in text and 'baseline_weight'not in text and not re.search(r'--phase\s+P\d\d',text),'ENTRY_LEGACY_AUTHORITY',target)
 demand(len(i['optional_entry_files'])==6,'ENTRY_COUNT')
 checks.append('six optional entry files use current paths and codes, not old path/weight/ordinal authority')
 return dict(result='PASS',scope='DOCUMENT_SELECTION_AND_PRESERVATION_ONLY',checks=checks,counts={'source_files':len(inv),'rule_groups':len(rules),'source_fragments':len(fr),'prior_items':len(oldnodes),'items':len(g['nodes']),'document_versions':len(docs),'logical_documents':len({d['document_trace_id']for d in docs.values()}),'old_document_versions_preserved':len(changes),'protected_files':len(p['protected_files'])},limits=['No actual IDE/Copilot loading tested','No production C/Yocto build or hardware test','No supplier acceptance, actual budget, security or certification approval','Reference citations do not prove complete semantic equivalence'])
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,default=ROOT);args=ap.parse_args()
 try: print(json.dumps(validate(args.root),ensure_ascii=False,indent=2))
 except (FlowError,OSError,ValueError,KeyError,TypeError,zipfile.BadZipFile)as e:
  print(json.dumps({'result':'FAIL','error':str(e)},ensure_ascii=False,indent=2));sys.exit(1)
