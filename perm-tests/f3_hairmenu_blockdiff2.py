#!/usr/bin/env python3
"""Word/operand-level structural diff era .s vs ours objdump -dr (f3 HairMenu render).
Match = same instruction class + same non-register operands (pool refs by VALUE,
branches weight-0, bl by target name, data arrays by name).
Print per-BLOCK stats + REAL diff regions (structural) only.
"""
import re, struct, subprocess, sys

REPO = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3"
ERA_S = f"{REPO}/build/GPOE8P/asm/pso/object/TObjCMName.s"
OURS_ASM = f"{REPO}/perm-tests/f3_hairmenu_ours_resume3.asm"

ALIAS = {
    "psq_st": {"psq_st", "xxsel", "xsmaddadp", "xsmsubmsp", "psq_stx"},
    "psq_l": {"psq_l", "psq_lx", "lxvwrx"},
    "subic.": {"subic.", "addic."},
    "subi": {"subi", "subic", "addi"},
    "rlwinm": {"rlwinm", "clrlwi", "slwi", "srwi", "rlinm"},
}

# era sdata2 label -> value
era_val = {}
txt = open(ERA_S).read()
sec = txt[txt.index('.section .sdata2'):]
for mm in re.finditer(r'\.obj (\S+), global\n(?:[^\n]*\n)*?\s*\.(?:float|double|4byte)\s+(\S+)', sec):
    v = mm.group(2)
    try: era_val[mm.group(1)] = struct.unpack(">f", struct.pack(">f", float(v)))[0]
    except ValueError: era_val[mm.group(1)] = v

def load_era():
    rows = []
    in_fn = False
    labels = {}
    # first pass: local .L labels inside fn
    for line in open(ERA_S):
        if line.startswith('.fn render__14TObjCMHairMenuFv'):
            in_fn = True; continue
        if in_fn and line.startswith('.endfn'):
            break
        if not in_fn: continue
        mm = re.match(r'/\* ([0-9A-F]{8}) \S+\s+((?:[0-9A-F]{2} ){3}[0-9A-F]{2})\s*\*/\s*(\S+)(.*)', line)
        if not mm:
            mm2 = re.match(r'^(\.L_\w+):', line)
            if mm2: labels[mm2.group(1)] = len(rows)
    # re-scan (labels resolved lazily in canon)
    in_fn = False
    addrs = {}
    for line in open(ERA_S):
        if line.startswith('.fn render__14TObjCMHairMenuFv'):
            in_fn = True; continue
        if in_fn and line.startswith('.endfn'):
            break
        if not in_fn: continue
        mm = re.match(r'/\* ([0-9A-F]{8}) \S+\s+((?:[0-9A-F]{2} ){3}[0-9A-F]{2})\s*\*/\s+(\S+)(.*)', line)
        if mm:
            addrs[mm.group(1)] = len(rows); rows.append((mm.group(1), mm.group(2).lower(), mm.group(3), mm.group(4).strip()))
    lab_addr = {}
    in_fn = False
    for line in open(ERA_S):
        if line.startswith('.fn render__14TObjCMHairMenuFv'):
            in_fn = True; continue
        if in_fn and line.startswith('.endfn'): break
        if not in_fn: continue
        m1 = re.match(r'/\* ([0-9A-F]{8})', line)
        if m1: cur = m1.group(1)
        m2 = re.match(r'^(\.L_\w+):', line)
        if m2: lab_addr[m2.group(1)] = cur
    return rows, lab_addr

def load_ours():
    rows = []
    reloc = {}  # inst offset -> (type, sym)
    lines = open(OURS_ASM).read().splitlines()
    i = 0
    cur_off = None
    for line in lines:
        mm = re.match(r'\s+([0-9a-f]+):\t([0-9a-f ]+?)\t(\S+)\s*(.*)', line)
        if mm:
            cur_off = mm.group(1)
            rows.append([cur_off, mm.group(2).replace(" ", ""), mm.group(3), mm.group(4).strip()])
        else:
            m3 = re.match(r'\s+([0-9a-f]+):\s+(R_PPC_\S+)\s+(\S+)', line)
            if m3 and cur_off:
                reloc[cur_off] = (m3.group(2), m3.group(3))
    return rows, reloc

