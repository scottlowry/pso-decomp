# Campaign: test_box_sphere_contact (TObjPlayer_803DF7A8 seat 0x803E112C) — v5 PARK receipt (visit-6)

- Lane: branch `card-boxsphere-v5`, tree `pso-decomp-f3`, base master `00cda35c`. v4 park tip (12782ea3) seeded VERBATIM as rung0 `f8bdf224` (blob-identity 902d6fa7 ✓, echo 97.70563/97.56493/1848 BEFORE kit).
- **Tip state: PARK at official 98.225105 / one_shot 98.08442, 87 diff-rows (462 orig), gate 0x738 exact, size 1848.** Unit UNLINKED (DOL inert `0d85744b51d7379efb025a943d0cd5aaae2191a3` ✓, linked_units untouched, full ninja rc=0 x3 rungs).
- PIN live-cited (kit compile.sh identical to repo ginja rule for seat, `# pso/player/TObjPlayer_803DF7A8.cpp: ginja (linked False)`): GC/2.6 -nodefaults -proc gekko -align powerpc -enum int -fp hardware -Cpp_exceptions off -RTTI off -str reuse -char signed -use_lmw_stmw on **-O3,p -inline off -opt nopeephole** -lang=c++ (proxy==official meters coincide, champ-echo fid-0 all rungs).

## v5 ladder (this visit)
| rung | knob | official | one-shot | rows | verdict |
|---|---|---|---|---|---|
| r0 seed | v4 park tip verbatim | 97.70563 | 97.56493 | 111 | BASE-VERIFY cdfdd157 ✓, census 39, DOL inert ✓, echoed BEFORE kit |
| r1 | permuter **round 9** re-rooted on r0 (BASE-VERIFY window-sha byte-ident `cdfdd157…` proxy==repo, base score 1065 chain-law ✓, CHAMP-ECHO 97.56493 fid-0, ~9110 iters, 13 harvests, 9 clean) — `output-905-1` **inline_fn234 helper split of pz site** (center->z + t*n->z), repo form `static inline` | (row not captured mid-visit) | **97.90044** | 91 | LANDED 27bbc36a; full battery green |
| r2 | permuter **round 10** re-rooted on r1 (BASE-VERIFY byte-ident `f3a76ccd…`, base score 905 chain-law ✓, CHAMP-ECHO 97.90044 fid-0, ~9024 iters, 17 harvests, 10 clean) — `output-825-1` **inline_fn2345 helper split of fx site** ((ex*s)+a->x), repo form `static inline` | **98.225105** | **98.08442** | 87 | LANDED d655094a; full battery green |

Kit budget consumed: 2/2 rounds (9+10), 2 promotions, 0 zeros. **WIN x2 keeps the 2-chain ARMED — a round-11 zero is lone-zero (chain reset by wins), NOT closure.** Zero2 CLOSURE limb did NOT fire; kit vein stays OPEN (round-9 lone-zero limb was never exercised).

## Residual at r2 (87 rows, v5 classification)
- ~64 fp color-ring (SEALED — def-binding home ring; source-lever-inert; headroom to sub-100 official remains fp-ring dominated).
- 13 pool-name display (`lbl_805E10xx@sda21` vs `@NN@sda21`) — ACCEPTED class.
- ~10 pure-GPR renumber (era 7-slot window r25–r31; permuter re-homing territory).
- Helper-split vein inventory at tip: px (inline_fn), py (inline_fn2), ex (inline_fn23), pz (inline_fn234), fx (inline_fn2345) extracted; **fy/fz edge-loop sites remain mintable** — vein 5-for-5 landing, rows 111->91->87 with official +0.38/+0.14.
- 98.0 official target REACHED at r2 (98.225105). 100.0-paired gate-exact PR bar NOT met — park (unit UNLINKED, inert-only).

