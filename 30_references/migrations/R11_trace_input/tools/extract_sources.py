"""Conservative, read-only OOXML extraction. Retains raw values and unresolved objects.

Supported: docx paragraphs/tables incl nested tables/revision text and XML parts;
xlsx cell/formula/cache/styles/merged/hidden/comment metadata; UTF-8 md/txt/csv.
Unsupported binary/complex objects are inventoried, never silently treated as absent.
No Office dependency, macro execution, recalc, network access, or OCR.
"""
from __future__ import annotations
import csv, io, json, posixpath, re, zipfile
import xml.etree.ElementTree as ET
from pathlib import Path
from common import FlowError, record_hash, sha_file, VERSION
MAX_MEMBERS=10000;MAX_TOTAL=100*1024*1024;MAX_XML=30*1024*1024
W='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
X='{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'
REL='{http://schemas.openxmlformats.org/package/2006/relationships}'
RID='{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id'

def package(path):
    z=zipfile.ZipFile(path)
    infos=z.infolist()
    if len(infos)>MAX_MEMBERS or sum(i.file_size for i in infos)>MAX_TOTAL:
        z.close();raise FlowError('OOXML package exceeds configured extraction limits')
    seen=set()
    for i in infos:
        name=i.filename
        if name in seen or '\\' in name or name.startswith('/') or '..' in Path(name).parts:
            z.close();raise FlowError('Unsafe or duplicate OOXML member: '+name)
        seen.add(name)
        if i.flag_bits&1:
            z.close();raise FlowError('Encrypted OOXML: manual conversion required')
    return z

def xml(z,name):
    b=z.read(name)
    if len(b)>MAX_XML or b'<!DOCTYPE' in b.upper() or b'<!ENTITY' in b.upper():raise FlowError('Unsafe/oversize XML: '+name)
    return ET.fromstring(b)

def paths(element,path=''):
    counts={}
    for e in element:
        local=e.tag.split('}')[-1];counts[local]=counts.get(local,0)+1
        p=f'{path}/{local}[{counts[local]}]'
        yield e,p
        yield from paths(e,p)

def fragment(source,loc,text,context=None,features=None,review=False):
    identity={'source_id':source['source_id'],'sha':source['sha256'],'locator':loc,'text':text}
    return {'fragment_id':'FRAG-'+record_hash(identity)[:24],'source_id':source['source_id'],'source_sha256':source['sha256'],'locator':loc,'raw_text':text,'context':context or {},'extraction_status':'NEEDS_REVIEW' if review else 'EXTRACTED','features':features or [],'verified_by':None,'review_note':None}

def extract_docx(path,source):
    fs=[];objects=[]
    with package(path) as z:
        parts=[n for n in z.namelist() if n.startswith('word/') and n.endswith('.xml') and (n=='word/document.xml' or re.match(r'word/(header\d+|footer\d+|footnotes|endnotes|comments)\.xml$',n))]
        if 'word/document.xml' not in parts:raise FlowError('No Word document part')
        for name in parts:
            root=xml(z,name); headings=[]
            for e,xpath in paths(root,root.tag.split('}')[-1]+'[1]'):
                if e.tag!=W+'p':continue
                # Paragraph descendants in nested tables handled by paths(); textbox paragraphs may also occur.
                texts=[]
                for n in e.iter():
                    if n.tag in [W+'t',W+'delText']:texts.append(n.text or '')
                    elif n.tag in [W+'tab']:texts.append('\t')
                    elif n.tag in [W+'br',W+'cr']:texts.append('\n')
                raw=''.join(texts)
                style=e.find('./'+W+'pPr/'+W+'pStyle');styleid=style.get(W+'val') if style is not None else None
                feats=[]
                for tag,label in [('ins','TRACKED_INSERTION'),('del','TRACKED_DELETION'),('drawing','DRAWING_MANUAL'),('pict','VML_MANUAL'),('object','OLE_MANUAL'),('fldChar','FIELD_UNEVALUATED'),('instrText','FIELD_UNEVALUATED'),('commentRangeStart','COMMENT_REFERENCE')]:
                    if any(n.tag==W+tag for n in e.iter()) or f'/{tag}[' in xpath:feats.append(label)
                if any(n.tag.endswith('}oMath') for n in e.iter()):feats.append('EQUATION_MANUAL')
                if '/txbxContent[' in xpath:feats.append('TEXTBOX_REVIEW')
                if '/tbl[' in xpath:feats.append('TABLE_CONTEXT_REQUIRED')
                if styleid and re.search(r'Heading|見出し',styleid,re.I):headings=(headings+[raw])[-6:]
                ctx={'style':styleid,'preceding_heading_context':list(headings),'part':name,'table_path':xpath.rsplit('/tc[',1)[0] if '/tc[' in xpath else None,'layout_page':None,'tracked_changes_policy':'BOTH_STORED_NO_ACCEPT_REJECT'}
                if raw or feats:fs.append(fragment(source,{'part':name,'xml_path':xpath},raw,ctx,feats,bool(feats)))
            for e,xpath in paths(root):
                if e.tag in [W+'gridSpan',W+'vMerge']:
                    objects.append({'part':name,'xml_path':xpath,'kind':'TABLE_MERGE_METADATA','attributes':e.attrib,'status':'METADATA_EXTRACTED_HUMAN_LAYOUT_REVIEW'})
                if e.tag in [W+'sdt',W+'altChunk']:
                    objects.append({'part':name,'xml_path':xpath,'kind':e.tag.split('}')[-1],'status':'MANUAL_REVIEW_REQUIRED'})
        for n in z.namelist():
            if n.startswith(('word/media/','word/embeddings/')):
                objects.append({'part':n,'kind':'IMAGE_OR_EMBEDDED_OBJECT','sha256':__import__('hashlib').sha256(z.read(n)).hexdigest(),'status':'NOT_INTERPRETED'})
        objects.append({'kind':'PAGE_LAYOUT_NUMBERING_CROSSREFERENCES','status':'NOT_RENDERED_NOT_EVALUATED','note':'ページ・番号・相互参照はWord表示と別途対照。XML位置と原本hashが主locator。'})
    return fs,objects

