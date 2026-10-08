#!/usr/bin/env python3
"""Validate R6 document completion coverage; no product or network testing.

--refresh-manifest writes the measured QA report and regenerates the manifest.
Without the flag regenerated content must be identical and manifest hashes are checked.
Uses markdown-it-py when available for link parsing; stdlib fallback is provided.
"""
from __future__ import annotations
import argparse
import collections
import hashlib
import importlib.util
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
OQ_MARK = '<!-- R6:OPEN_QUESTIONS -->'
ITEM_MARK = '<!-- R6:COMPLETION_ITEMS -->'


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load(rel: str) -> dict:
    return json.loads((ROOT/rel).read_text(encoding='utf-8'))


def current_md() -> list[Path]:
    return sorted(p for p in ROOT.rglob('*.md') if 'sources' not in p.relative_to(ROOT).parts)


def files_for_manifest() -> list[Path]:
    return sorted(p for p in ROOT.rglob('*') if p.is_file() and p.relative_to(ROOT).as_posix()!='MANIFEST_SHA256.txt' and '__pycache__' not in p.parts)


def all_tokens(tokens):
    for token in tokens:
        yield token
        if token.children:
            yield from all_tokens(token.children)


def anchors_of(text: str) -> set[str]:
    explicit=set(re.findall(r'<a\s+id="([^"]+)"',text))
    counts=collections.Counter()
    for h in re.findall(r'^#{1,6}\s+(.+)$', text, re.M):
        h=re.sub(r'\[([^\]]+)\]\([^)]*\)',r'\1',h)
        slug=re.sub(r'[^\w\-\s]', '', h.strip().lower(),flags=re.U).replace(' ','-')
        n=counts[slug];counts[slug]+=1
        explicit.add(slug if n==0 else f'{slug}-{n}')
    return explicit


