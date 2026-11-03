#!/usr/bin/env python3
"""f3 p7 row-map final: slot space + shift decomposition.
(c) split: 'shift' = normalized instruction exists in OURS window +-12 (order/LCS artifact);
'true-value' = no nearby counterpart."""
import re, json
from collections import Counter

REPO = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3"
ERA_S = f"{REPO}/build/GPOE8P/asm/pso/object/TObjCMName.s"
OURS_ASM = f"{REPO}/perm-tests/f3_hairmenu_ours_p2.asm"
SCORE = f"{REPO}/perm-tests/f3_hairmenu_p7_score_base.txt"

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
        if hm: in_fn = 'render__14TObjCMHairMenuFv' in hm.group(1); continue
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

MASK = 0x03E00000 | 0x001F0000 | 0x0000F800
def mask_regs(w): return w & ~MASK

def norm(mn, op, reloc, word):
    mn = fix_artifact(mn, word)
    if reloc:
        rt, sym = reloc
        if rt == 'R_PPC_REL24': return f"{mn} {sym}"
        if 'SDA21' in rt:       return f"{mn} R S21"
        if rt == 'R_PPC_ADDR16_HA': return f"{mn} R HA"
        if rt in ('R_PPC_ADDR16_LO','R_PPC_ADDR16_LA'): return f"{mn} R R LO"
    op = re.sub(r'@\s*sda21\s*\(\s*r0\s*\)', '@sda21', op)
    if '@sda21' in op: return f"{mn} R S21"
    if '@ha' in op:    return f"{mn} R HA"
    if re.search(r'@l\b', op): return f"{mn} R R LO"
    op = op.replace('(', ' ').replace(')', ' ')
    op = re.sub(r'<[^>]*>', ' ', op)   # objdump cosmetic <sym+off> annotations
    t = []
    for tok in re.split(r'[\s,]+', op):
        if not tok: continue
        if re.fullmatch(r'[rf]\d+', tok): t.append('R')
        elif re.fullmatch(r'0x[0-9A-Fa-f]+|-?\d+', tok): t.append(str(int(tok,0)))
        elif tok == 'qr0': t.append('0')
        elif '@' in tok or tok.startswith('lbl_') or re.fullmatch(r'[0-9a-f]{4,}', tok): t.append('S')
        else: t.append(tok)
    k = ' '.join(t)
    if reloc:
        rt, sym = reloc
        if rt == 'R_PPC_REL24': k = sym
        elif 'SDA21' in rt: k = "S21"          # pool REF regardless of name: display-only
        elif 'ADDR16' in rt: k = "A16"
    return f"{mn} {k}"

era = era_rows(); ours = ours_rows()
assert len(era) == len(ours) == 460
ek = [norm(e[2], e[3], None, e[1]) for e in era]
ok = [norm(u[2], u[3], u[4], u[1]) for u in ours]

rows = []
for line in open(SCORE):
    mm = re.match(r'\s+slot\s*(\d+) O: (.*?)\s+N: (.*?)\s*$', line)
    if mm: rows.append(int(mm.group(1)))
rows.sort()

