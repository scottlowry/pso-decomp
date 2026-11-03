#!/bin/bash
# 12-version (all installed GC dirs) C-inexpressibility sweep for the 0x14 dead-epilogue
# pad_03_8042E9FC_text. For each compiler version and each pure-C spelling, compile with
# the unit's exact profile flags and report the emitted pad size + whether the 5 target
# words appear verbatim at .text offset 0.
cd /Users/scott/Hermes/pso-decomp/pso-decomp-f3 || exit 1
GNM=/opt/homebrew/opt/binutils/bin/gnm
OD=/opt/homebrew/opt/binutils/bin/gobjdump
FLAGS="-nodefaults -proc gekko -align powerpc -enum int -fp hardware -Cpp_exceptions off -RTTI off -str reuse -maxerrors 1 -nosyspath -i build/GPOE8P/include -i include -i src -i libs/dolphin/include -i libs/dolphin/include/dolphin -char signed -use_lmw_stmw on -O4,p -inline off -lang=c++"
TARGET="bb410008 80010024 7c0803a6 38210020 4e800020"
K=perm-tests/f3_text_8042E9FC
for d in build/compilers/GC/*/; do
  v=$(basename "$d")
  for var in v1_empty v2_regs v3_stmtasm v4_asminc; do
    o=$K/sw_${v}_${var}.o
    log=$(build/tools/wibo "$d/mwcceppc.exe" $FLAGS -c $K/$var.cpp -o "$o" 2>&1)
    if [ ! -f "$o" ]; then printf "%-9s %-11s ERR-COMPILE\n" "$v" "$var"; continue; fi
    sz=$($GNM -S "$o" | awk '/pad_03_8042E9FC_text/{print $2}')
    words=$($OD -d "$o" 2>/dev/null | awk '/^[0-9a-f]+ <.*>:/{f=$0 ~ /pad_03/} f&&match($0,/\t[0-9a-f]{8} /){printf "%s ", substr($0,RSTART+1,8)}' | sed 's/ $//')
    if [ "$sz" = "00000014" ] && [ "$words" = "$TARGET" ]; then verdict="EXACT-14"; else verdict="no(size=${sz:-absent})"; fi
    printf "%-9s %-11s size=%s %s\n" "$v" "$var" "${sz:-0}" "$verdict"
    [ "$verdict" = "EXACT-14" ] && printf "          words=%s\n" "$words"
  done
done
