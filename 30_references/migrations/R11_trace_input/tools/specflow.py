#!/usr/bin/env python3
"""SPK-GW specification workflow, Python 3.11+. See 00_governance/STD_Import_Merge.md.
All extraction/analysis/drafting is outside 10_canonical. Publication is pointer-last.
"""
from __future__ import annotations
import argparse, contextlib, datetime as dt, io, json, os, shutil, sys, tempfile, uuid, zipfile
from pathlib import Path
from common import *
from validate_model import validate, projection_paths, sources
from extract_sources import extract
from view_renderer import render
DEFAULT_ROOT=Path(__file__).resolve().parents[1]

def now():return dt.datetime.now(dt.timezone.utc).isoformat(timespec='seconds')
def draft_path(w,id):return inside(w,'20_work/drafts/'+require_id(id))
def record_dir(w):
    p=w/'20_work/analysis/draft_records';p.mkdir(parents=True,exist_ok=True);return p

def register(w:Path,file:Path,document_id:str,revision:str,basis='UNKNOWN',scope=None,approval='UNVERIFIED'):
    file=file.resolve()
    if not file.is_file() or file.is_symlink():raise FlowError('Expected a regular source file')
    require_id(document_id)
    if not revision.strip():raise FlowError('Document revision is required')
    raw=file.read_bytes();h=sha_bytes(raw);sid='SRC-'+record_hash([document_id,revision,h])[:24]
    registry=jread(w/'30_references/source_register.json');schema_check(w,'source_register',registry)
    found=next((s for s in registry['sources'] if s['source_id']==sid),None)
    if found:
        if sha_file(w/found['path'])!=h:raise FlowError('Registered original has changed')
        return {'result':'ALREADY_REGISTERED','source':found}
    relative='30_references/originals/'+sid+'/'+file.name
    dest=inside(w,relative);dest.parent.mkdir(parents=True,exist_ok=True)
    if dest.exists() and sha_file(dest)!=h:raise FlowError('Original collision')
    if not dest.exists():atomic_bytes(dest,raw)
    source={'source_id':sid,'document_id':document_id,'revision':revision,'sha256':h,'bytes':len(raw),'path':relative,'format':file.suffix.lower().lstrip('.') or 'unknown','basis':basis,'approval_state':approval,'received_at':now(),'access':'PROJECT_INTERNAL','scope':scope or {'applicability':'UNCONFIRMED'},'note':'原資料登録のみ。抽出・内容採用・製品承認は未完了。'}
    registry['sources'].append(source);schema_check(w,'source_register',registry);jwrite(w/'30_references/source_register.json',registry)
    return {'result':'REGISTERED','source':source}

def extract_source(w,sid):
    sm=sources(w)
    if sid not in sm:raise FlowError('Unknown source ID')
    run=extract(w/sm[sid]['path'],sm[sid]);schema_check(w,'extraction_run',run)
    out=w/'20_work/analysis/imports'/run['run_id']
    if out.exists():
        if jread(out/'extraction.json')!=run:raise FlowError('Existing run differs; never overwrite raw extraction')
        return {'result':'ALREADY_EXTRACTED','run_id':run['run_id'],'fragments':len(run['fragments'])}
    stage=out.with_name('.'+out.name+'.'+uuid.uuid4().hex);stage.mkdir(parents=True)
    try:
        jwrite(stage/'extraction.json',run)
        text='# 原資料抽出・未処理一覧\n\n状態：'+run['status']+'。以下は原文の抽出であり、解釈・採用は未実施。\n\n'
        for f in run['fragments']:
            text+='## '+f['fragment_id']+'\n\n位置：`'+json.dumps(f['locator'],ensure_ascii=False)+'`\n\n```text\n'+f['raw_text'].replace('```','` ` `')+'\n```\n\n特徴：'+', '.join(f['features'])+'\n\n'
        text+='## 未処理・要確認オブジェクト\n\n```json\n'+json.dumps(run['unhandled_objects'],ensure_ascii=False,indent=2)+'\n```\n\n## Open Questions\n\n表・注記・図・数式キャッシュ・変更履歴・適用範囲を原本と確認する。\n'
        (stage/'Extraction_Review.md').write_text(text,encoding='utf-8');os.replace(stage,out)
    finally:
        if stage.exists():shutil.rmtree(stage)
    return {'result':'EXTRACTED','run_id':run['run_id'],'status':run['status'],'fragments':len(run['fragments']),'unhandled_objects':len(run['unhandled_objects'])}

