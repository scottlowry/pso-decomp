#!/bin/bash
# Serial 802C4B64 lane harness: swap a variant into the real TU path, rebuild the
# unit .o (rm -f first = stale-.o trap), gnm size gate, objdiff score + rows.
# Usage: run_variant.sh <variant.cpp>
set -u
REPO=/Users/scott/Hermes/pso-decomp/pso-decomp-f7
SRC=$REPO/src/pso/ui/TAdSelectGameModeGC_802C4748.cpp
O=build/GPOE8P/src/pso/ui/TAdSelectGameModeGC_802C4748.o
GNM=/opt/homebrew/opt/binutils/bin/gnm
ONE=/Users/scott/.hermes/profiles/pso-decomp/skills/pso-decomp/scripts/one_shot_diff.py
VAR=$(cd "$(dirname "$1")" && pwd)/$(basename "$1")
cd "$REPO" || exit 9
cp "$VAR" "$SRC" || exit 9
rm -f "$O"
ninja -j2 "$O" > /dev/null 2>&1
RC=$?
if [ $RC -ne 0 ]; then echo "$(basename "$1") BUILD_FAIL rc=$RC"; exit 8; fi
SZ=$($GNM -S "$O" | grep -i '802c4b64' | awk '{print $2}')
OUT=$(python3 "$ONE" psov3/pso/ui/TAdSelectGameModeGC_802C4748 sub_802C4B64 2>&1)
SC=$(echo "$OUT" | grep '^ORIG' | sed 's/.*match=\([0-9.]*\).*/\1/')
NR=$(echo "$OUT" | grep -c '^  slot')
echo "$(basename "$1")  score=$SC  gnm=0x$SZ $( [ "$SZ" = "0000013c" ] && echo GATE_OK || echo GATE_BAD )  diffrows=$NR"
echo "$OUT" | grep '^  slot' | sed 's/^/    /'
