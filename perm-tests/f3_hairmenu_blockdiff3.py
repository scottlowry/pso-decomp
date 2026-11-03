#!/usr/bin/env python3
"""f3 HairMenu render: structural diff via masked machine words.
era: build .s resolved words. ours: objdump -dr words + reloc types/names.
equal(a,b) iff: (mnemonic-class of b matches a) AND masked-words equal AND
reloc-semantics tuple equal (SDA21 by float value, others by symbol name).
Prints REAL diff regions with slot indices.
"""
import re, struct, subprocess

REPO = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3"
ERA_S = f"{REPO}/build/GPOE8P/asm/pso/object/TObjCMName.s"
OURS_ASM = f"{REPO}/perm-tests/f3_hairmenu_ours_resume3.asm"

era_val = {}
txt = open(ERA_S).read()
sec = txt[txt.index('.section .sdata2'):]
for mm in re.finditer(r'\.obj (\S+), global\n(?:[^\n]*\n)*?\s*\.(?:float|double|4byte)\s+(\S+)', sec):
    try: era_val[mm.group(1)] = struct.unpack(">f", struct.pack(">f", float(mm.group(2))))[0]
    except ValueError: era_val[mm.group(1)] = mm.group(2)

def era_rows():
    rows = []
    in_fn = False
    for line in open(ERA_S):
        if line.startswith('.fn render__14TObjCMHairMenuFv'):
            in_fn = True; continue
        if in_fn and line.startswith('.endfn'):
            break
        if not in_fn: continue
        mm = re.match(r'/\* ([0-9A-F]{8}) \S+\s+((?:[0-9A-F]{2} ){3}[0-9A-F]{2})\s*\*/\s+(\S+)(.*)', line)
        if mm:
            rows.append((mm.group(1), int(mm.group(2).replace(" ", ""), 16), mm.group(3), mm.group(4).strip()))
    return rows

def ours_rows():
    rows = []
    relocs = {}
    cur = None
    for line in open(OURS_ASM):
        mm = re.match(r'\s+([0-9a-f]+):\t([0-9a-f ]+?)\t(\S+)\s*(.*)', line)
        if mm:
            cur = mm.group(1)
            rows.append([cur, int(mm.group(2).replace(" ", ""), 16), mm.group(3), mm.group(4).strip()])
        else:
            m3 = re.match(r'\s+([0-9a-f]+):\s+(R_PPC_\S+)\s+(\S+)', line)
            if m3:
                relocs[m3.group(1)] = (m3.group(2), m3.group(3))
    return rows, relocs

def ours_pool_map():
    o = f"{REPO}/build/GPOE8P/src/pso/object/TObjCMName.o"
    dump = subprocess.run(["/opt/homebrew/opt/binutils/bin/objdump", "-s", "-j", ".sdata2", o],
                          capture_output=True, text=True).stdout
    byts = {}
    for line in dump.splitlines():
        mm = re.match(r'\s+([0-9a-f]{4,8})((?: +[0-9a-f]{2,8})+)', line)
        if mm:
            a = int(mm.group(1), 16)
            raw = bytes.fromhex(mm.group(2).replace(" ", ""))
            for k, b in enumerate(raw):
                byts[a + k] = b
    sy = subprocess.run(["/opt/homebrew/opt/binutils/bin/readelf", "-sW", o], capture_output=True, text=True).stdout
    mp = {}
    for line in sy.splitlines():
        mm = re.match(r'\s*\d+:\s+([0-9a-f]+)\s+\d+\s+\w+\s+\w+\s+\w+\s+\S+\s+(\S+)', line)
        if mm and mm.group(2).startswith('@'):
            mp[mm.group(2)] = struct.unpack(">f", bytes(byts.get(int(mm.group(1), 16) + k, 0) for k in range(4)))[0]
    return mp
POOLV = ours_pool_map()

BR = {"b", "bl", "beq", "bne", "blt", "bgt", "ble", "bge", "bdnz", "bdz", "bne-", "beq+", "b+", "bl+"}
MASK = {"R_PPC_REL24": 0x03FFFFFC, "R_PPC_EMB_SDA21": 0x0000FFFF, "R_PPC_ADDR16_HA": 0x0000FFFF,
        "R_PPC_ADDR16_LO": 0x0000FFFF, "R_PPC_ADDR16_DS": 0x0000FFFE, "R_PPC_ADDR16_DQM": 0x0000E000,
        "R_PPC_ADDR16_DFP16": 0x0000FFFF, "R_PPC_ADDR16_DFP18": 0x000CFFFE}
OPM = 0xFC000000  # primary opcode

def sem_era(mn, ops, word):
    s = []
    pool = re.search(r'(\S+?)@sda21', ops)
    if pool: s.append(('P', era_val.get(pool.group(1), pool.group(1))))
    arr = re.search(r'(\S+?)@(ha|l)', ops)
    if arr: s.append(('A', arr.group(1)))
    if mn in BR or ops.startswith('.'):
        if mn == 'bl': s.append(('B', ops.split()[0] if ops else '?'))
        else: s.append(('B', mn))
    w = word
    for typ in (MASK,):
        pass
    if pool: w &= ~MASK["R_PPC_EMB_SDA21"]
    if arr: w &= ~MASK["R_PPC_ADDR16_HA"]; w &= ~MASK["R_PPC_ADDR16_LO"]
    if mn in BR: w &= ~MASK["R_PPC_REL24"]
    return w, tuple(s)