def review_fragment(w,run_id,fragment_id,actor,note):
    if not actor.strip() or not note.strip():raise FlowError('Reviewer and source comparison note required')
    run=jread(inside(w,'20_work/analysis/imports/'+require_id(run_id)+'/extraction.json'));schema_check(w,'extraction_run',run)
    f=next((f for f in run['fragments'] if f['fragment_id']==fragment_id),None)
    if not f or f['extraction_status']=='BLOCKED':raise FlowError('Fragment missing/blocked')
    result={'run_id':run_id,'fragment_id':fragment_id,'fragment_sha256':record_hash(f),'source_sha256':run['source_sha256'],'reviewer':actor,'review_note':note,'reviewed_at':now(),'status':'SOURCE_COMPARED'}
    path=w/'20_work/analysis/reviews'/(fragment_id+'.json')
    if path.exists():raise FlowError('Review already exists; retain it and create a new run or review decision rather than overwriting')
    jwrite(path,result);return result

def new_draft(w,id):
    src,meta=current(w);dest=draft_path(w,id)
    if dest.exists():raise FlowError('Draft exists')
    shutil.copytree(src,dest)
    for p in ['data/build_manifest.json']: (dest/p).unlink(missing_ok=True)
    record={'draft_id':id,'base_path':meta['path'],'base_sha256':meta['tree_sha256'],'created_at':now(),'status':'DRAFT','note':'草案。現行正本への適用はprepareと承認済みpublishが必要。'}
    jwrite(record_dir(w)/(id+'.json'),record)
    jwrite(record_dir(w)/(id+'.review.json'),{'schema':'spkgw.draft-review/v1','candidates':[],'decisions':[]})
    return {'result':'DRAFT_CREATED','draft_id':id,'path':str(dest.relative_to(w)),'base_sha256':meta['tree_sha256']}

def add_candidate(w,draft,id,run_id,fragment_ids,target_kind,target_ids,text,classification,scope):
    dest=draft_path(w,draft)
    if not dest.exists():raise FlowError('Draft missing')
    require_id(id)
    run=jread(inside(w,'20_work/analysis/imports/'+require_id(run_id)+'/extraction.json'))
    fm={f['fragment_id']:f for f in run['fragments']}
    if not set(fragment_ids)<=set(fm):raise FlowError('Candidate references missing fragment')
    review=jread(record_dir(w)/(draft+'.review.json'))
    if any(c['candidate_id']==id for c in review['candidates']):raise FlowError('Candidate ID exists')
    c={'candidate_id':id,'fragment_ids':fragment_ids,'target_kind':target_kind,'target_ids':target_ids,'interpretation':text,'classification':classification,'scope':scope,'status':'CONFLICT' if classification=='CONFLICT' else 'IN_REVIEW','resolution_note':None}
    review['candidates'].append(c);schema_check(w,'draft_review',review);jwrite(record_dir(w)/(draft+'.review.json'),review)
    # Map candidate to immutable extraction run outside the canonical tree.
    refs=record_dir(w)/(draft+'.runs.json');m=jread(refs) if refs.exists() else {}
    for fid in fragment_ids:m[fid]=run_id
    jwrite(refs,m);return c

