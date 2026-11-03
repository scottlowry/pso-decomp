#!/bin/bash
# Build one self-contained permuter kit per rotation state, base-verify each
# (compile.sh base.c vs the battery-produced gen .o — bytes must be identical).
K=/Users/scott/Hermes/pso-decomp/pso-decomp-f3/perm-tests/TLobby_80428DC8-v2
export PATH=/Users/scott/Hermes/pso-decomp/pso-decomp-f3/build/binutils:$PATH
declare_pair() { :; }   # bash3.2-safe

make_kit() {
  local d="$1" src="$2" gold="$3"
  mkdir -p "$K/$d"
  cp "$K/settings.toml" "$K/compile.sh" "$K/target.o" "$K/target.s" "$K/bverify.py" "$K/$d/"
  cp "$K/$src" "$K/$d/base.c"
  ( cd "$K/$d" && bash compile.sh base.c -o base_direct.o >/dev/null 2>&1
    echo "[$d] compile-rc=$?" )
  ls -la "$K/$d/base_direct.o" "$K/$gold" 2>&1 | awk '{print $5, $NF}'
  ( cd "$K/$d" && /opt/homebrew/bin/python3.14 bverify.py base_direct.o "$K/$gold" )
  echo "[$d] BVERIFY-rc=$?"
}
make_kit rS3v44 gen_v44_subfirst.c gen_v44_subfirst.o
make_kit rS3w04 gen_w04_v44_paren.c gen_w04_v44_paren.o
make_kit rS2v10 gen_v10_fold_muladd.c gen_v10_fold_muladd.o
make_kit rS1v41 gen_v41_lassoc.c gen_v41_lassoc.o
