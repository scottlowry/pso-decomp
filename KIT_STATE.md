# KIT_STATE — card-fd88-vt4 v2 (t_72dee42a) vt4__20TWindowSubStatusDispFv (0x8027FF6C, gate 0x544, 337 insns)

Visit-2, base e175bcd9, tree f4, branch card-fd88-v2. Seed ef11902a (transplant from park/f7-fd88)
survival EXACT: 98.78339 gate-exact (337/337 rows), clean-rebuild adjudicated. FLOOR CONFIRMED.
Unit code 100% (141/141 fns, 51356/51356B — v1 census); vt4 is lone row-match blocker; no unit
completion claim (98.78 paired, not 100.0); linked_units untouched.

## Twin-rung decode (zero-build, visit-2)
vt5__20TWindowSubStatusDispFv (100% matched structural twin, same guard+init prefix, era asm
text_8027FD88.s lines 60-156): era binds arg0→r30, mode-class (get_display_mode result)→**r31**,
e0 (get_array_entry(0) result)→r28, n→r29, i→r26. Our compile = byte-identical: the
mode-above-e0 relative binding IS representable on byte-exact terrain at this pin.
vt4 era prologue decode (asm 196-240): li r27,0 / li r27,2 (t→r27), mr r30,r27 (mode copy),
bl get_array_entry(0), cmpwi r27,0, mr r26,r3 (e0→r26). Era t HOME IS FORCED by the bl clobber:
t def→test spans the call. Twin NOT sealing era's t→r27/e0→r26 — opener admissible.

## Named probe verdict: e0-HOIST INERT-NEGATIVE (opener SPENT)
Probe (grind-1): hoist `e1 = get_array_entry(arg0,0)` def above the t/mode-scratch def
(61FC def-order head-flip pattern). Result: **96.58754** (−2.196), gate 0x544 HELD, 337/337,
79 diff rows. Mechanism decoded:
- Moving the bl ABOVE the t def removes t's call-span liveness: t materializes in r3 scratch
  (li r3,0 / li r3,2 / cmpwi r3 / mr r30,r3) — t loses its callee-save home entirely.
- Ring slots 54/58/63 (block A e1/e2/e3 bindings) UNMOVED — cascade_rows_moved = 0.
- Hoist costs an 11-slot order inversion (slots 26-36) vs era's li-first/bl-after placement:
  era asm keeps bl get_array_entry AFTER the mode copy; source def-order hoist cannot emit that
  order (scheduler emits the call at def position under prop-off).
CONCLUSION: era's t→r27 home is forced by era-scheduler call placement (bl between t def and
mode copy), not by source def order. The {t↔e0} mirror pair (ours t→r26/e0→r27 vs era
t→r27/e0→r26) is not reachable by def-order permutation of the call. Def-binding/era-scheduler
call-placement kin. Census floor 98.78339 (beats WSSD 98.2 precedent). NO 2nd visit absent a
bind mechanism.

## Closed classes (do-not-re-roll, cumulative)
v1: decl-order swaps x2 (win-first, t-before-mode) = byte-identical ring; COPY-BIRTH-TOP-PIN;
self-accum fmuls (WSSD); MIRROR-BASIN; def-binding prologue pins (edc20/ba38); ternary mode form
(+2W arith chain).
v2: e0-call def-hoist (INERT-NEGATIVE, this file, receipts scratch/v2_probe1.txt); slots 9/10
@53@ha pool display = link-gated class, not source-beatable.

## Residual (84 rows, stable)
- slots 9/10: TWindowSubStatusDisp__data_8044FB00 vs @53@ha — link-gated pool naming (2 rows).
- 82 rows: pure swap ring homes {r26,r27,r28,r29} + mode2 (r30-era/r29-ours). Multiset-identical.
  Era home map per block: A(e1=29,e2=27,e3=28,win=26,t=27-vacated) B(26,28,29,v=27)
  C(26,27,29,v=28) D(26,27,29,v=28,mode2=30) E(27,28,29,v=26).

## Winning levers (v1, committed in seed)
1. mode statement-form (not ternary): 96.09→98.47. 2. `#pragma push/opt_propagation off/<fn>/pop`
FUNCTION WINDOW keeps mode=t copy (mr r30,r26) = gate 0x544, 98.47→98.78, zero sibling effect.

## Cold-start commands (v2, tree f4)
```
cd /Users/scott/Hermes/pso-decomp/pso-decomp-f4 && git branch --show-current  # card-fd88-v2
rm -f build/GPOE8P/src/pso/unk/text_8027FD88.o && ninja -C . build/GPOE8P/src/pso/unk/text_8027FD88.o
/opt/homebrew/opt/binutils/bin/gnm -S build/GPOE8P/src/pso/unk/text_8027FD88.o | grep ' vt4'  # 0x544
PY=/Users/scott/.hermes/installs/60d8a79da6991a71/environments/28d86d1068e44adc8d1a5d2ca8c63c2c/venv/bin/python3.14
$PY ~/.hermes/profiles/pso-decomp/skills/pso-decomp/scripts/one_shot_diff.py psov3/pso/unk/text_8027FD88 vt4
```
Era block: build/GPOE8P/asm/pso/unk/text_8027FD88.s lines 166-524. vt5 twin lines 60-156.
ps-arith screen: 0 hits. Builds used v2: 3 (control re-measure + probe + confirm), cap 3+1.
