# dispatch_chunk_polygon_list — 772B (0x304, 193 insn) — PLAIN-C, staged attack, visit 1

WIP state landed: **99.404 % objdiff, 776/772 bytes (+1 insn), 2 reg-color rows**.
Not a match: size gate fails (gnm `T 0x308` vs gate `0x304`).

## Triage (C, not asm)
193 orig words, ZERO `ps*`/`f*` ops (grep of orig_fn.s: FP-ish opcode list = `[]`).
Pure integer display-list walker + sibling calls → plain-C route, per brief's
"don't pre-assume asm". No fp_contract, no asm-class survey needed.

## Semantics recovered (all names from symbols.txt; no inventions)
`dispatch_chunk_polygon_list(s16 *list, s32 buffer)` = resumable polygon
display-list interpreter. Loop: `cmd = *list++` (lha, signed cursor), terminate on
`0xFF`. `op = cmd & 0xFF` (low byte), sub-operand = `(cmd >> 8) & 0xFF` (high byte).
* op 1 → `set_chunk_blend(cmd)`
* op 4 → save: `chunk_polygon_list_cache[slot] = list; lbl_805D7798++; return`
* op 5 → resume: recurse on the cached cursor with the same buffer, `lbl_805D7798--`
* op 0,2,3,6,7 → nop; 8..15 → `apply_chunk_texture_command(cmd, *list); list++`
* 16..63 → `n=*list++; set_chunk_blend(cmd); submit_chunk_material_color(cmd,list); list+=n`
* ≥0x40 → `count=*list` (u16), `info=list[1]` (s16), `list+=2`;
  if `model_render_flags & 0x800` (bit 11 — NOT 0x80000, see LADDER):
  `cmd = (s16)(cmd & chunk_polygon_flags_and_mask); cmd = (s16)(cmd | chunk_polygon_flags_or_mask);`
  then `cmd = (s16)(cmd >> 8)`;
  `changed = cmd ^ chunk_previous_strip_flags; changed |= chunk_strip_dirty_flags;`
  `chunk_previous_strip_flags = cmd; chunk_strip_dirty_flags = 0;`
  `if (changed & 1) set_strip_lighting_chan_ctrl(cmd);`
  then switch(op): 0x40 = `set_chunk_blend_depth_mode(cmd,1|0)` +
  (bit `cmd & 0x40`: `setup_chunk_tev_stages` + `GXSetTexCoordGen2(0,0,1,0x2A,0,0x7D)` +
  `draw_strip_pos_normal`, else `setup_tev_passclr` + `draw_strip_list_pos_nrm`);
  0x41/0x42 = `set_chunk_blend_depth_mode(cmd,1)` + (bit6: tev+`GXSetTexCoordGen2(0,0,1,0x2A,…)`+
  `draw_triangle_strips`; else `chunk_has_vertex_colors` → color-tex vs textured strips, both with
  `GXSetTexCoordGen2(0,1,4,0x3C,0,0x7D)`, 4th arg = `op == 0x42`);
  default (≥0x43) → nothing; tail `list += count - 1`.
Frame: `stwu r1,-0x20(r1)` + `addi r11,r1,0x20` + `bl _savegpr_26` = 6 callee regs
{r26 cmd, r27 list, r28 buffer, r29 op|n, r30 info, r31 count}.

## Winning spelling (every lever below required; #pragma push region: scheduling off + use_lmw_stmw off)
1. `#pragma use_lmw_stmw off` — the ONLY way to get `_savegpr_26` instead of
   `stmw r25,0x14(r1)`; 3 sibling fns in this file use it (house lever).
2. **Exactly 6** long-lived values, with cmd in place: color-arm count REUSES `op`
   (`op = *list++; … list += op;`) and the decl order is `cmd, count, info, op,
   slot, changed, t` (reverse-decl: op declared after count/info → op→r29,
   info→r30, count→r31 = era bank). A 7th home (e.g. a separate `n`, or a 7th SSA
   copy) flips the bank to r25-31 + frame 0x30 + `stmw`.
3. `cmd` typed **s32** with explicit `(s16)` casts on the three mutating assignments
   (s16 cmd emits an extra `extsh` promote copy at the if-join: 7 rows vs era 6).
4. Info read via a temp: `t = list[1]; list += 2; info = t;` reproduces the era's
   `lha r0,2(r27) … mr r30,r0` pair (a direct `info = list[1]` gives 1 insn, missing row).
5. Two-statement `changed = cmd ^ prev; changed = changed | dirty;` reproduces the
   era's load order (prev→xor→dirty→or); the single-expression form sinks the dirty load.
6. `u32 changed` (era compares with `cmplwi`, not `cmpwi`).
7. `submit_chunk_material_color__FUcPs(s32, s16*)` spelled as a literal-mangled
   extern-C name (house precedent) — the header's `u8` first param forced
   `clrlwi r3,r26,24` before the call (era passes the word raw).
8. `draw_chunk_color_tex_strips(s16*, void*, u32, bool)` — bool 4th param removes the
   caller-side bool→int clamp for the `op == 0x42` arg (see WALL below).

