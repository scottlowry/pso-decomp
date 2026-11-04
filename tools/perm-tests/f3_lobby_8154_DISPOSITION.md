# card-lobby-8154 (t_89487c5b) — TLobby__sub_80228154 FLOOR disposition, 2026-11-03

Tree f3, branch card-lobby-8154 @ base 5695627b. Tip 2f778e94.
Gate: 0x3AC (235 insns, symbols.txt size:0x3AC). Committed-tip state: **0x3A8 (234), one_shot 86.48085, rows 208**. NOT byte-exact → no unit completion (unit 43/44; linked_units stays 3308).

## Anatomy (fully decoded, all regions structurally aligned)
Fish-quad draw: guards (self, self+0x18) → set_global_param__8TObjFishFl(self+0x18) →
e = self+0x1c base + idx*0x14; 8 s16 corner deltas via int-neg (neg+xoris) magic;
4 s16 heights via **plain (f32)(s32)e[k]** (sign folded in magic; era head neg+xoris, era sites xoris-only);
pts[8] = 4 corners (0x18-0x24) + 4 heights (0x28-0x34) as ONE escape array passed to
draw_textured_quad_at_depth(r1+0x18) — heights DCE-class: array escape is what makes 58 insns of
height/clamp/copy live (q[4]+h[4] split = -76W, 55.78).
flags&1 = midpoint A/B (f30/f29) + z=C77C + matrix push/rotateZ(self+0x14)/rotvec/pop;
flags&2 = color = (u8*)&color writes of (s32)(C780*mmc[k]), init color=-1;
flags&4: pts[6]=pts[4]; pts[4]=pts[4] (3-insn lfs/2×stfs); flags&8: pts[7]=pts[5]; pts[4]=pts[5];
tail: C784/depth in f31 (arg3 reassign), begin_screen_draw(bool), tex=e[8], get_player tail call.

## Winning levers (this unit)
1. pts[8] escape array (unit of work: heights+copies+reload lfs = +73W)
2. site spelling (f32)(s32)e[k] * scale with **scale-first** mul (dest = scale reg): kills fneg/neg, -4W→gate-track
3. #pragma push/opt_common_subs off window: forces era's per-site pool remat (lfs C770/C774 + lis pairs, +6W, 83.70→86.48)
4. u32 guard load → cmplwi (era slot 16); tail (arg2&0x20) != 0.

## Residual (gate -1W + ~25 real rows)
- Tail bool: era rlwinm; subi 0x20; cntlzw; extrwi = 4-insn bounded-quotient normalize (== (arg2&0x20)/0x20 for v∈{0,32}).
  2.6 spells: `!= 0`/`? 1:0`/`== 0x20` → extrwi (1, -3W); `/ 0x20` → rlwinm+srawi+addze (3, +1W OVER: 0x3B0).
  No spelling emits era's subi+cntlzw chain = era int-to-bool stratum (def-binding kin; CB44/EXTSH-BIND family). PARKED — do not re-roll bool spellings.
- Head xoris/neg emission order + slot-pair interleave (era c4,c0 | our c4,c0,c6,c2 birth mix; LCS-slide rows).
- fpool scratch colors (f5↔f6, f1↔f2 sites; f3/f4 flags&1 adds) = regcanon lineage.
- Color stb emission order (era pb[3],pb[2],pb[1],pb[0]; ours 2,3,1,0) + fctiwz/stfd interleave.
- Pool-name rows: 2^52+2^51 magic renders @223 vs lbl_8044C9F0 (unclaimed .rodata gap; unnameable while staged per draw-desc law; resolves at link).

## ps screen
PS=6: ALL are prologue/epilogue psq_st/psq_l bank spills (use_lmw_stmw on f29-f31 pairs). Zero paired-single arithmetic in body → anatomy pass, not a ps-wall.

## Siblings
44 T symbols in unit .o: 43/44 sizes era-exact (only target at 0x3A8 vs 0x3AC). Insertion position between sub_80228118/clear_ready matches asm emission order.

## Next-visit opening
Only path to gate = +1 insn in tail region: era bool-normalize (stratum, source-inert at 2.6 — census datum) ⇒ park.
If a bind mechanism surfaces (era MAP), the residual colors are one def-binding sweep. Unit completion blocked on this 1 word.
