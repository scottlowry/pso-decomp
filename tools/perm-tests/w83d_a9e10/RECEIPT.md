# w83d DOOR receipt — psov3/pso/unk/text_801A9CB8, seat TObjPlayer__sub_801A9E10

Date base: master 00cda35c (Merge PR #228), lane tree pso-decomp-f8, branch card-door-a9cb8-v1.

## Absorption screen (first)
- report.json pairing at tip (address-keyed): seat row size=876, NO fuzzy key = NO-PAIR. Unit stub (91 lines, twins only). NOT absorbed.
- Twins 100.0: __dt__13TUnk_804C349CFv 344B, get_photon_blast_chain 164B.

## Park-lineage sweep (git log --all --grep 801A9E10)
- Champions: f3 v3 91.15gate / f4 pass3 95.67fold (-1W parser-canonicalization wall) / f8 v1 90.30 / f8 92.92gate / **f8 95.87v2 (1e634c2a, GATE-EXACT 0x36C) DOMINANT** — gate-VERIFIED echo by recovery leg 9b5d869d on pkg tip 126fa504 (219/219 rows, zero decay).
- 4 leg commits (9b5d869d/ea430706/67803b98/9a8809e3) carry identical owner-file blob db8ee711.
- Drift precheck: `git diff 126fa504..00cda35c -- src/pso/unk/text_801A9CB8.cpp` = EMPTY (zero drift). Recovery legs live on wave14-pkg chain, NOT in master (merge-base screen) — seat open at master tip.

## Transplant rung (1 build)
- `git checkout 9b5d869d -- src/pso/unk/text_801A9CB8.cpp` (blob db8ee711 = post-remap champion; zero surgery needed at 00cda35c).
- rm -f unit .o; ninja -> MWCC line printed, rc=0.
- one_shot: ORIG/OURS paired 95.86758, size 876, rows 219/219 = park echo ZERO DECAY on master tip (survival datum).
- Gate: llvm-nm -S INT-parse OURS 0x36c = 876 = gate EXACT.
- Sibling safety (int-parse all 4 sized syms): __dt 344, __vt 24, get_photon_blast_chain 164 — all stable; twins 100.0 in linked report.json.

## Residual census at tip (20 diff rows / 219)
- lwzx/stwx indexed-with-addi-induction (era) vs add+lwz/stw-disp-fold (ours): 10 rows = def-binding fold stratum (G7 rung family; champion already realigns 3 addis in-loop).
- extsh r3,r3 (era in-place) vs extsh r0,r3 (fresh): EXTSH-BIND version stratum (1.0-1.2.5n in-place table; sealed).
- cmplwi vs cmpwi: sign-view row (def-binding).
- li/addi/cmpwi r10-vs-r8 color ring: allocation tiebreak.
- slots 158/159 subi/li order swap: tail-li layout mirror/scheduler order.
- Verdict: SAME classes as park seal (parser-canonicalization def-binding + EXTSH-BIND + scheduler). Wall has NOT moved at 00cda35c. NO re-roll. Sealed => park max-meter + visit-2 receipt.

## Battery (verbatim)
- Base snapshot: configure (repo-root venv python3.14) + full ninja rc=0 at 00cda35c; DOL 0d85744b51d7379efb025a943d0cd5aaae2191a3; cp report.json -> base_report_w83d_00cda35c.json.
- Post-transplant full ninja: RC=0 (Code 51356/51356, 141/141 functions; Data 6392/6392 100.00%).
- DOL post: 0d85744b51d7379efb025a943d0cd5aaae2191a3 (unit unlinked => DOL-inert; inertness window-sha + report_delta).
- report_delta base..tip --check: all counters +0, New exact functions: 0; regressions: 0 (fuzzy pairing moves no counters — seat 95.87 < 100).
- check_pr.py: PASS. link_units check OK 2871; linked now: 2871; exact candidates to add: 2 (unchanged); regressed 0; skipped 0.
- UNIT-COMPLETENESS: 2/3 fns 100.0, seat 95.86758, data 100.0, complete=False (unlinked door; linked_units row = config/integrator).

## Disposition
- Parked max-meter on master: 95.86758 gate-exact. Park label park/f8-a9e10@95.87m16 (this commit).
- visit-2 screen DONE: residual classes re-verified identical at tip; re-grind needs a NEW mechanism (def-binding/extsh-bind strata), do not card a grind without one.
