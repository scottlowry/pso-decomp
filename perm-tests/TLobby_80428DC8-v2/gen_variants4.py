#!/usr/bin/env python3.14
"""Grid round-2: hunt the ch-in-r0 flip inside the fold basin.
Axes: fold expression topology × pre-loop statement order × decl order.
All compiled offline via kit compile.sh; gate size 248; fingerprint loop rows.
Zero repo builds.
"""
import os, re, subprocess, itertools, json, sys

KIT = os.path.dirname(os.path.abspath(__file__))
SYM = "TLobby__sub_80428DC8"
BASE_SRC = f"{KIT}/gen_v44_subfirst.c"

EXPRS = {
 "e1":  "entry = entry * 10 - '0' + ch;",
 "e2":  "entry = entry * 10 + ch - '0';",
 "e3":  "entry = (entry * 10 - '0') + ch;",
 "e4":  "entry = ch + (entry * 10 - '0');",
 "e5":  "entry = (ch - '0') + entry * 10;",
 "e6":  "entry = entry * 10 - (0x30 - ch);",
 "m1":  "entry *= 10;\n      entry = entry + ch - '0';",
 "m2":  "entry *= 10;\n      entry = ch + entry - '0';",
 "m3":  "entry *= 10;\n      entry += ch;\n      entry -= '0';",
 "m4":  "entry = entry * 10;\n      entry += ch;\n      entry -= '0';",
 "m5":  "entry = entry * 10;\n      entry = entry + ch - '0';",
 "m6":  "entry = entry * 10;\n      entry = ch + (entry - '0');",
 "m7":  "entry = entry * 10;\n      entry = entry - '0' + ch;",
 "m8":  "entry *= 10;\n      entry = entry - '0' + ch;",
}
PRES = {
 "nie": "n = *num_cnt;\n    i = 0;\n    entry = 0;",
 "ine": "i = 0;\n    n = *num_cnt;\n    entry = 0;",
 "nie2":"n = *num_cnt;\n    entry = 0;\n    i = 0;",
 "eni": "entry = 0;\n    n = *num_cnt;\n    i = 0;",
 "ien": "i = 0;\n    entry = 0;\n    n = *num_cnt;",
 "ein": "entry = 0;\n    i = 0;\n    n = *num_cnt;",
}
DECLS = {
 "d0":  "  s16 c;\n  s16 n;\n  char *dest;\n  s16 i;\n  u8 ch;\n",
 "d1":  "  s16 c;\n  s16 n;\n  char *dest;\n  u8 ch;\n  s16 i;\n",
 "d2":  "  s16 c;\n  s16 n;\n  s16 i;\n  char *dest;\n  u8 ch;\n",
 "d3":  "  s16 c;\n  s16 n;\n  u8 ch;\n  char *dest;\n  s16 i;\n",
 "d4":  "  s16 n;\n  s16 c;\n  char *dest;\n  s16 i;\n  u8 ch;\n",
 "d5":  "  char *dest;\n  s16 c;\n  s16 n;\n  s16 i;\n  u8 ch;\n",
}

orig = open(BASE_SRC).read()
ORIG_DECL = "  s16 c;\n  s16 n;\n  char *dest;\n  s16 i;\n  u8 ch;\n"
ORIG_PRE = "n = *num_cnt;\n    i = 0;\n    entry = 0;"
ORIG_E = "entry = entry * 10 - '0' + ch;"
assert ORIG_DECL in orig and ORIG_PRE in orig and ORIG_E in orig

def words(obj):
    txt = subprocess.run(["/opt/homebrew/bin/powerpc-eabi-objdump", "-d", obj],
                         capture_output=True, text=True).stdout
    lines = txt.splitlines()
    i = next(k for k, l in enumerate(lines) if f"<{SYM}>:" in l)
    out = []
    for l in lines[i + 1:]:
        m = re.match(r"^\s+[0-9a-f]+:\s+((?:[0-9a-f]{2} )+)\s*(.*)", l)
        if not m:
            if out and not l.strip().startswith("R_PPC"):
                break
            continue
        out.append((m.group(1).replace(" ", "").rstrip(), m.group(2).split("#")[0].strip()))
    return out

tw = words(f"{KIT}/target.o")

def size_of(obj):
    out = subprocess.run(["/opt/homebrew/opt/binutils/bin/gnm", "-S", obj],
                         capture_output=True, text=True).stdout
    for line in out.splitlines():
        p = line.split()
        if len(p) == 4 and p[-1] == SYM:
            return int(p[1], 16)
    return None

results = []
grid = list(itertools.product(EXPRS, PRES, (["d0"] if any(k not in ("m1","m2","m3","m4","m5","m6","m7","m8") for k in EXPRS) else ["d0"] for _ in [0])))
# phase 1: exprs × pres, base decl
combos = [(e, p, "d0") for e in EXPRS for p in PRES]
# phase 2: best-known fold exprs × decl variants
combos += [(e, p, d) for e in ("e1","e2","m1","m4","m5") for p in ("nie",) for d in DECLS if d != "d0"]

for (ek, pk, dk) in combos:
    name = f"g_{ek}_{pk}_{dk}"
    src = orig.replace(ORIG_DECL, DECLS[dk]).replace(ORIG_PRE, PRES[pk]).replace(ORIG_E, EXPRS[ek])
    c = f"{KIT}/gridsrc_{name}.c"; o = f"{KIT}/grid_{name}.o"
    open(c, "w").write(src)
    r = subprocess.run(["bash", f"{KIT}/compile.sh", c, "-o", o], capture_output=True, text=True, cwd=KIT)
    if r.returncode != 0:
        results.append((name, "FAIL", None, None)); continue
    sz = size_of(o)
    w = words(o)
    if sz != 248 or len(w) != 62:
        results.append((name, f"SZ{sz}/{len(w)}", None, None)); continue
    bad = [k for k in range(62) if w[k][0] != tw[k][0]]
    ch_home = w[44][1].split(",")[0].strip() if len(w) > 44 else "?"
    results.append((name, "OK", bad, ch_home))

for name, st, bad, chh in results:
    line = f"{name:18} {st:8} ch={chh}"
    if bad is not None:
        line += f" nbad={len(bad)} {bad}"
    print(line)

wins = [r for r in results if r[2] == []]
print(f"\nEXACT-MATCH variants: {len(wins)}")
near = sorted([r for r in results if isinstance(r[2], list) and r[2] is not None], key=lambda r: len(r[2]))[:8]
print("closest:", [(r[0], r[2]) for r in near])
json.dump([[r[0], r[1], r[2], r[3]] for r in results], open(f"{KIT}/grid_round2.json", "w"), indent=1)
