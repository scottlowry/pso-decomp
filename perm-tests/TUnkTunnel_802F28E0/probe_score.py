#!/opt/homebrew/bin/python3.14
"""Raw objdiff score of run_task for any candidate .o (offline, no ninja).
Calibration: repo .o must print 90.15094.
Usage: probe_score.py cand.o [cand2.o ...]
"""
import json, re, subprocess, sys

REPO = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3"
ORIG = f"{REPO}/build/GPOE8P/obj/pso/boss/TObjBoss2Tunnel_802F2070.o"
SYM = "run_task__13TUnk_804E4B3CFv"

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
    # find symbol stats in either structure
    txt = json.dumps(d)
    mps = re.findall(r'"name":\s*"[^"]*run_task[^"]*".{0,400}?"match_percent":\s*([\d.]+)', txt)
    seq = d.get("left", {})
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
    stats = dig(d)
    ours = [s for s in stats if s[0] == SYM]
    print(f"{o}: {ours if ours else stats[:4]}")
