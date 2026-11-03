#!/usr/bin/env python3
"""f3 p10 gate: run on current build obj. Checks span/460w, stmw r23, era trio+pokes
faithful; reports GPR bank colors (tail counter) + FPR dest histogram. Exit 0 iff gate."""
import re, subprocess, sys, hashlib
REPO = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3"
OBJ = REPO + "/build/GPOE8P/src/pso/object/TObjCMName.o"
md5 = hashlib.md5(open(OBJ, "rb").read()).hexdigest()
out = subprocess.run(["/opt/homebrew/opt/binutils/bin/objdump", "-dr", OBJ],
                     capture_output=True, text=True).stdout
fn = []; on = False
for line in out.splitlines():
    hm = re.match(r'^[0-9a-f]+ <(.*)>:', line)
    if hm: on = 'render__14TObjCMHairMenuFv' in hm.group(1); continue
    if on:
        mm = re.match(r'\s+([0-9a-f]+):\t([0-9a-f ]+?)\t(\S+)\s*(.*)', line)
        if mm: fn.append((int(mm.group(1), 16), mm.group(3), mm.group(4).strip()))
sz = fn[-1][0] + 4 - fn[0][0]
body = "\n".join(f"{m} {o}" for _, m, o in fn)
def has(rx): return bool(re.search(rx, body, re.M))
checks = [
    ("words=460", len(fn) == 460),
    ("span 0x730", sz == 0x730),
    ("stmw r23", has(r'stmw\s+r23,140\(r1\)')),
    ("lha hair r27", has(r'lha\s+r27,64\(r3\)')),
    ("poke stb r0,11", has(r'stb\s+r0,11\(r1\)')),
    ("poke stb r0,15", has(r'stb\s+r0,15\(r1\)')),
    ("no stw-20 corrupt", not has(r'stw\s+r\d+,20\(r1\)')),
    ("era trio addi r4,r1,8", has(r'addi\s+r4,r1,8')),
    ("era trio stw r5,8", has(r'stw\s+r5,8\(r1\)')),
    ("lbz readback 15", has(r'lbz\s+r0,15\(r1\)')),
]
for name, ok in checks:
    print(f"{'PASS' if ok else 'FAIL'} {name}")
print("md5:", md5)
tail = [f"{a:x}:{m} {o}" for a, m, o in fn if a >= 0x17e0 and m in ("addi", "cmpwi")]
print("tail-counter sites:", "; ".join(tail))
c421 = [f"{a:x}:{m} {o}" for a, m, o in fn if 0x17b0 <= a < 0x17e0 and m == "mr"]
print("staging mr sites:", "; ".join(c421))
fpr = {}
for a, m, o in fn:
    if m in ("fmadds", "fdivs", "fmr", "fadds", "fsubs", "fctiwz"):
        d = re.match(r'f\d+', o)
        if d: fpr[d.group(0)] = fpr.get(d.group(0), 0) + 1
print("FPR dest hist:", dict(sorted(fpr.items(), key=lambda x: -x[1])))
allok = all(ok for _, ok in checks)
print("VERDICT:", "GATE-PASS" if allok else "GATE-FAIL")
sys.exit(0 if allok else 1)
