# Campaign: test_box_sphere_contact (TObjPlayer_803DF7A8 seat 0x803E112C) — v6 PARK receipt (visit-7)

- Lane: branch `card-boxsphere-v6`, tree `pso-decomp-f3`, base master `00cda35c`. v5 park tip code d655094a seeded VERBATIM as rung0 `935d3f91` (blob-identity d6117eb9 ✓, echo 98.225105/98.08442/1848 BEFORE kit).
- **Tip state: PARK at official 98.40909 (report row) / one_shot 98.268394, 80 diff-rows (462 orig), gate 0x738 exact, size 1848.** Unit UNLINKED (DOL inert `0d85744b51d7379efb025a943d0cd5aaae2191a3` ✓, linked_units untouched, full ninja rc=0 x3 rungs: base/r1/r2).
- Base snapshot: `cache/base_report_w89.json` (rung0 on seed, rc=0), logs `cache/w89_{configure,ninja_base,ninja_seat,ninja_r1,ninja_r2}.log`. PIN unchanged (kit compile.sh == ginja rule for seat).

## v6 ladder (this visit)
| rung | knob | official (report row) | one-shot | rows | verdict |
|---|---|---|---|---|---|
| r0 seed | v5 park tip d655094a verbatim | 98.225105 | 98.08442 | 87 | BASE-VERIFY window-sha `a4f77aaf…` byte-ident ✓, CHAMP-ECHO 98.08442 fid-0, census 39, DOL inert |
| r1 | permuter **round 11** re-rooted on r0 (base score 825 chain-law ✓, 9115 iters @9.75/s, 36 harvests, 30 clean) — `output-740-1` **fy decl reorder in edge loop** (fy after fx) | 98.38744 | **98.24675** | 81 | LANDED 889c5e79; full battery green |
| r2 | permuter **round 12** re-rooted on r1 (base score 740 chain-law ✓, ~9808 iters @10.5/s, 6 harvests, 3 clean) — `output-730-1` **FADD commutative swap in s denominator** ((ez*ez)+((ex*ex)+(ey*ey)) era-order) | **98.40909** | **98.268394** | 80 | LANDED facf1add; full battery green |

Kit budget consumed: 2/2 rounds (11+12), 2 promotions, 0 zeros. **WIN x2 — 2-chain stays ARMED, round 13 zero would be lone-zero (not closure). No closure datum this visit; kit vein stays OPEN.**

## Residual at r2 (80 rows, v6 classification)
- ~63 fp color-ring (SEALED — def-binding home ring; source-lever-inert).
- 13 pool-name display (`lbl_805E10xx@sda21` vs `@NN@sda21`) — ACCEPTED class.
- ~7 pure-GPR renumber (era 7-slot window; permuter re-homing territory).
- Helper-split vein: fy/fz edge-loop sites did NOT mint helpers x2 rounds; the wins came as decl-reorder (fy) and commutative-swap (s-denominator) classes. Vein class-shifted at r11 — the productive pool at this depth is ORDER/COMMUTATION, not extraction. fz reorder (735-1/2, 98.257576) and ex reorder (775-7) are banked runner-up shapes NOT fused (730-1 supersedes rows-wise).
- 100.0-paired gate-exact PR bar NOT met — park (unit UNLINKED, inert-only).

## Sealed datums added this visit
- **FADD-COMM-NULL refinement**: the sealed one-probe null was era=acc-LEFT; round-12 `output-730-1` WINS the commutative swap in the RIGHT subtree of `(ez*ez)+(…)` (+0.02164 one_shot, 81->80 rows). Commutation is seat-slot-specific, not globally null — probe at the exact slot before citing the seal.
- **PERMUTER-SCORE-INVERSION x6**: r11 winner perm 740 < base 825; r12 winner perm 730 < base 740 — winners keep landing below the base band.
- **PROXY-UNDERSHOOT/CONTEXT-FICTION receipts (r11/r12 repo-splice screens)**: `output-755-1` (collisionRoot->inline_fn23456 helper rename) proxy 98.20563 => repo EXACT champ tie 98.08442 (rename codegen-invisible); `output-735-2` (phantom `inline_fn23456` call in r12 cohort) NINJA-FAIL `undefined identifier` — dir-name-keyed leftovers from the r11 pool carry into later rounds; repo-splice decides, proxy never.
- **Champion-echo fid-0 held 7/7** (…, 98.08442 / 98.24675 / 98.268394): proxy raw-objdiff echoes official one_shot EXACTLY at every root.
- REROOT-HELPER TRAP: no new helpers landed (no inline_fn* minted in v6) — preamble stable at 5 helpers; law check (grep body for inline_fn* calls) passed at every re-root.

