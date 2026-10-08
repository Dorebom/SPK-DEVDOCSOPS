#!/usr/bin/env python3
"""Read-only engineering lifecycle trace checks (not product/test approval).
Local, hash-bound evidence only; no external repository/API calls. Python >=3.11.
"""
from __future__ import annotations
import argparse, collections, hashlib, json, re, sys
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker
from common import FlowError, inside
from identitytrace import validate_identities, legacy_view, resolve, document_report

ROOT = Path(__file__).resolve().parents[1]
GRAPH = Path('20_work/analysis/project/trace_graph.json')
PROFILE = Path('00_governance/lifecycle_profile.json')
SCHEMA = Path('00_governance/schemas/lifecycle-trace.schema.json')
CONTROL = Path('20_work/analysis/project/control.json')

class TraceError(FlowError):
    pass

def load(path: Path):
    def pairs(items):
        value = {}
        for key, item in items:
            if key in value:
                raise TraceError('Duplicate JSON key: ' + key)
            value[key] = item
        return value
    return json.loads(path.read_text(encoding='utf-8-sig'), object_pairs_hook=pairs)

def index(rows, key, label):
    result = {}
    for row in rows:
        if row[key] in result:
            raise TraceError('Duplicate ' + label + ': ' + row[key])
        result[row[key]] = row
    return result

def confirmed(review):
    return review is not None and review['state'] == 'CONFIRMED'

def subject_hash(record):
    """Bind review to content/identity; selection/active flags only select an evaluation view."""
    ignored={'review','selected','active'}
    if 'thread_id' in record: ignored |= {'trace_id','related_trace_ids'}
    value={k:v for k,v in record.items() if k not in ignored}
    return hashlib.sha256(json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode('utf-8')).hexdigest()

def membership(node):
    return {x for x in [node['trace_id'], *node['related_trace_ids']] if x is not None}

def _cycles(graph, label):
    # Iterative Kahn: large graphs do not rely on Python recursion depth.
    degree = {key: 0 for key in graph}
    for targets in graph.values():
        for target in targets:
            degree[target] = degree.get(target, 0) + 1
    queue = collections.deque(key for key, value in degree.items() if value == 0)
    done = 0
    while queue:
        key = queue.popleft(); done += 1
        for target in graph.get(key, []):
            degree[target] -= 1
            if degree[target] == 0:
                queue.append(target)
    if done != len(degree):
        raise TraceError('Cycle in ' + label)

