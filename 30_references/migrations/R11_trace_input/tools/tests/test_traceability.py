"""Synthetic lifecycle records only; never imported into operational ledgers."""
import copy,json,shutil,sys,tempfile,unittest,hashlib
from pathlib import Path
TOOLS=Path(__file__).resolve().parents[1];ROOT=TOOLS.parent
sys.path.insert(0,str(TOOLS))
from tracecheck import validate,report,impact,TraceError,GRAPH,subject_hash
from common import FlowError
from govcheck import lifecycle_meta,GovernanceError

class TraceTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(prefix='trace-r11-test-');self.w=Path(self.tmp.name)
        for rel in ['00_governance/lifecycle_profile.json','00_governance/schemas/lifecycle-trace.schema.json']:
            p=self.w/rel;p.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(ROOT/rel,p)
        self.c={'traces':[{'id':'TRC-TEST-A'},{'id':'TRC-TEST-B'}],'actors':[{'id':'ACT-TEST-HUMAN','kind':'HUMAN'}]}
        p=self.w/'20_work/analysis/project/control.json';p.parent.mkdir(parents=True);p.write_text(json.dumps(self.c))
        self.proof=self.file('20_work/analysis/project/SYNTHETIC_EVIDENCE.txt','SYNTHETIC_REVIEW_ONLY')
        self.review={'state':'CONFIRMED','reviewer':'ACT-TEST-HUMAN','reviewed_at':'2026-10-08T10:00:00+09:00','evidence':self.proof,'rationale':'Synthetic confirmation, not project evidence','subject_sha256':None}
        self.d={'schema':'spkgw.lifecycle-trace/v1','profiles':[{'trace_id':'TRC-TEST-A','assessment_scope':'SYNTHETIC_TEST_ONLY','root_node_ids':['NODE-P01'],'phase_plan':[]}],'nodes':[],'edges':[],'trace_relations':[]}
        profile=json.loads((self.w/'00_governance/lifecycle_profile.json').read_text())
        for phase in profile['phases']:
            id=phase['id'];kind=phase['example_artifact_kind'];self.node('NODE-'+id,'ART-'+id,kind,[id])
            needed=[kind]
            if id in ['P09','P10','P11','P12']:needed+=['TEST_CASE']
            if id=='P15':needed+=['RELEASE']
            self.d['profiles'][0]['phase_plan'].append({'phase_id':id,'applicability':'APPLICABLE','required_kinds':needed,'rationale':'Synthetic full example','review':None})
        for i in range(2,9):self.edge(f'NODE-P{i:02d}',f'NODE-P{i-1:02d}','implements'if i==8 else 'derives_from')
        for i in range(9,13):
            phase=f'P{i:02d}';case='CASE-'+phase;self.node(case,'ART-'+case,'TEST_CASE',[phase]);self.edge(case,'NODE-P03','verifies');self.edge('NODE-'+phase,case,'result_of');self.edge('NODE-'+phase,'NODE-P08','evidence_for')
        self.edge('NODE-P13','NODE-P01','validates');self.edge('NODE-P13','NODE-P12','derives_from')
        self.edge('NODE-P14','NODE-P13','derives_from');self.node('REL-TEST','ART-REL','RELEASE',['P15'])
        self.edge('REL-TEST','NODE-P08','includes');self.edge('REL-TEST','NODE-P14','includes')
        self.edge('NODE-P15','REL-TEST','deployment_of');self.edge('NODE-P16','NODE-P15','observed_in');self.edge('NODE-P17','NODE-P16','derives_from')
        self.save()
    def tearDown(self):self.tmp.cleanup()
    def file(self,rel,text):
        p=self.w/rel;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text,encoding='utf-8')
        return {'path':rel,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
    def node(self,nid,aid,kind,phases,trace='TRC-TEST-A',related=None):
        n={'node_id':nid,'artifact_id':aid,'revision':'1.0.0','kind':kind,'title':'SYNTHETIC '+aid,'trace_id':trace,'related_trace_ids':related or [],'phase_ids':phases,'record_state':'RECORDED','selected':True,'locator':self.file('20_work/analysis/project/examples/'+nid+'.txt',nid),'review':copy.deepcopy(self.review)}
        n['review']['subject_sha256']=subject_hash(n);self.d['nodes'].append(n);return n
    def edge(self,a,b,kind='derives_from'):
        e={'edge_id':'EDGE-%03d'%len(self.d['edges']),'from_node':a,'to_node':b,'relation':kind,'active':True,'basis':'Synthetic link only','review':copy.deepcopy(self.review)}
        e['review']['subject_sha256']=subject_hash(e);self.d['edges'].append(e);return e
    def save(self):(self.w/GRAPH).write_text(json.dumps(self.d,ensure_ascii=False,indent=2),encoding='utf-8')
    def fail(self,msg):
        self.save()
        with self.assertRaisesRegex((TraceError,FlowError),msg):validate(self.w)
    def test_01_full_17_phase_example(self):
        r=report(self.w,'TRC-TEST-A');self.assertTrue(r['record_chain_ready']);self.assertEqual(len(r['phases']),17);self.assertIsNone(r['product_progress'])
    def test_02_pending_phase_is_not_complete(self):
        self.d['profiles'][0]['phase_plan'][3]['applicability']='TBD';self.save();self.assertFalse(report(self.w,'TRC-TEST-A')['record_chain_ready'])
    def test_03_missing_phase_plan(self):self.d['profiles'][0]['phase_plan'].pop();self.fail('every configured phase')
    def test_04_duplicate_phase_plan(self):self.d['profiles'][0]['phase_plan'].append(copy.deepcopy(self.d['profiles'][0]['phase_plan'][0]));self.fail('Duplicate phase')
    def test_05_unknown_trace(self):self.d['nodes'][0]['trace_id']='TRC-MISSING';self.fail('Unknown node TraceID|Root belongs')
    def test_06_unknown_related_trace(self):self.d['nodes'][0]['related_trace_ids']=['TRC-MISSING'];self.fail('Unknown related')
    def test_07_duplicate_node(self):self.d['nodes'].append(copy.deepcopy(self.d['nodes'][0]));self.fail('Duplicate node')
    def test_08_same_artifact_revision_not_cloned(self):
        n=copy.deepcopy(self.d['nodes'][0]);n['node_id']='NODE-CLONE';self.d['nodes'].append(n);self.fail('Duplicate artifact/revision')
    def test_09_missing_endpoint(self):self.d['edges'][0]['to_node']='NODE-MISSING';self.fail('Unknown edge target')
    def test_10_unknown_relation(self):self.d['edges'][0]['relation']='AUTO_APPROVED';self.fail('Schema')
    def test_11_hash_tampering(self):
        (self.w/self.d['nodes'][0]['locator']['path']).write_text('TAMPER');self.fail('hash mismatch')
    def test_12_path_escape(self):self.d['nodes'][0]['locator']['path']='../../outside';self.fail('path|Path|escape|workspace')
    def test_13_floating_revision(self):self.d['nodes'][0]['revision']='HEAD';self.fail('Floating revision')
    def test_14_two_selected_versions(self):
        n=copy.deepcopy(self.d['nodes'][0]);n['node_id']='NODE-V2';n['revision']='2.0.0';self.d['nodes'].append(n);self.fail('Multiple selected')
    def test_15_review_unknown_actor(self):self.d['nodes'][0]['review']['reviewer']='ACT-MISSING';self.fail('Unknown reviewer')
    def test_16_no_evidence_for_confirmed(self):self.d['edges'][0]['review']['evidence']=None;self.fail('Schema')
    def test_17_na_without_decision(self):self.d['profiles'][0]['phase_plan'][0]['applicability']='NOT_APPLICABLE';self.fail('N/A requires')
    def test_18_na_with_evidence_allowed(self):
        p=self.d['profiles'][0]['phase_plan'][-1];p.update(applicability='NOT_APPLICABLE',rationale='Synthetic impact-based omission',review=copy.deepcopy(self.review));p['review']['subject_sha256']=subject_hash(p);self.save();self.assertEqual(report(self.w,'TRC-TEST-A')['phases'][-1]['record_status'],'NOT_APPLICABLE')
    def test_19_discussion_is_not_implementation(self):
        # All links remain, but only association: tagging and meetings cannot form the technical chain.
        for e in self.d['edges']:e['relation']='discusses';e['review']['subject_sha256']=subject_hash(e)
        self.save();self.assertFalse(report(self.w,'TRC-TEST-A')['record_chain_ready'])
    def test_20_meeting_cannot_be_test_case(self):
        self.d['nodes'][1]['kind']='MEETING';self.d['nodes'][1]['review']['subject_sha256']=subject_hash(self.d['nodes'][1]);self.edge('NODE-P02','NODE-P03','verifies');self.fail('verifies must')
    def test_21_planned_not_evidence(self):
        self.d['nodes'][0].update(record_state='PLANNED',locator=None);self.fail('Planned artifact')
    def test_22_derivation_cycle(self):self.edge('NODE-P01','NODE-P02');self.fail('Cycle')
    def test_23_trace_lineage_cycle(self):
        self.d['trace_relations']=[{'id':'TL-001','from_trace':'TRC-TEST-A','to_trace':'TRC-TEST-B','relation':'split_from','basis':'Synthetic'}, {'id':'TL-002','from_trace':'TRC-TEST-B','to_trace':'TRC-TEST-A','relation':'follow_up_to','basis':'Synthetic'}];self.fail('Cycle in trace')
    def test_24_shared_research_and_multi_trace_meeting(self):
        self.node('RES-SHARED','ART-RES','RESEARCH',['P04','P05'],related=['TRC-TEST-B']);self.node('MTG-SHARED','ART-MTG','MEETING',['P04','P05'],related=['TRC-TEST-B']);self.edge('RES-SHARED','NODE-P04','investigates');self.edge('MTG-SHARED','RES-SHARED','discusses');self.save();self.assertEqual(validate(self.w)[0]['nodes'],24)
    def test_25_old_revision_impact_warning(self):
        self.d['nodes'][2]['selected']=False
        n=copy.deepcopy(self.d['nodes'][2]);n.update(node_id='NODE-P03-V2',revision='2.0.0',selected=True);n['review']['subject_sha256']=subject_hash(n);self.d['nodes'].append(n);self.edge(n['node_id'],'NODE-P03','supersedes');self.save()
        r=report(self.w,'TRC-TEST-A');self.assertFalse(r['record_chain_ready']);self.assertTrue(any(w['code']=='STALE_REFERENCE'for w in r['warnings']))
    def test_26_change_impact_reaches_tests_and_deployment(self):
        r=impact(self.w,'NODE-P03');ids={x['node_id']for x in r['review_candidates']};self.assertIn('NODE-P08',ids);self.assertIn('NODE-P15',ids);self.assertIn('CASE-P09',ids)
    def test_27_report_is_read_only(self):
        before={str(p):hashlib.sha256(p.read_bytes()).hexdigest()for p in self.w.rglob('*')if p.is_file()};report(self.w,'TRC-TEST-A');after={str(p):hashlib.sha256(p.read_bytes()).hexdigest()for p in self.w.rglob('*')if p.is_file()};self.assertEqual(before,after)
    def test_28_unknown_json_pointer(self):
        l=self.file('20_work/analysis/project/example.json','{"id":"A"}');l['selector']='json:/missing';self.d['nodes'][0]['locator']=l;self.fail('JSON pointer not found')
    def test_29_explicit_anchor(self):
        l=self.file('20_work/analysis/project/example.md','<a id="req-a"></a>\n# Sample');l['selector']='anchor:req-a';self.d['nodes'][0]['locator']=l;self.d['nodes'][0]['review']['subject_sha256']=subject_hash(self.d['nodes'][0]);self.save();self.assertEqual(validate(self.w)[0]['result'],'PASS')
    def test_30_missing_review_reports_pending(self):
        self.d['nodes'][2]['review']=None;self.save();r=report(self.w,'TRC-TEST-A');self.assertFalse(r['record_chain_ready']);self.assertEqual(r['phases'][2]['record_status'],'PENDING_REVIEW')
    def test_31_lifecycle_active_needs_phase(self):
        x={'trace_contract':'spkgw.lifecycle-tags/v1','trace_id':'TRC-TEST-A','related_trace_ids':[],'phase_ids':[],'phase_scope':'UNASSIGNED','phase':'UNASSIGNED','activity_type':'MEETING'}
        with self.assertRaisesRegex(GovernanceError,'active task'):lifecycle_meta(x,{'TRC-TEST-A'},True)
    def test_32_lifecycle_cross_phase_meeting(self):
        x={'trace_contract':'spkgw.lifecycle-tags/v1','trace_id':'TRC-TEST-A','related_trace_ids':['TRC-TEST-B'],'phase_ids':['P04','P05'],'phase_scope':'CROSS_PHASE','phase':'P04','activity_type':'MEETING'}
        lifecycle_meta(x,{'TRC-TEST-A','TRC-TEST-B'},True)
    def test_33_lifecycle_primary_must_be_member(self):
        x={'trace_contract':'spkgw.lifecycle-tags/v1','trace_id':'TRC-TEST-A','related_trace_ids':[],'phase_ids':['P04'],'phase_scope':'PHASE_SPECIFIC','phase':'P05','activity_type':'RESEARCH'}
        with self.assertRaisesRegex(GovernanceError,'Primary phase'):lifecycle_meta(x,{'TRC-TEST-A'})
    def test_34_duplicate_json_key(self):
        p=self.w/GRAPH;s=p.read_text();p.write_text(s.replace('"nodes": [','"nodes": [], "nodes": [',1))
        with self.assertRaisesRegex(TraceError,'Duplicate JSON'):validate(self.w)
    def test_35_task_done_is_not_lifecycle_completion(self):
        # A TASK tagged into every phase cannot stand in for engineering outputs.
        self.d['nodes'][0]['kind']='TASK';self.d['nodes'][0]['review']['subject_sha256']=subject_hash(self.d['nodes'][0]);self.save();self.assertFalse(report(self.w,'TRC-TEST-A')['record_chain_ready'])
    def test_36_invalid_verifies_target(self):self.edge('CASE-P09','REL-TEST','verifies');self.fail('verifies target')

    def test_37_changed_node_invalidates_review(self):
        self.d['nodes'][0]['title']='Changed meaning';self.fail('subject hash mismatch')
    def test_38_changed_edge_invalidates_review(self):
        self.d['edges'][0]['basis']='Changed interpretation';self.fail('subject hash mismatch')
    def test_39_orphaned_meeting_is_reported(self):
        self.node('MTG-ORPHAN','ART-MTG','MEETING',['P04']);self.save();r=report(self.w,'TRC-TEST-A');self.assertFalse(r['record_chain_ready']);self.assertIn('MTG-ORPHAN',r['context_unconnected_nodes'])
    def test_40_context_link_does_not_replace_technical_evidence(self):
        self.node('MTG-LINKED','ART-MTG','MEETING',['P04']);self.edge('MTG-LINKED','NODE-P04','discusses');self.save();r=report(self.w,'TRC-TEST-A');self.assertTrue(r['record_chain_ready']);self.assertIn('MTG-LINKED',r['context_linked_nodes']);self.assertIn('MTG-LINKED',r['selected_unconnected_nodes'])

if __name__=='__main__':unittest.main()
