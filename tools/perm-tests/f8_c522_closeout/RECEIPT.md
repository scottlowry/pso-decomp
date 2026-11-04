# fn_802855C4 v2 closeout (card t_8cfa38e2, lane f8, Nov-4, base e175bcd9)

## Status: FLOOR 98.39844 PAIRED, gate-exact 0x200 — sealed pin, disposition = park

## Seed survival
- Seed = true tip 7b40c522 (card-802855c4 v1, Nov-3, claimed 98.398).
- Fold-drift screen: `git diff e175bcd9 7b40c522 -- src/pso/misc/TWindowSubSymbolChatParts.cpp`
  = 46+/2-, 3 hunks, transplant-only (fwd-decl retype, fn body, call-site cast). Base file
  untouched by merge waves => survival expected.
- Control probe on committed tip 3b1e0100: rm .o + ninja (MWCC line, rc=0) +
  gnm = `000009c0 00000200 T fn_802855C4` (gate-exact) + one_shot PAIRED 98.39844.
- SURVIVAL: EXACT (98.398 == 98.39844 at the 4th digit).

## Residual census (46 diff rows of 128)
- 36 rows: UNIFORM 1-slot callee-int ring rotation. Era->ours = reg-1 over the whole
  callee span: {arg0 r25->r24, arg1 r26->r25, e0 r27->r26, e2 r28->r27, e1 r29->r28,
  row r30->r29, i r31->r30}. Identical instruction multiset; REAL:0.
- 2 rows (slots 42/45): RANK CARRIER — era `lis r23,0x4330; stw r23,0x8(r1)`
  (magO 176.0f magic-literal class bound BELOW bank, caller-saved scratch) vs ours
  `lis r31,0x4330; stw r31,0x8(r1)` (same class bound at bank TOP; the 8th in-span
  home pushes the 7 live classes down one slot = the ring above). Slot 70/75 second
  materialization follows the same mirror (era r24 spare-slot scratch, ours r23).
- 2 rows (slots 90/93): `(s8)*arg0->p78` byte read — era in-place coalesce
  `lbz r7,0(r7); extsb r7,r7` vs ours `lbz r0,0(r7); extsb r7,r0` (dest-coalescing
  class, 117e50-kin).
- 8 rows: `@NNN` pool display (lbl_8044FC08/805DD7D4/7DC/7E8 @NN vs lbl names) —
  byte-equal, link-gated display noise (same rows visible on run_task sibling, 99.9375,
  whose content rows are 100.0 pre-existing).

## Ring-class classification (from one_shot rows)
UNIFORM 1-slot swap (36/36 ring rows on the same -1 map) -> TWIN-RUNG FIRST executed.

## Twin-rung (ZERO-BUILD, decisive)
Committed 100.0 siblings decoded from our .o (= era decode, byte-exact):
- Twin fn_80285314 (688B): binds post-call bl-result class at bank TOP (mr r31,r3),
  magO class `lis r20,17200` bound BELOW bank — on twin terrain the bank is FULL
  (8 live homes r21..r31), so the scratch class is forced low, and our compiler
  reproduces era byte-exactly.
- In fn_802855C4 terrain the home count is 7 live (era) — MWCC 1.3-2.7 hands the
  free in-span slot r31 to the magO lis-dest class (top-down fill); era keeps that
  slot for the i counter and binds magO to r23/r24-spare (ascending low-const class).
DATUM: era's binding class is terrain-reachable (twin proves the low-const binding
exists byte-exactly in-unit), it is bound by HOME-COUNT/BIRTH-RANK, not by placement:
boxdrop v5 law ("matched twin's own body top-pins the same class => no seed-construct
transplant can flip it") transfers here — twin top-pins r31 for post-call class.

## Version rung (ZERO-BUILD rosetta, 20 GC versions, verbatim unit flags, fingerprint decode)
Table (size + slot-20/21/22/40/42 destinations):
- 1.0, 1.1, 1.1p1, 1.2.5, 1.2.5n: 0x180 MISS (fold stratum, -32 insns)
- 1.3, 1.3.2, 1.3.2r, 2.0, 2.5, 2.6 (pin), 2.7: 0x200 gate OK, ALL emit champion:
  arg1->r25, arg0->r24, row->r29, i->r30, lis r31 (magO in bank) — byte-identical at
  all five fingerprint slots across the whole gate family.
- 2.0p1: 0x1b8 MISS outlier. 3.0a3..3.0a5.2: 0x1e0 MISS collapse.
ERA binding set {arg0->r25, row->r30, i->r31, magO lis->r23}: ZERO emitters of 20.
Sealed era-scheduler-preference (ASK-1 memo kin: handle_box_drop_directive,
TObjPlayer__sub_80117E50, PanBARA slot-71).

## LI-ZERO-COPY / kin check (before any re-roll — passed, NO closed-spell re-roll run)
Era zeros materialize direct-to-home (li r30,0 / li r31,0 / mr rX,r0 copies); no
`li rX,0; mr rY,rX` adjacency anywhere in the residual -> ring is NOT the
parser-canonicalization zero-copy fold substrate. It is a def-binding rank
color-rotation (RA-PAIR/COPY-BIRTH-TOP-PIN lineage) => rank bisect is the admissible
lever class, decl/def/prop-off re-rolls closed-class (qvm-EDC20/dhcp census) — not re-run.

## Budget (cap: 4 probes + 2 builds; hard 6+1 teeth)
- 1 repo build (control transplant), 1 scored probe (control), 3 zero-build axes
  (twin decode, row census, 20-version rosetta). 1 build + 3 probes SPARED
  (reserve-aware stop: all residual rows closed-class: ring+magO = sealed pin (0/20),
  lbz coalesce = 117e50-class dest-coalescing, pool rows = link-gated).
- No bisect rung built: twin rung is non-transplantability seal per boxdrop v5;
  adding a phantom 8th live home to fill the bank would be inventing state era lacks
  (era is 7-home + spare) — a lie in the code, banned.

## Disposition
Champ = transplant commit (tip). Park branch card-802855c4-v2. Unit
TWindowSubSymbolChatParts INCOMPLETE-by-one: 18/20 fns 100.0 + run_task content-100
(3 display rows, link-gated) + fn_802855C4 floor 98.39844. linked_units 3310 unlock
requires byte-exact fn_802855C4; revival needs an era low-const scratch-binding
mechanism (era MAP / context-binding), do NOT re-roll decl/def/pragma grids.
