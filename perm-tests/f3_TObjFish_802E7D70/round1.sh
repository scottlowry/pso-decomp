#!/bin/bash
KIT=/Users/scott/Hermes/pso-decomp/pso-decomp-f3/perm-tests/f3_TObjFish_802E7D70
REPO=/Users/scott/Hermes/pso-decomp/pso-decomp-f3
cd "$KIT" || exit 1
export PATH="$REPO/build/binutils:/opt/homebrew/opt/binutils/bin:$PATH"
nohup /Users/scott/Hermes/tools/decomp-permuter/.venv/bin/python /Users/scott/Hermes/tools/decomp-permuter/permuter.py . --stop-on-zero --better-only -j 4 > run1.log 2>&1 &
P=$!
echo "$P" > round1.pid
echo "launched pid $P"
sleep 1500
if kill -0 "$P" 2>/dev/null; then kill "$P"; echo "capped at 1500s"; fi
wait "$P" 2>/dev/null
echo "round1 DONE rc=$?"
grep -c '^\s*iteration' run1.log | head -1
ls -d "$KIT"/output-* 2>/dev/null | wc -l
