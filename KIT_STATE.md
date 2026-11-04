# KIT_STATE V2 — f3 campaign: TAdEndText__sub_8001A998 (card t_6e3aacdf, branch card-endtext-v1)

State at visit-1 close: commit 307ee029, sub = 73.584984 unlinked, size 0x3E8
vs gate 0x3F4 (−3W / −12B). All 13 matched siblings re-verified 100.0 at era
sizes (render byte-stable under the 5-arg call; helper defs untouched).
Ladder: 70.26 (skeleton) -> 71.57 (block-scope protos) -> 73.58 (sign/maths fix).

Gate: symbols.txt `.text:0x8001A998 size:0x3F4` (253 insns). Era asm:
build/GPOE8P/asm/pso/menu/TAdEndText.s lines 21-304. Unit split owns .text
ONLY (0x8001A988-0x8001B424) -> pool-literal externs pass ownership screen.
All f64/f32/data addresses referenced: UNCLAIMED windows (805D7DF0-E04,
804345D8/5E0, 804347A0/A8, 804F5800, 805D49F4).

## CORRECTED anatomy (visit-1 decode; supersedes V1 numbers)

Constants (objdump -s verified): lbl_805D7DF0=2.0f, DF4=10.0f,
TAdEndText__data_805D7DF8=20.0f (glyph cell/y-advance), DFC=0.0f, E00=1/256.
lbl_804347A0 = f64 2^51+2^15 (SIGNED int->f64 conv magic, loaded once into
f3 via lfd 0x0(r6)); lbl_804347A8 = f64 2^51 (u8->f64 extraction magic, f5).
NO 109.0 EXISTS (V1 misread of conv magic). Glyph math:
a = (u8)(20.0f*(f64)(q%6)); b = (u8)(20.0f*(f64)(q/6));
u0=a/256, v0=b/256, u1=(a+w)/256, v1=(20+b)/256, x1=x0+w, y1=y0+20, x+=w.

