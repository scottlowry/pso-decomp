# ANATOMY — TAdTrialModemChkGC__sub_8042EC14 (psov3/pso/unk/text_8042EAD4, 0x184)

## Verdict
MATCHED 100.0 (97/97 rows, gnm size 0x184 = gate). The whole unit
text_8042EAD4 is now 888/888 code, 4/4 functions, fuzzy 100.0 -> unit-complete
(link candidate; linked_units row is config/integrator).

## What the three-lane wall actually was
Prior parks: fb3c30b5 / c5a7461d (f4) / ff589b55 (f8) all at 95.87629, residual
8 rows = pure prologue scheduler-pool ORDER (identical multiset + identical
register colors):

    ORIG slots 2-9:  lwzE11 | lis | stw r0,0x14(r1) | stw r31 | addi | lwzCA8 | stwCB4 | cmpwi
    champ slots 2-9: lis    | stw r0,0x14(r1) | stw r31 | addi | lwzCA8 | lwzE11 | cmpwi | stwCB4

f8 ran a fair trial (22 spellings, 7 permuter basins ~30k iters, 8 compiler x
-O4,p/s cells) and recorded the only revival route as: "if a future visit finds
a MATCHED fn with load-before-LR-save, THAT is the Rosetta for this wall".
Their corpus screen counted 0 such fns -- it screened the SHAPE but never read
the DECLARATIONS of the hits.

## The Rosetta screen (this lane, scripts/rosetta inline)
Screened all 5090 orig .s files for an integer/fixed-point LOAD emitted between
`mflr r0` and the first `stw rX,N(r1)` frame save, joined against report.json
per-fn fuzzy: 566 candidates, 558 inside 100%-matched fns; 6 of those are
integer lwz:
  init_and_add_ref__6TLobbyFv        `extern const s32 lbl_805E0D30;`
  init_afs_adxf_state__6TLobbyFv     `extern const char *const volatile lbl_805E0D80;`
  sj_ring_buffer_init                `__declspec(section ".sdata2") extern const char* const volatile`
  gcrna_initialize                   `extern "C" const char *const volatile gcrna_version_pointer`
  TBoss6Type1::advance_animations / TBoss6Type2::update_motion_tracks
Every one reads a QUALIFIED (const / const-volatile) sda21 symbol. None used a
plain `extern u32` -- which is exactly what all four prior lanes' 22+ spellings
kept re-using.

## THE LEVER (minimal, abliterated)
`extern u32 lbl_805E11F0;` -> `extern const s32 lbl_805E11F0;`  ==> 100.0, 0 rows.
MWCC hoists a load whose source symbol is const-qualified (read-only section =>
no aliasing store can invalidate it) above the frame saves, which is precisely
the orig ordering. On an unqualified extern the compiler keeps the load next to
its consuming store, giving the champ order.

Offline 3-way ablation (kit, 0 repo builds; splice + full-TU .o-swap scoring):
  A01 guard-volatile only   95.87629   (no effect)
  A03 temp-only             95.87629   (no effect)
  A06 guard+const           100.0
  A02 CONST ONLY            100.0      <-- sole necessary lever
  A07 all three             100.0
Also banked en route: X05 (volatile guard + use-site cast) 97.83505/5 rows --
a real improvement over the fleet champ, kept as the runner-up spelling.

## const-qualification is evidence, not a hack
config/GPOE8P/psov3/symbols.txt:59484
  `lbl_805E11F0 = .sdata2:0x805E11F0; // type:object size:0x4 data:4byte`
- .sdata2 = read-only small-data section
- repo-wide refs (grep over build/GPOE8P/asm/): exactly ONE `lwz`, ZERO stores
- house precedent for the same spelling on adjacent .sdata2 externs:
  `extern const f32 lbl_805E10B0;`, `extern const ByteColor lbl_805E1090;`, ...

## Signature correction (report-only change from the f4/f8 seed)
Seed spelled `(int arg0, int arg1)`; neither reg is read (slot 2 overwrites r3,
slot 3 overwrites r4) and the single caller 0x8007F904 sets nothing. Shipped as
`(void)` -- kit proof S01_voidsig.o is word-IDENTICAL over 0x140..0x2c4 to the
(int,int) build, so the byte claim is unaffected. `(void)` is the house form
(4901 uses); the `(int arg0, int arg1)` unused-pair pattern exists in 2 files.

## Naming proposal (report-only, row kept as symbols.txt has it)
Class evidence: this is the TAdTrialModemChkGC first-touch context installer --
it snapshots E11F0, allocates/relocates the 0x8000 modem blob via fn_8042E8B8
(returns the 0x80003100 trampoline base), lays out the four sub-buffers
(+0x6020/+0x6820/+0x7020/+0x7820), validates the 'SEGA' magic at offset 0,
zero-fills and stamps it, then runs the same 9-call init chain as the MATCHED
sibling TAdTrialModemChkGC::init_modem_check_params (0x8042EA10, one unit back)
and registers five message strings through fn_8042ED98.
Proposal: TAdTrialModemChkGC::init_modem_context() / reset_modem_context_init.
Guard `if ((s32) lbl_805D7CA8 == 0)` = already-initialized latch (set to 1 here).

## Gates (all on fleet/f3 @d3d0b6e5 + this change)
- gnm OURS: 4 syms 0xD0/0x70/0x184/0xB4 = .text 0x378 == split range
  0x8042EAD4..0x8042EE4C exactly (no gaps -> no orphan chiplet in this unit;
  the pad screen was resolved offline from the .fn map before any build).
- one_shot: 100.0 x4 (ORIG and OURS sides agree), no data FAIL lines.
- report_delta --check vs clean-tip before-report: RC=0, New exact functions 1
  (+0x8042EC14 TAdTrialModemChkGC__sub_8042EC14), regressions 0, FAIL count 0.
- full ninja: RC=0, psov3.dol sha 0d85744b... == config/GPOE8P/psov3/build.sha1.
- check_pr.py: RC=0 PASS; link_units check OK (3539 all exact);
  exact candidates to add 3, regressed (drop) 0.
- Repo builds: 7/8 (unit .o x4, full ninja x3). ~45 kit compiles at 0 build cost.
- Sacred parks byte-untouched: fn_8042E8C4 (79a4cfae), pad_03_8042E9FC (d3d0b6e5),
  E9FC init_modem_check_params, fish/dc78/crawfish/AttackCol/check_equip/
  428DC8/803D0714 -- all still 100.0 in the post-change report.
- ORPHAN-CHIPLET screen for this unit: CLEAN (four .fn blocks tile 0x378).

## Kit
perm-tests/f3_42EC14/ (untracked): base.cpp (champ, BYTE-IDENTICAL base-verify),
compile.sh (unit-exact GC/2.6 flags), score_splice.py (objdiff splice, restores
in finally), score_full.py (full-TU .o swap -> sibling regression detector),
gen_w/gen_x/gen_y/gen_z/gen_p/gen_abl.py + W*/X*/Y*/Z*/P*/A* variants, ORIG.s.
