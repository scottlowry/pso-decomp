#!/bin/bash
set -e
REPO=/Users/scott/Hermes/pso-decomp/pso-decomp-f3
DIR=$(cd "$(dirname "$0")" && pwd)
cd "$REPO"
{
  echo '.include "macros.inc"'
  echo '.text'
  echo 'TLobby__sub_80428DC8:'
  awk '/^\.fn TLobby__sub_80428DC8/{f=1;next} /^\.endfn TLobby__sub_80428DC8/{f=0} f' \
    build/GPOE8P/asm/pso/misc/TLobby_80428374.s
} > "$DIR/target.s"
build/binutils/powerpc-eabi-as -mgekko -I build/GPOE8P/include "$DIR/target.s" -o "$DIR/target.o"
echo "target.o built:"
/opt/homebrew/opt/binutils/bin/gnm -S "$DIR/target.o"
