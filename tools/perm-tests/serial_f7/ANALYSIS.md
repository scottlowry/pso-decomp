# f7 card-serialaccess — TAdEnterSerialAccessGC__sub_802C4B64 (0x802C4B64, 0x13C=316B=79w)

VERDICT: PARK at 99.620255 (75/79 real rows). Branch card-serialaccess @ ac9f5ff3, WIP commit banked.

## Ownership / size (brief correction)
- symbols.txt row 20270: `TAdEnterSerialAccessGC__sub_802C4B64 = .text:0x802C4B64; size:0x13C`
  → **316 B / 79 words**, NOT the 790 B / 198 words in the card brief.
- Owner unit (splits.txt, by range containment, not boundary): `pso/ui/TAdSelectGameModeGC_802C4748.cpp`
  (.text 0x802C4748–0x802C4CA0). This fn is the unit's LAST function and ends exactly on the
  split boundary (0x802C4B64+0x13C = 0x802C4CA0) → ownership/split already byte-correct, no config ask.
- Era class attribution (TAdEnterSerialAccessGC) differs from the unit's class (TAdSelectGameModeGC):
  link-order interleave, not an ownership error. Callee of render__19TAdPlyChrSelPlateGCFv (0x802C4CA0,
  the retired neighbor) — the plate-render kit's "serial-access plate painter" note is this function.

## Disasm decode (79 words, no switch table, no jumptable relocs)
State-machine NO — it is a straight-line draw-descriptor builder:
frame 0x60, `stmw r29,0x54` (3 callee homes: r29=arg0 plate, r30=arg2 colour src, r31=arg3 index),
col[16]@r1+0x8, desc{pos,col,a,n}@r1+0x18, pos[8]@r1+0x28, double-lo/hi spill @0x48/0x4c.
4x `bl copy4__18TAdChrMoveEffectGCFPv` (RGBA broadcast), plate deltas @0x21c/@0x220,
tail `bl draw_tri_fan_2d__14TObjCMHairMenuFllf(&desc, 4, 7, lbl_805DE544*(f32)arg3 + lbl_805DE540)`
via the 2^87 magic (lis r0,0x4330 / stw lo / lfd / fsubs / fmadds) — unsigned path, so arg3 MUST be u32.
Pool reads: 2 (lbl_805DE540/544 sda21 + lbl_80471A78 .data double). Referrers: the ChrSel plate
renderer + TAdEnterSerialAccessGC::draw_serial_plates path (per f3 evidence).

## Row-by-row wall table (79 slots; 6 printed, 4 real)
| slot | ORIG | OURS | class |
|---|---|---|---|
| 4  | `addi r8, r1, 0x8`   | `addi r9, r1, 0x8`   | REAL: &col address → scratch colour mirror |
| 5  | `addi r9, r1, 0x28`  | `addi r8, r1, 0x28`  | REAL: &pos address → scratch colour mirror |
| 14 | `stw r8, 0x1c(r1)`   | `stw r9, 0x1c(r1)`   | REAL: desc.col store (same mirror reg) |
| 15 | `stw r9, 0x18(r1)`   | `stw r8, 0x18(r1)`   | REAL: desc.pos store (same mirror reg) |
| 61 | `lis r3, lbl_80471A78@ha` | `lis r3, @96@ha` | DISPLAY-ONLY (pool name) |
| 64 | `lfd f2, lbl_80471A78@l(r3)` | `lfd f2, @96@l(r3)` | DISPLAY-ONLY (pool name) |
All other 73 slots byte+text exact. Pool rows proven non-blocking: twin
`sub_80348E34__18TAdChrMoveEffectGCFv` (pso/ui/TAdChrMoveEffectGC) scores **100.0** while
carrying 4 identical `@NNN` vs `lbl_...` rows.

## Ladder this visit (15 builds + 20-version survey; control first)
v0_ctl 99.620255 (harness calibrated = BASE-VERIFY) · v2 desc-first-decl 99.620255 INERT ·
v9 casts 99.620255 INERT · v11/v12/v6 ptr-temp decouple 99.620255 INERT (propagation folds) ·
v4 peephole on 99.620255 INERT · v3 p0/p1 flop 99.46835 (-2 lfs rows) · v13 (unassigned pp)
93.46835 · v20 col-before-temps 93.6076 · v24 imm-interleave 91.74683 · v22 desc-block-first
91.64557 · v26 coldecl+assignswap 95.49367 · v25 col-declared-first 99.417725 — frame
RE-LAYOUT (desc@0x8, 19 rows): decl order is pinned by the era's offsets, cannot be freed ·
v1_posfirst 95.68355 · v10_defdecouple 96.860756 **colors flip CORRECT (col→r8,pos→r9) but the
pos store leaves slot 15** · v5 peephole off 83.139244 **GATE_BAD 0x140**.

## Compiler-version screen (the new dead-end proof)
`survey/regmap.tsv`: 1.0/1.1/1.1p1/1.2.5/1.2.5n = COMPILE_FAIL (TU needs ≥1.3); 1.3, 1.3.2,
1.3.2r, 2.0, 2.0p1, 2.5, 2.6, 2.7 = size 0x13C and ALL emit `col→r9, pos→r8`;
3.0a3/3.0a3.2/.3/.4/3.0a3p1/3.0a5/3.0a5.2 = size 0x144 (gate fail), also mirror.
=> NOT a version wall. No config version proposal.

## Named class: ADDRCOLOR-TRIPLE-PIN (subclass of f3's INTEGER-GPR-MIRROR)
Three properties are jointly pinned and mutually exclusive in one 2.6 IR ordering:
(1) addi emission offset-ascending (0x8 then 0x28), (2) colour col→r8 / pos→r9,
(3) store emission col(0x1c) before pos(0x18). Every reachable spelling gives a 2-of-3;
v10 buys (2) at the cost of (1)+(3). Permuter NOT run: f3's 3 rounds (≈78k iters) harvested
zero above-champ size-gate-passing candidate; budget spent on the version screen instead.

## Gates
ninja full rc=0 (DOL linked; Runtime 100.00% matched) · gnm OURS 0x13C = symbols size ·
unit 76.90058 → 99.91228 · 7/7 siblings 100.0 (no regression) · report_delta regressions: 0 ·
check_pr PASS, link_units check OK (3357 exact), regressed(drop) 0.

## Integrator notes (report-only, no config touched)
- linked_units/completed row for psov3/pso/ui/TAdSelectGameModeGC_802C4748 stays open until the
  4 mirror rows land; do NOT mark complete.
- The anonymous `.data` double at 0x80471A78 (`@96`) will want a `.data` claim when the unit
  completes; it does not affect the score (twin precedent above).
