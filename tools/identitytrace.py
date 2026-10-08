"""Document/item identity checks. Local, read-only; no inference of requirement approval.
DTR identifies a logical document; ITR an individual semantic item; THR an optional theme.
"""
from __future__ import annotations
import copy, hashlib, json, re
from pathlib import Path
from common import FlowError, inside
DTR = r'DTR-SPKGW-[A-Z][A-Z0-9]*-[0-9]{6}'
ITR = r'ITR-SPKGW-[A-Z][A-Z0-9]*-[0-9]{6}'
THR = r'THR-SPKGW-[A-Z][A-Z0-9]*-[0-9]{6}'
PHASES = ['CONCEPT','REQAN','REQSPEC','SYSDES','ARCH','BASIC','DETAIL','IMPL','UT','IT','ST','NFT','VALID','RELPREP','RELEASE','OPS','IMPROVE']
class IdentityError(FlowError):pass

def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def unique(rows,key):
    out={}
    for x in rows:
        if x[key] in out:raise IdentityError('Duplicate '+key+': '+x[key])
        out[x[key]]=x
    return out

def pointer(obj, selector):
    if not selector.startswith('json:'):raise IdentityError('Expected JSON selector')
    p=selector[5:]
    if p and not p.startswith('/'):raise IdentityError('Invalid JSON pointer')
    try:
        for k in p.split('/')[1:]:
            k=k.replace('~1','/').replace('~0','~')
            obj=obj[int(k)] if isinstance(obj,list) else obj[k]
    except (ValueError,KeyError,IndexError,TypeError) as e:raise IdentityError('JSON pointer not found: '+p) from e
    return obj

def check_selector(root, doc, selector):
    p=inside(root,doc['path'])
    if selector.startswith('json:'):
        return pointer(json.loads(p.read_text(encoding='utf-8-sig')),selector)
    if selector.startswith('anchor:'):
        a=selector[7:]
        if not re.fullmatch(r'[A-Za-z0-9_.:-]+',a):raise IdentityError('Invalid anchor')
        if not re.search(r'id\s*=\s*[\'"]'+re.escape(a)+r'[\'"]',p.read_text(encoding='utf-8-sig')):
            raise IdentityError('Explicit anchor missing: '+a)
        return None
    raise IdentityError('Unsupported selector: use anchor: or json:. Office/code locators require a locally extracted record, not an unverified free-text selector.')

