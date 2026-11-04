# KIT_STATE — card-taginfo-564 (t_2cd4abc9), render__22TChCrTagInformationStrFv (0x80309944, gate 0x234)

Base 5695627b, branch card-taginfo-564, tip committed 2026-11-03.

## Verdict
FLOOR 99.49645 (141/141 rows, gate size pass on committed tip, clean rebuild).
Unit: ALL 5 fns present at era sizes (create 0x50, render 0x234, run_task 0x10C, __dt 0x58, __ct 0xA4).
Gates: report_delta --check regressions 0; check_pr PASS; 4 siblings byte-stable. linked_units 3308 — 3309
NOT claimable until render hits 100.0 (needs link of this unit).

## PS screen (new law)
GSP arith count = 0 (PS-CLEAN). Gekko spill map: 9× stfd+psq_st f23–f31 prologue (0x50–0xd8), 9× psq_l+lfd
epilogue, frame 0xe0, bank stmw r21. Benign FPR-pressure info; the spill home-count + frame landed first build.

## Landed levers (in score order)
- v1 author (transcribe from era anatomy): 94.35461, size 0x230.
- f32 pos[2] = {315.0f, 280.0f} mid-block array-init (era pool pair 0x804755F0 = unit's own UNCLAIMED .rodata,
  splits has only .text+.data): pool-copy shape lwz-pair, +1 insn = gate 0x234. 95.84397.
- rp_sin/rp_cos named product temps in ring draw: era sin-first staging, kills fmr f2,f28. 97.54610 (size −1).
- color2 3rd field re-read `*(f32*)((s8*)arg0+0x30)`: restores era lfs f0,0x30(r31) reload, gate back. 98.36170.
- t2 mutated in place (t2 = 1.0f - t2): era fsubs in-place identity. 98.50355.
- INLINE division in k-loop header `k += 0x1000000/(4*j)`: defeats MWCC 2.6 ×16 loop-normalization
  (named `step` local variant scales span+bound to 0x10000000). Lands divw r29,r28,r30 + whole GPR callee
  ring. 99.24823. KEY: division must NOT be a named local.
- s32 i declared before const char *entry: flips i<->entry GPR transposition (era i@r24 > entry@r23;
  decl-order = higher-rank rule works on GPR ring here). 99.49645 (CHAMP 749125d8).

## CLOSED classes (this visit, do not re-roll)
- opt_propagation off (function window): INERT on divw ×16 and arg staging (byte-identical score).
- (j<<2) divisor form: folds to same AST as 4*j, ×16 persists.
- Pool names @18/@47 rows (slots 30,31,75,79): staged-unit noise, address-resolved at link; free in report.

## Residual frontier (6 rows, ranked)
1. FPR ladder {t2 f27 vs era f25; t2b f26 vs f25; scale f25 vs f26} = 6 rows: t2 BIRTH rank = coalescer
   tiebreak stratum (era allocates free-lowest f25 at t2 def; ours center-packs f27). t2b/scale in-place
   chain already matched. Class: def-binding (anatomy MEMBER-DECL-ORDER kin). Cheap next probe: fade/t2
   decl swap grid (2 builds) — FPR decl-rank was INERT on the campaign that produced the map note.
2. Guard beq target (slot 26): era skips ALL FPR+GPR restores + lwz r0 on the fade==0.0 early-out
   (dead-restore CFG elimination, lands mtlr with live r0=lr); ours skips only psq_l f31. RA transform,
   no source lever found; coupled to the 5 branch-target rows (they re-align if block layout matches).
3. span home imm (slot 81 lis r28,0x100 vs 0x1): ×16 residue rides the BOUND value only after inline-division
   (divw/bound registers era-exact). Angle-quantization semantics: k hits 16× era values → NOT
   ship-able-as-is at floor; frontier probe: bound spelled via separate literal from numerator, or
   strength_reduction off window (gate risk −1 insn: li/addi ladder dies).

## Cold start
cd /Users/scott/Hermes/pso-decomp/pso-decomp-f7 && git branch --show-current  # card-taginfo-564
rm -f build/GPOE8P/src/pso/misc/TChCrTagInformationStr.o && ninja build/GPOE8P/src/pso/misc/TChCrTagInformationStr.o
/opt/homebrew/opt/binutils/bin/gnm -S build/GPOE8P/src/pso/misc/TChCrTagInformationStr.o | grep render__22  # 0x234
/Users/scott/.hermes/installs/60d8a79da6991a71/environments/28d86d1068e44adc8d1a5d2ca8c63c2c/venv/bin/python3.14 \
  /Users/scott/.hermes/profiles/pso-decomp/skills/pso-decomp/scripts/one_shot_diff.py psov3/pso/misc/TChCrTagInformationStr render__22TChCrTagInformationStrFv
Era block: build/GPOE8P/asm/pso/misc/TChCrTagInformationStr.s (.fn render__22TChCrTagInformationStrFv)
