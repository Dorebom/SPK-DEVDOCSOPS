#!/usr/bin/env python3
"""R8の章末OQを読み、機能・要求・OQ・統合ビューを再生成する。標準ライブラリのみ。"""
from __future__ import annotations
import json, os, re, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
LINK=re.compile(r'(!?\[[^\]\n]*\]\()([^\s\)]+)(\))')
def load(p: str):return json.loads((ROOT/p).read_text(encoding='utf-8'))
def write(p: str,s: str):
 path=ROOT/p;path.parent.mkdir(parents=True,exist_ok=True)
 tmp=path.with_suffix(path.suffix+'.tmp');tmp.write_text(s,encoding='utf-8',newline='\n');os.replace(tmp,path)
def save(p: str,d):write(p,json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def href(src: str,target: str,a: str='')->str:
 if src==target and a:return '#'+a
 return os.path.relpath(target,Path(src).parent).replace(os.sep,'/')+('#'+a if a else '')
def link(src: str,target: str,label: str,a: str='')->str:return f'[{label}]({href(src,target,a)})'
def adapt(text: str,source: str,target: str)->str:
 def one(m):
  d=m[2]
  if re.match(r'(https?:|mailto:|data:)',d):return m[0]
  v,_,a=d.partition('#');p=os.path.normpath(str(Path(source).parent/v)).replace(os.sep,'/') if v else source
  return m[1]+href(target,p,a)+m[3]
 return LINK.sub(one,text)
def split_oq(text: str,qid: str)->str:
 marker=f'<a id="{qid.lower()}"></a>'
 if text.count(marker)!=1:raise ValueError(f'{qid}: 正本アンカーが一意ではありません')
 body=text.split(marker,1)[1]
 return re.split(r'<a id="oq-r6-|^### 他章',body,maxsplit=1,flags=re.M)[0]
def field(body: str,label: str)->str:
 m=re.search(r'\*\*'+re.escape(label)+r'：\*\*\s*(.*?)(?=\n\n\*\*|\*\*決定記録：\*\*|$)',body,re.S)
 if not m:raise ValueError(f'OQフィールド欠落: {label}')
 return m[1].strip().removesuffix('。')
def nullish(x: str):return None if x in ('未記入','未割当','未定','') else x

def main():
 idx=load('data/document_index.json');chs={x['code']:x for x in idx['chapters']}
 qs=load('data/completion_items.json');bindings=load('data/open_question_bindings.json')['questions'];qm={x['question_id']:x for x in qs['items']}
 for b in bindings:
  q=qm[b['id']];t=(ROOT/b['owner_note']).read_text(encoding='utf-8');body=split_oq(t,b['id'])
  m=re.search(r'状態：\*\*([^*]+)\*\*',body)
  if not m:raise ValueError(f'{b["id"]}: 状態欄欠落')
  q['status']=m[1].strip();q['answer']=nullish(field(body,'回答'));q['decision_record']=nullish(field(body,'決定記録'))
  q['rendered_question']=field(body,'質問');q['rendered_closure']=field(body,'必要資料・完了条件')
  q['rendered_owner']=field(body,'決定担当');q['rendered_gate']=field(body,'確定時点')
  q['owner']=nullish(q['rendered_owner'].split('（候補：')[0].strip())
  due=re.search(r'回答期限：([^。\n]+)',q['rendered_gate']);q['due_date']=nullish(due[1].strip()) if due else q.get('due_date')
  appr=re.search(r'承認者：([^。\n]+)',q['rendered_owner']);q['approver']=nullish(appr[1].strip()) if appr else q.get('approver')
  if q['status'] in ('CLOSED','RESOLVED') and (not q['answer'] or not q['decision_record']):raise ValueError(f'{b["id"]}: 解決済みには回答と決定記録が必要です')
 save('data/completion_items.json',qs)
 # The two function chapters are projections of one catalog, not two edited copies.
 fc=load('data/function_catalog.json')
 for level,records,code in [('system',fc['system_functions'],'I-03'),('gw',fc['gw_functions'],'II-02')]:
  p=chs[code]['path'];t=(ROOT/p).read_text(encoding='utf-8')
  title='システム全体' if level=='system' else 'SPK-GW製品';n=len(records)
  s=f'## {title}の機能一覧（{n}機能群）\n\n'
  s+='| ID | 機能・要求の要約 | 実現責任／GW内担当 | 対応する機能 |\n|---|---|---|---|\n'
  def related(f):return f['gw_function_ids'] if level=='system' else f['parent_system_function_ids']
  target=chs['II-02' if level=='system' else 'I-03']['path']
  for f in records:
   s+='| '+link(p,p,f['id'],f['id'].lower())+' | **'+f['name']+'**：'+f['behavior']+' | '+f['realization_owners' if level=='system' else 'allocation']+' | '+'、'.join(link(p,target,id,id.lower()) for id in related(f))+' |\n'
  s+='\n## 機能別の適用・根拠カード\n\n'
  for f in records:
   s+=f'<a id="{f["id"].lower()}"></a>\n### {f["id"]} — {f["name"]}\n\n{f["behavior"]}\n\n'
   s+=f'**適用条件：** {f["applicability"]}\n\n**判断状態：** {f["basis"]}。採用リリース・実装確認・正式USDM対応は未確定。\n\n'
   s+='**実現責任／GW内担当：** '+f['realization_owners' if level=='system' else 'allocation']+'。\n\n'
   s+='**機能配賦：** '+' ／ '.join(link(p,target,id,id.lower()) for id in related(f))+'。\n\n'
   s+='**関連SYS要求：** '+'、'.join(link(p,'appendices/Requirements_Catalog.md',id,id.lower()) for id in f['requirement_ids'])+'。\n\n'
   s+='**詳細章：** '+' ／ '.join(link(p,n,Path(n).stem) for n in f['source_notes'])+'。\n\n'
   s+='**具体的な不足：** '+' ／ '.join(link(p,qm[id]['note'],id,id.lower()) for id in f['open_question_ids'])+'。\n\n'
  start=t.index(f'## {title}の機能一覧')
  end=t.index('<a id="open-questions"></a>',start) if level=='system' else t.index('<a id="legacy-4-10-1"></a>',start)
  write(p,t[:start]+s+t[end:])
 # Requirement prose preserves semantics, with revised navigational bindings.
 p='appendices/Requirements_Catalog.md';req=load('data/requirements.json')['requirements'];s='# システム要求カタログ — 124件\n\n要求ID・本文・適用条件・判断状態を継承する。旧章番号は履歴、新しい章は参照の配置であり、配賦する実装責任の変更ではない。\n\n'
 for r in req:
  s+=f'<a id="{r["id"].lower()}"></a>\n## {r["id"]} — {r["title"]}\n\n{r["requirement"]}\n\n'
  s+=f'**配賦：** {r["allocation"]}。**適用：** {r.get("applicability","TBD")}。**状態：** {r.get("status","DRAFT_FOR_REVIEW")}。\n\n'
  s+='**主記載章：** '+link(p,r['primary_note'],r['chapter'])+'。\n\n'
  s+='**関連する現行章：** '+' ／ '.join(link(p,n,Path(n).stem) for n in r['related_current_notes'])+'。\n\n'
  s+='**検証：** '+(', '.join(r.get('verification_ids',[])) or r.get('verification_review','未確定'))+'。\n\n'
  s+='**根拠：** '+', '.join(r.get('source_ids',[]))+'。**原典ARCH：** '+', '.join(r.get('source_arch_ids',[]))+'。**正式USDM：** '+(r.get('usdm_id') or '未確定')+'。\n\n'
 s+='## Open Questions — 本カタログの完成\n\n'+link(p,qm['OQ-R6-19-01']['note'],'OQ-R6-19-01','oq-r6-19-01')+'：正式USDMと双方向トレース。'+link(p,qm['OQ-R6-17-01']['note'],'OQ-R6-17-01','oq-r6-17-01')+'：受入条件。\n';write(p,s)
 # OQ cross-register is a true chapter-derived view, including latest answer/status.
 p='appendices/Open_Question_Register.md';s='# Open Question横断台帳 — 85件\n\n**記入正本は各担当章の末尾。** 本表は章から生成する。IDに含むR6と旧章数字は識別子であり、現在の章番号ではない。4利用者の名称は部分回答済み、権限は未確定である。\n\n| OQ／担当章 | 状態 | 具体的な質問・残る判断 | 必要資料・完了条件 | 回答・決定記録 |\n|---|---|---|---|---|\n'
 for q in qs['items']:
  def cell(x):return str(x).replace('|','&#124;').replace('\n','<br/>')
  s+='| '+link(p,q['note'],q['question_id'],q['question_id'].lower())+'<br/>'+q['chapter']+' | '+q['status']+' | '+cell(q.get('known_answer','')+' '+q['rendered_question'])+' | '+cell(adapt(q['rendered_closure'],q['note'],p))+' | '+cell(q['answer'] or '未記入')+'／'+cell(q['decision_record'] or '未記入')+' |\n'
 s+='\n## Open Questions — 本台帳の管理\n\n'+link(p,qm['OQ-R6-19-02']['note'],'OQ-R6-19-02','oq-r6-19-02')+'：回答責任・期限・ゲートを確定する。\n';write(p,s)
 # Consolidate all current chapters and normative annexes with namespaced anchors.
 paths=[c['path'] for c in idx['chapters']]+idx['appendices'];prefix={p:'doc-'+re.sub(r'[^a-z0-9]+','-',Path(p).stem.lower()) for p in paths}
 def combine_text(p):
  s=(ROOT/p).read_text(encoding='utf-8');s=re.sub(r'\A---\n.*?\n---\n','',s,count=1,flags=re.S)
  s=re.sub(r'<a id="([^"]+)"></a>',lambda m:f'<a id="{prefix[p]}--{m[1]}"></a>',s)
  def dest(m):
   uri=m[2]
   if re.match(r'(https?:|mailto:|data:)',uri):return m[0]
   v,_,a=uri.partition('#');tgt=os.path.normpath(str(Path(p).parent/v)).replace(os.sep,'/') if v else p
   if tgt in prefix:new='#'+prefix[tgt]+('--'+a if a else '')
   else:new=tgt+('#'+a if a else '')
   return m[1]+new+m[3]
  s=LINK.sub(dest,s)
  lines=[];fenced=False
  for l in s.splitlines():
   if re.match(r'^\s*```',l):fenced=not fenced
   if not fenced:
    m=re.match(r'^(#{1,6}) (.*)',l)
    if m:l='#'*min(6,len(m[1])+2)+' '+m[2]
   lines.append(l)
  return '\n'.join(lines).strip()
 out='---\ntitle: "SPK-GW_HEMS システム仕様書 R8 統合閲覧版"\nrevision: R8\nstatus: DRAFT_FOR_REVIEW\n---\n\n# SPK-GW_HEMS システム仕様書 R8\n\n[正本MOC](00_MOC.md) ／ [仕様完成ガイド](01_Completion_Guide.md)\n\n5部・44章の本文と規範別冊を連結した生成ビュー。直接編集しない。技術仕様の採否・数値・機種・権限・認証は未確定事項を含む。\n\n## 目次\n\n'
 for part in idx['parts']:
  out+=f'### Part {part["id"]} {part["title"]}\n\n'
  for co in part['chapters']:
   c=chs[co];out+=f'- [{co} {c["title"]}](#{prefix[c["path"]]})\n'
  out+='\n'
 out+='### 規範別冊・管理台帳\n\n'
 for p in idx['appendices']:out+=f'- [{Path(p).stem}](#{prefix[p]})\n'
 for part in idx['parts']:
  out+=f'\n---\n\n## Part {part["id"]} {part["title"]}\n\n'
  for co in part['chapters']:
   p=chs[co]['path'];out+=f'<a id="{prefix[p]}"></a>\n\n'+combine_text(p)+'\n\n'
 out+='\n---\n\n## 規範別冊・管理台帳\n\n'
 for p in idx['appendices']:out+=f'<a id="{prefix[p]}"></a>\n\n'+combine_text(p)+'\n\n'
 out+='\n## Open Questions — 統合版の扱い\n\n質問は各担当章末尾を正本として更新する。横断一覧は[Open Question台帳](appendices/Open_Question_Register.md)を参照。\n'
 write('90_All_In_One.md',out)
 # Active note-to-question references; archived notes are deliberately excluded.
 nqb={}
 for path in sorted(ROOT.rglob('*.md')):
  rel=path.relative_to(ROOT).as_posix()
  if rel.startswith('sources/'):continue
  txt=path.read_text(encoding='utf-8')
  tail=txt.rsplit('## Open Questions',1)[-1]
  nqb[rel]=list(dict.fromkeys(re.findall(r'OQ-R6-\d{2}-\d{2}',tail)))
 save('data/note_question_bindings.json',{'revision':'R8','source':'current_note_footers','note_bindings':nqb})

 save('data/view_generation.json',{'status':'GENERATED','revision':'R8','function_groups':{'system':len(fc['system_functions']),'gw':len(fc['gw_functions'])},'requirements':len(req),'questions':len(qs['items']),'chapters':len(idx['chapters']),'integrated_source_documents':len(paths),'note':'生成ビューの作成結果。文書適合／実機試験の結果ではない。'})
 print(json.dumps({'generated':'R8 views','chapters':len(idx['chapters']),'questions':len(qs['items'])},ensure_ascii=False))
if __name__=='__main__':
 try:main()
 except (OSError,ValueError,KeyError,StopIteration) as e:
  print(f'ERROR: {e}',file=sys.stderr);sys.exit(1)