def check() -> dict:
    errors=[];checks={}
    docs=current_md()
    checks['current_markdown_notes']=len(docs)
    for p in docs:
        t=p.read_text(encoding='utf-8')
        heads=re.findall(r'^## (.+)$',t,re.M)
        if not heads or not heads[-1].startswith('Open Questions'):
            errors.append('Question section not at note tail: '+str(p.relative_to(ROOT)))
        if '\ufffd' in t: errors.append('Replacement character: '+str(p.relative_to(ROOT)))
    checks['all_current_notes_end_with_open_questions']=not any('Question section' in x for x in errors)
    index=load('data/document_index.json')
    items=load('data/completion_items.json')['items']
    sections=load('data/completion_section_map.json')['sections']
    qrows=load('data/open_questions_r6.json')['questions']
    cov=load('data/coverage_completion_map.json')['coverage']
    checks.update(chapters=len(index['chapters']),appendices=len(index['appendices']),completion_items=len(items),open_questions=len(qrows),coverage_rows=len(cov))
    qids=[x['question_id'] for x in items]
    sids=[x['id'] for x in items]
    if len(set(qids))!=len(qids) or len(set(sids))!=len(sids):errors.append('Duplicate canonical item/question ID')
    if {c['number'] for c in index['chapters']} != set(range(1,28)):errors.append('Unexpected chapter numbers')
    if {x['id'] for x in cov} != {f'C{i:02d}' for i in range(1,35)}:errors.append('Coverage observations missing')
    if any(not x['completion_items'] or not x['question_ids'] for x in cov):errors.append('Coverage row lacks items or questions')
    if any(x['r6_status']!='STRUCTURE_PRESENT_CONTENT_OPEN' for x in cov):errors.append('Coverage closure claimed')
    allowed_statuses={'OPEN','ANSWERED','DECISION_PENDING','CLOSED','NOT_APPLICABLE'}
    checks['question_status_counts']=dict(collections.Counter(x['status'] for x in items))
    for x in items:
        if x['status'] not in allowed_statuses:errors.append('Unknown question status: '+x['question_id'])
        if x['status'] in {'CLOSED','NOT_APPLICABLE'} and not all(x.get(k) for k in ['answer','approver','decision_record']):
            errors.append('Question closure lacks answer/approval/decision record: '+x['question_id'])
    # Every item is a real numbered subheading, and every Q is defined in its owning chapter tail.
    section_by={x['id']:x for x in sections}
    for x in items:
        t=(ROOT/x['note']).read_text(encoding='utf-8')
        if t.count(f'<a id="{x["id"].lower()}"></a>') !=1:errors.append('Item anchor missing/duplicated: '+x['id'])
        if t.count(f'<a id="{x["question_id"].lower()}"></a>') !=1:errors.append('Question anchor missing/duplicated: '+x['question_id'])
        sn=section_by[x['id']]['section']
        if f'### {sn} {x["title"]}' not in t:errors.append('Subsection heading missing: '+x['id'])
        tail=t.split(OQ_MARK)[-1]
        if x['question'] not in tail or x['closure'] not in tail:errors.append('Concrete question/closure absent: '+x['question_id'])
        if not x['fields'] or not x['question'] or not x['closure'] or not x['impact']:errors.append('Empty completion content: '+x['id'])
    oldids=set()
    for fn,key in [('open_issues.json','issues'),('parameters.json','parameters')]:
        oldids |= {x['id'] for x in load('data/'+fn)[key]}
    referenced={z for x in items for z in x['related_ids']}
    if oldids-referenced:errors.append('Unmapped legacy IDs: '+','.join(sorted(oldids-referenced)))
    if referenced-oldids:errors.append('Unknown related legacy IDs: '+','.join(sorted(referenced-oldids)))
    checks['existing_TBDs_linked']=len(load('data/open_issues.json')['issues'])
    checks['existing_parameters_linked']=len(load('data/parameters.json')['parameters'])
    # All definitions exist exactly once in the integrated source view.
    allone=(ROOT/'90_All_In_One.md').read_text(encoding='utf-8')
    for q in qids:
        if allone.count(f'<a id="{q.lower()}"></a>')!=1: errors.append('Integrated question anchor missing/duplicated: '+q)
    explicit=re.findall(r'<a\s+id="([^"]+)"',allone)
    dups=[a for a,n in collections.Counter(explicit).items() if n>1]
    if dups:errors.append('Duplicate consolidated anchors: '+','.join(dups[:10]))
    # Verify immutable input and original source files against the actual R5 zip.
    baseline=ROOT/'sources/baseline/R5.zip'
    orig_count=0;diagram_count=0;record_counts={};unchanged_ch=0
    with ZipFile(baseline) as z:
        bad=z.testzip()
        if bad:errors.append('R5 archive CRC failure: '+bad)
        prefix='SPK-GW_HEMS_System_Spec_20261006_R5/'
        for name in z.namelist():
            if name.endswith('/'):continue
            rel=name[len(prefix):]
            if rel.startswith('sources/'):
                p=ROOT/rel
                if not p.exists() or p.read_bytes()!=z.read(name):errors.append('Original source changed: '+rel)
                orig_count+=1
            if rel.startswith('diagrams/') and not rel.endswith('.md'):
                if (ROOT/rel).read_bytes()!=z.read(name):errors.append('R5 figure changed: '+rel)
                diagram_count+=1
        immutable={'requirements.json':('requirements',124),'test_catalog.json':('tests',69),'open_issues.json':('issues',48),'parameters.json':('parameters',50),'external_interfaces.json':('interfaces',16)}
        for fn,(key,n) in immutable.items():
            rel='data/'+fn
            if (ROOT/rel).read_bytes()!=z.read(prefix+rel):errors.append('Baseline records changed: '+rel)
            rows=load(rel)[key]
            record_counts[fn]=len(rows)
            if len(rows)!=n:errors.append('Unexpected baseline record count: '+fn)
        for fn in ['grid_connection_profiles.json','grid_network_routes.json','echonet_normal_routes.json','decision_overrides.json']:
            if (ROOT/'data'/fn).read_bytes()!=z.read(prefix+'data/'+fn):errors.append('Network/decision contracts changed: '+fn)
        # Existing body semantic text preserved, except the explicitly logged correction.
        change=load('data/r6_document_changes.json')['changes'][0]
        for c in index['chapters']:
            if c['number']>21:continue
            rel='chapters/'+c['file']
            old=z.read(prefix+rel).decode('utf-8')
            now=(ROOT/rel).read_text().split(ITEM_MARK)[0]
            strip=lambda s:re.sub(r'^---\n.*?\n---\n','',s,count=1,flags=re.S).strip()
            old=strip(old);now=strip(now)
            if rel==change['file']:old=old.replace(change['before'],change['after'])
            if old!=now: errors.append('Unlogged pre-existing chapter text change: '+rel)
            else:unchanged_ch+=1
    checks['r5_input_sha256']=sha(baseline.read_bytes())
    checks['source_files_preserved']=orig_count
    checks['r5_diagram_assets_preserved']=diagram_count
    checks['baseline_record_counts_preserved']=record_counts
    checks['existing_chapters_preserved_except_logged_correction']=unchanged_ch
    review_sha=sha((ROOT/'sources/review/R5_Coverage_Review_A1.md').read_bytes())
    checks['review_input_sha256']=review_sha
    # Strict JSON decode of all managed data, excluding immutable source/history copies.
    js=list((ROOT/'data').glob('*.json'))+[ROOT/'package_info.json']
    for p in js:
        try:json.loads(p.read_text(encoding='utf-8'))
        except (ValueError,UnicodeError) as exc:errors.append('Bad JSON '+str(p.relative_to(ROOT))+': '+str(exc))
    checks['json_files_parsed']=len(js)
    # Real Markdown link parsing, including table links and anchors. No web access.
    try:
        from markdown_it import MarkdownIt
        md=MarkdownIt('commonmark').enable('table')
        def links(t):
            for token in all_tokens(md.parse(t)):
                if token.type=='link_open':yield token.attrGet('href')
                if token.type=='image':yield token.attrGet('src')
        checks['link_parser']='markdown-it-py'
    except ImportError:
        def links(t):
            t=re.sub(r'```.*?```','',t,flags=re.S)
            yield from re.findall(r'\[[^\]\n]+\]\(([^)\n]+)\)',t)
        checks['link_parser']='stdlib-fallback'
    linked=0;anchor_count=0;anchor_cache={}
    for p in docs:
        t=p.read_text(encoding='utf-8')
        for target in links(t):
            if not target:continue
            parts=urlsplit(target)
            if parts.scheme or parts.netloc:continue
            path=unquote(parts.path)
            dest=(p.parent/path).resolve() if path else p.resolve()
            linked+=1
            if not dest.is_relative_to(ROOT):errors.append('Link escapes package '+str(p.relative_to(ROOT))+': '+target);continue
            if not dest.exists():errors.append('Missing link '+str(p.relative_to(ROOT))+': '+target);continue
            if parts.fragment and dest.suffix=='.md':
                anchor_count+=1
                if dest not in anchor_cache:anchor_cache[dest]=anchors_of(dest.read_text(encoding='utf-8'))
                frag=unquote(parts.fragment)
                if frag not in anchor_cache[dest]:errors.append('Missing anchor '+str(p.relative_to(ROOT))+': '+target)
    checks['local_links_checked']=linked
    checks['markdown_anchor_links_checked']=anchor_count
    # R5 diagram semantics/model validators are retained and run unchanged.
    for script,outkey in [('validate_el_routes.py','el_route_document_model'),('validate_grid_selection.py','grid_connection_document_model')]:
        proc=subprocess.run([sys.executable,str(ROOT/'tools'/script)],cwd=ROOT,capture_output=True,text=True,timeout=30)
        try:obj=json.loads(proc.stdout)
        except ValueError:obj={'status':'FAIL','output':proc.stdout,'stderr':proc.stderr}
        checks[outkey]=obj.get('status','FAIL')
        if proc.returncode or obj.get('status')!='PASS':errors.append(script+' failed: '+str(obj))
    # R6 rebuild must not change any generated/current document or its source registers.
    watch=[*docs,*sorted((ROOT/'data').glob('*.json')),ROOT/'package_info.json']
    before={str(p.relative_to(ROOT)):sha(p.read_bytes()) for p in watch}
    proc=subprocess.run([sys.executable,str(ROOT/'tools/rebuild_views.py')],cwd=ROOT,capture_output=True,text=True,timeout=30)
    if proc.returncode:errors.append('Rebuild failed: '+proc.stderr)
    changed=[rel for rel,s in before.items() if sha((ROOT/rel).read_bytes())!=s]
    checks['rebuild_checked_files']=len(watch)
    checks['deterministic_rebuild']=not changed
    if changed:errors.append('Rebuild changed existing outputs: '+','.join(changed))
    return {'revision':'R6','status':'FAIL' if errors else 'PASS','scope':'DOCUMENT_STRUCTURE_AND_BASELINE_INTEGRITY_ONLY','checks':checks,'errors':errors,'system_tests':'NOT_RUN','new_rendering':'NOT_PERFORMED_R5_IMAGES_PRESERVED','external_standards_reverified':False,'product_specification_complete':False}


