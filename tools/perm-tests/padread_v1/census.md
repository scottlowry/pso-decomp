# padread v1 census receipt (f4 card-padread-v1, base 00cda35c, Nov-8)

Seat: PADRead = .text:0x80402E68 (symbols.txt:27466, size:0x300). Gate FROM ROW: 768B.
llvm-nm -S OURS: 00005f24 00000300 T PADRead => GATE-EXACT 768/768, INT-parse clean.
Unit: psov3/pso/network/TLobby_803FCF44 (home src/pso/network/TLobby_803FCF44.c lines
~4401-4466, body PRESENT, wrapped #pragma push / dont_inline off / inline_depth(4) / pop).
linked False (verified: absent from config/GPOE8P/psov3/linked_units.txt) => DOL-insensitive;
inertness = unit .o sha + report_delta regressions 0.
Pin (live build.ninja:57941 cited): GC/1.2.5n -char signed -use_lmw_stmw on -O4,p
-inline off -opt nocse -lang=c.

## MEASURE-TIP-FIRST
rm unit .o + ninja rebuild printed MWCC line. Paired meter (needle PADRead, row addr
80402E68): ORIG/OURS match=99.24479 size=768/768, rows orig 192 ours 192, 29 diff rows.
Frontier census #2 of unit CONFIRMED (99.24479, 768B).
Official report.json pairing agrees: PADRead size 768, fuzzy 99.24479, vaddr 0x80402E68.

## PAIRING-BREAK census
Ours unit .text total = 0x79A4 = era EXACT; 118 T symbols, all int-parse, 0 stubs.
No missing body, no mis-split.

## Residual row taxonomy (29 rows = seat's entire residual)
ALL 29 rows are PURE REGISTER SUBSTITUTION (strip r\d+ -> rows identical; prologue/
epilogue byte-identical: frame 0x38, stmw r26,0x20(r1), lmw r26 tail). No jumptable
@NNN display rows, no shape rows. Slot map era->ours:
- 31->29: f30 top load slot8 + f30[0]/[4] stores 181/183 (CASE-3 stores keyed off TOP
  f30 load on both sides; era kept top range in r31, ours in r29).
- 29->26: p (self+0xc) case-1 load 35 + uses 45/46/48.
- 28->29: f30 case-2 reload 55 + (+8) store 93.
- 29->28: self-copy addi 81/153 + extsh src 95/167 (EXTSH-BIND stratum).
- 28->26: p case-2 load 107 + uses 117/118/120.
- 27->31: f30 case-3 reload 127 + (+8) store 165.
- 28->27: n extsh 143/144/146 + cmpw 162/168 + mr r5 156.
- 3->5: caller-saved zero scratch li/stbx 88/89 (c2), 160/161 (c3).

## RELATIVE-RANK-PRESERVE diagnostic (zero-build, BEFORE any decl grid) — FIRES
Era per-range homes: f30 {31(top),28(c2),27(c3)} all DISTINCT; ours f30 {29,29,31}
NOT injective. Tests:
1) Uniform cyclic shift over 6-bank: NO bijection fits (non-injective target).
2) Global bijection: era r28->ours {26,27,29}, era r29->ours {26,28} MULTI-VALUED
   => era performs per-case live-range recycling (one physical reg serves f30, then p,
   then n ranges across case kills); ours keeps stable per-decl homes. The era's c2
   f30==p SHARED register is unreachable by ANY permutation of stable homes.
3) Relative ranks of distinct roles (c1: p<f30) preserved on BOTH sides.
=> def-binding home-ring + decl-order grid STRUCTURALLY INERT. Grid cap 0 (sealed).
Classes struck (all in fleet closed list, no re-roll): def-binding home-ring
(rank-preserve, 4th firing incl this unit), RA-spill era-layout (per-case range
recycling incl caller-saved r3/r5 scratch choice), EXTSH-BIND.

## Sibling-safety
All 118 unit symbols int-parse at tip (scratch/padread_gnm.txt); no source edit made —
tip state IS the park state; unit .o byte-identical to fe6cc visit-1 (sha below).

## Battery (zero-build census close; 0 grind builds spent)
- configure.py -v GPOE8P + full ninja rc=0 (scratch/padread_full_ninja_base.log)
- report_delta cache/base_report_padread.json build/GPOE8P/report.json --check:
  matched_functions 27432->27432 (+0); New exact functions: 0; regressions: 0
- check_pr.py: PASS (linked now: 2871, exact candidates to add: 2, regressed 0, skipped 0)
- DOL sha1 0d85744b51d7379efb025a943d0cd5aaae2191a3 = expected constant (unlinked)
- unit .o sha1 584a185666eff0e695e56d55f953155d43ecddbb (= fe6cc receipt sha; inert)

## Cross-tree (law p, read-only)
f3 twin card-803ffb84-v1 @ 00cda35c, TLobby_803FCF44.c locally modified (active grind
on 0x803FFB84, rows below my seat's region; function-scoped, disjoint). Ship order:
twin address 0x803FFB84 < PADRead 0x80402E68 — lowest-address-first is twin-side.

## Verdict
PARK at sealed-class ceiling 99.24479, GATE-EXACT (768/768, 192/192 rows).
NOT 100.0-paired => NOT PR material. Re-open requires NEW mechanism for the
RA-recycling stratum (stable-home model cannot spell per-case range splits).
Budget: 0 grind builds (1 unit-.o tip rebuild, base full ninja).
