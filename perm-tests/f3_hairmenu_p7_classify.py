#!/usr/bin/env python3
"""f3 p7: classify aligner diff rows into 4 classes:
 (a) pure-color permutation  (b) @NNN pool/display-only
 (c) real value-diff         (d) link-resident @ha/@l
Method: pair O/N rows per replace hunk (equal spans) or LCS-offset pairing for
insert/delete; compare instruction WORDS (era .s hex vs ours objdump hex).
word-equal -> display artifact (b). reg-fields-only diff -> (a).
ours SDA21 @NNN pool ref vs era lbl -> (b). @ha/@l -> (d). else (c)."""
import re, sys

REPO = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3"
ERA_S = f"{REPO}/build/GPOE8P/asm/pso/object/TObjCMName.s"
OURS_ASM = f"{REPO}/perm-tests/f3_hairmenu_ours_p2.asm"

def era_rows():
    rows, in_fn = [], False
    for line in open(ERA_S):
        if line.startswith('.fn render__14TObjCMHairMenuFv'): in_fn = True; continue
        if in_fn and line.startswith('.endfn'): break
        if not in_fn: continue
        mm = re.match(r'/\* ([0-9A-F]{8}) \S+\s+((?:[0-9A-F]{2} ){3}[0-9A-F]{2})\s*\*/\s+(\S+)\s*(.*)', line)
        if mm: rows.append((mm.group(1), int(mm.group(2).replace(" ",""),16), mm.group(3), mm.group(4).strip()))
    return rows

def ours_rows():
    rows, in_fn, pend = [], False, None
    for line in open(OURS_ASM):
        hm = re.match(r'^[0-9a-f]+ <(.*)>:', line)
        if hm:
            in_fn = 'render__14TObjCMHairMenuFv' in hm.group(1); continue
        if not in_fn: continue
        mm = re.match(r'\s+([0-9a-f]+):\t([0-9a-f ]+?)\t(\S+)\s*(.*)', line)
        if mm:
            rows.append([mm.group(1), int(mm.group(2).replace(" ",""),16), mm.group(3), mm.group(4).strip(), None]); pend=len(rows)-1
        else:
            m3 = re.match(r'\s+([0-9a-f]+):\s+(R_PPC_\S+)\s*(\S*)', line)
            if m3 and pend is not None: rows[pend][4] = (m3.group(2), m3.group(3))
    return rows

def fix_artifact(mn, word):
    top = word >> 26
    if mn in ("xxsel","xsmaddadp","xsmsubmsp","xxsel-") and top == 60: return "psq_st"
    if mn == "lq" and top == 56: return "psq_l"
    return mn

def norm(mn, op, word, reloc):
    mn = fix_artifact(mn, word)
    op = op.replace('(', ' ').replace(')', ' ')
    t = []
    for tok in re.split(r'[\s,]+', op):
        if not tok: continue
        if re.fullmatch(r'[rf]\d+', tok): t.append('R')
        elif re.fullmatch(r'0x[0-9A-Fa-f]+|-?\d+', tok): t.append(str(int(tok,0)))
        elif tok == 'qr0': t.append('0')
        elif '@' in tok or tok.startswith('lbl_') or tok.startswith('.L') or re.fullmatch(r'[0-9a-f]{4,}', tok): t.append('S')
        else: t.append(tok)
    k = ' '.join(t)
    if reloc:
        rt, sym = reloc
        if rt == 'R_PPC_REL24': k = sym
        elif 'SDA21' in rt: k = f"S21:{sym.split('+')[0]}+{sym.split('+')[1] if '+' in sym else '?'}"
        elif 'ADDR16' in rt: k = f"@{sym}"
        elif 'REL' in rt: k = "S"
    return f"{mn} {k}"

# reg-field mask: GPR/FR fields at bits 25-21(RS? actually RT 25-21, RA 20-16, RB 15-11)
def mask_regs(w):
    keep = 0xFC0003FF  # clear RT(21-25), RA(16-20), RB(11-15)? careful big-endian bit numbering
    # PPC word: bits 0..31 from MSB. RT=6..10, RA=11..15, RB=16..20, FXM=12..19(bcr)
    # in LSB-numbered int: RT at bits 21..25 (mask 0x03E00000), RA bits 16..20 (0x001F0000), RB bits 11..15 (0x0000F800)
    return w & ~(0x03E00000 | 0x001F0000 | 0x0000F800)

era = era_rows(); ours = ours_rows()
ek = [norm(m,o,w,None) for _,w,m,o in era]
ok = [norm(r[2],r[3],r[1],r[4]) for r in ours]
import difflib
sm = difflib.SequenceMatcher(None, ek, ok, autojunk=False)

def is_ha_l(row_era, row_ours):
    for s in (row_era[3] if row_era else "", (row_ours[3] if row_ours else "") + " " + (row_ours[4][1] if row_ours and row_ours[4] else "")):
        if re.search(r'@(ha|l)\b', s) or (row_ours and row_ours[4] and row_ours[4][0] in ("R_PPC_ADDR16_HA","R_PPC_ADDR16_LO")):
            return True
    return False

