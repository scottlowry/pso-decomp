#!/bin/bash
# e2964 in-place probe: write candidate to real TU path, run verbatim ninja compile cmd, score, restore.
# Usage: e2964_probe.sh <candidate.cpp> [lo hi]
set -u
REPO=/Users/scott/Hermes/pso-decomp/pso-decomp-f8
S=/Users/scott/.hermes/profiles/pso-decomp/cache/scratch
CAND="$1"; shift
REL=src/pso/enemy/TObjEnePanarms.cpp
SYM=TObjEnePanarms__sub_800E2964
cd "$REPO" || exit 1
cp "$CAND" "$REL" || { echo CP-FAIL; exit 1; }
python3 - <<'PYEOF'
import shlex, subprocess, sys
line = open('/Users/scott/.hermes/profiles/pso-decomp/cache/scratch/e2964_cc.txt').read().split(' && ')[0]
args = shlex.split(line)
r = subprocess.run(args, capture_output=True, text=True)
out = (r.stdout + r.stderr).strip().splitlines()
print('\n'.join(out[-6:]))
sys.exit(r.returncode)
PYEOF
RC=$?
git show HEAD:$REL > $REL
if [ $RC -ne 0 ]; then echo "COMPILE FAIL rc=$RC"; exit $RC; fi
python3 /Users/scott/.hermes/profiles/pso-decomp/skills/pso-decomp/scripts/probe_diff.py \
  "build/GPOE8P/${REL%.cpp}.o" "$SYM" "build/GPOE8P/asm/pso/enemy/TObjEnePanarms.s" "$@" 2>&1 | tail -40
/opt/homebrew/opt/binutils/bin/gnm -S "build/GPOE8P/${REL%.cpp}.o" | grep "$SYM"
git status --porcelain | head -3
