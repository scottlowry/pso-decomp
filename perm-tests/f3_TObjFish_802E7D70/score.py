#!/usr/bin/env python3
"""word-diff oracle: objdump -d both .o, exclude rows with reloc operand (bl / @sda21 / .),
print diff slots + size. Target = exclude-set-zero-diff on 7 register rows."""
import re, subprocess, sys
OBJD='/opt/homebrew/bin/powerpc-eabi-objdump'
def rows(o):
    txt=subprocess.run([OBJD,'-d',o],capture_output=True,text=True).stdout
    out=[]; started=False
    for l in txt.splitlines():
        if '<TObjFish__sub_802E7D70>' in l: started=True; continue
        if started:
            if re.match(r'^[0-9a-f]+ <',l): break
            m=re.match(r'\s+[0-9a-f]+:\s+((?:[0-9a-f]{2} ){4})\s+(.*)',l)
            if m: out.append((m.group(1).replace(' ','').strip(), m.group(2).strip()))
    return out
t=rows(sys.argv[1]); c=rows(sys.argv[2])
print('target words', len(t), 'cand words', len(c))
if len(t)!=len(c):
    print('SIZE MISMATCH (gate fail: need 76/76)'); sys.exit(2)
EXT=lambda txt: ('@sda21' in txt) or txt.startswith('bl ') or txt.startswith('b ') or ('<' in txt and '>' in txt and ':' in txt and 'r' not in txt.split()[0])
diff=[i for i in range(len(t)) if t[i][0]!=c[i][0] and not EXT(t[i][1]) and not EXT(c[i][1])]
extd=[i for i in range(len(t)) if t[i][0]!=c[i][0] and (EXT(t[i][1]) or EXT(c[i][1]))]
print('REGDIFF slots:', diff, f'count={len(diff)}')
print('  (ext-excluded diffs, expect only reloc-addend noise):', extd)
sys.exit(0 if len(diff)==7 and set(diff)=={15,17,30,31,34,35,37} else (1 if len(diff)<7 else 3))