cls = {"a":[], "b":[], "c":[], "d":[]}
pending_pairs = []
unpaired = []
for tag,i1,i2,j1,j2 in sm.get_opcodes():
    if tag == 'equal': continue
    if tag == 'replace':
        if (i2-i1) == (j2-j1):
            for s in range(i2-i1): pending_pairs.append(((i1+s),(j1+s),tag))
        else:
            # unequal replace: pair by offset while both exist; leftover unpaired
            n = min(i2-i1, j2-j1)
            for s in range(n): pending_pairs.append(((i1+s),(j1+s),tag))
            for s in range(n, i2-i1): unpaired.append((("O",i1+s),tag))
            for s in range(n, j2-j1): unpaired.append((("N",j1+s),tag))
    elif tag == 'delete':
        for s in range(i1,i2): unpaired.append((("O",s),tag))
    elif tag == 'insert':
        for s in range(j1,j2): unpaired.append((("N",s),tag))

for ei, oj, tag in pending_pairs:
    ew, ow = era[ei][1], ours[oj][1]
    emn, omn = fix_artifact(era[ei][2], ew), fix_artifact(ours[oj][2], ow)
    erec, orec = era[ei], ours[oj]
    reloc = orec[4]
    # (d) link-resident @ha/@l
    ha = ('@ha' in erec[3] or '@l' in erec[3]) or (reloc and reloc[0] in ("R_PPC_ADDR16_HA","R_PPC_ADDR16_LO"))
    # (b) display-only: words equal OR pool-name-only diff
    if ew == ow:
        c = "b"; why = "word-identical(objdump-artifact)"
    elif emn == omn and mask_regs(ew) == mask_regs(ow):
        c = "a"; why = "reg-fields-only"
    elif (reloc and "SDA21" in reloc[0] and reloc[1].startswith("@")) and emn == omn:
        c = "b"; why = f"@NNN-pool({reloc[1]})"
        if ha: c = "d"; why = "@ha/@l " + why
    elif ha:
        c = "d"; why = "@ha/@l"
    else:
        c = "c"; why = "value/mnemonic diff"
    rec = (c, why, ei, oj, f"O-{ei:3d} {erec[0]}: {erec[2]:8s} {erec[3]}",
                 f"N-{oj:3d} {orec[2]:8s} {orec[3]}  r={reloc}")
    cls[c].append(rec)

for (side, idx), tag in unpaired:
    r = era[idx] if side=="O" else ours[idx]
    txt = f"{side}-{idx:3d} {r[0]}: {r[2]:8s} {r[3]}" + (f"  r={r[4]}" if side=="N" else "")
    ha = ('@ha' in r[3]) or ('@l' in r[3]) or (side=="N" and r[4] and r[4][0] in ("R_PPC_ADDR16_HA","R_PPC_ADDR16_LO"))
    pool = side=="N" and r[4] and "SDA21" in r[4][0] and r[4][1].startswith("@")
    c = "d" if ha else ("b" if pool else "c")
    cls[c].append((c, f"unpaired-{tag}-{side}", idx, idx, txt if side=="O" else "", txt if side=="N" else ""))

print(f"CLASS COUNTS: a={len(cls['a'])} b={len(cls['b'])} c={len(cls['c'])} d={len(cls['d'])} TOTAL={sum(len(v) for v in cls.values())}")
print(f"pairs={len(pending_pairs)} unpaired={len(unpaired)}")
# sub-buckets of a: build remap table per pair
from collections import Counter
remaps = Counter()
for c,why,ei,oj,eo,no in cls['a']:
    ew, ow = era[ei][1], ours[oj][1]
    def regs(w): return ((w>>21)&31,(w>>16)&31,(w>>11)&31)
    remaps[(fix_artifact(era[ei][2],ew), regs(ew), regs(ow))]+=1
print("\n--- (a) COLOR REMAP TABLE (mnemonic, era RT/RA/RB, ours RT/RA/RB) ---")
for k,v in remaps.most_common(): print(f"  {v:3d}x {k[0]:8s} era={k[1]} -> ours={k[2]}")
with open(f"{REPO}/perm-tests/f3_hairmenu_p7_rows.txt","w") as f:
    for c in "abcd":
        f.write(f"\n######## CLASS ({c}) n={len(cls[c])} ########\n")
        for cc,why,ei,oj,eo,no in cls[c]:
            f.write(f"[{why}] {eo}\n          {no}\n")
print(f"\nfull rows written to perm-tests/f3_hairmenu_p7_rows.txt")
# print class c inline (the claims)
print("\n--- (c) REAL VALUE-DIFF ROWS ---")
for cc,why,ei,oj,eo,no in cls['c']:
    print(f"[{why}]\n{eo}\n{no}")
