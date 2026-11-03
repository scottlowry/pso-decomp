#!/usr/bin/env python3.14
"""Rank harvests across all state-kits: size gate 248 -> NEW-SYMBOL gate ->
raw objdiff score vs target.o. Zero repo builds. Prints top candidates per kit."""
import subprocess, json, sys, os, glob, tempfile

KIT = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3/perm-tests/TLobby_80428DC8-v2"
REPO = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3"
TARGET = f"{KIT}/target.o"
SYM = "TLobby__sub_80428DC8"
EXPECT = 248
CHAMP_RAW = 99.67742  # recalibrated Oct31 visit-3: m4 basin (rS4m4/base_direct.o) — was 99.51613 (v44 fold)

def fn_size(obj):
    out = subprocess.run(["/opt/homebrew/opt/binutils/bin/gnm", "-S", obj],
                         capture_output=True, text=True).stdout
    for line in out.splitlines():
        p = line.split()
        if len(p) == 4 and p[-1] == SYM:
            return int(p[1], 16)
    return None

def defined_syms(obj):
    out = subprocess.run(["/opt/homebrew/opt/binutils/bin/gnm", obj],
                         capture_output=True, text=True).stdout
    return {l.split()[-1] for l in out.splitlines()
            if len(l.split()) >= 2 and l.split()[-2] not in "undU"}

BASE_SYMS = defined_syms(f"{KIT}/base_direct.o")

def score(obj):
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as tf:
        p = tf.name
    subprocess.run([f"{REPO}/build/tools/objdiff-cli", "diff", "-1", TARGET, "-2", obj,
                    SYM, "--format", "json", "-o", p], capture_output=True, text=True, cwd=REPO)
    try:
        d = json.load(open(p))
        for side in ("left", "right"):
            for s in d.get(side, {}).get("symbols", []):
                if isinstance(s, dict) and SYM in str(s.get("name", "")):
                    mp = s.get("match_percent")
                    if mp is not None:
                        return float(mp)
    except Exception:
        return None
    finally:
        os.unlink(p)
    return None

kits = sys.argv[1:] or sorted(glob.glob(f"{KIT}/rS*"))
allrows = []
for kd in kits:
    if not os.path.isdir(kd):
        continue
    gold = f"{kd}/base_direct.o"
    gold_syms = defined_syms(gold) if os.path.exists(gold) else BASE_SYMS
    dirs = [d for d in glob.glob(f"{kd}/output-*") if os.path.isdir(d)]
    n = 0
    for d in dirs:
        src = f"{d}/source.c"
        if not os.path.exists(src):
            continue
        n += 1
        o = d + ".o"
        if not (os.path.exists(o) and os.path.getmtime(o) > os.path.getmtime(src)):
            r = subprocess.run(["bash", f"{kd}/compile.sh", src, "-o", o],
                               capture_output=True, text=True, cwd=kd)
            if r.returncode != 0:
                allrows.append((os.path.basename(kd), d, "COMPILE_FAIL", None)); continue
        sz = fn_size(o)
        if sz != EXPECT:
            allrows.append((os.path.basename(kd), d, f"SIZE-{sz}", None)); continue
        extra = defined_syms(o) - gold_syms
        if extra:
            allrows.append((os.path.basename(kd), d, f"NEWSYM-{sorted(extra)}", None)); continue
        allrows.append((os.path.basename(kd), d, "PASS", score(o)))
    print(f"[{os.path.basename(kd)}] harvest dirs with source: {n}", file=sys.stderr)

ok = [r for r in allrows if r[2] == "PASS" and r[3] is not None]
bad = [r for r in allrows if r[2] != "PASS"]
ok.sort(key=lambda r: -r[3])
print(f"\n=== GATE-FAIL rows: {len(bad)} (SIZE/NEWSYM/COMPILE), PASS ranked top 15:")
for kit, d, _, sc in ok[:15]:
    mark = " *** BEATS CHAMP" if sc > CHAMP_RAW + 1e-9 else ""
    print(f"{sc:9.5f}  {kit:14} {d.split('/')[-1]:22}{mark}")
winners = [r for r in ok if r[3] > CHAMP_RAW + 1e-9]
print(f"\nwinners > {CHAMP_RAW}: {len(winners)}")
json.dump([{"kit": k, "dir": d, "score": s} for k, d, st, s in ok],
          open(f"{KIT}/rank_all.json", "w"), indent=1)
