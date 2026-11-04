#!/usr/bin/env python3
"""Rank df748 permuter harvests: size gate 0x3B8 + symbol-table check + probe_diff REAL rows."""
import os, re, subprocess, sys, glob

KIT = '/Users/scott/Hermes/pso-decomp/pso-decomp-f8/tools/perm-tests/f8_TObjEnePanarms_DF748'
REPO = '/Users/scott/Hermes/pso-decomp/pso-decomp-f8'
SYM = 'TObjEnePanarms__sub_800DF748'
ASM = 'build/GPOE8P/asm/pso/enemy/TObjEnePanarms_800DF6E0.s'
GNM = '/opt/homebrew/opt/binutils/bin/gnm'
PD = '/Users/scott/.hermes/profiles/pso-decomp/skills/pso-decomp/scripts/probe_diff.py'
env = dict(os.environ, PATH=f"/opt/homebrew/opt/binutils/bin:{REPO}/build/binutils:" + os.environ.get('PATH',''))

dirs = sorted([d for d in glob.glob(KIT + '/output-*') if os.path.isdir(d)],
              key=os.path.getmtime)
if len(sys.argv) > 1 and sys.argv[1] == 'all':
    pass
results = []
for d in dirs:
    sc = os.path.join(d, 'source.c')
    if not os.path.exists(sc):
        continue
    o = sc + '.ro.o'
    r = subprocess.run(['bash', f'{KIT}/compile.sh', sc, '-o', o], capture_output=True, text=True, env=env, cwd=REPO)
    if not os.path.exists(o):
        results.append((d, 'COMPILE-FAIL', None, None)); continue
    nm = subprocess.run([GNM, '-S', o], capture_output=True, text=True).stdout
    m = re.search(r'^[0-9a-f]+ (000003b8) T ' + SYM + '$', nm, re.M)
    size = re.search(r'^[0-9a-f]+ (\w+) T ' + SYM + '$', nm, re.M)
    # new-symbol reject: any defined T besides our fn?
    defs = [l.split()[-1] for l in nm.splitlines() if re.search(r' T \S+$', l) or re.search(r' [TWV] \S+$', l)]
    extra = [x for x in defs if x != SYM]
    if extra:
        results.append((d, 'NEWSYM:' + ','.join(extra), size.group(1) if size else '?', None)); continue
    if not m:
        results.append((d, 'SIZE-FAIL', size.group(1) if size else 'None', None)); continue
    p = subprocess.run(['python3', PD, o, SYM, ASM], capture_output=True, text=True, env=env, cwd=REPO)
    mm = re.search(r'verdict: (\d+) REAL', p.stdout)
    rows = int(mm.group(1)) if mm else -2
    results.append((d, 'OK', '000003b8', rows))

ok = sorted([r for r in results if r[3] is not None], key=lambda x: x[3])
fails = [r for r in results if r[3] is None]
print(f"harvests: {len(results)}  size-pass: {len(ok)}")
for d, st, sz, rows in ok[:8]:
    print(f"  {rows:4d} rows  {os.path.basename(d)}")
for d, st, sz, rows in fails[:10]:
    print(f"  X {os.path.basename(d)}: {st} size={sz}")
if ok:
    best = ok[0]
    print("BEST=", best[0], "rows=", best[3])
