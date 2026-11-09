# Campaign: test_box_sphere_contact (TObjPlayer_803DF7A8 seat 0x803E112C) — v1

- Seat: `.text:0x803E112C` `test_box_sphere_contact`, gate **0x738 / 1848B** (verified vs `config/GPOE8P/psov3/symbols.txt:26807` at intake).
- Branch `card-boxsphere-v1`, base `00cda35c` (master; the 803DFB1C decl-swap lives on PARK branch c6153df7 only — read as grammar, not merged).
- Owner file `src/pso/player/TObjPlayer_803DF7A8.cpp` (seat body lines 653–745, box–sphere OBB contact test, f32-dense).
- PIN (live build.ninja `build/GPOE8P/src/pso/player/TObjPlayer_803DF7A8.o`): `GC/2.6 -O3,p -inline off -opt nopeephole -use_lmw_stmw on -fp hardware -char signed -lang=c++` — **-O4,p brief assumption REFUTED at the row** (re-verified this visit).
- Unit UNLINKED: DOL expected-constant `0d85744b51d7379efb025a943d0cd5aaae2191a3` ✓ at base snapshot (full ninja rc=0); inertness = unit .o + report_delta 0.
- Base snapshot: `cache/base_report_boxesphere.json`; base unit .o sha `8ba65c83de8cc31e108fd77ce33826bfccc6503c`.
- Intake pairing: official report.json **96.02814** (= census, exact); one_shot 95.88744, **200/462 diff rows**.
- File windows over the seat: `use_lmw_stmw off` (108, leaks to EOF), `fp_contract off`(98)→pop(748), inner `dont_inline off + inline_depth(2)`(637)→pop(746). collisionRoot static-inline (640–651) inside the depth(2) window.

## Row-classify census (200 rows at r0)
- **~14 pool-name display rows** (`lbl_805E10xx@sda21` vs `@NN@sda21`): ACCEPTED class — twin proof IN-UNIT (sub_803DF840/sub_803DF9D0 100.0-paired show pool rows; proven accepted 66 rows at seat 803DFB1C).
- **~60 fp color-ring rows** (era homes a.x→f30, ex→f13, px→f4 vs ours a.x→f13, ex→f27, px→f5; non-uniform): def-binding home ring. ROOT CAUSE NAMED THIS VISIT: era binds the pool constants 0.025f (f4) and 0.0f (f5) PROLOGUE-live across the whole function; ours' constants die inside loop bodies → free at face-loop slot 190 → fdivs dest f4 vs era in-place f6 → whole face-loop FPR map +1. NEVER re-roll (ladder law sealed).
- **~110 GPR slot-map rows** (era box→r29, sphere→r30, faceHit→r31, normals→r27, a→r28, b→r26, k2→r25 = 7-slot window r25–r31 FULL; ours box→r30, sphere→r31, a→r25, order[0..3]→r26–29; faceHit/normals unbound (r8/r10)): every pointer-touching row shifts +1. Binding rank opaque to ALL source levers at pin (see rungs).
- **~15 rotation rows** (era loads a.x at slot 243, BEFORE b-index chain 244–248; ours 248; operand-order swaps 272/276/257): plain-C schedule class → permuter-authorized (law n).

