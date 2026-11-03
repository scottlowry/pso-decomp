#!/usr/bin/env python3.14
"""Grid round-5: residual-cluster full permutation grid around the m4 winner.
Axes: body-token (4 spellings of the in-place basin) x cond-spelling (3) x
i-token (2) x pre-loop order (6) x decl-order (subset). Target: add r7,r0,r7
in the m4 basin (nbad=0). All offline compiles.
"""
import os, re, subprocess, json, itertools

KIT = os.path.dirname(os.path.abspath(__file__))
SYM = "TLobby__sub_80428DC8"
orig = open(f"{KIT}/gen_v44_subfirst.c").read()
ORIG_DECL = "  s16 c;\n  s16 n;\n  char *dest;\n  s16 i;\n  u8 ch;\n"
ORIG_PRE = "n = *num_cnt;\n    i = 0;\n    entry = 0;"
ORIG_LOOP = "while ((ch = text[i]) != 0)\n    {\n      %s\n      i++;\n    }"
ORIG_E = "entry = entry * 10 - '0' + ch;"

BODIES = {
 "b1": "entry = entry * 10;\n      entry += ch;\n      entry -= '0';",
 "b2": "entry *= 10;\n      entry += ch;\n      entry -= '0';",
 "b3": "entry = entry * 10;\n      entry += ch;\n      entry = entry - '0';",
 "b4": "entry *= 10;\n      entry += ch;\n      entry = entry - '0';",
}
CONDS = {
 "c0": "while ((ch = text[i]) != 0)",
 "c1": "while (0 != (ch = text[i]))",
 "c2": "while ((ch = text[i]))",
}
ITOK = {"i0": "i++;\n", "i1": "++i;\n"}
PRES = {
 "nie": "n = *num_cnt;\n    i = 0;\n    entry = 0;",
 "ine": "i = 0;\n    n = *num_cnt;\n    entry = 0;",
 "nie2": "n = *num_cnt;\n    entry = 0;\n    i = 0;",
 "eni": "entry = 0;\n    n = *num_cnt;\n    i = 0;",
 "ien": "i = 0;\n    entry = 0;\n    n = *num_cnt;",
 "ein": "entry = 0;\n    i = 0;\n    n = *num_cnt;",
}
DECLS = {
 "d0": ORIG_DECL,
 "d1": "  s16 c;\n  s16 n;\n  char *dest;\n  u8 ch;\n  s16 i;\n",
 "d3": "  s16 c;\n  s16 n;\n  u8 ch;\n  char *dest;\n  s16 i;\n",
 "d4": "  s16 n;\n  s16 c;\n  char *dest;\n  s16 i;\n  u8 ch;\n",
}

def words(obj):
    txt = subprocess.run(["/opt/homebrew/bin/powerpc-eabi-objdump", "-d", obj],
                         capture_output=True, text=True).stdout
    lines = txt.splitlines()
    i = next(k for k, l in enumerate(lines) if f"<{SYM}>:" in l)
    out = []
    for l in lines[i + 1:]:
        m = re.match(r"^\s+[0-9a-f]+:\s+((?:[0-9a-f]{2} )+)\s*", l)
        if not m:
            if out and not l.strip().startswith("R_PPC"):
                break
            continue
        out.append(m.group(1).replace(" ", "").rstrip())
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
combos = list(itertools.product(BODIES, CONDS, ITOK, PRES, ["d0"])) + \
         list(itertools.product(["b1", "b2"], ["c0"], ["i0", "i1"], ["nie"], ["d1", "d3", "d4"]))
for (bk, ck, ik, pk, dk) in combos:
    name = f"p_{bk}_{ck}_{ik}_{pk}_{dk}"
    loop = CONDS[ck] + "\n    {\n      " + BODIES[bk] + "\n      " + ITOK[ik].strip() + "\n    }"
    # ORIG_LOOP full-shape replace: reconstruct original loop-block with current tokens
    src = orig.replace(ORIG_DECL, DECLS[dk]).replace(ORIG_PRE, PRES[pk])
    # replace the whole while-block (greedy to the closing of loop)
    m = re.search(r"while \(\(ch = text\[i\]\) != 0\)\s*\n\s*\{\s*\n.*?\n\s*\}", src, re.S)
    if not m:
        print("LOOP-MATCH-FAIL"); break
    src = src[:m.start()] + loop + src[m.end():]
    c = f"{KIT}/gs5_{name}.c"; o = f"{KIT}/gs5_{name}.o"
    open(c, "w").write(src)
    r = subprocess.run(["bash", f"{KIT}/compile.sh", c, "-o", o], capture_output=True, text=True, cwd=KIT)
    if r.returncode != 0:
        continue
    sz = size_of(o)
    try:
        w = words(o)
    except StopIteration:
        continue
    if sz != 248 or len(w) != 62:
        results.append((name, f"SZ{sz}/{len(w)}", None)); continue
    bad = [k for k in range(62) if w[k] != tw[k]]
    results.append((name, "OK", bad))
    if bad == []:
        print(f"EXACT-MATCH {name} !!!")

os.makedirs(f"{KIT}/gs5_keep", exist_ok=True)
for name, st, bad in results:
    if isinstance(bad, list) and len(bad) <= 2:
        for ext in ("c", "o"):
            try: os.link(f"{KIT}/gs5_{name}.{ext}", f"{KIT}/gs5_keep/{name}.{ext}")
            except OSError: pass
results.sort(key=lambda r: (len(r[2]) if isinstance(r[2], list) else 99))
print(f"compiled+gated: {len(results)}")
for name, st, bad in results[:15]:
    print(f"{name:26} {st:10} bad={bad}")
json.dump([[n, s, b] for n, s, b in results], open(f"{KIT}/grid_round5.json", "w"), indent=1)
