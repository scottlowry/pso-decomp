# KIT_STATE — TEF_LensFlare::render (0x800812D0, gate 0x608 / 386 insns) — lane f3, card t_893ce5b5

Branch `card-lensflare-1544` @ base 5695627b (tree tip = e175bcd9, upstream incl #191).
Unit `psov3/pso/effect/TEF_LensFlare` (6 fns, code 14.03 at intake; sole open fn = this one).
Profile: `GC/2.6`, `-O4,s -inline off -use_lmw_stmw on -sdata2 4 -char signed -lang=c++`.

## Committed frontier

| sha | state |
|---|---|
| 912fec98 | full anatomy transcription, 90.481865, size 0x5FC (-3W) |
| bdf57f3e | +item address home (r31) + def-table `+9` index fold, 90.17876, 0x604 (-1W) |
| 9577ffc9 | **CHAMP: gate-exact 0x608 (386/386 rows), 90.62953** |

## GATE #1 — GSP ps-arith screen (report law: counts documented)

`ps_screen_count (GSP) = 0`. Zero `ps_add*/ps_mul*/ps_sum/ps_madd*/lhfs`, zero 2+reg ps
addressing. All PS-family rows are the Gekko spill map: 9× `stfd+psq_st` prologue /
9× `psq_l+lfd` epilogue, base+disp(r1), QM=0 → **benign, not a wall**.

spill_map (FPR-pressure map, all confirmed reproduced byte-shape by our compile):
f31@0x170/0x178, f30@0x160/0x168, f29@0x150/0x158, f28@0x140/0x148, f27@0x130/0x138,
f26@0x120/0x128, f25@0x110/0x118, f24@0x100/0x108, f23@0xf0/0xf8 · `stmw r28,0xe0` (r28..r31)
· LR@0x184 · frame 0x180. 9 denied FPR homes + 4 GPR homes = the bank; our build lands
the identical map on the first author pass.

## Anatomy (decoded, evidence-cited)

Head: `get_render_pass()==0` → return; `camera_ctrl_instance==NULL` → return; 0x28-byte
local `item` memberwise zero-init (8 f32 + u32 + u8 + u16, color first);
`set_additive_blend()`; `if (self->0x68 >= 0.0f) { k = 10.0f*self->0x68; if (is_player_near(k*k)) return; }`;
`begin_effect_render()`; view = self(0x38,3C,40) − cam(0x178,17C,180); `vec_squared_length`;
`if (0.0f != len2) normalize_vector`; `push_matrix_from(identity_matrix)`; dir = lbl_80438E40
(= (0,0,−1), 3-word inline copy); `rotate_matrix_y(0, cam->0x194)`; `rotate_matrix_x(0, cam->0x190)`;
`rotate_vector_by_matrix(0,&dir,&rot)`; `pop_matrix`; `dot = vec3_dot(&rot,&view)`;
`if (dot > 0.0)`: `set_depth_buffer_settings_1`, `project_world_to_screen(0, self+0x38, &scr)` …
finally `end_effect_render()`.

Three draw blocks, each: colour bytes → `VecCopy(&item.pos,&point)` → `begin_screen_draw(1)` →
`TObjFish::set_global_param` → `set_draw_texture_and_color(…, -1)` → 8-float quad
{x0,y0,x1,y1,rgba floats (0,0,1,1)} → `set_constant_material_color(item.color)` →
`draw_textured_quad_at_depth(&quad, 0.5f)` → `TWindowSubStatusDisp::get_player()`.

1. GLOW (dot > 0.99): `u = (50.0f*(dot-0.98f))²`; α = `255.0f*(0.9f*u)` → `(s32)` via
   fctiwz/stfd/lwz/stb; size = `20.0f*u`; record 15 (disps 0x25c/0x260/0x26c/0x270).
2. HALO: α = `dot>0.6 ? 3.0f*(dot-0.6f) : 0.0f`; α⁴ chain (a²,a³,a⁴ self-accum);
   colour 0xffffffff; `center_dx = 320.0f-scr.x`, `center_dy = 240.0f-scr.y`; size 1.0;
   record 9 (0x16c/0x170/0x17c/0x180).
3. REFLECTED ELEMENTS ×9: cursor = `*(void**)(this+0x90)` (=
   `lens_flare_reflected_element_descriptors`, 0x8048E040, stride 0x18: s32 def_index,
   f32 offset, f32 size, f32 alpha, f32 color_mul);
   `fnmsubs`: `sz = size*(1.0f − (1.0f−α⁴)*alpha)`, clamp `<0 → 0`; colour byte0 =
   `(s32)(255.0f*(α⁴*color_mul))`; point = `center_dx*offset + scr.x` (fmadds, both axes);
   `item.sx = sz; item.sy = (f32)(f64)sz;` ← **the frsp**; defs = `lbl_804C5820[def_index+9]`
   (mulli 0x28 + add + 0x16c/0x170/0x17c/0x180 disp, rematerialized 3× per iteration).
   Tail: `cmpwi r28,9 / addi r30,0x18 / addi r28,1 / blt` then `restore_saved_depth_alpha_state()`.

Pool-record identity proof: 0x25c = 15*0x28+4, 0x16c = 9*0x28+4 → the record type is the
repo's `ParticleDefinition` (0x28: flags, texlist, texture, uv_count, uvs, width, height,
color, texlist_index, sprite_type) defined in `src/pso/misc/TParticleCtrl_801E5330.cpp:136`;
`+4 = texlist`, `+8 = texture`, `+0x14 = width`, `+0x18 = height`. `lis @ha + addi @l` =
the table base itself (NOT a +0x5820 relbase — the printer reuses the symbol name for the
0x5820 immediate).

