#!/bin/bash
# permuter compile hook: bash compile.sh <file.c> -o <out.o>   (f8 TObjPlayer__sub_801D4368)
# REPO = MY worktree only (path hygiene: never the main checkout)
IN=$(cd "$(dirname "$1")" && pwd)/$(basename "$1")
OUT="$3"
case "$OUT" in /*) ;; *) OUT=$(pwd)/$OUT ;; esac
REPO=/Users/scott/Hermes/pso-decomp/pso-decomp-f8
cd "$REPO" || exit 1
TMP=$(mktemp /tmp/perm4368XXXX).cpp
{
  echo 'extern "C" {'
  cat "$IN"
  echo '}'
} > "$TMP"
build/tools/wibo build/compilers/GC/2.6/mwcceppc.exe -nodefaults -proc gekko -align powerpc -enum int \
  -fp hardware -Cpp_exceptions off -RTTI off -str reuse -maxerrors 1 -nosyspath \
  -i build/GPOE8P/include -i include -i src -i libs/dolphin/include -i libs/dolphin/include/dolphin \
  -char signed -use_lmw_stmw on -O4,s -inline off -sdata2 4 -lang=c++ \
  -c "$TMP" -o "$OUT"
RC=${PIPESTATUS[0]}
rm -f "$TMP"
exit $RC
