# f7-2 disposition census — sub_8042CD64 — Nov-3 (close @ ~70min)

## Ladder (all committed, tree f7, branch card-modem-8042cd64)
- ba1d9730 inherited: 78.92079, OURS 420 (gate 0x194=404), 101/105 rows
- 2d165087 control probe receipt (clean rebuild confirms 78.92, +4)
- 57a2805d c3: early-mat hoist (cmd/state/flag/match first stmts) -> 86.98, 408
- a9a2f637 c4 datum: +u8*p cursor = 86.11 (+5) — cursor poisons slot packing
- 9c76d5b8 c5 datum: in-loop-only cmd = 85.64; loop-prep lis pair, stw/iter, bank6
- (c6) 86.11: dual cmd assign = double materialization (+5)
- bbe51d46 c6: pat=lbl_805D487C early stmt -> prologue li sda21 home = 89.58, 408
- 45c07b79 c7: pat birth after match = era head order -> 89.62
- 3e900619 c8: named v=value copy, single reload -> 92.39, GATE SIZE 404, 101 rows
- 2728682f c9: STRUCTURAL FIX nested re-pump (era tail b outer-head: pump never
  exits by drain; returns only via -6/K) -> 92.98 at gate
- 90d86160 TIP c10: in-loop cmd assign (home-bound pair post-stmw + per-iter
  stw) -> **96.38614**, OURS 404, rows 101/101, 32 diff rows

## Gates on committed tip (full ninja, rc=0)
report_delta --check: total_code +0, regressions 0, link_units OK,
check_pr: PASS (DOL byte-identical).

## Residual census (32 rows, zero multiset rows — colors/forms only)
1. HEAD BIRTH SWAP (rows 1,3,6,7): era binds cmd lis@r4-slot1 + home r30;
   binds pool lis@r3-slot3 + home r31. Ours: pool first (r4/r30), cmd second
   (r3/r31). Identical instruction multiset + frame roles — birth-order of the
   two prologue materializations. Era shape needs cmd born before state= with
   NO loop-prep remat: dual-assign (c6) = +2 remat rows in GC/1.2.5n;
   in-loop-only (c10) = pair lands @3/@6, birth transposed. = DEF-BINDING
   PROLOGUE PIN (qvm-edc20 kin), pre-declared wall.
2. SLOT-ALLOC PASS (rows 12,17,25,35,42,47,55 + epilogue frame rows):
   era = decl-order pass (cmd@0xc, value@0x10, inline frame 0x14/0x18/0x1a),
   1.2.5n = first-use pass (inline 0x10/0x12, value@0x14, cmd@0x18; frame
   0x38 vs era 0x40, bank stmw r26 vs r25 — cmd home r31 not r30 shifts the
   save-window base). Version-stratum, source-inert (probed c3/c4/c5/c6).
3. CALLEE-SAVE RING (rows 8,9,40,65..93): {match,flag,i} = r26,r27,r28 (era)
   vs r27,r28,r26 (ours); pool/cmd r31/r30 swap; v=r4 vs r3; count r29 MATCHES.
   Liveness-rotate beyond decl/statement permutations tried (8 grinds).
4. CMP FORM (rows 81,87): cmplwi r4,0x4f/0x4b (era, raw u8 slot load) vs
   cmpwi r3 (ours, v-copy operand) — sign-form tie to the v-binding.
5. ADDR FORM (rows 69,70): add r3,r31,r3; stb r4,0x14(r3) (era) vs
   addi r0,r4,0x14; stbx r3,r30,r0 (ours) — scheduler folding choice.

## Verdict
status=floor, 96.38614 at gate-exact size (404) and rows (101/101).
All 32 residual rows are color/slot-form census classes (def-binding pin
family + slot-alloc pass stratum). No multiset delta, no size delta.
Levers banked: early-mat hoist, pat-address early stmt (kills sda21 remat),
named v-copy (kills double lbz), in-loop assign (home+spill era shape),
nested re-pump structure (semantic fix — successor: verify callers of
sub_8042CD64 treat non-termination as era-true).
No transfers: LEVERS ARE PER-UNIT HYPOTHESES.
