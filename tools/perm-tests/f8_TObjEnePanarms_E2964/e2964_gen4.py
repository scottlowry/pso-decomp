import re
S = '/Users/scott/.hermes/profiles/pso-decomp/cache/scratch/'
body = open(S+'e2964_body.txt').read().splitlines()
pat = re.compile(r'^/\*\s*[0-9A-Fa-f]{8}\s+[0-9A-Fa-f]{8}\s+(?:[0-9A-Fa-f]{2}\s){3}[0-9A-Fa-f]{2}\s*\*/\s*(\S+)\s*(.*?)\s*$')
mref = re.compile(r'^(r\d+),\s*(-?0x[0-9A-Fa-f]+)\((r\d+)\)$')
regd = {}
stmts = []
for ln in body:
    mm = pat.match(ln)
    if not mm: continue
    op, args = mm.group(1), mm.group(2)
    if op == 'mr':
        d, s = [x.strip() for x in args.split(',')]
        regd[d] = regd.get(s)
        continue
    if op not in ('lwz', 'stw'): continue
    d, off, b = mref.match(args).groups()
    off = int(off, 16)
    if op == 'lwz':
        if b == 'r16':
            regd[d] = ('G', 0x80495458 + off)
        elif b == 'r1':
            regd[d] = ('S', off)
        else:
            raise SystemExit(ln)
    else:  # stw
        v = regd.get(d)
        assert v is not None, ln
        if b == 'r1':
            if v[0] == 'G':
                stmts.append(f'tmp[0x{off//4:X}] = s[0x{(v[1]-0x804955C4)//4:X}];')
            else:
                stmts.append(f'tmp[0x{off//4:X}] = tmp[0x{v[1]//4:X}];')
        else:
            j = (0x80495458 + off if b == 'r16' else 0x8049575C + off - 0x8049575C + 0x8049575C) - 0x8049575C
            j //= 4
            if v[0] == 'G':
                stmts.append(f'd[0x{j:X}] = s[0x{(v[1]-0x804955C4)//4:X}];')
            else:
                stmts.append(f'd[0x{j:X}] = tmp[0x{v[1]//4:X}];')
fn = ('void TObjEnePanarms__sub_800E2964(void) {\n'
      '    s32 tmp[40];\n'
      '    u8 *b = lbl_80495458;\n'
      '    s32 *s = (s32 *)(b + 0x16C);\n'
      '    s32 *d = (s32 *)(b + 0x304);\n'
      + '\n'.join('    ' + t for t in stmts) + '\n}\n')
orig = open('/Users/scott/Hermes/pso-decomp/pso-decomp-f8/src/pso/enemy/TObjEnePanarms.cpp').read()
anchor_decl = 'u8 TObjEnePanarms__sub_800E2E54(void *arg0);'
decls_extra = 'void TObjEnePanarms__sub_800E2964(void);\nextern u8 lbl_80495458[];'
anchor = 'void TObjMotion::clear_motion_flags(s32 arg1) {'
assert anchor_decl in orig and anchor in orig
out = orig.replace(anchor_decl, decls_extra + '\n' + anchor_decl)
out = out.replace(anchor, fn + '\n' + anchor)
open(S + 'cand_e2964_v4.cpp', 'w').write(out)
print('v4 statements:', len(stmts))
