#!/bin/bash
# rosetta one-version: $1=version dir, $2=probe.cpp, $3=out.o  (run from repo root)
set -u
REPO=/Users/scott/Hermes/pso-decomp/pso-decomp-f3
V=$1; SRC=$2; OUT=$3
cd "$REPO"
build/tools/wibo "build/compilers/GC/$V/mwcceppc.exe" \
  -nodefaults -proc gekko -align powerpc -enum int -fp hardware \
  -Cpp_exceptions off -RTTI off -str reuse -maxerrors 1 -nosyspath \
  -i build/GPOE8P/include -i include -i src \
  -i libs/dolphin/include -i libs/dolphin/include/dolphin \
  -char signed -use_lmw_stmw on -O4,p -inline off -lang=c++ \
  -c "$SRC" -o "$OUT" 2>&1
rc=$?
echo "RC=$rc"
[ $rc -ne 0 ] && exit $rc
/opt/homebrew/opt/binutils/bin/objdump -d "$OUT" > "$OUT.asm"
/opt/homebrew/opt/binutils/bin/gnm -S "$OUT" | grep 803F2F1C
