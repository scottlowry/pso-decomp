# ANATOMY — pad_03_8042E9FC_text (psov3/pso/unk/text_8042E9FC, 0x8042E9FC, size 0x14, 5 words)

## Verdict
Unit COLD target fully paired: pad_03 (0x14) + init_modem_check_params (0xC4)
both 100.0 one-shot; unit fuzzy 90.74 -> 100.0 (216/216 code, 2/2 functions).
Pad body shipped as function-level asm via the house `tools/orig_asm.py` include
(`orig_asm/pso/unk/text_8042E9FC/pad_03_8042E9FC_text.inc`, tool-generated, 5 opwords).

## What the pad IS (synthesis check)
`BB410008 lmw r26,0x8(r1) | 80010024 lwz r0,0x24(r1) | 7C0803A6 mtlr r0 |
 38210020 addi r1,r1,0x20 | 4E800020 blr`
It is the *frame-restore epilogue of fn_8042E8C4* (previous unit, 0x8042E8C4..0x8042E9FC,
symbols size 0x138). Proof: that function's own prologue is
`stwu r1,-0x20(r1) ... stw r0,0x24(r1) ... stmw r26,0x8(r1)` — the pad restores
exactly that frame. fn_8042E8C4 exits via an epilogue-free computed jump
(lwz r0,0xE0(r26); isync; mtlr; blr, per the fresh 79a4cfae match), so the epilogue
is unreachable tail-duplication; the 0x8042E9FC split boundary strands it in THIS unit,
where dtk names it pad_03_8042E9FC_text (local 't', absent from symbols.txt) and
config.yml already carries skip_cfa_ranges .text:0x8042E9FC..0x8042EA10.
No referrer anywhere: grep over build/GPOE8P/asm/ hits only this unit's own .s.
Zero relocations in the pad (pure opwords).

## C-inexpressibility — ALL 20 installed MWCC versions (not 12)
build/compilers/GC/: 1.0 1.1 1.1p1 1.2.5 1.2.5n 1.3 1.3.2 1.3.2r 2.0 2.0p1 2.5
2.6 2.7 3.0a3 3.0a3.2 3.0a3.3 3.0a3.4 3.0a3p1 3.0a5 3.0a5.2 — every one probed with
the unit's exact profile flags (ninja -t commands .../text_8042E9FC.o: -O4,p -inline off
-use_lmw_stmw on -lang=c++ -char signed -enum int -fp hardware -str reuse ...), wibo runner.
Receipts: sweep.log (size per version/spelling) + table.txt (byte-exactness verdict,
word compare done in-python over gobjdump -d of all 80 probe .o files).

| spelling | emitted pad | byte-exact 5 words @ .text+0 |
|---|---|---|
| v1 empty C function `void pad(void){}` | 0x4 (`blr`) | 0/20 |
| v2 callee-reg-hungry C function (6 live loads/stores -> lmw epilogue) | 0x50 (stwu/mflr/stw/stmw prologue + body + epilogue) | 0/20 |
| v3 statement-asm `asm{lmw...blr}` in a C function | 0x28 (1.0–1.2.5n) / 0x30 (1.3–2.7) / 0x2c (3.0a*) — own frame + dead tail after the asm blr; also warns "reserved registers" | 0/20 |
| v4 `static asm void` + tool-generated .inc (SHIP) | 0x14 | 20/20 |

Structural argument: the target is an epilogue with no prologue; MWCC emits
lmw/mtlr/addi only as the tail of a function whose prologue saved those registers,
so no C body can start the unit with these 5 words. `static` keeps the symbol local
('t') exactly like the original object; unreferenced static *asm* functions are still
emitted (verified in the real unit .o).

## Sibling/alternatives considered (report-only)
The clean ownership fix is CONFIG: move the .text split boundary to 0x8042EA10 and fold
the 5 words into fn_8042E8C4's asm body. Rejected for the lane: splits/symbols edits are
pinned (config hard line) and fn_8042E8C4 is a fresh sacred park (its 0x138 size gate
would break). Integrator may prefer that shape.

## Gates (all on fleet/f3 @79a4cfae + this change)
- gnm OURS: `t pad_03_8042E9FC_text` 0x14 + `T init...` 0xC4 = .text 0xD8 == split 0xD8.
- one_shot: ORIG/OURS pad 100.0/20, init 100.0/196. (ours [.mwcats.text] 8B extra is
  repo-wide MWCC noise, present on every complete=True unit too.)
- report_delta --check (before=pre-change report.json copy): New exact functions 1
  (+0x8042E9FC pad_03_8042E9FC_text), regressions 0, RC=0.
- full ninja: build/GPOE8P/psov3.dol OK (sha vs config/GPOE8P/psov3/build.sha1) — the
  unit is unlinked so the DOL is untouched by construction; siblings byte-untouched.
- check_pr.py: PASS (RC=0). link_units scan: this unit NOT in linked_units_blocked.json;
  check_pr reports "exact candidates to add: 2" (this unit + text_8042E8C4) —
  linked_units.txt/completed row is config, integrator adds it.
- Builds: unit .o x2, full ninja x2, check_pr x1 = 5/8.
