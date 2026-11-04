import re
S = '/Users/scott/.hermes/profiles/pso-decomp/cache/scratch/'
body = open(S+'e2964_body.txt').read().splitlines()
pat = re.compile(r'^/\*\s*[0-9A-Fa-f]{8}\s+[0-9A-Fa-f]{8}\s+(?:[0-9A-Fa-f]{2}\s){3}[0-9A-Fa-f]{2}\s*\*/\s*(\S+)\s*(.*?)\s*$')
mref = re.compile(r'^(r\d+),\s*(-?0x[0-9A-Fa-f]+)\((r\d+)\)$')
regval = {}   # reg -> ('G',abs) or ('T', tempname) for loaded global value
temps = {}    # reg -> temp id at last load
spill = {}    # slot -> temp id (value spilled)
nextid = [0]
stmts = []
GLOAD, GSTORE = 0, 0
for ln in body:
    mm = pat.match(ln)
    if not mm: continue
    op, args = mm.group(1), mm.group(2)
    if op == 'mr':
        d, s = [x.strip() for x in args.split(',')]
        temps[d] = temps.get(s)
    elif op == 'lwz':
        d, off, b = mref.match(args).groups()
        off = int(off, 16)
        if b == 'r16':
            nid = nextid[0]; nextid[0] += 1
            t = f't{nid}'
            src_idx = (0x80495458 + off - 0x804955C4) // 4
            stmts.append((f'{t} = s[0x{src_idx:X}];', 'load'))
            temps[d] = t
            GLOAD += 1
        elif b == 'r1':
            temps[d] = spill[off]
        else:
            raise SystemExit('unexpected load base ' + ln)
    elif op == 'stw':
        d, off, b = mref.match(args).groups()
        off = int(off, 16)
        t = temps[d]
        if b == 'r1':
            spill[off] = t
        elif b in ('r16', 'r20'):
            absaddr = 0x80495458 + off if b == 'r16' else 0x8049575C + off
            dst_idx = (absaddr - 0x8049575C) // 4
            stmts.append((f'd[0x{dst_idx:X}] = {t};', 'store'))
            GSTORE += 1
print('global loads:', GLOAD, 'global stores:', GSTORE, 'temps:', nextid[0])
head = '''
void TObjEnePanarms__sub_800E2964(void) {
    u8 *b = lbl_80495458;
    s32 *s = (s32 *)(b + 0x16C);
    s32 *d = (s32 *)(b + 0x304);
'''
decls = ''.join(f'    s32 t{i};\n' for i in range(nextid[0]))
mid = '\n'.join('    ' + s for s, _ in stmts)
fn = head + '}'  # placeholder
# insert decls before body (MWCC decl order shouldn't matter, list in load order)
fnv3b = ('\nvoid TObjEnePanarms__sub_800E2964(void) {\n' + decls +
         '    u8 *b = lbl_80495458;\n    s32 *s = (s32 *)(b + 0x16C);\n    s32 *d = (s32 *)(b + 0x304);\n' +
         mid + '\n}\n')

# v3a: grouped batch loads then batch stores per 5 regions
groups = [list(range(24, 45)), list(range(0, 24)), list(range(69, 89)), list(range(45, 69)), list(range(89, 102))]
lines = ['void TObjEnePanarms__sub_800E2964(void) {',
         '    u8 *b = lbl_80495458;',
         '    s32 *s = (s32 *)(b + 0x16C);',
         '    s32 *d = (s32 *)(b + 0x304);',
         '    s32 v[45];']
for g in groups:
    for i in g: lines.append(f'    v[{i-max(g)}] = s[0x{i:X}];')
    for i in g: lines.append(f'    d[0x{i:X}] = v[{i-max(g)}];')
lines.append('}')
fnv3a = '\n'.join(lines) + '\n'

orig = open('/Users/scott/Hermes/pso-decomp/pso-decomp-f8/src/pso/enemy/TObjEnePanarms.cpp').read()
anchor_decl = 'u8 TObjEnePanarms__sub_800E2E54(void *arg0);'
assert anchor_decl in orig
decls_extra = 'void TObjEnePanarms__sub_800E2964(void);\nextern u8 lbl_80495458[];'
anchor = 'void TObjMotion::clear_motion_flags(s32 arg1) {'
for name, body_fn in (('v3a', fnv3a), ('v3b', fnv3b)):
    out = orig.replace(anchor_decl, decls_extra + '\n' + anchor_decl)
    out = out.replace(anchor, body_fn + '\n' + anchor)
    open(S + f'cand_e2964_{name}.cpp', 'w').write(out)
print('wrote v3a, v3b')
