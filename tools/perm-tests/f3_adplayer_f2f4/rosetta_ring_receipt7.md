# FOLD-INTEL RECEIPT #7 — TAdPlayerLoadGC__sub_803F2F1C {r27<->r28} COLOR-RING ROSETTA
fleet/f3 card-adplayer-f2f4 VISIT-3 (rosetta-fingerprint scope) — Nov-3, 2026
Pin: GC/1.2.5, flags verbatim from ninja line. Tip base: cd873b53 (v3b, 99.39286, gate-exact 0x2A0).

## Control-probe-first (repro cd873b53) — GREEN
- rm + ninja unit .o -> gnm: `00000818 000002a0 T TAdPlayerLoadGC__sub_803F2F1C` (gate-exact).
- one_shot_diff.py: ORIG/OURS match=99.39286, rows 168/168. Reproduced.
- Self-contained probe (scratch f3_adplayer_v3/probe_while.cpp): verbatim v3b while-form body,
  hand typedefs + extern decls, class methods as static-member decls (preserves call flavor),
  wrapped extern "C", pragma push/opt_propagation off window reproduced.
  Probe@1.2.5: size 0x2A0, frame -40, ch2=r28 off2=r27 px=r27 py=r28 rows=168 —
  byte-shape IDENTICAL to real unit .o on every fingerprint slot. Control green before negatives.

## 20-version rosetta table (all 20 COMPILED — zero construct-crash; version-class law satisfied)
Era target (ORIG rows, slots 93/94/104/105/107/110/118/119/120/129/144/147/150/153/155/156/157):
  frame 0x28, size 0x2A0, ch2=r27, off2=r30, px=r28, py=r27

| version class      | frame | size  | ch2 | off2 | px  | py  | gate |
|--------------------|-------|-------|-----|------|-----|-----|------|
| 1.0,1.1,1.1p1,1.2.5,1.2.5n | -40 (0x28 era) | 0x2A0 | r28 | r27 | r27 | r28 | EXACT |
| 1.3–2.7 (8 vers)   | -48   | 0x2A0 | r28 | r27 | r26 | r28 | exact size, frame +8 |
| 3.0a3–3.0a5.2 (7)  | -48   | 0x288 | r27 | r26 | folded(imm) | folded | MISS -6W |

Raw table: scratch f3_adplayer_v3/table.txt (fp.py = rows+frame+bank/ep fingerprinter).

## VERDICT — path (b): NONE EMIT
No installed version (1.0→3.0a5.2) emits era's ring {ch2=r27 + off2=r30 + px=r28 + py=r27}
at era's frame/gate class. The 5 era-frame-compatible versions (1.0–1.2.5n, frame 0x28 +
gate 0x2A0) ALL agree with the pin — identical rotation {r28,r27,r27,r28}. The lone ch2→r27
emitters (3.0a3+) produce it inside a wholesale different allocator stratum (size 0x288
off-gate, frame 0x30, off2→r26, px/py windows folded into displacements) — NOT the era
ring, and version-pin change is integrator-config anyway. Path-(a) "try its shape at the
pin" is therefore refuted by construction: the r27-ch2 datum has no 1.2.x-spelling analog.
No grid re-rolls executed or warranted (v2-directive ban + zero-emitter proof).

## Census entry (era-build-identity, 7th unit)
Unit: TAdPlayerLoadGC__sub_803F2F1C (psov3/ TAdPlayerLoadGC TU, @803F2F1C, 672B)
- Frame class: SOLVED by while-form induction (v2: comma-for reserved-slot class).
- Era-compatible version window: 1.2.x family (frame 0x28 + 0x2A0 unique to 1.0–1.2.5n).
- Residual: 13-ish-word color-ring rows (px/py trio @93/94 + @104–110 reads + loop-2 init
  chain @118–157) + 2 pool-name rows @116/117 (resolved by integrator .data carve FCE10
  → 99.48 projected). Ring = BIND-TO-HOME def-binding stratum (QVM-kin lineage:
  DEF-BINDING PROLOGUE PIN, bank-rotation-by-same-layer), not a version marker,
  not a spelling gap. v3b already proved def/decl swap moves ranks but cannot cross
  the 2-reg rotate; the rosetta now proves NO version crosses it either.
- Foreign-body candidate: WEAK — frame/gate are era-exact at pin (unlike mixed-build
  outliers); era was almost certainly built in the 1.2.x family with a register-home
  binding layer absent from every installed build.

## Recommendation
PARK-V4 at v3b (cd873b53): 99.39286, gate-exact, 0 regressed siblings. STOP the color grind.
Ship path remains the integrator .data carve (→99.48); ring rows join the era-scheduler/
def-binding maintainer memo, no per-wall ask. No second visit unless an era .map or a
bind-mechanism (not rank lever) surfaces.
