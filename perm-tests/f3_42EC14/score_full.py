#!/usr/bin/env python3
"""Full-TU .o swap scorer: put a candidate unit .o in place of the repo one and
score EVERY symbol (siblings must hold 100.0 too). Restores in finally."""
import os, shutil, subprocess, sys, re

REPO = "/Users/scott/Hermes/pso-decomp/pso-decomp-f3"
UNIT_O = f"{REPO}/build/GPOE8P/src/pso/unk/text_8042EAD4.o"
UNIT_ARG = "psov3/pso/unk/text_8042EAD4"
SCRIPTS = "/Users/scott/.hermes/profiles/pso-decomp/skills/pso-decomp/scripts"

bak = UNIT_O + ".fullbak"
made = not os.path.exists(bak)
if made:
    shutil.copy2(UNIT_O, bak)
try:
    for cand in sys.argv[1:]:
        shutil.copy2(cand, UNIT_O)
        p = subprocess.run(["/opt/homebrew/bin/python3.14", f"{SCRIPTS}/one_shot_diff.py", UNIT_ARG],
                           capture_output=True, text=True, cwd=REPO)
        print("###", os.path.basename(cand))
        for ln in p.stdout.splitlines():
            if 'match=' in ln:
                print("   ", ln.strip()[:96])
        if p.returncode != 0:
            print("   ERR", p.stderr[:300])
finally:
    shutil.copy2(bak, UNIT_O)
    if made:
        os.remove(bak)