def validate(root: Path, graph_path: Path | None = None):
    root = root.resolve()
    path = graph_path or root / GRAPH
    # Even CLI overrides must stay inside this workspace.
    path = inside(root, str(path.resolve().relative_to(root)))
    data, config, control = load(path), load(root / PROFILE), load(root / CONTROL)
    is_v2 = data.get('schema') == 'spkgw.lifecycle-trace/v2'
    schema_path = root / SCHEMA if is_v2 else root / '00_governance/schemas/lifecycle-trace-v1.schema.json'
    errors = list(Draft202012Validator(load(schema_path), format_checker=FormatChecker()).iter_errors(data))
    if errors:
        error = errors[0]
        raise TraceError('Schema ' + '/'.join(map(str, error.path)) + ': ' + error.message)
    identity_check = validate_identities(root,data,load) if is_v2 else None
    if is_v2: data = legacy_view(data)
    phases = index(config['phases'], 'id', 'phase')
    phase_ids = set(phases)
    traces = index(control['traces'], 'id', 'TraceID')
    actors = index(control['actors'], 'id', 'actor')
    profiles = index(data['profiles'], 'trace_id', 'trace profile')
    nodes = index(data['nodes'], 'node_id', 'node')
    edges = index(data['edges'], 'edge_id', 'edge')
    trels = index(data['trace_relations'], 'id', 'trace relation')
    warnings = list(identity_check['warnings']) if identity_check else [{'code':'LEGACY_V1_GRAPH_NO_DOCUMENT_ITEM_BINDING'}]
    for group in [profiles, nodes, edges, trels]:
        # These maps are separate namespaces; endpoint identities are explicitly typed.
        if not isinstance(group, dict):
            raise TraceError('Invalid registry')

    def has(key, collection, label):
        if key not in collection:
            raise TraceError('Unknown ' + label + ': ' + str(key))

    checked = {}
    def locator(value):
        p = inside(root, value['path'])
        if not p.is_file():
            raise TraceError('Locator missing: ' + value['path'])
        digest = checked.setdefault(value['path'], hashlib.sha256(p.read_bytes()).hexdigest())
        if digest != value['sha256']:
            raise TraceError('Locator hash mismatch: ' + value['path'])
        selector = value.get('selector')
        if selector:
            if selector.startswith('anchor:'):
                anchor = selector[7:]
                if not re.fullmatch(r'[A-Za-z0-9_.:-]+', anchor):
                    raise TraceError('Invalid explicit anchor selector')
                text = p.read_text(encoding='utf-8-sig')
                if not re.search(r'id\s*=\s*[\'"]' + re.escape(anchor) + r'[\'"]', text):
                    raise TraceError('Explicit anchor missing: ' + anchor)
            elif selector.startswith('json:'):
                pointer = selector[5:]
                if pointer and not pointer.startswith('/'):
                    raise TraceError('Invalid JSON pointer')
                obj = load(p)
                try:
                    for part in pointer.split('/')[1:]:
                        part = part.replace('~1', '/').replace('~0', '~')
                        obj = obj[int(part)] if isinstance(obj, list) else obj[part]
                except (ValueError, IndexError, KeyError, TypeError) as e:
                    raise TraceError('JSON pointer not found: ' + pointer) from e
            else:
                raise TraceError('Unsupported locator selector; use explicit anchor: or json:')

    def review(value, subject):
        if value is None:
            return
        if value['reviewer'] is not None:
            has(value['reviewer'], actors, 'reviewer')
        if value['evidence'] is not None:
            locator(value['evidence'])
        if confirmed(value) and value['subject_sha256'] != subject_hash(subject):
            raise TraceError('Review subject hash mismatch; changed content needs re-review')
        # Fields are declared evidence, not a cryptographic signature or identity proof.

    for tid, item in profiles.items():
        has(tid, traces, 'profile TraceID')
        plan = index(item['phase_plan'], 'phase_id', 'phase plan')
        if set(plan) != phase_ids:
            raise TraceError('Phase plan must declare every configured phase: ' + tid)
        for row in plan.values():
            review(row['review'], row)
            if row['applicability'] == 'NOT_APPLICABLE':
                if not row['rationale'] or not confirmed(row['review']):
                    raise TraceError('N/A requires rationale and confirmed decision evidence')
        for nid in item['root_node_ids']:
            has(nid, nodes, 'root node')
            if tid not in membership(nodes[nid]):
                raise TraceError('Root belongs to different TraceID')
    identities = set(); selected = set()
    for nid, node in nodes.items():
        if node['trace_id'] is not None: has(node['trace_id'], traces, 'node TraceID')
        for tid in node['related_trace_ids']:
            has(tid, traces, 'related TraceID')
        if node['trace_id'] in node['related_trace_ids']:
            raise TraceError('Primary TraceID repeated in related_trace_ids')
        if not node['phase_ids'] and not is_v2:
            warnings.append({'code':'PHASE_UNASSIGNED', 'node':nid})
        pair = (node['artifact_id'], node['revision'])
        if pair in identities:
            raise TraceError('Duplicate artifact/revision; share one node across traces')
        identities.add(pair)
        if node['revision'].strip().lower() in {'head','latest','current'}:
            raise TraceError('Floating revision is not a pinned identity')
        if node['selected']:
            if node['artifact_id'] in selected:
                raise TraceError('Multiple selected revisions for artifact: ' + node['artifact_id'])
            selected.add(node['artifact_id'])
        if node['locator'] is not None:
            locator(node['locator'])
        if confirmed(node['review']) and node['record_state'] != 'RECORDED':
            raise TraceError('Planned artifact cannot be confirmed as recorded')
        review(node['review'], node)
    duplicates = set(); directed = {nid: [] for nid in nodes}
    for eid, edge in edges.items():
        has(edge['from_node'], nodes, 'edge source')
        has(edge['to_node'], nodes, 'edge target')
        has(edge['relation'], config['relations'], 'relation type')
        if edge['from_node'] == edge['to_node']:
            raise TraceError('Self edge is not a dependency')
        triple = (edge['from_node'], edge['relation'], edge['to_node'])
        if triple in duplicates:
            raise TraceError('Duplicate typed edge')
        duplicates.add(triple)
        a, b = nodes[edge['from_node']], nodes[edge['to_node']]
        relation = edge['relation']
        # High-value relation kind checks. Remaining relations require content review.
        if relation == 'implements' and a['kind'] != 'IMPLEMENTATION':
            raise TraceError('implements must start at IMPLEMENTATION')
        if relation == 'verifies' and a['kind'] != 'TEST_CASE':
            raise TraceError('verifies must start at TEST_CASE, not a meeting or test result')
        if relation == 'verifies' and b['kind'] not in {'REQUIREMENT','SPECIFICATION','SYSTEM_DESIGN','ARCHITECTURE','STRUCTURAL_DESIGN','DETAIL_DESIGN','IMPLEMENTATION'}:
            raise TraceError('verifies target must be a requirement, design or implementation')
        if relation == 'validates' and a['kind'] != 'VALIDATION':
            raise TraceError('validates must start at VALIDATION')
        if relation == 'deployment_of' and (a['kind'] != 'DEPLOYMENT' or b['kind'] != 'RELEASE'):
            raise TraceError('deployment_of requires DEPLOYMENT -> RELEASE')
        if relation == 'supersedes' and a['artifact_id'] != b['artifact_id']:
            raise TraceError('supersedes requires versions of the same artifact')
        review(edge['review'], edge)
        if confirmed(edge['review']) and (a['record_state'] != 'RECORDED' or b['record_state'] != 'RECORDED'):
            raise TraceError('Confirmed edge requires recorded endpoints')
        if edge['active'] and (not a['selected'] or not b['selected']):
            # A supersedes link to the old revision is intentionally historical.
            if relation != 'supersedes':
                warnings.append({'code':'STALE_REFERENCE','edge':eid})
        if relation in {'derives_from','refines','allocated_from','supersedes'}:
            directed[edge['from_node']].append(edge['to_node'])
    _cycles(directed, 'derivation/version dependencies')
    tg = {tid: [] for tid in traces}
    for row in trels.values():
        has(row['from_trace'], traces, 'child TraceID'); has(row['to_trace'], traces, 'parent TraceID')
        if row['from_trace'] == row['to_trace']:
            raise TraceError('Trace relation cannot point to itself')
        tg[row['from_trace']].append(row['to_trace'])
    _cycles(tg, 'trace lineage')
    for tid in traces:
        if tid not in profiles:
            warnings.append({'code':'TRACE_PROFILE_MISSING','trace_id':tid})
    from govcheck import frontmatter
    registered_tasks={aid for n in nodes.values() if n['kind']=='TASK' and n['selected'] for aid in [n['artifact_id'],*n.get('native_ids',[])]}
    for task_path in sorted((root/'20_work/drafts/project/tasks').glob('*.md')):
        task=frontmatter(task_path)
        if task['task_id'] not in registered_tasks:
            warnings.append({'code':'TASK_NOT_IN_ARTIFACT_GRAPH','task_id':task['task_id'],'thread_id':task.get('thread_id',task.get('trace_id'))})
    result = {'schema':'spkgw.trace-check/v1','result':'PASS','scope':'STRUCTURAL_RECORD_CHECK_NOT_PRODUCT_APPROVAL',
              'trace_profiles':len(profiles),'nodes':len(nodes),'edges':len(edges),'warnings':warnings,
              'inputs':{p.relative_to(root).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in [path, root/PROFILE, root/SCHEMA, root/CONTROL, root/'tools/tracecheck.py'] if p.is_file()},
              'checked_local_evidence':checked,'identity_check':identity_check}
    return result, data, config

