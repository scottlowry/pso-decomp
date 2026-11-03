#!/opt/homebrew/bin/python3.14
"""rank_all_v3.py — final comprehensive re-rank for visit-3.
Sweeps output dirs in perm/, perm_s15/, perm_s16/, perm_s09/ (fresh output-* +
v12-* archives) AND kit-root v12-*. Compiles each source.c via its dir's
compile.sh (cached .o reuse gated by mtime), gates: nm size == 0x1B4 and NO
extra defined symbols, ranks by raw objdiff match. Reports best-per-round-dir
and anything beating 99.633026."""
import glob, json, os, subprocess, sys

K = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3/perm-tests/TRaderMapCore_801FA6CC"
REPO = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3"
ORIG_O = f"{REPO}/build/GPOE8P/obj/pso/misc/TRaderMapCore.o"
SYM = "draw_compass__13TRaderMapCoreFv"
CHAMP = 99.633026

dirs = []
for pat in ("perm*/output-*", "perm*/r1-output-*", "perm*/v12-output-*", "v12-output-*"):
    for d in glob.glob(f"{K}/{pat}"):
        if os.path.isdir(d) and os.path.exists(f"{d}/source.c"):
            dirs.append(d)
print(f"sweeping {len(dirs)} candidate dirs")

NM = "/opt/homebrew/opt/binutils/bin/gnm"
results, fails = [], 0
for d in dirs:
    src = f"{d}/source.c"
    o = d + ".o"
    permdir = os.path.dirname(d)
    if not (os.path.exists(o) and os.path.getmtime(o) > os.path.getmtime(src)):
        r = subprocess.run(["bash", "compile.sh", src, "-o", o], cwd=permdir,
                           capture_output=True, text=True)
        if r.returncode != 0 or not os.path.exists(o):
            fails += 1; continue
    nm = subprocess.run([NM, "-S", o], capture_output=True, text=True).stdout
    lines = [l for l in nm.splitlines() if SYM in l and " T " in l]
    if not lines: continue
    size = int(lines[0].split()[1], 16) if len(lines[0].split()) == 4 else None
    defined = [l.split()[-1] for l in nm.splitlines()
               if len(l.split()) >= 3 and l.split()[1] in "TtDdBbRrWw"]
    extra = [s for s in defined if s != SYM]
    p = subprocess.run([f"{REPO}/build/tools/objdiff-cli", "diff", "-1", ORIG_O, "-2", o, SYM,
                        "--format", "json", "-o", "-"], capture_output=True, text=True)
    if p.returncode != 0: continue
    d0 = json.loads(p.stdout)
    vals = []
    def dig(x):
        if isinstance(x, dict):
            if "match_percent" in x: vals.append(x["match_percent"])
            for v in x.values(): dig(v)
        elif isinstance(x, list):
            for v in x: dig(v)
    dig(d0)
    match = max(vals) if vals else None
    results.append((match, size, os.path.relpath(d, K), extra))

results.sort(key=lambda t: (-(t[0] if t[0] is not None else -1),))
print(f"compile-fails={fails} ranked={len(results)}")
best_size_ok = [r for r in results if r[1] == 0x1B4 and not r[3]]
print(f"size+symtab-gate PASS: {len(best_size_ok)}")
print("--- TOP 12 (any) ---")
for m, sz, rel, ex in results[:12]:
    flags = ("OK" if sz == 0x1B4 and not ex else "") + (f" SIZE={sz}" if sz != 0x1B4 else "") + (f" EXTRA={ex}" if ex else "")
    print(f"  {m}  {rel}  {flags}")
print("--- size-gate-passing above champ ---")
winners = [r for r in best_size_ok if (r[0] or 0) > CHAMP]
for m, sz, rel, ex in winners:
    print(f"  {m}  {rel}")
print(f"winners={len(winners)}")
