CB44 VISIT-2 DATUM — extsh-pair + p-rank are VERSION-CLASS (EXTSH-BIND family), not spelling
===========================================================================================
Base: master 7008688d (post-61FC). Re-land: diff 1e5823fa..04444f0d -- TLobby_804050DC.cpp
applies CLEAN to 7008688d (v1 brief said v6=3a991745 — WRONG state: floor fixup 04444f0d reverts
sibling ref->refbox renames, use 1e5823fa..04444f0d). Control probe reproduced 96.639595 @0x314.

PROBE LADDER (one_shot, unit psov3/pso/misc/TLobby_804050DC, sym sub_8040CB44):
  control      96.639595  146 diff rows
  B1 pkt-decl-last (after mskv, before pad)  -> 97.451775, FIXED 23 rows, BROKE 0, gate 0x314
      moved: a0/a1/a2 binds 29/30/31 -> 28/29/30 (era), pkt 27 -> 31 (era),
             f2-copy 28 -> 27 (era), r-home 28 -> 27 (era), + tail pair rows 173/182.
  E2 p-decl before word   -> byte-identical (inert)
  E3 p init-at-decl       -> byte-identical (inert; also breaks decl-order minimality)
  E6 opt_propagation off window -> 96.28426, size 0x318 GATE FAIL (+4B) — dead.

REMAINING STRUCTURAL ROWS after B1 (8):
  7,12   : p@r27 vs era r26 (era merges p INTO trip-counter r26; ours keeps i alone @26)
  50,51  : NetMemcpy arg-prep dst-r3-before-src-r4 vs era src-first
  54,55  : f cursor subi before bl (era) vs after (ours)
  68,69  : era single extsh. r0,r27(home),@test; ours extsh r0,r27 + extsh. r0,r0 PAIR
  (branch-target/jumptable @1592 rows = unlinked-view naming, resolve in paired scoring)

ROSETTA RECEIPT (scratch probe_cb44.cpp at unit's exact flags, per-version .o in this dir):
  1.2.5n  -> extsh r0,r28 ; extsh. r0,r0   (THE PAIR — pinned-version behavior, ours)
  1.3.2   -> extsh. r0,r29                  (era shape: single dot-clamp from home)
  2.0p1   -> extsh. r0,r29
  2.6     -> extsh. r0,r29
  2.7     -> extsh. r0,r29
Head binds in the same probe: 1.2.5n mr r26,r3/addi r24,r4/addi r25,r5, p->r28 (NOT lowest);
1.3-2.7 family: mr r24,r3/mr r25,r4/mr r26,r5 (dense ascending binds).
=> Era CB44 exhibits 1.3-2.7-family clamp AND a head-merge (p into trip-counter home) that the
   pinned 1.2.5n never emits for any spelling tried (B1/E2/E3/E6 + v1's ladder).
   CLASS: EXTSH-BIND VERSION-CLASS per TLobby__sub_80406328 v2 precedent — feeds era-build-identity
   memo. STOP. (Also candidate explanation for 50/51/54/55 scheduler-order rows: same family.)

SIBLING SAFETY: B1 touches only CB44's own decl block; file compiles; gnm CB44 size 0x314 unchanged;
all other TLobby symbols byte-stable (full-file rebuild diff only in CB44 region).

B1 IS SHIPPABLE STATE (not 100 — paired-100 is the only success bar; no PR this visit).
Champion: 02011eb6 = control re-land + B1, 97.451775 @0x314.
full-ninja rc=0
