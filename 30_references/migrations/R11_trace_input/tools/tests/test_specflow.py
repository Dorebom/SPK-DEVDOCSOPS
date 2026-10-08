"""Synthetic management-tool tests. No case is a real product requirement/test.
OOXML fixtures exercise raw structural handling; they do NOT validate Office rendering.
"""
from __future__ import annotations
import copy,contextlib,io,json,shutil,sys,tempfile,unittest,zipfile
from pathlib import Path
TOOLS=Path(__file__).resolve().parents[1];WORKSPACE=TOOLS.parent
sys.path.insert(0,str(TOOLS))
from common import *
from validate_model import validate
from view_renderer import render
from extract_sources import extract
from specflow import register,extract_source,review_fragment,new_draft,add_candidate,decide,apply_record,prepare,publish,compare_runs,audit_baseline,record_dir,draft_path,import_coverage

class WorkflowTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(prefix='spkgw-r9-test-');self.w=Path(self.temp.name)
        # Regression fixture is the distributed initial R9, NOT future user-edited CURRENT.
        for d in ['00_governance','schemas','tools']:
            shutil.copytree(WORKSPACE/d,self.w/d,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
        snap='10_canonical/releases/BL-R9-0001'
        shutil.copytree(WORKSPACE/snap,self.w/snap)
        receipt='10_canonical/receipts/BL-R9-0001.json';(self.w/receipt).parent.mkdir(parents=True);shutil.copy2(WORKSPACE/receipt,self.w/receipt)
        r=jread(self.w/receipt)
        jwrite(self.w/'10_canonical/CURRENT.json',{'schema':'spkgw.current-baseline/v1','baseline_id':'BL-R9-0001','path':snap,'tree_sha256':r['selected_tree_sha256'],'receipt':receipt,'content_status':'DRAFT_FOR_REVIEW','product_requirements_approved':False})
        originals='30_references/baselines/R8_FIX001';shutil.copytree(WORKSPACE/originals,self.w/originals)
        registry=jread(self.w/snap/'data/source_bindings.json')
        for record in registry['sources']:
            p=Path(record['path']);dest=self.w/p;dest.parent.mkdir(parents=True,exist_ok=True)
            if not dest.exists():shutil.copy2(WORKSPACE/p,dest)
        jwrite(self.w/'30_references/source_register.json',registry)
        (self.w/'20_work/drafts').mkdir(parents=True);(self.w/'20_work/analysis').mkdir(parents=True)
        self.base,self.meta=current(self.w)
        self.pointer=(self.w/'10_canonical/CURRENT.json').read_bytes();self.basehash=tree_hash(self.base)
    def tearDown(self):self.temp.cleanup()
    def draft(self,id='DR-TEST'):
        new_draft(self.w,id);return draft_path(self.w,id)
    def unchanged(self):
        self.assertEqual(self.pointer,(self.w/'10_canonical/CURRENT.json').read_bytes());self.assertEqual(self.basehash,tree_hash(self.base))
    def quiet_prepare(self,id='DR-TEST',**kw):return prepare(self.w,id,**kw)
    def approval(self,id='DR-TEST'):
        a=jread(self.w/'20_work/analysis/approvals'/(id+'.request.json'))
        a.update(decision='APPROVE_DOCUMENT_BASELINE',approved_by='SYNTHETIC_REVIEWER',approved_at='2026-10-08T00:00:00Z',rationale='Synthetic test only, not product approval')
        p=self.w/'20_work/analysis/approvals'/(id+'.approval.json');jwrite(p,a);return p
    def source(self,text='試験用原文。製品仕様ではない。',revision='1.0',document_id='SYNTHETIC'):
        p=self.w/('source-'+revision+'.txt');p.write_text(text,encoding='utf-8')
        s=register(self.w,p,document_id,revision,'AS_IS')['source'];rr=extract_source(self.w,s['source_id']);run=jread(self.w/'20_work/analysis/imports'/rr['run_id']/'extraction.json')
        return s,run
    def adopted_record(self,id='DR-TEST'):
        d=self.draft(id);s,run=self.source();f=run['fragments'][0]
        review_fragment(self.w,run['run_id'],f['fragment_id'],'SYNTHETIC_REVIEWER','Test fixture text compared; no real product source')
        add_candidate(self.w,id,'CAND-TEST',run['run_id'],[f['fragment_id']],'SYS',['SYS-IMPORT-001'],f['raw_text'],'ADDITION',{'basis':'AS_IS','product':'SYNTHETIC_ONLY'})
        decide(self.w,id,'CAND-TEST','ADOPT','SYNTHETIC_DECIDER','Synthetic management test')
        row=copy.deepcopy(jread(d/'data/requirements.json')['requirements'][0]);row.update(id='SYS-IMPORT-001',title='合成テストのみ',requirement=f['raw_text'],source_ids=[s['source_id']],source_arch_ids=[],basis='SOURCE_EXTRACTED')
        row.pop('source_requirement_text',None);p=self.w/'test_record.json';jwrite(p,row)
        apply_record(self.w,id,'CAND-TEST',p)
        return d,s,run
    def check_no_fresh(self,d):return validate(d,self.w,freshness=False,links=False)
    def test_01_baseline_integrity_and_freshness(self):
        self.assertEqual('PASS',audit_baseline(self.w)['result']);self.assertEqual(124,validate(self.base,self.w)['counts']['requirements']);self.unchanged()
    def test_02_empty_requirement_rejected(self):
        d=self.draft();x=jread(d/'data/requirements.json');x['requirements'][0]['requirement']=' ';jwrite(d/'data/requirements.json',x)
        with self.assertRaises(FlowError):self.check_no_fresh(d)
        self.unchanged()
    def test_03_wrong_status_type_rejected(self):
        d=self.draft();x=jread(d/'data/requirements.json');x['requirements'][0]['status']=12345;jwrite(d/'data/requirements.json',x)
        with self.assertRaises(FlowError):self.check_no_fresh(d)
    def test_04_duplicate_ids_rejected_before_render(self):
        d=self.draft();x=jread(d/'data/requirements.json');x['requirements'].append(copy.deepcopy(x['requirements'][0]));jwrite(d/'data/requirements.json',x)
        with self.assertRaisesRegex(FlowError,'duplicate'):self.check_no_fresh(d)
    def test_05_unknown_source_rejected(self):
        d=self.draft();x=jread(d/'data/requirements.json');x['requirements'][0]['source_ids']=['NO-SOURCE'];jwrite(d/'data/requirements.json',x)
        with self.assertRaisesRegex(FlowError,'source'):self.check_no_fresh(d)
    def test_06_unknown_usdm_rejected(self):
        d=self.draft();x=jread(d/'data/requirements.json');x['requirements'][0]['usdm_id']='USDM-NOT-FOUND';jwrite(d/'data/requirements.json',x)
        with self.assertRaisesRegex(FlowError,'USDM'):self.check_no_fresh(d)
    def test_07_requirement_test_asymmetry_rejected(self):
        d=self.draft();x=jread(d/'data/requirements.json');x['requirements'][0]['verification_ids']=['T01'];jwrite(d/'data/requirements.json',x)
        with self.assertRaisesRegex(FlowError,'reverse links'):self.check_no_fresh(d)
    def test_08_stale_views_rejected(self):
        d=self.draft();x=jread(d/'data/requirements.json');x['requirements'][0]['requirement']+=' 合成差分。';jwrite(d/'data/requirements.json',x)
        with self.assertRaisesRegex(FlowError,'STALE_VIEWS'):validate(d,self.w,freshness=True)
    def test_09_input_failure_never_changes_canonical(self):
        d=self.draft();x=jread(d/'data/function_catalog.json');x['gw_functions'][0].pop('name');jwrite(d/'data/function_catalog.json',x)
        # OQ is edited but will never reach a selected partial JSON index.
        q=jread(d/'data/open_question_bindings.json')['questions'][0];p=d/q['owner_note'];p.write_text(p.read_text().replace('**回答：** 未記入','**回答：** 合成回答',1))
        with self.assertRaises(FlowError):self.quiet_prepare()
        self.unchanged()
    def test_10_staged_render_failure_never_changes_canonical(self):
        self.draft()
        with self.assertRaisesRegex(FlowError,'Injected'):self.quiet_prepare(fail_at='after-render')
        self.unchanged();self.assertEqual([],list((self.w/'20_work/drafts').glob('PREP-*')))
    def test_11_pending_approval_rejected(self):
        self.draft();self.quiet_prepare()
        with self.assertRaises(FlowError):publish(self.w,'DR-TEST',self.w/'20_work/analysis/approvals/DR-TEST.request.json')
        self.unchanged()
    def test_12_publish_and_idempotent_republication(self):
        self.draft();self.quiet_prepare();a=self.approval();r=publish(self.w,'DR-TEST',a)
        self.assertEqual('PUBLISHED_DOCUMENT_BASELINE',r['result']);self.assertEqual(self.basehash,tree_hash(self.base));self.assertEqual('ALREADY_SELECTED',publish(self.w,'DR-TEST',a)['result'])
    def test_13_failure_before_pointer_retains_selected_baseline(self):
        self.draft();self.quiet_prepare();a=self.approval()
        with self.assertRaisesRegex(FlowError,'Injected'):publish(self.w,'DR-TEST',a,fail_at='before-pointer')
        self.unchanged();self.assertEqual('PUBLISHED_DOCUMENT_BASELINE',publish(self.w,'DR-TEST',a)['result'])
    def test_14_prepared_tampering_rejected(self):
        self.draft();p=self.quiet_prepare();a=self.approval();path=self.w/p['prepared_path']/'data/requirements.json';path.write_text(path.read_text()+' ')
        with self.assertRaisesRegex(FlowError,'changed'):publish(self.w,'DR-TEST',a)
        self.unchanged()
    def test_15_wrong_approval_hash_rejected(self):
        self.draft();self.quiet_prepare();a=self.approval();x=jread(a);x['prepared_sha256']='0'*64;jwrite(a,x)
        with self.assertRaisesRegex(FlowError,'mismatch'):publish(self.w,'DR-TEST',a)
        self.unchanged()
    def test_16_stale_parent_baseline_rejected(self):
        self.draft('DR-A');self.draft('DR-B');prepare(self.w,'DR-A');prepare(self.w,'DR-B')
        aa=self.approval('DR-A');bb=self.approval('DR-B');publish(self.w,'DR-B',bb)
        # Identical prepared trees can select the same hash; add a distinct authored change for A.
        # Each build records a draft fingerprint, but with equal drafts trees may match; both outcomes are safe.
        pa=jread(record_dir(self.w)/'DR-A.prepared.json');pb=jread(record_dir(self.w)/'DR-B.prepared.json')
        if pa['prepared_sha256']==pb['prepared_sha256']:
            self.assertEqual('ALREADY_SELECTED',publish(self.w,'DR-A',aa)['result'])
        else:
            with self.assertRaisesRegex(FlowError,'STALE_BASE'):publish(self.w,'DR-A',aa)
        with self.assertRaisesRegex(FlowError,'STALE_BASE'):prepare(self.w,'DR-A')
    def test_17_original_tampering_detected(self):
        p=self.w/'30_references/baselines/R8_FIX001/00_MOC.md';p.write_text(p.read_text()+'bad')
        with self.assertRaises(FlowError):audit_baseline(self.w)
    def test_18_registration_and_extraction_idempotence(self):
        s,r=self.source();p=self.w/'source-1.0.txt';a=register(self.w,p,'SYNTHETIC','1.0','AS_IS');b=extract_source(self.w,s['source_id'])
        self.assertEqual('ALREADY_REGISTERED',a['result']);self.assertEqual('ALREADY_EXTRACTED',b['result']);self.unchanged()
    def test_19_old_binary_format_is_blocked(self):
        p=self.w/'synthetic.doc';p.write_bytes(b'old-binary-placeholder');s=register(self.w,p,'OLD-TEST','1')['source'];r=extract_source(self.w,s['source_id'])
        self.assertEqual('BLOCKED_MANUAL',r['status']);self.assertEqual(0,r['fragments']);self.unchanged()
    def test_20_docx_nested_table_revision_and_image_inventory(self):
        p=self.w/'synthetic.docx'
        doc='''<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body><w:p><w:pPr><w:pStyle w:val="Heading1"/></w:pPr><w:r><w:t>試験見出し</w:t></w:r></w:p><w:tbl><w:tr><w:tc><w:p><w:r><w:t>外側</w:t></w:r></w:p><w:tbl><w:tr><w:tc><w:p><w:del><w:r><w:delText>旧テスト</w:delText></w:r></w:del><w:ins><w:r><w:t>新テスト</w:t></w:r></w:ins></w:p></w:tc></w:tr></w:tbl></w:tc></w:tr></w:tbl></w:body></w:document>'''
        with zipfile.ZipFile(p,'w')as z:z.writestr('word/document.xml',doc);z.writestr('word/media/image1.bin',b'SYNTHETIC')
        s=register(self.w,p,'DOCX-TEST','1')['source'];run=extract(p,s)
        found=next(f for f in run['fragments']if '旧テスト' in f['raw_text'])
        self.assertIn('新テスト',found['raw_text']);self.assertIn('TRACKED_DELETION',found['features']);self.assertGreater(found['locator']['xml_path'].count('/tbl['),1)
        self.assertTrue(any(o['kind']=='IMAGE_OR_EMBEDDED_OBJECT'for o in run['unhandled_objects']))
    def test_21_xlsx_formula_cache_hidden_merge_comments(self):
        p=self.w/'synthetic.xlsx'
        parts={
        'xl/workbook.xml':'''<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><sheets><sheet name="試験" sheetId="1" state="hidden" r:id="rId1"/></sheets></workbook>''',
        'xl/_rels/workbook.xml.rels':'''<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Target="worksheets/sheet1.xml"/></Relationships>''',
        'xl/worksheets/sheet1.xml':'''<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"><sheetData><row r="1"><c r="A1" t="inlineStr"><is><t>試験ヘッダ</t></is></c></row><row r="2" hidden="1"><c r="A2"><f>1+1</f><v>2</v></c></row></sheetData><mergeCells><mergeCell ref="A1:B1"/></mergeCells></worksheet>''',
        'xl/comments1.xml':'''<comments xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"><commentList><comment ref="A2" authorId="0"><text><t>試験注記</t></text></comment></commentList></comments>'''}
        with zipfile.ZipFile(p,'w') as z:
            for k,v in parts.items():z.writestr(k,v)
        before=sha_file(p);s=register(self.w,p,'XLSX-TEST','1')['source'];run=extract(p,s)
        f=next(f for f in run['fragments']if f['context'].get('formula'))
        self.assertEqual('1+1',f['context']['formula']['text']);self.assertEqual('2',f['context']['cached_value']);self.assertIn('HIDDEN_CONTENT',f['features']);self.assertTrue(any('MERGED_CELL'in f['features']for f in run['fragments']));self.assertTrue(any('試験注記'in f['raw_text']for f in run['fragments']));self.assertEqual(before,sha_file(p))
    def test_22_unsafe_zip_path_rejected(self):
        p=self.w/'bad.docx'
        with zipfile.ZipFile(p,'w')as z:z.writestr('../evil.txt','x');z.writestr('word/document.xml','<x/>')
        s=register(self.w,p,'BAD-ZIP','1')['source']
        with self.assertRaisesRegex(FlowError,'Unsafe'):extract(p,s)
    def test_23_dtd_rejected(self):
        p=self.w/'bad.docx'
        with zipfile.ZipFile(p,'w')as z:z.writestr('word/document.xml','<!DOCTYPE x [<!ENTITY t "x">]><x/>')
        s=register(self.w,p,'BAD-XML','1')['source']
        with self.assertRaisesRegex(FlowError,'Unsafe'):extract(p,s)
    def test_24_unresolved_conflict_cannot_be_adopted(self):
        self.draft();s,run=self.source();f=run['fragments'][0]
        add_candidate(self.w,'DR-TEST','CAND-X',run['run_id'],[f['fragment_id']],'SYS',['SYS-IMPORT-001'],'試験矛盾','CONFLICT',{'product':'SYNTHETIC'})
        with self.assertRaisesRegex(FlowError,'Resolve'):decide(self.w,'DR-TEST','CAND-X','ADOPT','TEST','TEST')
        self.unchanged()
    def test_25_unreviewed_fragment_cannot_be_applied(self):
        d=self.draft();s,run=self.source();f=run['fragments'][0]
        add_candidate(self.w,'DR-TEST','CAND-X',run['run_id'],[f['fragment_id']],'SYS',['SYS-IMPORT-001'],'試験','ADDITION',{'product':'SYNTHETIC'});decide(self.w,'DR-TEST','CAND-X','ADOPT','TEST','TEST')
        row=copy.deepcopy(jread(d/'data/requirements.json')['requirements'][0]);row.update(id='SYS-IMPORT-001',source_ids=[s['source_id']]);p=self.w/'row.json';jwrite(p,row)
        with self.assertRaises((OSError,FlowError)):apply_record(self.w,'DR-TEST','CAND-X',p)
        self.unchanged()
    def test_26_125th_requirement_end_to_end(self):
        d,s,run=self.adopted_record();p=self.quiet_prepare();self.assertEqual(125,p['counts']['requirements'])
        a=self.approval();publish(self.w,'DR-TEST',a);new,m=current(self.w)
        self.assertIn('125件',(new/'appendices/Requirements_Catalog.md').read_text());self.assertEqual(1,validate(new,self.w)['counts']['import_bindings']);self.assertEqual(self.basehash,tree_hash(self.base))
    def test_27_unbound_addition_cannot_prepare(self):
        d=self.draft();x=jread(d/'data/requirements.json');r=copy.deepcopy(x['requirements'][0]);r['id']='SYS-UNBOUND';x['requirements'].append(r);jwrite(d/'data/requirements.json',x)
        with self.assertRaisesRegex(FlowError,'needs source'):self.quiet_prepare()
        self.unchanged()
    def test_28_deleting_old_id_is_rejected(self):
        d=self.draft();x=jread(d/'data/requirements.json');x['requirements'].pop();jwrite(d/'data/requirements.json',x)
        with self.assertRaisesRegex(FlowError,'silently delete'):self.quiet_prepare()
    def test_29_usdm_unknown_reason_not_approved(self):
        d=self.draft();u=jread(self.w/'templates/usdm.example.json') if (self.w/'templates/usdm.example.json').exists() else {'id':'USDM-X','kind':'REQUIREMENT','text':'試験','reason':{'text':None,'state':'UNKNOWN','fragment_ids':[],'confirmed_by':None},'parent_ids':[],'source_fragment_ids':[],'applicability':'SYNTHETIC','status':'DRAFT_FOR_REVIEW','approved_by':None,'approval_record':None}
        u.update(status='APPROVED',approved_by='TEST',approval_record='TEST');x=jread(d/'data/usdm.json');x['elements']=[u];jwrite(d/'data/usdm.json',x)
        with self.assertRaisesRegex(FlowError,'rationale'):self.check_no_fresh(d)
    def test_30_usdm_cycle_rejected(self):
        d=self.draft();u={'id':'USDM-A','kind':'REQUIREMENT','text':'試験','reason':{'text':None,'state':'UNKNOWN','fragment_ids':[],'confirmed_by':None},'parent_ids':['USDM-B'],'source_fragment_ids':[],'applicability':'SYNTHETIC','status':'DRAFT_FOR_REVIEW','approved_by':None,'approval_record':None};v=copy.deepcopy(u);v.update(id='USDM-B',parent_ids=['USDM-A']);x=jread(d/'data/usdm.json');x['elements']=[u,v];jwrite(d/'data/usdm.json',x)
        with self.assertRaisesRegex(FlowError,'cycle'):self.check_no_fresh(d)
    def test_31_bad_typed_endpoint_rejected(self):
        d=self.draft();x=jread(d/'data/trace_links.json');x['links']=[{'id':'TRACE-X','from':{'kind':'SYS','id':'SYS-RESP-001','revision':None},'to':{'kind':'USDM','id':'USDM-MISSING','revision':None},'relation':'SATISFIES','state':'UNREVIEWED','basis':'test','reviewed_by':None}];jwrite(d/'data/trace_links.json',x)
        with self.assertRaisesRegex(FlowError,'endpoint'):self.check_no_fresh(d)
    def test_32_new_function_groups_have_no_fixed_count(self):
        d=self.draft();x=jread(d/'data/function_catalog.json');s=copy.deepcopy(x['system_functions'][0]);g=copy.deepcopy(x['gw_functions'][0]);s.update(id='S-FN-999',gw_function_ids=['GW-FN-999']);g.update(id='GW-FN-999',parent_system_function_ids=['S-FN-999']);x['system_functions'].append(s);x['gw_functions'].append(g);jwrite(d/'data/function_catalog.json',x)
        with contextlib.redirect_stdout(io.StringIO()):render(d,self.w)
        r=validate(d,self.w);self.assertEqual(22,r['counts']['system_functions']);self.assertEqual(33,r['counts']['gw_functions'])
    def test_33_new_interface_parameter_and_test_no_fixed_count(self):
        d=self.draft()
        for name,key,newid in [('external_interfaces','interfaces','IF-TEST-99'),('parameters','parameters','PAR-TEST-99')]:
            x=jread(d/'data'/f'{name}.json');r=copy.deepcopy(x[key][0]);r['id']=newid;x[key].append(r);jwrite(d/'data'/f'{name}.json',x)
        x=jread(d/'data/test_catalog.json');t=copy.deepcopy(x['tests'][0]);t.update(id='SYS-T99',system_requirement_ids=[]);x['tests'].append(t);jwrite(d/'data/test_catalog.json',x)
        with contextlib.redirect_stdout(io.StringIO()):render(d,self.w)
        self.assertEqual(70,validate(d,self.w)['counts']['tests'])
    def test_34_new_oq_id_is_not_r6_bound(self):
        d=self.draft();qs=jread(d/'data/completion_items.json');q=copy.deepcopy(qs['items'][-1]);q.update(id='SLOT-TEST-001',question_id='OQ-TEST-001',question_anchor='oq-test-001',section_anchor='slot-test-001');qs['items'].append(q);jwrite(d/'data/completion_items.json',qs)
        bs=jread(d/'data/open_question_bindings.json');bs['questions'].append({'id':'OQ-TEST-001','owner_note':q['note'],'slot_anchor':'slot-test-001','anchor':'oq-test-001'});jwrite(d/'data/open_question_bindings.json',bs)
        p=d/q['note'];t=p.read_text().replace('<a id="open-questions"></a>','<a id="slot-test-001"></a>\n## 合成追加項目\n\nTest only.\n\n<a id="open-questions"></a>',1)
        t+='\n<a id="oq-test-001"></a>\n### OQ-TEST-001 — 合成質問\n\n**対象項：** [SLOT-TEST-001](#slot-test-001)。状態：**OPEN**。\n\n**質問：** 合成確認か。\n\n**必要資料・完了条件：** テスト記録。\n\n**決定担当：** 未割当（候補：TEST）。承認者：未定。\n\n**確定時点：** TEST。回答期限：未定。\n\n**回答：** 未記入。**決定記録：** 未記入。\n';p.write_text(t)
        with contextlib.redirect_stdout(io.StringIO()):render(d,self.w)
        self.assertEqual(92,validate(d,self.w)['counts']['questions'])
    def test_35_compare_revision_detects_move_not_auto_delete(self):
        s,a=self.source('A unique\nB unique','1.0');s,b=self.source('NEW\nA unique\nB unique','2.0');r=compare_runs(self.w,a['run_id'],b['run_id'])
        self.assertEqual(2,len(r['moved_exact_text_candidates']));self.assertEqual([],r['removed_candidates']);self.unchanged()
    def test_36_approved_binding_text_tampering_rejected(self):
        d,s,run=self.adopted_record();x=jread(d/'data/requirements.json');x['requirements'][-1]['requirement']='unreviewed change';jwrite(d/'data/requirements.json',x)
        with self.assertRaisesRegex(FlowError,'reviewed record'):self.check_no_fresh(d)
    def test_37_selected_snapshot_direct_edit_detected(self):
        p=self.base/'data/requirements.json';p.write_text(p.read_text()+' ')
        with self.assertRaisesRegex(FlowError,'modified'):current(self.w)
    def test_38_duplicate_json_key_rejected(self):
        p=self.w/'bad.json';p.write_text('{"a":1,"a":2}')
        with self.assertRaisesRegex(FlowError,'Duplicate JSON'):jread(p)
    def test_39_path_traversal_draft_rejected(self):
        with self.assertRaises(FlowError):new_draft(self.w,'../BAD')
    def test_40_tool_change_invalidates_approval(self):
        self.draft();self.quiet_prepare();a=self.approval();p=self.w/'schemas/requirements.schema.json';p.write_text(p.read_text()+' ')
        with self.assertRaisesRegex(FlowError,'Tools/schema changed'):publish(self.w,'DR-TEST',a)
        self.unchanged()

    def test_41_fragment_text_tampering_rejected(self):
        d,s,run=self.adopted_record();x=jread(d/'data/import_provenance.json');x['fragments'][0]['raw_text']='TAMPERED ORIGINAL';jwrite(d/'data/import_provenance.json',x)
        with self.assertRaisesRegex(FlowError,'raw text/locator'):self.check_no_fresh(d)
    def test_42_coverage_distinguishes_unclassified_and_selected(self):
        d,s,run=self.adopted_record();r=import_coverage(self.w,run['run_id']);self.assertEqual(1,r['counts']['DECISION_RECORDED'])
        self.quiet_prepare();publish(self.w,'DR-TEST',self.approval());r=import_coverage(self.w,run['run_id']);self.assertEqual(1,r['counts']['SELECTED_CANONICAL'])
        s,run2=self.source('UNCLASSIFIED ONLY','2.0');r=import_coverage(self.w,run2['run_id']);self.assertEqual(1,r['counts']['NOT_CLASSIFIED'])
    def test_43_delete_oq_is_blocked_by_change_gate(self):
        d=self.draft();x=jread(d/'data/completion_items.json');x['items'].pop();jwrite(d/'data/completion_items.json',x)
        with self.assertRaisesRegex(FlowError,'Stable IDs removed'):self.quiet_prepare()
        self.unchanged()
    def test_44_preparation_diff_lists_all_modified_files(self):
        d=self.draft();p=d/'chapters/I_System/I-01_Purpose_Scope.md';p.write_text(p.read_text().replace('## Open Questions','合成テスト注記。\n\n## Open Questions',1))
        self.quiet_prepare();diff=jread(record_dir(self.w)/'DR-TEST.diff.json')
        self.assertTrue(any(x['path']=='chapters/I_System/I-01_Purpose_Scope.md'for x in diff['files']))
        self.unchanged()
    def test_45_usdm_many_to_many_draft_roundtrip(self):
        d=self.draft();s,run=self.source();f=run['fragments'][0]
        review_fragment(self.w,run['run_id'],f['fragment_id'],'SYNTHETIC_REVIEWER','Synthetic source compared')
        for n,kind in [(1,'REQUIREMENT'),(2,'REQUIREMENT'),(3,'SPECIFICATION')]:
            uid='USDM-TEST-'+str(n);cid='CAND-USDM-'+str(n)
            add_candidate(self.w,'DR-TEST',cid,run['run_id'],[f['fragment_id']],'USDM',[uid],'合成USDM候補','ADDITION',{'product':'SYNTHETIC_ONLY'})
            decide(self.w,'DR-TEST',cid,'ADOPT','SYNTHETIC_REVIEWER','Draft model test, rationale unknown')
            e={'id':uid,'kind':kind,'text':'合成テスト。製品要求ではない。','reason':{'text':None,'state':'UNKNOWN','fragment_ids':[],'confirmed_by':None},'parent_ids':[] if n<3 else ['USDM-TEST-1','USDM-TEST-2'],'source_fragment_ids':[f['fragment_id']],'applicability':'SYNTHETIC_ONLY','status':'DRAFT_FOR_REVIEW','approved_by':None,'approval_record':None}
            p=self.w/f'usdm-{n}.json';jwrite(p,e);apply_record(self.w,'DR-TEST',cid,p)
        ls=[]
        for n in [1,2]:ls.append({'id':'TRACE-TEST-'+str(n),'from':{'kind':'USDM','id':'USDM-TEST-3','revision':None},'to':{'kind':'USDM','id':'USDM-TEST-'+str(n),'revision':None},'relation':'SATISFIES','state':'UNREVIEWED','basis':'SYNTHETIC_ONLY','reviewed_by':None})
        jwrite(d/'data/trace_links.json',{'schema':'spkgw.trace-links/v1','links':ls})
        original=jread(d/'data/usdm.json');p=self.quiet_prepare();self.assertEqual(3,p['counts']['usdm_elements']);self.assertEqual(2,p['counts']['typed_links']);publish(self.w,'DR-TEST',self.approval());c,_=current(self.w)
        self.assertEqual(original,jread(c/'data/usdm.json'));self.assertTrue(all(e['reason']['text'] is None for e in original['elements']));self.assertEqual('NOT_CLAIMED',original['official_schema_adoption'])

    def test_46_legacy_source_alias_identity_checked(self):
        p=self.w/'30_references/source_register.json';x=jread(p);a=next(s for s in x['sources']if s['source_id']=='A01');b=next(s for s in x['sources']if s['source_id']=='A02')
        self.assertEqual('01_Architecture.md',Path(a['path']).name)
        for k in ['path','sha256','bytes']:a[k]=b[k]
        jwrite(p,x)
        with self.assertRaisesRegex(FlowError,'alias'):self.check_no_fresh(self.base)

    def test_47_moc_cannot_redirect_current_view_to_history(self):
        d=self.draft();p=d/'00_MOC.md';p.write_text(p.read_text().replace('[統合閲覧版](90_All_In_One.md)','[統合閲覧版](../../../30_references/baselines/R8_FIX001/90_All_In_One.md)'))
        with self.assertRaisesRegex(FlowError,'MOC integrated view'):self.check_no_fresh(d)

if __name__=='__main__':unittest.main()
