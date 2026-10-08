"""Document tool utilities. No untrusted code, macro or remote link is executed."""
from __future__ import annotations
import contextlib, hashlib, json, os, re, tempfile, uuid
from pathlib import Path
VERSION='1.0.0'
class FlowError(ValueError): pass

def jread(path: Path):
    def unique(pairs):
        out={}
        for k,v in pairs:
            if k in out: raise FlowError(f'Duplicate JSON key: {k} in {path}')
            out[k]=v
        return out
    return json.loads(path.read_text(encoding='utf-8'),object_pairs_hook=unique)
def jbytes(value): return (json.dumps(value,ensure_ascii=False,indent=2)+'\n').encode('utf-8')
def sha_bytes(value: bytes)->str:return hashlib.sha256(value).hexdigest()
def sha_file(path: Path)->str:return sha_bytes(path.read_bytes())
def record_hash(value)->str:return sha_bytes(json.dumps(value,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode())
def atomic_bytes(path: Path,value: bytes):
    path.parent.mkdir(parents=True,exist_ok=True)
    temp=path.with_name('.'+path.name+'.'+uuid.uuid4().hex+'.tmp')
    try:
        with temp.open('xb') as f:
            f.write(value);f.flush();os.fsync(f.fileno())
        os.replace(temp,path)
    finally:temp.unlink(missing_ok=True)
def jwrite(path: Path,value):atomic_bytes(path,jbytes(value))
def inside(root: Path,relative: str)->Path:
    if '\\' in relative or re.match(r'^[A-Za-z]:',relative):raise FlowError('Unsafe path: '+relative)
    path=(root/relative).resolve()
    if path==root.resolve() or not path.is_relative_to(root.resolve()):raise FlowError('Path escapes allowed root: '+relative)
    # Symlinks are not accepted as an alternative way into/out of the controlled tree.
    probe=root
    for bit in Path(relative).parts:
        probe=probe/bit
        if probe.is_symlink():raise FlowError('Symlink not supported: '+str(probe))
    return path

def file_map(root:Path):
    out={}
    for p in sorted(root.rglob('*')):
        if p.is_symlink():raise FlowError('Symlink forbidden: '+str(p))
        if p.is_file():
            rel=p.relative_to(root).as_posix()
            if '__pycache__' in p.parts or p.suffix=='.pyc':continue
            out[rel]=sha_file(p)
    return out

def tree_hash(root:Path)->str:return record_hash(file_map(root))
def toolchain_hash(workspace:Path)->str:
    return record_hash({str(p.relative_to(workspace)):sha_file(p) for d in ['tools','schemas'] for p in sorted((workspace/d).rglob('*')) if p.is_file() and p.suffix in ['.py','.json'] and '__pycache__' not in p.parts and 'tests' not in p.parts})

def current(workspace:Path,verify=True):
    meta=jread(workspace/'10_canonical/CURRENT.json')
    path=inside(workspace,meta['path'])
    if not path.is_relative_to((workspace/'10_canonical/releases').resolve()):raise FlowError('CURRENT outside releases')
    if verify and tree_hash(path)!=meta['tree_sha256']:raise FlowError('Selected canonical baseline was modified. Do not edit it in place; restore or use a draft.')
    return path,meta

@contextlib.contextmanager
def workspace_lock(workspace:Path):
    path=workspace/'20_work/analysis/.workspace.lock';path.parent.mkdir(parents=True,exist_ok=True)
    try:fd=os.open(path,os.O_WRONLY|os.O_CREAT|os.O_EXCL,0o600)
    except FileExistsError:raise FlowError('Workspace locked. Confirm no writer is running before manually removing '+str(path))
    try:
        os.write(fd,jbytes({'pid':os.getpid(),'purpose':'single writer document workflow'}));os.close(fd);yield
    finally:path.unlink(missing_ok=True)

def require_id(s:str)->str:
    if not re.fullmatch(r'[A-Za-z][A-Za-z0-9_-]*',s):raise FlowError('Invalid ID: '+s)
    return s

def schema_check(workspace:Path,name:str,value):
    try:
        from jsonschema import Draft202012Validator
    except ImportError as e:raise FlowError('Install tools/requirements.txt (jsonschema) first') from e
    schema=jread(workspace/'schemas'/f'{name}.schema.json')
    errors=sorted(Draft202012Validator(schema).iter_errors(value),key=lambda e:str(list(e.path)))
    if errors:
        raise FlowError(name+': '+'; '.join('/'.join(map(str,e.path))+': '+e.message for e in errors[:8]))
