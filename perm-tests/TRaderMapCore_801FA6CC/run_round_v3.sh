#!/bin/bash
# usage: run_round_v3.sh <permdir> <cap> <jobs> <log>
D=$1; CAP=$2; J=$3; LOG=$4
K=/Users/scott/Hermes/pso-decomp/pso-decomp-f3/perm-tests/TRaderMapCore_801FA6CC
cd "$K/$D" || exit 1
PATH="/Users/scott/Hermes/pso-decomp/pso-decomp-f3/build/binutils:$PATH" \
  /usr/bin/timeout "$CAP" /Users/scott/Hermes/tools/decomp-permuter/.venv/bin/python \
  /Users/scott/Hermes/tools/decomp-permuter/permuter.py . \
  --better-only --stop-on-zero --stack-diffs -j "$J" > "$LOG" 2>&1
echo "exit=$? cap=${CAP}s jobs=${J}" >> "$LOG"
