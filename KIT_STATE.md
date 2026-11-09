# Campaign: test_box_sphere_contact (TObjPlayer_803DF7A8 seat 0x803E112C) — v7 PARK receipt (visit-8)

- Lane: branch `card-boxsphere-v7`, tree `pso-decomp-f3`, base master `00cda35c`. v6 r2 tip facf1add seeded VERBATIM as rung0 `52ba7adf` (blob-identity f7dfee57 ✓, echo 98.40909/98.268394/1848 BEFORE kit).
- **Tip state: PARK at official 98.48485 (report row) / one_shot 98.344154, 80 diff-rows (462 words), gate 0x738 exact, size 1848.** Unit UNLINKED (DOL inert `0d85744b51d7379efb025a943d0cd5aaae2191a3` ✓, linked_units untouched, full ninja rc=0 all rungs).
- Base snapshot: `cache/base_report_w93.json` (rung0, rc=0), logs `cache/w93_{configure,ninja_base,ninja_r13,ninja_r14}.log`.

## v7 ladder (this visit)
| rung | knob | official (report row) | one-shot | rows | verdict |
|---|---|---|---|---|---|
| r0 seed | v6 r2 tip facf1add verbatim | 98.40909 | 98.268394 | 80 | BASE-VERIFY window-sha `61ede0aa…` byte-ident ✓, CHAMP-ECHO 98.268394 fid-0, census 39, DOL inert |
| r1 | permuter **round 13** re-rooted on r0 (base score 730 chain-law ✓, ~10,678 iters @935s cap, 11 harvests… 10 kept, 4 clean) — `output-725-1` **u8* new_var3 hoist + fx-before-fz decl reorder** | 98.419914 | **98.27922** | 80 | LANDED 684d8196; repo-splice x3 confirm (725-1/2/4 all 98.27922; 725-3 NINJA-FAIL inline_fn23456 leftover) |
| r2 | permuter **round 14** re-rooted on r1 (base score 725 chain-law ✓, ~10,663 iters, 11 harvests, 3 clean) — `output-695-1` **fy site helper-mint inline_fn23456 ((ey*s)+a->y)** + preamble add | 98.48485 | **98.344154** | 80 | LANDED 02f51511; full battery green |

Kit budget consumed: 2/2 rounds (13+14), 2 promotions, 0 zeros. **WIN x2 — CHAMP-ECHO chain 9/9, kit stays ARMED. No closure datum; vein OPEN.**

## Residual at r2 (80 rows)
- ~63 fp color-ring (SEALED). 13 pool-name display (ACCEPTED). ~7 pure-GPR renumber.
- Helper-split vein RE-ARMED: round 14 minted `inline_fn23456` at the fy site (+0.064932 one_shot — biggest single beat of the chain). fx site was already minted (inline_fn2345); **fz site analog (720-1 shape `(ez*s)+a->z` -> helper) scored 98.29005 proxy and FAILED raw-splice only for missing preamble — mint-eligible next visit. 705-1 (mass y-chain helper fan) same class.**
- Round-13 class recap: reorder+hoist wins (725-1/2/4 identical scores — pick canonical 725-1).

## Sealed datums added this visit
- **HELPER-MINT SPAWN**: fy-site extraction wins big (+0.065) after two no-helper rounds — the v6 "CLASS-SHIFTED to order/commutation" claim is superseded: extraction productivity returned at the (ey*s)+a->y slot specifically. Slot-specificity law stands (probe the exact slot).
- **PERMUTER-SCORE-INVERSION x7/x8**: r13 winner 725 < base 730; r14 winner 695 < base 725 — winners keep landing below base band; rank objdiff-clean only.
- **POOL-@NN carryover receipts**: r14 NINJA-FAIL `inline_fn23456` in 725-3/695-1/705-1/720-1 raw splices = r11-era pool dir-names; fix = hand-mint helper in preamble + repo file (bs_splice maps body only).
- **Champion-echo fid-0 held 9/9** (…, 98.268394 / 98.27922 / 98.344154).

## Kit state after visit-8
- base.c = r2 body + **6-helper preamble** (inline_fn, 2, 23, 234, 2345, 23456), BASE-VERIFY window-sha `c32ab845b71c5e769da51f7b344fbef1f664dfcd` byte-ident proxy<->repo (462 words), CHAMP-ECHO 98.344154 fid-0.
- VISIT-9 STARTER: **round 15**. Procedure: re-root base.c on repo tip 02f51511 (git show; window-sha == c32ab845…), RE-ROOT PURGE (archive output-* -> archive-r15; `find -H /tmp -maxdepth 1 -name 'perm*' -exec rm -rf {} +`; 0 at visit end), `bs_round15.sh` (935s cap, sed from bs_round14.sh), rank `python3 bs_rank.py 15`. ZERO => lone-zero (kit ARMED, zero1); WIN => promote + round 16 (budget 2/2 max). If a win references inline_fn234567 (705-1 class), mint via hand-patch — bs_splice will NINJA-FAIL it raw.
- Archives: archive-r13 (10), r14 (22 incl. splice temps), r12 (556 era), r3-r12-v6 (v5/v6 era). run1-14.log, harvest1/3-14.json kept.
- w89_verify.py arg = rung label; reads kit base_direct.o vs repo seat .o.

## Battery at tip 02f51511 (verbatim)
- full ninja rc=0 (cache/w93_ninja_r14.log; `[4/9] MWCC build/GPOE8P/src/pso/player/TObjPlayer_803DF7A8.o`).
- report_delta cache/base_report_w93.json: total_code 4353092->4353092 (+0); total_data 1760197->1760197 (+0); New exact functions: 0; regressions: 0; source_bearing_units 2965->2965; linked_units 2871->2871.
- check_pr.py --no-build: PASS (2 pre-existing exact candidates, 0 regressed).
- DOL shasum = 0d85744b51d7379efb025a943d0cd5aaae2191a3 (inert, unlinked).
- Sibling safety: llvm-nm -S census 39 def-lines; FB1C `TObjPlayer__sub_803DFB1C` 0x11AC intact (static-inline helpers emit no new symbols).
- Seat: one_shot 98.344154, report row 98.48485, gate 0x738 exact, size 1848.

## Files
- lane f3: `src/pso/player/TObjPlayer_803DF7A8.cpp` (tip 02f51511), `KIT_STATE.md` (this), `cache/base_report_w93.json`, `cache/w93_*.log`.
- kit: bs_round13.sh, bs_round14.sh, harvest13.json (4 clean), harvest14.json (3 clean), base.c = r2 root (6 helpers).