def decide(w,draft,candidate_id,action,actor,rationale,resolution=None):
    path=record_dir(w)/(draft+'.review.json');review=jread(path)
    c=next((c for c in review['candidates'] if c['candidate_id']==candidate_id),None)
    if c is None:raise FlowError('Candidate missing')
    if any(d['candidate_id']==candidate_id for d in review['decisions']):raise FlowError('Decision already recorded; create a revised candidate for a different decision')
    if resolution:c['resolution_note']=resolution
    unresolved=c['classification']=='CONFLICT' and not c['resolution_note']
    if action in ['ADOPT','EQUIVALENT'] and (unresolved or c['classification'] in ['UNCLASSIFIED','INSUFFICIENT']):raise FlowError('Resolve source meaning/scope/conflict before adoption')
    d={'decision_id':'DEC-'+uuid.uuid4().hex[:20],'candidate_id':candidate_id,'action':action,'decided_by':actor,'decided_at':now(),'rationale':rationale,'unresolved_conflict':unresolved}
    review['decisions'].append(d);schema_check(w,'draft_review',review);jwrite(path,review);return d

def apply_record(w,draft,candidate_id,record_file):
    dest=draft_path(w,draft);review=jread(record_dir(w)/(draft+'.review.json'));schema_check(w,'draft_review',review)
    c=next((x for x in review['candidates'] if x['candidate_id']==candidate_id),None)
    dec=next((x for x in review['decisions'] if x['candidate_id']==candidate_id and x['action'] in ['ADOPT','EQUIVALENT']),None)
    if c is None or dec is None:raise FlowError('An explicit adopt/equivalent decision is required')
    row=jread(record_file)
    if row.get('id') not in c['target_ids']:raise FlowError('Record ID differs from candidate target')
    fn,key=('requirements','requirements') if c['target_kind']=='SYS' else ('usdm','elements')
    table=jread(dest/'data'/f'{fn}.json');previous=next((r for r in table[key] if r['id']==row['id']),None)
    if dec['action']=='EQUIVALENT' and previous!=row:raise FlowError('EQUIVALENT cannot change the target record')
    table[key]=[row if r['id']==row['id'] else r for r in table[key]] if previous else table[key]+[row]
    schema_check(w,fn,table)
    prov=jread(dest/'data/import_provenance.json');runs=jread(record_dir(w)/(draft+'.runs.json'))
    for fid in c['fragment_ids']:
        run=jread(w/'20_work/analysis/imports'/runs[fid]/'extraction.json');f=next(f for f in run['fragments'] if f['fragment_id']==fid)
        reviewed=jread(w/'20_work/analysis/reviews'/(fid+'.json'))
        if reviewed['fragment_sha256']!=record_hash(f) or reviewed['source_sha256']!=f['source_sha256']:raise FlowError('Source comparison review is stale')
        f=dict(f,verified_by=reviewed['reviewer'],review_note=reviewed['review_note'])
        if fid not in {x['fragment_id'] for x in prov['fragments']}:prov['fragments'].append(f)
    if c['candidate_id'] not in {x['candidate_id']for x in prov['candidates']}:prov['candidates'].append(c)
    if dec['decision_id'] not in {x['decision_id']for x in prov['decisions']}:prov['decisions'].append(dec)
    prov['bindings']=[b for b in prov['bindings'] if (b['target_kind'],b['target_id'])!=(c['target_kind'],row['id'])]
    prov['bindings'].append({'target_kind':c['target_kind'],'target_id':row['id'],'fragment_ids':c['fragment_ids'],'decision_id':dec['decision_id'],'record_sha256':record_hash(row)})
    schema_check(w,'import_provenance',prov)
    # These writes only affect a draft, never the selected canonical baseline.
    jwrite(dest/'data'/f'{fn}.json',table);jwrite(dest/'data/import_provenance.json',prov)
    return {'result':'APPLIED_TO_DRAFT_ONLY','target':row['id'],'next':'Update other trace links if required; prepare regenerates all managed views.'}

