#!/usr/bin/env python3
# text_802E34AC storm provenance + DOL literals + fnptr naming -> storm_map.json
import struct, re, json

ROOT = '/Users/scott/Hermes/pso-decomp/pso-decomp-f7'
ASM = ROOT + '/build/GPOE8P/asm/pso/unk/text_802E34AC.s'
DOL = ROOT + '/orig/GPOE8P/files/PsoV3.dol'
SYMS = ROOT + '/config/GPOE8P/psov3/symbols.txt'

d = open(DOL, 'rb').read()
toff = list(struct.unpack('>18I', d[0x00:0x48]))
addr = list(struct.unpack('>18I', d[0x48:0x90]))
size = list(struct.unpack('>18I', d[0x90:0xD8]))
segs = [(addr[i], toff[i], size[i]) for i in range(18) if toff[i] and size[i]]
def read_va(va, n):
    for a, fo, s in segs:
        if a <= va and va + n <= a + s:
            return d[fo + (va - a): fo + (va - a) + n]
    raise ValueError(hex(va))

sym_rows = []
for ln in open(SYMS):
    m = re.match(r'(\S+) = (\S+):0x([0-9A-Fa-f]+); // type:(\w+) size:0x([0-9A-Fa-f]+)', ln)
    if m:
        sym_rows.append((int(m.group(3), 16), m.group(1), m.group(2), int(m.group(5), 16)))
by_addr = {a: (n, s, z) for a, n, s, z in sym_rows}

def name_word(w):
    if w in by_addr:
        n, s, z = by_addr[w]; return f'{n}[{s}:0x{z:X}]'
    if 0x8000F740 <= w < 0x80433F20:
        for a, n, s, z in sym_rows:
            if s == '.text' and a <= w < a + max(z, 4):
                return f'{n}+0x{w-a:X}'
        return f'TEXT@0x{w:08X}'
    return f'0x{w:08X}'

FRAG = 0x804E3040
lns = []
for l in open(ASM):
    m = re.match(r'/\* ([0-9A-F]{8}) \S+\s+((?:[0-9A-F]{2} ){3}[0-9A-F]{2})\s*\*/\s*(.+)', l)
    if m: lns.append((int(m.group(1), 16), m.group(3).strip()))

# base tracking: b3=('frag'), b5: rodata-head then ptmf, cursors via ('ptr',off)
val, frame = {}, {}
copy, nulls, fptrace, misc = [], [], [], []
R5_MODE = {'m': 'rodata'}  # r5 switches to __ptmf_null at 0x802E385C

def fragoff(x): return x  # symbolic absolute frag-relative disp

def resolve_base(tok):
    # tok like '0x18(r3)' ; return (disp, basetag) basetag in frag/r19/f5/r1/ptr/<name>
    m = re.match(r'(0x[0-9A-Fa-f]+|lbl_[0-9A-Fa-f]+(?:@\w+)?|__ptmf_null(?:@\w+)?|multi\S*)\((r\d+|f\d+)\)$', tok)
    if not m: return None
    disp_s, b = m.groups()
    try: disp = int(disp_s, 16)
    except ValueError: disp = disp_s
    return disp, b

