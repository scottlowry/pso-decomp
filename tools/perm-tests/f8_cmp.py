#!/usr/bin/env python3
"""Compare era .fn block (at-style asm) vs objdump -dr of our .o symbol. Canonical token compare."""
import re, sys, difflib

def era_tokens(path):
    toks = []; addrs = []
    labels = {}
    for ln in open(path):
        ln = ln.rstrip()
        if ln.startswith('.fn') or ln.startswith('.endfn'): continue
        m = re.match(r'/\* ([0-9A-F]+) [0-9A-F]+  [0-9A-F ]+\*/\t(.*)', ln)
        if m:
            addrs.append(int(m.group(1), 16)); toks.append(m.group(2))
        elif ln.startswith('.L'):
            labels[ln[:-1].strip()] = len(toks)
    out = []
    for a, t in zip(addrs, toks):
        out.append((a, canon(t, labels, addrs)))
    return out

def ours_tokens(path):
    raw = []; off = None; label_at = {}
    lines = open(path).read().splitlines()
    i = 0
    base = None
    while i < len(lines):
        ln = lines[i]
        m = re.match(r'^\s*([0-9a-f]+):\t(.*)$', ln)
        if m:
            o = int(m.group(1), 16)
            segs = m.group(2).split('\t')
            txt = '\t'.join(segs[1:]) if len(segs) > 1 else segs[0]
            rel = None
            if i + 1 < len(lines):
                r = re.match(r'^\s*(?:[0-9a-f]+:\s*)?R_PPC_\S+\s+(\S+)', lines[i + 1])
                if r:
                    rel = r.group(1); i += 1
            raw.append((o, txt, rel))
        else:
            m2 = re.match(r'^([0-9a-f]+) <[^>]*>:\s*$', ln)
            if m2: label_at[int(m2.group(1), 16)] = True
            m3 = re.match(r'^\s*([0-9a-f]+):\s*$', ln)
            if m3: label_at[int(m3.group(1), 16)] = True
        i += 1
    base = raw[0][0]
    idx_at = {o - base: k for k, (o, t, r) in enumerate(raw)}
    labels = {}
    for lbl in label_at:
        k = lbl - base
        if k in idx_at: labels[k] = idx_at[k]
    out = []
    for (o, txt, rel) in raw:
        t = txt
        if rel:
            op0 = txt.split()[0]
            if op0 in BRANCHES:
                t = op0 + ' ' + rel
            else:
                t = re.sub(r'\b0\(0\)', rel + '@sda21(r0)', txt)
        out.append((o - base, canon(t, labels, None, idx_at)))
    return out

BRANCHES = {'b', 'bl', 'beq', 'bne', 'ble', 'blt', 'bge', 'bgt', 'bnl', 'bc', 'bnd'}

def canon(t, labels, addrs, idx_at=None):
    t = t.strip()
    parts = t.split(None, 1)
    op = parts[0]
    rest = parts[1].strip() if len(parts) > 1 else ''
    # branch/label targets
    if op in BRANCHES:
        m = re.match(r'(\.L_[0-9A-F]+)', rest)
        if m and m.group(1) in labels:
            rest = 'TGT%d' % labels[m.group(1)]
        elif m:
            rest = 'TGT-' + m.group(1)
        else:
            m2 = re.match(r'([0-9a-f]+) <.*\+0x([0-9a-f]+)>', rest)
            if m2 and idx_at is not None:
                rest = 'TGT%d' % idx_at.get(int(m2.group(2), 16), -1)
            elif re.match(r'^0x[0-9a-f]+$', rest):
                rest = 'TGT?'
    # sda21 name from reloc
    m3 = re.match(r'(\S+) @(\S+)', rest)
    if m3 and m3.group(2).startswith('lbl_') and 'lfs' in op:
        rest = m3.group(2) + '@sda21'
    # normalize ints (hex and decimal both)
    def toint(x):
        try: return str(int(x, 0))
        except Exception: return x
    toks = re.split(r'[,\s]+', rest)
    toks = ['0' if t == 'qr0' else t for t in toks]
    def tonum(x):
        # handle "52(r1)" / "-48(r1)" displacement forms too
        m = re.match(r'^(-?(?:0[xX])?[0-9a-fA-F]+)\((r\d+|sp)\)$', x)
        if m:
            v = int(m.group(1), 0)
            return hex(v) + '(' + m.group(2) + ')'
        return toint(x)
    toks = [tonum(x) for x in toks]
    toks = [t.lower() if t.startswith('0x') else t for t in toks]
    return op + ' ' + ' '.join(toks)

era = era_tokens(sys.argv[1])
ours = ours_tokens(sys.argv[2])
ea = [t for _, t in era]; ob = [t for _, t in ours]
print(f"era insns: {len(ea)}  ours insns: {len(ob)}")
sm = difflib.SequenceMatcher(a=ea, b=ob, autojunk=False)
n = 0
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag != 'equal':
        print(f"--- {tag} era[{i1}:{i2}] ours[{j1}:{j2}]")
        for k in range(i1, i2): print(f"  E{k:3d}:", era[k][1])
        for k in range(j1, j2): print(f"  O{k:3d}:", ours[k][1])
        n += 1
# equal-region register-color check is automatic (tokens include regs)
print("diff hunks:", n)
