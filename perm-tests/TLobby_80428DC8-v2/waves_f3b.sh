#!/bin/bash
# f3 continuation wave B: the combinational pass class the hand-grid can't reach
# (compound/split expansion on the m4 champ base) + second plain seed run.
K=/Users/scott/Hermes/pso-decomp/pso-decomp-f3/perm-tests/TLobby_80428DC8-v2
clean() { find "$K/$1" -maxdepth 1 -name 'output-*' -exec rm -rf {} + 2>/dev/null; true; }

echo "=== WB1 start $(date)"
clean rS5mc; clean rS4m4b
mkdir -p "$K/rS4m4b"
cp "$K/rS4m4/base.c" "$K/rS4m4/settings.toml" "$K/rS4m4/compile.sh" "$K/rS4m4/target.o" "$K/rS4m4/target.s" "$K/rS4m4/bverify.py" "$K/rS4m4b/"
(cd "$K/rS4m4b" && export PATH="/opt/homebrew/opt/binutils/bin:$PATH" && bash compile.sh base.c -o base_direct.o >/dev/null 2>&1)
bash "$K/run_round.sh" rS5mc 900 -j 2 &
PA=$!
bash "$K/run_round.sh" rS4m4b 900 -j 2 &
PB=$!
wait $PA; wait $PB
echo "=== WB1 done $(date)"
echo "=== ALL-WAVES-F3B-DONE"
