# card-photon-464 floor receipt — spawn_photon_blast_attachment_effects (t_2e8869c1)
Gate 0x1D0 (symbols.txt 11551, .text:0x801A7748). COMMITTED TIP b806dbd8:
gnm OURS size=0x1d0 EXACT; one_shot match=95.50862 (116/116 rows).

## PS gate #1
ps-arith screen on era block (asm .s lines 519-644): 0 ps_ insns = PS-CLEAN.
Twin screen: spawn_photon_blast_opening_effects (0x801A7428, matched sibling,
same formulaic summon-attach family: table-claim -> matrix pipeline -> emitter
spawn) + RX-pump hoist levers. 7 callers (TPhoton{Golla,Mylla,Leilla,Estlla,
Pilla,Youlla,Farlla}) pass (self, 0..6) = table index into
photon_blast_attachment_table[7] (Group_801A7428 stride 0x10 confirmed).

## Anatomy (all names = era reloc/symbols evidence)
frame 0x60; bank stmw r21,0x34(r1) (11 regs r21-r31 all homed); LR 0x64.
slots: dir[3]@0x08, rot[3]@0x14, v[3]@0x20; def=PhotonAttachmentDef_801A7748
stride 0x20 (fields +0,+4,+8,+C,+10[3],+1C); effect record: obj@+0 (stwx
r3), flag=def+0xC -> +0x10, copy_xyz vec -> +0x14 (writes pos at +0x14;
matched update_photon_blast_attachments READS pos at +0x4 = era-side
layout quirk, kept as authored via Eff_801A7748).
control: bottom-test while (cmplw unsigned, count u32@0x100); guard
v[2]!=0||v[0]!=0||v[1]!=0 (three bne, tail zero-liquir at 0x7d0, TAIL-LI
positive-cond layout); mem_alloc(count*32) slwi r3,r0,5.
Callees: mem_alloc, copy_xyz__FPvPv, push_matrix_from, rotate_matrix_z/x/y,
matrix_mult_vec, pop_matrices, direction_to_rotation_xz__FPUcPlPl,
create_timed_particle_emitter_with_angles__FPvPvllll; data:
photon_blast_attachment_table, identity_matrix, lbl_80446A38 (.rodata size
0xC; splits.txt has NO .rodata window for this unit -> extern naming safe,
pool-literal ownership screen PASS).

## Grind log (5 of 8)
p1 author (frame/guard/loop)            86.39  0x1D4
p2 reverse array decls (v,rot,dir) +
   negated ||-guard compute-first +
   g-before-self                        94.01  0x1D4
p3 rot_z decl-init                      93.44  0x1D4  INERT (inert;
   hoists addi above stmw - revert p4)
p4 self stmt-cast after g               94.01  0x1D4  INERT (self binds r21)
p5 inline &rot[2] at direction_to_
   rotation_xz call                     95.51  0x1D0  GATE EXACT
   (named pre-loop rot_z home pays addi r0-scratch + mr split = +1W;
    inline spelling collapses it to one addi + mr r5 chain matching era
    insn count exactly)

## Residual (parked — def-binding bank ring, CLOSED class)
Ring map ours->era: self 21->22, g 22->21, i 23->24, u 24->23, defs 28->25,
def 29->26, rotz 30->27, a 27->28, c 25->29, b 26->30, base 31=31. Non-uniform
permutation + clrlwi birth slot (O:93 N:88) + pre-loop pair order
(O:18,19 addi r27/addi r31 vs N: addi r31/addi r30). qvm-edc20 law: decl/
stmt permutations rotate the ring, cannot reach era k-rotation. p2/p4 confirm
inertness of the top pair. All 35 residual rows are identical opcodes,
register colors only.

## Sibling safety
gnm on tip: spawn_photon_blast_opening_effects 0x114, free_photon 0x2c,
update_photon_blast_attachments 0x9c, copy_effect_params 0x3c — unchanged.
Unit code 86.54 -> (per-symbol) floor; unit NOT complete => linked_units
3308 stands (3309 claim blocked by this row).
