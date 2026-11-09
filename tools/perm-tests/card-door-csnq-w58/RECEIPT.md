# card-door-csnq-w58 — CsnQuery door lane: verified park tip landed verbatim on master tip; sealed ceiling re-affirmed

Seat: `evaluate_ground_triangles` (0x800791BC), unit `psov3/pso/map/CsnQuery`, owner `src/pso/map/CsnQuery.cpp`.
Base: master tip `00cda35c` (branch `card-door-csnquery-v1`), tip after rung0 = `9e9694cc`.
Budget: 1 grind + 1 confirm of 6+1 (~35 min of 120). NO grind beyond transplant.

## Lineage (brief premise (m) REFUTED)
Brief said "no park lineage for CsnQuery; likely net-home/virgin". `git log --all -S 800791BC`
shows REAL seeds with battery receipts, NOT cache census artifacts:
- `park/f8-csq@83.31crown` (ef8656ff; content b3a06cf2, fork+scott remotes) = 83.3112 @ gate-exact 0x3C4
- `card-csnq-m13` e20ee751 (+twin ec9f81b5): park floor landed on f8 chain 71f56516 (721e0b3e base),
  full battery, "gate-verified echo beats self-declared rung, lands with NO re-roll" doctrine applies.
- f7 chain: 1cf1996c (floor 83.06224), 394a2bbf (v2 seed).

## STEP-0 + intake screens (zero-build)
- Report row at tip: present at era size 964, NO fuzzy/matching keys = UNPAIRED (body absent;
  decl :135 + call sites :733-758 only) -> pairing-break census = body ABSENT at master tip.
- Gate RE-READ: config/GPOE8P/psov3/symbols.txt:3115 `size:0x3C4` = 964B / 241 insns.
- Drift pre-check: `git diff 721e0b3e..00cda35c -- CsnQuery.cpp + header` = ZERO lines;
  HEAD blob 31ef3d0b == m13 parent blob (71f56516/721e0b3e) -> pure verbatim git-show copy (m9 method).
  Delta +166/-1 == m13 receipt exactly (-1 = champion pad0[0x14] restage in Poly_80079F58).
- Pin VERIFIED live build.ninja:4586-4595: GC/2.6 -O4,s -char signed -use_lmw_stmw on -inline off
  -sdata2 4 -str reuse; unit `linked False` (linked_units.txt grep rc=1) -> DOL-insensitive class.

## Battery (all rc captured on redirected logs)
- rm .o + ninja unit rc=0 (MWCC line printed). .o sha1 012f4ae3e12d7c24814ed1e0f6c0688bbb534520.
- llvm-nm -S int-parse: T 26->27, added = seat ONLY, sibling size-drift 0, seat 0x3c4 GATE-EXACT.
- one_shot PAIRED ORIG=OURS 83.3112, sizes 964/964, rows 241/241 = park echo ZERO decay; 26/26 siblings 100.0.
- full ninja rc=0; link 141/141 Code, Data 100.00%.
- report_delta.py cache/base_report_w58.json build/GPOE8P/report.json --check rc=0:
  New exact 0 / regressions 0; matched_functions 27432 +0; matched_data +0 (seat data bytes already
  counted at current master — wave-merge provenance, unlike m13's +88 over 721e0b3e); linked_units 2871 +0.
- check_pr.py PASS rc=0: linked 2871, regressed 0, skipped 0, exact candidates 2 (known non-config class);
  link_units check OK (2871 all exact, embedded in check_pr).
- DOL byte-identical 0d85744b51d7379efb025a943d0cd5aaae2191a3 lane == main checkout (unlinked, metric-only).
- Meters: unit fuzzy 81.988045 -> 97.524666 (+15.54); report seat row PAIRED 86.25726 (address-resolved;
  one_shot 83.3112 = unit-view echo).

## Residual — sealed ceiling (rows read, 206 diff slots of 241)
Era clear-site slots 12-16: `li r0,0x0 / lis r7,pool@ha / stwu r0,pool@l(r7) / mr r19,r5 / lis ...@ha`
vs ours `lis;mr;addi;li;stw` = def-binding bank rotation + stwu-deferral class (f7 1cf1996c, m13).
Spelled successor rung (stwu-fusion transfer per text_803D31A4 self-emitter) is BLOCKED by the
sda21 def-size gate at pin 2.6 -O4,s = sealed class lane-law (f) "SDA21 fold pin 2.6 -O4,s"
(lands only at 2.6 -O3,p — player r1 proof). NO re-roll per sealed-never-reroll law.
Trio window inert+gate-kill (m13 census inherited). Ladder clause: rung 1 is not spelled by ROWS
at this pin -> close at rung 0.

## Door / unit completeness
26/27 fn-exact + seat paired 83.3112 (gate-exact size). NOT pair-complete (byte-exact seat required)
-> linked_units row NOT earned; door stays shut; config/linked-row side = integrator, lane never
touched config/**. No PR material (PR bar = seat byte-exact 100.0 paired; this is max-meter park).

## Visit-2 receipt
Only path to byte-exact = sda21-def-size-gate transfer of the proven stwu-fusion emitter, which needs
a pin/config change (2.6 -O3,p stratum) = integrator key, not a source lever at -O4,s.
If integrator ever re-pins, re-run census FIRST: slots 12-16 fused clear-site is the first row to check.

Co-editor disclosure: w57 twin (AdxStreamRuntime), M5U particle/player lanes — disjoint files, no shared hunks.
