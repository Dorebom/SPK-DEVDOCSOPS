"""Synthetic document/item separation tests. No synthetic product records are adopted."""
import copy,hashlib,json,shutil,sys,tempfile,unittest
from pathlib import Path
TOOLS=Path(__file__).resolve().parents[1];ROOT=TOOLS.parent;sys.path.insert(0,str(TOOLS))
from common import FlowError
from tracecheck import validate,report,subject_hash,impact
from identitytrace import resolve,document_report

class IdentityTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(prefix='idtrace-tests-');self.w=Path(self.tmp.name)
        for rel in ['00_governance/lifecycle_profile.json','00_governance/schemas/lifecycle-trace.schema.json','00_governance/schemas/lifecycle-trace-v1.schema.json']:
            p=self.w/rel;p.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(ROOT/rel,p)
        self.thread='THR-SPKGW-TEST-000001';self.actor='ACT-TEST-HUMAN'
        self.write('20_work/analysis/project/control.json',{'traces':[{'id':self.thread}],'actors':[{'id':self.actor,'kind':'HUMAN'}]})
        profile=json.loads((self.w/'00_governance/lifecycle_profile.json').read_text())
        self.g={'schema':'spkgw.lifecycle-trace/v2','registry_scope':'SYNTHETIC_ONLY','profiles':[{'thread_id':self.thread,'assessment_scope':'SYNTHETIC_ONLY','root_node_ids':[],'phase_plan':[{'phase_id':p['id'],'applicability':'TBD','required_kinds':[],'rationale':None,'review':None}for p in profile['phases']]}],'documents':[],'nodes':[],'edges':[],'document_edges':[],'trace_relations':[]}
        self.d1=self.doc('DTR-SPKGW-SPEC-000001','spec.json',{'records':[{'id':'REQ-TEST-A','text':'A'},{'id':'REQ-TEST-B','text':'B'}]})
        self.d2=self.doc('DTR-SPKGW-SPEC-000002','test.json',{'records':[{'id':'TEST-CASE-A','text':'test A'}]})
        self.a=self.node('ITR-SPKGW-REQ-000001','REQ-TEST-A',self.d1,0,'REQUIREMENT',['REQSPEC'])
        self.b=self.node('ITR-SPKGW-REQ-000002','REQ-TEST-B',self.d1,1,'REQUIREMENT',['REQSPEC'])
        self.t=self.node('ITR-SPKGW-UT-000001','TEST-CASE-A',self.d2,0,'TEST_CASE',['UT'])
        self.g['edges'].append({'edge_id':'LINK-TEST-001','from_node':self.t['node_id'],'to_node':self.a['node_id'],'relation':'verifies','active':True,'basis':'SYNTHETIC_ONLY','review':None})
        self.save()
    def tearDown(self):self.tmp.cleanup()
    def write(self,rel,obj):
        p=self.w/rel;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(obj,ensure_ascii=False,indent=2));return p
    def doc(self,id,name,content):
        p=self.write('20_work/analysis/project/'+name,content)
        d={'document_trace_id':id,'document_version_id':id+'_V_1','document_id':'DOC-'+name.replace('.','-'),'revision':'1','title':'Synthetic '+name,'kind':'REGISTER','path':p.relative_to(self.w).as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'source_ids':[],'representation':'IMMUTABLE_REFERENCE','origin_status':'TEST_ONLY'}
        self.g['documents'].append(d);return d
    def node(self,id,native,doc,index,kind,phases):
        n={'node_id':id+'_V_1','item_trace_id':id,'artifact_id':id,'revision':'1','kind':kind,'title':'Synthetic '+native,'thread_id':self.thread,'related_thread_ids':[],'phase_ids':phases,'phase_basis':'EXPLICIT','record_state':'RECORDED','selected':True,'document_version_id':doc['document_version_id'],'native_ids':[native],'reference_document_version_ids':[],'locator':{'path':doc['path'],'sha256':doc['sha256'],'selector':f'json:/records/{index}/id'},'occurrences':[],'review':None}
        self.g['nodes'].append(n);return n
    def save(self):self.write('20_work/analysis/project/trace_graph.json',self.g)
    def check(self):self.save();return validate(self.w)[0]
    def fail(self,pattern):
        self.save()
        with self.assertRaisesRegex(FlowError,pattern):validate(self.w)
    def test_01_one_document_contains_two_distinct_items(self):
        c=self.check();self.assertEqual(c['identity_check']['documents'],2);self.assertEqual(c['identity_check']['items'],3)
    def test_02_document_id_is_not_item_id(self):
        self.a['item_trace_id']=self.d1['document_trace_id'];self.fail('Schema|identity')
    def test_03_item_id_is_not_document_id(self):
        self.d1['document_trace_id']=self.a['item_trace_id'];self.fail('Schema|TraceID')
    def test_04_unknown_document(self):
        self.a['document_version_id']='UNKNOWN';self.fail('containing document')
    def test_05_exact_locator_required(self):
        self.a['locator'].pop('selector');self.fail('exact selector')
    def test_06_wrong_document_path(self):
        self.a['locator']['path']=self.d2['path'];self.fail('containing document version')
    def test_07_wrong_native_id_selector(self):
        self.a['locator']['selector']='json:/records/1/id';self.fail('Native item ID')
    def test_08_no_document_to_item_verifies_shortcut(self):
        self.g['edges'][0]['from_node']=self.d2['document_version_id'];self.fail('document endpoint')
    def test_09_citation_is_not_verification(self):
        self.g['document_edges']=[{'edge_id':'DE-TEST','from_document':self.d2['document_version_id'],'to_document':self.d1['document_version_id'],'relation':'references','basis':'SYNTHETIC_ONLY'}]
        self.save();r=report(self.w,self.thread);self.assertFalse(r['record_chain_ready']);self.assertEqual(self.check()['identity_check']['document_edges'],1)
    def test_10_unknown_reference_document(self):
        self.a['reference_document_version_ids']=['DTR-NOT-FOUND'];self.fail('reference document')
    def test_11_duplicate_document_version(self):
        self.g['documents'].append(copy.deepcopy(self.d1));self.fail('Duplicate document_version_id')
    def test_12_duplicate_current_native_item(self):
        self.b['native_ids']=self.a['native_ids'];self.b['locator']=copy.deepcopy(self.a['locator']);self.fail('Native alias')
    def test_13_ordinal_phase_not_current(self):
        self.a['phase_ids']=['P03'];self.fail('Schema|phase')
    def test_14_unknown_phase(self):
        self.a['phase_ids']=['WHATEVER'];self.fail('Schema|phase')
    def test_15_document_hash_change_detected(self):
        (self.w/self.d1['path']).write_text('changed');self.fail('Document hash')
    def test_16_no_floating_document_version(self):
        self.d1['revision']='latest';self.fail('Floating document')
    def test_17_no_floating_item_version(self):
        self.a['revision']='HEAD';self.fail('Floating revision')
    def test_18_one_item_moves_to_new_document_keeps_identity(self):
        d=self.doc('DTR-SPKGW-SPEC-000003','moved.json',{'records':[{'id':'REQ-TEST-A','text':'A'}]})
        self.a['selected']=False;n=copy.deepcopy(self.a);n.update(node_id=self.a['item_trace_id']+'_V_2',revision='2',selected=True,document_version_id=d['document_version_id'],locator={'path':d['path'],'sha256':d['sha256'],'selector':'json:/records/0/id'})
        self.g['nodes'].append(n)
        c=self.check();self.assertEqual(c['identity_check']['items'],3);self.assertEqual(c['identity_check']['item_versions'],4)
    def test_19_two_selected_versions_rejected(self):
        n=copy.deepcopy(self.a);n.update(node_id=self.a['item_trace_id']+'_V_2',revision='2');self.g['nodes'].append(n);self.fail('Multiple selected')
    def test_20_document_report_not_whole_document_verified(self):
        r=document_report(self.g,self.d1['document_trace_id']);self.assertEqual(len(r['items']),2);self.assertFalse(r['whole_document_verified'])
    def test_21_native_lookup(self):
        r=resolve(self.g,{},'REQ-TEST-A','item');self.assertEqual(r['matches'][0]['id'],self.a['item_trace_id']);self.assertFalse(r['auto_selected'])
    def test_22_unknown_lookup_no_fake_identity(self):
        self.assertEqual(resolve(self.g,{},'NO-SUCH-ID')['result'],'NOT_FOUND')
    def test_23_thread_alias_resolves_as_thread_only(self):
        r=resolve(self.g,{'thread_aliases':{'TRC-OLD':self.thread}},'TRC-OLD');self.assertEqual([x['namespace']for x in r['matches']],['thread'])
    def test_24_parent_document_rename_not_item_rename(self):
        p=self.w/self.d1['path'];q=p.with_name('renamed.json');p.rename(q);self.d1['path']=q.relative_to(self.w).as_posix()
        for n in [self.a,self.b]:n['locator']['path']=self.d1['path']
        self.assertEqual(self.check()['identity_check']['items'],3)
    def test_25_many_phases_do_not_clone_an_item(self):
        self.a['phase_ids']=['REQSPEC','IMPL','UT','OPS'];self.assertEqual(self.check()['identity_check']['items'],3)
    def test_26_new_view_has_same_item_id(self):
        d=self.doc('DTR-SPKGW-SPEC-000003','view.md',{})
        p=self.w/d['path'];p.write_text('<a id="req-a"></a>\n# View');d['sha256']=hashlib.sha256(p.read_bytes()).hexdigest()
        self.a['occurrences']=[{'document_version_id':d['document_version_id'],'selector':'anchor:req-a','role':'VIEW'}]
        self.assertEqual(self.check()['identity_check']['items'],3)
    def test_27_missing_view_anchor(self):
        self.a['occurrences']=[{'document_version_id':self.d2['document_version_id'],'selector':'anchor:missing','role':'VIEW'}];self.fail('anchor missing')
    def test_28_unverified_office_selector_rejected(self):
        self.a['locator']['selector']='xlsx:Sheet1!A1';self.fail('Unsupported selector')
    def test_29_subject_review_invalidates_after_change(self):
        p=self.write('20_work/analysis/project/review.json',{'note':'SYNTHETIC_ONLY'})
        rev={'state':'CONFIRMED','reviewer':self.actor,'reviewed_at':'2026-10-08T11:00:00+09:00','evidence':{'path':p.relative_to(self.w).as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()},'rationale':'Synthetic review','subject_sha256':subject_hash(self.a)}
        self.a['review']=rev;self.assertEqual(self.check()['result'],'PASS');self.a['title']='changed';self.fail('subject hash mismatch')
    def test_30_impact_targets_only_related_item(self):
        self.save();r=impact(self.w,self.a['node_id']);self.assertEqual([x['node_id']for x in r['review_candidates']],[self.t['node_id']]);self.assertNotIn(self.b['node_id'],str(r))
    def test_31_readonly_queries(self):
        before={str(p):hashlib.sha256(p.read_bytes()).hexdigest()for p in self.w.rglob('*')if p.is_file()}
        validate(self.w);report(self.w,self.thread);resolve(self.g,{},'REQ-TEST-A');document_report(self.g,self.d1['document_trace_id'])
        after={str(p):hashlib.sha256(p.read_bytes()).hexdigest()for p in self.w.rglob('*')if p.is_file()};self.assertEqual(before,after)
    def test_32_changed_source_native_alias_rejected(self):
        n=copy.deepcopy(self.a);n.update(node_id=self.a['item_trace_id']+'_V_2',revision='2',selected=False,native_ids=['REQ-TEST-B'],locator=copy.deepcopy(self.b['locator']));self.g['nodes'].append(n);self.fail('Native identity changed')
    def test_33_document_relation_cannot_target_item(self):
        self.g['document_edges']=[{'edge_id':'DE-TEST','from_document':self.d1['document_version_id'],'to_document':self.a['node_id'],'relation':'references','basis':'SYNTHETIC_ONLY'}];self.fail('Document edge')
    def test_34_unassigned_is_not_a_guessed_phase(self):
        self.a['phase_basis']='UNASSIGNED';self.fail('UNASSIGNED item')
    def test_35_duplicate_document_path_rejected(self):
        d=copy.deepcopy(self.d1);d.update(document_trace_id='DTR-SPKGW-SPEC-000009',document_version_id='DTR-SPKGW-SPEC-000009_V_1');self.g['documents'].append(d);self.fail('path registered twice')

if __name__=='__main__':unittest.main()
