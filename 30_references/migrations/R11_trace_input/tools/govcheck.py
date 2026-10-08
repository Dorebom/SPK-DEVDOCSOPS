#!/usr/bin/env python3
"""Governance metadata/task validator and read-only progress/cost reporting.
Does not authorize spending or prove a reviewer's identity. Python >=3.11.
Authoritative working records: project TASK markdown and analysis/project/control.json.
"""
from __future__ import annotations
import argparse, copy, datetime as dt, hashlib, json, re, sys, uuid
from decimal import Decimal
from pathlib import Path
import yaml
from jsonschema import Draft202012Validator, FormatChecker
from common import FlowError, inside, jread, jwrite, sha_file, current, workspace_lock

ROOT=Path(__file__).resolve().parents[1]
SCHEMAS=Path('00_governance/schemas')
CONTROL=Path('20_work/analysis/project/control.json')
TASKS=Path('20_work/drafts/project/tasks')
class GovernanceError(FlowError): pass
class StrictLoader(yaml.SafeLoader): pass
# Keep ISO dates as strings; unsafe objects remain disabled.
StrictLoader.yaml_implicit_resolvers=copy.deepcopy(yaml.SafeLoader.yaml_implicit_resolvers)
for k,vals in StrictLoader.yaml_implicit_resolvers.items():
    StrictLoader.yaml_implicit_resolvers[k]=[(t,r) for t,r in vals if t!='tag:yaml.org,2002:timestamp']
def mapping(loader,node,deep=False):
    result={}
    for k,v in node.value:
        key=loader.construct_object(k,deep=deep)
        if not isinstance(key,str):raise GovernanceError('YAML keys must be strings')
        if key in result:raise GovernanceError('Duplicate YAML key: '+key)
        result[key]=loader.construct_object(v,deep=deep)
    return result
StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,mapping)

def frontmatter(path:Path):
    text=path.read_text(encoding='utf-8-sig')
    m=re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)',text,re.S)
    if not m:raise GovernanceError('Missing FrontMatter: '+str(path))
    try:value=yaml.load(m.group(1),Loader=StrictLoader)
    except yaml.YAMLError as e:raise GovernanceError('Invalid YAML: '+str(path)+': '+str(e)) from e
    if not isinstance(value,dict):raise GovernanceError('FrontMatter must be an object')
    return value

def schema(root:Path,name:str,value):
    sch=jread(root/SCHEMAS/(name+'.schema.json'))
    errors=sorted(Draft202012Validator(sch,format_checker=FormatChecker()).iter_errors(value),key=lambda e:str(list(e.path)))
    if errors:raise GovernanceError(name+': '+'; '.join('/'.join(map(str,e.path))+': '+e.message for e in errors[:5]))

def catalog_ids(root):
    path,meta=current(root)
    found=set()
    def walk(x):
        if isinstance(x,dict):
            for k,v in x.items():
                if (k=='id' or k.endswith('_id')) and isinstance(v,str):found.add(v)
                walk(v)
        elif isinstance(x,list):
            for v in x:walk(v)
    # Only actual declared identities; references alone do not create entities.
    primary=['requirements.json','function_catalog.json','test_catalog.json','open_issues.json','parameters.json','external_interfaces.json','completion_items.json','usdm.json']
    for fn in primary:
        p=path/'data'/fn
        if not p.exists():continue
        def declarations(x):
            if isinstance(x,dict):
                for k,v in x.items():
                    if k in {'id','question_id','item_id','interface_id'} and isinstance(v,str):found.add(v)
                    declarations(v)
            elif isinstance(x,list):
                for v in x:declarations(v)
        declarations(jread(p))
    return found,meta

