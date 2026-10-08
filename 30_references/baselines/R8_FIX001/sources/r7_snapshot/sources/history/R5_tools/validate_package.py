#!/usr/bin/env python3
"""Validate document structure and provenance; not firmware or certification tests.

Usage: python tools/validate_package.py [--refresh-manifest] [--skip-manifest]
After editing, inspect the diffs before refreshing a document manifest.
"""
from pathlib import Path
from urllib.parse import unquote
import argparse
import hashlib
import json
import re
import sys
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]

def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def entries(root: Path):
    return sorted(p for p in root.rglob('*') if p.is_file() and '__pycache__' not in p.parts)

def refresh_manifest() -> None:
    lines = [f'{sha(p)}  {p.relative_to(ROOT).as_posix()}' for p in entries(ROOT)
             if p != ROOT / 'MANIFEST_SHA256.txt']
    (ROOT/'MANIFEST_SHA256.txt').write_text('\n'.join(lines)+'\n',encoding='utf-8')

def run(skip_manifest=False):
    errors=[]
    checks={}
    allfiles=entries(ROOT)
    md_files=[p for p in allfiles if p.suffix=='.md']
    texts={}
    for p in md_files:
        try:
            text=p.read_text(encoding='utf-8')
            texts[p.resolve()]=text
            if '\ufffd' in text: errors.append(f'UTF-8 replacement character: {p.relative_to(ROOT)}')
        except UnicodeDecodeError as e:
            errors.append(f'UTF-8: {p}: {e}')
    checks['markdown_utf8_files']=len(texts)
    checks['markdown_code_fences']=0
    checks['mermaid_diagrams_generated']=0
    checks['json_code_examples_parsed']=0
    for p,text in texts.items():
        active=None
        language=''
        body=[]
        for n,line in enumerate(text.splitlines(),1):
            m=re.match(r'^\s*(`{3,}|~{3,})(.*)$',line)
            if not m:
                if active: body.append(line)
                continue
            fence,rest=m.groups()
            if active is None:
                active=fence; language=rest.strip(); body=[]
                checks['markdown_code_fences']+=1
            elif fence[0]==active[0] and len(fence)>=len(active) and not rest.strip():
                if language=='json':
                    try: json.loads('\n'.join(body));checks['json_code_examples_parsed']+=1
                    except json.JSONDecodeError as e:errors.append(f'JSON code block {p}:{n}: {e}')
                if language=='mermaid' and '/sources/' not in p.as_posix() and p.name!='90_All_In_One.md':
                    checks['mermaid_diagrams_generated']+=1
                    if not body or not re.match(r'^(flowchart|graph|sequenceDiagram|stateDiagram-v2)\b',body[0].strip()):
                        errors.append(f'Unknown Mermaid type: {p}:{n}')
                active=None;language='';body=[]
        if active: errors.append(f'Unclosed fence: {p}')
        explicit=re.findall(r'<a\s+id="([^"]+)"\s*>',text)
        if len(explicit)!=len(set(explicit)):errors.append(f'Duplicate explicit anchors: {p}')
    link_count=0
    for p,text in texts.items():
        # Drop fenced code for link scanning.
        clean=re.sub(r'```.*?```','',text,flags=re.S)
        for m in re.finditer(r'\[[^\]\n]+\]\(([^)\n]+)\)',clean):
            target=unquote(m.group(1))
            if re.match(r'^[a-zA-Z][\w+.-]*:',target):continue
            base,sep,fragment=target.partition('#')
            dest=(p.parent/base).resolve() if base else p
            link_count+=1
            if not dest.exists():
                errors.append(f'Missing local link: {p.relative_to(ROOT)} -> {target}')
                continue
            if sep and fragment:
                target_text=texts.get(dest)
                if target_text is not None:
                    explicit=set(re.findall(r'<a\s+id="([^"]+)"\s*>',target_text))
                    headings=set()
                    for heading in re.findall(r'^#{1,6}\s+(.+)$',target_text,re.M):
                        slug=re.sub(r'[^\w\s-]','',heading.lower()).strip().replace(' ','-')
                        headings.add(slug)
                    if fragment not in explicit|headings:
                        errors.append(f'Missing anchor: {p.relative_to(ROOT)} -> {target}')
    checks['local_links_checked']=link_count
    parsed={}
    for p in allfiles:
        if p.suffix=='.json':
            try:parsed[p.relative_to(ROOT).as_posix()]=json.loads(p.read_text(encoding='utf-8'))
            except (UnicodeDecodeError,json.JSONDecodeError) as e:errors.append(f'JSON parse: {p}: {e}')
    checks['json_files_parsed']=len(parsed)
    for p in allfiles:
        if p.suffix=='.py':
            try:compile(p.read_text(encoding='utf-8'),str(p),'exec')
            except (SyntaxError,UnicodeDecodeError) as e:errors.append(f'Python syntax: {p}: {e}')
    reqs=parsed['data/requirements.json']['requirements']
    tests=parsed['data/test_catalog.json']['tests']
    issues=parsed['data/open_issues.json']['issues']
    decisions=parsed['data/open_issues.json']['decisions']
    params=parsed['data/parameters.json']['parameters']
    index=parsed['data/document_index.json']
    src=(ROOT/'sources/architecture/10_Requirements_Tests.md').read_text(encoding='utf-8')
    aids=set(re.findall(r'^\| (ARCH-\d{3}) \|',src,re.M))
    tids=set(re.findall(r'^\| (T\d{2}) \|',src,re.M))
    for label,collection in [('requirements',reqs),('tests',tests),('issues',issues),('decisions',decisions),('parameters',params)]:
        ids=[x['id'] for x in collection]
        if len(ids)!=len(set(ids)):errors.append(f'Duplicate IDs: {label}')
        checks[label+'_count']=len(ids)
    covered=set(a for r in reqs for a in r['source_arch_ids'])
    if covered!=aids:errors.append(f'ARCH coverage mismatch: missing={aids-covered}, extra={covered-aids}')
    test_ids={t['id'] for t in tests}
    if not tids.issubset(test_ids):errors.append('Source tests missing')
    for r in reqs:
        if not r['requirement'].strip():errors.append(f'Empty requirement: {r["id"]}')
        if r['chapter'] not in {c['number'] for c in index['chapters']}:errors.append(f'Unknown chapter: {r["id"]}')
        if set(r['verification_ids'])-test_ids:errors.append(f'Unknown tests: {r["id"]}')
        if not r['verification_ids'] and not r['verification_review']:errors.append(f'No verification: {r["id"]}')
        if r['basis'] not in {'SOURCE_DERIVED','USER_CONTEXT_DERIVED','SYSTEM_SPEC_PROPOSAL'}:errors.append(f'Unknown basis: {r["id"]}')
        if r['requirement'] not in (ROOT/'appendices/Requirements_Catalog.md').read_text(encoding='utf-8'):
            errors.append(f'Requirement view is stale: {r["id"]}')
    for t in tests:
        expected={r['id'] for r in reqs if t['id'] in r['verification_ids']}
        if set(t['system_requirement_ids'])!=expected:errors.append(f'Test inverse mapping stale: {t["id"]}')
        if not expected:errors.append(f'Test without requirements: {t["id"]}')
    issue_ids={i['id'] for i in issues}
    for p in params:
        if p['issue_id'] not in issue_ids:errors.append(f'Unknown parameter issue: {p["id"]}')
    srcdec=(ROOT/'sources/architecture/11_Migration_Decisions.md').read_text(encoding='utf-8')
    for d in decisions:
        row=re.search(r'^\| '+re.escape(d['id'])+r' \| (.+?) \| (.+?) \|$',srcdec,re.M)
        if row is None or row.group(2)!=d['source_status']:errors.append(f'Decision status changed: {d["id"]}')
    if set(re.findall(r'^\| (TBD-\d{3}) \|',srcdec,re.M))!={i['id'] for i in issues if i['origin']=='SOURCE_INHERITED'}:
        errors.append('Source TBD coverage changed')
    checks['source_ARCH_coverage']=len(covered)
    checks['source_T_coverage']=len(tids & test_ids)
    checks['source_TBD_coverage']=sum(i['origin']=='SOURCE_INHERITED' for i in issues)
    checks['source_DEC_status_preserved']=len(decisions)
    checks['all_tests_NOT_RUN']=all(t['status']=='NOT_RUN' for t in tests)
    checks['all_requirements_DRAFT']=all(r['status']=='DRAFT_FOR_REVIEW' for r in reqs)
    checks['all_parameters_UNSET']=all(p['value'] is None for p in params)
    source_manifest=ROOT/'sources/architecture/MANIFEST_SHA256.txt'
    n=0
    for line in source_manifest.read_text(encoding='utf-8').splitlines():
        h,name=line.split('  ',1);p=source_manifest.parent/name
        if not p.is_file() or sha(p)!=h:errors.append(f'Source file changed: {name}')
        n+=1
    checks['source_manifest_verified']=n
    inputs=parsed['data/input_manifest.json']['inputs']
    input_md=next(x for x in inputs if x['filename'].endswith('.md'))
    if sha(ROOT/'sources/architecture/90_All_In_One.md')!=input_md['sha256']:
        errors.append('Source integrated MD differs from uploaded input SHA')
    checks['source_integrated_input_hash_match']=True
    # Verify immutable baseline archives and accept only explicitly logged record changes.
    changes=parsed['data/revision_changes.json']['changes']
    changes_by_key={(c['file'],c['id']):c for c in changes}
    if len(changes_by_key)!=len(changes): errors.append('Duplicate change-log keys')
    expected_changed={
        'data/requirements.json':{'SYS-GRID-001','SYS-DEPLOY-001','SYS-GSEL-001','SYS-GSEL-002','SYS-GSEL-007','SYS-GSEL-013','SYS-GSEL-017'},
        'data/test_catalog.json':{'SYS-T29','SYS-T30','SYS-T31','SYS-T33','SYS-T39'},
        'data/open_issues.json':{'SYS-TBD-003','SYS-TBD-024','SYS-TBD-026'},
        'data/external_interfaces.json':{'IF-GRID-01','IF-GRID-02','IF-GRID-03','IF-RS-01','IF-EL-01'},
    }
    observed_changes={}
    baseline=ROOT/'sources/baseline/R3.zip'
    baseline_input=next(x for x in inputs if x.get('bundled_as')=='sources/baseline/R3.zip')
    if sha(baseline)!=baseline_input['sha256']:errors.append('R3 ZIP input hash mismatch')
    current_collections={
      'data/requirements.json':('requirements',reqs),
      'data/test_catalog.json':('tests',tests),
      'data/open_issues.json':('issues',issues),
      'data/parameters.json':('parameters',params),
      'data/external_interfaces.json':('interfaces',parsed['data/external_interfaces.json']['interfaces']),
    }
    with ZipFile(baseline) as z:
        prefix='SPK-GW_HEMS_System_Spec_20261006_R3/'
        for file,(key,current_records) in current_collections.items():
            old_records=json.loads(z.read(prefix+file))[key]
            byid={x['id']:x for x in current_records};changed=set();exact=0
            for old in old_records:
                cur=byid.get(old['id'])
                if cur==old: exact+=1;continue
                changed.add(old['id'])
                log=changes_by_key.get((file,old['id']))
                if log is None or log['before']!=old or log['after']!=cur:
                    errors.append('Unlogged baseline record change: '+file+':'+old['id'])
            observed_changes[file]=changed
            if changed!=expected_changed.get(file,set()):errors.append('Unexpected changed record set: '+file)
            added=[x for x in current_records if x['id'] not in {a['id'] for a in old_records}]
            if any(x.get('introduced_revision')!='R4' for x in added):errors.append('Missing R4 addition provenance: '+file)
            checks['r3_'+key+'_exactly_preserved']=exact
            checks['r4_'+key+'_modified']=len(changed)
            checks['r4_'+key+'_added']=len(added)
        if z.testzip() is not None:errors.append('R3 nested ZIP CRC failed')
    checks['r3_input_sha256_verified']=True
    checks['r4_logged_record_changes']=len(changes)
    r1=ROOT/'sources/baseline/R1.zip'
    r1_input=next(x for x in inputs if x.get('bundled_as')=='sources/baseline/R1.zip')
    if sha(r1)!=r1_input['sha256']:errors.append('R1 archive changed')
    checks['r1_archive_hash_preserved']=True
    r2=ROOT/'sources/baseline/R2.zip'
    r2_input=next(x for x in inputs if x.get('bundled_as')=='sources/baseline/R2.zip')
    if sha(r2)!=r2_input['sha256']:errors.append('R2 archive changed')
    checks['r2_archive_hash_preserved']=True
    # Validate mode templates without enabling any real profile.
    grid=parsed['data/grid_connection_profiles.json']
    if set(grid['supported_mode_values'])!={'PCS_DIRECT','GW_MANAGED'}:errors.append('Mode definitions missing')
    if grid['default_mode'] is not None:errors.append('Implicit grid mode default is not allowed')
    if any(p['validated_for_activation'] or p['authority']['active_mode'] is not None for p in grid['profiles']):
        errors.append('Template wrongly marked deployable/active')
    checks['grid_connection_mode_templates']=len(grid['profiles'])
    overrides=parsed['data/decision_overrides.json']['decisions']
    if not any(x['id']=='R3-DEC-001' and 'DEC-004' in x.get('supersedes_current_policy',[]) for x in overrides):errors.append('Missing explicit DEC-004 policy override')
    if not any(x['id']=='R4-DEC-002' for x in overrides):errors.append('Missing R4 device eligibility override')
    if grid.get('router_required') is not True:errors.append('Home router must be mandatory')
    expected_eligibility={'ECHONET_LITE_PCS':['PCS_DIRECT'],'RS485_PCS':['GW_MANAGED']}
    actual_eligibility={x['normal_connection_class']:x['allowed_modes'] for x in grid.get('eligibility_rules',[])}
    if actual_eligibility!=expected_eligibility:errors.append('Wrong R4 eligibility matrix')
    for prof in grid['profiles']:
        for key in ('request_path','response_path'):
            if 'HOME_ROUTER' not in prof['network'].get(key,[]):errors.append('Router absent from template route')
        if prof['normal_connection_class'] not in expected_eligibility or prof['mode'] not in expected_eligibility.get(prof['normal_connection_class'],[]):errors.append('Ineligible template mode')
    checks['r4_eligibility_and_router_explicit']=True
    checks['current_policy_override_explicit']=True
    ifs=parsed['data/external_interfaces.json']['interfaces']
    if len({i['id'] for i in ifs})!=len(ifs):errors.append('Duplicate IF IDs')
    checks['interface_count']=len(ifs)
    info=parsed['package_info.json']
    for key,n in [('system_requirements',len(reqs)),('test_scenarios',len(tests)),('open_issues',len(issues)),('parameters',len(params)),('chapters',len(index['chapters'])),('external_interfaces',len(ifs))]:
        if info[key]!=n:errors.append('Package metadata mismatch: '+key)
    checks['package_counts_consistent']=True
    # R5 changes only diagram clarity; preserve the existing R4 runtime contracts exactly.
    r4=ROOT/'sources/baseline/R4.zip'
    r4_input=next(x for x in inputs if x.get('bundled_as')=='sources/baseline/R4.zip')
    if sha(r4)!=r4_input['sha256']:errors.append('R4 archive changed')
    immutable_r4=[
      'data/requirements.json','data/test_catalog.json','data/open_issues.json',
      'data/parameters.json','data/external_interfaces.json','data/grid_network_routes.json',
      'data/grid_connection_profiles.json','data/decision_overrides.json','data/revision_changes.json']
    with ZipFile(r4) as z:
        for name in immutable_r4:
            if (ROOT/name).read_bytes()!=z.read('SPK-GW_HEMS_System_Spec_20261006_R4/'+name):
                errors.append('R5 changed an R4 contract/history register: '+name)
    checks['r4_contract_registers_byte_identical']=len(immutable_r4)
    from validate_el_routes import check as check_el_routes
    el_result=check_el_routes()
    if el_result['status']!='PASS':errors.extend(el_result['errors'])
    checks['r5_el_route_diagram_validation']=el_result['status']
    checks['r5_changed_diagrams_rendered']=info.get('r5_rendered_diagrams',0)
    # Scan explicit SYS references; numeric range ends are not separate references.
    allowed_sys={r['id'] for r in reqs}|{x['id'] for x in tests}|{x['id'] for x in issues}
    for p,txt in texts.items():
        if '/sources/' in p.as_posix():continue
        for id_ in re.findall(r'\bSYS-(?:TBD-\d{3}|T\d{2}|[A-Z]+-\d{3})\b',txt):
            if id_ not in allowed_sys:errors.append(f'Unknown SYS reference in {p.name}: {id_}')
    for n in range(16,23):
        if f'### SYS-UC-{n:02d}：' not in (ROOT/'chapters/20_Northbound_Monitoring_FW.md').read_text(encoding='utf-8'):
            errors.append(f'Missing R2 usecase: SYS-UC-{n:02d}')
    checks['r2_usecases_count']=7
    for p in (ROOT/'chapters').glob('*.md'):
        nums=re.findall(r'^## (\d+\.\d+)\b',p.read_text(encoding='utf-8'),re.M)
        if len(nums)!=len(set(nums)):errors.append('Duplicate section numbers: '+p.name)
    checks['chapter_section_numbers_unique']=True
    checks['new_Mermaid_rendered']=bool(info.get('mermaid_rendered',False))

    if not skip_manifest:
        manifest=ROOT/'MANIFEST_SHA256.txt'
        if not manifest.exists():errors.append('Missing package manifest')
        else:
            listed=set()
            for line in manifest.read_text(encoding='utf-8').splitlines():
                h,name=line.split('  ',1);listed.add(name);p=ROOT/name
                if not p.is_file() or sha(p)!=h:errors.append(f'Package manifest mismatch: {name}')
            actual={p.relative_to(ROOT).as_posix() for p in allfiles if p!=manifest}
            if listed!=actual:errors.append(f'Manifest coverage mismatch: {actual-listed} / {listed-actual}')
            checks['package_manifest_verified']=len(listed)
    checks['file_count']=len(allfiles)
    checks['integrated_lines']=len((ROOT/'90_All_In_One.md').read_text(encoding='utf-8').splitlines())
    return {'status':'PASS' if not errors else 'FAIL','scope':'DOCUMENT_STRUCTURE_ONLY','checks':checks,'errors':errors}

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--refresh-manifest',action='store_true')
    ap.add_argument('--skip-manifest',action='store_true')
    args=ap.parse_args()
    if args.refresh_manifest:refresh_manifest()
    result=run(args.skip_manifest)
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return 0 if result['status']=='PASS' else 1
if __name__=='__main__':sys.exit(main())
