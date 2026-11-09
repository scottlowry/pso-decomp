# TLobby__sub_803FCC10 v1 — census receipt (f3 card-803fcc10-v1, base 00cda35c, Nov-8)

## Intake (measured, not assumed)
- Symbols row: `TLobby__sub_803FCC10 = .text:0x803FCC10; size:0x334` (820B) — verified.
- Pin (live build.ninja row 57921): GC/1.2.5n, `-char signed -use_lmw_stmw on -O4,p -inline off -opt nocse -lang=c`. verified, not assumed.
- Unit psov3/pso/network/TLobby_803FC178 UNLINKED (grep linked_units rc=1, build.ninja 'linked False') — DOL-insensitive, law h.
- Base snapshot: cache/base_report_fcc10.json + DOL sha 0d85744b51d7379efb025a943d0cd5aaae2191a3 (regenerated full-ninja rc=0 at tip).

## PAIRING-BREAK census (law a)
- Body PRESENT at size-correct position: orig 205 / ours 205 rows, gate 0x334 = gnm 0x334, paired 99.21951 at tip. NOT cold-author, NOT mis-split.

## Ladder
- Seed (base tip): 99.21951 official, 33 one_shot rows = 5 frame-geometry + 28 color.
- Rung 1 (cd79d0d1, ONE knob): drop dead `int new_var4[2]`. Diagnosis (objdump frame scan of pre-rung .o): only referenced slots were v@0x10 (9x) + ctx@0x14 (3x) — the array was PURE PADDING: RA kept rem in r30 (store folded), `new_var4[1] = 0x10` assignment-expr folded to the era's immediate (`addi r3,r31,0x10`). Replaced with direct `rem` + literal 0x10. Frame 0xa0→0x98, stmw bank 0x78→0x70, LR 0xa4→0x9c: ALL 5 frame-class rows closed. Gate stays 0x334, all 11 unit symbols gnm size == era row (int-parse, zero drift).
- Official paired meter post-rung: 99.21951 FLAT (report.json address-resolved; the 5 geometry rows contribute 0 partial-credit delta, the ring rotated to absorb the 28→32 row count — lha len row enters as lha slot re-ranked).
- one_shot post-rung: 99.07317, 32 rows, all pure register renames.

## Sealed-class ceiling datum
Residual 32 rows = def-binding home ring (law f sealed, RELATIVE-RANK-PRESERVE proven zero-build):
- Era rank map (strictly descending): self=r31, len=r30, g=r29, walk1=r24 (+ i/walk2 share {r24,r25} swap, cnt=r26, src=r23, r27=0 const).
- Ours: len=r31, g=r30, walk1=r29, self=r24 — same 4-reg set {24,29,30,31}, cyclic rank-rotate by exactly 1; every pair's relative order preserved mod rotation => decl-grid levers structurally inert (banked: rank-UP levers cannot cross a ring rotate; colors bind to variable identity through def/decl/cast/window permutations).
- Bank-scratch tie: era l1 lives in r22 (bank-bottom as data: clrlwi r22 + addi r30,r22,1), ours in r25 (slot 139/143) — same family (bank allocation tie-break, EB4D4-kin clobber-analysis lineage: era's in-TU analysis keeps r22 alive across the two bl NetStringLength sites).
- Instruction MULTISET is era-identical (each row same mnemonic/disp/imm, only reg name differs). Frame/bank/LR geometry now era-exact.

## Visit-2 frontier
1. Ring cross {self,len,g,walk1} = def-binding home ring: no C spelling emitter at pin (sealed class list) — needs era-object-layout/def-binding mechanism, not a rung. Census row: rank-rotate-by-1 of a 4-reg cyclic set.
2. l1-in-r22 bank-scratch: era uses bank-bottom as live-across-bl data — era clobber-analysis stratum (EB4D4 visit-3 family), do NOT grind.
No geometry rows remain; no spelled non-color rung remains -> ladder closed at rung 1.

## Battery (rung 1, committed tip)
- rm .o + ninja unit: MWCC line printed, rc=0.
- Full ninja: rc=0.
- tools/report_delta.py cache/base_report_fcc10.json build/GPOE8P/report.json --check: New exact 0; regressions 0; all counters +0. rc=0.
- tools/check_pr.py: PASS (link_units check OK, regressed 0).
- DOL shasum: 0d85744b51d7379efb025a943d0cd5aaae2191a3 — constant (expected-constant: unlinked unit).
- Gate: llvm-nm -S int-parse: 0x334 = era 0x334. Siblings: 11/11 sizes == symbols.txt rows.

## Verdict
99.21951 official paired, GATE-EXACT, geometry-exact after rung 1. SUB-100: NOT PR material; ledger park on branch card-803fcc10-v1 (cd79d0d1). Builds used: 2 grind-equivalents of 8.
