#!/bin/bash
# Compile a full-TU probe .cpp with THIS unit's exact repo flags (no extern-C wrapper;
# the probe file is a complete text_8042EAD4.cpp variant).
# Usage: sh compile.sh <probe.cpp> <out.o>
IN=$(cd "$(dirname "$1")" && pwd)/$(basename "$1")
OUT="$2"; case "$OUT" in /*) ;; *) OUT=$(pwd)/$OUT ;; esac
REPO=/Users/scott/Hermes/pso-decomp/pso-decomp-f3
cd "$REPO" || exit 1
mkdir -p .cache/giprobe
TMP=".cache/giprobe/f3ec14_$$.cpp"
cp "$IN" "$TMP"
build/tools/wibo build/compilers/GC/2.6/mwcceppc.exe -nodefaults -proc gekko -align powerpc \
  -enum int -fp hardware -Cpp_exceptions off -RTTI off -str reuse -maxerrors 1 -nosyspath \
  -i build/GPOE8P/include -i include -i src -i libs/dolphin/include -i libs/dolphin/include/dolphin \
  -char signed -use_lmw_stmw on -O4,p -inline off -lang=c++ -c "$TMP" -o "$OUT" > "$OUT.log" 2>&1
RC=$?
rm -f "$TMP" "$TMP".d
echo "RC=$RC out=$OUT"
[ -s "$OUT.log" ] && head -6 "$OUT.log"
exit $RC