def lifecycle_meta(value,traces,active=False):
    """Optional R11 contract; legacy tasks retain explicit migration warnings."""
    if 'trace_contract' not in value:return
    phases=value['phase_ids'];scope=value['phase_scope']
    if value['trace_id'] in value['related_trace_ids']:
        raise GovernanceError('Primary trace repeated in related traces')
    for tid in value['related_trace_ids']:
        if tid not in traces:raise GovernanceError('Unknown related trace: '+tid)
    if scope=='PHASE_SPECIFIC' and len(phases)!=1:
        raise GovernanceError('PHASE_SPECIFIC requires one phase')
    if scope=='CROSS_PHASE' and len(phases)<2:
        raise GovernanceError('CROSS_PHASE requires multiple phases')
    if scope=='UNASSIGNED' and phases:
        raise GovernanceError('UNASSIGNED cannot have selected phases')
    primary=value.get('phase')
    if primary and re.fullmatch(r'P[0-9]{2}',primary) and primary not in phases:
        raise GovernanceError('Primary phase not in phase_ids')
    if active and (not phases or value['activity_type']=='UNSPECIFIED'):
        raise GovernanceError('R11 active task needs phase_ids and activity_type')

def unique(rows,label):
    out={}
    for r in rows:
        k=r['id']
        if k in out:raise GovernanceError('Duplicate '+label+' id: '+k)
        out[k]=r
    return out

def no_cycles(graph,label):
    pending=set();done=set()
    def visit(n):
        if n in pending:raise GovernanceError('Cycle in '+label+': '+n)
        if n in done:return
        pending.add(n)
        for d in graph.get(n,[]):visit(d)
        pending.remove(n);done.add(n)
    for n in graph:visit(n)

