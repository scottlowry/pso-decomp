#!/opt/homebrew/bin/python3.14
"""Raw objdiff score of draw_compass for any candidate .o (offline, no ninja).
Calibration: repo .o champ must print 85.899086.
Usage: probe_score.py cand.o [cand2.o ...]
"""
import json, re, subprocess, sys

REPO = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3"
ORIG = f"{REPO}/build/GPOE8P/obj/pso/misc/TRaderMapCore.o"
SYM = "draw_compass__13TRaderMapCoreFv"

for o in sys.argv[1:]:
    p = subprocess.run([f"{REPO}/build/tools/objdiff-cli", "diff",
                        "-1", ORIG, "-2", o, SYM, "--format", "json", "-o", "-"],
                       capture_output=True, text=True)
    if p.returncode != 0:
        print(f"{o}: rc={p.returncode} {p.stderr[:200]}")
        continue
    try:
        d = json.loads(p.stdout)
    except Exception:
        m = re.search(r'"match_percent":\s*([\d.]+)', p.stdout)
        print(f"{o}: match={m.group(1) if m else 'PARSEFAIL'}")
        continue
    def dig(x):
        out = []
        if isinstance(x, dict):
            if "match_percent" in x:
                out.append((x.get("name", "?"), x["match_percent"], x.get("size", "?")))
            for v in x.values():
                out += dig(v)
        elif isinstance(x, list):
            for v in x:
                out += dig(v)
        return out
    for nm, mp, sz in dig(d):
        if SYM in str(nm) or nm == "?":
            print(f"{o}: {nm} match={mp} size={sz}")
