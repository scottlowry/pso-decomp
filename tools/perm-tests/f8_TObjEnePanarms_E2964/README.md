# f8 lane kit — TObjEnePanarms__sub_800E2964 (1152B cold target)

VERDICT: INCONCLUSIVE — anatomy solved, schedule not. No commit (no gate-exact body).

## Anatomy (PROVEN, decode in e2964_decode.py / e2964_body.txt)
- Pure straight-line block copy, NO calls/branches/loops: 102 dwords
  0x800E2964: dst = TObjEnePanarms__state_fn_table[0..101] (0x8049575C..0x804958F0,
  src = last 0x198 bytes of lbl_80495524 (0x804955C4..0x80495758) = lbl_80495524 + 0xA0.
  Uniform +0x198 shift, verified 102/102. table symbol size 0x1C0: LAST 5 Ent entries NOT copied.
- Referrer: the unit's ONLY .ctors entry is this fn (startup static-init, NOT class __ct;
  sibling unit's .ctors fn 0x800DF748 has IDENTICAL tempo shape, also unpaired).
- Prologue/epilogue: stwu -0xf0, stmw r14,0xa8 / lmw, addi 0xf0, blr.
  Window bases: r16 = &lbl_80495458 (lis+addi), r20 = r16+0x304.
- Op budget = 288: 102 global-lwz + 102 global-stw + 38 stw-to-slot + 38 lwz-from-slot
  (slots 0x8..0x9C(r1), each used once) + 2 mr (3480, 3608 — value feeds BOTH a slot
  spill and a dst store) + 8 frame/return.
- Program order (dword idx): A{24,26..43 slot-tempo; 25,44 singles-late} B{0..23 GPR batch},
  C{69,71..88 tempo; 70 late} D{45..68 GPR batch} E{89..101 plain pairs}. Store order != load order.

## Oracle (armed, BASE-VERIFY PASSED byte-identical)
- e2964_cc.txt = verbatim ninja -t commands line (wibo mwcceppc 2.6, -O4,s, -use_lmw_stmw on).
- e2964_probe.sh <cand.cpp> [lo hi]: cp cand -> real TU path, compile IN PLACE (path string
  is embedded in .o; scratch-path compiles NEVER byte-match — cost me a debug cycle),
  restore via git show HEAD>, probe_diff vs build/GPOE8P/asm/pso/enemy/TObjEnePanarms.s, gnm -S.
- Unit is LINKED (only 69 matched fns); the 1152B gap + .ctors entry currently resolve via
  rule-less origin extraction — check how link fills it BEFORE committing any wrong-size body
  (wrong-size body + gap-fill = dup/overflow = red tree). THIS is why nothing was committed.

## Candidates scored (builds 7/8 of cap used incl base)
v1 struct-copy `*(S*)(b+0x304)=*(S*)(b+0x16C)` (S=51*{s32,s32}) -> bl libcall, 0x30. RULES OUT
   struct-assignment: MWCC 2.6 -O4,s libcalls copies >= ~0x40; the 288W inline MUST be
   source-level field/array copies. DEAD END, do not retry.
v2 102 pairs in store order, (s32*)(lbl_80495458+0x304) -> 0x4B4 (301w), single r16 base,
   no r20; stores stw r?,disp(r16); 285 rows mismatch.
v3a grouped loads+stores via local s32 v[45] array -> 0x55C WORST (array forced stack).
v3b literal transcription: fresh temp per load, stmts in EXACT op order (102 t) ->
   gnm 0x4A4 = 297w CLOSEST. Prologue lis+addi r3 (no r16/r20), 44 spill pairs (vs 38+2mr).
v4 transcription with 38 real slot temps as tmp[40] local array + b/s/d -> 0x4AC (299w);
   tmp landed 0xCC(r10) region, wrong placement, 285 rows.
v5 = v2 with b variable + pairs store-order -> 0x4B4 identical to v2 (b CSE'd away).

## Ladder for next session (cheapest-first)
1. Diff v3b schedule vs orig (objdump .o is gone; regenerate): +9w = 3 extra spill pairs
   + missing r16/r20 addi pair + mr-vs-lwz at 2 spots. Kill exactly 6 pairs: shrink live-set
   by reordering the 21-word A/C tempo statements to store-ASAP (values live only 1 stmt),
   keep B/D batch as 24 pair-statements back-to-back; expect MWCC to batch them under the
   scheduler pool (as original). Target 288.
2. If size lands, chase rows via rosetta_screen only for order-residuals (E2964 has no
   hoist candidate: no loads above frame saves except the pool pattern).
3. Permuter (references/permuter.md) over statement order WITHIN superblocks (A/B swap inside
   half is fixed by store order; the 2 singles 25/44, 70 and mr-dup positions are the free vars).
4. Compare with sibling 0x800DF748 (238W, same family, also cold) — ONE source pattern should
   match BOTH schedules; solving either template solves both. 0x800DF748 is SMALLER —
   maybe better permuter target to crack the family spelling first.
5. Naming: report-only. sub_800E2964 is a .ctors static-init; evidence supports
   "install_state_fn_table"-style naming; extern lbl_80495458[] (u8[]) used for anchor is fine
   but DATA CLAIMS are integrator-owned (AGENTS: stay out of splits.txt defines).

## Files
- e2964_cc.txt, e2964_probe.sh — oracle command + in-place probe driver
- e2964_body.txt (288 raw insn lines), e2964_decode.py (permutation verifier: asserts 102x+0x198)
- e2964_gen3.py / e2964_gen4.py — transcription generators (v3b/v4); cand_e2964_v1..v5.cpp
- All in: tools/perm-tests/f8_TObjEnePanarms_E2964/ (copied here from scratch 2026-11-02 f8 lane)