def change_gate(base,dest):
    changes=[];bindings={(b['target_kind'],b['target_id']):b for b in jread(dest/'data/import_provenance.json')['bindings']}
    for fn,key,kind in [('requirements','requirements','SYS'),('usdm','elements','USDM')]:
        a={r['id']:r for r in jread(base/'data'/f'{fn}.json')[key]};b={r['id']:r for r in jread(dest/'data'/f'{fn}.json')[key]}
        missing=set(a)-set(b)
        if missing:raise FlowError('Do not silently delete stable IDs; mark RETIRED/SUPERSEDED: '+str(sorted(missing)))
        for k,r in b.items():
            if k not in a or a[k]!=r:
                if (kind,k) not in bindings or bindings[kind,k]['record_sha256']!=record_hash(r):raise FlowError('Changed/new semantic record needs source and adoption decision: '+k)
                changes.append({'kind':kind,'id':k,'change':'ADDED' if k not in a else 'CHANGED'})
    # Other stable catalog IDs must also survive editing. Retirement is explicit, not deletion.
    for fn,key,idkey in [('test_catalog','tests','id'),('completion_items','items','question_id'),('parameters','parameters','id'),('external_interfaces','interfaces','id'),('open_issues','issues','id'),('function_catalog','system_functions','id'),('function_catalog','gw_functions','id')]:
        old={x[idkey] for x in jread(base/'data'/f'{fn}.json')[key]};new={x[idkey] for x in jread(dest/'data'/f'{fn}.json')[key]}
        if old-new:raise FlowError('Stable IDs removed from '+fn+': '+str(sorted(old-new)))
    return changes

def prepare(w,draft,fail_at=None):
    dest=draft_path(w,draft);record=jread(record_dir(w)/(draft+'.json'));base,meta=current(w)
    if record['base_sha256']!=meta['tree_sha256']:raise FlowError('STALE_BASE: canonical changed; rebase with explicit review')
    changes=change_gate(base,dest)
    # The first gate rejects invalid inputs, before any generated write.
    validate(dest,w,freshness=False,links=False)
    token='PREP-'+draft+'-'+uuid.uuid4().hex[:10];stage=draft_path(w,token)
    draft_hash=tree_hash(dest);shutil.copytree(dest,stage)
    try:
        if fail_at=='before-render':raise FlowError('Injected generation failure')
        with contextlib.redirect_stdout(io.StringIO()):render(stage,w)
        if fail_at=='after-render':raise FlowError('Injected failure after staged view generation')
        report=validate(stage,w,freshness=True)
        if tree_hash(dest)!=draft_hash:raise FlowError('Draft changed during preparation')
        t_hash=toolchain_hash(w)
        jwrite(stage/'data/build_manifest.json',{'schema':'spkgw.build-manifest/v1','toolchain_sha256':t_hash,'input_draft_sha256':draft_hash,'counts':report['counts'],'outputs':{p:sha_file(stage/p) for p in projection_paths(stage)},'note':'Generated/validated snapshot; no product approval implied.'})
        prep_hash=tree_hash(stage)
        before=file_map(base);after=file_map(stage)
        file_diff=[{'path':p,'change':'ADDED' if p not in before else 'REMOVED' if p not in after else 'CHANGED','before_sha256':before.get(p),'after_sha256':after.get(p)} for p in sorted(set(before)|set(after)) if before.get(p)!=after.get(p)]
        jwrite(record_dir(w)/(draft+'.diff.json'),{'base_path':meta['path'],'prepared_path':stage.relative_to(w).as_posix(),'base_sha256':meta['tree_sha256'],'prepared_sha256':prep_hash,'semantic_records':changes,'files':file_diff})
        preparation={'draft_id':draft,'prepared_path':stage.relative_to(w).as_posix(),'prepared_sha256':prep_hash,'base_sha256':meta['tree_sha256'],'toolchain_sha256':t_hash,'draft_sha256':draft_hash,'changes':changes,'validation':report,'prepared_at':now()}
        jwrite(record_dir(w)/(draft+'.prepared.json'),preparation)
        approval={'schema':'spkgw.adoption-approval/v1','decision':'PENDING','draft_id':draft,'prepared_sha256':prep_hash,'base_sha256':meta['tree_sha256'],'toolchain_sha256':t_hash,'approved_by':None,'approved_at':None,'rationale':None,'product_requirements_approved':False}
        ap=w/'20_work/analysis/approvals'/(draft+'.request.json');jwrite(ap,approval)
        return {'result':'PREPARED_NOT_PUBLISHED','prepared_path':preparation['prepared_path'],'approval_template':ap.relative_to(w).as_posix(),'prepared_sha256':prep_hash,'diff_report':str((record_dir(w)/(draft+'.diff.json')).relative_to(w)),'counts':report['counts']}
    except Exception:
        shutil.rmtree(stage,ignore_errors=True);raise

