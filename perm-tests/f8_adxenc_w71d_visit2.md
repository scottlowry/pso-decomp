# card w71d (f8 lane, card-door-adxenc-v1) — adx_encode_available_blocks visit-2 — max-meter park — Nov-9

Base: 00cda35c (master tip, tree tracked-clean). Tree: pso-decomp-f8.
Gate (row is truth): report row psov3/pso/audio/AdxEncoder adx_encode_available_blocks
addr 0x803C7978 size 664 (0x298, 166i). Unit 15/16 fns, DATA 100.0 (8272/8272), unit UNLINKED.
Pin (live-cited build.ninja:55321-55330): GC/2.6 -O4,p -inline off, linked False.

## Measure-tip (zero-change rebuild)
rm -f build/GPOE8P/src/pso/audio/AdxEncoder.o && ninja (MWCC line) rc=0.
llvm-nm -S (Xcode, INT-parse): adx_encode_available_blocks = 0x298 == row GATE-EXACT;
16/16 unit syms sizes == report rows (reg-0 structural, siblings 0 drift).
one_shot_diff: 98.07229, size 664==664, rows 166/166, 49 diff slots (rows file f8_adxenc_w71d_rows.txt).

## Residual anatomy (programmatic census)
All 49 diff slots = ONE consistent register permutation, zero mnemonic/immediate/structural/slot
deltas: era->ours r20->r25 (9), r21->r20 (11), r22->r21 (8), r23->r22 (6), r24->r23 (3),
r25->r24 (11, main region) and r25->r19 (6, tail pool-store loop counter).
= def-binding bind-to-home color ring = SEALED def-ring class (lane law (f) never-re-roll;
kin datum: a8b4 rosetta c503dc95 "era ring emitted by ZERO versions, all 15 gate-size emitters
rotate identically to pin 2.6"; visit-1 receipt names this exact residual "def-binding
bind-to-home ring (a8b4 kin, no-2nd-visit law)").
Ring rotation via source spelling at -O4,p is the sealed stratum; NO rung rolled (sealed NEVER
re-roll). tiebreak DO-NOT-GRIND respected.

## Park-lineage screen (git log --all -S name + -S 803C7978)
Seeds (owner-file blobs): b39bf140 v1 transcribe (+1W @0x29C, gate-MISSING);
f3-encode-v2 chain f37d6b1c/6120ccaf/1bec08e5/2fedcceb -> disposition 67270d4f
(receipt perm-tests/f3_adxr_encode_v2_floor.md on card-adxr-encode-v2):
v6 seed 86.93374 GATE-EXACT [park shipped tip]; v8 90.92771 @0x294 -1W; P1 90.945786 @0x294 -1W
(i binds r19 EXACT); P2/P3 inert; P4 89.981926 reject. LI-ZERO-COPY FOLD class (5 seam spellings
all fold mr r19,r25 -> li r19,0; prop-off DEAD, census 13).
ABSORPTION VERDICT (zero-build): measure-tip 98.07229 GATE-EXACT dominates every park rung
(+11.14pp over park official best v6, +7.13pp over gate-missing P1). Park echo = receipt meters
reproduced as recorded. NO transplant (tip body is master-resident via ae797d39 Matchpass 15,
which already resolved the gate + zero-share + most of the ring).

## Battery (base snapshot build/GPOE8P/base-w71d-00cda35c.json)
ninja rc=0 (Code 51356/51356 bytes, 141/141 functions; Data 6392/6392 100.00%).
report_delta base..tip --check: complete_data +0, total_functions +0, New exact 0, regressions 0,
linked_units 2871->2871, rc=0.
check_pr.py: PASS; link_units check OK (2871 exact); regressed (drop) 0.
DOL build/GPOE8P/psov3.dol sha1 0d85744b51d7379efb025a943d0cd5aaae2191a3 == main
(unit UNLINKED (grep linked_units.txt: no AdxEncoder row) => DOL-insensitive, inertness proven
at unit-.o/report_delta level per DOL caveat).

## KIT-ELIGIBILITY screen (NO kit run)
166i < 400i lifecycle threshold (3cdeb200 law) => kit-INELIGIBLE; residual is pure 6-reg ring
rotation at a 166i gate — permuter EV below lifecycle floor. No permuter call.

## Verdict
Seat floored at 98.07229 GATE-EXACT (unit 99.8696 fuzzy, 15/16). Residual 49 rows = sealed
def-ring. Max-meter park; visit-2 receipt per no-2nd-visit law. Unit NOT pair-complete
(15/16): sub-100 seat = ledger inventory, not a linked-row unlocker (unit also unlinked).
Files: this receipt + f8_adxenc_w71d_rows.txt. No push, no config, no kit, no linked_units edit.
