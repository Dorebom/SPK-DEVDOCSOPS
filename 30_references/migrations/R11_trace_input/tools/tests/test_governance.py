"""Synthetic fixtures only. No test actor, budget or effort is a business record."""
import copy, datetime, json, shutil, sys, tempfile, unittest
from pathlib import Path
import yaml
TOOLS=Path(__file__).resolve().parents[1];ROOT=TOOLS.parent
sys.path.insert(0,str(TOOLS))
from common import jread,jwrite,sha_file,tree_hash,FlowError
from govcheck import validate,report,new_task,frontmatter,GovernanceError,CONTROL,TASKS

class GovernanceTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(prefix='spkgw-gov-test-');self.w=Path(self.tmp.name)
        # Copy small working scope plus selected frozen canonical; no test mutates distribution.
        for d in ['00_governance','10_canonical','20_work/drafts/project','20_work/analysis/project','tools']:
            shutil.copytree(ROOT/d,self.w/d,ignore=shutil.ignore_patterns('__pycache__','*.pyc','reports'))
        p=self.w/'30_references/decisions/CTX-R10-GOV.md';p.parent.mkdir(parents=True);shutil.copy2(ROOT/'30_references/decisions/CTX-R10-GOV.md',p)
        self.c=jread(self.w/CONTROL)
        self.ids=sorted(frontmatter(p)['task_id']for p in (self.w/TASKS).glob('*.md'))
        self.tid=self.ids[0];self.pointer=(self.w/'10_canonical/CURRENT.json').read_bytes();self.canhash=tree_hash(self.w/'10_canonical/releases/BL-R9-0001')
    def tearDown(self):self.tmp.cleanup()
    def save(self):jwrite(self.w/CONTROL,self.c)
    def task(self,tid=None,**updates):
        p=self.w/TASKS/((tid or self.tid)+'.md');t=frontmatter(p);t.update(updates)
        p.write_text('---\n'+yaml.safe_dump(t,allow_unicode=True,sort_keys=False).strip()+'\n---\n\n# Synthetic task\n\n## Open Questions\n\nSynthetic only.\n',encoding='utf-8');return t
    def check(self):self.save();return validate(self.w,'2026-10-08')
    def fail(self,pattern):
        self.save()
        with self.assertRaisesRegex(GovernanceError,pattern):validate(self.w,'2026-10-08')
    def evidence(self):
        p=self.w/'20_work/analysis/project/evidence/SYNTHETIC.txt';p.parent.mkdir(parents=True,exist_ok=True);p.write_text('Synthetic evidence only.')
        self.c['evidence']=[{'id':'EVD-TEST-001','path':p.relative_to(self.w).as_posix(),'sha256':sha_file(p),'description':'Synthetic only','run_id':None}]
        self.c['actors']=[{'id':'ACT-TEST-HUMAN','name':'SYNTHETIC REVIEWER','kind':'HUMAN','responsibilities':['TEST_ONLY']},{'id':'ACT-TEST-AI','name':'SYNTHETIC AI','kind':'AI','responsibilities':['TEST_ONLY']}]
        self.c['decisions']=[{'id':'DEC-TEST-WORK','actor_id':'ACT-TEST-HUMAN','decision':'AUTHORIZE_TEST_WORK','scope':'SYNTHETIC_ONLY','decided_at':'2026-10-08T10:00:00+09:00','evidence_id':'EVD-TEST-001'}]
    def active(self,**extra):
        self.evidence();return self.task(state='IN_PROGRESS',owner='ACT-TEST-HUMAN',assignees=['ACT-TEST-AI'],reviewers=['ACT-TEST-HUMAN'],estimate_hours=2,remaining_hours=1,approval_refs=['DEC-TEST-WORK'],**extra)
    def done(self):
        self.active();self.task(state='DONE',remaining_hours=0,evidence_ids=['EVD-TEST-001'],acceptance={'decision':'ACCEPT','actor_id':'ACT-TEST-HUMAN','accepted_at':'2026-10-08T11:00:00+09:00','evidence_ids':['EVD-TEST-001']})
    def money(self):
        self.evidence();self.c['cost_basis']={'currency':'JPY','tax_basis':'EXCLUSIVE'}
        self.c['budget']={'id':'BUD-TEST-001','approval':{'actor_id':'ACT-TEST-HUMAN','approved_at':'2026-10-08T09:00:00+09:00','evidence_id':'EVD-TEST-001'},'currency':'JPY','tax_basis':'EXCLUSIVE','amount':'1000','scope':'SYNTHETIC_ONLY'}
        self.c['costs']=[{'id':'CST-TEST-001','task_id':self.tid,'incurred_on':'2026-10-08','amount':'100','currency':'JPY','tax_basis':'EXCLUSIVE','category':'TEST_ONLY','source_key':'SYNTHETIC-INV-1-L1','evidence_id':'EVD-TEST-001','commitment_id':'COM-TEST-001','reverses_id':None}]
        self.c['commitments']=[{'id':'COM-TEST-001','task_id':self.tid,'amount':'300','currency':'JPY','tax_basis':'EXCLUSIVE','evidence_id':'EVD-TEST-001','committed_on':'2026-10-08'}]
        self.c['forecasts']=[{'id':f'FCT-TEST-{i:03d}','task_id':tid,'as_of':'2026-10-08','etc_amount':'400'if tid==self.tid else '0','currency':'JPY','tax_basis':'EXCLUSIVE','includes_open_commitments':True,'basis':'SYNTHETIC_ONLY'}for i,tid in enumerate(self.ids)]
        self.c['actuals_complete_through']='2026-10-08';self.c['actuals_confirmation']={'actor_id':'ACT-TEST-HUMAN','evidence_id':'EVD-TEST-001'}
    def test_01_initial_state_is_incomplete_not_approved(self):
        v,ts,c,o=self.check();r=report(self.w,'2026-10-08')
        self.assertEqual(v['result'],'PASS');self.assertIsNone(r['weighted_accepted_progress']);self.assertIsNone(r['EAC']);self.assertIsNone(r['BAC']);self.assertFalse(r['actuals_complete']);self.assertEqual(r['task_states']['PROPOSED'],4)
    def test_02_duplicate_yaml_key(self):
        p=self.w/TASKS/(self.tid+'.md');p.write_text(p.read_text().replace('project: SPK-GW_HEMS','project: SPK-GW_HEMS\nproject: X'))
        self.fail('Duplicate YAML')
    def test_03_empty_title(self):self.task(title=' ');self.fail('frontmatter|task:')
    def test_04_wrong_state_type(self):self.task(state=123);self.fail('task:')
    def test_05_unknown_trace(self):self.task(trace_id='TRC-UNKNOWN');self.fail('Unknown task trace')
    def test_06_unknown_requirement(self):self.task(linked_ids=['SYS-NOT-FOUND']);self.fail('Unknown linked_id')
    def test_07_duplicate_task(self):
        shutil.copy2(self.w/TASKS/(self.tid+'.md'),self.w/TASKS/'duplicate.md');self.fail('Duplicate task')
    def test_08_dependency_cycle(self):
        self.task(depends_on=[self.ids[1]]);self.task(self.ids[1],depends_on=[self.tid]);self.fail('Cycle')
    def test_09_missing_dependency(self):self.task(depends_on=['TASK-MISSING']);self.fail('Unknown dependency')
    def test_10_ready_without_owner(self):self.task(state='READY');self.fail('Active task requires')
    def test_11_active_without_estimate(self):self.active();self.task(estimate_hours=None);self.fail('estimates missing')
    def test_12_active_without_authorization(self):self.active();self.task(approval_refs=[]);self.fail('authorization')
    def test_13_ready_unfinished_dependency(self):self.active();self.task(depends_on=[self.ids[1]]);self.fail('Unfinished dependency')
    def test_14_done_no_evidence(self):self.active();self.task(state='DONE',remaining_hours=0);self.fail('DONE requires')
    def test_15_done_remaining_work(self):self.done();self.task(remaining_hours=1);self.fail('DONE has remaining')
    def test_16_done_ai_acceptance(self):
        self.done();self.task(reviewers=['ACT-TEST-AI'],acceptance={'decision':'ACCEPT','actor_id':'ACT-TEST-AI','accepted_at':'2026-10-08T11:00:00+09:00','evidence_ids':['EVD-TEST-001']});self.fail('Human accountability')
    def test_17_done_with_evidence_and_review(self):self.done();self.assertEqual(self.check()[0]['result'],'PASS')
    def test_18_hash_tampering(self):
        self.done();(self.w/self.c['evidence'][0]['path']).write_text('modified');self.fail('Evidence hash')
    def test_19_path_escape(self):
        self.evidence();self.c['evidence'][0]['path']='../../secret';self.save()
        with self.assertRaises(FlowError):validate(self.w,'2026-10-08')
    def test_20_blocker_contract(self):self.active();self.task(state='BLOCKED');self.fail('BLOCKED')
    def test_21_cancel_without_decision(self):self.task(state='CANCELLED');self.fail('CANCELLED')
    def test_22_summary_not_counted_in_cost(self):self.money();self.task(summary=True);self.fail('summary task')
    def test_23_budget_doublecount_avoided(self):
        self.money();self.save();r=report(self.w,'2026-10-08');self.assertEqual(r['recorded_AC'],'100');self.assertEqual(r['outstanding_commitments'],'200');self.assertEqual(r['EAC'],'500');self.assertEqual(r['VAC'],'500')
    def test_24_etc_below_commitment(self):self.money();self.c['forecasts'][0]['etc_amount']='199';self.fail('ETC below')
    def test_25_duplicate_invoice(self):self.money();x=copy.deepcopy(self.c['costs'][0]);x['id']='CST-TEST-002';self.c['costs'].append(x);self.fail('Duplicate cost source')
    def test_26_mixed_currency(self):self.money();self.c['costs'][0]['currency']='USD';self.fail('currency')
    def test_27_mixed_tax(self):self.money();self.c['costs'][0]['tax_basis']='INCLUSIVE';self.fail('tax')
    def test_28_decimal_no_float_artifact(self):
        self.money();self.c['costs'][0]['amount']='0.1';self.c['commitments'][0]['amount']='0.3';self.c['forecasts'][0]['etc_amount']='0.2';self.save();self.assertEqual(report(self.w,'2026-10-08')['EAC'],'0.3')
    def test_29_unconfirmed_actuals_no_eac(self):self.money();self.c['actuals_complete_through']=None;self.save();self.assertIsNone(report(self.w,'2026-10-08')['EAC'])
    def test_30_missing_forecast_no_eac(self):self.money();self.c['forecasts'].pop();self.save();self.assertIsNone(report(self.w,'2026-10-08')['EAC'])
    def test_31_future_cost(self):self.money();self.c['costs'][0]['incurred_on']='2026-10-09';self.fail('Future cost')
    def test_32_ai_time_not_human_effort(self):
        self.evidence();self.c['effort']=[{'id':'EFF-TEST-001','task_id':self.tid,'actor_id':'ACT-TEST-AI','worked_on':'2026-10-08','hours':'2','source_key':'TEST-ONLY','evidence_id':'EVD-TEST-001'}];self.fail('not human labor')
    def test_33_duplicate_effort(self):
        self.evidence();r={'id':'EFF-TEST-001','task_id':self.tid,'actor_id':'ACT-TEST-HUMAN','worked_on':'2026-10-08','hours':'2','source_key':'TEST-ONLY','evidence_id':'EVD-TEST-001'};self.c['effort']=[r,{**r,'id':'EFF-TEST-002'}];self.fail('Duplicate effort')
    def test_34_reversal_no_doublecount(self):
        self.money();o=self.c['costs'][0];self.c['costs'].append({**o,'id':'CST-TEST-REVERSE','amount':'-100','source_key':'TEST-CREDIT','reverses_id':o['id']});self.save();r=report(self.w,'2026-10-08');self.assertEqual(r['recorded_AC'],'0');self.assertEqual(r['outstanding_commitments'],'300')
    def test_35_negative_cost_requires_source(self):self.money();self.c['costs'][0]['amount']='-100';self.fail('reverses_id')
    def test_36_progress_fixed_denominator(self):
        self.done();self.c['plan']={'id':'PLN-TEST-001','approval':{'actor_id':'ACT-TEST-HUMAN','approved_at':'2026-10-08T09:00:00+09:00','evidence_id':'EVD-TEST-001'},'lines':[{'task_id':self.tid,'weight_hours':2,'kind':'DISCRETE','start_on':'2026-10-01','finish_on':'2026-10-08'},{'task_id':self.ids[1],'weight_hours':6,'kind':'DISCRETE','start_on':'2026-10-01','finish_on':'2026-10-15'}]};self.save();self.assertEqual(report(self.w,'2026-10-08')['weighted_accepted_progress'],'0.25')
        self.task(self.ids[1],estimate_hours=100);self.save();self.assertEqual(report(self.w,'2026-10-08')['weighted_accepted_progress'],'0.25')
    def test_37_extend_tasks_without_fixed_count(self):
        new_task(self.w,'Synthetic added task','TRC-SPKGW-000001','WBS-SPKGW-BOOT');self.assertEqual(validate(self.w)[0]['tasks'],5)
    def test_38_current_unchanged(self):
        self.check();report(self.w,'2026-10-08');self.assertEqual(self.pointer,(self.w/'10_canonical/CURRENT.json').read_bytes());self.assertEqual(self.canhash,tree_hash(self.w/'10_canonical/releases/BL-R9-0001'))
    def test_39_run_reverse_link(self):
        self.evidence();self.c['runs']=[{'id':'EXE-TEST-001','task_id':self.tid,'trace_id':'TRC-SPKGW-000001','actor_id':'ACT-TEST-AI','role':'EXECUTION','started_at':'2026-10-08T10:00:00+09:00','finished_at':'2026-10-08T10:05:00+09:00','input_baseline':'BL-R9-0001','result':'PASS','evidence_ids':['EVD-TEST-001']}];self.fail('reverse task')
    def test_40_actual_confirmation_required(self):self.money();self.c['actuals_confirmation']=None;self.fail('completeness needs')
    def test_41_wbs_cycle(self):self.c['work_packages'][0]['parent_id']='WBS-SPKGW-BOOT';self.fail('Cycle')
    def test_42_invalid_date(self):self.task(updated_on='2026-15-40');self.fail('task:')
    def test_43_unknown_actor(self):self.task(owner='ACT-UNKNOWN');self.fail('Unknown owner')
    def test_44_commitment_overrun(self):self.money();self.c['costs'][0]['amount']='301';self.fail('Commitment overrun')

if __name__=='__main__':unittest.main()