def decimal_string(n):return format(n,'f')
def validate(root:Path,as_of:str|None=None):
    root=root.resolve();cutoff=dt.date.fromisoformat(as_of) if as_of else dt.datetime.now(dt.timezone(dt.timedelta(hours=9))).date()
    controls=jread(root/CONTROL);schema(root,'project-control',controls)
    c=controls;warnings=[]
    groups={k:unique(c[k],k) for k in ['actors','traces','work_packages','effort','costs','commitments','forecasts','evidence','runs','decisions','edges']}
    seen={}
    for group,rows in groups.items():
        for id in rows:
            if id in seen:raise GovernanceError('Cross-entity duplicate id: '+id)
            seen[id]=group
    actors=groups['actors'];traces=groups['traces'];evidence=groups['evidence'];tasks={};task_paths={};docs={}
    def ref(id,allowed,label):
        if id not in allowed:raise GovernanceError('Unknown '+label+': '+str(id))
    declared,meta=catalog_ids(root)
    legacy=jread(root/'00_governance/legacy_documents.json')['documents']
    legacy_paths={i['path']for i in legacy}
    for i in legacy:
        p=inside(root,i['path'])
        if not p.is_file() or sha_file(p)!=i['sha256']:raise GovernanceError('Legacy governance bytes changed: '+i['path'])
        declared.add(i['document_id'])
    for p in sorted((root/'00_governance').rglob('*.md')):
        rel=p.relative_to(root).as_posix()
        if rel in legacy_paths:continue
        f=frontmatter(p);schema(root,'frontmatter',f)
        if f['document_id'] in docs:raise GovernanceError('Duplicate document_id: '+f['document_id'])
        docs[f['document_id']]=f;declared.add(f['document_id'])
        if f['updated_on']<f['created_on']:raise GovernanceError('updated_on before created_on')
        if f['owner'] is not None:ref(f['owner'],actors,'owner')
        ref(f['trace_id'],traces,'trace')
        lifecycle_meta(f,traces)
        if '## Open Questions' not in p.read_text(encoding='utf-8'):raise GovernanceError('Open Questions missing: '+rel)
    for p in sorted((root/TASKS).glob('*.md')):
        t=frontmatter(p);schema(root,'task',t)
        if t['document_type']!='TASK' or t['task_id']!=t['document_id']:raise GovernanceError('TASK identity mismatch')
        tid=t['task_id']
        if tid in tasks or tid in docs or tid in seen:raise GovernanceError('Duplicate task id: '+tid)
        if t['updated_on']<t['created_on']:raise GovernanceError('Task dates reversed')
        tasks[tid]=t;task_paths[tid]=p.relative_to(root).as_posix()
    declared.update(tasks);declared.update(seen)
    for key in ['plan','budget']:
        if c[key]:
            if c[key]['id']in declared:raise GovernanceError('Cross-entity duplicate plan/budget id')
            declared.add(c[key]['id'])
    for f in docs.values():
        for x in f['related_ids']:ref(x,declared,'document relation')
    for trace in traces.values():
        if not inside(root,trace['source_path']).is_file():raise GovernanceError('Trace source missing')
    for e in evidence.values():
        p=inside(root,e['path'])
        if not p.is_file() or sha_file(p)!=e['sha256']:raise GovernanceError('Evidence hash mismatch/missing: '+e['id'])
        if e['run_id'] is not None:ref(e['run_id'],groups['runs'],'evidence execution')
    graph={};parents={}
    for tid,t in tasks.items():
        ref(t['trace_id'],traces,'task trace');ref(t['wbs_id'],groups['work_packages'],'WBS')
        if t['owner'] is not None:ref(t['owner'],actors,'owner')
        for k in ['assignees','reviewers']:
            for x in t[k]:ref(x,actors,k)
        for x in t['linked_ids']+t['related_ids']:ref(x,declared,'linked_id')
        for x in t['evidence_ids']:ref(x,evidence,'task evidence')
        for x in t['run_ids']:ref(x,groups['runs'],'task run')
        for x in t['approval_refs']:ref(x,groups['decisions'],'approval decision')
        for dep in t['depends_on']:ref(dep,tasks,'dependency')
        graph[tid]=t['depends_on'];parents[tid]=[t['parent_task_id']] if t['parent_task_id'] else []
        if t['parent_task_id']:
            ref(t['parent_task_id'],tasks,'parent')
            if not tasks[t['parent_task_id']]['summary']:raise GovernanceError('Parent task is not summary')
        if t['milestone_id'] is not None:ref(t['milestone_id'],groups['work_packages'],'milestone/WBS')
        if t['source_baseline']!=meta['baseline_id']:warnings.append(tid+': work based on non-current baseline; review compatibility')
        active=t['state']not in ['PROPOSED','CANCELLED']
        lifecycle_meta(t,traces,active)
        if 'trace_contract' not in t:warnings.append(tid+': R10 phase requires explicit R11 lifecycle mapping')
        if active:
            if not t['owner'] or not t['assignees'] or not t['reviewers']:raise GovernanceError('Active task requires owner, assignees, reviewers: '+tid)
            if not t['summary'] and (t['estimate_hours'] is None or t['remaining_hours'] is None):raise GovernanceError('Active task estimates missing: '+tid)
            if not t['linked_ids']:raise GovernanceError('Active task lacks purpose linkage')
            if not t['approval_refs']:raise GovernanceError('Active task lacks work authorization record')
        else:
            if t['owner'] is None or t['estimate_hours'] is None:warnings.append(tid+': owner/estimate not assigned; not ready')
        if t['state']in ['READY','IN_PROGRESS','IN_REVIEW','DONE']:
            for dep in t['depends_on']:
                if tasks[dep]['state']!='DONE':raise GovernanceError('Unfinished dependency: '+tid+' -> '+dep)
        if t['state']=='BLOCKED':
            if not t['blocker']:raise GovernanceError('BLOCKED task lacks unblock contract')
            ref(t['blocker']['owner'],actors,'blocker owner')
        if t['state']=='CANCELLED':
            if not t['cancellation']:raise GovernanceError('CANCELLED lacks decision')
            ref(t['cancellation']['decision_id'],groups['decisions'],'cancellation decision')
        if t['state']=='DONE':
            if not t['acceptance'] or not t['evidence_ids']:raise GovernanceError('DONE requires acceptance and evidence')
            if t['remaining_hours']!=0:raise GovernanceError('DONE has remaining work')
            a=t['acceptance'];ref(a['actor_id'],actors,'acceptance actor')
            if a['actor_id']not in t['reviewers']:raise GovernanceError('Acceptance actor not assigned reviewer')
            if actors[a['actor_id']]['kind']!='HUMAN':raise GovernanceError('Human accountability required for task acceptance')
            for eid in a['evidence_ids']:ref(eid,evidence,'acceptance evidence')
            if not set(a['evidence_ids']).issubset(t['evidence_ids']):raise GovernanceError('Acceptance evidence not on task')
        for p in t['artifacts']:
            target=inside(root,p)
            if t['state'] in ['IN_REVIEW','DONE'] and not target.exists():raise GovernanceError('Submitted artifact missing: '+p)
    no_cycles(graph,'task dependency');no_cycles(parents,'task parent')
    wg={}
    for w in groups['work_packages'].values():
        if w['parent_id']:ref(w['parent_id'],groups['work_packages'],'WBS parent')
        wg[w['id']]=[w['parent_id']]if w['parent_id']else []
    no_cycles(wg,'WBS')
    for t in tasks.values():
        if t['summary']:
            children=[x for x in tasks.values()if x['parent_task_id']==t['task_id']]
            if t['state']=='DONE' and any(x['state']!='DONE'for x in children):raise GovernanceError('Summary DONE with unfinished children')
    def approval(a,label):
        ref(a['actor_id'],actors,label+' approver');ref(a['evidence_id'],evidence,label+' approval evidence')
        if actors[a['actor_id']]['kind']!='HUMAN':raise GovernanceError('Human approver required for '+label)
    if c['plan']:
        approval(c['plan']['approval'],'plan');ids=[]
        for line in c['plan']['lines']:
            ref(line['task_id'],tasks,'plan task');t=tasks[line['task_id']]
            if t['summary']:raise GovernanceError('Plan weights may only cover leaf tasks')
            if line['kind']!=t['kind']:raise GovernanceError('Plan/task kind mismatch')
            if line['finish_on']<line['start_on']:raise GovernanceError('Plan dates reversed')
            ids.append(line['task_id'])
        if len(ids)!=len(set(ids)):raise GovernanceError('Duplicate plan task')
    else:warnings.append('PLAN_NOT_APPROVED: weighted progress unavailable')
    for t in tasks.values():
        if t['baseline_plan_id'] is not None and (not c['plan'] or t['baseline_plan_id']!=c['plan']['id']):raise GovernanceError('Unknown baseline_plan_id')
    if c['budget']:
        approval(c['budget']['approval'],'budget')
        if c['budget']['currency']!=c['cost_basis']['currency'] or c['budget']['tax_basis']!=c['cost_basis']['tax_basis']:raise GovernanceError('Budget currency/tax mismatch')
    else:warnings.append('BUDGET_NOT_APPROVED: budget variance unavailable')
    for group in ['effort','costs','commitments','forecasts','runs']:
        for row in c[group]:
            ref(row['task_id'],tasks,group+' task')
            if tasks[row['task_id']]['summary']:raise GovernanceError('Cannot account actual/forecast on summary task')
    for r in c['runs']:
        ref(r['trace_id'],traces,'run trace');ref(r['actor_id'],actors,'run actor')
        if dt.datetime.fromisoformat(r['finished_at'].replace('Z','+00:00'))<dt.datetime.fromisoformat(r['started_at'].replace('Z','+00:00')):raise GovernanceError('Run dates reversed')
        for eid in r['evidence_ids']:ref(eid,evidence,'run evidence')
        if r['id']not in tasks[r['task_id']]['run_ids']:raise GovernanceError('Run missing reverse task link')
    for tid,t in tasks.items():
        for rid in t['run_ids']:
            if groups['runs'][rid]['task_id']!=tid:raise GovernanceError('Task run points to other task')
    keys=set()
    for e in c['effort']:
        ref(e['actor_id'],actors,'effort actor');ref(e['evidence_id'],evidence,'effort evidence')
        if actors[e['actor_id']]['kind']!='HUMAN':raise GovernanceError('AI/service duration is not human labor')
        if Decimal(e['hours'])<=0:raise GovernanceError('Effort hours must be positive')
        if e['source_key']in keys:raise GovernanceError('Duplicate effort source_key')
        keys.add(e['source_key'])
        if dt.date.fromisoformat(e['worked_on'])>cutoff:raise GovernanceError('Future effort beyond report cutoff')
    costkeys=set();reversed_ids=set()
    for row in c['costs']:
        ref(row['evidence_id'],evidence,'cost evidence')
        if row['source_key']in costkeys:raise GovernanceError('Duplicate cost source_key')
        costkeys.add(row['source_key'])
        if dt.date.fromisoformat(row['incurred_on'])>cutoff:raise GovernanceError('Future cost beyond report cutoff')
        amount=Decimal(row['amount'])
        if amount<0:
            if not row['reverses_id']:raise GovernanceError('Negative cost requires reverses_id')
            ref(row['reverses_id'],groups['costs'],'reversed cost')
            original=groups['costs'][row['reverses_id']]
            if original['reverses_id'] is not None or amount!=-Decimal(original['amount']):raise GovernanceError('Reversal must exactly offset original')
            if row['task_id']!=original['task_id'] or row['commitment_id']!=original['commitment_id']:raise GovernanceError('Reversal scope differs')
            if row['reverses_id']in reversed_ids:raise GovernanceError('Double reversal')
            reversed_ids.add(row['reverses_id'])
        elif row['reverses_id']is not None:raise GovernanceError('Positive reversal is not allowed')
        if row['commitment_id']:
            ref(row['commitment_id'],groups['commitments'],'cost commitment')
            if groups['commitments'][row['commitment_id']]['task_id']!=row['task_id']:raise GovernanceError('Commitment/task mismatch')
    forecasts={}
    for f in c['forecasts']:
        if f['task_id']in forecasts:raise GovernanceError('Multiple current forecasts for task; archive old records first')
        forecasts[f['task_id']]=f
        if dt.date.fromisoformat(f['as_of'])>cutoff:raise GovernanceError('Future forecast beyond report cutoff')
    oc={}
    for co in c['commitments']:
        ref(co['evidence_id'],evidence,'commitment evidence')
        if dt.date.fromisoformat(co['committed_on'])>cutoff:raise GovernanceError('Future commitment beyond report cutoff')
        actual=sum((Decimal(x['amount'])for x in c['costs']if x['commitment_id']==co['id']),Decimal(0))
        residual=Decimal(co['amount'])-actual
        if residual<0:raise GovernanceError('Commitment overrun requires documented amendment')
        if actual<0:raise GovernanceError('Negative allocated actual')
        oc[co['task_id']]=oc.get(co['task_id'],Decimal(0))+residual
    for tid,residual in oc.items():
        if tid in forecasts and Decimal(forecasts[tid]['etc_amount'])<residual:raise GovernanceError('ETC below outstanding commitment')
    allmoney=c['costs']+c['commitments']+c['forecasts']
    for row in allmoney:
        if row['currency']!=c['cost_basis']['currency'] or row['tax_basis']!=c['cost_basis']['tax_basis']:raise GovernanceError('Mixed/undefined currency or tax basis')
    for d in c['decisions']:
        ref(d['actor_id'],actors,'decision actor');ref(d['evidence_id'],evidence,'decision evidence')
    for e in c['edges']:
        ref(e['from_id'],declared,'edge source');ref(e['to_id'],declared,'edge target')
    if c['actuals_complete_through']:
        if not c['actuals_confirmation']:raise GovernanceError('Actuals completeness needs confirmation')
        ref(c['actuals_confirmation']['actor_id'],actors,'actuals confirmer')
        ref(c['actuals_confirmation']['evidence_id'],evidence,'actuals confirmation evidence')
        if actors[c['actuals_confirmation']['actor_id']]['kind']!='HUMAN':raise GovernanceError('Actuals confirmation needs human accountability')
        if dt.date.fromisoformat(c['actuals_complete_through'])>cutoff:raise GovernanceError('Completeness claim beyond cutoff')
    else:warnings.append('ACTUALS_NOT_CONFIRMED: empty ledger is not proof of zero cost')
    inputfiles=[root/CONTROL,root/'10_canonical/CURRENT.json',root/'tools/govcheck.py']+[root/p for p in task_paths.values()]+sorted((root/SCHEMAS).glob('*.json'))
    inputs={p.relative_to(root).as_posix():sha_file(p)for p in inputfiles}
    return {'result':'PASS','checked_on':cutoff.isoformat(),'tasks':len(tasks),'governance_notes':len(docs),'warnings':warnings,'canonical_baseline':meta['baseline_id'],'inputs':inputs},tasks,c,oc