## Sealed datums added this visit
- **helper-split vein 5/5**: every round's winner since r7 is a file-scope `static inline` helper extraction (py, ex, pz, fx sites in order). PERMUTER-SCORE-INVERSION x4 (round-9 WINNER perm score 905 = bottom of cohort band, beats 1015/1025 perm-best band; round-10 winner 825 < base 905 — rank objdiff-clean ONLY, perm band ordering is anti-correlated at this seat).
- **REROOT-HELPER TRAP CONFIRMED x2**: `reroot_base.py` splices the repo body over the OLD preamble; any helper newly landed in the repo (inline_fn234, inline_fn2345) is MISSING from base.c after re-root -> proxy compile dies `undefined identifier`. Law: after EVERY re-root, grep body for `inline_fn*` calls and ensure EVERY one has a preamble definition before compiling base.c (v4 law named 3 helpers; generalizes to N).
- **Champion-echo fid-0 held 5/5** (97.31602 / 97.42424 / 97.56493 / 97.90044 / 98.08442): proxy raw-objdiff echoes official one_shot EXACTLY. One per commit message: r1/r2 commit lines quote the one_shot meter in both "one_shot / official" slots — the report-row official at r1 was not captured mid-visit; tip official measured = 98.225105 (one_shot 98.08442, +0.14 slot-restore gap, consistent with seed's 97.70563/97.56493).
- Transplant recipe unchanged: harvest body + every file-scope helper it calls, repo spelling `static inline f32 NAME(…) {…}` stacked after the last helper; proxy .o emits ZERO helper symbols (fully inlined), repo census stays 39 def-lines.

## Kit state after visit-6
- Kit dir retargeted REPO=f3 (reroot_base.py, compile.sh, bs_rank.py sed f4->f3). base.c = r2 body (round-10 winner) + 5-helper preamble (inline_fn, inline_fn2, inline_fn23, inline_fn234, inline_fn2345), BASE-VERIFY byte-ident `a4f77aaf13319670125390172462f0d7ff8c3dcf`, CHAMP-ECHO 98.08442 fid-0.
- VISIT-7 STARTER: next round = **round 11** (lone-zero limb, not closure — WIN x2 reset the chain). Procedure unchanged: re-root base.c on repo tip, ADD any newly-landed helpers to the preamble (grep law above), BASE-VERIFY window-sha == `a4f77aaf13319670125390172462f0d7ff8c3dcf`, RE-ROOT PURGE (archive output-* into archive-r10, rm -f base_direct.o output-*.o /tmp/bs_asm.*; find -H /tmp for mktemp churn — /tmp is a SYMLINK, plain find doesn't descend), `bs_round11.sh` (935s cap), rank `python3 bs_rank.py 11`. ZERO => lone-zero (kit stays ARMED, stop per law; chain counter: zero1); WIN => promote + round 12 (zero2 re-arms closure candidacy).
- Archives: archive-r12 (556), r3 (19), r4 (32), r5 (16), r6 (16), r7 (9), r8 (24), r9 (26 items). run1-10.log, harvest1/3/4/5/6/7/8/9/10.json kept. output-* dirs at tip = round-10 harvests (17, incl. winner 825-1).

## Battery at tip d655094a (verbatim)
- full ninja rc=0 (`MWCC build/GPOE8P/src/pso/player/TObjPlayer_803DF7A8.o`, REPORT, LINK lines present in cache/w84_ninja_r2.log).
- `python3 tools/report_delta.py cache/base_report_w84.json build/GPOE8P/report.json --check`: total_code 4353092->4353092 (+0); total_data 1760197->1760197 (+0); **New exact functions: 0; regressions: 0**; source_bearing_units 2965->2965 (+0); linked_units 2871->2871 (+0).
- `python3 tools/check_pr.py --no-build`: link_units check OK (2871 all exact); exact candidates to add: 2 (pre-existing config asks); regressed (drop): 0; **PASS**.
- DOL: `shasum build/GPOE8P/psov3.dol` = 0d85744b51d7379efb025a943d0cd5aaae2191a3 (inert, unit unlinked).
- Sibling safety (each promotion): powerpc-eabi-nm -S census 39 def-lines; drift = ONLY pool-slot display labels @848->@852->@856 (same addr 0x78/size 0x12 family; pool-name ACCEPTED). 0 true-sym drift. FB1C `TObjPlayer__sub_803DFB1C` present at seed AND tip with size 0x11AC (seed carried the parked FB1C body; no add/remove — boxesphere-seat-only file ownership respected).
- Unit completeness: unit fuzzy 99.17484 (was 99.08138 at v4 tip), 23/25 functions matched; non-exact = TObjPlayer__sub_803DFB1C (parked 0x11AC state) + test_box_sphere_contact (seat, official 98.225105, gate-exact). Seat UNLINKED => report rows inert-only.

## Files
- lane f3: `src/pso/player/TObjPlayer_803DF7A8.cpp` (r2 tip d655094a), `KIT_STATE.md` (this), `cache/base_report_w84.json` (base snapshot = rung0 seed on master 00cda35c), `cache/w84_{configure,ninja_base,ninja_r1,ninja_r2}.log`, host scratch: bs_v5_r0/r1/r2_oneshot.txt, bs_v5_r1/r2_report_delta.txt, bs_v5_r1/r2_checkpr.txt, w84_r{0,1,2}_nm.txt.
- kit: bs_round9.sh, bs_round10.sh, harvest9.json (9 clean), harvest10.json (10 clean), base.c = r2 root, bs_rank.py (pool whitelist kept), reroot_base.py/compile.sh retargeted to f3.
