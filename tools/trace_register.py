"""Minimal task document/item registration. No source fetch or semantic auto-classification."""
from __future__ import annotations
import copy, json, hashlib, re, os
from pathlib import Path
import yaml
from common import FlowError, workspace_lock, jread, jwrite
GRAPH=Path('20_work/analysis/project/trace_graph.json')

def next_id(prefix,values):
    nums=[int(v[len(prefix):])for v in values if v.startswith(prefix) and re.fullmatch(r'\d{6}',v[len(prefix):])]
    number=max(nums,default=0)+1
    if number>999999:raise FlowError('ID namespace exhausted')
    return prefix+f'{number:06d}'

def task_node(f,path,sha,doc):
    iid=f['item_trace_ids'][0]
    return {'node_id':iid+'_V_'+f['revision'].replace('.','_'),'item_trace_id':iid,'artifact_id':iid,'revision':f['revision'],'kind':'TASK','title':f['title'],
      'thread_id':f['thread_id'],'related_thread_ids':f.get('related_thread_ids',[]),'phase_ids':f['phase_ids'],'phase_basis':'UNASSIGNED' if not f['phase_ids'] else 'EXPLICIT',
      'record_state':'RECORDED','selected':True,'document_version_id':doc['document_version_id'],'native_ids':[f['task_id']],
      'locator':{'path':path,'sha256':sha,'selector':'anchor:'+f['task_id'].lower()},'occurrences':[],'reference_document_version_ids':[],'review':None}

def create_task(root,path,f,title):
    """Roll back both writes on handled failure. Crash durability still requires repository/OS discipline."""
    with workspace_lock(root):
        graph_path=root/GRAPH;old=graph_path.read_bytes();g=json.loads(old)
        if g.get('schema')!='spkgw.lifecycle-trace/v2':raise FlowError('Migrate graph to v2 before creating R12 tasks')
        f['document_trace_id']=next_id('DTR-SPKGW-TASK-',{d['document_trace_id']for d in g['documents']})
        f['item_trace_ids']=[next_id('ITR-SPKGW-TASK-',{n['item_trace_id']for n in g['nodes']})]
        from govcheck import schema
        schema(root,'task',f)
        rel=path.relative_to(root).as_posix()
        text='---\n'+yaml.safe_dump(f,allow_unicode=True,sort_keys=False).strip()+'\n---\n\n<a id="'+f['task_id'].lower()+'"></a>\n# '+title.strip()+'\n\n## 目的・範囲\n\n記入待ち。\n\n## 完了条件・証拠\n\nFrontMatterへ記入する。\n\n## Open Questions\n\n担当・見積・期日・入力・レビュー条件を確定する。\n'
        h=hashlib.sha256(text.encode()).hexdigest()
        d={'document_trace_id':f['document_trace_id'],'document_version_id':f['document_trace_id']+'_V_'+f['revision'].replace('.','_'),'document_id':f['document_id'],'revision':f['revision'],'title':title,'kind':'TASK','path':rel,'sha256':h,'source_ids':[],'representation':'AUTHORING','origin_status':f['status']}
        g['documents'].append(d);g['nodes'].append(task_node(f,rel,h,d))
        created=False
        try:
            with path.open('x',encoding='utf-8',newline='\n')as out:out.write(text)
            created=True;jwrite(graph_path,g)
        except Exception:
            if created:path.unlink(missing_ok=True)
            if graph_path.read_bytes()!=old:
                tmp=graph_path.with_suffix('.rollback.tmp');tmp.write_bytes(old);os.replace(tmp,graph_path)
            raise
