# draw_compass__13TRaderMapCoreFv — visit-3 state (fleet/f3, Oct 31)

CARD: 99.633026 / 436 @ HEAD 00bda022. Residual = 2 REAL rows (slots 40/44:
`slwi r5,r30,4 / add r30,r4,r5` vs orig `r6,r6` — scratch-home tiebreak of the
mode*16 index inside the hoisted color-conversion cluster) + 5 display rows
(beq@9 branch-shift, @480-vs-lbl_8044A7A8 pool naming @32/33/73/75, zero perm
cost, never chase).

## THE VISIT-2 BUG (root cause of the void claim) — FIXED + CONFIRMED
visit-2's perm/settings.toml put weights under `[mwcc]`; this fork reads ONLY a
flat `[weight_overrides]` dict (decomp-permuter src/main.py:334). All visit-2
"tuned size-preserving" rounds silently ran DEFAULT mwcc weights (temp_for_expr=100
etc.) => the 2-row 'saturation' claim was UNPROVEN.
settings.toml now carries the real profile (reorder 60/60, temp_for_expr 30,
refer_to_var 20, remove_ast 15, commutative 15, add_self_assign 20; ALL
size-risky + noise passes zeroed; ins_block/var_cond_block at defaults).
VERIFY: `--debug --show-errors` base score = 10 (2x PENALTY_REGALLOC=5;
Stack/Branch/Reorder/Insert/Delete = 0 — the 2 mirror rows are the ENTIRE
objective; pool rows cost 0 = display-only confirmed).
BASE-VERIFY re-passed non-vacuously: kit base.c 109/109 insns, 0 word-diff vs
repo .o; probe_score calibrated EXACT 99.633026/436.

## Manual probe results (this visit, ALL offline via kit compile.sh, 0 repo builds)
REFUTED — fold byte-identical to champ ({r5,r5} home kept):
- fillers x8: unk18/self, new_var, color, mode, m_174 before+after, a, b,
  sandwich(new_var+color) — the m_19c-winner family does NOT transfer to a SECOND
  instance at the slwi/add def seam (same verdict class as Serial: no live GPR
  consumer between pool-addi and slwi to force r6).
- comma-def x3 (D80 idiom `(0, lbl_804C87B4)[mode]`, `(0, ...)`, idx-commas) — fold.
- named idx temp `mi`, split decl/defer-def — fold.
DISTINCT (regressed states, used as round seeds):
- q15 useflip (tbl[3]/tbl[2] consumer swap): 99.39449, 436B, home {r5,r5}, 13 slots —
  ONLY size-preserving distinct neighbor; no r6.
- q16 m_19c-above-def: 87.2 (115 rows). q09/q10 def-above-bl: 55.5/55.1 (132 rows).
  q11 def-before-rot0: 54.4 (133 rows). q14 inline reindex: 448B SIZE KILL.
=> ~46 cumulative source spellings (v2 ~25 + v3 21) never produce home {r6}.

## Rounds (FINAL — all fixed-profile, --stack-diffs, --better-only, -j4, 1500s cap,
## separate seed dirs per rotation state, iterations>0 verified, velocity 6-13/s)
- r1 champ seed: 31,095 iters — ZERO harvests. Champ basin saturated under the TRUE
  size-preserving neighborhood (the void visit-2 claim, now PROVEN).
- r2 q15 seed (score 10-basin, 99.39 state): 31,040 iters — 9 harvests: 6x score-10
  (= champ re-derivations, objdiff 99.633026), 18/18/28 = 99.615/99.615/99.523.
  Basin bottoms AT champ.
- r3 q16 seed (87.2 state): 19,732 iters — 34 harvests, descends 792->...->40/45->10.
  Bottom = champ (6x score-10), zero <10.
- r4 q09 seed (55.5 remat state): 19,663 iters — 51 harvests, bottom = champ
  (5x score-10), zero <10.
- Total 101,530 iters over ALL FOUR rotation states.
- Final comprehensive re-rank (rank_all_v3.py): 108 dirs (4 basins + visit-1/2
  r1-output-* archives) -> 94 size(0x1B4)+symtab-gate PASS, ZERO above 99.633026.
  (Pool rows: `@480` symbols match=None by design; data-gate carve ask unchanged
  and pending: extend unit .rodata to 0x8044A7B0 for pool slot 0x8044A7A8.)

## POST-MORTEM: fixed profile vs default (fleet datum)
The corrected [weight_overrides] profile CHANGED THE SEARCH (deep seeds produced
ladder intermediates 18/28/40/45/70/190 that visit-2's default-weight rounds never
mapped; zeroed noise families kept every harvest size-pure — 94/108 passed the gate)
but did NOT change the reachable optimum: every basin bottoms at the same 2-row
wall. The voided-weights correction CONFIRMS rather than overturns visit-2's
saturation verdict.

## VERDICT: HOLD 00bda022, tree UNCHANGED — card RETIRES (mirror-class v2)
r5<->r6 scratch-home tiebreak is invariant to ~46 manual spellings AND to
rotation-state-seeded real-tuned permuter rounds over every reachable state
(all basins bottom at champ). objdiff final read: draw_compass match=99.633026
size=436; siblings unchanged (unit sweep verified from disk); even at 100.0 the
f64 pool slot 0x8044A7A8 sits outside the .rodata split => carve ask stays
pending; this tree is carve-ready.

## Files (kit, untracked/banked): perm/settings.toml (FIXED profile),
gen_probes_v3.py + run_probes_v3.py + q*.c/q*.o (21 probes), setup_v3_rounds.sh,
run_round_v3.sh, perm_s15/s16/s09 seed dirs (base.c=state, run_v3_r[2-4].log),
rank_all_v3.py + rank_all_v3.out (final sweep), perm/run_v3_r1.log,
visit-1/2 harvests archived r1-output-* (re-ranked in final sweep).
