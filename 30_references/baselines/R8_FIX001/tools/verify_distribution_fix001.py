#!/usr/bin/env python3
"""Validate the *distributed* R8-FIX001 ZIP, not just its staging directory.

Usage: python tools/verify_distribution_fix001.py <path-to-zip>
Does not alter any files.
"""
import json,zipfile,hashlib,sys,pathlib

def sha(b): return hashlib.sha256(b).hexdigest()
def assert_ok(v,msg):
 if not v: raise ValueError(msg)

def main(p):
 with zipfile.ZipFile(p,'r') as z:
  corrupt=z.testzip()
  assert_ok(corrupt is None,f'ZIP CRC failure: {corrupt}')
  seen=set(); files={}
  for info in z.infolist():
   name=info.filename
   pp=pathlib.PurePosixPath(name)
   assert_ok(not pp.is_absolute() and '..' not in pp.parts and len(pp.parts)>=2,f'Unsafe path: {name}')
   if info.is_dir(): continue
   assert_ok(name not in seen, f'Duplicate ZIP path: {name}')
   seen.add(name);files[name]=z.read(name)
  roots={k.split('/')[0] for k in files}
  assert_ok(len(roots)==1,'ZIP must contain one common top directory')
  root=next(iter(roots))+'/'
  rel={k[len(root):]:v for k,v in files.items()}
  manifest={}
  for line in rel['MANIFEST_SHA256.txt'].decode('utf-8').splitlines():
   digest,sep,fn=line.partition('  ')
   assert_ok(bool(sep) and len(digest)==64,f'Invalid manifest line: {line[:90]}')
   assert_ok(fn not in manifest,f'Duplicate hash entry: {fn}')
   manifest[fn]=digest
  assert_ok(set(manifest)==set(rel)-{'MANIFEST_SHA256.txt'},'Root Manifest files differ from ZIP contents')
  for k,h in manifest.items():assert_ok(sha(rel[k])==h,f'Root Manifest hash mismatch: {k}')
  inp=json.loads(rel['data/input_manifest.json'])
  entries=inp['archived_nonzip_files']
  assert_ok(len(entries)==175,'R7 non-ZIP source count should be 175')
  for e in entries:
   path='sources/r7_snapshot/'+e['path']
   assert_ok(path in rel,f'Missing original R7 nonzip: {path}')
   assert_ok(len(rel[path])==e['size'] and sha(rel[path])==e['sha256'],f'Original byte mismatch: {path}')
  arch='sources/architecture/MANIFEST_SHA256.txt'
  assert_ok(arch in rel,'Active architecture SHA-256 manifest is missing')
  source_e=next(e for e in entries if e['path']=='sources/architecture/MANIFEST_SHA256.txt')
  assert_ok(sha(rel[arch])==source_e['sha256'],'Active architecture manifest differs from source')
  amap={}
  for l in rel[arch].decode('utf-8').splitlines():
   h,sep,k=l.partition('  ');assert_ok(bool(sep),'Invalid architecture hash record')
   assert_ok('sources/architecture/'+k in rel,'Missing architecture referenced asset: '+k)
   assert_ok(sha(rel['sources/architecture/'+k])==h,'Architecture original mismatch: '+k)
   amap[k]=h
  meta=json.loads(rel['package_info.json'])
  assert_ok(meta.get('distribution_patch')=='R8-FIX001','Wrong distribution patch ID')
  assert_ok(meta.get('technical_specification_changed') is False,'Technical modification forbidden by repair')
  assert_ok(not any(k.endswith('.zip') for k in rel),'Nested historical ZIP should remain excluded')
  return {'status':'PASS','distribution_patch':'R8-FIX001','zip_entries':len(files),'root_manifest_hashes_verified':len(manifest),'r7_nonzip_originals_verified':len(entries),'active_architecture_originals_verified':len(amap),'restored_missing_files':3,'archive_nested_zip_count':0,'zip_sha256':sha(pathlib.Path(p).read_bytes())}

if __name__=='__main__':
 try:
  print(json.dumps(main(sys.argv[1]),ensure_ascii=False,indent=2))
 except (OSError,KeyError,ValueError,IndexError,zipfile.BadZipFile) as e:
  print('FAIL:',e,file=sys.stderr);sys.exit(1)
