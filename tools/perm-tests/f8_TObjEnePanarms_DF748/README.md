# f8 kit — TObjEnePanarms__sub_800DF748 (238W copy-tempo .ctors init)

## Anatomy (PROVEN — decode scratch/df748_decode.py, df748_anatomy.txt)
- Pure straight-line: 84 dword copies, src = sym+0x18c..0x2d8 -> dst = sym+0x2dc..0x428
  (sym = bm7_s_paa_body_model_names, .data 0x80494E80; src/dst non-overlapping; uniform +0x150 shift; 0 holes/dups).
- dtk obj (build/GPOE8P/obj/pso/enemy/TObjEnePanarms_800DF6E0.o): ONE U data symbol
  (bm7_s_paa_body_model_names); `addi r17, r16, 0x2dc` carries NO RELOC => dst window is
  DERIVED ARITHMETIC, not a second symbol. Unit .ctors (splits.txt 2026-2028, 0x80433F60)
  content == 0x800DF748 (verified from linked elf) => startup static-init. Baseline: no body
  in src (unpaired, fuzzy None trivially).
- Superblocks (store-occurrence order): G1 tempo k=[26,24,27..44] (chain r30/r0 ping-pong
  through slots 0x7c,0x8..0x48(r1); k=44 tail uses mr r0,r30 + dead slot 0x4c),
  G2 batch k=[0..23,25] (25 loads r29..r31, then stores; first 3 dst stores anchored
  r16+0x2dc/0x2e0/0x2e4 = d[0..2] via src base, rest via r17), G3 tempo k=[71,69,72..82]
  (slots 0x80,0x50..0x78), G4 batch k=[45..68,70,83].
- Op total 238 = 84 src lwz + 84 dst stw + 31 slot stw + 30 slot lwz + 1 mr + 8 frame
  (stwu -0xd0, stmw r14 0x88, lis+addi r16, addi r17, lmw, addi sp, blr).
  Slot 0x4c = DEAD spill (store-only, original k=44 mr tail feeds both slot and dst store).

## Family spelling STATUS (cracked partially — window mechanism FOUND)
- E2964 v3b-family form (fresh temp per load, pair stmts, single base) => 235w, all dst
  stores fold to r16+big-disp, NO window register. 235w class: M1/M4(+=)/M6(&sym[0x2dc])/
  F1(u16 cast)/F2(u8+cast)/F3(late redef)/M8(direct pairs) — MWCC 2.6 constant-propagates
  pointer locals THROUGH uses; no pure local-arithmetic form keeps a window register.
- Two-symbol form (extern u8 lbl_8049515C[] at dst addr) => window YES but 239w
  (second `lis r?,symB@ha` can never be CSEd across different relocs). DEAD for gate.
- S3 KEY FINDING: early literal dst-base uses `d[0]=b[99]; d[1]=b[100]; d[2]=b[101];`
  BEFORE the 84 pair-statements (which then re-store k=0..2 from G2 positions) =>
  MWCC materializes `addi r17,r16,0x2dc` AND size lands EXACTLY 0x3B8 (238W).
  This mirrors the orig fingerprint (orig d[0..2] stores r16-anchored in batch1).
- Residual 231 mism rows = SCHEDULING BASIN (chain rotation k7/5 vs orig k26/24 start,
  store anchoring mix, slot offsets) — permuter seed = S3 base.c, size-preserving profile
  (reorder/temp_for_expr heavy, structural mutators zeroed) run 900s (--better-only -j4).

## Oracle
- compile.sh: exact ninja mwcc line (scratch df748_cc.txt, pre-cut at ' && '), candidate
  wrapped extern "C", abs paths, out=src.o by default. BASE-VERIFY: kit .o vs repo in-place
  .o = byte-identical fn block (M1 test) — PASS.
- Ranking: probe_diff.py <kit.o> TObjEnePanarms__sub_800DF748 \
  build/GPOE8P/asm/pso/enemy/TObjEnePanarms_800DF6E0.s  (REAL mism rows) + gnm size==000003b8.
- target.o = as(1)-sliced target_sliced.s (dtk full-unit obj gave 72 phantom Deletions;
  sliced = penalty rows cover our fn only; base score S3 = 3990).

## Files
- df748_probe.sh, df748_gen.py, df748_kitsetup.py, gen_S.py, df748_decode.py — scratch kit
- cand/spelling variants: scratch df748_M*.c/F*/S* + cand_df748_v1a/v2 (in-place probes)
- Round: launch via scratch/df748_round.sh; harvest via df748_rank.py (this dir).

## Round r1 FINAL RESULTS (this session)
- S3 seed round: 3550 iters/900s, 278 harvests. Size gate (0x3B8) survivors at 231-rows floor;
  BEST = output-3485-1: 238W gnm-EXACT, 221 REAL rows (in-place transplant probe, cap 6/6 used).
  Its r17 use is batch DATA (lwz r17,396(r16)) — window NEVER materialized in folded family.
  221/238 = ~7% paired — far below WIP bar (fleet precedent 90.9-99.9). NOT committed; repo clean at c3121002.
- Fold law (deliverable): MWCC 1.3.2-2.7 propagate single-symbol-derived pointer locals into ALL uses
  (no window addi survives); two-symbol spelling keeps window but pays a 2nd lis (+1W = gate FAIL
  vs 0x3B8 slot; also link-dup risk vs origin-extraction fill on this UNLINKED unit, build.ninja:10013).
- Row-floor math: folded family ~204-row floor = 84 store-anchor + ~90 operand-column + rotation residue.
  100.0 impossible without the mechanism. Morning family card must attack: per-unit flag pin (integrator),
  pragma/asm-injection forms, or accept folded-family INCONCLUSIVE parking for both members.
- NOTE litter trap: MWCC -MMD writes `<tmpbase>.o.src.d` into CWD — kit compile.sh runs from REPO ->
  ~2800 .d files littered repo root (git clean -f -- '*.src.d' cleared; future kits: drop -MMD or cd KIT).

## Ladder (next visit if round < 238/0)
1. Re-rank ALL output-*/source.c with SIZE GATE 0x3B8 first, then probe_diff rows; transplant
   best into repo file in-place (df748_probe.sh), full ninja build (cap!), battery, commit.
2. If plateau: hand-sweep ORDER permutations of the 3 early dup-stores (0/1/2/3 dups, and
   d[0..2] placed at other program points) + pair vs fresh-temp — basin hops permuter misses.
3. E2964 application: if a harvest hits ~0 mism rows here, the SAME S3 form (3 early d[0..2]
   dup stores + fresh-temp pairs) applies over there (+9w kill-list: r16/r20 addi via this
   lever, spill-count via fresh temps, mr tail site) — morning family card material.
4. KNOWN: naming report-only — TObjEnePanarms__sub_800DF748 (symbols.txt row, 0x3B8).
   Data claims untouched (no splits.txt edits; symbol reference only).
