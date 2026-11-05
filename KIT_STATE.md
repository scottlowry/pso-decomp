# KIT_STATE — card-wssd-vt4 (t_e6eea3af) vt4__20TWindowSubStatusDispFv (0x8027FF6C, gate 0x544, 337 insns)
Visit-3(f8), base c8599a7e, tree f8, branch card-wssd-vt4. Pin CITE: build.ninja L37052 GC/2.6
-O4,s -inline off -sdata2 4 -lang=c++ -use_lmw_stmw on. VT evidence: vt4 = vtable row4 =
render__20TWindowSubStatusDispFv (auto_07_804D2B20_data.s rows 0,0,dt,run_task,render,render_shadows).

## State
Seed d24f4cff (f4 card-fd88-v2 champion ef11902a2 transplant) SURVIVAL EXACT on c8599a7e:
gnm 0x544, one_shot 98.78339 paired 337/337, clean-rebuild adjudicated. Unit code 100% (141/141,
51356B), data 6392/6392 100.0%. NOT 100.0 seat -> census-park, NOT-CANDIDATE. check_pr PASS,
report_delta regressions 0. Battery confirm x2 spent.

## Probes (5 grinds, budget 6+2)
P1 full-reverse-decl (8026E1D4 ff703c72 kin, prop-off terrain): BYTE-IDENTICAL .o. DECL-ORDER LAW
INERT at vt4 — ring is birth-rank/pressure-bound, NOT decl-rank. Closes the brief's transfer-law probe.
P2 peephole-off function window: GATE-KILL 0x5D4 (+36W), 85.73. Dead knob.
P3 opt_lifetimes-off window: GATE-KILL 0x558 (+5W), 96.56. Dead knob.
P4 trio birth-swap block-A calls (1,3,2): 99.22255 (+0.44) gate-KILL +1W (0x548). BINDING WIN:
  trio homes become era-exact (e1→r29, e2→r27, e3→r28; seed was 28,29,27). The +1W = trio3 result
  home DEFERRAL: `mr r0,r3` + `mr r28,r0` two-insn transit (era: single `mr r28,r3` at bl).
  All rows after slot 58 shift +1; register CONTENT matches era (windowed-shift, ~286 pair-rows).
P5 comma-def pack of the P4 trio defs: BYTE-IDENTICAL to P4. Deferral is scheduler packing,
  not statement grouping.

## Spelled successor rung (v4)
From P4 terrain (1,3,2 birth): kill the trio3 r0-transit (2 rows -> era 1 row). Mechanism screen:
at trio3 bl, pool {r26,r27,r28} free, r3 needed for next bl args — era binds trio3 direct because
era's trio3 is the LAST call (order 1,2,3). Era trio-map death-rank decode: era binds {trio2→27
(dies 1st in walk), trio3→28, trio1→29} = death-order-ascending rank (e0 pinned 26). A source
spelling that binds trio2 early-dying at r27 with trio3 LAST call = order (1,2,3) + trio1→29 birth
claim. Candidates: swap ONLY trio2/trio3 defs (1,3,2 walk unchanged?); sink e1 birth (e1 = gea(1)
def AFTER e3/e2 bl pair, i.e. (3,2,1) with trio1 mr at post-walk slot).
Era home map: A(26=e0,29,27,28,win26) B(26,28,29,v27) C(26,27,29,v28; mode2 li r30) D(26,27,29,v28)
E(27,28,29,v26). mode2 era REUSES r30; ours binds new r29 (slot294 class).

## Closed classes (cumulative, state-stamped)
v1(f7/f4): ternary mode form +2W; prop-off window = gate-key; decl swaps x2 byte-identical;
  COPY-BIRTH-TOP-PIN; MIRROR-BASIN; self-accum fmuls.
v2(f4): e0-call def-hoist INERT-NEGATIVE 96.58754 (prop-off window terrain; t-home call-span-forced).
v3(f8): full-reverse-decl byte-identical (prop-off window terrain); peephole-off +36W;
  opt_lifetimes-off +5W; trio birth-swap (1,3,2) = +1W RING-LAND rung (spelled, see successor);
  comma-def pack inert vs deferral.
F4 v2 twin-rung law stands: mode-above-e0 representable at pin (vt5 byte-exact); era map reachable,
path = era-scheduler death-rank bind, no decl-rank route.

## Cold-start (v4)
cd /Users/scott/Hermes/pso-decomp/pso-decomp-f8 && git checkout card-wssd-vt4
rm -f build/GPOE8P/src/pso/unk/text_8027FD88.o && ninja build/GPOE8P/src/pso/unk/text_8027FD88.o
/opt/homebrew/opt/binutils/bin/gnm -S build/GPOE8P/src/pso/unk/text_8027FD88.o | grep ' vt4'  # 0x544
PY=/Users/scott/.hermes/installs/60d8a79da6991a71/environments/28d86d1068e44adc8d1a5d2ca8c63c2c/venv/bin/python3.14
$PY ~/.hermes/profiles/pso-decomp/skills/pso-decomp/scripts/one_shot_diff.py psov3/pso/unk/text_8027FD88 vt4
Era asm: build/GPOE8P/asm/pso/unk/text_8027FD88.s L166-524. P4 rows dump: scratch/wssd-vt4_p4_rows.txt.
