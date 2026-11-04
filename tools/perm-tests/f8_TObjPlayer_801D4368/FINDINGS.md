# TObjPlayer__sub_801D4368 — recovered-campaign ladder (fleet/f8, Nov 1)

Unit psov3/pso/unk/text_801D40D4 · file src/pso/unk/text_801D40D4.cpp · orig 0x248 / 146 insns
Flags (from build.ninja, unit-true): GC/2.6 `-O4,s -inline off -char signed -use_lmw_stmw on -sdata2 4 -lang=c++`

## Ladder (all official one_shot_diff; repo builds = 7 of cap 10, 1 fail = void*->u8* implicit)
| step | spelling | % | rows | commit |
|---|---|---|---|---|
| seed a6d10ea5 | era tip as-is | 98.83562 | 28 | dc427b67 |
| fix | extern-fiction `alloc__23TAdSinglePlyChrSelectGCFv` -> `__nw__FUl` (0x8007EB94; never existed in symbols.txt even at era base) | 98.869865 | 27 | 585fe222 |
| r1 | perm output-50-1: down_4 hoist to pos5 + down_3 before down_2 + p3 def-swap (down_3 before rec_2) | 99.65753 | 8 | 24b37b97 |
| r2 | perm output-30-1: rec_3 decl hoist to pos9 (p4 rec bank r26->r29) | 99.79452 | 5 | 2b2025d3 |
| r3 | perm output-20-1: cnt_2->pos2 + down->pos11 INTERACTION | 99.863014 | 3 | (this) |
| r4 | perm output-0-1: cnt/rec swap (cnt after rec) | **100.0** | 0 | Match |

Era label "98.87" = post-rename truth; seed itself measured 98.83562. Era "28 word-diff" ≈ 28 diff rows.

## Verify-first datums (mandate: record seed's TRUE size AND score)
- Seed gnm OURS 0x248 EXACT at a6d10ea5 state; score 98.83562 (era mislabeled 98.87 — that's the post-fix number).
- Callee audit: ALL externs pre-existing in master symbols.txt except alloc__23... (fiction, caught by screen; seed
  would have failed link battery). orig-vs-ours bl multiset IDENTICAL (18 relocs) once renamed.

## Row anatomy (all residuals were PURE GPR renumber — triage real=0 at every step)
- p1-p3 list cursors wanted ONE shared color r27 (reverse-decl rule: later-declared pointer locals color LOWER).
- p4 rec cursor r29 = freed cnt_2 home; p1 counter r28 vs r29 tie = last, cracked by cnt/rec decl swap.
- Walker MERGE (shared variable) is BAD here (98.70) — separate dead-range locals + decl order is the mechanism.
  (Contrast TLobby_8002058C where shared walker was REQUIRED — the merge lever is card-specific.)
- Decl-position probes that FAILED at 5-row state (20-spelling grid): every single-var move of down, comma-def
  variants, def-swaps, merges; permuter found the cnt/rec swap in 69 iterations from champ seed. Interaction space
  >> single moves: 3 of 4 breach levers were multi-decl interactions.

## Kit (this dir)
- target.o = dtk orig per-unit obj SLICED to single fn via as from dtk .fn block (full-unit obj gave 349 phantom
  deletions — func_name setting trims the CANDIDATE side only, not the target dump).
- base.c pure-C mirror (method calls lowered to mangled externs, s32/u32=long typedeffed verbatim):
  BASE-VERIFY 146/146 words byte-identical to repo .o at every re-root — C++->C lowering is codegen-neutral here.
- orank.py / harvest_rank.py: official-% oracle calibrated EXACT (98.869865, 99.65753, 99.79452, 99.863014 all
  reproduced by kit raw objdiff before repo build).
- 37-family flat [weight_overrides]: decl100/stmts60/temp30/refer20/remove_ast20/commutative15, ALL size-risky +
  variable-identity families (esp. perm_remove_var — r9 trap) = 0.
- Semantic-fidelity: every harvest gated on size 0x248 + callee-multiset identity vs champ + winner-row hand review.
- Rounds: r1 88970 / r2 89376 / r3 89353 / r4 69 (stop-on-zero) iterations; iters>0 receipts in run*.log.
