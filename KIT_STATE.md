# Campaign: test_box_sphere_contact (TObjPlayer_803DF7A8 seat 0x803E112C) — v4 PARK receipt (visit-5)

- Lane: branch `card-boxsphere-v4`, tree `pso-decomp-f4`, base master `00cda35c`. v3 park tip (824b705d) seeded VERBATIM as rung0 `8e8e8fd0` (blob-identity 57da67a0 ✓, echo 97.45671/97.31602/1848 BEFORE kit).
- **Tip state: PARK at official 97.70563 / one_shot 97.56493, 111 diff-rows (462 orig), gate 0x738 exact, size 1848.** Unit UNLINKED (DOL inert `0d85744b51d7379efb025a943d0cd5aaae2191a3` ✓, linked_units grep 0 ✓, full ninja rc=0).
- PIN live-cited (build.ninja `# pso/player/TObjPlayer_803DF7A8.cpp: ginja (linked False)`, mwcc rule): GC/2.6 -nodefaults -proc gekko -align powerpc -enum int -fp hardware -Cpp_exceptions off -RTTI off -str reuse -char signed -use_lmw_stmw on **-O3,p -inline off -opt nopeephole** -lang=c++ (identical to kit compile.sh — proxy/official meters coincide, champ-echo fid-0 all three rungs).

## v4 ladder (this visit)
| rung | knob | official | one-shot | rows | verdict |
|---|---|---|---|---|---|
| r0 seed | v3 park tip verbatim | 97.45671 | 97.31602 | 119 | gate 0x738 ✓, census 39, DOL inert ✓, echoed BEFORE kit |
| r1 | permuter **round 7** re-rooted on r0 (BASE-VERIFY window-sha byte-ident `efa2a148…` proxy==repo, base score 1175 chain-law ✓, CHAMP-ECHO 97.31602 fid-0, 8765 iters ~9.4/s, 9 harvests, 2 clean) — `output-1125-3` **inline_fn2 helper split of py site** (f32+f32 add), hand-transplanted repo form `static inline` | **97.56493** | **97.42424** | 111 | LANDED d028bfc7; full battery green |
| r2 | permuter **round 8** re-rooted on r1 (BASE-VERIFY byte-ident `c5c98fd4…`, base score 1125 chain-law ✓, CHAMP-ECHO 97.42424 fid-0, 8553 iters ~9.2/s, 11 harvests, 3 clean) — `output-1065-1` **inline_fn23 helper split of ex-site sub** (Vec*-Vec* x-sub); 1065-2 alternate spelling codegen-IDENTICAL (same window-sha `cdfdd157…`) | **97.70563** | **97.56493** | 111 | LANDED 12782ea3; full battery green |

Kit budget consumed: 2/2 rounds (7+8), 2 promotions, 0 zeros. **WIN x2 re-arms the 2-chain** (v3 saturation armed on lone round-6 zero; chain RESETS — a round-9 zero is lone-zero, NOT closure). Zero2 CLOSURE limb did NOT fire.

## Residual at r2 (111 rows, final classification for v4)
- ~77 fp color-ring (SEALED — def-binding home ring; source-lever-inert; headroom to sub-100 official remains fp-ring dominated).
- 13 pool-name display (`lbl_805E10xx@sda21` vs `@NN@sda21`) — ACCEPTED class.
- ~21 pure-GPR renumber (era 7-slot window r25–r31; permuter re-homing territory — the only productive vein left, helper-split class has now landed 2/2 in-family).
- Helper-split vein inventory at tip: px (inline_fn), py (inline_fn2), ex (inline_fn23) already extracted; remaining sites (fx/fy/fz edge-loop subs) exist in body — round 9 can still mint helper winners; rows 119->111->111 with score +0.108/+0.141 (operand-match gains without slot-count change at r2).
- 97.5+ official target REACHED at r2 (97.70563). 100.0-paired gate-exact PR bar NOT met — park (unit UNLINKED, inert-only).

