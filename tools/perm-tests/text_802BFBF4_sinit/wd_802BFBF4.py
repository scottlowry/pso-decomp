#!/usr/bin/env python3
"""Raw-word proof for text_802BFBF4 synthesis vs era window.
orig: build/GPOE8P/asm/pso/unk/text_802BFBF4.s (fn_802BFBF4)
ours: objdump -dr probe .o (__sinit_text_802BFBF4_cpp)
link-class rows re-resolved against era addresses (symbols.txt + placeholder map)."""
import re, sys, subprocess
from collections import Counter

R = '/Users/scott/Hermes/pso-decomp/pso-decomp-f7/'
ORIG_S = R + 'build/GPOE8P/asm/pso/unk/text_802BFBF4.s'
FN_ORIG, FN_OURS = 'fn_802BFBF4', '__sinit_text_802BFBF4_cpp'

# era addresses: parse symbols.txt once
ERA = {}
for ln in open(R + 'config/GPOE8P/psov3/symbols.txt'):
    m = re.match(r"(\S+) = \.\w+:0x([0-9A-Fa-f]+);", ln.strip())
    if m: ERA[m.group(1)] = int(m.group(2), 16)
# placeholder mirror-name -> era unmangled address
extra = {}
for n, a in list(ERA.items()):
    if n.startswith('TBoss6Type2__sub_'):
        extra['sub_' + n.split('__sub_')[1] + '__11TBoss6Type2Fv'] = a
ERA.update(extra)
for n, a in list(ERA.items()):
    if n.startswith('lbl_') and n[4:].isdigit():
        ERA.setdefault(n, a)

def orig_rows():
    t = open(ORIG_S).read()
    t = t.split('.fn ' + FN_ORIG)[1]; t = t[:t.index('.endfn')]
    return [(int(m.group(1), 16), m.group(2).upper().split(), m.group(3).strip())
            for m in re.finditer(r"/\* (\w{8}) \w+\s+((?:[0-9A-F]{2} ){3}[0-9A-F]{2}) ?\*/\s*(.*)", t)]

def ours_rows(o):
    txt = subprocess.run([R + 'build/binutils/powerpc-eabi-objdump', '-dr', o], capture_output=True, text=True).stdout
    sec = txt.split('Disassembly of section .text:')[1].split('Disassembly of section')[0]
    body = sec.split('<' + FN_OURS + '>:')[1]
    rows, pend = [], None
    for ln in body.splitlines():
        m = re.match(r"\s+([0-9a-f]+):\t((?:[0-9a-f]{2} )+)\t(.*)", ln)
        if m:
            if pend and rows: rows[-1].append(pend); pend = None
            rows.append([m.group(1), m.group(2).upper().split(), m.group(3).strip()])
        else:
            r = re.match(r"\s+[0-9a-f]+: (R_\w+)\t(\S+)", ln)
            if r and rows: pend = (r.group(1), r.group(2))
    if pend and rows: rows[-1].append(pend)
    return rows

def canon(tok, row=None):
    mn = re.sub(r"\s+", " ", tok).strip().lower()
    if row and len(row) > 3:
        cls, sym = row[3]
        if cls == 'R_PPC_ADDR16_HA': mn = re.sub(r",\s*0(\(|$)", "," + sym.lower() + "@ha\\1", mn)
        elif cls == 'R_PPC_ADDR16_LO': mn = re.sub(r",\s*0(\(|$)", "," + sym.lower() + "@l\\1", mn)
        elif cls == 'R_PPC_REL24': mn = "bl " + sym.lower()
    t = re.sub(r"(-?)0x([0-9a-f]+)", lambda m: m.group(1) + str(int(m.group(2), 16)), mn)
    t = re.sub(r"[\(\),]", " ", t)
    return " ".join(t.split())

def canon_orig(tok):
    t = tok.lower()
    t = re.sub(r"(-?)0x([0-9a-f]+)", lambda m: m.group(1) + str(int(m.group(2), 16)), t)
    t = re.sub(r"[\(\),]", " ", t)
    return " ".join(t.split())

