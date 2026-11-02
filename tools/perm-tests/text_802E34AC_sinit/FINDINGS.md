# text_802E34AC (fn_802E34AC, 0x638) — CLASS-A confirmed, MWCC __sinit synthesis, GATE-EXACT

Era cold: src was 1-byte placeholder, unit unlinked (linked False in build.ninja), report 0 rows paired.

## CLASS TRIAGE (first, per protocol)
CLASS-A compiler-synthesized `__sinit_<file>_cpp` — proof:
- body = [6 computed-f32 runtime stores] + [147-word dense template->instance copy storm]
  + [runtime __ptmf_null triple insertion] + [stmw/lmw bookends]; ZERO bl calls (not the
  global-object ctor-wrapper family); `addi r4,r3,0` cursor artifact; .ctors-registered
  single word 0x80433FD0 = 0x802E34AC (DOL-verified); era name fn_ + local __sinit semantics.
- force_active: fn_802E34AC NOT in config/GPOE8P/psov3/config.yml -> swap-safe for cold link
  (TRAP cleared; unit stays unlinked anyway, see LINK).
- sub-family: A6C8/BFBF4 trio doctrine (state-action PMF table boot seed) + 69C extern-const
  f32-expression preamble. New member: this is the first trio unit whose preamble contains a
  MUL (needs FP contraction, see below).

## Decoded anatomy (parse_storm.py -> storm_map.json, 398 words, symbolic copy-provenance)
- Fragment (era map, all rows live): lbl_804E3040 f32[2] {a dyn, b=90.0 static},
  lbl_804E3048 f32[2] {c,e dyn}, lbl_804E3050 0x254 = {g,h dyn + 49x12B template pool 0x24C},
  lbl_804E32A4 0x258 = instance (zero in DOL), lbl_805D68E0 .sbss {k dyn}.
  Consumer: `TAdTimeSetGC::run_task` + ChrSelectGC dispatch read `+idx*0x18` pairs, null-check.
- Expressions (W=RO[0]=540.0, H=RO[1]=260.0 via extern lbl_80472930[2], literals
  0.5/640/20/10/40/85 = sdata2 rows lbl_805DE8E8..90C, all era-named):
  a=0.5*(640−W)=50.0, c=20+a=70.0, e=10+(90+H)=360.0, g=0.5*W+a=320.0(FUSED fma), h=e−85=265.0, k=W−40=500.0.
- Storm: pool src +0x18..+0x260 (147 words) -> dst +0x264..+0x4BC dense, single 3-word
  __ptmf_null insertion at dst +0x3cc (instance slot 30) — 147+3=150 = row size exact.
  Pool = 49 {0,−1,fnptr} triples: 26 named TAdSinglePlyChrSelectGC members (Fv/FPv/Fl/Fi)
  + 23 era-UNMANGLED TAdSinglePlyChrSelectGC__sub_* placeholders (21 distinct, 3x reuse of
  sub_802E22A4, 2x sub_802E24B8). All 49 targets owned by matched linked sibling
  pso/ui/TAdSinglePlyChrSelectGC_802E13C8.cpp (0x802E13C8-0x802E32E8).

## KEY FINDING: era TU built with FP CONTRACTION (family-wide update)
g's tree 0.5*W + a compiles to `fmuls+fadds` (399 words, GATE FAIL 0x63C) in every plain
spelling (operand swap / mul+mul dup / K-position all inert). Era word = `fmadds f1,f6,f7,f5`.
Fix: `#pragma push` + `#pragma fp_contract on` at FILE TOP, never popped -> GATE 0x638 EXACT.
Measured placement law (offline compiles, GC/2.6 -O4,s = repo edge flags):
- pragma scoped around the f32 initializers only: NO fusion (0x63C) — pragma region around
  declarations does NOT reach the synthesized __sinit.
- pragma at file top through EOF: fusion ✓. Command-line `-fp_contract on` (same build) ✓.
- => synthesis obeys the pragma state at TU END. Future trio/69C-class units with mul in
  computed-float inits: file-top `#pragma fp_contract on` is the first knob, not expression surgery.
- `extern const f32` on the rodata source is load-bearing: non-const refills badly (0x634,
  pos 2-3 — W reload spam). Keep const.

