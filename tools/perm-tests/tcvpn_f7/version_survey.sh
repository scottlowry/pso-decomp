#!/bin/bash
# ASM-CLASS screen: compile current v1 natural-C TU with EVERY installed GC compiler
# using the unit's verbatim profile flags; record fn size + ps-chain presence.
cd /Users/scott/Hermes/pso-decomp/pso-decomp-f7 || exit 1
GNM=/opt/homebrew/opt/binutils/bin/gnm
CMD=$(ninja -t commands build/GPOE8P/src/pso/unk/text_803E2D70.o | tail -1 | sed 's/ &&.*//')
OUT=tools/perm-tests/tcvpn_f7/survey
mkdir -p "$OUT"
: > "$OUT/results.tsv"
for V in $(ls build/compilers/GC/); do
  CC="build/compilers/GC/$V/mwcceppc.exe"
  C2="${CMD/build\/compilers\/GC\/2.6\/mwcceppc.exe/$CC}"
  C2="${C2// -MMD / }"
  O="$OUT/$V.o"
  eval "${C2} -o $O" > "$OUT/$V.log" 2>&1
  RC=$?
  if [ $RC -ne 0 ]; then
    printf "%s\tCOMPILE_FAIL\trc=%s\t\t\t\n" "$V" "$RC" >> "$OUT/results.tsv"
    continue
  fi
  SZ=$($GNM -S "$O" 2>/dev/null | awk '/T transform_chunk_vertices_pos_normal/{print toupper($2)}')
  PS=$(build/binutils/powerpc-eabi-objdump -d "$O" 2>/dev/null | grep -cE 'ps_madds|ps_muls|ps_mul\b|psq_lu')
  WC=$(build/binutils/powerpc-eabi-objdump -d "$O" 2>/dev/null | awk '/<transform_chunk_vertices_pos_normal>:/{f=1;next} f&&/^$/{exit} f&&/^\s+[0-9a-f]+:/{c++} END{print c}')
  printf "%s\tsize=%s\tps-ops=%s\tinsn=%s\trc=0\n" "$V" "${SZ:-ABSENT}" "$PS" "${WC:-0}" >> "$OUT/results.tsv"
done
cat "$OUT/results.tsv"
