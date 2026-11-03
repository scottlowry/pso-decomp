#!/bin/bash
# launch a capped permuter round in one state-kit. usage: run_round.sh <dir> <cap_sec> [extra flags...]
# PROOF STANDARD: reports mtime/iters/harvest deltas so a dead glob-abort or stale
# dir can never masquerade as an executed round.
K=/Users/scott/Hermes/pso-decomp/pso-decomp-f3/perm-tests/TLobby_80428DC8-v2
D="$1"; CAP="$2"; shift 2
cd "$K/$D" || { echo "MISSING $D"; exit 2; }
GNM=/opt/homebrew/opt/binutils/bin/gnm
export PATH="/opt/homebrew/opt/binutils/bin:/Users/scott/Hermes/pso-decomp/pso-decomp-f3/build/binutils:$PATH"
command -v "$GNM" >/dev/null || { echo "GNM-MISSING $GNM"; exit 3; }
[ -x "$GNM" ] || { echo "GNM-NOT-EXEC $GNM"; exit 3; }
T0=$(date +%s)
PREV_HARV=$(find . -maxdepth 1 -name 'output-*' -type d 2>/dev/null | wc -l | tr -d ' ')
/usr/bin/timeout "$CAP" /Users/scott/Hermes/tools/decomp-permuter/.venv/bin/python \
  /Users/scott/Hermes/tools/decomp-permuter/permuter.py . --stop-on-zero --better-only "$@" > run.log 2>&1
RC=$?
ITERS=$(tr '\r' '\n' < run.log | grep -c 'iteration')
LOGMT=$(stat -f %m run.log 2>/dev/null || echo 0)
HARV=$(find . -maxdepth 1 -name 'output-*' -type d 2>/dev/null | wc -l | tr -d ' ')
FRESH=$(find . -maxdepth 1 -name 'output-*' -type d -newermt "@$T0" 2>/dev/null | wc -l | tr -d ' ')
PROOF="NO"
if [ "$LOGMT" -ge "$T0" ] && [ "$ITERS" -gt 0 ]; then PROOF="YES"; fi
echo "$D rc=$RC t0=$T0 logmt=$LOGMT iters=$ITERS harvests=$HARV(prev=$PREV_HARV) fresh=$FRESH PROOF=$PROOF"