# ours @NNN -> value: parse symtab addrs + .sdata2 dump
def ours_pool_map():
    o = f"{REPO}/build/GPOE8P/src/pso/object/TObjCMName.o"
    dump = subprocess.run(["/opt/homebrew/opt/binutils/bin/objdump", "-s", "-j", ".sdata2", o],
                          capture_output=True, text=True).stdout
    byts = {}
    for line in dump.splitlines():
        mm = re.match(r'\s+([0-9a-f]{4,8})((?: [0-9a-f]{2,8}){1,8})', line)
        if mm:
            a = int(mm.group(1), 16)
            for k, hx in enumerate(mm.group(2).split()):
                for b in bytes.fromhex(hx):
                    byts[a + k * len(hx) // 2 if False else 0] = 0  # placeholder
            raw = bytes.fromhex(mm.group(2).replace(" ", ""))
            for k, b in enumerate(raw):
                byts[a + k] = b
    def f32(addr):
        w = bytes(byts.get(addr, 0) for _ in range(4))
        w = bytes(byts.get(addr + k, 0) for k in range(4))
        return struct.unpack(">f", w)[0]
    sy = subprocess.run(["/opt/homebrew/opt/binutils/bin/readelf", "-sW", o], capture_output=True, text=True).stdout
    mp = {}
    sec_off = None
    for line in sy.splitlines():
        mm = re.match(r'\s*\d+:\s+([0-9a-f]+)\s+\d+\s+\S+\s+\S+\s+\S+\s+(\[\s*\d+\])\s+(\S+)', line)
        if mm and mm.group(3) in ("@409",):
            pass
    # simpler: reloc-name -> value needs symtab section-relative addr; use gnm -A
    sy = subprocess.run(["/opt/homebrew/opt/binutils/bin/gnm", "-A", "-n", o], capture_output=True, text=True).stdout
    # gnm -A prints addr in hex per line for -A? fallback: parse readelf fully
    sy = subprocess.run(["/opt/homebrew/opt/binutils/bin/readelf", "-sW", o], capture_output=True, text=True).stdout
    secs = subprocess.run(["/opt/homebrew/opt/binutils/bin/readelf", "-SW", o], capture_output=True, text=True).stdout
    sd2 = None
    for line in secs.splitlines():
        if '.sdata2' in line:
            mm = re.search(r'\]\s+\S+\s+\S+\s+([0-9a-f]+)', line)
    for line in sy.splitlines():
        mm = re.match(r'\s*\d+:\s+([0-9a-f]+)\s+\d+\s+\w+\s+\w+\s+\w+\s+\w+\s+(\S+)', line)
        if mm and mm.group(2).startswith('@'):
            addr = int(mm.group(1), 16)
            mp['@' + mm.group(2)] = struct.unpack(">f", bytes(byts.get(addr + k, 0) for k in range(4)))[0]
    return mp

POOLV = ours_pool_map()

def canon_era(mn, ops, lab_addr):
    pool = re.search(r'(\S+?)@sda21', ops)
    pv = None
    if pool:
        nm = pool.group(1)
        pv = era_val.get(nm, nm)
    arr = re.search(r'(\S+?)@(?:ha|l)', ops)
    blt = re.search(r'^(\w+)', ops) if mn == 'bl' else None
    mnb = mn
    if mn.startswith('lfs') or mn == 'stfs': pass
    t = None
    if pool: t = ('P', pv)
    elif arr: t = ('A', arr.group(1), ops)
    elif mn in ('b', 'bl', 'beq', 'bne', 'blt', 'bgt', 'ble', 'bge', 'bdnz', 'bdnz', 'bc'):
        t = ('B', mn)
    regs = re.findall(r'\b[rf]\d+\b|\bcr\d+\b', ops)
    cls = 'F' if any(x.startswith('f') for x in regs) else ('R' if regs else 'N')
    imm = re.search(r'(?<![0-9a-fx])(-?0x[0-9a-f]+|\d+)\)?$|,\s*(-?\d+)($|\))', ops)
    disp = re.search(r'\((-?[0-9a-fx]+)\)', ops)
    return (mn, t, tuple('R' if r.startswith('r') else ('F' if r.startswith('f') else 'C') for r in regs),
            (disp.group(1) if disp else None))

def canon_ours(mn, ops, rel, lab):
    if rel:
        typ, sym = rel
        if typ == 'R_PPC_EMB_SDA21':
            v = POOLV.get(sym if sym.startswith('@') else '@' + sym)
            if v is None:
                # sym may be 'lbl_...' or with section marker
                v = sym
            t = ('P', v)
        elif typ in ('R_PPC_ADDR16_HA', 'R_PPC_ADDR16_LO', 'R_PPC_ADDR16_DS', 'R_PPC_ADDR16_DHA16'):
            t = ('A', sym)
        elif typ == 'R_PPC_REL24':
            t = ('B', mn)
        else:
            t = ('R', typ, sym)
    else:
        t = None
        if mn == 'bl': t = ('B', 'bl', ops)
        if mn in ('b', 'beq', 'bne', 'blt', 'bgt', 'ble', 'bge', 'bdnz', 'bdnz'): t = ('B', mn)
    ops2 = ops
    if t and t[0] == 'A':
        ops2 = re.sub(r'^\S.*', '', ops2)
    regs = re.findall(r'\b[rf]\d+\b|\bvs\d+\b|\bcr\d+\b|\bqr\d+\b', ops2)
    disp = re.search(r'(-?\d+)\(', ops2) or re.search(r'\((-?\d+)\)', ops2)
    mn_c = mn
    if mn in ('xxsel', 'xsmaddadp', 'xsmsubmsp'): mn_c = 'psq_st'
    if mn == 'addic.': mn_c = 'subic.' if '-1' in ops2 else mn
    return (mn_c, t, None, disp.group(1) if disp else None)

# For simplicity compare per-instruction a signature dict, era:
def sig_era(mn, ops, lab_addr):
    r = {}
    pool = re.search(r'(\S+?)@sda21', ops)
    arr = re.search(r'(\S+?)@(ha|l)', ops)
    r['mn'] = mn
    r['pool'] = era_val.get(pool.group(1)) if pool else ('POOLADDR' if pool else None)
    r['arr'] = arr.group(1) if arr else None
    r['regs'] = tuple('R' if x.startswith('r') else 'F' if x.startswith('f') else 'X' for x in re.findall(r'\b[rf]\d+\b', ops))
    dm = re.search(r'(-?0x[0-9a-f]+|[0-9]+)\((?:r\d+|0)\)?', ops)
    if dm:
        v = dm.group(1)
        r['disp'] = str(int(v, 16)) if (v.startswith('-0x') or v.startswith('0x') or re.fullmatch(r'[0-9a-f]{3,}', v)) else str(int(v))
    elif re.search(r'0x[0-9a-f]+$', ops):
        r['disp'] = str(int(re.search(r'0x([0-9a-f]+)$', ops).group(1), 16))
    else:
        r['disp'] = None
    if mn == 'bl':
        r['bl'] = re.sub(r'^(\S+).*', r'\1', ops)
    return r

def sig_ours(mn, ops, rel):
    r = {}
    r['mn'] = mn
    r['pool'] = None
    r['arr'] = None
    r['bl'] = None
    if rel:
        typ, sym = rel
        if typ == 'R_PPC_EMB_SDA21':
            key = sym if sym.startswith('@') else '@' + sym
            r['pool'] = POOLV.get(key, sym)
        elif typ.startswith('R_PPC_ADDR16') or typ.startswith('R_PPC_DARWIN') or 'ADDR' in typ:
            r['arr'] = sym.replace('@ha', '').replace('@l', '')
        elif typ == 'R_PPC_REL24':
            r['bl'] = sym
        else:
            r['other'] = (typ, sym)
    if mn == 'bl' and r['bl'] is None:
        r['bl'] = ops.split()[0] if ops else '?'
    r['regs'] = tuple('R' if x.startswith('r') else 'F' if x.startswith('f') else 'X' for x in re.findall(r'\b[rf]\d+\b', ops))
    dm = re.search(r'(-?\d+)\((?:r\d+|0)\)?', ops)
    r['disp'] = str(int(dm.group(1))) if dm else None
    return r

def mneq(a, b):
    if a == b: return True
    for k, vs in ALIAS.items():
        if a in vs and b in vs: return True
    return False

era_rows, lab_addr = load_era()
ours_rows, relocs = load_ours()
esig = []
for addr, w, mn, ops in era_rows:
    s = sig_era(mn, ops, lab_addr)
    esig.append(s)
osig = []
for addr, w, mn, ops in ours_rows:
    s = sig_ours(mn, ops, relocs.get(addr))
    osig.append(s)

def eq(a, b):
    if not mneq(a['mn'], b['mn']): return False
    if a['pool'] != b['pool']: return False
    if a['arr'] != b['arr']:
        # era arr names: lbl_8046509C etc; ours sym same names if declared extern with same name
        return False
    if a.get('bl') and b.get('bl'):
        an, bn = a['bl'].split()[0], b['bl']
        if an.rstrip('<>').split('<')[0] != bn: return False
    if a.get('other') or b.get('other'): return False
    if a['regs'] != b['regs']: return False
    if a['disp'] != b['disp']: return False
    return True

n, m_ = len(esig), len(osig)
dp = [[0]*(m_+1) for _ in range(n+1)]
for i in range(n-1, -1, -1):
    di, dn = dp[i], dp[i+1]
    for j in range(m_-1, -1, -1):
        di[j] = dn[j+1]+1 if eq(esig[i], osig[j]) else max(dn[j], di[j+1])
diffs = []
i = j = 0
while i < n and j < m_:
    if eq(esig[i], osig[j]): i += 1; j += 1
    elif dp[i+1][j] >= dp[i][j+1]: diffs.append(('DEL', i)); i += 1
    else: diffs.append(('INS', j)); j += 1
while i < n: diffs.append(('DEL', i)); i += 1
while j < m_: diffs.append(('INS', j)); j += 1
matched = n - sum(1 for d in diffs if d[0]=='DEL')
print(f"era {n}  ours {m_}  struct-matched {matched}/{n} = {100*matched/n:.2f}%")
regions = []
for op, idx in diffs:
    if regions and regions[-1][0] == op and regions[-1][1] + regions[-1][2] == idx:
        regions[-1][2] += 1
    else:
        regions.append([op, idx, 1])
def fmt(side, idx):
    if side == 'era':
        r = era_rows[idx]; return f"E {r[0]} {r[2]:10s} {r[3]}"
    r = ours_rows[idx]; rel = relocs.get(r[0], ('', ''))[1]
    return f"N {r[0]} {r[2]:10s} {r[3]}   <<{rel}>>  poolv={POOLV.get('@'+rel if not rel.startswith('@') else rel)}"
for op, idx, cnt in regions:
    side = 'era' if op == 'DEL' else 'ours'
    print(f"--- {op} x{cnt} @slot{idx}:")
    for k in range(idx, min(idx+cnt, len(era_rows if op=='DEL' else ours_rows))):
        print("   ", fmt(side, k))
