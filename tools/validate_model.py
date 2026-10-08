"""Incremental validation; no fixed requirement/function/OQ counts. Read-only."""
from __future__ import annotations
import collections, contextlib, io, json, os, re, shutil, tempfile
from pathlib import Path
from urllib.parse import unquote
from common import FlowError,jread,schema_check,sha_file,record_hash,inside,toolchain_hash
SCHEMAS=['requirements','test_catalog','function_catalog','completion_items','document_index','open_question_bindings','parameters','external_interfaces','open_issues','usdm','trace_links','import_provenance']
GENERATED=['data/completion_items.json','data/note_question_bindings.json','data/view_generation.json','data/source_bindings.json','appendices/Requirements_Catalog.md','appendices/Open_Question_Register.md','appendices/Test_Profiles.md','appendices/Traceability.md','appendices/Functional_Allocation.md','appendices/Source_Register.md','appendices/Import_Merge_Decisions.md','appendices/USDM_Traceability.md','90_All_In_One.md']
LINK=re.compile(r'!?\[[^\]\n]*\]\(([^\s\)]+)(?:\s+"[^"]*")?\)')
EXPLICIT=re.compile(r'<a\s+(?:name|id)=["\']([^"\']+)["\'][^>]*>',re.I)

def outside_fences(text):
    out=[];fence=None
    for line in text.splitlines():
        m=re.match(r'^\s*(`{3,}|~{3,})',line)
        if m:
            if fence is None:fence=m[1][0]
            elif m[1][0]==fence:fence=None
            continue
        if fence is None:out.append(line)
    return '\n'.join(out),fence is not None

def anchors(text):
    s,_=outside_fences(text);a=set(EXPLICIT.findall(s));seen=collections.Counter()
    for line in s.splitlines():
        m=re.match(r'^#{1,6}\s+(.+?)\s*#*$',line)
        if not m:continue
        v=re.sub(r'!?\[([^]]+)\]\([^)]*\)',r'\1',m[1]);v=re.sub(r'<[^>]+>','',v)
        slug=re.sub(r'[^\w\-\s]','',v.lower());slug=re.sub(r'\s','-',slug)
        k=seen[slug];seen[slug]+=1;a.add(slug+('-'+str(k) if k else ''))
    return a

def unique(rows,key,label):
    ids=[r[key] for r in rows];bad=[v for v,c in collections.Counter(ids).items() if c>1]
    if bad:raise FlowError(label+' duplicate IDs: '+', '.join(bad))
    return {r[key]:r for r in rows}

def projection_paths(root):
    idx=jread(root/'data/document_index.json');cs={c['code']:c for c in idx['chapters']}
    return GENERATED+[cs['I-03']['path'],cs['II-02']['path']]

def sources(workspace):
    v=jread(workspace/'30_references/source_register.json');schema_check(workspace,'source_register',v)
    sm=unique(v['sources'],'source_id','sources')
    for s in sm.values():
        p=inside(workspace,s['path'])
        if not p.is_relative_to((workspace/'30_references').resolve()):raise FlowError('Original outside 30_references: '+s['path'])
        if not p.is_file() or p.stat().st_size!=s['bytes'] or sha_file(p)!=s['sha256']:raise FlowError('Original modified/missing: '+s['source_id'])
    alias_file=workspace/'00_governance/baseline_source_aliases.json'
    if alias_file.exists():
        for sid,e in jread(alias_file)['aliases'].items():
            if sid not in sm or sm[sid]['path']!=e['path'] or sm[sid]['sha256']!=e['sha256']:raise FlowError('Legacy source alias was rebound: '+sid)
    return sm