## Spellings that hit the gate (winner = q_a48.cpp; repo file = header + it verbatim)
- Mirror class TAdSinglePlyChrSelectGC decl-only (46 members); `typedef void (C::*Handler)();`
- overloaded names (update_state Fi/FPv, update_load_state Fv/FPv): bare `(Handler)&C::m`
  AMBIGUOUS -> disambiguate via full pmf-type cast `(Handler)(void (C::*)(int))&C::m` —
  accepted, era mangle bytes verbatim, no codegen impact. NEW SPELLING (BFBF4 had no dup names).
- `__declspec(section ".data")` on the three f32[2] arrays; K = plain `static f32` (.sbss);
  `static Handler lbl_804E32A4[50]` with plain `0` at slot 30 -> MWCC auto [pool][instance]
  + null-triple storm (802B0A44 strided-law extended: pure-PMF array = pool 49x12, single
  null -> one 3-word __ptmf_null fill; cursor addi +0x264 native).
- Instance named EXACT era row lbl_804E32A4; geometry arrays named lbl_804E3040/048/050.
- K decl position: after lbl_804E3048 = best (pos 354); first/a40/last = 350/351/354.

## Proof (wd_802E34AC.py; repo_wd_proof.txt from the repo-built .o)
- gnm __sinit_text_802E34AC_cpp = 0x638 == row size:0x638 GATE EXACT.
- positional raw-byte equal 354/398; resolve-at-link class rows 13 (2/13 era-word re-compute
  match; the rest = preamble FP register COLOR rows, see residual); content multiset 380/398
  (era-only 18 / ours-only 17); LCS 373/398.
- RESIDUE = 45-row FP preamble scheduler tie-class ONLY (f1-vs-f2 first-color, W load @7 vs
  @13, sunk sub/mul adds, spill-slot order); storm + cursor + tail 100% byte-equal, zero
  order residue in 353 rows. Same class as 69C stfs-sink residual + TBoss6Rock bank rotation
  — color rows violate word-diff==0 by definition, NOT raisable; ~20 spelling/K-position
  probes exhausted (grid c0/c1 x4, non-const, paren, g-swap, pragma placements).

## PAIRING / ASK (#173 template shape)
- rename row 21008 `fn_802E34AC` -> `__sinit_text_802E34AC_cpp` scope:local
  (precedents rows 1128/2174/2256/14846/22209/23145/23312/20155 + 67F4 23120; 13 era-named
  __sinit rows incl. __sinit_TObjEneDelDepth_cpp prove renames land in map treatment).
- est. pairing ~93.7% at rename (LCS 373/398) pre-color-fixes; .ctors-0 row already pairs
  100.0 in report pre-rename (verify post-build).

## LINK STATUS: HELD UNLINKED (double-reason)
1. .data fragment 0x804E3040-0x804E352C is ALREADY CLAIMED + LINKED by matched sibling
   pso/menu/TAdTimeSetGC.cpp (100.0 complete_units, data 1260/1260 — it bakes the same pool
   words as flat void* statics, verified word-identical to era DOL). Our .o re-emits the
   fragment from its TU -> link would double-own the range. Integrator decision: move the
   static data into this TU (true era TU shape: TAdTimeSetGC text ends EXACTLY at
   0x802E34AC = this __sinit was the tail of the era TAdTimeSetGC.cpp TU) or keep sibling
   ownership + this unit text-only forever (needs extern-data synthesis variant = rejected
   class, cursor addi unreachable).
2. 23 placeholder pool refs member-mangled vs era free-export names = link-breakers
   (row-rename territory; free->pmf cast hard-rejected, family law).
CYCLE NOTE: bidirectional consumer cycle exists in spirit (sibling reads blob, blob relocs
reach sibling text) but is MOOT for claiming — data already owned+linked; our unit adds
.text+ctors only.

## Screens
- splits: .text 0x802E34AC-0x802E3AE4 == row size 0x638 exact; .ctors 1 word value
  0x802E34AC DOL-verified; unit owns NO .data (correct — sibling owns fragment).
- def-count: fn_802E34AC defined nowhere in src (era row 1 def); blob names defined only by
  linked sibling (our refs = internal statics, no collision).
- absent-verify teeth: 49 pool targets + lbl_80472930 + lbl_804E3040/048/050/32A4 +
  lbl_805D68E0 + 6 x lbl_805DExxx + __ptmf_null = ALL symbols.txt rows verbatim
  (parse_storm name-resolution, zero RAW_TEXT rows).
- gate: gnm OURS 0x638 == size:0x638.
