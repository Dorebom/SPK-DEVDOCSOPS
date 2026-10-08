#!/usr/bin/env python3
"""Verify the final ZIP, including nested historical manifests and CURRENT snapshot.
Usage: python tools/verify_package.py <distributed.zip>. Does not extract or execute it.
"""
from pathlib import Path,PurePosixPath
import hashlib,json,re,sys,zipfile
from common import FlowError,sha_bytes,record_hash

def verify(path):
    with zipfile.ZipFile(path) as z:
        if z.testzip() is not None:raise FlowError('CRC error')
        entries={}
        for i in z.infolist():
            n=i.filename;p=PurePosixPath(n)
            if p.is_absolute() or '..' in p.parts or '\\' in n or len(p.parts)<2:raise FlowError('Unsafe ZIP path')
            if i.is_dir():continue
            if n in entries:raise FlowError('Duplicate ZIP member')
            if ((i.external_attr>>16)&0o170000)==0o120000:raise FlowError('Symlink ZIP member')
            entries[n]=z.read(i)
        roots={n.split('/')[0]for n in entries}
        if len(roots)!=1:raise FlowError('Single package root required')
        root=next(iter(roots))+'/';files={k[len(root):]:v for k,v in entries.items()}
        if 'MANIFEST_SHA256.txt' not in files:raise FlowError('Root manifest missing')
        manifest={}
        for line in files['MANIFEST_SHA256.txt'].decode().splitlines():
            h,sep,n=line.partition('  ')
            if not sep or not re.fullmatch('[0-9a-f]{64}',h) or n in manifest:raise FlowError('Invalid root manifest')
            manifest[n]=h
        if set(manifest)!=(set(files)-{'MANIFEST_SHA256.txt'}):raise FlowError('Final ZIP manifest inventory differs')
        for n,h in manifest.items():
            if sha_bytes(files[n])!=h:raise FlowError('File hash differs: '+n)
        profile=json.loads(files['00_governance/baseline_R8_FIX001.json'])
        if sha_bytes(files[profile['zip_path']])!=profile['zip_sha256']:raise FlowError('Baseline original ZIP differs')
        for n,h in profile['files'].items():
            path2=profile['extracted_path']+'/'+n
            if path2 not in files or sha_bytes(files[path2])!=h:raise FlowError('Historical original missing/different: '+n)
        meta=json.loads(files['10_canonical/CURRENT.json']);prefix=meta['path']+'/'
        selected={n[len(prefix):]:sha_bytes(v)for n,v in files.items()if n.startswith(prefix)}
        if not selected or record_hash(selected)!=meta['tree_sha256']:raise FlowError('CURRENT tree hash differs')
        receipt=json.loads(files[meta['receipt']])
        if receipt['selected_tree_sha256']!=meta['tree_sha256']:raise FlowError('Receipt/CURRENT mismatch')
        # In particular, inherited MANIFEST files are NOT filtered out by basename.
        required=[profile['extracted_path']+'/sources/r7_snapshot/MANIFEST_SHA256.txt',profile['extracted_path']+'/sources/r7_snapshot/sources/architecture/MANIFEST_SHA256.txt',profile['extracted_path']+'/sources/architecture/MANIFEST_SHA256.txt']
        if not all(x in files for x in required):raise FlowError('FIX001 restored manifests missing')
        return {'result':'PASS','files':len(files),'root_manifest_entries':len(manifest),'r8_original_files':len(profile['files']),'restored_manifest_files':len(required),'selected_baseline':meta['baseline_id'],'canonical_files':len(selected),'zip_bytes':Path(path).stat().st_size,'zip_sha256':sha_bytes(Path(path).read_bytes())}
if __name__=='__main__':
    try:print(json.dumps(verify(sys.argv[1]),ensure_ascii=False,indent=2))
    except (OSError,KeyError,ValueError,IndexError,zipfile.BadZipFile) as e:print('FAIL: '+str(e),file=sys.stderr);sys.exit(1)
