# f7-11 TLobby__sub_803FB358 (card t_eef4a946) — disposition: FLOOR 99.882355 (tiebreak wall, 3-visit closed class)

Branch card-lobby-b358 @ base 5695627b. Committed tip 06c8fc0b (candidate v2), tree clean, full
ninja rc=0.

## State on committed tip (clean rebuild: rm .o + ninja + gnm + one_shot)
- gate: gnm -S OURS `TLobby__sub_803FB358` size 0x154 == symbols.txt row size:0x154 (85/85 rows).
- score: one_shot psov3/pso/misc/TLobby_803FAEA0 sub_803FB358 -> ORIG/OURS match=99.882355.
- residual = 2 rows, pure integer-GPR color mirror (8 bytes):
    slot 12  O: addi r5, r3, 0xd4   N: addi r4, r3, 0xd4
    slot 34  O: lbz  r0, 0x0(r5)    N: lbz  r0, 0x0(r4)
  i.e. the single-use address temp for lbl_805C0038+0xd4 binds r4 (lowest-free) where the era
  bound r5 with r4 free.
- all 16 unit symbols size-exact vs era .fn headers; report_delta --check vs
  baseline-5695627b.json: New exact 0, regressions 0; check_pr.py PASS; link_units check OK
  (3308 linked units all exact).

## Route (twin-parallel transcribe, per brief)
Era block read + row-by-row decode (1 ps screen); twin screen of the 15 matched in-unit siblings
(5 corpus/section greps: lbl_805D7BDC users, `0x104(r3)`, `lbz 0x6c(r3)`, `0xd4` addi, lock_mutex
callers). Spellings copied from matched siblings: NetLinkDisconnect (prologue `lis r4,@ha` +
`lwz r3,@l(r4)` + `bl TLobby::lock_mutex(lbl_805C18A0.value)`, the `((s32 *)&lbl_805C18A0)[0]`
unlock materialization, `addi r30, r3, 0x0` arg bind), TLobby_803FC178 house form
`u8 *p = lbl_805C0038 + 0xD4`, is_timed_out's `lbl_805D7A8A == 5` test; the two ==5 gate tests
spelled as positive if/else pairs (TAIL-LI layout mirror), the four 4-byte NetMemcpy quads fed by
two address-taken u32 locals (stack slots r1+0x10 / r1+0xc, era-exact).
Externs resolved by ADDRESS from current symbols.txt rows (zone law): lbl_805D7BDC .sbss size 0x4
-> `extern s32`; lbl_805D7A82/84/8A .sbss size 0x2 -> existing `extern s16`; callees
lock_mutex__6TLobbyFi = 0x803F95C4, unlock_mutex__10TUdpSocketFi = 0x803F95A4,
NetMemcpy = 0x803F9F04. New decl added: `extern s32 lbl_805D7BDC;` (no name guesses).

## Builds (4 of 8+1)
1. v1 92.0 / 0x148: omitted the lock_mutex call (the -3 insns = lis/lwz/bl of the lock arg).
2. v2 99.882355 / 0x154 gate-exact, 85/85 rows, 2 color rows. COMMITTED (06c8fc0b).
3. probe: local declaration-position reorder of the address temp (RA-HOMES-FOLLOW-DECL-POSITION)
   -> INERT (byte-identical r4 binding), gate preserved. Reverted.
4. confirm rebuild on committed tip (full ninja) -> numbers above.

## Closed-class citation (why no further grind)
The identical 2-row residual is census-closed over 3 prior visits:
- skills/pso-decomp/references/stmw-bank-spellings.md "GPR address-temp tiebreak wall (fleet/f8
  TLobby__sub_803FB358, 3rd visit park 99.88 30586b57)": ~76 hand spellings (comma-def, (u8*)&sym+K
  under #undef, struct-view &arr[0]/decay, fillers, restages, alias grids, retypes, def-position
  moves) + 1,317 permuter harvests over 3 rounds, ZERO size-pass at gate 0x154; corpus screen says
  the r4 binding is canonical for same-pool twins (TLobby__sub_803FED78 `addi r4, r3, 0xd4` exact).
- references/mwcc-notes.md "INTEGER-GPR MIRROR twin: TLobby__sub_803FB358 99.882355 f4080470
  (fleet f4)": def-order x type matrix, alias/phantom address temps, register keyword, s64
  wide-return theory, 7 opt pragmas all zero-diff, 2 permuter rounds -> "DO-NOT-RE-MINE".
Brief condition "4th visit: new skeleton only" is satisfied by this transcribe (first source body
for the fn on this branch); the new skeleton reproduces the champ state exactly and adds the
decl-position inert datum. Not re-rolled: pragma/permuter/type matrices (closed).

## Consequence for linkage
Unit TLobby_803FAEA0 = 15/16 functions matched (code 92.95 at base, +2 rows short of byte-exact
on the last fn) => unit NOT complete, linked_units stays 3308 (no 3309 claim). Revival requires a
mechanism outside the closed matrix (era MAP / register-bind context), per the fleet park rule.
