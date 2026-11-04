# KIT_STATE — f3 campaign: TAdEndText__sub_8001A998 (card t_6e3aacdf, branch card-endtext-v1)

Gate: symbols.txt row `.text:0x8001A998 size:0x3F4` (253 insns). Era asm:
`build/GPOE8P/asm/pso/menu/TAdEndText.s` lines 21-304. Unit split owns
`.text 0x8001A988-0x8001B424` ONLY (no data/pool claims → pool-literal
named-externs pass the ownership screen by construction; all referenced
.sdata2/.rodata/.data addresses are UNCLAIMED windows).

Unit: 14 fns, 13 matched siblings, this is the ONLY open fn → unit is a
linkage blocker (current .o: `U TAdEndText__sub_8001A998`).

## Semantics (decoded, naming evidence = TEndingPic precedent, names stay fn_ placeholders)

`TAdEndText__sub_8001A998(s32 color, u8 *str, f32 x, f32 y, f32 scale)` =
**big-font ending-text line renderer** — verbatim structural twin of the
100%-matched `draw_small_font_text` (src/pso/misc/TWindowSubStatusDisp_800FBD74.cpp:172),
with the glyph-quad build INLINED and grid metrics. Sole caller:
render__10TAdEndTextFv (matched, 100%) case 0x23 — era callsite leaves
r4 = `TAdEndText__credit_script_lines[i]` (string INCLUDING the '#' marker;
the sub's '#' case = marker-skip `continue`). No PTMF/vtable refs to
0x8001A998 in psov3.elf data scan (zero hits) — pure direct-call leaf.

## Anatomy table

| feature | era |
|---|---|
| frame | 0xc0; stw lr @0xc4 |
| FPR saves | f31,f30,f29,f28 (stfd+psq pairs @0xb0,0xa0,0x90,0x80) |
| GPR bank | stmw r27 @0x6c (r27..r30, 4 homes) |
| entry binds | f1→f28 (x-acc), r3→r28 (color), f2→f29 (y), r4→r29 (str), f3→f30 (scale), li r30=0xfe (lastpage=254) |
| loop head | lbz c,*str; str++; mr r31,c (id default); cmpwi 0x23 beq→loop-test (skip '#') |
| y0 | box.y0 = (B404(c) bit0x40) ? yb : y; yb = lbl_805D7DF0 + y |
| class chain | B3EC(c&0xD0): B3D4(0x80)→id=c-0x41 (A-Z); B404(0x40)→id=c-0x3d; B3BC(0x10)→id=c+0xe; (else id=c) |
| switch | (s8)c: 0x28→0x1a 0x29→0x1b 0x2f→0x1c 0x2e→0x1d 0x3a→0x1e 0x26→0x1f 0x7e→0x20 0x5e→0x21 0x2d→0x22 0x2c→0x23 0x3c→0x48 0x3e→0x49 default→0x52; MWCC binary tree (12 cmpwi, out-of-line li+b arms join @AB90) |
| missing-glyph (id==0x52) | x+=DF4; box[2]=DF4+x0(box[0] reload); box[3]=DF8+y0; box[4..7]=DFC(0.0f); store order 18,10,14,1c,20,24 |
| normal path | row=id/36; q1=id-row*36; q2=id-row*36 (REMAT pair, spelled twice); c6=q2/6; cq=q1-(q1/6)*6; w=lbl_804345E0[row*36+q2] (108 f32 metrics, unclaimed .rodata); y1=13+y0 FIRST store @0x14; b=(u8)(s32)(DF8*((f64)c6-109.0)); a=(u8)(s32)(DF8*((f64)cq-109.0)); x1=x0+w; x+=w; u0=(f32)a*E00; v0=(f32)b*E00; u1=((f32)a+w)*E00; v1=(13.0+(f32)b)*E00; store order 20,18,1c,24 |
| int→f64 | xoris 0x8000 + lis 0x4330 stw-slots (×6 slots 0x28..0x60) + fsubs vs lbl_804347A0 (2^51+109.0 double) / lbl_804347A8 (2^51.0 double); fctiwz ×2 (b, a); u8 = clrlwi 24 of fctiwz low word |
| join | page=(u8)id/36 (divw RE-materialized at AD18); if(page!=lastpage){set_draw_texture_and_color(page,color); lastpage=page;} draw_textured_quad_at_depth(&box[0],scale) |
| tail | loop test `lbz r0,0(r29); extsb.; bne`; then bl get_player__20TWindowSubStatusDispFv (NO return-value write) |
| ps-arith | ZERO ps_ ops (psq_st/psq_l prologue/epilogue spills only) → early-floor doctrine NOT triggered |
| divw | ×4 (36, 6, 6, 36) — hardware divide, NO magic-expand |
| calls | set_default_alpha_blend__Fv, begin_screen_draw(1), set_texlist__FUl(loaded_font_texture_list), B404,B3EC,B3D4,B404,B3BC, set_draw_texture_and_color, draw_textured_quad_at_depth, get_player |
| data | DF0,DF4,DFC,E00 f32 + TAdEndText__data_805D7DF8(=13.0f, x2) .sdata2 UNCLAIMED; lbl_804345E0[108 f32], lbl_804347A0/A8 (f64 magics) .rodata UNCLAIMED; lbl_804F5800[0x100] .data via helpers; TAdEndText__loaded_font_texture_list .sbss |

## Per-character store-order fingerprint (box = 8 f32 @0x8..0x24 = Quad{x0,y0,x1,y1,u0,v0,u1,v1})

missing: stfs x0(8)@AA14 pre-id, y0(0xc)@AA34; then 18,10,14,1c,20,24.
normal: 14 (y1) @AC54 → 10 (x1) @ACA4 → 20,18,1c,24 @AD00-AD0C.

## V2 FRONTIER (ranked)

1. [visit-1] Skeleton transcribe (twin-parallel + era-order), 5-arg decl + render callsite string arg → control probe, gnm size gate.  [IN PROGRESS]
2. TAIL-LI polarity set: y0 ternary (beq-zeroarm = `if(B404) yb else y` ✓ authored), store-order permutations for box[4..7] missing-path (era 18-first), switch case order (era tree median = sorted insertion? probe 11-case natural).
3. PER-BRANCH remat law: q1/q2 DOUBLE spelling (mulli+subf then mullw+subf) — era REMAT = source spelled `id - row*36` twice → opt_common_subs off function-window pragma push/pop candidate IF ours CSEs to one chain (-4W). divw RE-materialization at AD18 (page) = `id/36` spelled a 2nd time (test+arg at callsite? era: `if ((u8)id/36 != lastpage) set(id/36...)` = two spellings — already authored).
4. Prologue scheduler: li r30,0xfe sits in the arg-bind block (A9DC, BEFORE set_default_alpha_blend) → `s32 lastpage = 254;` decl at top with init; yb assigned after set_texlist (declare-assign split per raw-disasm ctor-asm-tells).
5. f64 magic slots: era interleaves stw-4330 hoists (0x28,0x38,0x58,0x60,0x48,0x50, 6 slots, 4 stores) — def-binding/scheduler stratum; if rows-identical-multiset: park as pin class per REC/RINGS law.
6. callee bank: stmw r27 (4 GPR homes: c,color,str,lastpage + id→r31 scratch? r31 IS saved (stmw r27..r31? NO: stmw r27,0x6c saves r27-r31 = 5 homes over 0x6c..0x7c (5×4=0x14, frame slot 0x6c..0x80 = 5 regs ✓). Homes: r27=c, r28=color, r29=str, r30=lastpage, r31=id. REC-decl-LAST (id → r31 = top rank = declared FIRST per TLobby-803C0238 flip law "declaration to END = binding rank LOWEST (r27)" → c decl LAST, id decl EARLY).

## CLOSED-CLASS / DO-NOT-RE-ROLL (grows per visit)

- (empty at visit-1 start)

## Cold-start commands (verbatim)

```
cd /Users/scott/Hermes/pso-decomp/pso-decomp-f3
git branch --show-current   # card-endtext-v1
PY=/Users/scott/.hermes/installs/60d8a79da6991a71/environments/28d86d1068e44adc8d1a5d2ca8c63c2c/venv/bin/python3.14
rm -f build/GPOE8P/src/pso/menu/TAdEndText.o && ninja build/GPOE8P/src/pso/menu/TAdEndText.o
/opt/homebrew/opt/binutils/bin/nm -S build/GPOE8P/src/pso/menu/TAdEndText.o | grep -i a998   # gate: size 0x3f4 T
python3 /Users/scott/.hermes/profiles/pso-decomp/skills/pso-decomp/scripts/one_shot_diff.py psov3/pso/menu/TAdEndText sub_8001A998
```