## Sealed datums added this visit
- **helper-split vein is the productive class at this seat**: round-7 top perm-cohort 1125 (x8) — 7/8 size-killed 0x73c, the ONE clean 1125-3 (mid) beat champ (+0.108); round-8 cohort 1065 (x2) + 1085 (x1) all clean, top 1065 pair beat champ (+0.141). PERMUTER-SCORE-INVERSION re-confirmed x2 (never rank by perm score; objdiff-clean only). POOL-@NN whitelist (bs_rank.py) kept — 0 newsym kills both rounds.
- **Transplant recipe scales**: harvest body + EVERY file-scope helper it calls, repo spelling `static inline f32 NAME(…) {…}` stacked after collisionRoot/inline_fn; proxy .o emits ZERO helper symbols (fully inlined), repo census stays 39; helper spelling `inline` vs `static inline` codegen-invisible (window-sha equality proxy<->repo all rungs: `efa2a148` r0, `c5c98fd4` r1, `cdfdd157` r2; skip=0x34+seat_off, count=1848).
- **Champion-echo fid-0 held 3/3**: proxy raw-objdiff echoes official one_shot EXACTLY (97.31602 / 97.42424 / 97.56493).
- **1065 cohort tie class**: two perm spellings of the same helper (Vec* arg vs f32 arg) emit the identical window — transplant any member, tiebreak by readability.

## Kit state after visit-5
- Kit dir retargeted REPO=f4; base.c = r2 body (round-8 winner) + 3-helper preamble (inline_fn, inline_fn2, inline_fn23), BASE-VERIFY byte-ident.
- VISIT-6 STARTER: next round = **round 9** (LONE-ZERO limb, not closure — WIN x2 reset the chain). Procedure unchanged: re-root base.c on repo tip (reroot_base.py + helper preamble: ensure ALL THREE helpers inline_fn/inline_fn2/inline_fn23 present in preamble before compiling base.c), BASE-VERIFY window-sha == `cdfdd157125c912f32d170cf83432ebe800235fe`, RE-ROOT PURGE (archive output-* incl. round-8 kept into archive-r8, rm -f base_direct.o output-*.o /tmp/bs_asm.*), `bs_round9.sh` (935s cap), rank `python3 bs_rank.py 9`. ZERO => lone-zero (kit stays ARMED, stop per law); WIN => promote + round 10 (zero2 re-arms closure candidacy).
- Archives: archive-r12/ (556), archive-r3/ (19), archive-r4/ (32), archive-r5/ (16), archive-r6/ (16), archive-r7/ (9 dirs + proxies). run1-8.log, harvest1/3/4/5/6/7/8.json kept.

## Battery at tip 12782ea3 (verbatim)
- full ninja rc=0 (`[4/8] REPORT, [5/8] LINK`, MWCC line seat rebuilt; link/DOL untouched).
- `python3 tools/report_delta.py cache/base_report_w74.json --check`: total_code 4353092->4353092 (+0); total_data 1760197->1760197 (+0); **New exact functions: 0; regressions: 0**; source_bearing_units 2965->2965 (+0); linked_units 2871->2871 (+0).
- `python3 tools/check_pr.py --no-build`: link_units check OK (2871 all exact); exact candidates to add: 2 (pre-existing config asks, integrator-side); regressed (drop): 0; **PASS**.
- DOL: `shasum build/GPOE8P/psov3.dol` = 0d85744b51d7379efb025a943d0cd5aaae2191a3 (inert, unit unlinked).
- Sibling safety (each promotion): llvm-nm -S census 39 defined; vs rung0 drift = ONLY pool-slot display labels @833->@837->@844->@848 (same addr/size family; pool-name ACCEPTED). 0 true-sym drift.
- Unit completeness: unit 99.08138 fuzzy, 23/25 functions exact; non-exact = TObjPlayer__sub_803DFB1C (other card) + test_box_sphere_contact (seat, official 97.70563, gate-exact). Seat UNLINKED => report rows inert-only.

## Files
- lane f4: `src/pso/player/TObjPlayer_803DF7A8.cpp` (r2 tip 12782ea3), `KIT_STATE.md` (this), `cache/base_report_w74.json` (base snapshot = w73, master tip seat row 96.02814), `cache/scratch` (host scratch): bs_v4_r0/r1/r2_oneshot.txt, bs_v4_r0/r1/r2_nm.txt, bs_v4_r1/r2_report_delta.txt, bs_v4_r2_checkpr.txt, w74_ninja_rung0.log, w74_ninja_full.log, w74_ninja_full2.log, w74_configure.log.
- kit: bs_round7.sh, bs_round8.sh, harvest7.json (2 clean), harvest8.json (3 clean), base.c = r2 root, bs_rank.py (pool whitelist kept).
