#!/opt/homebrew/bin/python3.14
# rowdump.py CAND.o — orig-vs-candidate aligned rows (raw objdiff view)
import json, subprocess, sys, itertools
REPO = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3"
K = f"{REPO}/perm-tests/TRaderMapCore_801FA6CC"
SYM = "draw_compass__13TRaderMapCoreFv"
cand = sys.argv[1]
p = subprocess.run([f"{REPO}/build/tools/objdiff-cli", "diff", "-1", f"{REPO}/build/GPOE8P/obj/pso/misc/TRaderMapCore.o", "-2", cand, SYM, "--format", "json", "-o", "-"], capture_output=True, text=True)
d = json.loads(p.stdout)
def sym(side):
    for s in d[side]["symbols"]:
        if isinstance(s, dict) and SYM in str(s.get("name", "")):
            return s
o, n = sym("left"), sym("right")
ro, rn = o.get("instructions", []), n.get("instructions", [])
def fmt(r):
    if r is None: return "<none>"
    i = r.get("instruction")
    if not i: return f"<{r.get('kind','?')}>"
    return str(i.get("formatted") or i.get("text"))[:46]
print("match:", o.get("match_percent"), "rows:", len(ro), len(rn))
for idx, (a, b) in enumerate(itertools.zip_longest(ro, rn)):
    fa, fb = fmt(a), fmt(b)
    mark = "  " if fa == fb else "!!"
    print(f"{mark}{idx:3} O: {fa:46} N: {fb}")
