#!/bin/bash
# f3 continuation waves: per-state size-preserving rounds, 2 at a time.
# Cleanup uses find (zsh no-match glob trap killed wave launches earlier).
K=/Users/scott/Hermes/pso-decomp/pso-decomp-f3/perm-tests/TLobby_80428DC8-v2
clean() { find "$K/$1" -maxdepth 1 -name 'output-*' -exec rm -rf {} + 2>/dev/null; true; }

echo "=== W1 start $(date)"
clean rS4m4; clean rS3v44
bash "$K/run_round.sh" rS4m4 1500 -j 3 &
P1=$!
bash "$K/run_round.sh" rS3v44 1500 -j 3 &
P2=$!
wait $P1; wait $P2
echo "=== W1 done $(date)"

echo "=== W2 start $(date)"
clean rS3w04; clean rS1v41
bash "$K/run_round.sh" rS3w04 1200 -j 3 &
P3=$!
bash "$K/run_round.sh" rS1v41 1200 -j 3 &
P4=$!
wait $P3; wait $P4
echo "=== W2 done $(date)"

echo "=== W3 start $(date)"
clean rS2v10
bash "$K/run_round.sh" rS2v10 900 -j 3 &
P5=$!
clean rS4m4_stack
mkdir -p "$K/rS4m4_stack"
cp "$K/rS4m4/base.c" "$K/rS4m4/settings.toml" "$K/rS4m4/compile.sh" "$K/rS4m4/target.o" "$K/rS4m4/target.s" "$K/rS4m4/bverify.py" "$K/rS4m4_stack/"
(cd "$K/rS4m4_stack" && bash compile.sh base.c -o base_direct.o >/dev/null 2>&1)
bash "$K/run_round.sh" rS4m4_stack 600 -j 2 --stack-diffs &
P6=$!
wait $P5; wait $P6
echo "=== W3 done $(date)"
echo "=== ALL-WAVES-F3-DONE"