def sem_ours(mn, ops, word, rel):
    s = []
    w = word
    if rel:
        typ, sym = rel
        if typ == "R_PPC_EMB_SDA21":
            key = sym if sym.startswith('@') else '@' + sym
            s.append(('P', POOLV.get(key, sym)))
        elif typ in ("R_PPC_ADDR16_HA", "R_PPC_ADDR16_LO", "R_PPC_ADDR16_DS"):
            s.append(('A', sym.split()[0]))
        elif typ == "R_PPC_REL24":
            s.append(('B', sym))
        w &= ~MASK.get(typ, 0)
        if typ == "R_PPC_REL24": pass
    if mn in BR and not (rel and rel[0] == "R_PPC_REL24"):
        w &= ~MASK["R_PPC_REL24"]; s.append(('B', mn))
    return w, tuple(s)

def opcls(mn):
    return mn.split('.')[0].rstrip('+')

era = era_rows()
ours, relocs = ours_rows()
E = [(a, w, mn, ops) + sem_era(mn, ops, w) for (a, w, mn, ops) in era]
N = [(a, w, mn, ops) + sem_ours(mn, ops, w, relocs.get(a)) for (a, w, mn, ops) in ours]

def eq(ei, ni):
    a = E[ei]; b = N[ni]
    # opcode class via primary opcode of the words (era word masked vs ours word masked)
    if (a[1] & OPM) != (b[1] & OPM): return False
    # for non-relocated, non-branch insns masked words must equal incl. regs? NO — regs color-diff allowed:
    # compare masked word with REGISTER fields... too complex; use: word-equal after masking + semantics
    if a[1] != b[1]: return False
    if sorted(a[4]) != sorted(b[4]): return False
    return True

# hmm eq() with full masked-word equality fails on legit register-color diffs (r24 vs r25).
# Register bits: GPR rD=(w>>21)&31, rA=(w>>16)&31, rB=(w>>11)&31, rS=(w>>21)&31; FPR same slots.
# Zero all 5 reg fields (bits 11-15,16-20,21-25) for comparison, keep imm/others.
RFIELDS = ~(0b11111 << 11 | 0b11111 << 16 | 0b11111 << 21)
def eq2(ei, ni):
    a, b = E[ei], N[ni]
    aw, bw, as_, bs = a[4], b[4], a[5], b[5]
    if (a[1] & OPM) != (b[1] & OPM): return False
    if (aw & RFIELDS) != (bw & RFIELDS): return False
    if sorted(as_) != sorted(bs): return False
    # bl target semantics:
    ta = [x for x in as_ if x[0] == 'B']; tb = [x for x in bs if x[0] == 'B']
    if ta and tb:
        xa, xb = ta[0][1], tb[0][1]
        if xa != xb and not (xa in BR or xb in BR):
            # era renders callee name; ours reloc name
            return False
    return True

n, m_ = len(E), len(N)
if n * m_ > 9_000_000:
    print("too big", n, m_); raise SystemExit
dp = [[0] * (m_ + 1) for _ in range(n + 1)]
for i in range(n - 1, -1, -1):
    di, dn = dp[i], dp[i + 1]
    for j in range(m_ - 1, -1, -1):
        di[j] = dn[j + 1] + 1 if eq2(i, j) else max(dn[j], di[j + 1])
diffs = []
i = j = 0
while i < n and j < m_:
    if eq2(i, j): i += 1; j += 1
    elif dp[i + 1][j] >= dp[i][j + 1]: diffs.append(('DEL', i)); i += 1
    else: diffs.append(('INS', j)); j += 1
while i < n: diffs.append(('DEL', i)); i += 1
while j < m_: diffs.append(('INS', j)); j += 1
matched = n - sum(1 for d in diffs if d[0] == 'DEL')
print(f"era {n}  ours {m_}  STRUCTURAL matched {matched}/{n} = {100*matched/n:.2f}%  (unmatched era {n-matched})")
regions = []
for op, idx in diffs:
    if regions and regions[-1][0] == op and regions[-1][1] + regions[-1][2] == idx:
        regions[-1][2] += 1
    else:
        regions.append([op, idx, 1])
def fmt(side, k):
    if side == 'era':
        a, w, mn, ops = era[k][:4]; return f"E {k:3d} {a} {w:08x} {mn:8s} {ops}"
    a, w, mn, ops = ours[k][:4]; rl = relocs.get(a, ('',''))
    return f"N {k:3d} {a} {w:08x} {mn:8s} {ops}   [{rl[0][6:] if rl[0] else ''} {rl[1]}]"
for op, idx, cnt in regions:
    side = 'era' if op == 'DEL' else 'ours'
    print(f"--- {op} x{cnt} @slot{idx}:")
    seq = era if op == 'DEL' else ours
    for k in range(idx, min(idx + cnt, len(seq))):
        print("   ", fmt(side, k))