cls = {"a":[], "b":[], "c_shift":[], "c_true":[], "d":[]}
cen = Counter()
W = 12
for slot in rows:
    e = era[slot]; u = ours[slot]
    ew, uw = e[1], u[1]
    emn, omn = fix_artifact(e[2], ew), fix_artifact(u[2], uw)
    reloc = u[4]
    ha = bool(re.search(r'@(ha|l)\b', e[3])) or bool(re.search(r'@(ha|l)\b', u[3])) or \
         (reloc and reloc[0] in ("R_PPC_ADDR16_HA","R_PPC_ADDR16_LO"))
    pool = bool(reloc and "SDA21" in reloc[0] and reloc[1].startswith("@"))
    eregs = re.findall(r'\b([rf]\d+)\b', e[3]); uregs = re.findall(r'\b([rf]\d+)\b', u[3])
    same_len = emn == omn and len(eregs) == len(uregs) and eregs and uregs
    if same_len:
        for a_,b_ in zip(eregs,uregs):
            if a_ != b_: cen[(a_,b_)] += 1
    regdiff = same_len and eregs != uregs
    if ha:
        c, why = "d", "@ha/@l" + ("+color" if regdiff else "")
    elif ew == uw:
        c, why = "b", "word-identical(artifact)"
    elif pool and emn == omn and not regdiff:
        c, why = "b", f"pool-name-only({reloc[1]})"
    elif pool and emn == omn and regdiff:
        c, why = "b", f"pool+color({reloc[1]})"
    elif emn == omn and mask_regs(ew) == mask_regs(uw) and regdiff:
        c, why = "a", "reg-color-only"
    else:
        # shift decomposition: does ek[slot] appear in ours window (or ok[slot] in era window)?
        lo, hi = max(0,slot-W), min(460,slot+W+1)
        shifted = (ek[slot] in ok[lo:hi] and ek[slot] != ok[slot]) or (ok[slot] in ek[lo:hi] and ek[slot] != ok[slot])
        c, why = ("c_shift","order/window-shift(near-match +-12)") if shifted else ("c_true","TRUE value diff")
    cls[c].append((why, slot, f"O-{slot:3d} {e[2]:8s} {e[3]}", f"N-{slot:3d} {u[2]:8s} {u[3]}  r={reloc}"))

tot = sum(len(v) for v in cls.values())
print(f"one_shot rows={len(rows)} (parsed {tot})")
print(f"  (a) pure-color      = {len(cls['a']):3d}")
print(f"  (b) @NNN/pool/disp  = {len(cls['b']):3d}  (hybrids incl {sum(1 for w,*_ in cls['b'] if 'pool+color' in w)})")
print(f"  (c) value/order     = {len(cls['c_shift'])+len(cls['c_true']):3d}  [shift={len(cls['c_shift'])} TRUE={len(cls['c_true'])}]")
print(f"  (d) link @ha/@l     = {len(cls['d']):3d}")
print("\nCOLOR CENSUS (era->ours):")
print("GPR:", dict(Counter({k:v for k,v in cen.items() if k[0][0]=='r'})))
print("FPR:", dict(sorted(((k,v) for k,v in cen.items() if k[0][0]=='f'), key=lambda x:-x[1])))

with open(f"{REPO}/perm-tests/f3_hairmenu_p7_rows.txt","w") as f:
    f.write("f3 p7 ROW MAP @ champ 4cf63208 (460w gate-exact 0x730, stmw r23, one_shot 84.097824)\n")
    f.write(f"official slot rows={len(rows)}: a={len(cls['a'])} b={len(cls['b'])} c={len(cls['c_shift'])+len(cls['c_true'])} (shift {len(cls['c_shift'])} / TRUE {len(cls['c_true'])}) d={len(cls['d'])}\n")
    f.write("aligner LCS(reg-masked) crosscheck=328: pool/display~84 value/order~107 @ha/@l~24, color invisible under masking\n")
    f.write("\n--- COLOR CENSUS era->ours (same-mnemonic rows, excl @ha/@l) ---\n")
    for k,v in cen.most_common(): f.write(f"  {v:3d}x {k[0]}->{k[1]}\n")
    for c in ["a","b","d","c_true","c_shift"]:
        f.write(f"\n######## CLASS {c} n={len(cls[c])} ########\n")
        for why, slot, eo, no in cls[c]:
            f.write(f"[{why}] {eo}\n          {no}\n")
print("\nwrote perm-tests/f3_hairmenu_p7_rows.txt")
if cls["c_true"]:
    print("\n--- TRUE VALUE-DIFF ROWS (each = ASK/claim datum) ---")
    for w,s,eo,no in cls["c_true"]:
        print(f"{eo}\n{'':11}{no}")
