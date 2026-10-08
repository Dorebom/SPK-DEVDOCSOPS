#!/usr/bin/env python3
"""Export two R5 Mermaid blocks from chapter 02; no rendering or device access."""
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
text=(ROOT/'chapters/02_System_Context.md').read_text(encoding='utf-8')
blocks=re.findall(r'```mermaid\n(.*?)\n```',text,flags=re.S)
if len(blocks)<2:raise SystemExit('Expected two context diagrams')
for name,body in zip(['02_01_System_Context','02_01_EL_Connections'],blocks):
 (ROOT/'diagrams'/f'{name}.mmd').write_text(body.strip()+'\n',encoding='utf-8')
print('Exported 2 Mermaid sources from chapter 02')
