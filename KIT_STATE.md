# KIT_STATE — TLobby__sub_803FFB84 campaign (branch card-803ffb84-v1)

## Seat spine
- Seat: TLobby__sub_803FFB84, .text:0x803FFB84, gate 0x5F0 (1520B, 380 insns).
  Row: config/GPOE8P/psov3/symbols.txt:27421. Era .fn:
  build/GPOE8P/asm/pso/network/TLobby_803FCF44.s:3333-3781.
- Owner unit: psov3/pso/network/TLobby_803FCF44 — UNLINKED (linked_units.txt
  verified absent v1). DOL-inert; inertness = unit .o sha + report_delta.
- Pin (live build.ninja 57943-57949): GC/1.2.5n -char signed -use_lmw_stmw on
  -O4,p -inline off -opt nocse -lang=c.
- Body home: src/pso/network/TLobby_803FCF44.c lines 2632-2874 (predecessor
  fe6cc fn ends with `#pragma pop` at 2631; seat itself NOT in a window).
- Era anatomy: frame 0x40; `stmw r25,0x24(r1)` (7-reg bank r25..r31); binds
  self(r3)->r30(mr), hdr(r6)->r26(mr), p(r4)->r25(addi), a(r5)->r31(addi),
  c(r7)->r27(addi); li r28=2 res; lbz r0,0(r6) switch value r0 NO HOME;
  subi r29=len(hdr[1]-2); balanced cmpwi tree {1,2,3,0x81,0x83,def};
  5 read-site blocks (sub_80401BCC self-first addi r3,rSELF + li lbl_805D7AA8@sda21);
  post-switch `lbz r4,0(r26)` reload + range test (u8 views, cmplwi) +
  slw/and. bit test on *(s16*)a; tail `while(len--)` guarded extsh. r27(c)/
  extsh. r29(len); epilogue lmw r25@0x24.
- Era home stack: {p25, hdr26, c27, res28, len29, self30, a31}.
- Tip home stack: 8 saves {p24, hdr25, c26, SWITCHVAL r27, res28, len29,
  self30, a31} — extra home = decompiler-port local `new_var2 = hdr[0]`.

## VISIT-1 (Nov-8, base 00cda35c) — 99.30526 CHAMPION, 3 rungs, ALL SEALED
Tip measured FIRST: 99.30526 paired, GATE-EXACT 1520/1520, 380/380 rows, 50 diffs.
PAIRING-BREAK: unit .text 0x79A4 = era exact. All rows classified (receipt
tools/perm-tests/ffb84_v1/census.md). Rungs: r1 kill-new_var2 (7 homes) =>
a/pin re-rank + gate death 0x5F4 (rank-preserve fires) = RA-spill era-layout
sealed. r2 pair-1 init-swap => scratch target flip +6. r3 pair-1 decl-split =>
pair-1 lands, pair-2 (0x7c/0x8) use rows break +3 = def-binding lineage, the two
pairs are ONE bind entity, no emitter. Battery green, 0 sibling drift (130 syms
int-parse), .o sha == fe6cc-v1 (tip byte-unchanged at close).

## CLOSED-CLASS list (do-not-re-roll, grows per visit)
- new_var2-home-kill / trio bank-shift / switch-home / tail-reload (48 rows):
  RA-spill era-layout + def-binding home ring, rank-preserve zero-build proof.
- load-order-swap pair (2 rows): def-binding lineage (rung2/3 bracket datum,
  bind follows variable identity through def/decl order permutations).
- jumptable @NNN pool-name: ACCEPTED display class (fe6cc law, none in this seat).

## VISIT-2 frontier
No spelled rung. Re-open ONLY with a new mechanism: era MAP/context-binding for
the 8->7-home rank collapse, or an EXTSH-BIND-style version rosetta at gate
(family ask, integrator key). Park ceiling 99.30526 (largest open residual of
the unit; unit 115/118 matched, fuzzy 99.92948).
UNIT SUPPLY (NOT this lane's seats): PADRead (768B, 99.24479) = f4 twin seat,
same file, own tree, function-scoped (law p). fe6cc seat parked 98.35294
(card-803fe6cc-v1 @ 051ddf30).

## Cold-start commands (verbatim)
```
cd /Users/scott/Hermes/pso-decomp/pso-decomp-f3
git branch --show-current   # card-803ffb84-v1
~/.hermes/installs/60d8a79da6991a71/environments/28d86d1068e44adc8d1a5d2ca8c63c2c/venv/bin/python3.14 configure.py -v GPOE8P
ninja   # rc=0 required
rm -f build/GPOE8P/src/pso/network/TLobby_803FCF44.o && ninja build/GPOE8P/src/pso/network/TLobby_803FCF44.o   # must print MWCC line
~/.hermes/installs/60d8a79da6991a71/environments/28d86d1068e44adc8d1a5d2ca8c63c2c/venv/bin/python3.14 /Users/scott/.hermes/profiles/pso-decomp/skills/pso-decomp/scripts/one_shot_diff.py psov3/pso/network/TLobby_803FCF44 803FFB84
/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/llvm-nm -S build/GPOE8P/src/pso/network/TLobby_803FCF44.o | grep -i 803ffb84   # gate 0x5F0, INT-parse
python3 tools/report_delta.py cache/base_report_ffb84.json build/GPOE8P/report.json --check
python3 tools/check_pr.py
```