for pc, t in lns:
    if pc >= 0x802E385C: R5_MODE['m'] = 'ptmf'
    op = t.split(None, 1)
    o = op[0]; args = [a.strip() for a in op[1].split(',')] if len(op) > 1 else []
    if o == 'lwz':
        r = args[0]; rd = resolve_base(args[1])
        disp, b = rd
        if b == 'r3': val[r] = ('frag', disp if isinstance(disp, int) else disp)
        elif b == 'r5': val[r] = ('RO' if R5_MODE['m'] == 'rodata' else 'PTMF', disp if isinstance(disp, int) else 0, pc)
        elif b == 'r1': val[r] = frame.get(disp, ('?', disp))
        elif b in val and val[b][0] == 'ptr': val[r] = ('frag', val[b][1] + disp)
        else: val[r] = ('?', (disp, b))
    elif o == 'stw':
        r = args[0]; disp, b = resolve_base(args[1])
        v = val.get(r)
        if b == 'r1': frame[disp] = v
        elif b == 'r19':
            tgt = 0x264 + disp
            if v and v[0] == 'frag': copy.append((v[1], tgt, pc))
            elif v and v[0] == 'PTMF': nulls.append((tgt, v[1], pc))
            else: misc.append(('stw?', pc, r, v, ('r19', disp)))
        elif b == 'r3':
            if v and v[0] == 'frag': copy.append((v[1], disp, pc))
            elif v and v[0] == 'PTMF': nulls.append((disp, v[1], pc))
            else: misc.append(('stw?', pc, r, v, ('r3', disp)))
        else: misc.append(('stwB', pc, r, v, (b, disp)))
    elif o == 'lfs':
        r = args[0]; disp, b = resolve_base(args[1])
        if b == 'r0': fptrace.append(('lfs-lit', r, str(disp), pc))
        elif b == 'r5': fptrace.append(('lfs-RO', r, disp, pc))
        elif b == 'r3': fptrace.append(('lfs-frag', r, disp, pc))
        elif b in val and val[b][0] == 'ptr': fptrace.append(('lfs-frag', r, val[b][1] + disp, pc))
        else: fptrace.append(('lfs?', r, (disp, b), pc))
    elif o == 'stfs':
        r = args[0]; disp, b = resolve_base(args[1])
        if b == 'r0': fptrace.append(('stfs-lit', r, str(disp), pc))
        elif b == 'r3': fptrace.append(('stfs-frag', r, disp, pc))
        elif b in val and val[b][0] == 'ptr': fptrace.append(('stfs-frag', r, val[b][1] + disp, pc))
        elif b == 'r5': fptrace.append(('stfs-RO', r, disp, pc))
        else: fptrace.append(('stfs?', r, (disp, b), pc))
    elif o == 'addi':
        if args[0] == 'r19' and args[1] == 'r3': val['r19'] = ('ptr', int(args[2], 16))
        elif args[1] == 'r3':
            val[args[0]] = ('ptr', int(args[2], 16) if args[2].startswith('0x') else 0)
        elif args[1] == 'r4' and '__ptmf_null' in args[2]: val['r5'] = ('PTMFbase',)
        elif args[1] == 'r3' or (len(args) > 1 and val.get(args[1], ('',))[0] == 'ptr'):
            v = val.get(args[1])
            if v and v[0] == 'ptr': val[args[0]] = ('ptr', v[1] + (int(args[2], 16) if args[2].startswith('0x') else 0))
    elif o == 'mr':
        val[args[0]] = val.get(args[1])
    elif o == 'fmuls':
        fptrace.append(('fmuls', args[0], args[1:], pc))
    elif o == 'fadds':
        fptrace.append(('fadds', args[0], args[1:], pc))
    elif o == 'fsubs':
        fptrace.append(('fsubs', args[0], args[1:], pc))
    elif o == 'fmadds':
        fptrace.append(('fmadds', args[0], args[1:], pc))

copy.sort(key=lambda x: x[1])
srcs = sorted(set(c[0] for c in copy))
print('copies:', len(copy), 'distinct src:', len(srcs))
holes = [(s, e) for s, e in zip(srcs, srcs[1:]) if e != s + 4]
print('src holes:', [(hex(a), hex(b)) for a, b in holes])
maxsrc = 0x264
print('src range:', hex(min(srcs)), hex(max(srcs)))
print('dst holes:', [(hex(a), hex(b)) for a, b in zip([c[1] for c in copy], [c[1] for c in copy][1:]) if b != a + 4])
print('null triples:', [(hex(t), i) for t, i, p in sorted(nulls)])
print('misc:', misc[:12])
print('--- fp trace ---')
for f in fptrace: print(f[0], f[1], f[2], hex(f[3]))

# DOL dumps
print('=== pool words 0x18..0x264 (frag-rel) ===')
pool = struct.unpack('>147I', read_va(FRAG + 0x18, 588))
for i, w in enumerate(pool):
    off = 0x18 + 4 * i
    print(f'+0x{off:03X} 0x{w:08X} {name_word(w) if w > 0x1000 else w}')
print('=== frag head initial 0x00..0x18 ===')
for i, w in enumerate(struct.unpack('>6I', read_va(FRAG, 0x18))):
    print(f'+0x{i*4:02X} 0x{w:08X}')
print('=== instance region 0x264..0x4BC initial (expect zeros) ===')
inst = struct.unpack('>150I', read_va(FRAG + 0x264, 600))
nz = [(i*4 + 0x264, w) for i, w in enumerate(inst) if w]
print('nonzero:', [(hex(a), hex(w), name_word(w)) for a, w in nz])
print('=== sdata2 literals ===')
for A in (0x805DE8E8, 0x805DE8FC, 0x805DE900, 0x805DE904, 0x805DE908, 0x805DE90C):
    w = struct.unpack('>I', read_va(A, 4))[0]
    print(f'lbl_{A:08X} 0x{w:08X} = {struct.unpack(">f", struct.pack(">I", w))[0]!r}')
print('=== rodata around lbl_80472930 (0x28 bytes) ===')
for i, w in enumerate(struct.unpack('>10I', read_va(0x80472930, 0x28))):
    print(f'+0x{i*4:02X} 0x{w:08X} f={struct.unpack(">f", struct.pack(">I", w))[0]!r} {name_word(w)}')
print('=== rows in 0x80472920..0x80472970 ===')
for a, n, s, z in sym_rows:
    if 0x80472920 <= a <= 0x80472970: print(f'{n} = {s}:0x{a:08X} size:0x{z:X}')

json.dump({'copy': copy, 'nulls': nulls, 'pool': list(pool)}, open(ROOT + '/tools/perm-tests/text_802E34AC_sinit/storm_map.json', 'w'))
