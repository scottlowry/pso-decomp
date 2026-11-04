# card f3-2 (t_c679ea2e) — control probe @ seed f37d6b1c — Nov-3 17:19 PST

Gate (symbols.txt row 26227): adx_encode_available_blocks .text:0x803C7978 size:0x298 (664B/166w).
rm .o -> ninja (MWCC line printed) -> gnm size 0x298 -> one_shot: 86.93374 paired (orig 166 / ours 166 rows, 22 diff rows).
Seed v6 state CONFIRMED (matches park 4d196f92: 86.93374 gate-exact, bank-r18).

Key era rows (opening-play target, slots 34-36):
  slot34 O: li r25,0x0      N: mr r18,r20     (avail=0)
  slot35 O: mr r21,r24      N: li r23,0x0     (walk=pch init)
  slot36 O: mr r19,r25      N: li r21,0x0     (i = avail ZERO-SHARE — folded by prop; comma-def target)
  slot54 O: slwi r21,r20,1  N: mr r27,r20     (q-materialization, mr+slwi residual)
  slot 3 O: stmw r19,0x1c(r1) N: stmw r18,0x18(r1) (ch-temp bank steal — v5 avoids)

Prior census (8 rows, f3_adxr_encode_receipt.md): v4 0x298 86.93 / v5 0x294 90.93 -1W /
v6 0x298 86.93 [seed] / v7 prop-off 0x2B0 DEAD.
Plan: ONE comma-def build on v5 (ch-free) form.
