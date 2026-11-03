#!/bin/sh
# 20-version rosetta sweep on the a8b4 probe (era ring: loop1 walker=r27 i=r30; loop2 walk=26 i=27 size=28 elem=29)
cd /Users/scott/Hermes/pso-decomp/pso-decomp-f3
G=/opt/homebrew/opt/binutils/bin
out=perm-tests/f3_adxr_a8b4_rosetta.txt
: > $out
for v in $(ls build/compilers/GC); do
  o=perm-tests/f3_adxr_a8b4_$v.o
  if build/tools/wibo build/compilers/GC/$v/mwcceppc.exe -nodefaults -proc gekko -align powerpc -enum int -fp hardware -Cpp_exceptions off -RTTI off -str reuse -maxerrors 1 -nosyspath -char signed -use_lmw_stmw on -O4,p -inline off -lang=c++ -c perm-tests/f3_adxr_a8b4_probe.cpp -o $o 2>perm-tests/f3_adxr_a8b4_$v.log; then
    sz=$($G/gnm -S $o | awk '/TLobby__sub_803CA8B4/{print $2}')
    d=$($G/objdump -d $o | awk '/<TLobby__sub_803CA8B4>:/,/blr/' | grep -E "mr +r[0-9]+, *r31|li +r[0-9]+, *0$|slwi +r[0-9]+, *r0, *1|lwz +r[0-9]+, *24\(r" | sed 's/.*\t//' | tr -s ' ' | paste -sd';' -)
    echo "$v size=$((16#$sz)) ring: $d" >> $out
  else
    echo "$v CONSTRUCT_CRASH" >> $out
  fi
done
cat $out