def report(root: Path, trace_id: str, graph_path: Path | None = None):
    check, data, config = validate(root, graph_path)
    aliases_path=root/'00_governance/trace_aliases.json'
    if aliases_path.is_file(): trace_id=load(aliases_path).get('thread_aliases',{}).get(trace_id,trace_id)
    profiles = {x['trace_id']: x for x in data['profiles']}
    if trace_id not in profiles:
        raise TraceError('No lifecycle profile for TraceID: ' + trace_id)
    p = profiles[trace_id]
    nodes = {x['node_id']:x for x in data['nodes'] if trace_id in membership(x)}
    usable = {nid for nid,n in nodes.items() if n['selected'] and n['record_state']=='RECORDED' and confirmed(n['review'])}
    neighbours = {nid:set() for nid in usable}
    for e in data['edges']:
        if (e['active'] and confirmed(e['review']) and config['relations'][e['relation']]['counts_for_connectivity']
            and e['from_node'] in usable and e['to_node'] in usable):
            neighbours[e['from_node']].add(e['to_node']); neighbours[e['to_node']].add(e['from_node'])
    roots = set(p['root_node_ids']) & usable
    def reach(adjacency):
        seen=set(roots);queue=collections.deque(sorted(roots))
        while queue:
            for nxt in sorted(adjacency[queue.popleft()] - seen):
                seen.add(nxt);queue.append(nxt)
        return seen
    seen=reach(neighbours)
    context={nid:set() for nid in usable}
    for edge in data['edges']:
        a,b=edge['from_node'],edge['to_node']
        if edge['active'] and confirmed(edge['review']) and a in usable and b in usable:
            context[a].add(b);context[b].add(a)
    context_seen=reach(context)
    plans = {x['phase_id']:x for x in p['phase_plan']}
    rows = []
    for phase in config['phases']:
        row = plans[phase['id']]
        phase_nodes = [n for n in nodes.values() if n['selected'] and phase['id'] in n['phase_ids']]
        recorded = [n for n in phase_nodes if n['record_state']=='RECORDED']
        linked = [n for n in phase_nodes if n['node_id'] in seen]
        required = set(row['required_kinds']); available = {n['kind'] for n in linked}
        if row['applicability']=='TBD': status='TBD'
        elif row['applicability']=='NOT_APPLICABLE': status='NOT_APPLICABLE'
        elif not required: status='REQUIRED_OUTPUTS_UNDEFINED'
        elif not phase_nodes: status='MISSING'
        elif not recorded: status='PLANNED_ONLY'
        elif required <= available: status='LINKED_RECORDS'
        elif not any(n['node_id'] in usable for n in recorded): status='PENDING_REVIEW'
        else: status='GAP'
        rows.append({'phase_id':phase['id'],'phase':phase['name'],'applicability':row['applicability'],
                     'record_status':status,'required_kinds':sorted(required),'missing_kinds':sorted(required-available),
                     'selected_nodes':[n['node_id'] for n in phase_nodes],'linked_nodes':[n['node_id'] for n in linked]})
    structural_ready = bool(roots) and all(row['record_status'] in {'LINKED_RECORDS','NOT_APPLICABLE'} for row in rows)
    relevant_ids=set(nodes)
    stale=[w for w in check['warnings'] if w['code']=='STALE_REFERENCE' and any(e['edge_id']==w['edge'] and (e['from_node'] in relevant_ids or e['to_node'] in relevant_ids) for e in data['edges'])]
    context_gaps=sorted(nid for nid,node in nodes.items() if node['selected'] and nid not in context_seen)
    if stale or context_gaps: structural_ready=False
    return {'schema':'spkgw.lifecycle-record-report/v1','thread_id':trace_id,'assessment_scope':p['assessment_scope'],
            'record_chain_ready':structural_ready,'product_progress':None,'phases':rows,
            'context_unconnected_nodes':context_gaps,'context_linked_nodes':sorted(context_seen),
            'selected_unconnected_nodes':sorted(nid for nid,n in nodes.items() if n['selected'] and nid not in seen),
            'warnings':check['warnings'],'inputs':check['inputs'],
            'limitations':['Linked records are not test PASS, phase approval, release authorization or assurance of semantic correctness.',
                           'No external repository fetch, ACL/identity proof or cost allocation. Only registered local hash-bound records are checked.',
                           '17-phase tailoring is not a requirement to execute every phase for each task. Unknown remains TBD.']}

