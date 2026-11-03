#!/usr/bin/env python3
"""6BD8 single-variant probe: mutate src via a lambda body, rebuild, score, restore.
Usage: probe_grid.py NAME 'PYCODE'   where PYCODE defines mut(src)->str|None
Prints NAME size score. Keeps mutated copy at /tmp/keep_NAME.cpp on success.
"""
import re, subprocess, sys, os
REPO = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3"
REL = "src/pso/misc/TLobby_804050DC.cpp"
GNM = "/opt/homebrew/opt/binutils/bin/gnm"
orig = open(os.path.join(REPO, REL)).read()
name, pycode = sys.argv[1], sys.argv[2]
loc = {}
exec(pycode, {}, loc)
new = loc["mut"](orig)
if not new or new == orig:
    print(f"{name} SKIP-NOOP"); sys.exit(0)
open(os.path.join(REPO, REL), "w").write(new)
try:
    r = subprocess.run(["ninja", "build/GPOE8P/src/pso/misc/TLobby_804050DC.o"],
                       cwd=REPO, capture_output=True, text=True)
    if r.returncode != 0:
        print(f"{name} BUILD_FAIL {r.stdout[-250:]}"); sys.exit(0)
    g = subprocess.run([GNM, "-S", "build/GPOE8P/src/pso/misc/TLobby_804050DC.o"],
                       cwd=REPO, capture_output=True, text=True)
    m = re.search(r"([0-9a-f]{8}) ([0-9a-f]{8}) T TLobby__sub_80406BD8", g.stdout)
    size = int(m.group(2), 16) if m else -1
    o = subprocess.run([sys.executable,
        "/Users/scott/.hermes/profiles/pso-decomp/skills/pso-decomp/scripts/one_shot_diff.py",
        "psov3/pso/misc/TLobby_804050DC", "sub_80406BD8"], cwd=REPO, capture_output=True, text=True)
    mm = re.search(r"match=([\d.]+)", o.stdout)
    print(f"{name} size={size} score={mm.group(1) if mm else 'PARSE? ' + o.stdout[:150]}")
    if mm:
        open(f"/tmp/keep_{name}.cpp", "w").write(new)
finally:
    open(os.path.join(REPO, REL), "w").write(orig)
