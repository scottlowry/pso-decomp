#!/opt/homebrew/bin/python3.14
"""harvest_rank.py — compile all output-*/source.c, size-gate at 436, rank by raw objdiff.
Usage: harvest_rank.py [--fresh]   (default: all dirs; --fresh: only dirs newer than last_rank.json)"""
import json, os, subprocess, sys, glob

HERE = os.path.dirname(os.path.abspath(__file__))
K = os.path.dirname(HERE)  # TRaderMapCore_801FA6CC
SYM = "draw_compass__13TRaderMapCoreFv"
REPO = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3"
ORIG_O = f"{REPO}/build/GPOE8P/obj/pso/misc/TRaderMapCore.o"

dirs = sorted([d for d in glob.glob(f"{HERE}/output-*") if os.path.isdir(d)],
              key=lambda d: os.path.getmtime(d))
if "--fresh" in sys.argv:
    cutoff = 0
    if os.path.exists(f"{HERE}/last_rank.json"):
        cutoff = json.load(open(f"{HERE}/last_rank.json")).get("max_mtime", 0)
    dirs = [d for d in dirs if os.path.getmtime(d) > cutoff]

results = []
for d in dirs:
    src = f"{d}/source.c"
    if not os.path.exists(src):
        continue
    o = f"{d}.o"
    if os.path.exists(o) and os.path.getmtime(o) < os.path.getmtime(src):
        os.remove(o)
    if not os.path.exists(o):
        r = subprocess.run(["bash", "compile.sh", src, "-o", o], cwd=HERE,
                           capture_output=True, text=True)
        if r.returncode != 0 or not os.path.exists(o):
            continue
    # size gate
    nm = subprocess.run(["/opt/homebrew/opt/binutils/bin/gnm", "-S", o], capture_output=True, text=True).stdout
    m = [l for l in nm.splitlines() if SYM in l and " T " in l]
    if not m:
        continue
    f = m[0].split()
    size = int(f[1], 16) if len(f) == 4 else None
    if size != 0x1B4:
        continue
    # new-symbol guard (permuter W helpers)
    defined = [l.split()[-1] for l in nm.splitlines() if len(l.split()) >= 3 and l.split()[1] in "TtDdBb"]
    extra = [s for s in defined if s not in (SYM,)]
    p = subprocess.run([f"{REPO}/build/tools/objdiff-cli", "diff", "-1", ORIG_O, "-2", o, SYM,
                        "--format", "json", "-o", "-"], capture_output=True, text=True)
    score = None
    mm = json.loads(p.stdout) if p.returncode == 0 else None
    def dig(x):
        out = []
        if isinstance(x, dict):
            if "match_percent" in x: out.append(x["match_percent"])
            for v in x.values(): out += dig(v)
        elif isinstance(x, list):
            for v in x: out += dig(v)
        return out
    vals = dig(mm) if mm else []
    score = max(vals) if vals else None
    results.append((score, d, os.path.getmtime(d), extra))

results.sort(key=lambda t: (-1 if t[0] is None else t[0],))
for sc, d, mt, extra in results[:25]:
    print(f"{sc}  {os.path.basename(d)}  perm={os.path.basename(d).split('-')[1] if len(d.split('-'))>1 else '?'}"
          + (f"  EXTRA-SYMS:{extra}" if extra else ""))
print(f"ranked {len(results)} size-passing of {len(dirs)} dirs")
if dirs:
    json.dump({"max_mtime": max(os.path.getmtime(d) for d in dirs)}, open(f"{HERE}/last_rank.json","w"))
