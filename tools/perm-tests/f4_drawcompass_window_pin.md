# f4 draw_compass__13TRaderMapCoreFv (0x801FA6CC, gate 0x1B4=436) — visit report, card t_fb37fe85

## Measured state
- Baseline/inherited = final: 87.3211, size=436 gnm gate-exact, rows 109/109.
- Inherited 52-line draft body committed as 237e3c13 ("f4 recovered draft in-tree, 87.3211 measured")
  on card-f4-pool (base d82be2a8). Tree left clean at 237e3c13.
- ps-arith screen (mandatory, run FIRST): ZERO ps_ instructions in era .fn block -> not hard-wall class.

## Era decode (scratch/f4_era_block.s)
Frame 0x60, bank stmw r30 (r31=self, r30=mode->row ptr). Slots: color@0x8, state@0xc..0x2b,
magic-pair scratch 0x30/0x34, 0x38/0x3c, fctiwz pair 0x40/0x44, 0x48/0x4c, 0x50/0x54.
Arithmetic = MWCC s16->f32 magic: lis 0x4330 + stw hi + lha + xoris 0x8000 + bias lfd
(lbl_8044A7A8 = 2^52+2^15, owned by ANOTHER unit's .rodata) + fsubs/fadds single-consumer fold.
Shared CSE: r30 = lbl_804C87B4 + mode*16 row pointer (single `add r30, r4, r6`, used by both draws).

## Residual anatomy (18 rows)
1. slots 30-44 (13 rows): pure scheduler-window permutation; slots IDENTICAL, instruction multiset
   IDENTICAL. Era: stw-hoist (stw r3,0x30(r1) at window head), bias/tbl address chains sink toward
   uses, slwi dest r6. Ours: address chains hoist to window head, pair store sinks to use, slwi dest r5.
2. slots 66-68 (3 rows): arg2 swizzle. Era `srwi r5,r0,16; rlwimi r5,r0,16,0,7; rlwimi r5,r0,16,8,15`
   decodes to base (color>>16) + insertion(0,7)=color bits16..23 + insertion(8,15)=color bits24..31
   -- insertions are value-no-ops (terms == what base already holds). Era runtime arg = color>>16.
   Champ spelling `(color>>16)|((color&0xFF)<<16)|((color<<16)&0xFF000000)` fuses to
   `clrlslwi + rlwimi(16,31) + rlwimi(0,7)` -- provably DIFFERENT value (byte0<<16|byte1<<8|byte2).
3. slots 73/75 (2 rows): @490 vs lbl_8044A7A8 pool-name rendering (unlinked-view noise per skill).

## Probe table (builds: 7 grind + 1 confirm-family; 1 pre-spent by control probe)
| # | lever | result |
|---|-------|--------|
| 1 | inline lbl_804C87B4[mode] (drop named row ptr) | 112 rows +3W, remat cascade -- era NEEDS named CSE row ptr |
| 2 | (f32)(f64)(s32) explicit cast chain | byte-identical (folded) -- INERT |
| 3 | #pragma push/opt_propagation off function window | byte-identical -- INERT |
| 4 | (color>>16)\|((color&0xFF0000)>>16)\|((color&0xFF000000)>>16) | 107 rows -2W: MWCC 2.6 mask-combiner folds all terms to bare srwi |
| 5 | 4x named f64 locals + (f32)cast (layout hypothesis) | 112 rows +3W: emits frsp+fsub, breaks single-consumer fold -- era has NO named f64 locals |
| 6 | #pragma push/peephole off function window | 82.5963, 113 rows, +4W, bank rotate r30/r31 -- REGRESSION |
Confirm: champ state full `ninja` rc=0, unit gnm size 0x1b4 gate-exact, New exact 0, regressions 0 (functions), link_units OK.

## DATA CLAIM ASK (integrator config, NOT fixable in-lane)
Era unit .o .rodata = 8 bytes (2^52 only). Era draw_compass bias 2^52+2^15 (lbl_8044A7A8) lives in a
DIFFERENT unit's .rodata. Our draft emits 16 bytes (2^52 + 2^52+2^15) -> report_delta FAIL
"matched_data -8, data: psov3 .rodata 0x8044A7A0 +8 bytes" while functions stay 0-regressed.
splits.txt row 6954 `.rodata start:0x8044A7A0 end:0x8044A7A8` covers only lbl_8044A7A0.
check_pr.py FAIL is EXCLUSIVELY this claim gap (tools say: "section: claim the data range into the
unit's split"). Fix = config/GPOE8P data-definition lane (humanpso niche + config edits are child-forbidden).
Until claimed, the matched function cannot ship (byte-exact-only policy).

## Classification
13-row window = SCHED-WINDOW/def-binding PIN (multiset-identical permutation, survives every tested
ordering lever incl. prop-off byte-inert -- DEF-BINDING PROLOGUE PIN kin). 3-row swizzle = era
redundant-term insertion form; MWCC 2.6 combiner makes all unifiable spellings fold (-2W) and all
non-unifiable spellings value-shift -- spelling producing exactly srwi+rlwimi(0,7)+rlwimi(8,15) NOT found.
Floor: 87.3211. No-2nd-visit unless: era source for the swizzle operand (a MAP file settles it) or
a bind mechanism is found for the window.