def extract_xlsx(path,source):
    fs=[];objects=[]
    with package(path) as z:
        root=xml(z,'xl/workbook.xml');rels={e.get('Id'):e for e in xml(z,'xl/_rels/workbook.xml.rels')}
        shared=[]
        if 'xl/sharedStrings.xml' in z.namelist():
            shared=[''.join(e.itertext()) for e in xml(z,'xl/sharedStrings.xml') if e.tag==X+'si']
        formats={};styles=[]
        if 'xl/styles.xml' in z.namelist():
            st=xml(z,'xl/styles.xml')
            for e in st.iter(X+'numFmt'):formats[e.get('numFmtId')]=e.get('formatCode')
            cx=st.find(X+'cellXfs');styles=[dict(e.attrib) for e in cx] if cx is not None else []
        for sh in root.findall('./'+X+'sheets/'+X+'sheet'):
            rr=rels.get(sh.get(RID))
            if rr is None or rr.get('TargetMode')=='External':raise FlowError('Invalid worksheet relationship')
            target=rr.get('Target','');part=posixpath.normpath(target.lstrip('/') if target.startswith('/') else posixpath.join('xl',target))
            if not part.startswith('xl/'):raise FlowError('Worksheet target escaped package')
            s=xml(z,part);merge=[m.get('ref') for m in s.iter(X+'mergeCell')]
            hidden_cols=[dict(c.attrib) for c in s.iter(X+'col') if c.get('hidden')=='1']
            def col_index(cell):
                n=0
                for c in re.match('[A-Za-z]+',cell)[0].upper():n=n*26+ord(c)-64
                return n
            def in_range(addr,rg):
                a,b=rg.split(':') if ':' in rg else (rg,rg)
                row=int(re.search(r'\d+',addr)[0]);return col_index(a)<=col_index(addr)<=col_index(b) and int(re.search(r'\d+',a)[0])<=row<=int(re.search(r'\d+',b)[0])
            prev=[]
            for row in s.findall('./'+X+'sheetData/'+X+'row'):
                rowsummary=[]
                for c in row.findall(X+'c'):
                    addr=c.get('r');f=c.find(X+'f');v=c.find(X+'v');t=c.get('t','n');val=v.text if v is not None else None
                    if t=='s' and val is not None:
                        try:display=shared[int(val)]
                        except (ValueError,IndexError):display='';objects.append({'part':part,'cell':addr,'kind':'BAD_SHARED_STRING','status':'BLOCKED'})
                    elif t=='inlineStr':display=''.join(n.text or '' for n in c.iter(X+'t'))
                    else:display=val or ''
                    if not display and f is None:continue
                    si=int(c.get('s','0'));style=styles[si] if si<len(styles) else {}
                    feats=[]
                    hidden=sh.get('state','visible')!='visible' or row.get('hidden')=='1' or any(int(x['min'])<=col_index(addr)<=int(x['max']) for x in hidden_cols)
                    if hidden:feats.append('HIDDEN_CONTENT')
                    matching=[m for m in merge if in_range(addr,m)]
                    if matching:feats.append('MERGED_CELL')
                    if f is not None:feats.append('FORMULA_CACHE_NOT_RECALCULATED')
                    if f is not None and f.get('t') in ['shared','array']:feats.append('SHARED_OR_ARRAY_FORMULA_REVIEW')
                    ctx={'cell_type':t,'raw_value':val,'formula':None if f is None else {'text':f.text,'attributes':dict(f.attrib)},'cached_value':val if f is not None else None,'display_text_unformatted':display,'style_index':si,'number_format_id':style.get('numFmtId'),'custom_number_format':formats.get(style.get('numFmtId')),'sheet_state':sh.get('state','visible'),'row_hidden':row.get('hidden')=='1','hidden_columns':hidden_cols,'merged_ranges':matching,'preceding_rows':prev[-3:],'date_system':(root.find(X+'workbookPr').get('date1904') if root.find(X+'workbookPr') is not None else None)}
                    raw=('='+str(f.text or '')+' [cached='+str(val)+']') if f is not None else display
                    fs.append(fragment(source,{'part':part,'sheet':sh.get('name'),'sheet_id':sh.get('sheetId'),'cell':addr},raw,ctx,feats,True))
                    rowsummary.append([addr,display])
                if rowsummary:prev.append(rowsummary)
            objects.append({'part':part,'sheet':sh.get('name'),'kind':'SHEET_LAYOUT','merged_ranges':merge,'status':'METADATA_EXTRACTED_HEADER_UNIT_REVIEW_REQUIRED'})
        for n in z.namelist():
            if re.match(r'xl/comments\d*\.xml$',n):
                for c in xml(z,n).iter(X+'comment'):
                    raw=''.join(t.text or '' for t in c.iter(X+'t'))
                    fs.append(fragment(source,{'part':n,'cell':c.get('ref'),'kind':'comment'},raw,{'author_id':c.get('authorId')},['COMMENT_SHEET_BINDING_REVIEW'],True))
            if n.startswith(('xl/drawings/','xl/media/','xl/embeddings/','xl/externalLinks/','xl/pivot','xl/tables/','xl/threadedComments/')) or 'vbaProject' in n:
                objects.append({'part':n,'kind':'COMPLEX_OBJECT','status':'NOT_INTERPRETED_OR_EXECUTED'})
            if n.endswith('.rels'):
                for e in xml(z,n):
                    if e.get('TargetMode')=='External':objects.append({'part':n,'kind':'EXTERNAL_RELATIONSHIP','target':e.get('Target'),'status':'NOT_FETCHED'})
        for e in root.iter(X+'definedName'):objects.append({'kind':'DEFINED_NAME','name':e.get('name'),'text':e.text,'status':'NOT_EVALUATED'})
    return fs,objects

