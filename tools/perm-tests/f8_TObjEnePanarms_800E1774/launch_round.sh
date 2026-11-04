#!/bin/bash
# launch capped permuter round (recorded PID cap; no raw globs)
KIT=/Users/scott/Hermes/pso-decomp/pso-decomp-f8/tools/perm-tests/f8_TObjEnePanarms_800E1774
cd "$KIT" || exit 1
export PATH="/Users/scott/Hermes/pso-decomp/pso-decomp-f8/build/binutils:/opt/homebrew/opt/binutils/bin:$PATH"
PERM=/Users/scott/Hermes/tools/decomp-permuter
find . -maxdepth 1 -name 'output-*' -exec rm -rf {} +
nohup "$PERM/.venv/bin/python" "$PERM/permuter.py" . --stack-diffs --better-only --stop-on-zero > run_r1.log 2>&1 &
P=$!
echo "$P" > round.pid
( sleep 900; kill -0 "$P" 2>/dev/null && kill "$P" ) > /dev/null 2>&1 &
echo "$!" > cap.pid
echo "round PID=$P cap-wrapper PID=$(cat cap.pid)"
