# ANATOMY — fn_8042E8C4 (psov3/pso/unk/text_8042E8C4, 0x8042E8C4, size 0x138, 78 words)

## Verdict: function-level asm unit (orig_asm transplant), byte-exact 78/78, gate gnm 0x138.

## Why not C (decisive evidence)
- Tail slots 74–77: `lwz r0,0xE0(r26); isync; mtlr r0; blr` — an epilogue-free
  computed jump: no lmw, no frame restore, no addi r1. Function keeps r26–r31
  live in callee slots and NEVER returns.
- Probed MWCC GC/1.2.5, 2.0p1, 2.5, 2.6, 2.7, 3.0a5.2 with `-O4,p`
  (unit profile from build.ninja; 'ntutl'): every inline `__asm{blr}`-tail
  variant (combined block + separate blocks) appends the dead
  lmw/lwz/mtlr/addi/blr epilogue (+5..7 words). v00 natural C @2.6 = 85w,
  frame 0x30/stmw r25 (len/i homes split → 7 callee regs), CSE `lis r5`
  artifact.
- `__declspec(noreturn)` → "illegal type qualifier"; `__attribute__((noreturn))`
  def → syntax error, decl-only → ignored (epilogue stays);
  `__attribute__((naked))` → rejected; string-form `__asm("blr")` → rejected.
- Only epilogue-dropping terminator found: `for(;;)` terminates CFG — emits
  `b .` (48000000) at slot 77 where the object has `blr` (4E800020): 78w
  size-exact, 1-row wall. That is the C ceiling (kept as fallback in
  v01-merge line of work).
- Corpus screen: the ONLY non-epilogue mtlr/blr tail in the whole 14k-split
  tree (1343 mtlr/blr fns scanned; twin hit __init_hardware is SDK asm).
  No sibling uses isync-from-C anywhere in src/.
- Additional tell: MWCC's asm-block DCE silently deleted `__asm{lwz r0,..}`
  when r0 died (probe e2) — statement-asm isn't passthrough; a C source
  producing exactly these words is not expressible.
- Precedent for asm-sourced units: TRK_MINNOW flush_cache (`asm void
  fn(register...) {#include "orig_asm/..."}`), musyx reverb/chorus (linked
  True), OSReboot Run / OSReset Reset static asm.

## Semantics (naming report-only)
arg (r3) = reset-request header; arg->0x104 = table/image base (r26),
arg->0x108 = payload size. Flow:
1. `memmove(0x80003100, arg, (size+0x132)&~31)`; `DCStoreRange(0x80003100, len)`
   — stash image+header into the reset-resident buffer @0x80003100
   (same fixed-address family as OSReboot.c's OS_RESET_CODE@0x800030F0,
   OS_REBOOT_BOOL@0x800030E2; fn_8042E8B8 in ModemRuntime returns this const).
2. `OSResetSystem(2,0,0)` (soft/hot reset request; pso_date/TKeyBoardControl
   matched siblings call it with mode 1).
3. `memset(base->[0xD8],0,base->[0xDC]); DCStoreRange(base->[0xD8],base->[0xDC])`.
4. 7-iteration table walk @base+0x00(src delta)/+0x48(dst)/+0x90(len):
   zero-terminated (cmplw vs always-0 sentinel r30; two induction regs r27=idx
   r31=off, no early exit observed in practice), per entry
   memmove(dst, base+delta, len); DCStoreRange; ICInvalidateRange.
5. 11-iteration twin walk @+0x1C/+0x64/+0xAC, memmove+DCStoreRange only.
6. Tail: jump to `base->0xE0` continuation inside the reloaded image
   (isync between load and mtlr; frame and callee regs abandoned → no return).
Caller context: fn_8042EAD4's twin fn_8042EBA4 fills hdr+0x100/0x104/0x108
(size 0x18000) from globals lbl_805D7CB0/D6B0 — GBA/modem-adapter image
reload-and-reset family (cf. GbaDownloadRuntime 0x40000 buffer alloc).

Synthesis check (A41C lesson): prologue is NOT __sinit-family — no .ctors
rows on unit (unit is pure .text 0x138), single global fn, no cursor chain.
Gate: symbols row size:0x138 == 78 disasm words == gnm 0x138 ✓.

## Receipts
- score.py target.o t_asm.o → 78/78, REGDIFF [] — TEXT-HEX-IDENTICAL (-s
  dump cmp), RELOCS-IDENTICAL (R_PPC_REL24 diff empty), gnm: T fn_8042E8C4
  00000138 + U {memmove,memset,DCStoreRange,ICInvalidateRange,OSResetSystem}
  == parked .o symbol set both ways.
- ABSENT screen: `git log --all -S 8042E8C4 -- src/` → only seed f52fa585
  (empty blob 8b137891, one newline) → no transplant content, cold confirmed.
- Inc regen: `python3 tools/orig_asm.py build/GPOE8P/asm
  config/GPOE8P/psov3/symbols.txt
  build/GPOE8P/include/orig_asm/pso/unk/text_8042E8C4/fn_8042E8C4.inc`
  (ninja has rule orig_asm; pin rule respected — configure.py never run).