def extract(path:Path,source:dict)->dict:
    if path.stat().st_size>MAX_TOTAL:raise FlowError('Source exceeds configured extraction size budget')
    if sha_file(path)!=source['sha256']:raise FlowError('Original SHA-256 mismatch')
    suffix=path.suffix.lower();fs=[];objs=[];notes=['抽出と解釈・採用は別。原文の注記・表ヘッダ・単位・適用範囲を人が確認する。']
    status='NEEDS_REVIEW'
    if suffix=='.docx':fs,objs=extract_docx(path,source)
    elif suffix=='.xlsx':fs,objs=extract_xlsx(path,source)
    elif suffix in ['.md','.txt','.csv']:
        try:text=path.read_text(encoding='utf-8-sig')
        except UnicodeError:
            status='BLOCKED_MANUAL';objs=[{'kind':'NON_UTF8_TEXT','status':'CONVERSION_REQUIRED_KEEP_ORIGINAL'}]
        else:
            lines=text.splitlines()
            for i,line in enumerate(lines,1):
                if line.strip():fs.append(fragment(source,{'line_start':i,'line_end':i},line,{'format':suffix,'previous_line':lines[i-2] if i>1 else ''},['CSV_HEADER_CONTEXT_REQUIRED'] if suffix=='.csv' else [],True))
    else:
        status='BLOCKED_MANUAL';objs=[{'kind':suffix or 'NO_EXTENSION','status':'UNSUPPORTED_FORMAT','note':'.doc/.xls/.xlsm、暗号化、画像主体等は原本保持の上で認可された変換・目視確認。自動変換・マクロ・外部参照・OCRは行わない。'}]
    fingerprint=sha_file(Path(__file__))
    run_id='RUN-'+record_hash([source['source_id'],source['sha256'],VERSION,fingerprint])[:24]
    for f in fs:
        f['context']['extraction']={'run_id':run_id,'extractor_version':VERSION,'extractor_sha256':fingerprint}
        f['fragment_id']='FRAG-'+record_hash({'source_id':f['source_id'],'sha':f['source_sha256'],'locator':f['locator'],'text':f['raw_text'],'extractor_sha256':fingerprint})[:24]
    return {'schema':'spkgw.extraction-run/v1','run_id':run_id,'source_id':source['source_id'],'source_sha256':source['sha256'],'extractor_version':VERSION,'extractor_sha256':fingerprint,'status':status,'fragments':fs,'unhandled_objects':objs,'notes':notes}
