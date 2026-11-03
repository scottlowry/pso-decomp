#!/usr/bin/env python3
"""word-diff oracle for fn_8042E8C4 (78 words). Compare target .o vs candidate .o,
exclude reloc-bearing rows (bl / sym(rN) / branch-with-symbol). Gate: 78/78 words, diff=0."""
import re, subprocess, sys
OBJD='/opt/homebrew/bin/powerpc-eabi-objdump'
FN='fn_8042E8C4'
def rows(o):
    txt=subprocess.run([OBJD,'-d',o],capture_output=True,text=True).stdout
    out=[]; started=False
    for l in txt.splitlines():
        if '<%s>'%FN in l: started=True; continue
        if started:
            if re.match(r'^[0-9a-f]+ <',l): break
            m=re.match(r'\s+[0-9a-f]+:\s+((?:[0-9a-f]{2} ){4})\s+(.*)',l)
            if m: out.append((m.group(1).replace(' ','').strip(), m.group(2).strip()))
    return out
t=rows(sys.argv[1]); c=rows(sys.argv[2])
print('target words', len(t), 'cand words', len(c))
if len(t)!=len(c):
    print('SIZE MISMATCH (gate: 78/78)'); sys.exit(2)
EXT=lambda txt: ('@sda21' in txt) or txt.startswith('bl ') or txt.startswith('b ') or ('<' in txt and '>' in txt)
diff=[i for i in range(len(t)) if t[i][0]!=c[i][0] and not EXT(t[i][1]) and not EXT(c[i][1])]
extd=[i for i in range(len(t)) if t[i][0]!=c[i][0] and (EXT(t[i][1]) or EXT(c[i][1]))]
print('REGDIFF slots:', diff, f'count={len(diff)}')
for i in diff: print(f'  [{i:2d}] T: {t[i][0]} {t[i][1]:32s} C: {c[i][0]} {c[i][1]}')
print('  ext-excluded diffs (reloc-addend noise expected):', extd)
for i in extd: print(f'  *[{i:2d}] T: {t[i][0]} {t[i][1]:32s} C: {c[i][0]} {c[i][1]}')
sys.exit(0 if len(diff)==0 else (1 if len(diff)<8 else 3))
