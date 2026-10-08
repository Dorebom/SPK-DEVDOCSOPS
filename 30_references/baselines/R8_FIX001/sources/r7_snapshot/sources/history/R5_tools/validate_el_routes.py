#!/usr/bin/env python3
"""Check document-only EL paths and Mermaid endpoints. No network/device tests."""
from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parents[1]

def parse_edges(source):
    edges=set()
    pat=re.compile(r'^\s*(\w+)(?:\[".*?"\])?\s*(<-->|-->|-\.->)\s*(?:\|".*?"\|)?\s*(\w+)')
    for line in source.splitlines():
        m=pat.match(line)
        if not m:continue
        a,arrow,b=m.groups();edges.add((a,b))
        if arrow=='<-->':edges.add((b,a))
    return edges

def check():
    errors=[];checks={}
    text=(ROOT/'chapters/02_System_Context.md').read_text(encoding='utf-8')
    blocks=re.findall(r'```mermaid\n(.*?)\n```',text,re.S)
    names=['02_01_System_Context','02_01_EL_Connections']
    for name,body in zip(names,blocks):
        disk=(ROOT/'diagrams'/f'{name}.mmd').read_text(encoding='utf-8').strip()
        if body.strip()!=disk:errors.append('Stale Mermaid export: '+name)
    checks['two_mermaid_exports_match_chapter']=len(blocks)>=2
    expected=[['EL','HNET','LAN','AC'],['EL','HNET','LAN','HW'],['EL','HNET','LAN','METER'],['EL','HNET','LAN','PN','EI']]
    for number,body in enumerate(blocks[:2],1):
        edges=parse_edges(body)
        for path in expected:
            for a,b in zip(path,path[1:]):
                if (a,b) not in edges or (b,a) not in edges:errors.append(f'Diagram {number} lacks bidirectional edge {a}/{b}')
        for target in ['AC','HW','METER','PN','EI']:
            if ('EL',target) in edges or (target,'EL') in edges:errors.append(f'Diagram {number} bypasses explicit LAN boundary: {target}')
        checks[f'diagram_{number}_ordinary_paths']=4
    e=parse_edges(blocks[0])
    path=['PC','PN','LAN','WAN','NET','GRID']
    for a,b in zip(path,path[1:]):
        if (a,b) not in e or (b,a) not in e:errors.append('PCS self-fetch edge missing '+a+'/'+b)
    if ('EL','PC') in e or ('PC','EL') in e:errors.append('Normal Controller incorrectly connected to PCS schedule client')
    if ('LINK','RSPCS') not in e or ('RSPCS','LINK') not in e:errors.append('RS-485 PCS path removed')
    for a,b in [('GC','LAN'),('LAN','WAN'),('WAN','NET'),('NET','GRID')]:
        if (a,b) not in e or (b,a) not in e:errors.append('GW G-side fetch edge missing '+a+'/'+b)
    checks['grid_paths_preserved_with_router']=True
    f=parse_edges(blocks[1])
    for x in ['DPC','FLC','MS']:
        if (x,'EL') not in f or ('EL',x) not in f:errors.append('Missing H responsibility '+x)
    checks['h_domain_roles_and_response_paths']=3
    routes=json.loads((ROOT/'data/echonet_normal_routes.json').read_text(encoding='utf-8'))['routes']
    if {x['route_id'] for x in routes}!={'EL-N01','EL-N02','EL-N03','EL-N04'}:errors.append('Unexpected route IDs')
    for x in routes:
        p=x['request_path']
        if p[0]!='GW_H_EL_CONTROLLER' or p[1:3]!=['GW_H_LAN_INTERFACE','HOME_ROUTER_LAN_AP']:errors.append('Incorrect LAN route '+x['route_id'])
        if x['response_path']!=p[::-1] or x['notification_path']!=p[::-1]:errors.append('Return path mismatch '+x['route_id'])
        if any(n in p for n in ['INTERNET','GRID_SERVER','GW_GRID_CLIENT']):errors.append('Normal EL path incorrectly routed to WAN/G')
        if x['interface_id']!='IF-EL-01':errors.append('Unexpected ordinary contract '+x['route_id'])
    checks['ordinary_route_records']=len(routes)
    if any(x['semantic_owner']!='Measurement / Device State Service' for x in routes if x['route_id']=='EL-N03'):errors.append('Meter incorrectly allocated as an actuator')
    checks['meter_owned_by_measurement']=True
    renders=json.loads((ROOT/'data/diagram_render_validation.json').read_text(encoding='utf-8'))
    import hashlib
    for r in renders['diagrams']:
        p=ROOT/r['source']
        if hashlib.sha256(p.read_bytes()).hexdigest()!=r['source_sha256']:errors.append('Rendered image source changed '+r['source'])
        for field in ['svg','png']:
            if not (ROOT/r[field]).is_file():errors.append('Missing diagram '+r[field])
    checks['rendered_source_hashes_verified']=len(renders['diagrams'])
    return {'status':'FAIL' if errors else 'PASS','scope':'DOCUMENT_MODEL_ONLY_NOT_DEVICE_CONNECTIVITY','checks':checks,'errors':errors}

if __name__=='__main__':
    result=check();print(json.dumps(result,ensure_ascii=False,indent=2));raise SystemExit(result['status']!='PASS')