Signature: sub(s32 color, u8 *str, f32 x, f32 y, f32 scale) -> void.
Binding: r3->r28, r4->r29 (cursor), f1->f28 (x-acc), f2->f29 (y), f3->f30
(scale), li r30=254 (lastpage). Bank stmw r27 (r27=c,r28=color,r29=str,
r30=lastpage,r31=id); frame 0xc0; f28-f31 stfd+psq pairs @0x80..0xb8.
Loop: while((s8)*str) { c=*str++ (lbz, NO extsb); id=c (mr); if(c=='#')
continue; box[0]=x; box[1]= B404(c)? yb : y (fmr-join, yb=2.0f+y); class
chain B3EC->{B3D4: id=(u8)(c-0x41); B404: id=(u8)(c-0x3d); B3BC:
id=(u8)(c+0xe)}; else switch(c) signed: 0x28->0x1a 0x29->0x1b 0x2f->0x1c
0x2e->0x1d 0x3a->0x1e 0x26->0x1f 0x7e->0x20 0x5e->0x21 0x2d->0x22 0x2c->0x23
0x3c->0x48 0x3e->0x49 default->0x52 (MWCC binary tree, 12 out-of-line
li+b arms); if((u8)id==0x52) missing-glyph path (x+=10.0f; uv zeros; store
order 18,10,14,1c,20,24); else normal (row=id/36; q=REMAT x2 (mulli+subf,
mullw+subf); c6=q2/6; cq=q1-(q1/6)*6; w=lbl_804345E0[row*36+q2] (108 f32
metrics, 2-stage add+mulli*144+slwi*4 lfsx); join: page=(u8)((u8)id/36)
PER-USE re-masks x2; if(page!=(u8)lastpage){set(page,color); lastpage=page;}
draw(&box[0],scale) }; get_player (no return write).
ps-arith: 0 (early-floor doctrine NOT triggered). divw x4 hardware.
Sole caller: render case 0x23 (era callsite passes r4=lines[i], NO PTMF,
zero data-table refs to 0x8001A998 in psov3.elf).
Naming proposal (report only, fn_ persists in code):
draw_big_font_text / ending_credit_line_render.

## V2 FRONTIER (ranked, visit-2 scope)

1. DEF-BINDING FUSION SET = the whole −3W + the row bulk. Era shapes ours
   cannot reach by decl/order (see closed classes): (a) head `lbz r27`
   binds c straight to callee home + single `mr r31,r27` (ours: lbz r3 +
   mr r27 + mr r31); (b) 3 class-arms write `clrlwi r31, r0, 24` INTO the
   id home (ours: clrlwi scratch + mr copy, +3W); (c) join per-use
   re-masks of id/lastpage + cmplw unsigned + divw-dest-r3->mr staging
   (era +2W there, ours folds to cmpw). Mechanism = def-binding lineage
   (QVM-EDC20 / TLobby-803C0238 / CB44 kin). Open probes for visit-2:
   comma-def at the 3 arm seams, `register` hints, block-scoped
   opt_propagation window, permuter round seeded from 307ee029 champ
   (harvest kit: perm-tests/ dir), split id into id_raw+id_u8 pair
   (era AB90 clrlwi r11 r31 = reads mask, arms write mask).
2. ERA-VERSION MARKER (fold-intel): fused (2^51+2^15) conv magic in era
   .rodata labels + per-use mask/CSE remat (6x lis-4330 stw slots vs our 4,
   divw kept, 2-stage metric addressing) all at 2.6 -O4,s = UNREACHABLE
   per BB-CSE/QVM decimal law; era object is pre-1.3 class (1.2.5 kin).
   Per FOLD-INTEL doctrine: offer the marker table to maintainer; run the
   4-version rosetta size fingerprint at the current spellings in visit-2
   BEFORE grinding (skill: EB4D4 precedent). No construction-hunt past
   census.
3. @76/@81 + @NN pool-name rows: our synthesized conv magics render
   anonymous vs era named lbl_804347A0/A8 (era defines them in its own
   UNCLAIMED .rodata window). Fix route = splits.txt Define-data claim
   (integrator/humarpso), NOT source. Free-row check per pool-literal law.
4. Slot-order residuals in normal block (stw 4330 pairs 0x28/0x38/0x48/
   0x50/0x58/0x60: era order 28,38,58,60,48,50; ours 28,38,60,48,50+shared
   0x58-remat) — scheduler stratum, count as multiset vs era AFTER 1 lands.

## CLOSED-CLASS / DO-NOT-RE-ROLL (visit-1 receipts)

- opt_common_subs off function-window pragma: BYTE-INERT at 2.6 on this
  unit (0x3E8/73.584984 identical). Reverted (307ee029..tip).
- id/lastpage decl swap: byte-identical fold (rank law inert at 2.6 basin).
- File-scope s32 helper prototypes: MWCC 'Conflicting types' ABORT vs
  include/pso/menu/TAdEndText.h u8 decl. FIXED via BLOCK-SCOPE s32 protos
  inside sub (417494 law) — kills all 5 caller clrlwi; helper defs stay u8
  (siblings byte-safe, verified 100.0).
- u32 q1/q2: emits divwu (era signed divw) — s32 required.
- (u8)(s32)(...) after fctiwz: +2 xoris (2W) — (u8)(...) direct.
- a/b s32 with (f32) casts: +2 xoris — u32 a/b.
- c as u8 local: cmplwi + no signed cmpwi — era c is s32 (cmpwi, lbz load,
  switch signed).
- str test `(s8)*str != 0`: era extsb.+bne tail-test REPRODUCED (slot
  233-235 clean).

## Cold-start commands (verbatim)

```
cd /Users/scott/Hermes/pso-decomp/pso-decomp-f3
git branch --show-current   # card-endtext-v1
git log --oneline -1        # >= 307ee029
rm -f build/GPOE8P/src/pso/menu/TAdEndText.o && ninja build/GPOE8P/src/pso/menu/TAdEndText.o
/opt/homebrew/opt/binutils/bin/nm -S build/GPOE8P/src/pso/menu/TAdEndText.o | grep -i a998   # gate 0x3f4
python3 /Users/scott/.hermes/profiles/pso-decomp/skills/pso-decomp/scripts/one_shot_diff.py psov3/pso/menu/TAdEndText sub_8001A998
```
Era fn dump: cache/scratch/endtext_fn.txt (scratch — re-dump from asm if gone).
