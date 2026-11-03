# Anatomy: TObjFish__sub_802E7D70 (fleet/f3, Nov 1) — PARKED 99.86842 @0x130 gate-exact

## Provenance
- NOT a cold virgin: f8 seed 86487a2d (99.47369, 7-row wall) transplanted into f3 file
  (src/pso/boss/Boss7DeRolLeCBehavior.cpp, inserted after twin 802E7CC4, before
  EffectNode_802E7EA0 — crawfish park + all parks untouched).
- BASE-VERIFY: kit harness reproduced official 7-row diff exactly (calibrated oracle).

## Row classes (76 words, frame 0x70, stmw r25@0x54)
- slots 0-14, 16, 18-29, 30-75: EXACT after store-swap breach.
- **Class B (slots 30,31,34,35,37) — BREACHED by STORE-SWAP**: emitting
  `block.sp8 = (u16)(f2c + rel);` BEFORE `block.spA = 1;` (swap of the two C statements;
  scheduler still places li r0,1 at slot 31) flips scratch homes to orig:
  lha r3/li r0/add r6/r6-store — all 5 rows. f8's falsified list never touched this pair.
  v08 sum-temp block achieves the same 2-row residual (equivalent winner, unchosen).
- **Class A (slots 15,17) — SCRATCH-HOME COALESCE WALL, floor**:
  orig `addi r30, r28, 0xb / extsh r30, r30` (unextended temp co-located with its
  sign-extended s16 class in the callee-saved home) vs MWCC-2.6 `addi r0 / extsh r30, r0`.
  Live ranges of temp and class do NOT overlap (temp dies at extsh, class born there)
  so r30 co-allocation is legal — but MWCC never chooses it at this profile.

## Exhaustiveness receipt (class A)
- f8's 5 falsified levers (s32 rel w/o-cast, CSE-inline, comma-def, reg-hint, s16 param).
- gridA: 4 rel-spellings x 120 decl-order perms = 480 states — all [15,17] (240) or 9-row worse (240, def-position).
- w-battery 8 + x-battery 3 typed/bool/guard/nest spellings — inert or worse.
- pragma family: trio/prop/csubs -> 75 words (opt_propagation drops `mr r28,r4` param
  spill — the f8 "entry mr rotation" death, re-confirmed at different scope);
  peephole -> 80w; dead-assign -> cascade 29 rows; combined-guard -> size fail.
- permuter r1: F4_FB358 size-preserving [weight_overrides] flat profile, base score 15
  (Register Diff 3, Del/Ins/Stack/Branch 0), 10,678 iters, 1500s cap, --better-only:
  ZERO output dirs = no state beats the champ. iters>0 receipt: run1.log.
- Kit: perm-tests/f3_TObjFish_802E7D70 (target.s/.o from dtk .fn block, base.c=champ
  pure-C mirror w/ TKtObj pad10[4] fix (m_down@0x14, m_next@0xc — 0x10 mis-mirror was
  caught by non-vacuous BASE-VERIFY), compile.sh=unit GC/2.6 -O4,s -sdata2 4 profile,
  gridA.py, score.py, rank1.py, round1.sh).

## Verdict
- 99.86842 / 0x130 gnm-EXACT (100% score = tiebreak-floor 2 register-role rows, 0.5 each).
- Family sibling: pool-read/addi-scratch class (mirror of 80117E50-style bank ties);
  source-unreachable-in-practice under GC/2.6 -O4,s across ~750 states + 10.7k perm iters.
- Naming: f8 evidence stands — placeholder kept per ros-87; proposal
  spawn_crawfish_child / TBoss7DeRolLeC__spawn_crawfish (0x7a4 group, +0x28/+0x2c s16 pair).
- Link eligibility: unit stays multi-park (crawfish 88.56, others) — no eligibility gain.
