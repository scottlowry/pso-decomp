#!/bin/sh
# try1.sh v11 v12 ... — compile + score + rowdiff each named probe cpp (no repo build)
cd /Users/scott/Hermes/pso-decomp/pso-decomp-f3 || exit 1
K=perm-tests/TRaderMapCore_801FA6CC
for n in "$@"; do
  sh /Users/scott/.hermes/profiles/pso-decomp/skills/pso-decomp/scripts/probe_compile.sh $K/$n.cpp $K/$n.o build/GPOE8P/src/pso/misc/TRaderMapCore.o >/dev/null 2>$K/$n.err || { echo "$n: COMPILE FAIL"; tail -3 $K/$n.err; continue; }
  /opt/homebrew/bin/python3.14 $K/probe_score.py $K/$n.o | grep -v '^$' | tail -1
done