def report(root,as_of=None):
    v,tasks,c,oc=validate(root,as_of)
    states={x:sum(t['state']==x for t in tasks.values())for x in ['PROPOSED','READY','IN_PROGRESS','BLOCKED','ON_HOLD','IN_REVIEW','DONE','CANCELLED']}
    plan=c['plan'];weight=Decimal(0);earned=Decimal(0)
    baseline_ids=set()
    if plan:
        for row in plan['lines']:
            baseline_ids.add(row['task_id'])
            if row['kind']!='DISCRETE':continue
            w=Decimal(str(row['weight_hours']));weight+=w
            if tasks[row['task_id']]['state']=='DONE':earned+=w
    ac=sum((Decimal(x['amount'])for x in c['costs']),Decimal(0))
    etc=sum((Decimal(x['etc_amount'])for x in c['forecasts']),Decimal(0))
    forecast_ids={r['task_id']for r in c['forecasts']}
    needed={tid for tid,t in tasks.items()if not t['summary'] and t['state']not in ['DONE','CANCELLED']}
    # Done/cancelled tasks with a residual commitment still require future exposure estimate.
    needed.update(tid for tid,value in oc.items()if value>0)
    missing=sorted(needed-forecast_ids)
    complete=(c['actuals_complete_through'] is not None and c['actuals_complete_through']>=v['checked_on'])
    eac=ac+etc if complete and not missing and c['cost_basis']['currency']else None
    bac=Decimal(c['budget']['amount'])if c['budget']else None
    return {'schema':'spkgw.management-report/v1','as_of':v['checked_on'],'document_baseline':v['canonical_baseline'],'plan_id':plan['id']if plan else None,'budget_id':c['budget']['id']if c['budget']else None,'task_states':states,'leaf_task_count':sum(not t['summary']for t in tasks.values()),'loe_task_count':sum(t['kind']=='LOE'and not t['summary']for t in tasks.values()),'weighted_accepted_progress':decimal_string(earned/weight)if weight>0 else None,'baseline_weight_hours':decimal_string(weight)if plan else None,'unbaselined_tasks':sorted(set(tasks)-baseline_ids),'unestimated_tasks':sorted(tid for tid,t in tasks.items()if not t['summary']and t['estimate_hours']is None),'remaining_hours':sum(t['remaining_hours']for t in tasks.values()if not t['summary']and t['remaining_hours']is not None),'remaining_hours_complete':all(t['remaining_hours']is not None for t in tasks.values()if not t['summary']and t['state']not in ['DONE','CANCELLED']),'recorded_effort_hours':decimal_string(sum((Decimal(x['hours'])for x in c['effort']),Decimal(0))),'currency':c['cost_basis']['currency'],'tax_basis':c['cost_basis']['tax_basis'],'BAC':decimal_string(bac)if bac is not None else None,'recorded_AC':decimal_string(ac),'actuals_complete':complete,'outstanding_commitments':decimal_string(sum(oc.values(),Decimal(0))),'recorded_ETC_including_commitments':decimal_string(etc),'missing_forecast_tasks':missing,'EAC':decimal_string(eac)if eac is not None else None,'VAC':decimal_string(bac-eac)if bac is not None and eac is not None else None,'warnings':v['warnings'],'inputs':v['inputs'],'limitations':['Ledger totals are recorded amounts, not proof of accounting completeness.','No CPM/automatic schedule optimization, EVM, FX conversion, identity authorization or product conformity judgment.','Approved baselines are declarative control records; content/authority are manually reviewed.']}

