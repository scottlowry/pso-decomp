#!/bin/bash
# vgrid.sh — compile all variants/*.c serially into v/<name>/out.o, then orank --all
KIT=/Users/scott/Hermes/pso-decomp/pso-decomp-f8/tools/perm-tests/f8_TObjPlayer_801D4368
cd "$KIT" || exit 1
export PATH="/opt/homebrew/opt/binutils/bin:/Users/scott/Hermes/pso-decomp/pso-decomp-f8/build/binutils:$PATH"
for f in variants/*.c; do
  name=$(basename "$f" .c)
  mkdir -p "v/$name"
  if bash compile.sh "$f" -o "v/$name/out.o" 2>"v/$name/err.txt"; then
    echo "compiled $name"
  else
    echo "COMPILE-FAIL $name: $(head -3 v/$name/err.txt | tr '\n' ' ')"
  fi
done
/opt/homebrew/bin/python3.14 orank.py --all