def publish(w,draft,approval_file,fail_at=None):
    prep=jread(record_dir(w)/(draft+'.prepared.json'));ap=jread(approval_file);schema_check(w,'approval',ap)
    for k in ['draft_id','prepared_sha256','base_sha256','toolchain_sha256']:
        if ap[k]!=prep[k]:raise FlowError('Approval identity mismatch: '+k)
    if toolchain_hash(w)!=prep['toolchain_sha256']:raise FlowError('Tools/schema changed after preparation; reprepare')
    p=inside(w,prep['prepared_path'])
    if tree_hash(p)!=prep['prepared_sha256']:raise FlowError('Prepared content changed after review')
    base,meta=current(w)
    if meta['tree_sha256']==prep['prepared_sha256']:return {'result':'ALREADY_SELECTED','path':meta['path']}
    if meta['tree_sha256']!=prep['base_sha256']:raise FlowError('STALE_BASE at publication')
    change_gate(base,p);report=validate(p,w,freshness=True)
    release='BL-'+prep['prepared_sha256'][:24];out=w/'10_canonical/releases'/release
    if not out.exists():
        stage=out.with_name('.incoming-'+uuid.uuid4().hex);shutil.copytree(p,stage)
        try:
            if tree_hash(stage)!=prep['prepared_sha256']:raise FlowError('Staged release hash mismatch')
            os.replace(stage,out)
        finally:
            if stage.exists():shutil.rmtree(stage)
    elif tree_hash(out)!=prep['prepared_sha256']:raise FlowError('Existing release differs')
    receipt={'schema':'spkgw.adoption-receipt/v1','approval':ap,'selected_tree_sha256':prep['prepared_sha256'],'base_path':meta['path'],'path':out.relative_to(w).as_posix(),'validation':report,'adopted_at':now()}
    rp=w/'10_canonical/receipts'/(release+'.json');jwrite(rp,receipt)
    if fail_at=='before-pointer':raise FlowError('Injected failure before CURRENT commit; old selected baseline is unchanged')
    # A single replacement is the visibility commit. Readers must resolve CURRENT once per operation.
    jwrite(w/'10_canonical/CURRENT.json',{'schema':'spkgw.current-baseline/v1','baseline_id':release,'path':out.relative_to(w).as_posix(),'tree_sha256':prep['prepared_sha256'],'receipt':rp.relative_to(w).as_posix(),'content_status':'DRAFT_FOR_REVIEW','product_requirements_approved':False})
    return {'result':'PUBLISHED_DOCUMENT_BASELINE','path':out.relative_to(w).as_posix(),'tree_sha256':prep['prepared_sha256']}

def compare_runs(w,old_id,new_id):
    a=jread(inside(w,'20_work/analysis/imports/'+require_id(old_id)+'/extraction.json'));b=jread(inside(w,'20_work/analysis/imports/'+require_id(new_id)+'/extraction.json'))
    loc=lambda x:record_hash(x['locator'])
    old={loc(f):f for f in a['fragments']};new={loc(f):f for f in b['fragments']}
    result={'old_run':old_id,'new_run':new_id,'unchanged':[],'changed_same_locator':[],'moved_exact_text_candidates':[],'ambiguous':[],'removed_candidates':[],'added_candidates':[],'policy':'No automatic replacement/deletion/approval. Similar text is only a review hint.'}
    handled_a=set();handled_b=set()
    for k in old.keys()&new.keys():
        f,g=old[k],new[k]
        if f['raw_text']==g['raw_text']:result['unchanged'].append([f['fragment_id'],g['fragment_id']]);handled_a.add(k);handled_b.add(k)
    for k,f in old.items():
        if k in handled_a:continue
        matches=[(nk,g)for nk,g in new.items()if nk not in handled_b and g['raw_text']==f['raw_text']]
        if len(matches)==1 and len([x for ok,x in old.items() if ok not in handled_a and x['raw_text']==f['raw_text']])==1:
            nk,g=matches[0];result['moved_exact_text_candidates'].append([f['fragment_id'],g['fragment_id']]);handled_a.add(k);handled_b.add(nk)
        elif matches:result['ambiguous'].append({'old':f['fragment_id'],'new_candidates':[g['fragment_id']for _,g in matches]})
    for k in old.keys()&new.keys():
        if k not in handled_a and k not in handled_b:result['changed_same_locator'].append([old[k]['fragment_id'],new[k]['fragment_id']]);handled_a.add(k);handled_b.add(k)
    result['removed_candidates']=[f['fragment_id']for k,f in old.items()if k not in handled_a]
    result['added_candidates']=[f['fragment_id']for k,f in new.items()if k not in handled_b]
    p=w/'20_work/analysis/comparisons'/f'{old_id}__{new_id}.json';jwrite(p,result);return result