def impact(root: Path, node_id: str, graph_path: Path | None = None):
    check,data,config=validate(root, graph_path)
    nodes={n['node_id']:n for n in data['nodes']}
    if node_id not in nodes: raise TraceError('Unknown impact node: '+node_id)
    reverse={nid:[] for nid in nodes}
    for edge in data['edges']:
        if edge['active'] and config['relations'][edge['relation']]['direction']=='dependent_to_basis':
            reverse[edge['to_node']].append((edge['from_node'],edge['edge_id']))
    seen={node_id};q=collections.deque([node_id]);paths=[]
    while q:
        parent=q.popleft()
        for child,eid in sorted(reverse[parent]):
            if child not in seen:
                seen.add(child);q.append(child);paths.append({'node_id':child,'via_edge':eid,'depends_on':parent,'selected':nodes[child]['selected']})
    return {'schema':'spkgw.trace-impact/v1','changed_node':node_id,'review_candidates':paths,
            'decision':'REVIEW_REQUIRED_NOT_AUTO_IMPACT_APPROVAL','inputs':check['inputs']}

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--workspace',type=Path,default=ROOT)
    ap.add_argument('--graph',type=str,default=GRAPH.as_posix())
    sp=ap.add_subparsers(dest='command',required=True)
    sp.add_parser('validate')
    p=sp.add_parser('report');p.add_argument('--thread','--trace',dest='trace',required=True);p.add_argument('--require-linked',action='store_true')
    p=sp.add_parser('impact');p.add_argument('--node',required=True)
    p=sp.add_parser('resolve');p.add_argument('--id',required=True);p.add_argument('--namespace',choices=['document','item','thread'])
    p=sp.add_parser('document');p.add_argument('--id',required=True)
    args=ap.parse_args();root=args.workspace.resolve()
    try:
        path=inside(root,args.graph)
        if args.command=='validate': result=validate(root,path)[0]
        elif args.command=='report': result=report(root,args.trace,path)
        elif args.command=='impact':result=impact(root,args.node,path)
        elif args.command=='resolve':
            validate(root,path);result=resolve(load(path),load(root/'00_governance/trace_aliases.json'),args.id,args.namespace)
        else:
            validate(root,path);result=document_report(load(path),args.id)
        print(json.dumps(result,ensure_ascii=False,indent=2))
        if getattr(args,'require_linked',False) and not result['record_chain_ready']:
            sys.exit(2)
    except (TraceError,FlowError,OSError,ValueError,KeyError,TypeError) as error:
        print(json.dumps({'result':'FAIL','error':str(error)},ensure_ascii=False),file=sys.stderr);sys.exit(1)
if __name__=='__main__':main()
