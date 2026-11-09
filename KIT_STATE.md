# Campaign: test_box_sphere_contact (TObjPlayer_803DF7A8 seat 0x803E112C) — v3 PARK receipt (visit-4)

- Lane: branch `card-boxsphere-v3`, tree `pso-decomp-f4`, base master `00cda35c`. v2 park tip (5bc98bdf/c6806347) seeded VERBATIM as rung0 `ec98a835` (blob-identity 72becc56 ✓).
- **Tip state: PARK at official 97.45671 / one_shot 97.31602, 119/462 rows, gate 0x738 exact, size 1848.** Unit UNLINKED (DOL inert `0d85744b51d7379efb025a943d0cd5aaae2191a3` ✓, linked_units grep 0 ✓, full ninja rc=0).
- PIN unchanged (GC/2.6 -O3,p -inline off -opt nopeephole -use_lmw_stmw on -fp hardware -char signed -lang=c++), kit retargeted REPO=f4 (compile.sh, bs_rank.py, bs_splice.py, reroot_base.py).

## v3 ladder (this visit)
| rung | knob | official | one-shot | rows | verdict |
|---|---|---|---|---|---|
| r0 seed | v2 park tip verbatim | 97.39178 | 97.25108 | 122 | gate 0x738 ✓, census-identical, report/DOL echoed BEFORE kit work |
| r1 | permuter **round 5** re-rooted on r9 (BASE-VERIFY window-sha byte-ident `a985e45f…`, base score 1205 chain-law ✓, 8915 iters, 8 harvests) — `output-1175-1` **inline_fn helper split of px site**, hand-transplanted to repo form (file-scope `static inline`, collisionRoot precedent) | **97.45671** | **97.31602** | 119 | LANDED 824b705d; full battery green |
| — | permuter **round 6** re-rooted on r1 (BASE-VERIFY byte-ident `efa2a148…`, base score 1175 chain-law ✓, 8995 iters, 8 harvests) | — | — | — | ZERO clean: 8/8 size-killed (0x73c). Lone zero => kit stays ARMED, stop per law |

Kit budget consumed: 2/2 rounds (5+6), 1 promotion. Hand rungs: 1 (r1 transplant). LONE-ZERO fired on round 6 — saturation NOT closed (needs 2 consecutive iters>0 zeros); visit-5 starter below.

## Residual at r1 (119 rows)
- ~77 fp color-ring (SEALED — def-binding home ring, era prologue-binds 0.025f@f4/0.0f@f5; never re-roll).
- 13 pool-name display (`lbl_805E10xx@sda21` vs `@NN@sda21`) — ACCEPTED class.
- ~25 pure-GPR renumber (era 7-slot window r25–r31; permuter re-homing territory).
- ~4 rotation/operand-swap (kit territory; r8/r9/r1 consumed 3 of ~8 — remaining tied to sealed fp-ring slots).
- Headroom to sub-100 official remains fp-ring dominated (source-lever-inert class). 97.5+ target NOT reached (97.45671); 100.0-paired gate-exact PR bar NOT met — park.

## Sealed datums added this visit
- **inline_fn-helper transplant class**: round-5 perm-best 1155 (x5) ALL size-killed 0x73c; mid-pack 1175 (x2) passed gate — PERMUTER-SCORE-INVERSION re-confirmed (v2 law: rank by objdiff-clean, never perm score). The 1175 pair dies as proxy-newsym (`@137/@138/@139` sdata2 slot display symbols) — POOL-UNIT CALIBRATION law applies: whitelist `^@\d+$` in the newsym screen, then score.
- **Harvest->repo transfer for helper class**: bs_splice.py extracts ONLY the seat fn — a harvest body calling a file-scope permuter helper NINJA-FAILs (`undefined identifier inline_fn`). Durable recipe: transplant = body + helper definition at file scope in repo spelling (`static inline f32 …`, mirrors existing collisionRoot precedent); proxy .o emits ZERO inline_fn symbol (fully inlined under -inline off at this site) -> repo census stable, DOL inert. Helper spelling `inline` vs `static inline` codegen-invisible (window-sha matched both sides).
- **Champion-echo fid-0**: proxy base_direct.o raw-objdiff echoes official one_shot EXACTLY (97.25108 r9, 97.31602 r1) — proxy offset 0.0 at this seat, both promotions.
- **f3 tree re-occupied**: f3 HEAD moved to card-80418d7c-v2 (co-editor lane); f3 worktree TObjPlayer file = older blob d58571d8, its .o window e84d8edbac ≠ committed-blob build a985e45fc. Cross-tree .o comparisons must hash-object-verify the SOURCE blob first (kit-reroot-drift law, third occurrence).
- v3 window-sha canon: r9 `a985e45fc552de996a019553ae0b778050af45f9`, r1 `efa2a148eb374f23bafcfa19652b308d54d61898` (proxy skip=52 count=1848 == official skip=0x34+0x1984 count=1848).