def validate_identities(root,data,read):
    docs=unique(data['documents'],'document_version_id')
    seen=set();pathseen={};logical={};notes={};warnings=[]
    for d in docs.values():
        if not re.fullmatch(DTR,d['document_trace_id']):raise IdentityError('Invalid document TraceID')
        pair=(d['document_trace_id'],d['revision'])
        if pair in seen:raise IdentityError('Duplicate document/revision')
        seen.add(pair)
        if d['revision'].strip().lower() in {'latest','head','current'}:raise IdentityError('Floating document revision')
        p=inside(root,d['path'])
        if not p.is_file() or digest(p)!=d['sha256']:raise IdentityError('Document hash mismatch/missing: '+d['path'])
        if d['path'] in pathseen:raise IdentityError('Document path registered twice: '+d['path'])
        pathseen[d['path']]=d['document_trace_id']
        logical.setdefault(d['document_trace_id'],[]).append(d)
        # Current editable FrontMatter and sidecar must agree. Frozen originals may use older metadata.
        if d['representation']=='AUTHORING' and p.suffix.lower()=='.md':
            text=p.read_text(encoding='utf-8-sig')
            if text.startswith('---\n'):
                from govcheck import frontmatter
                f=frontmatter(p)
                if f.get('trace_contract')=='spkgw.lifecycle-tags/v2':
                    if f.get('document_trace_id')!=d['document_trace_id']:raise IdentityError('FrontMatter document TraceID mismatch: '+d['path'])
                    if str(f['revision'])!=d['revision']:raise IdentityError('FrontMatter revision mismatch')
                    notes[d['document_version_id']]=f
    known={d['document_version_id']for d in data['documents']};itemids={};native={};selected=set()
    for n in data['nodes']:
        if n['item_trace_id']!=n['artifact_id'] or not re.fullmatch(ITR,n['item_trace_id']):raise IdentityError('Item identity mismatch / document ID used as item ID')
        if n['document_version_id'] not in known:raise IdentityError('Unknown containing document version')
        doc=docs[n['document_version_id']]
        if n['record_state']=='RECORDED':
            loc=n['locator']
            if loc['path']!=doc['path'] or loc['sha256']!=doc['sha256']:raise IdentityError('Item locator does not match its containing document version')
            if not loc.get('selector'):raise IdentityError('Item requires an exact selector, not just a whole document')
            value=check_selector(root,doc,loc['selector'])
            if isinstance(value,str) and n['native_ids'] and value not in n['native_ids']:
                raise IdentityError('Native item ID does not match source selector')
        if n['thread_id'] is not None and not re.fullmatch(THR,n['thread_id']):raise IdentityError('Invalid thread identity')
        if n['phase_basis']=='UNASSIGNED' and n['phase_ids']:raise IdentityError('UNASSIGNED item must not declare phases')
        if not set(n['phase_ids']).issubset(PHASES):raise IdentityError('Unknown/ordinal phase code')
        # Different nodes may be revisions of the same item; the native identity must remain compatible.
        if n['item_trace_id'] in itemids and itemids[n['item_trace_id']]!=set(n['native_ids']):raise IdentityError('Native identity changed across item revisions')
        itemids[n['item_trace_id']]=set(n['native_ids'])
        if n['selected']:
            if n['item_trace_id'] in selected:raise IdentityError('Multiple selected item revisions')
            selected.add(n['item_trace_id'])
            for a in n['native_ids']:
                if a in native and native[a]!=n['item_trace_id']:raise IdentityError('Native alias maps to multiple current items: '+a)
                native[a]=n['item_trace_id']
        for vid in n['reference_document_version_ids']:
            if vid not in known:raise IdentityError('Unknown reference document version')
        for loc in n['occurrences']:
            if loc['document_version_id'] not in known:raise IdentityError('Unknown occurrence document version')
            check_selector(root,docs[loc['document_version_id']],loc['selector'])
    nodes={n['node_id']for n in data['nodes']}
    for e in data['edges']:
        if e['from_node']not in nodes or e['to_node']not in nodes:raise IdentityError('Item edge cannot use a document endpoint / unknown item node')
    de=unique(data.get('document_edges',[]),'edge_id')
    for e in de.values():
        if e['from_document']not in docs or e['to_document']not in docs:raise IdentityError('Document edge cannot use an item endpoint')
        if e['relation']not in {'references','generated_from','supersedes'}:raise IdentityError('Invalid document relation')
        if e['relation']=='supersedes' and docs[e['from_document']]['document_trace_id']!=docs[e['to_document']]['document_trace_id']:
            raise IdentityError('Document supersedes requires the same stable document ID')
    for vid,f in notes.items():
        for iid in f['item_trace_ids']:
            matches=[n for n in data['nodes'] if n['item_trace_id']==iid and (n['document_version_id']==vid or any(o['document_version_id']==vid for o in n['occurrences']))]
            if not matches:raise IdentityError('FrontMatter item not present in document: '+iid)
        # item_trace_ids lists owned items, not every cited item. Empty governance summary lists are allowed.
    if not data['nodes']:warnings.append({'code':'NO_ITEM_RECORDS'})
    for code,test in [('ITEM_PHASE_UNASSIGNED',lambda n:not n['phase_ids']),('ITEM_THREAD_UNASSIGNED',lambda n:n['thread_id']is None),('ITEM_RELATION_REVIEW_PENDING',lambda n:n['review']is None)]:
        count=sum(test(n)for n in data['nodes'])
        if count:warnings.append({'code':code,'count':count})
    return {'documents':len(logical),'document_versions':len(docs),'items':len(itemids),'item_versions':len(data['nodes']),'document_edges':len(de),'warnings':warnings}

def legacy_view(data):
    """In-memory adapter only; v2 on-disk registry remains the sole graph authority."""
    out=copy.deepcopy(data)
    for group in ['profiles','nodes']:
        for row in out[group]:
            row['trace_id']=row.get('thread_id')
            if group=='nodes':row['related_trace_ids']=row['related_thread_ids']
    return out

def resolve(data,aliases,value,namespace=None):
    value=aliases.get('thread_aliases',{}).get(value,value)
    answers=[]
    if namespace in (None,'document'):
        for d in data.get('documents',[]):
            if value in {d['document_trace_id'],d['document_version_id'],d['document_id']}:
                answers.append({'namespace':'document','id':d['document_trace_id'],'version_id':d['document_version_id'],'revision':d['revision'],'path':d['path']})
    if namespace in (None,'item'):
        for n in data['nodes']:
            if value in {n.get('item_trace_id'),n['node_id'],*n.get('native_ids',[])}:
                answers.append({'namespace':'item','id':n.get('item_trace_id',n['artifact_id']),'node_id':n['node_id'],'revision':n['revision'],'selected':n['selected'],'document_version_id':n.get('document_version_id'),'locator':n['locator']})
    if namespace in (None,'thread'):
        for p in data['profiles']:
            if p.get('thread_id',p.get('trace_id'))==value:answers.append({'namespace':'thread','id':value})
    return {'requested_id':value,'matches':answers,'result':'RESOLVED' if len(answers)==1 else ('NOT_FOUND' if not answers else 'MULTIPLE_VERSIONS_OR_NAMESPACES'),'auto_selected':False}

def document_report(data,value):
    docs=[d for d in data['documents']if value in {d['document_trace_id'],d['document_version_id']}]
    if not docs:raise IdentityError('Unknown document TraceID')
    ids={d['document_version_id']for d in docs}
    items=[{'item_trace_id':n['item_trace_id'],'node_id':n['node_id'],'native_ids':n['native_ids'],'phases':n['phase_ids'],'locator':n['locator'],'review':n['review']}for n in data['nodes']if n['document_version_id']in ids or any(o['document_version_id']in ids for o in n['occurrences'])]
    return {'documents':docs,'items':items,'whole_document_verified':False,'limitation':'Document existence/approval does not prove every contained item implements or verifies a requirement.'}
