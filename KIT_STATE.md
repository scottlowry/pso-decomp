# KIT_STATE — TLobby__sub_803FE6CC campaign (branch card-803fe6cc-v1)

## Seat spine
- Seat: TLobby__sub_803FE6CC, .text:0x803FE6CC, gate 0x154 (340B, 85 insns).
- Owner unit: psov3/pso/network/TLobby_803FCF44 — UNLINKED (linked_units.txt verified
  absent). DOL-inert; prove inertness via unit .o sha + report_delta.
- Pin (live build.ninja): GC/1.2.5n -char signed -use_lmw_stmw on -O4,p -inline off
  -opt nocse -lang=c.
- Body home: src/pso/network/TLobby_803FCF44.c lines ~1829-1911, wrapped in
  `#pragma push / opt_lifetimes off / pop` (function window).
- Era anatomy: frame 0x40; `stmw r26,0x28(r1)` (6-reg bank); prologue binds
  c(r6)→r30 tested, self(r3)→r28, a(r4)→r29, r31=self[0xc]; c==0 pool-bump block
  (lbl_805C04A8 at @ha/@l, rebinds buf→r30); `(u8)a` switch ≤0xB via
  jumptable_804FD5F8; join range test 9..11 → write_network_u32_be; get_field_4 +
  alloc_from_buffer + 2×stb + write_network_u16_be tail; alloc-null → -1; tail call
  TLobby__sub_80406624(0,0,m[4],buf); epilogue lmw r26.

## VISIT-1 (Nov-8, base 00cda35c) — ZERO-BUILD CENSUS CLOSE
Tip measured FIRST: 98.35294 paired, GATE-EXACT 340/340, 85/85 rows, 19 residual rows.
PAIRING-BREAK census: unit .text total 0x79A4 = era exact → body PRESENT, no mis-split.
All 19 rows classified; sealed classes ONLY:
1. def-binding home ring (17 rows): cyclic +1 rotation over (r28,r29,r30) of
   {self,a,c/buf}; r26/r27/r31 pinned. Relative-rank-preserve fires ⇒ decl-order
   STRUCTURALLY INERT. DO NOT RE-ROLL (grid cap 0 — sealed).
2. jumptable pool-name @391 vs jumptable_804FD5F8 (2 rows): symbols.txt claim exists
   (45788, size 0x30, local). OURS name is .o-symbol-table-sourced ⇒ unfixable by
   config (load_bml_exec @139 precedent). ACCEPTED.
Battery green: full ninja rc=0; report_delta regressions 0; check_pr PASS;
DOL 0d85744b... constant; .o 584a1856.... Receipt: tools/perm-tests/fe6cc_v1/census.md.
Budget spent: 0 grind builds (1 unit-.o tip-measure rebuild + base full ninja).

## CLOSED-CLASS list (do-not-re-roll, grows per visit)
- def-binding home ring (cyclic 3-reg rotation, rank-preserve proven zero-build).
- jumptable @NNN pool-name display (config-unfixable, claimed already).
- opt_lifetimes window: inherited from tip (present, do not strip without a spelled row).

## VISIT-2 frontier (ranked)
1. THIS SEAT: no spelled rung. Re-open ONLY on a new mechanism (era MAP /
   context-binding / version rosetta at gate — ring has 17 rows, all cyclic-color;
   nothing decl-grid can touch). Park ceiling 98.35294.
2. UNIT SUPPLY (same file, for carding — NOT this lane's seat): remaining sub-100
   rows in TLobby_803FCF44 at tip:
   - TLobby__sub_803FFB84 (1520B) — 99.30526
   - PADRead (768B) — 99.24479
   Unit: 115/118 fns matched, fuzzy 99.92948, data 100.0, .text total exact.
   Cold-author stub count: 0 (all bodies present).
3. Linked_units row for TLobby_803FCF44: INCOMPLETE (3 sub-100 fns) — pair-complete
   unit is the gate; config ask, never lane-touched.

## Cold-start commands (verbatim)
```
cd /Users/scott/Hermes/pso-decomp/pso-decomp-f4
git branch --show-current   # card-803fe6cc-v1
~/.hermes/installs/60d8a79da6991a71/environments/28d86d1068e44adc8d1a5d2ca8c63c2c/venv/bin/python3.14 configure.py -v GPOE8P
ninja   # rc=0 required
rm -f build/GPOE8P/src/pso/network/TLobby_803FCF44.o && ninja build/GPOE8P/src/pso/network/TLobby_803FCF44.o   # must print MWCC line
~/.hermes/installs/60d8a79da6991a71/environments/28d86d1068e44adc8d1a5d2ca8c63c2c/venv/bin/python3.14 /Users/scott/.hermes/profiles/pso-decomp/skills/pso-decomp/scripts/one_shot_diff.py psov3/pso/network/TLobby_803FCF44 803FE6CC
/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/llvm-nm -S build/GPOE8P/src/pso/network/TLobby_803FCF44.o | grep -i 803FE6CC   # gate 0x154, INT-parse
python3 tools/report_delta.py cache/base_report_fe6cc.json build/GPOE8P/report.json --check
python3 tools/check_pr.py
```
