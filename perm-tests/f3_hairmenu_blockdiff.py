#!/usr/bin/env python3
"""Block-staged structural triage for render__14TObjCMHairMenuFv.
- era rows: build/GPOE8P/asm/pso/object/TObjCMName.s .fn render__14TObjCMHairMenuFv block (has raw words + names)
- ours rows: objdump -dr of our unit .o (words + reloc names on following lines)
Normalization: pool refs resolved by VALUE (era lbl table from .sdata2 emission; ours @NNN from .o .sdata2 hex dump),
registers -> role tokens, branch targets -> order-ids. Prints LCS-aligned REAL diff regions (ins/del/operand).
Usage: python3 f3_hairmenu_blockdiff.py
"""
import re, subprocess, sys, struct

REPO = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3"
ERA_S = f"{REPO}/build/GPOE8P/asm/pso/object/TObjCMName.s"
OURS_ASM = f"{REPO}/perm-tests/f3_hairmenu_ours_resume3.asm"

# ---- era pool: label -> float value
era_lbl_val = {}
txt = open(ERA_S).read()
m = re.search(r'\.section \.sdata2.*', txt, re.S)
sec = m.group(0)
for mm in re.finditer(r'\.obj (lbl_\w+|TObj\w+_\w+), global.*?\n(?:.*?\n)*?\s*\.(float|double|4byte)\s+(\S+)', sec):
    era_lbl_val[mm.group(1)] = (mm.group(2), mm.group(3))
era_addr_lbl = {}
for mm in re.finditer(r'# \.sdata2:0x[0-9A-Fa-f]+ \| (0x805DD\w+) \| size', sec):
    era_addr_lbl[mm.group(1)] = None
for mm in re.finditer(r'\.obj (\w+), global\n# (0x805DD\w+)', sec):
    era_addr_lbl[mm.group(2)] = mm.group(1)

# ---- ours pool: @NNN -> value, via readelf/a.out .sdata2 contents + rela
def ours_pool_values():
    out = subprocess.run(["/opt/homebrew/opt/binutils/bin/objdump", "-s", "-j", ".sdata2",
                          f"{REPO}/build/GPOE8P/src/pso/object/TObjCMName.o"], capture_output=True, text=True).stdout
    data = {}
    for line in out.splitlines():
        mm = re.match(r'\s+([0-9a-f]{4,8}) ((?:[0-9a-f]{2,4} ){1,4})', line)
        if mm:
            addr = int(mm.group(1), 16)
            hexb = mm.group(2).replace(" ", "")
            raw = bytes.fromhex(hexb)
            for i in range(0, len(raw) - 3, 4):
                data[addr + i] = struct.unpack(">f", raw[i:i+4])[0]
    # symbol table for @NNN offsets
    sy = subprocess.run(["/opt/homebrew/opt/binutils/bin/gnm", "-A",
                         f"{REPO}/build/GPOE8P/src/pso/object/TObjCMName.o"], capture_output=True, text=True).stdout
    mp = {}
    for line in sy.splitlines():
        mm = re.search(r'(\w*@[0-9]+|lbl_\w+|TObj\w+)\s+.*\b[aA]\b', line)
    # fallback: readelf symtab
    re_out = subprocess.run(["/opt/homebrew/opt/binutils/bin/readelf", "-sW",
                             f"{REPO}/build/GPOE8P/src/pso/object/TObjCMName.o"], capture_output=True, text=True).stdout
    for line in re_out.splitlines():
        mm = re.match(r'\s*\d+:\s+([0-9a-f]+)\s+\d+\s+\w+\s+\w+\s+\w+\s+(\S+)\s+(\S+)', line)
        if mm and mm.group(3).startswith('@'):
            try:
                mp[mm.group(3)] = data.get(int(mm.group(1), 16))
            except Exception:
                pass
    return mp
ours_pool = ours_pool_values()

def norm_era(mnem, ops):
    ops = ops.strip()
    ops = re.sub(r'(lbl_\w+|TObj\w+)_?805D\w*@sda21\(r0\)', lambda m: 'P%s' % (m.group(0)), ops)
    ops = re.sub(r'r\d+|f\d+|fr\d+|vs\d+', 'R', ops)
    ops = re.sub(r'cr\d+', 'CR', ops)
    return mnem + " " + re.sub(r'0x[0-9a-f]+', lambda m: m.group(0), ops)