## Kit state after visit-4
- Kit `/Users/scott/Hermes/tools/perm-tests/TObjPlayer_803DF7A8_test_box_sphere_contact` retargeted REPO=f4; bs_rank.py newsym screen now whitelists pool `@NN`.
- base.c = r1 body (round-6 root), BASE-VERIFY byte-ident. Round-6 = LONE ZERO: kit stays ARMED.
- VISIT-5 STARTER: rounds 5+6 done; next round = **round 7** (zero2 candidate). Procedure: re-root on repo tip (fy-form body, add helper preamble line as done here), BASE-VERIFY window-sha == r1 window `efa2a148…` (or current tip window after re-measure), PURGE (archive output-* dirs incl. round-6 kept, rm -f base_direct.o /tmp/bs_asm.*), `bs_round7.sh` (935s cap), rank `python3 bs_rank.py 7`. CLOSURE limb: zero2 with triple-confirm (iters>0, healthy ~9/s velocity band, min-logged-score==base histogram) => saturation datum CLOSES kit vein for this seat; a WIN re-arms (2-chain rule).
- Archives: archive-r12/ (556), archive-r3/ (19), archive-r4/ (32), archive-r5/ (16), archive-r6/ (16). run1-6.log, rank1-4.out, harvest1/3/4/5/6.json kept.

## Battery at tip 824b705d (verbatim)
- full ninja rc=0 (MWCC line; 1 unit rebuilt, link/DOL untouched).
- `python3 tools/report_delta.py cache/base_report_w73.json --check`: total_code 4353092->4353092 (+0); total_data 1760197->1760197 (+0); **New exact functions: 0; regressions: 0**; source_bearing_units 2965->2965 (+0); linked_units 2871->2871 (+0).
- `python3 tools/check_pr.py --no-build`: link_units check OK (2871 all exact); exact candidates to add: 2 (pre-existing config asks, integrator-side); regressed (drop): 0; **PASS**.
- DOL: `shasum build/GPOE8P/psov3.dol` = 0d85744b51d7379efb025a943d0cd5aaae2191a3 (inert, unit unlinked).
- Sibling safety: llvm-nm -S census 39 defined, diff vs rung0 = ONLY pool-slot display label @833->@837 (same addr 0x78/size 0x12; pool-name ACCEPTED class). 0 true-sym drift.
- Unit completeness: unit 99.036606 fuzzy, 23/25 functions exact; non-exact = TObjPlayer__sub_803DFB1C (other card) + test_box_sphere_contact (seat, 119/462 rows, gate-exact). Seat UNLINKED => report rows inert-only.

## Files
- lane f4: `src/pso/player/TObjPlayer_803DF7A8.cpp` (r1 tip), `KIT_STATE.md` (this), `cache/base_report_w73.json` (base snapshot at master tip: seat row 96.02814), `cache/bs_v3_r0_oneshot.txt`, `bs_v3_r0_nm.txt`, `bs_v3_r1_oneshot.txt`, `bs_v3_r1_nm.txt`, `bs_v3_f3_r9_nm.txt`; ninja logs /tmp/w73_*.log.
- kit: bs_round5.sh, bs_round6.sh, harvest5.json (clean=[]), harvest6.json (clean=[]), bs_rank.py (pool whitelist), retargeted compile/splice/reroot to f4.