## Remaining wall (2 items, for visit 2 / integrator)
(W1) +1 insn: `draw_chunk_textured_strips` (defined IN THIS TU, 0x803E352C) has its
repo 4th param `s32 large`; MWCC GC/2.6 then always emits
`srwi r0,r0,5 ; clrlwi r6,r0,24` for a bool→int argument. Proved with a standalone
probe (mini3.cpp, 20 spellings: `+0`,`|0`,`^0`,`*1`,`-0`,`&1`,`(int)`,unsigned operand,
int operand, commuted `2==a`, via an int local, `!()`, `<<0`, enum cast, `?:`) — EVERY
`==`-to-int-arg form clamps; only a NARROW (bool/u8) declared param avoids it.
Declaring the callee `bool` fixes the caller but changes the callee's own body
(`large ? 0xC : 8` → `clrlwi r0,r26,24; cmplwi r0,0` instead of the era's raw
`cmpwi r26,0x0`; size 0x198→0x19C) — i.e. era caller says "narrow param", era callee
says "int param", mutually impossible for one declaration in one TU under this profile.
`#pragma peephole on` does NOT help (it over-folds: 192 insn, lcs 82 %).
ASK candidate: era TU-wide bool width / an era prototype mismatch (integrator/config
question), OR a per-call spelling class not yet found. Also try `opt_common_subs off`
(already inert here: t1_ocs) and a permuter round on the arg-home tiebreak.
(W2) 2 rows: `extsh r26 / or r0,r26` (era) vs `extsh r3 / or r0,r3` (ours) —
MWCC copy-forwards the first `(s16)` cast into a volatile instead of the var's home.
Operand-order swaps (mask&cmd, or-operand swap, u32 mask globals, `& (u32)`, nested
casts, t-chains) are ALL inert: bad stays 2 → allocator tiebreak class.

## LADDER (offline probe rounds; wprobe2.py = word-level, reloc-aware oracle)
* v1 natural C (u16 cursor, s16 cmd) 0x30c/195 → objdiff 92.544 % (one_shot, real build)
* round2 (op-reuse/compound/alias/change-order) 0x304 but r25-31 bank — wrong mechanism
* round3-4 (bank hunt; s32 cmd; 0x800 bit fix; decl orders) lmw_d2 196, frame 0x20, r26-31 ✓
* round5 BoTeq 195, bad 33, lcs 189/193
* round6/7 t2_cubool **194, lcs 190**, sibling-safe ← LANDED
* round7 t1_bothbool **193 = GATE-OK, lcs 191** but SIBLING-DRIFTS draw_chunk_textured_strips ✗ rejected
* round8-12 45+ arg/mask/register/peephole spellings — all ≥ t2 or gate-fail; peephole-on
  and register-hint probes dead.
Builds used on the repo: 4 (v1 fail, v1 ok, candidate ok, full ninja) ≤ 8 cap.
Probe compiles: ~90 offline (skills/probe_compile.sh), 0 repo builds each.

## Gates (landed state)
gnm `T 0x308` vs gate 0x304 → FAIL (no match claim) | one_shot 99.404 %,
776 vs 772 B | full ninja rc=0, dol verify 100 % matched/linked 55/55 |
report_delta vs baseline-c5e453d7 rc=0: +3 new exact (sibling's transform_chunk +
2 lane-local pre-merge), **regressions 0** | check_pr --no-build PASS
(linked 3540 all exact, regressed 0) | unit stays UNLINKED (config = integrator).
one_shot shows `setup_model_draw_state` at 99.782 in the UNLINKED .o view (= anonymous
`.sdata2` pool rows `@387-@390` vs named lbl_805E109C… — cosmetic pool naming, NOT a
report regression; report_delta confirms 0 and report.json keeps it at 100.0).

## Files
* `src/pso/unk/text_803E2D70.cpp` — body + extern-C decls + `ChunkModel_803E44D4.polygons`
  u16*→s16* (era loop head loads with `lha`; caller codegen unchanged) + forward decl
  param type + the two callee prototypes described above.
