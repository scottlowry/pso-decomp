# f3 card-mirage-e7b94 — TObjEneMe3ShinowaMirage__sub_800E7B94 (gate .text:0x800E7B94 size 0x510, 324 insns)

FLOOR 88.88271 at 0x4F4 (-7W vs gate), committed tip 22b193a4, base e175bcd9, branch card-mirage-e7b94.
Unit psov3/pso/enemy/TObjEneMe3ShinowaMirage_800E7A70: siblings 3/3 at 100.0 (0x28 / 0xDC / 0x20, gnm-verified
after clean rebuild); unit stays 3/4 functions = NOT complete, linked_units 3309 unchanged (row would make 3310).
Gates on the tip: full ninja rc=0, report_delta --check vs baseline-e175bcd9.json = New exact 0 / regressions 0,
check_pr PASS, link_units check OK.

## Screens (first acts)
- GSP ps-arith screen: 0 hits. One Gekko spill pair (stfd f31,0x50(r1) + psq_st f31,0x58(r1) / psq_l + lfd in
  the epilogue) = 1 denied FPR home, the clamped `step` value (live across 4 bl). Anatomy pass VALID.
- Aligned-frame ASK scope check (Me3Shinowa v118 class): all three `lfd` are 8-aligned (rodata pool @l,
  0x30(r1) int->f32 magic slot, 0x50(r1) spill restore). Class ABSENT at this site -> ASK does not transfer;
  screened fresh per the retirement-scope note (branch-list 0, board 0 receipts).
- Twin: TObjEneMe3Stelth::load_shared_resources (era 0x800F53E8, 0x47C, 100.0-paired, unit 61/61) = verbatim
  structural parallel through 15 blocks. Transcribed statement-for-statement, swap bases/values.

## Anatomy (frame 0x60, stmw r27 = 5 GPR homes {r31 anchor, src, n, 2 loop temps}, 22 bl callees)
B zero-trio off the .bss window anchor -> v2-mode branch (load_enemy_bml_resource_named / plain, string
lbl_8043CFE8) -> res store -> mem_alloc(count*0xC) + copy_vec3 loop (ONE shared 12-byte cursor) -> bdnz
z-copy i -> i+3 -> 4 x 2-iteration lwzx/stwx handler loops (register_boss / dispatch_b / register_object /
dispatch_a over lbl_8043CE1C/24/2C/34) -> set_slot(6, d+0xC), set_slot(3, d+0x10) -> render_node_index=0 +
spawn-vec trio (lbl_80500FF4) -> 3 x find_model_node(9/0xD/0x26) cursor chains into lbl_80501000[0..2] ->
TBreakUpMdl new(0x10)+init (0x4330 f64 magic) -> 3 x SampledMotionPoints new(0x18)+ct+sample_node_offsets
(node_index 0x22/0x22/0x15, stack vecs @0x24 zeros / @0x18 {C,0,0}) -> 2 x spawn_npc_enemy(0x26, 0x27) with a
4-word desc copy from lbl_8043CF84 + word-0 overwrite by res->f430.

## Data-map law (the wall)
The era unit .o addresses the whole 0x80500FC0..0x80501010 .bss window through the ONE symbol
TObjEneMe3ShinowaMirage__data_80500FC0: `objdump -dr` shows reloc-free `addi r4,r31,44` / `addi r28,r31,0xc` /
`addi r5,r31,0x34` / `stw r0,0x40(r31)` and the U list carries only that anchor (+ lbl_80500FEC, used by the
sibling free fn). symbols.txt tiles the same window into 6 rows (data_80500FC0 0x24 / mirage_info_table 0x8 /
lbl_80500FEC 0x8 / lbl_80500FF4 0xC / lbl_80501000 0x10) - adjacency artifacts, NOT source symbols in this TU.
splits.txt: the window is an UNCLAIMED .bss hole (TObjFish_800E2FFC ends 0x80500FC0, TObjEneSlimeTailAttack
starts 0x80501010); our unit's split owns .text only.

