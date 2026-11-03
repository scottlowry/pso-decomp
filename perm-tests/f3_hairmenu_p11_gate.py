#!/usr/bin/env python3
"""f3 p11 gate: run on ANY obj (OBJ env or argv[1]) — superset of p10 checks:
words=460 + span 0x730 + stmw r23 + lha r27 + pokes faithful + era trio present.
Exit 0 iff all pass. Prints md5 for dedupe."""
import re, subprocess, sys, hashlib, os
OBJ = sys.argv[1] if len(sys.argv) > 1 else os.environ.get(
    "OBJ", "/Users/scott/Hermes/pso-decomp/pso-decomp-f3/build/GPOE8P/src/pso/object/TObjCMName.o")
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
if not fn:
    print("FAIL no-fn"); print("md5:", md5); sys.exit(2)
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
fails = [n for n, ok in checks if not ok]
print("md5:", md5, "| words:", len(fn), "| checks:", "ALL-PASS" if not fails else "FAIL:" + ",".join(fails))
sys.exit(0 if not fails else 1)