def lcs(a, b):
    n, m = len(a), len(b)
    prev = [0]*(m+1)
    for i in range(n-1, -1, -1):
        cur = [0]*(m+1)
        for j in range(m-1, -1, -1):
            cur[j] = prev[j+1]+1 if a[i] == b[j] else max(prev[j], cur[j+1])
        prev = cur
    return prev[0]

o = sys.argv[1] if len(sys.argv) > 1 else R + 'tools/perm-tests/text_802BFBF4_sinit/v1.o'
O, U = orig_rows(), ours_rows(o)
print(f"orig words={len(O)} ours words={len(U)}")
if len(O) != len(U): print("!! SIZE CLASS MISMATCH")

# positional alignment via our .o offsets (word 0 = 0x802BFBF4 base)
BASE = 0x802BFBF4
pos = link = hard = 0
linkrows = []
for i in range(min(len(O), len(U))):
    if O[i][1] == U[i][1]: pos += 1
    elif len(U[i]) > 3: link += 1; linkrows.append(i)
    else:
        hard += 1
        if hard <= 10: print(f"HARD [{i}] {hex(BASE+4*i)} orig={' '.join(O[i][1])} {O[i][2]!r} ours={' '.join(U[i][1])} {U[i][2]!r}")
print(f"positional raw-byte EXACT: {pos}/{len(O)}; resolve-at-link class: {link}; hard fails: {hard}")

TEMPLATE_BASE=0x804DFC50
import subprocess as _sp
_g=_sp.run(['/opt/homebrew/opt/binutils/bin/gnm','-S',o],capture_output=True,text=True).stdout
bloboff={m.group(2):int(m.group(1),16) for m in re.finditer(r'([0-9a-f]{8}) 0000000c d (@\d+)',_g)}
wok = wn = 0
for i in linkrows:
    addr = BASE + 4*i
    cls, sym = U[i][3]
    w = int(''.join(U[i][1]), 16)
    a = ERA.get(sym)
    if sym == "...data.0":
        sym = "@1"
    if a is None and re.fullmatch(r"@\d+", sym):
        a = TEMPLATE_BASE + bloboff.get(sym, 0)   # compiler-anon template blob @N
    elif a is None and sym == "TBoss6Type2__actions_804E00DC":
        a = 0x804E00DC                            # instance: our label vs era placeholder lbl_804E00DC
    if a is None:
        print(f"  NAME-MISS {sym} row {i}"); wn += 1; continue
    if cls == 'R_PPC_ADDR16_HA': exp = (w & 0xFFFF0000) | ((a + 0x8000) >> 16 & 0xFFFF)
    elif cls == 'R_PPC_ADDR16_LO': exp = (w & 0xFFFF0000) | (a & 0xFFFF)
    elif cls == 'R_PPC_REL24': exp = (w & ~0x03FFFFFC) | ((((a - addr) >> 2) & 0xFFFFFF) << 2)
    else: exp = None
    got = int(''.join(O[i][1]), 16)
    if exp == got: wok += 1
    else:
        wn += 1
        if wn <= 12: print(f"  LINKDIFF [{i}] {hex(addr)} {cls} {sym}: exp={hex(exp if exp else 0)} orig={hex(got)}")
print(f"linked-word proof: {wok}/{len(linkrows)} MATCH ({wn} diff)")

ca = [canon_orig(r[2]) for r in O]
cb = [canon_ours := canon(r[2], r) for r in U]
mo, mu = Counter(ca), Counter(cb)
same = sum((mo & mu).values())
print(f"content multiset: {same}/{max(len(O),len(U))}  orig-only={len(mo-mu)} ours-only={len(mu-mo)}")
d1 = Counter(mo - mu); d2 = Counter(mu - mo)
print("  orig-only sample:", list(d1.items())[:8])
print("  ours-only sample:", list(d2.items())[:8])
print(f"positional LCS: {lcs(ca, cb)}/{min(len(ca),len(cb))}")
