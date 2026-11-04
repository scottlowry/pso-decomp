# card t_7e80c8eb / lane f8 804f112c — apply_use_effect__13TUnk_804F112CFv (0x803531FC, 0x184)

status: FLOOR 97.73196 at gate-exact size 0x184 (97/97 rows, 5 residual) — f4 v8 seed re-verified on base 5695627b
tree: pso-decomp-f8, branch card-804f112c-use, seed tip 7cf7a130 (transplant of card-804f112c @ cdb825e9)
profile: GC/2.6 -O4,s -inline off. Base wave f4200fcb..5695627b = 1 commit (Matchpass lane9) — transplant hunks only, survival EXACT.

## Owner path correction (card mispair)
Card tombstone said owner src/pso/unk/text_8033C69C.cpp; the symbols row (gate law)
places the fn at .text:0x803531FC size:0x184 and splits.txt gives a dedicated unit
pso/unk/text_803531FC.cpp (.text 0x803531FC..0x80353380 = exactly the fn).
text_8033C69C.cpp owns fn_8033C69C (0x12C). Unit target = build/GPOE8P/src/pso/unk/text_803531FC.o.

## Screens (fresh, per card law)
- GSP ps screen (exact def): ps-arith = 0 (no ps_add/mul/sum/madd/lhf); zero psq_l/psq_st
  — no Gekko spill pairs at all. No ps wall.
- ESCAPE-ARRAY: only escape is the 12B PTMF desc trio -> 0x8(r1), r12=0x8(r1) ->
  bl __ptmf_scall (transcribed literally via (this->*fn)(w[1],w[0])). buf[27] is never
  passed whole; its liveness rides the dynamic-index read (v2 law). No array-to-callee
  liveness construct beyond the desc.
- Twin screen: zero siblings in-unit (unit = single fn; gnm -S ours = 5 symbols, 1 T).
  Real-size key 0x184 across the 18 apply_use_effect symbols.txt rows: zero size twins.
- Callers by address: no direct bl to 0x803531FC in the era asm corpus; class reached
  via __vt__13TUnk_804F112C (.data:0x804F112C, 0xB4); PTMF table auto_07_804F10C0_data.s
  + vtable refs live in sibling units text_80353380/80353414.
- Name claims verified vs era .fn: bl get_technique__11TItemObjectFv on this; clrlwi r0,r3,24
  (u8 clamp) + cmplwi r0,9 guard; 27-word bdnz copy from lbl_80479100 (.rodata zeros) is
  DEAD-into-live under the 27 lwz/27 stw shuffle from lbl_804F10C0 (9 x PTMF desc);
  9/9 targets = TEndingPic methods (f4 nm -S psov3.elf receipt). No field derefs —
  zero member names used (disp-evidence law satisfied).

## Grind this visit (2/7 builds, classes closed, close clean)
- Probe A: shuffle-head statement swap buf.w[1] before buf.w[0] (STORE-SWAP lever,
  TObjFish precedent) — gate 0x184 held, rows 5 -> 8 (inversion point moves to slots
  21/22 + store pair 48/49 inverts). Negative datum: tail-store sink not a store-order
  permutation. Reverted.
- Probe B: #pragma push/opt_common_subs off/pop function window — BYTE-IDENTICAL residual
  (97.73196, same 5 rows). Consistent with pure-permutation-window inertness law
  (draw_compass). Reverted.

## Residual 5 rows (unchanged from f4 census — pin classes, no bind mechanism)
- slots 20/21: loop-tail stw vs first shuffle lwz transposition — SCHED-WINDOW-PIN kin.
- slots 79/80/83: mulli dest era r4 vs r0 / base addi era r0 vs r6 (+ add operand roles)
  — def-binding scheduler-pool color cycle {r0,r4,r6} (qvm-edc20 kin). Era index bind is
  FRESH-dest (mulli r4,r0) at a 2.6-pinned unit = def-binding stratum, INERT to
  named temps (v6), trio decl order (v7), inline index (v9, regressed), store-swap (A),
  cs-window (B).

## Gates on committed tip (clean rebuild)
rm .o + ninja MWCC line; gnm -S 0x184 = gate; one_shot PAIRED 97.73196 (97/97).
Full ninja rc=0; report_delta vs baseline-5695627b.json: New exact 0, regressions 0,
linked_units 3308 (+0), complete_data +0; check_pr.py PASS (exact candidates to add: 1
— config link row, integrator). report.json row: paired at 0x803531FC, 388B, 97.73196.

unit_linkage_state: unit text_803531FC fn count = 1; 1/1 paired at 97.73196; unit
INCOMPLETE (floor, no completion claim); linked_units stays 3308; data pairing N/A
(unit split .text-only); link-scan clean (0 regressed, 0 skipped).