* kit (untracked, like the sibling's): orig_fn.s, probe.cpp, wprobe2.py (oracle),
  wprobe.py (first version), gen*.py + variants*/ (98 spelling variants), mini*.cpp
  (bool-clamp proof), build/shot/delta/checkpr logs.

---

# VISIT 2 (permuter round, card-poly-perm) — INERT at 99.404, both walls receipted

## Harness (finished the interrupted visit-2 child; kit perm/ subdir)
* `base.c` = champ body verbatim (fleet/f7 c9e71e33, byte-check vs landed lines 640-730:
  only sanctioned deltas = `TObjPlayer::setup_tev_passclr()` -> literal mangled extern-C,
  and 5 callees hand-mangled to era-U names (`set_chunk_blend__FUl`, `apply_chunk_texture_command__Fll`,
  `set_strip_lighting_chan_ctrl__FUl`, `set_chunk_blend_depth_mode__Fll`, `setup_chunk_tev_stages__Fv`)
  so relocs pair by name under the extern-C wrapper. `bool` param -> `permbool` typedef +
  compile.sh `sed -e '/^typedef int permbool/d' -e 's/permbool/bool/g'` (pycparser CANNOT parse
  `bool` as a type — child's lexer-based faith claim FALSIFIED by control probe; MWCC still
  sees true `bool` so codegen is champ-faithful).
* `compile.sh` = verbatim unit ninja MWCC line: GC/2.6 `-O3,p -opt nopeephole` (NOT the
  802C6DD4 -O4,s template — unit flags differ), -MMD dropped, wrapper extern-"C", abs in/out,
  no gobjcopy (unit rule has none).
* `settings.toml` = func_name + compiler_type=mwcc + FLAT [weight_overrides] size-preserving
  profile (reorder_decls/stmts 80, temp_for_expr 30, refer_to_var 25, commutative/inequalities 20,
  add_self_assignment/pad_var_decl/reverse_cond 15, noise families 0).
* `target.o` = era dtk block via as(1): gnm `0x304 T dispatch_chunk_polygon_list` (gate-true),
  U-list 23/23 matched by base_direct.o.

## CONTROL-PROBE-FIRST receipts
* BASE-VERIFY: `compile.sh base.c` -> base_direct.o, dispatch block = 194 words, BYTE-IDENTICAL
  vs fresh ninja champ .o (rm+rebuild, MWCC line observed). PASS, non-vacuous (ls'd both, len>0).
* `permuter.py --debug --show-errors`: penalty = Insertions 1 (clamp, W1) + Register Diff 3
  (W2 rows + clamp-adjacent color row) + 0 Deletions (func_name slice clean) ->
  **champ perm score = 115** = --better-only threshold.
* Card ownership re-verified via config/GPOE8P/psov3: splits `pso/unk/text_803E2D70.cpp
  .text 0x803E2D70-0x803E4954` contains symbol `dispatch_chunk_polygon_list @0x803E3F2C size:0x304`.

## ROUND 1 (the mandated 1x900s) — ZERO harvests
* Launch 15:24:42 PST, PID 4972 (perm.pid), cap wrapper PID 4973 (sleep 900 -> TERM -> KILL).
  Slot pre-check: `pgrep -fl permuter.py` empty (f8 idle). -j 4, --better-only --stop-on-zero.
* 30s liveness: iteration 2527 (>0) ALIVE -> no retry authorized/fired.
* Cap exit 15:39:47: **44,882 iters (~50/s healthy), 1401 candidate compile-fails (3.1% noise,
  no permuter-internal failures), output-* count = 0** => zero candidates below 115.
* Dead-round guard SATISFIED (iters>0, velocity healthy): saturation datum is real, not extraction death.

## W2 verdict (the target of this visit)
Scratch-home tiebreak `extsh r26/or r0,r26` (era) vs `extsh r3/or r0,r3` (ours): permutation
found NO spelling below champ in 44.8k iters under a decl/stmt-reorder-dominant profile —
the search-side confirmation of visit-1's 60+ hand-variant inertness. Combined datum:
MWCC GC/2.6 copy-forward-to-volatile at the if-join is an allocator decision that neither
relocates, splits (temp_for_expr active), nor aliases escape = tiebreak wall CONFIRMED permuter-class-exhausted.

## W1 memo (NOT re-litigated — two data points banked, memo only)
+1 clamp insertion dominates the base penalty (100 of 115); pinned by the same-TU
`s32 large` decl of draw_chunk_textured_strips (bool decl fixes caller, drifts callee 0x198->0x19C).
Era caller-narrow vs era callee-int = era bool-width/prototype maintainer ASK. No gate-0x304
harvest was ever reachable by body spelling in this context — clamp is decl-determined, not order-determined.

## Gates / tree state at close
* Branch card-poly-perm = origin/master(9575dbb7) + cherry-pick -x c9e71e33 -> 4d3445e4 (Scott
  authorship preserved, clean 3-way — master's #178/#180 additions are disjoint regions).
* REVERT-TO-CHAMP: fresh card-branch unit .o dispatch block = 194 words BYTE-IDENTICAL vs
  base_direct.o; git status 0 tracked diffs at HEAD 4d3445e4.
* one_shot on new base: dispatch match=99.404144, ORIG 772 / OURS 776 (gate 0x304 FAIL — unchanged, expected).
* Screening ladder ARMED for a future visit: `perm/harvest_dcpol.py` (gate-0x304-first +
  ub_poison def-dominance (fleet law port) + NEWSYM-vs-base_direct + wprobe2 oracle rank) and
  `perm/port_candidate.py` (brace-balanced verbatim splice). Run on empty harvest — 0 candidates screened.
* Report copy: report_cardstart_fleetstate.json (saved at card start).
* Re-root path if a future lever breaks W1: the ONLY route to a gate-pass is the narrow-decl
  flip + callee-body salvage (t1_bothbool family) — permuter basin re-seed from THAT state,
  not from this one.
