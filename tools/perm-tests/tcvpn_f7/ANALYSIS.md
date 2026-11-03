# transform_chunk_vertices_pos_normal — cold 288B — ASM-CLASS MATCH (46ebd9c1)

## Semantics (decoded from orig_fn.s, 72 insns)
`(Hdr_803E34B0 *job, s32 matrix)`: dst=str[j] 32B out, src=str[i] 24B in
{pos3,nrm3}, count = job->count. Matrix r4 = f32[12] viewed as 4 groups x 3:
pos = m[3] + vx*m[0] + vy*m[1] + vz*m[2] (translation-first fold, per-component
pair lanes via ps_madds0/madds1, overlapping wr-swapped psq_l pair loads at
m-elements 0,2/3,5/6,8/9,11(+12 junk lane)); nrm = 3x3 rotate (ps_muls1 seed,
no translation), outputs (px,py)(pz,junk)(nx,ny)(nz,junk) written by 4
psq_stu (wr=1 swaps the two z/junk lanes; junk lands under later quad — benign).
Peeled first vertex, CTR loop (mtctr count-1; guard cmpwi/beq when count==1;
tail store after bdnz exhaustion), f14-f18 spill at frame 0x40. Zero relocs:
all 72 words raw opwords; internal .L branches encoded directly.

## ASM-class proof
- survey/results.tsv: FULL TU with v1 natural-C body, 20/20 compilers,
  verbatim profile flags (-O3,p -inline off ... wibo): 0x130 everywhere, 0 ps-ops.
- survey2/results.tsv: self-contained probe (probe_v1.cpp), 20/20:
  0x130 (1.3+) / 0x134 (1.0-2.0p1), ps-ops=0 at EVERY version.
  (script bug round1: MWCC -o takes a DIRECTORY — all outputs piled into
  build/GPOE8P/src/pso/unk/probe_v1.o — fixed with per-version dirs; that
  stray probe .o was removed after.)
- Corpus corroboration: zero matched ps-arith C functions exist repo-wide;
  all matched ps emitters (gx/mtx/musyx/E8C4/E9FC) are themselves asm-class.
  MWCC GC never pairs scalar float expressions into ps_madds chains.

## Verdict note for the fleet (IMPORTANT)
fleet/f7 lineage is based on c5e453d7 (BEHIND origin/master 5d6f83cb by
#169..#171). Lane battery MUST use baseline-c5e453d7.json
(+3 new exact = mine + lane-local pre-merge copies of #169/#170 fns, 0
regressions, rc=0). Against baseline-5d6f83cb.json the missing merge
progress reads as 6 phantom regressions (linked 3543->3540 etc.).
Integrator promotion: cherry-pick 46ebd9c1 (pure 6-line src add,   text_803E2D70.cpp in
  5d6f83cb..HEAD stat = 4 deletions → MASTER CHANGED THIS FILE since
  c5e453d7! MEASURED DRIFT (diff HEAD..origin/master, this file): only a
  +4-line tail addition after clear_chunk_render_flags (far from my
  line-272 insertion; both context anchors `#undef node` /
  `transform_vertex_list` verbatim-identical) → clean git-apply
  expected; still promote via `git show 46ebd9c1 -- file > patch` +
  apply --check on master tip, rebuild, re-score (expect +1/0 vs
  baseline-5d6f83cb).

## Gates (lane)
gnm T 0x120 EXACT | one_shot 100.0/100.0 72 rows, 0 encoding word-diff |
full ninja rc=0 | dol CHECK OK (unit unlinked) | report_delta rc=0 +3/0 |
check_pr PASS (3540 linked all exact) | builds 3/6 repo + 40 probes.
