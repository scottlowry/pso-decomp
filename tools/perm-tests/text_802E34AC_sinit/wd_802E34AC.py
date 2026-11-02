#!/usr/bin/env python3
"""Raw-word proof for text_802E34AC synthesis vs era window.
orig: build/GPOE8P/asm/pso/unk/text_802E34AC.s (fn_802E34AC)
ours: objdump -dr probe .o (__sinit_*_cpp)
link-class rows (R_PPC_ADDR16_HA/LO, REL24, EMB_SDA21) re-resolved against era addresses."""
import re, sys, subprocess
from collections import Counter

R = '/Users/scott/Hermes/pso-decomp/pso-decomp-f7/'
ORIG_S = R + 'build/GPOE8P/asm/pso/unk/text_802E34AC.s'
BASE = 0x802E34AC
FN_ORIG = 'fn_802E34AC'
R13 = 0x805DFD00
FRAG = 0x804E3040

ERA = {}
for ln in open(R + 'config/GPOE8P/psov3/symbols.txt'):
    m = re.match(r"(\S+) = \.\w+:0x([0-9A-Fa-f]+);", ln.strip())
    if m: ERA.setdefault(m.group(1), int(m.group(2), 16))
# placeholder mirror-name -> era unmangled address
for n, a in list(ERA.items()):
    if n.startswith('TAdSinglePlyChrSelectGC__sub_'):
        ERA.setdefault('sub_' + n.split('__sub_')[1] + '__23TAdSinglePlyChrSelectGCFv', a)

def orig_rows():
    t = open(ORIG_S).read()
    t = t.split('.fn ' + FN_ORIG)[1]; t = t[:t.index('.endfn')]
    return [(int(m.group(1), 16), m.group(2).upper().split(), m.group(3).strip())
            for m in re.finditer(r"/\* (\w{8}) \w+\s+((?:[0-9A-F]{2} ){3}[0-9A-F]{2}) ?\*/\s*(.*)", t)]

def ours_rows(o, fnours):
    txt = subprocess.run([R + 'build/binutils/powerpc-eabi-objdump', '-dr', o], capture_output=True, text=True).stdout
    sec = txt.split('Disassembly of section .text:')[1].split('Disassembly of section')[0]
    body = sec.split('<' + fnours + '>:')[1]
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
    return rows, txt

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

o = sys.argv[1] if len(sys.argv) > 1 else R + 'tools/perm-tests/text_802E34AC_sinit/v1.o'
fnours = sys.argv[2] if len(sys.argv) > 2 else '__sinit_probe_802E34AC_v1_cpp'
O, U = orig_rows(), None
U, txt = ours_rows(o, fnours)
print(f"orig words={len(O)} ours words={len(U)}")
if len(O) != len(U): print("!! SIZE CLASS MISMATCH", hex(4*len(O)), hex(4*len(U)))

pos = link = hard = 0
linkrows = []
for i in range(min(len(O), len(U))):
    if O[i][1] == U[i][1]: pos += 1
    elif len(U[i]) > 3: link += 1; linkrows.append(i)
    else:
        hard += 1
        if hard <= 14: print(f"HARD [{i}] {hex(BASE+4*i)} orig={' '.join(O[i][1])} {O[i][2]!r} ours={' '.join(U[i][1])} {U[i][2]!r}")
print(f"positional raw-byte EXACT: {pos}/{len(O)}; resolve-at-link class: {link}; hard fails: {hard}")

# map compiler-anon @NN sdata2 syms to era address via their float value
g = subprocess.run(['/opt/homebrew/opt/binutils/bin/gnm', '-S', o], capture_output=True, text=True).stdout
sd2 = {}
for m in re.finditer(r'([0-9a-f]{8}) 00000004 d (@\d+)', g): sd2[m.group(2)] = int(m.group(1), 16)
sd = subprocess.run([R + 'build/binutils/powerpc-eabi-objdump', '-s', '-j', '.sdata2', o], capture_output=True, text=True).stdout
data = {}
for m in re.finditer(r'^\s+([0-9a-f]{4}) ((?:[0-9a-f]{2,8} )+)', sd, re.M):
    off = int(m.group(1), 16)
    for j, b in enumerate(m.group(2).split()): data[off + j] = int(b, 16) if len(b) == 2 else None
raw = bytes.fromhex(re.sub(r'\s', '', ''.join(m.group(2) for m in re.finditer(r'^\s+[0-9a-f]{4} ((?:[0-9a-f]{2,8} )+)', sd.replace('\n', '\n'), re.M)))) if False else None
lines = [l for l in sd.splitlines() if re.match(r'\s+[0-9a-f]{4}\s', l)]
blob = bytes.fromhex(''.join(l.split()[1] for l in lines))
ERA_SDA21 = {0x3F000000: 0x805DE8E8, 0x44200000: 0x805DE8FC, 0x41A00000: 0x805DE900,
             0x41200000: 0x805DE904, 0x42200000: 0x805DE908, 0x42AA0000: 0x805DE90C,
             0x44070000: 0x80472930, 0x43820000: 0x80472934}
wok = wn = 0
for i in linkrows:
    addr = BASE + 4*i
    cls, sym = U[i][3]
    w = int(''.join(U[i][1]), 16)
    a = None
    if sym in ERA: a = ERA[sym]
    elif sym == '...data.0': a = FRAG
    elif re.fullmatch(r'@\d+', sym):
        off = sd2.get(sym)
        if off is not None:
            v = int.from_bytes(blob[off:off+4], 'big') if off+4 <= len(blob) else None
            a = ERA_SDA21.get(v)
        if a is None:
            print(f"  SDA21-MISS {sym} off={off} row {i}"); wn += 1; continue
    if a is None:
        print(f"  NAME-MISS {sym} row {i}"); wn += 1; continue
    if cls == 'R_PPC_ADDR16_HA': exp = (w & 0xFFFF0000) | ((a + 0x8000) >> 16 & 0xFFFF)
    elif cls == 'R_PPC_ADDR16_LO': exp = (w & 0xFFFF0000) | (a & 0xFFFF)
    elif cls == 'R_PPC_EMB_SDA21': exp = (w & 0xFFFF0000) | ((a - R13) & 0xFFFF)
    elif cls == 'R_PPC_REL24': exp = (w & ~0x03FFFFFC) | ((((a - addr) >> 2) & 0xFFFFFF) << 2)
    else: exp = None
    got = int(''.join(O[i][1]), 16)
    if exp == got: wok += 1
    else:
        wn += 1
        if wn <= 12: print(f"  LINKDIFF [{i}] {hex(addr)} {cls} {sym}: exp={hex(exp if exp else 0)} orig={hex(got)}")
print(f"linked-word proof: {wok}/{len(linkrows)} MATCH ({wn} diff)")

ca = [canon_orig(r[2]) for r in O]
cb = [canon(r[2], r) for r in U]
mo, mu = Counter(ca), Counter(cb)
same = sum((mo & mu).values())
print(f"content multiset: {same}/{max(len(O),len(U))}  orig-only={len(mo-mu)} ours-only={len(mu-mo)}")
d1 = Counter(mo - mu); d2 = Counter(mu - mo)
print("  orig-only sample:", list(d1.items())[:10])
print("  ours-only sample:", list(d2.items())[:10])
print(f"positional LCS: {lcs(ca, cb)}/{min(len(ca),len(cb))}")