Addressing-model ladder, all measured at the unit's own GC/2.6 -O4,s pin (ninja line verbatim):
1. single typed view-struct anchor + named cursor locals (CHAMP, 22b193a4) = 0x4F4 (-7W), 88.88271.
   Deficits: 5 era cursor sites keep `addi rD,rANCHOR,K` + disp-store where MWCC 2.6 store-folds to one
   disp store (1 D, 1 H, 3 I-cursor arms = -6W) + the era's `addi r3,r31,0x0` walk copy (-1W).
   Both = CLOSED classes (parser-canonicalization store-fold; ZERO-OFFSET-COPY).
2. per-row externs for the derived slots (pass 5, 22b193a4..reverted) = 0x524 (+20W), 87.99383: every extern
   forces its own lis@ha and rematerialises per BB.
3. the twin's model = co-define the window symbols in-file (`f32 lbl_805010E0[3];` idiom, TObjEneMe3Stelth.cpp
   65-72) -> reproduces the era's reloc-free derived addis exactly (twin proof). BLOCKED for a lane: needs the
   splits.txt row `.bss start:0x80500FC0 end:0x80501010` for pso/enemy/TObjEneMe3ShinowaMirage_800E7A70.cpp
   (config = integrator), then the window symbols defined in-file in era order.

## Spelled successor (micro-card, config-gated)
Integrator adds the .bss claim; lane then moves the 5 window rows into in-file definitions in era layout order
(m_0 f32[3] @+0, m_c s32[6] @+0xC, m_24 s32[2] @+0x24, m_2c s32[2] @+0x2C, m_34 f32[3] @+0x34, m_40 s32[4]
@+0x40), re-scores; the 7 residual rows are predicted to land with the twin's cursor shapes. Screen order:
objdump -dr the era unit .o and COUNT reloc-free `addi rD, rANCHOR, 0x` sites BEFORE choosing the data
spelling - a window with >3 such sites is a claim/ownership card, not a grind card.

## Other receipts
- 8-arg repo decls of spawn_npc_enemy__6TLobbyFsllPvff (text_8035B6B0.cpp:15, TObjEnePanarms_800DCEB8.cpp:214)
  are decompiler-view inflation: the mangle FsllPvff = 6 params (s16,s32,s32,void*,f32,f32); the era's r7/r8 at
  call 1 are the desc-copy leftovers. Declaring 8 params costs the era-absent r7/r8 remat at call 2.
- copy_vec3 loop: src array element type must be the 12-byte vec (8-byte element type buys a second IV, +1W).
- 0x8043CFA0 (2^51, the int->f32 magic) sits inside TObjEneMe3ShinowaMirage.cpp's .rodata claim; our compile
  puts it in our own 8-byte .rodata pool -> +1W (pool base + addi@l + lfd vs era's lis + lfd@l) and the row
  renders @140 (link-gated naming). Lane-inert; a .rodata claim for the consuming unit is the only route.
- Names: gate row keeps the `sub_800E7B94` placeholder (adopted verbatim as the extern-C symbol name so objdiff
  pairs); callee/target names all come from config/GPOE8P/psov3/symbols.txt rows; SampledMotionPoints/NJS
  method names come from upstream 8e518f16 (provenance re-cited). No invention.

## Cold start
git -C /Users/scott/Hermes/pso-decomp/pso-decomp-f3 branch --show-current   # card-mirage-e7b94
cd /Users/scott/Hermes/pso-decomp/pso-decomp-f3
rm -f build/GPOE8P/src/pso/enemy/TObjEneMe3ShinowaMirage_800E7A70.o && ninja build/GPOE8P/src/pso/enemy/TObjEneMe3ShinowaMirage_800E7A70.o
/opt/homebrew/opt/binutils/bin/gnm -S build/GPOE8P/src/pso/enemy/TObjEneMe3ShinowaMirage_800E7A70.o   # gate: 0x510
/Users/scott/.hermes/installs/60d8a79da6991a71/environments/28d86d1068e44adc8d1a5d2ca8c63c2c/venv/bin/python3.14 \
  /Users/scott/.hermes/profiles/pso-decomp/skills/pso-decomp/scripts/one_shot_diff.py psov3/pso/enemy/TObjEneMe3ShinowaMirage_800E7A70 800E7B94
