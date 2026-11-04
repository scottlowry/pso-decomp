import re
body = open('/Users/scott/.hermes/profiles/pso-decomp/cache/scratch/e2964_body.txt').read().splitlines()
pat = re.compile(r'^/\*\s*[0-9A-Fa-f]{8}\s+[0-9A-Fa-f]{8}\s+(?:[0-9A-Fa-f]{2}\s){3}[0-9A-Fa-f]{2}\s*\*/\s*(\S+)\s*(.*?)\s*$')
mref = re.compile(r'^(r\d+),\s*(-?0x[0-9A-Fa-f]+)\((r\d+)\)$')
mem, regs, seq = {}, {}, []
BASE16, TAB = 0x80495458, 0x8049575C
def loc(b, off):
    return ('G', BASE16 + off) if b == 'r16' else ('G', TAB + off) if b == 'r20' else ('S', off) if b == 'r1' else None
def unwrap(v):
    while isinstance(v, tuple) and v and v[0] == 'V':
        v = v[1]
    return v
nlines = 0
for ln in body:
    mm = pat.match(ln)
    if not mm:
        continue
    nlines += 1
    op, args = mm.group(1), mm.group(2)
    if op == 'mr':
        d, s = [x.strip() for x in args.split(',')]
        regs[d] = ('V', regs.get(s))
    elif op in ('lwz', 'stw'):
        p = mref.match(args)
        if not p:
            print('UNPARSED:', ln)
            continue
        d, off, b = p.group(1), int(p.group(2), 16), p.group(3)
        L = loc(b, off)
        if op == 'lwz':
            regs[d] = L if L[0] == 'G' else unwrap(mem.get(L))
        else:
            v = regs.get(d)
            mem[L] = v
            if b != 'r1':
                seq.append((unwrap(v), L))
print('parsed insns:', nlines, 'global stores:', len(seq))
badsrc = [(s, d) for s, d in seq if not (s and s[0] == 'G')]
print('unresolved srcs:', len(badsrc), badsrc[:4])
badshift = [(hex(s[1]), hex(d[1])) for s, d in seq if s and s[0] == 'G' and d[1] - s[1] != 0x198]
print('non +0x198:', len(badshift), badshift[:6])
srcs = sorted(s[1] for s, d in seq if s)
dsts = sorted(d[1] for s, d in seq)
print('src', hex(srcs[0]), '..', hex(srcs[-1]), 'uniq', len(set(srcs)), 'contig', srcs == list(range(srcs[0], srcs[-1] + 4, 4)))
print('dst', hex(dsts[0]), '..', hex(dsts[-1]), 'uniq', len(set(dsts)), 'contig', dsts == list(range(dsts[0], dsts[-1] + 4, 4)))
def runs(vals):
    out, run = [], [vals[0]]
    for v in vals[1:]:
        if v != run[-1] + 4:
            out.append((hex(run[0]), hex(run[-1]), len(run)))
            run = []
        run.append(v)
    out.append((hex(run[0]), hex(run[-1]), len(run)))
    return out
print('dst runs, program order:', runs(dsts))
print('src runs, program order:', runs(srcs))
# spill slots used
slots = sorted(set(k[1] for k in mem if k[0] == 'S'))
print('stack slots used:', len(slots), hex(slots[0]), hex(slots[-1]))
