# card-80412ca4-v1 — TLobby__sub_80412CA4 census + disposition (park)

Seat: .text:0x80412CA4 size 0x58C (1420B, 355 insns), unit psov3/pso/network/TLobby_8041112C
(unit NOT in linked_units — DOL-insensitive; inertness via unit .o sha + report_delta).
Pin (cited from build.ninja L57998-58006 row): GC/1.2.5n, `-O4,p -opt nocse -use_lmw_stmw on -inline off -lang=c`.
Base: 00cda35c (origin/master). Tip champion: 99.169014 GATE-EXACT 1420/1420, rows 355/355, .o sha 6e02259a6a025e651c1f5320d44ea62a37264376.

## Rung table (grind 4/8, ONE knob per build, all builds printed MWCC line)

| rung | knob | meter | rows | gate | verdict |
|------|------|-------|------|------|---------|
| tip  | committed 00cda35c body | 99.169014 | 59 | 1420 EXACT | champion |
| R1   | decl-front `new_var[2]` (p16 rank-up) | 99.169014 | 59 | 1420 | BYTE-INERT (rows identical) |
| R2   | retype new_var s32 + fresh s16 p16 view | 97.490140 | 131 | 1420 | REGRESSION -1.68 — reject-as-land |
| R3   | raw `plen` store at e+20 (slot 111 side) | 98.887320 | 266 | **1424 +4B** | GATE DEATH (pin emits extsh+sth) — reject |
| R4   | decl-front new_var[2] + pn-after-pe | 99.084510 | 65 | 1420 | -0.08, 0 greened / 6 new red — reject |

DECL grid capped at 4 per intake law (p) — exhausted.

## Row census (59 rows, classifier: per-token diff decode)

- 54 rows = pure callee-save HOME ROTATION: 1-step ring over {r22,r23,r24,r27},
  era {p16→r22, addr→r23, y→r24, pn→r27} vs pin {addr→r22, y→r23, pn→r24, p16→r27};
  includes 7 reg-BASE-disp color rows (same imm, base r24 vs r27 etc) and slot 111
  (sth r29 raw vs sth r27 extsh-ed — R3 datum: raw spelling = +1 insn extsh remat at pin).
- 5 rows = frame base +8: slots 2,3 (stwu -0xa0 vs -0xa8, stmw 0x74 vs 0x7c) +
  epilogue 350,351,352. CAUSE: pin allocates 2 dedicated spill slots (0x74/0x78) for the
  inlined-helper arg-pair; era spills the SAME pair into live array slots 0x18/0x1c
  (era slots 261-264 = stw/lwz evict+reload of r31(e)/r27(pn); pin rows 340-343 stage
  from freed homes r22/r23 — visible as color-pair, zero net insns). Bank lifted 8 by the
  2 extra slots; disps all shift uniformly. RA spill-placement strategy, no source lever at pin.
- 2 rows = scratch double-conversion (slots 89/90: era lha r4,0x2(r31) + extsh. r0,r4;
  pin lha r0 + extsh. r0,r0) = DEF-CLAMP REMAT pin family; era's r4 scratch bind has no
  emitter from the value-faithful spelling.

ZERO rows with order, immediate, opcode, insert/delete deltas.

## Sealed classes (with datums)

1. DEF-BINDING RING (54 rows): era PRE-RESERVES r22 at prologue (slot 7 `addi r23,r3`
   skips r22) for the slot-35 def-site extsh home; pin binds lowest-free-without-reservation.
   Decl-front inert (R1), def-order and reverse-decl grids produce the pin's own order;
   fresh-var insertion rotates prologue homes (R2 -1.68, kin of the 418d7c fresh-var seal).
   = bind-to-home stratum (QVM/CB44 1-step-ring kin): park, no re-roll.
2. EXTSH-BIND era stratum (slot 111 side): era 1-insn `sth` of raw s32 home; pin
   canonicalizes s32→s16 store via extsh+sth (R3: +4B gate death, 266 rows).
3. RA spill-slot placement (frame +8): era spills to array-top slots (0x18/0x1c),
   pin allocates dedicated slots; era-object-layout class.

Ladder clause: no further rung is spelled by one_shot rows (all residuals are color of
the sealed ring). Census-close per (p).

## Sibling safety (g)

Unit .o sha byte-identical to base at every revert (6e02259a...); all rung builds kept
gate 1420 except R3 (seat-size only, reverted). No file-scope edits — all changes were
function-scoped inside TLobby__sub_80412CA4 (co-editor f4 lane at 0x80411604 unaffected).

## Not PR material

99.169014 < 100.0 paired, 54+5 rows in sealed classes above → park receipt, not a landing.
