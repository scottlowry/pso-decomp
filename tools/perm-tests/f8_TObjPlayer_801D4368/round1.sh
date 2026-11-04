#!/bin/bash
# wave-1 launcher — f8 TObjPlayer__sub_801D4368 kit
KIT=/Users/scott/Hermes/pso-decomp/pso-decomp-f8/tools/perm-tests/f8_TObjPlayer_801D4368
PERM=/Users/scott/Hermes/tools/decomp-permuter
cd "$KIT" || exit 1
export PATH="/opt/homebrew/opt/binutils/bin:/Users/scott/Hermes/pso-decomp/pso-decomp-f8/build/binutils:$PATH"
command -v gnm >/dev/null || { echo "GNM-MISSING"; exit 1; }
nohup "$PERM/.venv/bin/python" "$PERM/permuter.py" . --stop-on-zero --better-only -j 4 > run1.log 2>&1 &
P=$!
echo "$P" > round1.pid
echo "launched permuter pid=$P at $(date)"
( sleep 1800; kill -0 "$P" 2>/dev/null && kill "$P" 2>/dev/null && echo "capped at $(date)" >> run1.log ) &
echo "cap-wrapper pid=$!"
