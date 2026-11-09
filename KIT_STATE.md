# KIT_STATE — TLobby_803FCF44 PADRead campaign (branch card-padread-v1)

## Seat spine
- Seat: PADRead, .text:0x80402E68, gate 0x300 (768B, 192 rows). Name era-true
  (symbols.txt:27466 PADRead — cold-author + rank-preserve seals name it).
- Owner unit: psov3/pso/network/TLobby_803FCF44 — UNLINKED (linked_units.txt verified
  absent). DOL-inert: sha1 0d85744b51d7379efb025a943d0cd5aaae2191a3 = expected constant;
  unit .o sha1 584a185666eff0e695e56d55f953155d43ecddbb stable across fe6cc+padread visits.
- Pin (live build.ninja:57941): GC/1.2.5n -char signed -use_lmw_stmw on -O4,p
  -inline off -opt nocse -lang=c.
- Body home: src/pso/network/TLobby_803FCF44.c ~4401-4466, wrapped
  `#pragma push / dont_inline off / inline_depth(4) / pop` (inherited, keep).
- Era anatomy: frame 0x38; stmw r26,0x20(r1) (6-reg bank 26..31); r30=self pinned;
  f30=self[0x30] loaded 3x (top r31, c2-reload r28, c3-reload r27); switch hdr.type
  {1,2,3}; p=self[0xc] loaded per-case (c1 r29, c2 r28 — SHARED with f30 after kill);
  byte-mask ~0x10(c1)/~0x20(c2) lbz/stb + self[0]=5 when (self[2]&0x30)==0; c2/c3
  read_text_field; (+8) stw keyed off f30 reload (93 c2, 165 c3); c3 f30[0]/[4]=0
  stores keyed off TOP f30 (181/183) + self[0]=0 + lbl_805D7A80=1; zero-byte stbx
  scratch r3 (ours r5) at 88/89, 160/161; TLobby__sub_803FE8BC header-read early
  return; hdr.len-=4; TLobby__sub_80401CAC; calls 80405304, 80400ACC, 80403308.

## VISIT-1 (Nov-8, base 00cda35c) — ZERO-BUILD CENSUS CLOSE
Tip measured FIRST: 99.24479 paired (meter + official report.json agree), GATE-EXACT
768/768, 192/192 rows, 29 residual rows. PAIRING-BREAK: .text 0x79A4 era-exact,
118 T symbols int-parse clean, 0 stubs. ALL 29 rows PURE REGISTER SUBSTITUTION.
Rank-preserve diagnostic FIRES 3 ways (full data in tools/perm-tests/padread_v1/census.md):
era f30 homes {31,28,27} distinct vs ours {29,29,31} non-injective => no cyclic shift;
era r28->ours {26,27,29} multi-valued => era per-case RA range-recycling (c2 f30==p
SHARED reg unreachable by ANY stable-home permutation); c1 distinct-role ranks
preserved both sides. Classes: def-binding home-ring (rank-preserve, 4th firing
campaign-wide), RA-spill era-layout (recycling + caller-saved r3/r5 scratch),
EXTSH-BIND. NO spelled rung; decl-grid cap 0 (sealed). Battery green, 0 grind builds.

## CLOSED-CLASS list (do-not-re-roll, grows per visit)
- def-binding home ring (cyclic rotation + rank-preserve: 3x fe6cc-unit + PADRead).
- RA-spill era-layout (per-case live-range recycling; stable-home model cannot spell
  shared-register eras). PADRead datum: era c2 f30==p==r28.
- EXTSH-BIND (extsh src binds self-copy home; PADRead slots 95/167 r29->r28 shape).
- jumptable @NNN pool-name display (config-unfixable; NOT struck in PADRead — 0 rows).
- opt_lifetimes / pragma windows: inherited at tip, do not strip without spelled row.

## UNIT SUPPLY (same file) — carding status
- TLobby__sub_803FE6CC: 98.35294 gate-exact PARKED (fe6cc v1, zero-build census).
- TLobby__sub_803FFB84 (1520B): 99.30526 — OPEN, f3 twin lane (card-803ffb84-v1,
  same base, read-only cross-tree observed active).
- PADRead (768B): 99.24479 gate-exact PARKED (this seat, padread v1, zero-build).
Unit: 115/118 fns matched, fuzzy 99.92948, .text total exact, 0 stubs. Linked_units
row for TLobby_803FCF44: INCOMPLETE (3 sub-100 fns) — pair-complete-unit is
INTEGRATOR-side, never lane-touched.

## VISIT-2 frontier (ranked)
1. THIS SEAT: no spelled rung. Re-open ONLY on new mechanism reaching per-case RA
   range recycling (era MAP / context-binding at gate). Park ceiling 99.24479.
2. Campaign: 803FFB84 twin is last sub-100 body in unit; when twin lands 100.0,
   unit link ask goes integrator-side (ship lowest-address-first per law p).

## Cold-start commands (verbatim)
```
cd /Users/scott/Hermes/pso-decomp/pso-decomp-f4
git branch --show-current   # card-padread-v1
~/.hermes/installs/60d8a79da6991a71/environments/28d86d1068e44adc8d1a5d2ca8c63c2c/venv/bin/python3.14 configure.py -v GPOE8P
ninja   # rc=0 required
rm -f build/GPOE8P/src/pso/network/TLobby_803FCF44.o && ninja build/GPOE8P/src/pso/network/TLobby_803FCF44.o   # must print MWCC line
~/.hermes/installs/60d8a79da6991a71/environments/28d86d1068e44adc8d1a5d2ca8c63c2c/venv/bin/python3.14 /Users/scott/.hermes/profiles/pso-decomp/skills/pso-decomp/scripts/one_shot_diff.py psov3/pso/network/TLobby_803FCF44 PADRead   # needle = row name, addr 80402E68
/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/llvm-nm -S build/GPOE8P/src/pso/network/TLobby_803FCF44.o | grep PADRead   # gate 0x300, INT-parse
python3 tools/report_delta.py cache/base_report_padread.json build/GPOE8P/report.json --check
python3 tools/check_pr.py
```
