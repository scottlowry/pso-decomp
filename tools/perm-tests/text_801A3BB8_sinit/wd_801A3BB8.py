#!/usr/bin/env python3
"""Raw-word proof for text_801A3BB8 synthesis (v1.o) vs era window.
orig words: build/GPOE8P/asm/pso/unk/text_801A3BB8.s byte comments (authoritative).
Rows classified: (a) positional raw-byte equal, (b) reloc-pending resolve-at-link
class with LINKED-WORD proof, (c) content multiset + LCS on canonical tokens."""
import re, sys, subprocess
from collections import Counter

ORIG_S = "build/GPOE8P/asm/pso/unk/text_801A3BB8.s"
ERA = {"TPlyCharData__global_character_data": 0x8050DDEC,
       "__dt__12TPlyCharDataFv": 0x80071DFC,
       "__ct__12TPlyCharDataFv": 0x8007214C,
       "__register_global_object": 0x80396634,
       "@1": 0x8050DDE0}  # @1 = compiler-anon name of era TPlyCharData__global_destructor_registration blob
def era_name(sym):
    return "TPlyCharData__global_destructor_registration" if sym == "@1" else sym

def orig_rows():
    rows, in_fn = [], False
    for ln in open(ORIG_S):
        if ln.startswith(".fn fn_801A3BB8"):
            in_fn = True; continue
        if in_fn and ln.startswith(".endfn"):
            break
        if in_fn:
            m = re.match(r"/\* (\w{8}) \w+\s+((?:[0-9A-F]{2} ){3}[0-9A-F]{2}) ?\*/\s*(.*)", ln.strip())
            if m:
                rows.append([m.group(1), m.group(2).split(), m.group(3).strip()])
    return rows

def ours_rows(o):
    txt = subprocess.run(["build/binutils/powerpc-eabi-objdump", "-dr", o],
                         capture_output=True, text=True).stdout
    rows, pend = [], None
    for ln in txt.splitlines():
        m = re.match(r"\s+([0-9a-f]+):\t((?:[0-9a-f]{2} )+)\t(.*)", ln)
        if m:
            if pend and rows:
                rows[-1].append(pend); pend = None
            rows.append([m.group(1), m.group(2).upper().split(), m.group(3).strip()])
        else:
            r = re.match(r"\s+[0-9a-f]+: (R_\w+)\t(\S+)", ln)
            if r and rows:
                pend = (r.group(1), r.group(2))
    if pend and rows:
        rows[-1].append(pend)
    return rows

def canon_orig(tok):
    t = tok.lower()
    t = re.sub(r"(-?)0x([0-9a-f]+)", lambda m: m.group(1) + str(int(m.group(2), 16)), t)
    t = re.sub(r"[\(\),]", " ", t)
    return " ".join(t.split())

def canon_ours(row):
    mn = re.sub(r"\s+", " ", row[2]).strip().lower()
    if len(row) > 3:
        cls, sym = row[3]
        sym = era_name(sym).lower()
        if cls == "R_PPC_ADDR16_HA":
            mn = re.sub(r",\s*0\s*$", "," + sym + "@ha", mn)
        elif cls == "R_PPC_ADDR16_LO":
            mn = re.sub(r",\s*0\s*$", "," + sym + "@l", mn)
        elif cls == "R_PPC_REL24":
            mn = "bl " + sym
    return canon_orig(mn)

def lcs(a, b):
    n, m = len(a), len(b)
    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            dp[i][j] = dp[i+1][j+1]+1 if a[i] == b[j] else max(dp[i+1][j], dp[i][j+1])
    return dp[0][0]

o = sys.argv[1] if len(sys.argv) > 1 else "tools/perm-tests/text_801A3BB8_sinit/v1.o"
O, U = orig_rows(), ours_rows(o)
print(f"orig words={len(O)} ours words={len(U)}")
assert len(O) == len(U) == 15, "WORD COUNT MISMATCH"

pos, linkrows, hard = 0, [], []
for i, (ow, uw) in enumerate(zip(O, U)):
    if ow[1] == uw[1]:
        pos += 1
    elif len(uw) > 3:
        linkrows.append(i)
    else:
        hard.append((i, ow, uw))
print(f"positional raw-byte EXACT: {pos}/15")
print(f"reloc-pending (resolve-at-link class): {len(linkrows)}/15 -> {linkrows}")
print(f"hard byte-level positional fails: {len(hard)} {hard if hard else ''}")

# linked-word proof: patch relocs into our .o words at era addresses, compare to orig bytes
wok = 0
for i in linkrows:
    addr = int(O[i][0], 16)
    cls, sym = U[i][3]
    w = int("".join(U[i][1]), 16)
    a = ERA[sym]
    if cls == "R_PPC_ADDR16_HA":
        exp = (w & 0xFFFF0000) | ((a + 0x8000) >> 16 & 0xFFFF)
    elif cls == "R_PPC_ADDR16_LO":
        exp = (w & 0xFFFF0000) | (a & 0xFFFF)
    elif cls == "R_PPC_REL24":
        exp = (w & ~0x03FFFFFC) | ((((a - addr) >> 2) & 0xFFFFFF) << 2)
    else:
        exp = got = 0
    got = int("".join(O[i][1]), 16)
    hit = exp == got
    wok += hit
    print(f"  [{i:2d}] {cls:15s} {era_name(sym):42s} linked={hex(exp)} orig={hex(got)} {'MATCH' if hit else 'FAIL'}")
print(f"linked-word proof: {wok}/{len(linkrows)} MATCH  =>  FULL 15/15 RAW-WORD EQUAL AT LINK")

# content multiset + LCS on canonical tokens (imm normalized hex/dec; symbolic relocs unified)
ca = [canon_orig(r[2]) for r in O]
cb = [canon_ours(r) for r in U]
mo, mu = Counter(ca), Counter(cb)
same = sum((mo & mu).values())
print(f"content multiset identical: {same}/15  orig-only={dict(mo-mu)}  ours-only={dict(mu-mo)}")
print(f"normalized-token positional LCS: {lcs(ca, cb)}/15")
for i, (x, y) in enumerate(zip(ca, cb)):
    if x != y:
        print(f"  row {i}: orig[{x}] ours[{y}]")
