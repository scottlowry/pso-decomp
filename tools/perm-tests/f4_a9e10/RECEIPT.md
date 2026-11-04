# f4 card a9e10 — TObjPlayer__sub_801A9E10 (876B, era ~219) — FLOOR 95.671234, gate 0x368 vs 0x36C (-1W)

Branch `card-player-a9e10` @ base 5695627b. Champion commit `34a7e8f2` (pass3).
Committed-tip clean rebuild verified 2026-11-04 02:52 PST: gnm 0x368, one_shot
95.671234 (218 rows vs era 219), siblings __dt__13TUnk_804C349CFv 100.0/0x158
and get_photon_blast_chain 100.0/0xa4 byte-exact. Full ninja green;
report_delta vs baseline-e175bcd9: regressions 0, New exact 0, linked_units
3309 +0 (unit NOT completed — 3-fn unit stays open at this floor).

## Anatomy (all byte-verified, era .s slots quoted)
- 6-arg ctor-like: (self, client_id, targets[0x18-stride], arr, flag, val);
  new(0x98) self (caller PhotonBlastResults bl-site). GSP screen 0. Zero FPR.
- Prologue mflr..stw27 (14) + li r9,0 / li r6,-1 / vt addis+addi+stw 0x18 /
  lis 1 + subi 0xFFFF (slot 18 reg r4; ours r5 — scratch-rank color,
  def-order coupled to loop1 wall) / li r0,4 + sth 0x3c + li r3,0 + 4x
  field stores (25 slots, all matched).
- loop1 dt addi 4 / li r0,0: lwzx arr; addi r0,r3,0x90; addi r7,r9,0x70;
  addi r5,r9,0x50; addi r8,r8,1; addi r3,2; stwx r8,r28,r7; addi r9,4;
  stwx r6,r28,r5; sthx r4,r28,r0; bdnz (10). era absorbs C into index
  subtree, raw self base, 3 offset vregs.
- field stores 0x40/0x28 (charge=0, count=4) + 2x player path:
  get_player_by_client_id -> get_photon_blast_charge / stw 0x38 (verbatim).
- loop2 dt: addi r0,r3,0x60 + stwx 0xFFFF x4 (verbatim).
- loop3 targets-walk (era, 24 slots): bl 80313114; extsh; cmpwi -1; bne;
  stw n,0x28; b tail; mr; bl; extsh r3; addi r0,r31,0x50; stwx (RAW r28);
  mr; bl get_section_id; addi r27; addi r0,r31,0x60; clrlwi; addi r31,4;
  stwx (RAW); addi r30,0x18; blt; mr; bl get_player_by_client_id;
  stw 0x38 — two-succ-bl shared-mr pattern landed in pass2 (probe2 verbatim).
- loop4/5 + state: dt twin __dt__13TUnk_804C349CFv VERBATIM (matched-fn in
  same TU). Dropped id/rec locals — re-spelled
  photon_blast_sequence_table[self->ids60[i]] per site; alias-store-forbids-CSE
  remat chain lands byte-exact (probe3: all loop4/5 slots match). loop5
  addi r9,r5,0x10 + bdnz -48 twin = fold direction proof.
- loop6 apply_photon_blast_action_hold__Flll per-i (era). loop7 flag4c!=0
  tail: get_player_by_client_id; beq; lwz; rlwinm; lwz; mtlr; addi;
  rlwinm r3,r3,2,0,22; bl freeze (3x clamp verbatim, era polarity != 0).
- loop3 extsh slot color (era r0/r3 alternating = def-binding) follows
  loop1 RA wave — same wall.

## CLOSED-class list (all byte-verified inert on build A)
1. Shared-base CSE in loop1/loop3: era absorbs constant into index subtree
   (addi rD,rIV,C + stwx raw r28); 2.6 m2c flattens sum(self, IV, C) into
   (self+IV) shared base + disp store. Levers tried, byte-verified inert:
   paren variants ((0x70+i*4) vs +0x70+i*4), named s32 offset temps (prop
   folds; byte-identical 95.671234), typed-member spelling (probe1 -0x30),
   #pragma opt_common_subs off function window (shape UNCHANGED, +1W
   over-remat elsewhere, 93.42 — sharing is parser canonicalization, not
   common-subs). = parser address-normalization fold stratum (rosetta's loop1
   construct is the version-class probe; not run, time-box).
2. slot-18 0xFFFF reg color (r4 vs r5): scratch rank driven by def order with
   loop1's offset-vreg class; follows wall 1.
3. loop3 extsh dest ping-pong (r0/r3) and addi r31,0x60-then-clrlwi slot
   order: def-binding re-rank under the same wave; follows wall 1.

## Gate state
FLOOR 95.671234, -1W (0x368 vs 0x36C), 218/219 rows. The -1W is exactly the
loop1 shared-base form (3 addi + 3 stwx = 6 era; 2 add + 3 disp-st = 5 ours).
No fabrications: no phantom stores, no invented names, closed-class list has
byte-verified receipts on every entry. Builds used: control + 4 probes +
confirm = 6 (cap 8+1).
