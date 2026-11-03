#!/usr/bin/env python3.14
"""Rank permuter outputs for TLobby__sub_80428DC8: size-gate 248 first, then
raw objdiff one-symbol score against target.o. Zero repo builds."""
import subprocess, json, sys, os, glob, tempfile

REPO = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3"
D = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3/perm-tests/TLobby_80428DC8-v2"
TARGET = f"{D}/target.o"
SYM = "TLobby__sub_80428DC8"
EXPECT = 248

def fn_size(obj):
    out = subprocess.run(["/opt/homebrew/opt/binutils/bin/gnm", "-S", obj],
                         capture_output=True, text=True).stdout
    for line in out.splitlines():
        parts = line.split()
        if len(parts) == 4 and parts[-1] == SYM:
            return int(parts[1], 16)
    return None

def new_symbols(obj):
    out = subprocess.run(["/opt/homebrew/opt/binutils/bin/gnm", obj],
                         capture_output=True, text=True).stdout
    return {l.split()[-1] for l in out.splitlines() if len(l.split()) >= 2 and l.split()[-2] not in "undU"}

BASE_SYMS = new_symbols(f"{D}/base_direct.o")

def score(obj):
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as tf:
        p = tf.name
    subprocess.run([f"{REPO}/build/tools/objdiff-cli", "diff", "-1", TARGET, "-2", obj,
                    SYM, "--format", "json", "-o", p], capture_output=True, text=True, cwd=REPO)
    try:
        d = json.load(open(p))
    except Exception:
        return None
    finally:
        os.unlink(p)
    for side in ("left", "right"):
        for s in d.get(side, {}).get("symbols", []):
            if isinstance(s, dict) and SYM in str(s.get("name", "")):
                mp = s.get("match_percent")
                if mp is not None:
                    return float(mp)
    return None

dirs = [d for d in glob.glob(f"{D}/output-*") if os.path.isdir(d)]
rows = []
for d in dirs:
    src = f"{d}/source.c"
    if not os.path.exists(src):
        continue
    o = d + ".o"
    if os.path.exists(o) and os.path.getmtime(o) > os.path.getmtime(src):
        pass
    else:
        r = subprocess.run(["bash", f"{D}/compile.sh", src, "-o", o], capture_output=True, text=True, cwd=D)
        if r.returncode != 0:
            rows.append((d, "COMPILE_FAIL", None)); continue
    sz = fn_size(o)
    if sz != EXPECT:
        rows.append((d, f"SIZE-{sz}", None)); continue
    extra = new_symbols(o) - BASE_SYMS
    if extra:
        rows.append((d, f"NEWSYM-{sorted(extra)[:2]}", None)); continue
    rows.append((d, "OK", score(o)))

good = sorted([r for r in rows if r[2] is not None], key=lambda x: -x[2])
print("== ranked (objdiff):")
for d, st, sc in good[:20]:
    print(f"{sc:7.3f}  {os.path.basename(d)}")
import collections
print("== rejects:", collections.Counter(st for _, st, sc in rows if sc is None))
json.dump([{"dir": d, "status": st, "score": sc} for d, st, sc in rows], open(f"{D}/harvest.json", "w"), indent=1)