def new_task(root,title,trace,wbs,phase=None,activity=None,related_traces=None):
    if not title.strip():raise GovernanceError('Empty task title')
    _,_,c,_=validate(root)
    if trace not in {x['id']for x in c['traces']}or wbs not in {x['id']for x in c['work_packages']}:raise GovernanceError('Register trace and WBS first')
    f=frontmatter(root/'00_governance/templates/Task.md')
    tid='TASK-SPKGW-'+uuid.uuid4().hex[:12].upper();day=dt.datetime.now(dt.timezone(dt.timedelta(hours=9))).date().isoformat()
    f.update(document_id=tid,task_id=tid,title=title.strip(),trace_id=trace,wbs_id=wbs,created_on=day,updated_on=day,source_baseline=current(root)[1]['baseline_id'])
    if phase is not None:
        f.update(phase=phase,phase_ids=[phase],phase_scope='PHASE_SPECIFIC')
    if activity is not None:f['activity_type']=activity
    if related_traces is not None:f['related_trace_ids']=related_traces
    schema(root,'task',f)
    lifecycle_meta(f,{x['id']for x in c['traces']})
    path=root/TASKS/(tid+'.md');path.parent.mkdir(parents=True,exist_ok=True)
    with workspace_lock(root):
        with path.open('x',encoding='utf-8',newline='\n')as out:
            out.write('---\n'+yaml.safe_dump(f,allow_unicode=True,sort_keys=False).strip()+'\n---\n\n# '+title.strip()+'\n\n## 目的・範囲\n\n記入待ち。\n\n## 完了条件・証拠\n\nFrontMatterへ記入する。\n\n## Open Questions\n\n担当・見積・期日・入力・レビュー条件を確定する。\n')
    return {'result':'CREATED_PROPOSED_TASK','task_id':tid,'path':path.relative_to(root).as_posix()}

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--workspace',type=Path,default=ROOT)
    sp=ap.add_subparsers(dest='cmd',required=True)
    for command in ['validate','report']:
        p=sp.add_parser(command);p.add_argument('--as-of');p.add_argument('--out',type=str)
    p=sp.add_parser('new-task');p.add_argument('--title',required=True);p.add_argument('--trace',required=True);p.add_argument('--wbs',required=True);p.add_argument('--phase',choices=['P%02d'%i for i in range(1,18)]);p.add_argument('--activity');p.add_argument('--related-trace',action='append',default=[])
    a=ap.parse_args();root=a.workspace.resolve()
    try:
        if a.cmd=='validate':result=validate(root,a.as_of)[0]
        elif a.cmd=='report':result=report(root,a.as_of)
        else:result=new_task(root,a.title,a.trace,a.wbs,a.phase,a.activity,a.related_trace)
        if getattr(a,'out',None):
            path=inside(root,a.out)
            if not path.is_relative_to((root/'20_work/analysis/project/reports').resolve()):raise GovernanceError('Reports may only be written under analysis/project/reports')
            if path.exists():raise GovernanceError('Report exists; choose a new report filename')
            jwrite(path,result)
        print(json.dumps(result,ensure_ascii=False,indent=2))
    except (GovernanceError,FlowError,OSError,ValueError,KeyError)as e:
        print(json.dumps({'result':'FAIL','error':str(e)},ensure_ascii=False),file=sys.stderr);sys.exit(1)
if __name__=='__main__':main()
