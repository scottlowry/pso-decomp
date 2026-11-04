# card f3-2 (t_c679ea2e) — adx_encode_available_blocks v2 — FLOOR disposition — Nov-3

Gate (symbols.txt 26227): .text:0x803C7978 size:0x298 (664B/166w) — row is truth.
Tree: card-adxr-encode-v2. Control probe @ seed f37d6b1c: 86.93374 gate-exact REPRODUCED
(rm .o -> ninja MWCC line -> gnm 0x298 -> one_shot 166/166 rows, 22 opcode diff).

MEASURED TABLE (all on rm-.o + ninja unit + one_shot):
v6 seed   ch-temp + `i=avail` stmt          0x298 GATE   86.93374   [SHIPPED STATE, bank-r18 steal, 22 opcode rows]
v8        v5 ch-free + comma-def `s32 avail=0, i=avail;`  0x294 -1W  90.92771  (96 rows; bank-r19 CLEAN, walker mr lands head)
P1 champ  v8 + named walker `avail=0; walk=pch; i=avail; for(;i..;i++,walk++)`  0x294 -1W  90.945786  (95 rows; i binds r19 EXACT)
P2        P1 seed moved to for-init `for (i=avail;...)`   0x294 -1W  90.945786  (inert)
P3        P1 + comma-op `i = (0, avail);` (HGW breach form) 0x294 -1W  90.945786  (inert)
P4        P1 + pointer decls hoisted above scalar pair    0x294 -1W  89.981926  (117 rows; REJECT — i ring broke)

VERDICT: comma-def DOES land v5's walker-init copy (slot 35 O mr r21,r24) at the loop-A head
and clears the v6 bank-steal cascade (stmw row gone, P1). It does NOT unfold the zero-share
`mr r19,r25`: 5 seam spellings (plain stmt / func comma-def / comma-op (0,avail) / for-init /
named-walk adjacency) ALL fold to `li r19,0` — m2c-parser LI-ZERO-COPY FOLD class
(mwcc-notes-2, ~25 spellings inert on that unit; prop-off DEAD here: census v7 0x2B0).
Gate-exactness needs the +1W; the only installed emitters of +1W here are v6's ch-copy
(bank steal, 86.93) and era's zero-share mr (unfoldable). 90.95 is gate-MISSING (-1W) ->
NOT pairable in report_delta; official best remains v6 86.93374 gate-exact. <95 after the
pre-recorded play + 4 targeted probes = CENSUS DISCIPLINE -> FLOOR.
Tip restored to v6 (blob b3d5085e = park 4d196f92 shipped state); P1's body lives in commit
2fedcceb (history = datum, 90.95/-1W banked for any future zero-share mechanism).

Census rows added this visit: 5 (v8, P1, P2, P3, P4) -> census total 13.
Residual P1 classes (rows file f3_encode_rows_p1.txt): prologue order (slots 6-10, magic-vs-pch
birth), q-materialize order (54-55 slwi/mr swap), loop C/D color ring ~80 rows = def-binding
bind-to-home ring (a8b4 kin, no-2nd-visit law). Sibling 803C5E78/C5ED4/C7DF0 untouched (C5ED4/
C7DF0 = closed cards; body not re-implemented). prop-off NOT re-rolled; full grids NOT re-rolled.
