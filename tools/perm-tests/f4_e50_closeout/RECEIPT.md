# f4-11 close-out receipt — TObjPlayer__sub_80117E50 (card t_611ac2f6)

Branch card-117e50-recover @ base 5695627b. Tip: transplant 23d712f9.

## Seed recovery + survival (test #5)
- Staged blob /tmp/e50-tip.cpp == f9c2b507 content (diff verified, Oct-28 true tip).
- Tip sweep: successor 81767f007 (fleet/f3 RAISE, Nov-1) = content tip; re-anchored
  shape == current base seam (ctor fns fold-shipped to TItemProArmor.cpp).
- Fold-wave rename applied by ADDRESS: get_field_3e4 -> get_floor (TObjPlayer.h:375,
  evidence: 100.0 sibling call site).
- CONTROL PROBE: rm .o + ninja (MWCC line printed, rc=0) + gnm OURS 0xC4 gate-exact.
  one_shot on committed tip: 99.4898, rows orig 49 / ours 49, size 196.
  SEED SURVIVAL = EXACT vs 99.49 (99.4898) after 6-day drift / TObjPlayer fold waves.

## Ring classification (from one_shot rows before spending)
Residual = ONE uniform 2-reg swap ring, multiset-identical: {me r27 <-> mask r28}
at slots {8,10,12,25,30}; bank otherwise era-exact (idx/counter r25, result r26,
key r29, idx-conv r30, other r31). REAL:0 (matches 81767f007 word-diff audit).

## boxdrop-v5 bisect (twin-rung-first; 3 probe axes, 1 repo build)
- P1 TWIN RUNG (zero-build; twin count_nearby_players_with_shield is 100.0-paired
  byte-exact => our decode == era decode): twin binds first bl-result class
  (mr. r29,r3) to ascending low-free seat; i-conv->r31, key->r30. Twin pins the
  era pattern (ascending post-call class) on this terrain.
- P2 MASK RUNG (zero-build scratch TU twin skeleton + mask construct, unit-exact
  GC/2.6 -O4,s flags via probe_compile.sh): reproduces OUR inversion on twin
  terrain — mask addi-class -> r27 BELOW me mr-copy -> r28. Inversion carrier =
  the mask def-materialize class (lwz/clrlwi/addi), terrain-general, NOT
  body-context. Explains census inertia (22 spellings + 137k perm iters inert).
- P3 VERSION RUNG (11 versions on P2 body: 1.0,1.2.5n,1.3,1.3.2,2.0,2.0p1,2.5,
  2.6,2.7,3.0a3,3.0a5): 1.0/1.2.5n invert (mask r25 < me r26, bank r23, off-gate
  frame 0x38); 1.3-2.7 ALL invert identically (mask r27 < me r28, bank r24 = pin);
  3.0a3/a5 fold me away. ZERO/11 emit era [me low, mask high] on mask-bearing
  terrain. Fingerprint table above; era ascending post-call class = zero emitters.

## Verdict
COPY-BIRTH-TOP-PIN (sealed v5-style): twin rung pins era pattern; mask-class
carrier inverts in 100% of gate-live states (era ordering needs the era
allocator's ASCENDING post-call class = era-scheduler-preference; ASK-1 memo
family, handle_box_drop_directive {id<->b1} kin).
Floor 99.4898 stands; status=floor; unit INCOMPLETE (all-or-nothing: sibling
100.0 + this 99.4898) => linked_units 3309 NOT unlocked; no claim.

Budget: 1/6 in-tree builds (control), probes 3/4 (P1-P3), 0 builds on probes.
Prior census refs: tools/perm-tests/TObjPlayer_80117E50/census (f3, 81767f007);
Oct-28 10-spelling + GC/1.3.2 confirm (f9c2b507).
