# card-dhcp-req-421620 (t_5943ed65) — dhcp_request_step @0x80423E80, gate 0x3AC (235 insns)

Status: PARKED at 98.27234% (one_shot, committed tip 2fd4c051 after c7 rebuild, .o = 0x3B0 = 236 insns).
Branch tip content = twin-parallel transcription; 41 siblings size-stable (gnm -S, 42/42 symbols,
only mismatch = target). Gates on tip: ninja rc=0, report_delta --check "New exact 0, regressions 0",
check_pr PASS, link_units OK (3308).

## Anatomy (all landed byte-shape)
- PS screen: zero float ops in era block (235 insns, integer/lwz/stw). twin_parallel_depth: HIGH —
  switch-head decision tree, case-1 send block, close-socket inline (dhcp_close_socket), timeout
  retry shape, and tail `return dhcp_state` all transcript-parallel to 100.0 sibling
  dhcp_discover_step @0x8042422C; frame slot map src@0x14/dst@0x28/buf@0x3c = sibling's decl-order tail.
- Statement-for-statement transplant landed 235/236 rows; residual = 1 instruction class:

## Residual: DEF-BINDING PROLOGUE PIN (era binds net @ha/@l IN-PLACE to r31)
  era:   mflr; lis r3,lbl_805C1E00@ha; stw r0,4; stwu -0x58; stw r31,0x54; addi r31,r3,@l; addi r3,r1,0x48; bl
  ours:  mflr; lis r3; stw r0,4; addi r0,r3,@l; stwu -0x50; stw r31,0x4c; mr r31,r0; addi r3,r1,0x44; bl
Every row after slot 2 is a uniform +1-shift; frame 0x50 vs 0x58 (era carries 3 allocated dead
words: 0x44 between buf/now, 0x4c/0x50 above now).

## Inert spellings (real TU, committed candidates c1–c8)
c1 base twin; c2 decl-order perm (net/delta/now/server/...); c3 &arr[0] decay; c4 decl-initializers
(u8 *net = lbl; u32 delta = 0; u32 server = 0xFFFFFFFF); c5 opt_propagation-off function window;
c6 register-kw; c7 = c4 cleanup (SHIPPED TIP); c8 dont_inline-on window (-14W, inlines
dhcp_close_socket, binding unchanged — REVERTED); v3 TLobby* typed birth (no flip).

## Rosetta (scratch/rosetta, unit flags, self-contained binding_probe; 20 versions)
1.0–1.2.5n: bind IN-PLACE (addi r31,r3,@l) at probe scale (62 insns, frame 0x48).
1.3–2.7: fresh-reg bind (61). 3.0x: (60). Probe mutations at 1.2.5n: +file pragmas → split (home
rotates to r30); +TLobby member-call birth → split; +3-case switch → split. Split appears at
era-context scale for every real-TU permutation tried; era's 1.2.5n emitted in-place from real
source → def-binding/def-stratum pin kin (qvm-edc20 family: 22 inert spellings precedent).
Capability exists in the pinned version; it is not reachable by source spelling in the 236-insn
real-TU context.

## Next-visit cold start (do NOT re-roll c1–c8 spellings)
1. Gate: gnm -S build/GPOE8P/src/pso/unk/text_80421620.o | grep request_step  (need 0x3AC)
2. python3.14 ~/.hermes/.../scripts/one_shot_diff.py psov3/pso/unk/text_80421620 dhcp_request_step
3. Open frontier: era dead slots 0x44/0x4c/0x50 = 3 slot demands our 1.2.5n does not allocate
   (siblings release/discover frame-reproduce exactly — request era body carries allocations the
   transcription lacks). A source construct that allocates 3 scalar slots AND binds @l in-place
   would collapse both. Candidates untested: struct-typed local passed by address; a second
   get_time_ms-style &arg path; era `net` as array-index base with &net escape.
4. Linked_units: unit is 41/42 fn matched; landing byte-exact completes 42-fn unit ->
   linked_units 3309 claim (config add = integrator).
