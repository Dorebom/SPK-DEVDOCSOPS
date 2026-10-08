"""Synthetic corruption checks for the R13 integration audit; not actual project approvals."""
import contextlib,copy,hashlib,json,shutil,sys,tempfile,unittest
from pathlib import Path
TOOLS=Path(__file__).resolve().parents[1];ROOT=TOOLS.parent;sys.path.insert(0,str(TOOLS))
from verify_ai_std_integration import validate,IntegrationError,AREA
class IntegrationTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.tmp=tempfile.TemporaryDirectory(prefix='r13-integration-tests-');cls.root=Path(cls.tmp.name)/'workspace'
  shutil.copytree(ROOT,cls.root,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
 @classmethod
 def tearDownClass(cls):cls.tmp.cleanup()
 @contextlib.contextmanager
 def edit(self,path,transform=None,delete=False,json_data=False):
  p=self.root/path;old=p.read_bytes()
  try:
   if delete:p.unlink()
   elif json_data:
    x=json.loads(old);transform(x);p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
   else:p.write_text(transform(old.decode()))
   yield
  finally:p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(old)
 def fail(self,code):
  with self.assertRaisesRegex(IntegrationError,code):validate(self.root)
 def source(self):return json.loads((self.root/AREA/'integration.json').read_text())['source_inventory'][0]['path']
 def test_01_current_integration(self):self.assertEqual(validate(self.root)['result'],'PASS')
 def test_02_missing_original(self):
  with self.edit(self.source(),delete=True):self.fail('SOURCE_BYTES')
 def test_03_original_tampering(self):
  with self.edit(self.source(),lambda s:s+'\nTAMPER'):self.fail('SOURCE_BYTES')
 def test_04_missing_target(self):
  with self.edit('00_governance/STD_16_Implementation_C_Yocto.md',delete=True):self.fail('TARGET_MISSING')
 def test_05_wrong_excerpt(self):
  with self.edit(AREA/'source_fragments.json',lambda x:x['fragments'][0]['segments'][0].update(quote='made up'),json_data=True):self.fail('FRAGMENT_QUOTE')
 def test_06_invalid_source_range(self):
  with self.edit(AREA/'source_fragments.json',lambda x:x['fragments'][0]['segments'][0].update(start_line=0),json_data=True):self.fail('FRAGMENT_RANGE')
 def test_07_missing_rule_anchor(self):
  with self.edit('00_governance/STD_14_Requirements_Change_Impact.md',lambda x:x.replace('id="aim-13"','id="removed"')):self.fail('RULE_ANCHOR')
 def test_08_duplicate_rule(self):
  with self.edit(AREA/'integration.json',lambda x:x['rules'].append(copy.deepcopy(x['rules'][0])),json_data=True):self.fail('RULE_INVENTORY')
 def test_09_invalid_source_document(self):
  with self.edit(AREA/'source_fragments.json',lambda x:x['fragments'][0]['segments'][0].update(document_version_id='NOT_FOUND'),json_data=True):self.fail('FRAGMENT_DTR')
 def test_10_canonical_tampering(self):
  with self.edit('10_canonical/CURRENT.json',lambda x:x+' '):self.fail('BASE_PROTECTED_CHANGED')
 def test_11_actual_task_tampering(self):
  with self.edit('20_work/drafts/project/tasks/TASK-SPKGW-000001.md',lambda x:x+'\n'):self.fail('BASE_PROTECTED_CHANGED')
 def test_12_existing_tool_tampering(self):
  with self.edit('tools/govcheck.py',lambda x:x+'\n'):self.fail('BASE_PROTECTED_CHANGED')
 def test_13_citation_is_not_implements(self):
  with self.edit('20_work/analysis/project/trace_graph.json',lambda x:x['edges'][-1].update(relation='implements'),json_data=True):self.fail('RULE_CITATION')
 def test_14_existing_item_unchanged(self):
  with self.edit('20_work/analysis/project/trace_graph.json',lambda x:x['nodes'][0].update(title='changed'),json_data=True):self.fail('OLD_ITEM_CHANGED')
 def test_15_existing_edges_unchanged(self):
  with self.edit('20_work/analysis/project/trace_graph.json',lambda x:x['edges'][0].update(basis='changed'),json_data=True):self.fail('OLD_ITEM_EDGE_CHANGED')
 def test_16_prior_document_snapshot_required(self):
  p=json.loads((self.root/'00_governance/R13_Input_Provenance.json').read_text())['old_document_versions'][0]['old_path']
  with self.edit(p,delete=True):self.fail('OLD_DOCUMENT_BYTES')
 def test_17_current_revised_document_hash_required(self):
  p=json.loads((self.root/'00_governance/R13_Input_Provenance.json').read_text())['old_document_versions'][0]['path']
  with self.edit(p,lambda x:x+'\n'):self.fail('NEW_DOCUMENT_BINDING')
 def test_18_no_old_authority_path(self):
  with self.edit('.github/copilot-instructions.md',lambda x:x+'\nwork/tickets') :self.fail('ENTRY_LEGACY_AUTHORITY')
 def test_19_no_implicit_product_approval(self):
  with self.edit(AREA/'integration.json',lambda x:x.update(product_requirements_approved=True),json_data=True):self.fail('SCOPE_OVERCLAIM')
 def test_20_previous_source_register_rows_preserved(self):
  with self.edit('30_references/source_register.json',lambda x:x['sources'][0].update(note='changed'),json_data=True):self.fail('PRIOR_SOURCE_ROW_CHANGED')
 def test_21_read_only_audit(self):
  def hashes():return {p.relative_to(self.root).as_posix():hashlib.sha256(p.read_bytes()).hexdigest()for p in self.root.rglob('*')if p.is_file()}
  before=hashes();validate(self.root);self.assertEqual(before,hashes())
if __name__=='__main__':unittest.main()
