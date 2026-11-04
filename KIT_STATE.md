# KIT_STATE — card-itemattackcol-ct (t_a5771ad5) — visit 1, Nov-3, m5u/f7

## State (committed tip e1eb8325, verify: rm .o + ninja unit + one_shot)
- `src/pso/item/TItemAttackCol.cpp`: Oct-28 seed 9d0317148 ct body transplanted surgical-insert
  between __dt and create (era address slot 0x802E40AC, gate 0x3A8=936B, 234/234 rows).
- Address-resolved rename: copy_vec3__11TBoss4Type2FPv -> set_direction__13TParticleCtrlFPv (2 sites;
  old name absent from current symbols.txt). FlagWord __ct/reset + copy_xyz survived as spelled (free fns,
  copy_xyz declared in pso/system/vector.h; era reloc copy_xyz__FPvPv = MWCC C++ mangle of it).
- `#pragma push / opt_propagation off / pop` function-window over ct: 88.38461 -> 88.666664, gate kept. KEEP.
- 12 siblings: 100.0 each (one_shot, unit psov3/pso/item/TItemAttackCol).

## Residual = 26 rows, ALL pure {r30 <-> r31} color swap (self/init callee-home inversion)
Era: mr r30,r3 (self) / mr r31,r5 (init). Ours: swapped. Slots/positions identical; only colors.

## Seed-survival datum
88.38 (Oct-28, base 5beecf0d8) -> 88.38461 EXACT on 5695627b. File untouched by merge waves -> score preserved
(the file-preservation clause of the transplant law, measured).

## INERT/REFUTED on this unit (do not re-roll)
1. decl-order swap (REC-decl-LAST on self) — byte-identical.
2. def-order flip (init first) — inert plain AND under prop-off.
3. init de-named (all uses cast inlined) — inert, gate kept.
4. self de-named (raw a0 casts, twin TPhotonRainbow form) — SIZE-KILL: bank grows to stmw r29, 0x3B0, 87.29.
5. const-qualified init local — inert.
6. comma-def (0,cast) at init birth seam — inert under prop-off.

## Twin intel (rosetta screen, offline probe_compile.sh grid at unit's exact flags)
- 339 matched ctors in corpus bind self->r30 with stmw r30 — era binding is the ctor-family norm, NOT a version pin.
- V1 = TForceOperate__ct verbatim skeleton (1-arg base call + named self + raw arg2) binds self->r30 ✓ era.
- V6 = V1 + named init local + init-deref stores -> flips to self->r31. V7 = V1 + 3-arg first call (raw init_)
  -> flips to self->r31. Both determinants reproduce the seed (bad) binding in MINIMAL bodies, while the FULL
  era object shows era binding WITH both ingredients present => def-binding rank is pressure-stratified;
  no decl/def/naming permutation in the full body reaches it (6 probes + 5 offline cells).
- Class: DEF-BINDING PROLOGUE PIN (edc20/ba38 lineage), 2-reg bank, census-at-5 complete.

## Next-visit openers (ONLY these)
A. Twin->seed statement-bisection on the scratch probe grid (escalate V1 body with seed statements one at a
   time, objdump head each step, find the exact statement that flips binding at full scale, transplant it).
   Zero repo builds for the search; confirm winner on real TU.
B. Maintainer ask: era ctor first-claimant binds LOW (r30) in 339 twins vs HIGH (r31) from our 2.6 -O4,p
   on this fn's ingredient mix — one pinned-unit allocator memo.
C. Do NOT re-roll items 1-6 above.

## Unit linkage state (13-fn unit)
12/13 byte-exact; ct 88.666664 blocks unit linkage (linked_units entry = integrator; check_pr not run —
unit unlinked, full battery reserved for 100.0 per brief).

python3.14: /Users/scott/.hermes/installs/60d8a79da6991a71/environments/28d86d1068e44adc8d1a5d2ca8c63c2c/venv/bin/python3.14
one_shot: <skill>/scripts/one_shot_diff.py psov3/pso/item/TItemAttackCol TItemAttackCol__ct
gate: /opt/homebrew/opt/binutils/bin/gnm -S build/GPOE8P/src/pso/item/TItemAttackCol.o | grep -w TItemAttackCol__ct