## Rung table (v1)
| rung | knob | one_shot rows | verdict |
|---|---|---|---|
| intake | committed tip 00cda35c | 200 @95.88744 | baseline; official 96.02814 |
| r1 | `s32 faceHit;` decl hoist to if-block top (assignment stays in i-loop) | 200 | **BYTE-INERT** (.o sha == r0) |
| r2 | faces/normals decl swap (661–663) | 201 | **REGRESSION** — reverted |
| r3 | `f32 ax = a->x;` def-split before b decl (era 243 interleave mimic) | 200 | **BYTE-INERT** (DAG folds def) |
| r4 | `f32 tol = 0.025f;` function-top def + 6 literal sites (era prologue-const-bind theory) | 200 | **BYTE-INERT** (already CSE'd same slots) |
| r5 | `register s32 faceHit = 1;` hint | 200 | **BYTE-INERT** |
| r6 | permuter round-1 harvest output-1280-1 (repo-seeded kit, size-preserving profile, 16,255 iters, 256 harvests, 18 clean / 222 sizekill / 16 newsym) → repo-spliced | 125 @97.088745 one-shot | **LANDED 04575fb9** official pairing 96.02814→**97.22944** (+1.201), gate 0x738 exact, siblings 27 T-symbols 0 drift, DOL constant, report_delta regressions 0, check_pr PASS |
| r7 | permuter round-2 re-rooted on champ (BASE-VERIFY 0/462, kit base=1280 chain-law ✓, 935s cap, ~7k iters, harvests to kit-1230) → output-1235-2 repo-spliced | 124 @97.18615 one-shot | **LANDED** official **97.32684** (+1.299 total), gate 0x738, siblings 0 drift, DOL constant, regressions 0, check_pr PASS |

## Verdict v1
PARK at **97.32684 official / 97.18615 one-shot, gate-exact 0x738** (r7 champion, two permuter wins landed: 04575fb9 + r7; sub-100 = ledger inventory, NOT PR material).
- Ladder: all 5 hand slot-map/def levers BYTE-INERT or regressing at the pin (datums r1–r5); the GPR-binding wall (era binds 7-slot window r25–r31 incl. faceHit→r31; ours binds box/sphere at 30/31) is source-order-opaque at GC/2.6 -O3,p — BROKEN by permuter (bank-flip precedent t_2b71f68f §72 reproduces here: rounds re-homed GPR bindings no hand probe touched, 200→124 rows).
- Residual at r7 (124 rows): ~77 fp color-ring (SEALED def-binding home ring; root cause named: era prologue-binds 0.025f@f4/0.0f@f5 function-live), ~27 pure-GPR renumber (era homes: faceHit r31 > sphere r30 > box r29 > normals r27, j-temps fill 25/26/28), 13 pool-name display (ACCEPTED, twin-proven), ~8 structural (rotation/operand-swap).
- Basin status: kit ARMED — 2 promotions, no saturation test yet (needs >=2 consecutive iters>0 zero-rounds). Visit-2: re-root base.c on r7 body (reroot_base.py proven), fire round 3 (cap 935s, harvest screen bs_rank.py: size+newsym gates, 18-clean cohort pattern), expect partial wins from the 27-row GPR class; fp-ring rows are perm-invariant (sealed) — projected ceiling ~97.5–98 at this stratum.

## Files
- kit: /Users/scott/Hermes/tools/perm-tests/TObjPlayer_803DF7A8_test_box_sphere_contact (base.c=champ, target.o 462/462 vs era, BASE-VERIFY 0/462, harvest_rank=bs_rank.py, splice=bs_splice.py, reroot=reroot_base.py, rounds bs_round{1,2}.sh; r1-* dirs archived)
- lane: cache/base_report_boxesphere.json, cache/KIT_STATE_boxesphere.md, scratch/bs_r{0,1,2,3,4,5,6}_oneshot.txt, scratch/bs_r0_nm.txt, scratch/bs_target.o

## Sealed classes hit this seat (with datum)
- pool-name ACCEPTED (twin proof, +park card 66-row proof at 803DFB1C).
- fp color-ring / def-binding home ring (root cause above = era prologue-constant binds; source levers inert).
- FP-contract function-window: seat already inside the committed push/pop windows — sealed, untouched.
- bool-clamp wall / DEAD-ARRAY / HOME-INSERTION / clobber-hoist: not probed (no rows of these classes).

## Cold-start commands (visit-2)
```
cd /Users/scott/Hermes/pso-decomp/pso-decomp-f4   # branch card-boxsphere-v1
export PATH=/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin:$PATH
~/.hermes/installs/60d8a79da6991a71/environments/28d86d1068e44adc8d1a5d2ca8c63c2c/venv/bin/python3.14 configure.py -v GPOE8P
rm -f build/GPOE8P/src/pso/player/TObjPlayer_803DF7A8.o && ninja build/GPOE8P/src/pso/player/TObjPlayer_803DF7A8.o
python3 /Users/scott/.hermes/profiles/pso-decomp/skills/pso-decomp/scripts/one_shot_diff.py psov3/pso/player/TObjPlayer_803DF7A8 test_box_sphere_contact
llvm-nm -S build/GPOE8P/src/pso/player/TObjPlayer_803DF7A8.o   # INT-parse, gate 0x738
# era .fn: build/GPOE8P/asm/pso/player/TObjPlayer_803DF7A8.s lines 1775..2256 (era prologue _savegpr_25, spills f27..f31)
# kit: /Users/scott/Hermes/tools/perm-tests/TObjPlayer_803DF7A8_test_box_sphere_contact (armed, base.c=master body, BASE-VERIFY 0/462)
# battery: ninja; tools/report_delta.py cache/base_report_boxesphere.json build/GPOE8P/report.json --check; tools/check_pr.py
```
