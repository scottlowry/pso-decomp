# text_802BFBF4 (fn_802BFBF4, 0xD68) — MWCC __sinit synthesis, GATE-EXACT first try

Era cold: unit src was empty (1 byte), report 0.100.0 -> now .ctors 100.0 + .o emitted.

## Decoded anatomy
`fn_802BFBF4` = synthesized `__sinit_text_802BFBF4_cpp` boot-seeding the
**TBoss6Type2 state-action table**: 36 rows x 48B
`{u8* code (rodata lbl_804713D0..8047152C + one sdata2 lbl_805DE4D8), s32 stateId (0..0xC, -1 term), s32 flag, void (TBoss6Type2::*h[3])()}`.
108 handler slots = 97 method-initialized ({0,-1,fnptr} template words, packed at
lbl_804DFC50 0x48C) + 11 zero (runtime __ptmf_null triples). Instance at template+0x48C
(era row lbl_804E00DC size 0x6C4 = 0x6C0 image + 4B pad).
Frame: stwu -0x230, stmw r14@0x1e8, single-anchor r4=template base + word disps,
lmw tail. Sources: template_words.txt (97 triples), dst map via provenance parser.

## Spellings that work (probe V1 -> 854/858 positional raw-byte EXACT + 4/4 link-recompute = 858/858)
- File-scope `static TBoss6Type2Action lbl_804E00DC[36] = {...}` with `Handler h[3]`
  pmf members: MWCC splits image: [97x@12B anon template blobs @1-@97 (...data.0)][instance
  with header words + zero pmf slots] contiguous .data — era geometry exactly.
- Member fns with args DO pair: `(Handler)&TBoss6Type2::start_death_sequence`
  (FPUc/FPv era names reproduced verbatim in relocs; pmf->pmf cast accepted,
  IMPLICIT rejected: "illegal implicit conversion").
- Local mirror class (43 decls) is house-legal (text_80071B30 precedent); the real
  header's class differs per-TU, no ODR at link.

## Dead ends / traps
- Free->pmf cast: MWCC 2.6 hard-rejects ("illegal explicit conversion from void(*)()
  to void (C::*)()const") — confirmed on 802B0A44 probe. Era UNMANGLED placeholders
  (TBoss6Type2__sub_802BE648/BF3F4/BF834/BF904/BFA1C/BFBE4/BEB78/BEC28/BEE38/BE6A0/BE738,
  11 slots) are extern-"C" free fns in siblings (TPlayerFootStamp_*, TBoss6Type2_802BF558)
  -> mirror-member refs carry member-mangle (sub_802BFBE4__11TBoss6Type2Fv) = link-breakers
  (69C class). Unit intentionally UNLINKED.
- Transcription drift matters: one slot-order swap (r01 slot1<->slot2) reshuffled the
  ENTIRE register allocation (854 -> 3/858). Regenerate repo file FROM the probe file.

## PAIRING / ASK (#173 template shape)
- rename row 20155 `fn_802BFBF4` -> `__sinit_text_802BFBF4_cpp` scope:local
  (precedents rows 2174/2256/14846/22209/23145/23312 + 67F4 23120). Est. **100.0% at
  pairing** (854 positional byte-exact + 4 link-resolved rows re-verified word-equal;
  zero order residue — first trio-class unit with full-match estimate).
- Link-readiness: NOT READY — needs (a) 11 placeholder handler symbol resolution
  (rename era rows to member-mangle + sibling src rename = naming decision; or
  sibling-owned member definitions), (b) if claiming .data 0x804DFC50-0x804E07A0
  (unclaimed filler today; window exact): CONSUMER CYCLE — matched sibling
  TBoss6Type2.cpp:665/2515/2541 externs `lbl_804E00DC` (kept valid: our .o exports
  EXACT era name `lbl_804E00DC`); our template relocs reach sibling text (11 subs +
  named methods) => bidirectional = TSaveChCr-class dtk cycle risk. CYCLE-FREE CLAIM
  SCOPE = .text 0x802BFBF4-0x802C095C + .ctors 0x80433FCC only (current state).
- Template pool row lbl_804DFC50 pairs only via claim+address (compiler-anon
  `...data.0`/`@NNN` — jumptable lore class, not source-nameable).

## Screens
- splits: .text range == symbols size:0xD68 exactly; .ctors 1 word; no .data owned (OK).
- def-count: 1 (this unit); refs absent-verify: all 45 lbl_ + 32 mangled names ==
  symbols.txt rows verbatim (bl/addr16 immediates measured vs disasm; era addresses
  via symbols.txt; NAME-MISS rows only the 11 known placeholders mapped member-mangle).
- gate: gnm OURS 0xD68 == row size 0xD68.
- report after swap: .ctors 100.0, fn row None (name block expected), matched_data 4/4.