## Kit state after visit-7
- base.c = r2 body (round-12 winner) + 5-helper preamble (inline_fn, inline_fn2, inline_fn23, inline_fn234, inline_fn2345), BASE-VERIFY window-sha `61ede0aa1e19baba35360d4e11d55c545934d0f3` byte-ident proxy<->repo (462 words), CHAMP-ECHO 98.268394 fid-0.
- VISIT-8 STARTER: next round = **round 13**. Procedure: re-root base.c on repo tip (no helper additions needed unless a win mints one), BASE-VERIFY window-sha == `61ede0aa…`, RE-ROOT PURGE (archive output-* -> archive-r13, rm -f base_direct.o output-*.o /tmp/bs_asm.*; `find -H /tmp -maxdepth 1 -name 'perm*' -exec rm -rf {} +` — graveyard was 2.17M dirs at visit start, 0 after; re-check count before launch), `bs_round13.sh` (935s cap), rank `python3 bs_rank.py 13`. ZERO => lone-zero (kit stays ARMED, chain counter zero1); WIN => promote + round 14.
- w89_verify.py (kit dir): window-sha + CHAMP-ECHO + report-row one-shot checker, arg = rung label.
- bs_splice.py RETARGETED f4->f3 (was stale — fired silently on first use, fixed at round-11 promotion).
- Archives: archive-r12 (556, era), r3-r9 (v5-era), archive-r10 (17), archive-r11 (36), archive-r12-v6 (6). run1-12.log, harvest1/3/4/5/6/7/8/9/10/11/12.json kept.

## Battery at tip facf1add (verbatim)
- full ninja rc=0 (8 steps, `[4/8] REPORT`, `[5/8] LINK build/GPOE8P/psov3.elf` in cache/w89_ninja_r2.log; MWCC seat line fired at splice ninja).
- `python3 tools/report_delta.py cache/base_report_w89.json build/GPOE8P/report.json --check`: total_code 4353092->4353092 (+0); total_data 1760197->1760197 (+0); **New exact functions: 0; regressions: 0**; source_bearing_units 2965->2965 (+0); linked_units 2871->2871 (+0).
- `python3 tools/check_pr.py --no-build`: link_units check OK (2871 all exact); exact candidates to add: 2 (pre-existing config asks); regressed (drop): 0; **PASS**.
- DOL: shasum build/GPOE8P/psov3.dol = 0d85744b51d7379efb025a943d0cd5aaae2191a3 (inert, unit unlinked).
- Sibling safety (each promotion): llvm-nm -S census 39 def-lines; FB1C `TObjPlayer__sub_803DFB1C` size 0x11AC present seed->tip (parked state untouched, boxesphere-seat-only ownership). 0 true-sym drift.
- Unit completeness: unit fuzzy 99.20795 (was 99.17484 at v5 tip), 23/25 functions matched; non-exact = FB1C (parked) + test_box_sphere_contact (seat, official 98.40909, gate-exact). Seat UNLINKED => report rows inert-only.

## Files
- lane f3: `src/pso/player/TObjPlayer_803DF7A8.cpp` (tip facf1add), `KIT_STATE.md` (this), `cache/base_report_w89.json`, `cache/w89_{configure,ninja_base,ninja_seat,ninja_r1,ninja_r2}.log`; host scratch: bs_v6_r0_oneshot.txt, w89_r1_nm.txt, w89_r2_nm.txt.
- kit: bs_round11.sh, bs_round12.sh, w89_verify.py, harvest11.json (30 clean), harvest12.json (3 clean), base.c = r2 root, bs_splice.py retargeted f3.
