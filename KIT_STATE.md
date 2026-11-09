# Campaign: TObjPlayer__sub_803DFB1C (v1 park state)

- Seat: `.text:0x803DFB1C` `TObjPlayer__sub_803DFB1C`, gate **0x11AC / 4524B** (verified vs symbols.txt row at intake).
- Branch `card-803dfb1c-v1`, base `00cda35c`. Owner file `src/pso/player/TObjPlayer_803DF7A8.cpp` (seat body lines 210–555, triple-projection quad edge-intersection FSM, inline frsqrte sqrt at 195).
- PIN (live build.ninja `build/GPOE8P/src/pso/player/TObjPlayer_803DF7A8.o`): `GC/2.6 -O3,p -inline off -opt nopeephole -use_lmw_stmw on -fp hardware -char signed -lang=c++`. Brief's `-O4,p` family assumption REFUTED at the row.
- File windows over the seat: `#pragma push/fp_contract off`(98)→pop(748); inner `push/dont_inline off + inline_depth(4)`(112)→pop(556).
- Unit UNLINKED (linked_units.txt no row): DOL expected-constant `0d85744b51d7379efb025a943d0cd5aaae2191a3` = main checkout; inertness = unit .o + report_delta 0.
- Base snapshot: `cache/base_report_df7a8.json`.

## Unit census (official report.json pairing, tip 00cda35c + r1)
25 fns, 23 paired 100.0. Open seats:
| addr | size | score | name |
|---|---|---|---|
| 0x803DFB1C | 4524B | **98.8992** (r1) | TObjPlayer__sub_803DFB1C (this campaign) |
| 0x803E112C | 1848B | 96.02814 | test_box_sphere_contact (SEPARATE seat, unassigned — next unit supply) |
.sdata2 section fuzzy 50.0 = pool literals (0x805E0FD8..0x805E1050, seat-owned constants).

## Rung table (v1)
| rung | knob | score | gate | verdict |
|---|---|---|---|---|
| intake | committed tip (Matchpass 15 ae797d39 seed) | 98.851456 | 0x11AC | 232 diff rows |
| r1 | `pa[4]; pb[4];` decl swap (slot-map mirror: era pa@0x70 hi / pb@0x50 lo, emitter = first-decl-highest at 2.6 -O3,p) | **98.8992** | 0x11AC | **LANDED** 379d7deb, 54 rows killed, siblings 0 drift |
| r2 | named loop-base bind `Vec_803E1B1C *bp; ... bp=b;` (×3 blocks) to hoist `mr r3,r28` | 98.8992 | 0x11AC | **BYTE-INERT** — reverted, datum banked |

## Residual census (178 rows at r1 tip, one_shot)
- **66 pool-name display rows** (`lbl_805E0FD8/FE0/FE8/FF0@sda21` vs `@52/@54/@55/@56@sda21`): ACCEPTED class. Twin proof IN-UNIT this visit: `TObjPlayer__sub_803DF840` 100.0-paired shows slot-6 pool row; `TObjPlayer__sub_803DF9D0` 100.0-paired shows slot-41 pool row. Unfixable by config (MWCC pool reloc naming).
- **92 fp color-ring rows**: era homes coordinates in f24–f30 (f27↔ours f19, f18↔f27, f24→f21, f22→f24, f28↔f18, f30→f20, f29→f22 — non-uniform permutation = def-binding home ring). NEVER re-roll (ladder law); RELATIVE-RANK not uniform-shift → structural inertness of decl-rank levers.
- **20 rotation rows**: 3× `mr r3,r28` (loop-base of `b`) sits ONE step EARLIER in era (slots 86/395/693, between `lfs prevB` pair and the lengthSqA fp chain) vs ours (95/400/698). Multiset identical. Named-bind inert at pin → era clobber-analysis hoist family (EB4D4 kin).

## CLOSED-CLASS do-not-re-roll list
1. pa/pb slot-map: resolved by r1 decl swap — do not re-swap.
2. bp/named-bind hoist of loop-base mr: inert at 2.6 -O3,p, bp-ON terrain (r2).
3. fp color ring f24–f30↔f18–f23: def-binding home ring (sealed by law, no probe spent).
4. pool-name display: accepted (twin proof above).
5. gate/frame/bank: exact at r1 (0x11AC, tail slots 0x50–0x8c land) — no GEOMETRY-STRATUM door.

## Visit-2 ranked frontier
1. **Permuter round (law-n authorized)** on rotation class only: ~20 rows across 3 blocks, plain-C statement-order residual, 1131-insn function (lifecycle pass, state space HUGE — expect partial; kit dirs in scratch, ONE build tree, kill-discipline; harness traps in references/permuter.md). Expected yield ≤+0.02pp — LOW priority at this size.
2. 20-version rosetta fingerprint on era color ring (seal census row; contributes to bind-to-home stratum table). Heavy, low yield.
3. test_box_sphere_contact (1848B @96.03, same file): NOT this seat — separate card per one-seat-one-card.

## Verdict v1
PARK at **98.8992 gate-exact** (rung-1 champion, sub-100 = ledger inventory, NOT PR material). Largest open seat in fleet at intake (98.85); +0.048 landed, 54/232 rows killed, all sealed classes named with datum.

## Cold-start commands (visit-2)
```
cd /Users/scott/Hermes/pso-decomp/pso-decomp-f4   # branch card-803dfb1c-v1
export PATH=/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin:$PATH
~/.hermes/installs/60d8a79da6991a71/environments/28d86d1068e44adc8d1a5d2ca8c63c2c/venv/bin/python3.14 configure.py -v GPOE8P
rm -f build/GPOE8P/src/pso/player/TObjPlayer_803DF7A8.o && ninja build/GPOE8P/src/pso/player/TObjPlayer_803DF7A8.o
python3 /Users/scott/.hermes/profiles/pso-decomp/skills/pso-decomp/scripts/one_shot_diff.py psov3/pso/player/TObjPlayer_803DF7A8 803DFB1C
llvm-nm -S build/GPOE8P/src/pso/player/TObjPlayer_803DF7A8.o   # INT-parse, gate 0x11ac
# era .fn: build/GPOE8P/asm/pso/player/TObjPlayer_803DF7A8.s lines 258..1472 (cache copy cache/dfb1c_era.fn)
# battery: ninja; tools/report_delta.py cache/base_report_df7a8.json build/GPOE8P/report.json --check; tools/check_pr.py
```
