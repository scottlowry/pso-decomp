# w63d visit-2 receipt — TItemAttackCol (pso/weapon), park max-meter

Seat: psov3/pso/weapon/TItemAttackCol, open fn TItemAttackCol__ct @0x802E40AC gate 0x3A8 (936B).
Base: card-door-attackcol-v1 @ 00cda35c (origin/master), tracked-clean.
Base snapshot: cache/base_report_w63d.json, DOL sha256 1f80fb82b41c05b26b6d0545b1ba9c0aa60b52e6589cf32fbb2ffe644692a61a (build/GPOE8P/psov3.dol), full ninja rc=0.

## Measure-tip-first
- unitscan: main unit 12/13 fns, seat fuzzy None = COLD. fragments ALL-EXACT (1+5 fns).
- llvm-nm -S tip .o: `U TItemAttackCol__ct` (body absent). ORIG row size=936 gate-verified.
- tip unit .o sha256 101640fc16e16e9499a21a88044b2bf00ff50ed8862aac49bd09dff2d15b20e4.
- PIN: build.ninja:42017 mwcc GC/2.6 -O4,s -inline off -sdata2 4 -char signed -use_lmw_stmw on.

## Lineage screen
- git log --all -S: seeds 9d031714 (Oct-28 WIP 88.38), 4cf7049c/5429eb31 (88.36 drift probes),
  e1eb8325 champion body, 02aca24b v2 transplant @88.666664 (park f3-attackcol@88.67v2),
  6fdb302e disposition (park f7-attackcol@88.67swap). Owner-file blob lineage; real (no cache-artifact).
- Absorption: owner-file content drift 02aca24b^..HEAD = 7+/7- (#213 include reshuffle only, body region untouched)
  => gate-verified echo (cold tip, ORIG gate 936 exact) => transplant VERBATIM, zero re-roll.

## Rung table
| rung | commit | change | measure |
|---|---|---|---|
| 1 | a801542e | champion 02aca24b +153L fn-level patch, path-remap src/pso/item->src/pso/weapon, git apply rc=0 | __ct 88.666664 PAIRED (ORIG==OURS), nm gate 3a8 EXACT, 234/234 rows, decay 0 |

## Sealed datums (no re-roll, lane law f)
- Residual 26 rows = uniform r30<->r31 swap, opens at slot4/5 (mr r30,r3 / mr r31,r5):
  self<->init home-tie def-binding pin = mirror-tie/def-ring SEALED (park disposition 6fdb302e agrees).
- Floor 88.666664 reproduced on tip 00cda35c exactly (decay 0 x-park): era regalloc home assignment unreachable by 15-knob stratum per prior rosetta.

## Battery (verbatim)
- full ninja rc=0; psov3 Code 3983860/4111356, Data 89.34%; Dolphin/Runtime 100.00%.
- report_delta cache/base_report_w63d.json -> build: matched_functions +0, New exact 0, regressions 0, linked_units 2871+0.
- check_pr: PASS; link_units check OK (2871 linked units all exact); regressed 0.
- DOL post-build sha256 == base 1f80fb82... (byte-identical).
- DOL inertness: main unit NOT in linked_units.txt (grep: only _802E3AF4 line 2701, _802E4798 line 524) => park changes are unlinked-unit measures; inertness proved by DOL byte-identity + report_delta 0.

## Unit-completeness statement
psov3/pso/weapon/TItemAttackCol: 12/13 fns 100.0-paired, data 100.0; seat __ct floor 88.666664 SEALED (26 rows mirror-tie).
NOT PAIR-COMPLETE — unit cannot reach 13/13 by spelled classes; sealed floor, park max-meter, visit-2 done.
No new rows for integrator linked-row battery (unit unlinked; DOL unchanged).

## Files
- src/pso/weapon/TItemAttackCol.cpp (+153 champion body)
- cache/base_report_w63d.json, cache/w63d_champion.patch, cache/w63d_visit2_receipt.md
- No config, no linked_units, no push. Builds: 2 unit-rebuilds + 2 full ninja (budget 6+1 OK).
