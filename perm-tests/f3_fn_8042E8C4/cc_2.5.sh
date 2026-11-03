#!/bin/bash
# per-variant compile hook: bash compile.sh <file.cpp> -o <out.o>  (standard unit profile)
IN=$(cd "$(dirname "$1")" && pwd)/$(basename "$1")
OUT="$3"; case "$OUT" in /*) ;; *) OUT=$(pwd)/$OUT ;; esac
REPO=/Users/scott/Hermes/pso-decomp/pso-decomp-f3
cd "$REPO" || exit 1
build/tools/wibo build/compilers/GC/2.5/mwcceppc.exe -nodefaults -proc gekko -align powerpc -enum int -fp hardware -Cpp_exceptions off -RTTI off -str reuse -maxerrors 1 -nosyspath -i build/GPOE8P/include -i include -i src -i libs/dolphin/include -i libs/dolphin/include/dolphin -char signed -use_lmw_stmw on -O4,p -inline off -lang=c++ -c "$IN" -o "$OUT"
