#!/bin/bash
# dcpol_f7 round 1 launcher — separate statements (zsh-glob & bg-precedence traps)
set -u
cd /Users/scott/Hermes/pso-decomp/pso-decomp-f7/tools/perm-tests/dcpol_f7/perm || exit 1
export PATH="/opt/homebrew/opt/binutils/bin:/Users/scott/Hermes/pso-decomp/pso-decomp-f7/build/binutils:$PATH"
nohup /Users/scott/Hermes/tools/decomp-permuter/.venv/bin/python /Users/scott/Hermes/tools/decomp-permuter/permuter.py . --better-only --stop-on-zero -j 4 > run1.log 2>&1 &
P=$!
echo "$P" > perm.pid
nohup bash -c "sleep 900; kill -0 $P 2>/dev/null && kill -TERM $P; sleep 15; kill -9 $P 2>/dev/null" > /dev/null 2>&1 &
C=$!
echo "$C" > cap.pid
echo "PERM_PID=$P CAP_PID=$C LAUNCH_TS=$(date +%s)"