def validate(root:Path,workspace:Path,*,freshness=True,links=True,reference_integrity=True):
    root=root.resolve();workspace=workspace.resolve();checks=[];warnings=[]
    data={}
    for name in SCHEMAS:
        d=jread(root/'data'/f'{name}.json');schema_check(workspace,name,d);data[name]=d
    checks.append('JSON schema/type/nonempty/enum')
    sm=sources(workspace) if reference_integrity else {s['source_id']:s for s in jread(workspace/'30_references/source_register.json')['sources']}
    rs=unique(data['requirements']['requirements'],'id','SYS');ts=unique(data['test_catalog']['tests'],'id','tests');qs=unique(data['completion_items']['items'],'question_id','OQ')
    unique(data['completion_items']['items'],'id','SLOT')
    fc=data['function_catalog'];ss=unique(fc['system_functions'],'id','system functions');gs=unique(fc['gw_functions'],'id','GW functions')
    for nm,key in [('parameters','parameters'),('external_interfaces','interfaces'),('open_issues','issues')]:unique(data[nm][key],'id',nm)
    idx=data['document_index'];cs=unique(idx['chapters'],'code','chapters');unique(idx['parts'],'id','parts')
    partlinks=[(p['id'],c) for p in idx['parts'] for c in p['chapters']]
    if len(partlinks)!=len(cs) or set(partlinks)!={(c['part'],c['code']) for c in cs.values()}:raise FlowError('Part/chapter allocation mismatch')
    for c in cs.values():
        if not inside(root,c['path']).is_file():raise FlowError('Missing chapter: '+c['code'])
    for p in idx['appendices']:
        if not inside(root,p).is_file():raise FlowError('Missing appendix: '+p)
    checks.append('IDs and dynamic chapter allocation')
    us=unique(data['usdm']['elements'],'id','USDM');links_by_id=unique(data['trace_links']['links'],'id','trace')
    pm=data['import_provenance'];fr=unique(pm['fragments'],'fragment_id','fragments');ca=unique(pm['candidates'],'candidate_id','candidates');de=unique(pm['decisions'],'decision_id','decisions')
    unique(pm['bindings'],'target_id','effective provenance bindings')
    for r in rs.values():
        if r['chapter'] not in cs or r['primary_note']!=cs[r['chapter']]['path']:raise FlowError('Requirement owner mismatch: '+r['id'])
        for n in r['related_current_notes']:
            if not inside(root,n).is_file():raise FlowError('Missing related note: '+n)
        if not set(r['source_ids'])<=set(sm):raise FlowError('Unknown source ID: '+r['id'])
        if not set(r['verification_ids'])<=set(ts):raise FlowError('Unknown test: '+r['id'])
        if r['usdm_id'] is not None and r['usdm_id'] not in us:raise FlowError('Unknown USDM reference: '+r['id'])
        if r['status']=='APPROVED' and (not r.get('approved_by') or not r.get('approval_record')):raise FlowError('APPROVED requires actor and evidence: '+r['id'])
    for t in ts.values():
        if t['source_id'] not in sm or not set(t['system_requirement_ids'])<=set(rs):raise FlowError('Invalid test source/requirement: '+t['id'])
        if t['status']=='PASS' and (not t.get('evidence') or 'TBD' in t['acceptance_profile']):raise FlowError('PASS requires test evidence and acceptance profile: '+t['id'])
    rp={(r['id'],tid) for r in rs.values() for tid in r['verification_ids']};tp={(rid,t['id'])for t in ts.values()for rid in t['system_requirement_ids']}
    if rp!=tp:raise FlowError('Requirement/test reverse links mismatch: '+str(sorted(rp^tp)[:10]))
    if {(s['id'],g) for s in ss.values() for g in s['gw_function_ids']}!={(s,g['id'])for g in gs.values()for s in g['parent_system_function_ids']}:raise FlowError('Bidirectional function links mismatch')
    for f in list(ss.values())+list(gs.values()):
        if not set(f['requirement_ids'])<=set(rs) or not set(f['open_question_ids'])<=set(qs) or not set(f['formal_usdm_ids'])<=set(us):raise FlowError('Function refs invalid: '+f['id'])
        for n in f['source_notes']:
            if not inside(root,n).is_file():raise FlowError('Function note missing: '+n)
    checks.append('source/USDM/test/function references and bidirectionality')
    # The Markdown question is authoritative; the JSON index is verified through regeneration below.
    qb=unique(data['open_question_bindings']['questions'],'id','OQ bindings')
    if set(qb)!=set(qs):raise FlowError('OQ binding set differs from items')
    oqall=[]
    for c in cs.values():oqall+=re.findall(r'^###\s+(OQ-[A-Za-z0-9_-]+)\s',inside(root,c['path']).read_text(),re.M)
    if set(oqall)!=set(qs) or len(oqall)!=len(qs):raise FlowError('Each OQ must have exactly one authored owner')
    from view_renderer import split_oq,field,nullish
    for qid,b in qb.items():
        text=inside(root,b['owner_note']).read_text();a=anchors(text)
        if b['anchor'] not in a or b['slot_anchor'] not in a or qs[qid]['note']!=b['owner_note']:raise FlowError('OQ owner/slot invalid: '+qid)
        body=split_oq(text,qid);m=re.search(r'状態：\*\*([^*]+)\*\*',body)
        if not m:raise FlowError('Missing OQ state: '+qid)
        if m[1] not in ['OPEN','IN_REVIEW','ANSWERED','RESOLVED','CLOSED','DEFERRED','NOT_APPLICABLE']:raise FlowError('Invalid OQ state: '+qid)
        if m[1] in ['RESOLVED','CLOSED','NOT_APPLICABLE'] and (not nullish(field(body,'回答')) or not nullish(field(body,'決定記録'))):raise FlowError('OQ closure missing answer/evidence: '+qid)
    checks.append('generic OQ ownership and closure')
    for f in fr.values():
        if f['source_id'] not in sm or sm[f['source_id']]['sha256']!=f['source_sha256']:raise FlowError('Fragment source mismatch: '+f['fragment_id'])
        expected_fid='FRAG-'+record_hash({'source_id':f['source_id'],'sha':f['source_sha256'],'locator':f['locator'],'text':f['raw_text'],'extractor_sha256':f.get('context',{}).get('extraction',{}).get('extractor_sha256')})[:24]
        if f['fragment_id']!=expected_fid:raise FlowError('Fragment raw text/locator integrity mismatch: '+f['fragment_id'])
    for c in ca.values():
        if not set(c['fragment_ids'])<=set(fr):raise FlowError('Candidate fragment missing: '+c['candidate_id'])
    for d in de.values():
        if d['candidate_id'] not in ca:raise FlowError('Decision candidate missing: '+d['decision_id'])
        if d['action'] in ['ADOPT','EQUIVALENT']:
            c=ca[d['candidate_id']]
            if d['unresolved_conflict'] or c['classification'] in ['UNCLASSIFIED','INSUFFICIENT'] or (c['classification']=='CONFLICT' and not c['resolution_note']):raise FlowError('Unresolved candidate cannot be adopted: '+c['candidate_id'])
    for b in pm['bindings']:
        target=(rs if b['target_kind']=='SYS' else us).get(b['target_id'])
        if target is None or record_hash(target)!=b['record_sha256']:raise FlowError('Adopted record differs from reviewed record: '+b['target_id'])
        if b['decision_id'] not in de or de[b['decision_id']]['action'] not in ['ADOPT','EQUIVALENT']:raise FlowError('Binding has no adopting decision: '+b['target_id'])
        c=ca[de[b['decision_id']]['candidate_id']]
        if b['target_id'] not in c['target_ids'] or b['target_kind']!=c['target_kind'] or not set(b['fragment_ids'])<=set(c['fragment_ids']):raise FlowError('Binding/candidate scope mismatch')
        for fid in b['fragment_ids']:
            f=fr.get(fid)
            if not f or not f['verified_by'] or not f['review_note'] or f['extraction_status']=='BLOCKED':raise FlowError('Adoption requires verified source fragment: '+fid)
            if b['target_kind']=='SYS' and f['source_id'] not in target['source_ids']:raise FlowError('SYS/source fragment linkage missing')
    checks.append('import provenance and explicit merge decisions')
    # Hierarchy and rationale are not inferred by tools.
    for e in us.values():
        if not set(e['parent_ids'])<=set(us) or e['id'] in e['parent_ids']:raise FlowError('USDM parent invalid: '+e['id'])
        if not set(e['source_fragment_ids'])<=set(fr) or not set(e['reason']['fragment_ids'])<=set(fr):raise FlowError('USDM evidence fragment missing: '+e['id'])
        if e['status']=='APPROVED':
            if not e['approved_by'] or not e['approval_record']:raise FlowError('USDM approval evidence missing')
            if e['kind']=='REQUIREMENT' and (e['reason']['state'] not in ['ORIGINAL','HUMAN_CONFIRMED'] or not e['reason']['text']):raise FlowError('Unknown/hypothesized rationale cannot be approved')
            if e['reason']['state']=='ORIGINAL' and not e['reason']['fragment_ids']:raise FlowError('Original rationale requires source fragment')
            if e['reason']['state']=='HUMAN_CONFIRMED' and not e['reason']['confirmed_by']:raise FlowError('Human rationale confirmer missing')
        if e['reason']['state']=='UNKNOWN' and e['reason']['text'] is not None:raise FlowError('UNKNOWN reason text must remain null')
    def visit(k,stack,done):
        if k in stack:raise FlowError('USDM hierarchy cycle: '+k)
        if k in done:return
        for p in us[k]['parent_ids']:visit(p,stack|{k},done)
        done.add(k)
    done=set()
    for k in us:visit(k,set(),done)
    sets={'SYS':set(rs),'USDM':set(us),'FUNCTION':set(ss)|set(gs),'TEST':set(ts),'FRAGMENT':set(fr),'OQ':set(qs),'SOURCE':set(sm)}
    allowed={'VERIFIED_BY':({'SYS','USDM'},{'TEST'}),'ALLOCATED_TO':({'SYS','USDM','FUNCTION'},{'SYS','FUNCTION'}),'SATISFIES':({'SYS','USDM'},{'USDM'}),'DERIVED_FROM':({'SYS','USDM','FUNCTION'},{'SOURCE','FRAGMENT','SYS','USDM'}),'REFINES':({'SYS','USDM'},{'SYS','USDM'}),'SUPERSEDES':({'SYS','USDM','FRAGMENT'},{'SYS','USDM','FRAGMENT'})}
    for l in links_by_id.values():
        for end in ['from','to']:
            if l[end]['id'] not in sets[l[end]['kind']]:raise FlowError('Unknown typed trace endpoint: '+l['id'])
        a,b=allowed[l['relation']]
        if l['from']['kind'] not in a or l['to']['kind'] not in b:raise FlowError('Trace relationship type invalid: '+l['id'])
        if l['relation']=='SATISFIES':
            if us[l['to']['id']]['kind']!='REQUIREMENT':raise FlowError('SATISFIES must target a USDM requirement')
            if l['from']['kind']=='USDM' and us[l['from']['id']]['kind']!='SPECIFICATION':raise FlowError('USDM SATISFIES must start at a specification')
        if l['state']=='REVIEWED' and not l['reviewed_by']:raise FlowError('Trace reviewer missing')
    checks.append('USDM rationale, hierarchy, typed multi-to-multi links')
    # The navigation entry must not silently select a historical integrated view.
    moc=(root/'00_MOC.md').read_text()
    integrated=re.search(r'\[統合閲覧版\]\(([^)]+)\)',moc)
    if not integrated or (root/integrated[1]).resolve() != (root/'90_All_In_One.md').resolve():raise FlowError('MOC integrated view must belong to the same snapshot')
    local_count=0
    if links:
        cache={};bad=[]
        for p in root.rglob('*.md'):
            text=p.read_text();s,unclosed=outside_fences(text)
            if unclosed:raise FlowError('Unclosed Markdown fence: '+str(p.relative_to(root)))
            dup=[x for x,n in collections.Counter(EXPLICIT.findall(s)).items() if n>1]
            if dup:raise FlowError('Duplicate explicit anchor: '+str(dup))
            heads=list(re.finditer(r'^##\s+(.+)$',s,re.M))
            if not heads or not heads[-1][1].startswith('Open Questions'):raise FlowError('Open Questions footer missing: '+str(p.relative_to(root)))
            for m in LINK.finditer(s):
                u=unquote(m[1])
                if re.match(r'^[A-Za-z][\w+.-]*:',u) or u.startswith('//'):continue
                local_count+=1;v,_,a=u.partition('#');t=(p.parent/v).resolve() if v else p.resolve()
                if not t.is_relative_to(workspace):bad.append((str(p.relative_to(root)),u,'OUTSIDE_WORKSPACE'));continue
                if not t.is_relative_to(root) and t.is_relative_to(workspace/'20_work'):bad.append((str(p.relative_to(root)),u,'WORK_NOT_AUTHORITY'));continue
                if not t.exists():bad.append((str(p.relative_to(root)),u,'MISSING'));continue
                if a and t.suffix=='.md':
                    if t not in cache:cache[t]=anchors(t.read_text())
                    if a not in cache[t]:bad.append((str(p.relative_to(root)),u,'ANCHOR'))
        if bad:raise FlowError('Document references invalid: '+str(bad[:12])+f' total={len(bad)}')
        checks.append('Markdown paths, anchors, footers and no work authority')
    if freshness:
        from view_renderer import render
        with tempfile.TemporaryDirectory(prefix='CHECK-',dir=workspace/'20_work/drafts') as tmp:
            dest=Path(tmp);shutil.copytree(root,dest,dirs_exist_ok=True)
            with contextlib.redirect_stdout(io.StringIO()):render(dest,workspace)
            stale=[p for p in projection_paths(root) if not (root/p).is_file() or sha_file(root/p)!=sha_file(dest/p)]
            if stale:raise FlowError('STALE_VIEWS: '+', '.join(stale))
        checks.append('all managed generated views are fresh')
    warnings=['文書・管理ツールの検査。抽出内容の意味・原資料承認・製品試験・認証は別。','詳細表のうち手編集正本は自動同期対象ではなくレビューを要する。','ローカル実行者はOS権限でファイルを変更可能。承認JSONは署名・本人認証サービスの代替ではない。']
    return {'result':'PASS','checks':checks,'counts':{'chapters':len(cs),'system_functions':len(ss),'gw_functions':len(gs),'requirements':len(rs),'tests':len(ts),'questions':len(qs),'usdm_elements':len(us),'typed_links':len(links_by_id),'import_bindings':len(pm['bindings']),'local_links':local_count},'warnings':warnings}