## Twin screen (5 siblings + corpus)

Unit siblings are tiny (dt 0x58 / ct 0x6C / 3 stubs) — no intra-unit twin. Corpus
callee-set screen over 28806 era blocks: best 11/23 shared callees =
`render__13TUnk_8048E778Fv` (ParticleBallistic, 100%), then the 100%-matched
`TQuadSpriteCol::render` (quad struct `{x0,y0,x1,y1,col.rgba}` + `draw_textured_quad_at_depth`
+ `set_global_param`/`set_draw_texture_and_color`/`get_player` tempo — transcribed idiom source),
`draw_sprite_quad__13TUnk_8048E778Fl` (camera head: push_matrix_from/rotate/vec3_dot),
`project_to_screen__13TObjTombstoneF*`. No verbatim structural twin: this fn is its own shape.

## Residual triage at the champ (229 unlinked-view diff rows)

* ~54 rows = `.sdata2` pool-name display (`@NNN` vs `lbl_805D9338`) — link-gated naming class,
  not codegen; resolves only in the linked view (report_delta is the truth).
* ~65 rows = frame-slot shift: era reserves one 4-byte slot at 0xac (item base 0xb0, ours 0xac).
  Refuted in-session: `union {f64; FlareVec}` inside the item type (GC/2.6 does not 8-align
  locals → byte-identical .o). Era-layout/reserved-slot stratum (PHANTOM-FRAME-SLOT kin).
* ~65 rows = FPR/GPR home-ring rotation (era dot→f29, glow_sq→f23, α→f25; ours f28/f24/f27)
  and the self↔cursor reg roles — def-binding/sched-window pin class (closed list).
* ~45 rows = scheduler interleave order inside the three draw blocks (same multisets).

## Next-visit frontier (ranked)

1. The 4-byte slot at 0xac: screen the era's whole local set for a 4-byte object we fold away;
   try `#pragma push/opt_propagation off` FUNCTION window (mid-body windows are byte-ignored)
   as a single probe; if inert, era-layout memo.
2. Loop-tail form: era `cmpwi(r28,9) → addi → addi → blt` (pre-increment test, blt polarity);
   ours `addi → addi → cmpwi → ble`. IV strength-reduce = CLOSED class, do not re-roll.
3. FPR home ring: 20-version rosetta fingerprint only if a bind mechanism is found (closed).

## Cold-start commands

```
cd /Users/scott/Hermes/pso-decomp/pso-decomp-f3
rm -f build/GPOE8P/src/pso/effect/TEF_LensFlare.o && ninja build/GPOE8P/src/pso/effect/TEF_LensFlare.o
/opt/homebrew/opt/binutils/bin/gnm -S build/GPOE8P/src/pso/effect/TEF_LensFlare.o | sort -k4
python3 <skill>/scripts/one_shot_diff.py psov3/pso/effect/TEF_LensFlare render__13TEF_LensFlareFv
```