def load_era():
    rows = []
    in_fn = False
    for line in open(ERA_S):
        if line.startswith('.fn render__14TObjCMHairMenuFv'):
            in_fn = True; continue
        if in_fn and line.startswith('.endfn'):
            break
        if not in_fn: continue
        mm = re.match(r'/\* ([0-9A-F]{8}) \S+\s+([0-9A-F ]+)\*/\s+(\S+)(.*)', line)
        if mm:
            addr, words, mn, ops = mm.group(1), mm.group(2).replace(" ","").lower(), mm.group(3), mm.group(4)
            p = re.search(r'(\w+)@sda21', ops)
            val = None
            if p:
                lbl = p.group(1)
                if lbl in era_lbl_val:
                    v = era_lbl_val[lbl][1]
                    try: val = float(v)
                    except: val = v
            rows.append((addr, words, mn, ops.strip(), val, 'era'))
    return rows

def load_ours():
    rows = []
    cur_reloc = None
    pend = []
    for line in open(OURS_ASM):
        mm = re.match(r'\s+([0-9a-f]+):\t([0-9a-f ]{4,16})\t(\S+)\s*(.*)', line)
        if mm:
            addr, words, mn, ops = mm.group(1), mm.group(2).replace(" ",""), mm.group(3), mm.group(4).strip()
            rows.append([addr, words, mn, ops, None, 'ours', False])
            m2 = re.search(r'@(\d+)@sda21', ops)
            if m2:
                rows[-1][4] = ours_pool.get('@' + m2.group(1))
                rows[-1][6] = True
        else:
            m3 = re.match(r'\s+R_PPC_EMB_SDA21\s+\S*?(@\d+|\w+)', line)
            if m3: pass
    return rows

def key(row):
    mn, ops, val = row[2], row[3], row[4]
    if val is not None and ('sda21' in ops or row[5]=='ours' and mn.startswith('lfs') and False):
        pass
    o = ops
    if 'sda21' in o or (val is not None and mn.startswith('lfs') and 'r2(' in o):
        o = re.sub(r'[^,]*sda21.*', 'POOLV%s' % val, o)
    elif val is not None and row[6]:
        o = re.sub(r'@ *\d+ *@sda21.*', 'POOLV%s' % val, o)
    o = re.sub(r'\br\d+\b', 'R', o)
    o = re.sub(r'\bf\d+\b', 'F', o)
    o = re.sub(r'\bvs\d+\b', 'V', o)
    o = re.sub(r'0x[0-9a-fA-F]+', lambda m: str(int(m.group(0),16)), o)
    return (mn.strip(), re.sub(r'\s+', '', o))

era = load_era()
ours = load_ours()
ek = [key(r) for r in era]
ok = [key(r) for r in ours]
print(f"era rows {len(era)}  ours rows {len(ours)}")

# LCS
n, m_ = len(ek), len(ok)
if n*m_ > 4_000_000:
    print("too big"); sys.exit()
dp = [[0]*(m_+1) for _ in range(n+1)]
for i in range(n-1, -1, -1):
    di, dn = dp[i], dp[i+1]
    for j in range(m_-1, -1, -1):
        di[j] = dn[j+1]+1 if ek[i]==ok[j] else max(dn[j], di[j+1])
i = j = 0
diffs = []
while i < n and j < m_:
    if ek[i] == ok[j]:
        i += 1; j += 1
    elif dp[i+1][j] >= dp[i][j+1]:
        diffs.append(('DEL', i, era[i])); i += 1
    else:
        diffs.append(('INS', j, ours[j])); j += 1
while i < n: diffs.append(('DEL', i, era[i])); i+=1
while j < m_: diffs.append(('INS', j, ours[j])); j+=1
# coalesce adjacent ops into regions
regions = []
for op, idx, row in diffs:
    if regions and regions[-1][0] == op and regions[-1][1] == idx - regions[-1][2]:
        regions[-1][2] += 1
    else:
        regions.append([op, idx, 1])
matched = n - len([d for d in diffs if d[0]=='DEL'])
print(f"normalized-LCS matched {matched}/{n} = {100*matched/n:.2f}%  regions={len(regions)}")
for op, idx, cnt in regions:
    print(f"--- {op} {cnt} at era/ours slot {idx}:")
    rows = era[idx:idx+cnt] if op=='DEL' else ours[idx:idx+cnt]
    for r in rows[:12]:
        print("   ", r[0], r[1], r[2], r[3])
