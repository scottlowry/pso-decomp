# ffb84 v1 census receipt (f3 card-803ffb84-v1, base 00cda35c, Nov-8)

Seat: TLobby__sub_803FFB84 = .text:0x803FFB84, size 0x5F0 (1520B, 380 insns).
Gate-from-ROW verified: config/GPOE8P/psov3/symbols.txt:27421
`TLobby__sub_803FFB84 = .text:0x803FFB84; // type:function size:0x5F0`.
Era .fn block: build/GPOE8P/asm/pso/network/TLobby_803FCF44.s lines 3333-3781 = 380 insns.
llvm-nm -S OURS: 00002c40 000005f0 T = GATE-EXACT at tip.
Unit: psov3/pso/network/TLobby_803FCF44 (net home src/pso/network/TLobby_803FCF44.c,
body lines 2632-2874, preceded by function-window `#pragma push/opt_lifetimes off/pop`).
linked False (verified this visit: grep count 0 in config/GPOE8P/psov3/linked_units.txt)
=> DOL-insensitive; inertness = unit .o sha + report_delta regressions 0.
Pin (live build.ninja rows 57943-57949): GC/1.2.5n -char signed -use_lmw_stmw on
-O4,p -inline off -opt nocse -lang=c.

## MEASURE-TIP-FIRST
rm unit .o + ninja (MWCC line printed); one_shot on committed tip:
ORIG/OURS match=99.30526 size=1520/1520, rows 380/380, 50 diff rows.
Body PRESENT (absorbed by #213 migration 76d99c97, decompiler port).

## PAIRING-BREAK census
Ours unit .text total = 0x79A4 (118 T/t syms, int-parsed gnm) = era total EXACT
(fe6cc-v1 receipt datum re-derived). No missing body, no mis-split, stub count 0.

## Residual row taxonomy (50 rows, 4 classes)
Era home stack (7 callee saves, frame 0x40, stmw r25@0x24):
{p:r25, hdr:r26, c:r27, res:r28, len:r29, self:r30, a:r31}.
Tip home stack (8 callee saves, stmw r24@0x20):
{p:r24, hdr:r25, c:r26, SWITCHVAL:r27, res:r28, len:r29, self:r30, a:r31}.
- 38 rows bank-shift-1: era r25/r26/r27 reads vs ours r24/r25/r26 (p/hdr/c trio) —
  includes stmw/lmw, bind slots 5/6/8, extsh. r0,r27 vs r26 sites.
- 6 rows switch-home: `new_var2 = hdr[0]` homed r27 + tested (slots 10,12,16,19,22,25;
  era: lbz r0,0(r6) + cmpwi r0 — switch value NEVER homed in era).
- 4 rows tail-reload: era `lbz r4,0x0(r26)` reload feeds cmplwi 0x80/0x90, subi 0x78
  (slots 326,330,333,338); ours reads new_var2 home r27.
- 2 rows load-order swap: era `lwz r3,0x78(r25); lwz r0,0x54(r25)` (x->r3 first);
  ours `lwz r0,0x54; lwz r3,0x78` (y first). Targets match (x<->r3, y<->r0).

## Rung ladder (3 grind builds, 1 confirm; cap 8+1)
| rung | knob | size | rows | match | verdict |
|---|---|---|---|---|---|
| 0 | tip (absorbed port) | 1520 GATE | 50 | 99.30526 | champion |
| 1 | kill `new_var2` home; tail test on hdr[0] (era-faithful, 7 homes) | 1524 +4 | 132 | 98.41579 | REVERT-WITH-DATUM |
| 2 | pair-1 init order x-first (swap the two decl-inits) | 1520 GATE | 56 | 99.12631 | REVERT-WITH-DATUM |
| 3 | pair-1 decl-split (decl y,x; init x,y) | 1520 GATE | 53 | 99.23158 | REVERT-WITH-DATUM |

Rung-1 datum (bank class SEALED): removing the 8th home does NOT restore the era
stack. 7-home config re-ranks to {p:25, a:26, hdr:27, c:28, res:29, len:30, self:31}
= era {hdr,c,res,len,self} shift UNIFORM +1 (relative-rank-preserve fires) and a
decisive a:31->26 jump; MWCC also pays +1 insn (381 rows, 0x5F4 gate death).
=> trio shift is the RA-spill era-layout stratum (the era's 7-stack pin lacks a
home-removal emitter at this pin). Decl grid capped; STRUCTURALLY INERT (rank-preserve
law). Do NOT re-roll new_var2-kill at this pin.

Rung-2 datum: pair-1 swap alone flips SCRATCH targets (x->r0, y->r3 via decl-order
rank) = +6 rows. Pair-1 and pair-2 (0x7c/0x8, already era-spelled x-first with
x->r3) share the {x<->r3, y<->r0} binding identity: any def-order knob on pair-1
re-binds pair-2's uses (rung-3 landed pair-1's loads era-exact, slots 64/65/66/68,
broke pair-2's cmpw/cmpwi operand rows 80/82/86 = net +3). The two pairs are ONE
def-binding lineage entity; era's simultaneous x-first/x->r3 in both pairs has no
C spelling at GC/1.2.5n -O4,p (color rows bind to VARIABLE IDENTITY through
def/decl/window permutations — QVM/417294 lineage law). SEALED at tip side.

## Sealed classes (this visit's datum, v2 re-opens need a NEW mechanism)
1. bank-shift-1 + switch-home + tail-reload (48 rows): new_var2 home/RA-spill
   era-layout stratum (rung-1 gate-death proof above; rank-preserve zero-build).
2. load-order swap pair (2 rows): def-binding lineage, bind-to-identity (rung-2/3
   bracket: -2/+6/+3 rows; era shape = x-first AND x->r3 in BOTH pairs = no emitter).
No spelled rung remains => ladder-clause close at 99.30526.

## Battery (zero-delta close at champion tip; 3 grind + 1 confirm builds)
- full ninja rc=0 (cache/ffb84_full_ninja_base.log, cache/ffb84/full_ninja_close.log)
- report_delta cache/base_report_ffb84.json build/GPOE8P/report.json --check:
  New exact functions: 0; regressions: 0; all counters +0
- check_pr.py: PASS (linked now: 2871, exact candidates to add: 2, regressed 0, skipped 0)
- sibling safety: llvm-nm -S 130 symbols, int-parse word compare base vs confirm:
  ZERO drift (law g; all rungs reverted)
- DOL sha1 0d85744b51d7379efb025a943d0cd5aaae2191a3 (expected-constant, unlinked unit)
- unit .o sha1 584a185666eff0e695e56d55f953155d43ecddbb (== fe6cc-v1 receipt .o:
  tip content byte-unchanged by this visit)

## Verdict
PARK at sealed-class ceiling 99.30526, GATE-EXACT (1520/1520, 380/380 rows).
Report row PAIRED display-rows 99.30526 (fuzzy), no matching_percent => NOT
100.0-paired => NOT PR material (byte-exact-only ship policy). Sub-100 floor is
ledger inventory. Unit supply: PADRead (768B, 99.24479) co-edited by f4 twin in
same file, own tree (law p). If PADRead lands 100.0, the unit's third sub-100 row
is THIS seat — pair-complete-unit linked row stays INTEGRATOR-side.
