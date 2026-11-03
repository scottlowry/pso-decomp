# RELBASE family memo — TLobby__sub_803CB858 visit-2 (fleet/f7, Nov 2)

## Verdict on salvaged co-def move (9c77e5ce, was UNVERIFIED)
- MEASURED: .o rebuild (ninja MWCC edge, RC=0) -> gnm -S `TLobby__sub_803CB858` = **0x1CC** vs gate **0x1C0**.
  Gate NOT reached: 115 insns vs era 112 (+3). Pre-move was 116 (.o 0x1D0, v1/v6 world).
- Report (paired by name, post-link view pairs size=448): fuzzy **92.97321%** — new family best
  (visit-1 v6 champ 85.768, +7.2 rows banked at HEAD).
- RELBASE WALL IS BROKEN AT REPO TERRAIN: era two-stage stack tops reproduce RELOC-FREE —
  `addi r6,r31,0x4930 / addi r6,r6,0x1000`, `addi r6,r31,0x2930 / +0x2000`, `addi r6,r31,0x930 / +0x2000`
  (objdump: no R_PPC on these rows) and thread-handle diffs fuse (`addi r3,r30,0x620`, `addi r3,r30,0x310`).
  Proof condition: the 6 adxm_* defs sit mid-file above first use, AND `include/pso/system/AdxmThreadStorage.h`
  extern-declares them at cpp line 5 (seen first) — preceding externs do NOT veto the diff-fold.
  probeK transfer CONFIRMED (was per-unit hypothesis).

## ROWS STANDING BETWEEN (exactly +3, all pool-dup cascade)
Era uses r31 as anchor AND pool; param copy = r30; frame 0x10; bank {r30,r31}.
Ours (slot numbers from probe_diff, tools/perm-tests/relbase_f7/diff_salvaged.txt):
  1. slot 8  `addi r30,r31,0`   — `u8 *pool = (u8*)&adxm_worker_thread;` materializes as its OWN home r30
  2. slot 9  `stw r29,20(r1)`   — param demoted `mr r29,r3`, third callee-save, frame 0x20
  3. slot112 `lwz r29,20(r1)`   — its restore
Cascade (word-diff only, size-neutral): every thread-arg row rides r30 vs era r31; era's two
`addi r3,r31,0x0` (worker-thread arg, OSResumeThread arg) render `mr r3,r30` here — zero-diff
spelling policy rides the dup. 98 "real" probe_diff rows = mostly this recolor shift.

## NEXT-VISIT LEVER (NOT executed — park rule on gate-miss; levers are per-unit hypotheses)
Fold the pool local into the anchor: drop `u8 *pool`, spell `(u8*)&adxm_worker_thread + <off>` at the
3 stack-top sites and `&adxm_worker_thread` at the handle sites; relbase now fuses plain-disp, so the
anchor r31 should serve pool duties directly -> bank {r30=param,r31} -> 0x1C0 candidate. If MWCC still
dups, zero-diff addi-vs-mr rows become the named residue.

## Gates (current HEAD + rebuilt .o)
- full ninja RC=0; report_delta --check RC=0, regressions: 0; check_pr PASS (linked 3540, exact 3540,
  add-candidates 2 = other lanes, blocked json exempt).
- builds used this visit: 2/5 (unit .o forced-rebuild, full tree). No src change (HEAD 9c77e5ce verified as-is).
- Siblings in unit: 105/112 fns exact (was 103+ at v6? not re-attributed; regressions 0 authoritative);
  6 zero-scored unpaired rows carried from visit-1 (803C5ED4, 803C61C4, adx_encode_available_blocks,
  803C7DF0, fn_803C8020, 803CA8B4) — unchanged.
- rosetta clean from visit-1 (const-volatile zero-store on lbl_805E0D78 holds; no UB screen needed — no new code).

# VISIT-3 RECEIPT (t_885f3180, Nov 2) — pool-drop lever MEASURED, gate MISS, parked

