#!/bin/bash
# permuter compile hook: bash compile.sh <file.c> -o <out.o>
IN=$(cd "$(dirname "$1")" && pwd)/$(basename "$1")
OUT="$3"
case "$OUT" in /*) ;; *) OUT=$(pwd)/$OUT ;; esac
REPO=/Users/scott/Hermes/pso-decomp/pso-decomp-f3
cd "$REPO" || exit 1
TMP=$(mktemp /tmp/perm8dc8XXXX).cpp
{
  echo 'extern "C" {'
  echo '#pragma push'
  echo '#pragma opt_propagation off'
  cat "$IN"
  echo '#pragma pop'
  echo '}'
} > "$TMP"
build/tools/wibo build/compilers/GC/1.2.5n/mwcceppc.exe -nodefaults -proc gekko -align powerpc -enum int \
  -fp hardware -Cpp_exceptions off -RTTI off -str reuse -maxerrors 1 -nosyspath \
  -i build/GPOE8P/include -i include -i src -i libs/dolphin/include -i libs/dolphin/include/dolphin \
  -char signed -use_lmw_stmw on -O4,p -inline off -lang=c++ \
  -c "$TMP" -o "$OUT"
RC=${PIPESTATUS[0]}
rm -f "$TMP"
exit $RC
