# fe6cc v1 census receipt (f4 card-803fe6cc-v1, base 00cda35c, Nov-8)

Seat: TLobby__sub_803FE6CC = .text:0x803FE6CC, size 0x154 (340B, gate-from-ROW verified;
era .fn header agrees; llvm-nm -S OURS: 00001788 00000154 T = GATE-EXACT).
Unit: psov3/pso/network/TLobby_803FCF44 (net home src/pso/network/TLobby_803FCF44.c),
linked False (verified: not in linked_units.txt) => DOL-insensitive, inertness = unit .o
sha + report_delta regressions 0.
Pin (live build.ninja row cited): GC/1.2.5n -char signed -use_lmw_stmw on -O4,p
-inline off -opt nocse -lang=c.

## MEASURE-TIP-FIRST result
Body PRESENT at tip (absorbed by #213 migration 76d99c97, decompiler port at
src file lines 1829-1911 inside #pragma push/opt_lifetimes off window).
Paired meter (one_shot, committed tip, after rm+unit-.o rebuild printing MWCC line):
ORIG/OURS match=98.35294 size=340/340, rows: orig 85 ours 85, 19 diff rows.

## PAIRING-BREAK census
Ours unit .text total = 0x79A4 = era total EXACT -> no missing body, no mis-split.
All 118 unit functions have bodies (cold-author stub count 0).

## Residual row taxonomy (19 rows = seat's entire residual; nothing else diverges)
- 17 rows: def-binding home ring. Cyclic +1 rotation of the 3 callee-save homes over
  ring (r28,r29,r30): era {self:28, a:29, c/buf:30} -> ours {self:29, a:30, c/buf:28}.
  r26 (alloc out), r27 (switch value), r31 (self->0xc) pinned identical.
  RELATIVE-RANK-PRESERVE diagnostic (zero-build): ranks unchanged under uniform cyclic
  shift => decl-order levers structurally inert. Sealed class (lane law f "def-binding
  home ring"; F2F4 bind-to-home stratum law). NO spelled rung.
- 2 rows: jumptable pool-name display, OURS @391 vs ORIG jumptable_804FD5F8.
  Claim already present: symbols.txt:45788 (jumptable_804FD5F8 = .data:0x804FD5F8;
  size:0x30 scope:local). Banked law: MWCC emits the switch table as an anonymous
  object-local .data symbol; the OURS reloc name comes from the .o symbol table, NEVER
  the symbols.txt claim (load_bml_exec @139 precedent). ACCEPTED display class.

## Battery (zero-build census close; 0 grind builds spent)
- full ninja rc=0 (scratch/full_ninja_base_fe6cc.log)
- report_delta cache/base_report_fe6cc.json build/GPOE8P/report.json --check:
  New exact functions: 0; regressions: 0
- check_pr.py: PASS (linked now: 2871, exact candidates to add: 2, regressed 0, skipped 0)
- DOL sha1 0d85744b51d7379efb025a943d0cd5aaae2191a3 (expected-constant, unlinked unit)
- unit .o sha1 584a185666eff0e695e56d55f953155d43ecddbb
- git tracked-clean at close; no source edit made (tip state IS the park state)

## Verdict
PARK at sealed-class ceiling 98.35294, GATE-EXACT (340/340, 85/85 rows).
Not 100.0-paired => NOT PR material (byte-exact-only ship policy). Sub-100 floors are
ledger inventory. Re-open requires a NEW mechanism for the ring class (era MAP /
context-binding), not a re-roll of decl grids.
