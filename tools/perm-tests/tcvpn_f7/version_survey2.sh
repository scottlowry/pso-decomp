#!/bin/bash
# ASM-CLASS screen v2b: self-contained probe TU, all 20 GC compilers, verbatim flags,
# per-version -o dirs (MWCC -o takes a directory; output name derives from input).
cd /Users/scott/Hermes/pso-decomp/pso-decomp-f7 || exit 1
GNM=/opt/homebrew/opt/binutils/bin/gnm
CMD=$(ninja -t commands build/GPOE8P/src/pso/unk/text_803E2D70.o | tail -1 | sed 's/ &&.*//')
PROBE=tools/perm-tests/tcvpn_f7/probe_v1.cpp
OUT=tools/perm-tests/tcvpn_f7/survey2
: > "$OUT/results.tsv"
for V in $(ls build/compilers/GC/); do
  mkdir -p "$OUT/$V"
  CC="build/compilers/GC/$V/mwcceppc.exe"
  C2="${CMD/build\/compilers\/GC\/2.6\/mwcceppc.exe/$CC}"
  C2="${C2/-MMD /}"
  C2="${C2/-o build\/GPOE8P\/src\/pso\/unk/-o $OUT/$V}"
  C2="${C2/src\/pso\/unk\/text_803E2D70.cpp/$PROBE}"
  eval "$C2" > "$OUT/$V.log" 2>&1
  RC=$?
  OBJ="$OUT/$V/probe_v1.o"
  if [ ! -f "$OBJ" ]; then
    ERRT=$(grep -m1 'Error:' "$OUT/$V.log" | tr -d '\r' | cut -c1-60)
    printf "%s\tNO_OBJ\trc=%s\t%s\n" "$V" "$RC" "$ERRT" >> "$OUT/results.tsv"
    continue
  fi
  SZ=$($GNM -S "$OBJ" 2>/dev/null | awk '/T transform_chunk_vertices_pos_normal/{print $2}')
  PS=$(build/binutils/powerpc-eabi-objdump -d "$OBJ" 2>/dev/null | grep -cE 'ps_madds|ps_muls|ps_madd\b|ps_mul\b|psq_lu')
  printf "%s\tsize=%s\tps-ops=%s\n" "$V" "${SZ:-ABSENT}" "$PS" >> "$OUT/results.tsv"
done
rm -f build/GPOE8P/src/pso/unk/probe_v1.o build/GPOE8P/src/pso/unk/probe_v1.d
cat "$OUT/results.tsv"