def refresh(result: dict) -> None:
    tail=(ROOT/'DOCUMENT_QA.md').read_text(encoding='utf-8').split(OQ_MARK,1)[-1]
    c=result['checks']
    lines=['# R6 文書QA', '', '検査日：2026-10-06。対象はR6文書・管理データ・リンク・原典保持。実機・安全・性能・セキュリティ・認証の合格を示さない。', '',
           f'**文書QA：{result["status"]}**。詳細：[data/r6_document_validation.json](data/r6_document_validation.json)。', '',
           '## 実施した検査', '', '| 項目 | 結果 |','|---|---|',
           f'| 現行MDの末尾Open Questions | {c["current_markdown_notes"]}ノート、配置確認 |',
           f'| 本編・別冊 | {c["chapters"]}章・{c["appendices"]}別冊 |',
           f'| 観点・補完項目・質問 | {c["coverage_rows"]}観点、{c["completion_items"]}項、{c["open_questions"]}件 |',
           f'| 既存未決/パラメータとの対応 | {c["existing_TBDs_linked"]} / {c["existing_parameters_linked"]} 全件対応 |',
           f'| ローカルリンク・MDアンカー | {c["local_links_checked"]}リンク・{c["markdown_anchor_links_checked"]}アンカー参照を検査 |',
           f'| 既存管理レコード | 124 SYS・69試験・48 TBD・50パラメータ・16 IFをR5とバイト比較 |',
           f'| 原典等のファイル | R5同梱のsources内 {c["source_files_preserved"]}ファイルを不変確認 |',
           f'| R5の図資産 | Mermaid/SVG/PNG {c["r5_diagram_assets_preserved"]}ファイルを不変確認。再描画なし |',
           f'| 既存章本文 | {c["existing_chapters_preserved_except_logged_correction"]}章。第4.5の記録済み補正・メタデータ・追加部分以外を不変確認 |',
           f'| 文書モデルの回帰 | EL経路 {c["el_route_document_model"]}、出力制御接続 {c["grid_connection_document_model"]} |',
           f'| 再生成 | {c["rebuild_checked_files"]}対象ファイルのハッシュが再生成前後で一致 |',
           '', '## 入力識別', '', f'R5 ZIP SHA-256：`{c["r5_input_sha256"]}`', '', f'A1レビュー SHA-256：`{c["review_input_sha256"]}`', '',
           '## 検査の限界', '',
           '34観点へ見出しと質問が対応することを検査した。全仕様値・機能採否・規範版・安全妥当性・製品保証の網羅を認定したものではない。質問はすべてOPEN。既存69システム試験はNOT_RUNのまま。JSONや文書モデルの合格を実機・JET判断と混同しない。', '',
           '原典・旧版・レビュー原本のMDはsources以下で不変のため、Open Questions追記の対象外。現行別冊の質問は正本章を参照する。既存R5の2図は描画済み入力の継承であり、今回新たに全図を描画確認していない。', '',
           '## 再検査', '', '```sh','python tools/rebuild_views.py','python tools/validate_package.py --refresh-manifest','python tools/validate_package.py','```','',
           'MANIFEST_SHA256.txtはルートmanifest自体と__pycache__を除くファイルを対象にする。ZIP CRCと外部ZIPハッシュは梱包時に別途確認する。', '']
    (ROOT/'DOCUMENT_QA.md').write_text('\n'.join(lines).rstrip()+'\n\n'+OQ_MARK+tail,encoding='utf-8')
    (ROOT/'data/r6_document_validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    rows=[f'{sha(p.read_bytes())}  {p.relative_to(ROOT).as_posix()}' for p in files_for_manifest()]
    (ROOT/'MANIFEST_SHA256.txt').write_text('\n'.join(rows)+'\n',encoding='utf-8')


def verify_manifest() -> tuple[int,list[str]]:
    errors=[];count=0;listed=set()
    for line in (ROOT/'MANIFEST_SHA256.txt').read_text().splitlines():
        if not line.strip():continue
        digest,rel=line.split('  ',1);p=ROOT/rel;count+=1;listed.add(rel)
        if not p.is_file() or sha(p.read_bytes())!=digest:errors.append('Manifest mismatch: '+rel)
    current={p.relative_to(ROOT).as_posix() for p in files_for_manifest()}
    if listed!=current:errors.append('Manifest inventory mismatch: '+str(sorted(listed^current)))
    return count,errors


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--refresh-manifest',action='store_true')
    args=parser.parse_args()
    result=check()
    if args.refresh_manifest and result['status']=='PASS':refresh(result)
    if result['status']=='PASS':
        n,errs=verify_manifest();result['manifest_entries_verified']=n;result['errors']+=errs
        if errs:result['status']='FAIL'
    print(json.dumps(result,ensure_ascii=False,indent=2))
    raise SystemExit(0 if result['status']=='PASS' else 1)

if __name__=='__main__':
    main()
