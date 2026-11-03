#!/bin/bash
# ASM-CLASS screen: compile the champ TU with EVERY installed GC compiler using the
# unit's verbatim flags; report fn size + which scratch reg takes &col(r1+0x8) vs &pos(r1+0x28).
cd /Users/scott/Hermes/pso-decomp/pso-decomp-f7 || exit 1
GNM=/opt/homebrew/opt/binutils/bin/gnm
OD=build/binutils/powerpc-eabi-objdump
CMD=$(ninja -t commands build/GPOE8P/src/pso/ui/TAdSelectGameModeGC_802C4748.o | tail -1 | sed 's/ &&.*//')
OUT=tools/perm-tests/serial_f7/survey
mkdir -p "$OUT"; : > "$OUT/results.tsv"
for V in $(ls build/compilers/GC/); do
  CC="build/compilers/GC/$V/mwcceppc.exe"
  C2="${CMD/build\/compilers\/GC\/2.6\/mwcceppc.exe/$CC}"
  C2="${C2// -MMD / }"
  O="$OUT/$V.o"
  eval "${C2} -o $O" > "$OUT/$V.log" 2>&1
  RC=$?
  if [ $RC -ne 0 ]; then printf "%s\tCOMPILE_FAIL rc=%s\n" "$V" "$RC" >> "$OUT/results.tsv"; continue; fi
  SZ=$($GNM -S "$O" 2>/dev/null | awk '/TAdEnterSerialAccessGC__sub_802C4B64/{print toupper($2)}')
  SEQ=$($OD -d "$O" 2>/dev/null | awk '/<TAdEnterSerialAccessGC__sub_802C4B64>:/{f=1;next} f&&/^$/{exit} f{print}' \
        | grep -E 'addi +r[0-9]+, *r1, 0x(8|28)$' | sed -E 's/.*addi (r[0-9]+), r1, (0x[0-9a-f]+).*/\2->\1/' | tr '\n' ' ')
  printf "%s\tsize=%s\t%s\n" "$V" "${SZ:-ABSENT}" "$SEQ" >> "$OUT/results.tsv"
done
cat "$OUT/results.tsv"