## What the lever did
Dropped `u8 *pool`; spelled `(u8*)&adxm_worker_thread + <off>` / `&adxm_worker_thread` inline at all 5 pool
sites (3 create arg1s + 2 resumes); stack-top array lines untouched (already era-exact reloc-free two-stage).
- BANK COLLAPSE CONFIRMED, as predicted: frame 0x20->0x10; `mr r30,r3` param copy; saves {r30,r31}; prologue
  `lis r5,@ha` + `addi r31,r5,@l` and epilogue (lwz r31,0xc / lwz r30,0x8 / lwz r0,0x14 / mtlr / addi r1,0x10)
  row-exact vs era. Colors r5/r31 matched era here (control had r4).
- BUT +3 PERSISTS, relocated into the body: MWCC 2.6 CSE-rematerializes `&adxm_worker_thread` per use-block as
  zero-disp `addi rX,r31,0x0` and rides the constant in-place, instead of era's single fused-disp addi:
    busy   ours: addi r3,r31,0 + addi r3,r3,0x620 (2) vs era addi r3,r31,0x620 (1)   [+1]
    vblank ours: addi r30,r31,0 + addi r30,r30,0x310 + mr r3,r30 (3) vs era addi r3,r31,0x310 (1)   [+2]
    resume-vblank reuses live r30 -> `mr r3,r30` (count-neutral vs era's 2nd fused remat, color/spelling row)
    worker + resume-worker: `addi r3,r31,0x0` x2 EXACT vs era (2 rows banked by the lever).
  Size stayed 0x1CC = 115 insns. Row: post-link fuzzy 92.82143 (= champ 92.97321 - 0.15178);
  unlinked one_shot 91.35714 (vs control 91.99107). Siblings regressions 0 (report_delta --check RC=0).

## FAMILY LAW datum #2 (supersedes recipe step-2 wording)
"(2) never alias-break with a local" is NOT sufficient. Two spellings of the same relbase function are BOTH
+pinned at +3 from opposite polarities: pool-local -> fused handles `addi rD,rPOOL,K` (era shape, wrong bank)
+ dup + frame; inline expr -> era bank but CSE-remat chain (wrong body). Era requires FUSED-DISP handles off
r31 (`addi r3,r31,0x620`/`0x310`) with frame 0x10 and zero-disp remat only at pure &sym sites — a third
attractor neither spelling reached. Remaining size rows are the anchor-CSE-remat class, not the dup class.

## NEXT-VISIT LEVERS (per-unit hypotheses, unexecuted — do NOT transfer)
- The addi-vs-mr named wall PARTIALLY ARRIVED as predicted (mr r3,r30 x2) but is NOT the size gate; the zero-diff
  rows sit at the +0x620/+0x310 sites, not the 0x0 sites (which match).
- Untested window: `#pragma opt_common_subs off` scoped to the create-block (trio inert vs the POOL-fold in
  v2 probes — anchor-CSE-remat is a different policy, no census). Cheap unit-.o probe only; if remat chain
  survives, retire relbase 803CB858 as compiler-policy floor at 0x1CC and name the class.
- Kit: v3_control/lever_oneshot.txt (rows), v3_*build/full logs, v3_delta*.txt, v3_checkpr_final.txt. 4/5 builds
  used. Tree reverted to HEAD champion (pool-local, 92.973); ninja + delta + check_pr re-verified PASS post-revert.

# VISIT-4 RECEIPT (t_60a221a6, Nov 2) — opt_common_subs window shot: INERT at both placements — CLASS CLOSED at 92.973

## Control probe (champ re-anchored, 28318892 source state at HEAD bd32a228)
- rm stale .o + forced unit ninja RC=0; gnm TLobby__sub_803CB858 = 0x1CC; rebuilt .o sha1
  4cb9b9de... == prior on-disk champ .o (determinism echo). report.json row fuzzy 92.97321
  (paired size 448); unlinked one_shot 91.99107 / rows 112-115 — byte-identical to
  v3_control_oneshot.txt. (one_shot unit id: "psov3/pso/system/AdxStreamRuntime" — no .cpp suffix.)

## The shot: #pragma push + #pragma opt_common_subs off windowed over the create-threads region
- P1 (card-literal): interior statement-extent window, first OSCreateThread..last OSResumeThread
  (lines 2728-2746 champ numbering). Build RC=0 -> .o BYTE-IDENTICAL to champ (cmp), gnm 0x1CC.
  => MWCC does not apply the opt_common_subs state at intra-function granularity (or it is a
  no-op there); window reached nothing.
- P2 (widest distinct scope): push before the function, pop after its closing brace (house
  function-window pattern). Build RC=0 -> .o BYTE-IDENTICAL again, gnm 0x1CC.
  => Function-scope opt_common_subs off produces ZERO codegen delta for this unit — the knob
  does not govern the anchor-CSE remat class (nor the pool-dup class) on MWCC GC/2.6 -O4,p.
- P3 not run: P1 (model: statement-textual scope) and P2 (model: function-entry scope) are the
  two semantics models and cover the full extent lattice (interior-create-block ... whole
  function); any third extent lies between two proven-inert bounds and cannot add information.
  Build cap 3 consumed (control + P1 + P2); no full-tree build used.

## 3-ATTRACTOR TAXONOMY (terminal — every predicted attractor measured)
A. CO-DEF WALL (visits 0-1; extern visibility): adxm_* externs split from defs (AdxmThreadStorage.h)
   -> per-symbol @ha/@l pairs, front-end folds pool+C1+C2 to ONE addi; file-top push/opt_common_subs/
   opt_propagation/opt_dead_assignments trio inert vs the fold. .o 0x1D0 (116), row 85.768 best.
   BROKEN by co-definition move (defs above first use, same object): plain-DIFF siblings reproduce
   reloc-free (probeK transfer confirmed v2).
B. BANK-COLLAPSE SEESAW (visit-2 champ, 28318892): pool-local spelling — era-fused handles
   `addi rD,r30,K` BUT pool materializes a third home (+3 = addi r30,r31,0 ; stw r29,0x20(r1) ;
   lwz r29,0x20(r1)), frame 0x20, bank {r29,r30,r31}. 0x1CC, row 92.97321 = FAMILY BEST.
C. REMAT FLOOR (visit-3 pool-drop): inline spelling — era bank {r30,r31} + frame 0x10, prologue/
   epilogue row-exact, BUT CSE-remat of &adxm_worker_thread per use-block: busy addi r3,r31,0 +
   addi r3,r3,0x620 (+1), vblank +mr chain (+2). 0x1CC, row 92.82143 (< champ — color-cascade cost).
Era shape = a FOURTH attractor no repo spelling reaches: fused-disp handles off the ANCHOR r31
(addi r3,r31,0x620/0x310) + era bank {r30=param,r31} + frame 0x10 + zero-disp addi only at pure
&sym sites. B holds the fused form with the wrong bank; C holds the right bank without the fused
form. Opposite polarities, both +3-pinned; the third attractor is an era allocator/policy artifact,
not a source extent.

## NAMED WALLS STANDING (class-closure inventory)
1. CSE-REMAT WALL: anchor-CSE rematerialization survives opt_common_subs off at every scope the
   compiler honors (visit-4 P1+P2 byte-identical) and the full trio survives the pool-fold (v1).
   No in-repo pragma governs it. Compiler-policy floor: 0x1CC.
2. ADDI-VS-MR ZERO-DIFF WALL: era `addi r3,r31,0x0` (worker arg, resume arg) render `mr r3,r30` in
   B and the vblank-resume `mr r3,r30` rows in C; zero-diff (size-neutral) spelling/recolor rows —
   NOT raisable, named, honest.
3. addi-vs-mr residue at the +0x620/+0x310 sites is color-only in both B and C (rides r30 vs era
   r31); per protocol, color-only residue = not raisable.

## WHY RETIRE: all three predicted attractors (A co-def, B dup-bank, C remat) mapped with receipts;
±3 gate rows exhausted across 4 visits (v1 file-top trio, v2 co-def, v3 pool-drop, v4 pragma-window
x2 placements); the only remaining delta is an era-object-layout question (Nintendo's own .o was 112
insns — see b4f1fdd1 WIP anatomy), i.e. an ASK, not a lever. RELBASE class TLobby__sub_803CB858
CLOSES HONEST AT 92.973 (champ 28318892 kept; tree at HEAD, .o champ-bytes 4cb9b9de; kit logs
v4_control_build.log, v4_control_oneshot.txt, v4_p1_build.log, v4_p1_oneshot.txt, v4_p2_build.log,
v4_champ.o). No push. No config touched.
