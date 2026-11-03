#!/bin/bash
# Permuter compile wrapper: dispatch_chunk_polygon_list (pso/unk/text_803E2D70.cpp, GPOE8P).
# $1 = candidate .c (pure C), $3 = output .o (ABS path).
set -e
REPO=/Users/scott/Hermes/pso-decomp/pso-decomp-f7
# absolutize in/out paths BEFORE cd repo (stray-.o-into-repo trap, permuter.md)
case "$1" in /*) :;; *) IN="$(cd "$(dirname "$1")" && pwd)/$(basename "$1")";; esac
[ -n "${IN:-}" ] && set -- "$IN" "$2" "$3"
case "$3" in /*) :;; *) OUT="$(cd "$(dirname "$3")" 2>/dev/null && pwd)/$(basename "$3")";; esac
[ -n "${OUT:-}" ] && set -- "$1" "$2" "$OUT"
TMPD=$(mktemp -d)
trap 'rm -rf "$TMPD"' EXIT
{ printf 'extern "C" {\n'; sed -e '/^typedef int permbool/d' -e 's/permbool/bool/g' "$1"; printf '\n}\n'; } > "$TMPD/text_803E2D70.cpp"
cd "$REPO"
# verbatim ninja mwcc command for this unit (GC/2.6, -O3,p, -opt nopeephole); -MMD dropped
# (depfile litter trap); no gobjcopy (unit rule has none)
build/tools/wibo build/compilers/GC/2.6/mwcceppc.exe \
  -nodefaults -proc gekko -align powerpc -enum int -fp hardware -Cpp_exceptions off \
  -RTTI off -str reuse -maxerrors 1 -nosyspath \
  -i build/GPOE8P/include -i include -i src -i libs/dolphin/include -i libs/dolphin/include/dolphin \
  -char signed -use_lmw_stmw on -O3,p -inline off -opt nopeephole -lang=c++ \
  -c "$TMPD/text_803E2D70.cpp" -o "$TMPD/out.o"
cp "$TMPD/out.o" "$3"