def import_coverage(w,run_id):
    run=jread(inside(w,'20_work/analysis/imports/'+require_id(run_id)+'/extraction.json'))
    schema_check(w,'extraction_run',run)
    accepted=set()
    baseline,_=current(w)
    for b in jread(baseline/'data/import_provenance.json')['bindings']:accepted.update(b['fragment_ids'])
    links={f['fragment_id']:[] for f in run['fragments']}
    for rp in record_dir(w).glob('*.review.json'):
        rv=jread(rp);schema_check(w,'draft_review',rv)
        decisions={x['candidate_id']:x for x in rv['decisions']}
        for c in rv['candidates']:
            d=decisions.get(c['candidate_id'])
            for fid in c['fragment_ids']:
                if fid in links:links[fid].append({'candidate_id':c['candidate_id'],'review_file':rp.relative_to(w).as_posix(),'classification':c['classification'],'decision':d['action'] if d else 'UNDECIDED'})
    rows=[]
    for f in run['fragments']:
        fid=f['fragment_id'];ref=links[fid]
        state='SELECTED_CANONICAL' if fid in accepted else 'NOT_CLASSIFIED' if not ref else 'IN_REVIEW' if any(x['decision']=='UNDECIDED' for x in ref) else 'DECISION_RECORDED'
        rows.append({'fragment_id':fid,'locator':f['locator'],'state':state,'candidate_decisions':ref})
    from collections import Counter
    report={'run_id':run_id,'source_id':run['source_id'],'counts':dict(Counter(x['state'] for x in rows)),'fragments':rows,'unhandled_objects':run['unhandled_objects'],'full_document_acceptance':'NOT_AUTOMATICALLY_GRANTED','note':'原文断片の処置状況。図等の未処理と採用内容の妥当性・承認は別。ADOPT判断のみではSELECTED_CANONICALにならない。'}
    p=w/'20_work/analysis/coverage'/(run_id+'.json');jwrite(p,report);return report

def audit_baseline(w):
    prof=jread(w/'00_governance/baseline_R8_FIX001.json');zpath=inside(w,prof['zip_path'])
    if sha_file(zpath)!=prof['zip_sha256']:raise FlowError('Original R8-FIX001 ZIP differs')
    base=inside(w,prof['extracted_path']);expected=prof['files'];actual=file_map(base)
    if actual!=expected:raise FlowError('R8 extracted originals differ: '+str(sorted(set(actual)^set(expected))[:10]))
    return {'result':'PASS','scope':'R8-FIX001 original archive + exact extracted tree','files':len(actual),'sha256':prof['zip_sha256']}

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--root',type=Path,default=DEFAULT_ROOT);sub=ap.add_subparsers(dest='cmd',required=True)
    sub.add_parser('current');sub.add_parser('audit-baseline')
    p=sub.add_parser('register');p.add_argument('--file',type=Path,required=True);p.add_argument('--document-id',required=True);p.add_argument('--revision',required=True);p.add_argument('--basis',choices=['AS_IS','TO_BE','UNKNOWN'],default='UNKNOWN');p.add_argument('--scope',default='{}');p.add_argument('--scope-file',type=Path)
    p=sub.add_parser('extract');p.add_argument('--source',required=True)
    p=sub.add_parser('review-fragment');p.add_argument('--run',required=True);p.add_argument('--fragment',required=True);p.add_argument('--by',required=True);p.add_argument('--note',required=True)
    p=sub.add_parser('new-draft');p.add_argument('--id',required=True)
    p=sub.add_parser('candidate');p.add_argument('--draft',required=True);p.add_argument('--id',required=True);p.add_argument('--run',required=True);p.add_argument('--fragment',action='append',required=True);p.add_argument('--target-kind',choices=['SYS','USDM'],default='SYS');p.add_argument('--target',action='append',required=True);p.add_argument('--interpretation',required=True);p.add_argument('--classification',choices=['UNCLASSIFIED','EQUAL','ADDITION','DETAIL','SCOPE_VARIANT','CONFLICT','OBSOLETE','INSUFFICIENT'],default='UNCLASSIFIED');g=p.add_mutually_exclusive_group(required=True);g.add_argument('--scope');g.add_argument('--scope-file',type=Path)
    p=sub.add_parser('decide');p.add_argument('--draft',required=True);p.add_argument('--candidate',required=True);p.add_argument('--action',choices=['ADOPT','EQUIVALENT','DEFER','REJECT','REFERENCE_ONLY'],required=True);p.add_argument('--by',required=True);p.add_argument('--rationale',required=True);p.add_argument('--resolution')
    p=sub.add_parser('apply-record');p.add_argument('--draft',required=True);p.add_argument('--candidate',required=True);p.add_argument('--record',type=Path,required=True)
    p=sub.add_parser('validate');p.add_argument('--draft');p.add_argument('--no-freshness',action='store_true')
    p=sub.add_parser('prepare');p.add_argument('--draft',required=True)
    p=sub.add_parser('publish');p.add_argument('--draft',required=True);p.add_argument('--approval',type=Path,required=True)
    p=sub.add_parser('compare-runs');p.add_argument('--old',required=True);p.add_argument('--new',required=True)
    p=sub.add_parser('coverage');p.add_argument('--run',required=True)
    args=ap.parse_args();w=args.root.resolve()
    # All writers use the same lock. Read-only validation does not modify selected data.
    readonly=args.cmd in ['current','audit-baseline','validate']
    with contextlib.nullcontext() if readonly else workspace_lock(w):
        if args.cmd=='current':p,m=current(w);result={**m,'moc':str(p/'00_MOC.md')}
        elif args.cmd=='audit-baseline':result=audit_baseline(w)
        elif args.cmd=='register':result=register(w,args.file,args.document_id,args.revision,args.basis,jread(args.scope_file) if args.scope_file else json.loads(args.scope))
        elif args.cmd=='extract':result=extract_source(w,args.source)
        elif args.cmd=='review-fragment':result=review_fragment(w,args.run,args.fragment,args.by,args.note)
        elif args.cmd=='new-draft':result=new_draft(w,args.id)
        elif args.cmd=='candidate':result=add_candidate(w,args.draft,args.id,args.run,args.fragment,args.target_kind,args.target,args.interpretation,args.classification,jread(args.scope_file) if args.scope_file else json.loads(args.scope))
        elif args.cmd=='decide':result=decide(w,args.draft,args.candidate,args.action,args.by,args.rationale,args.resolution)
        elif args.cmd=='apply-record':result=apply_record(w,args.draft,args.candidate,args.record)
        elif args.cmd=='validate':result=validate(draft_path(w,args.draft) if args.draft else current(w)[0],w,freshness=not args.no_freshness)
        elif args.cmd=='prepare':result=prepare(w,args.draft)
        elif args.cmd=='publish':result=publish(w,args.draft,args.approval)
        elif args.cmd=='compare-runs':result=compare_runs(w,args.old,args.new)
        elif args.cmd=='coverage':result=import_coverage(w,args.run)
        else:raise FlowError('Unknown command')
    print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':
    try:main()
    except (FlowError,OSError,KeyError,TypeError,ValueError,zipfile.BadZipFile) as e:
        print(json.dumps({'result':'FAIL','error':str(e)},ensure_ascii=False),file=sys.stderr);sys.exit(1)
