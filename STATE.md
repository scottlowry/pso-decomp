# STATE — TLobby__sub_8020B47C (src/pso/unk/text_8020B47C.cpp) — lane f8 visit-5

Branch card-b47c-v5. Seed c3efccca (transplant of b4b0cee3 twin-transcribed state).
Gate 0x10c / 268B, 67/67 rows. Baseline receipt: build/GPOE8P/baseline-d82be2a8.json.

## Control probe (v5, c3efccca, integrator-replicated)

- `rm -f build/GPOE8P/src/pso/unk/text_8020B47C.o && ninja build/GPOE8P/src/pso/unk/text_8020B47C.o` → MWCC line printed, .o rebuilt.
- one_shot_diff psov3/pso/unk/text_8020B47C sub_8020B47C → **98.80597, ORIG/OURS match 98.80597, size 268, rows orig 67 / ours 67, 14 pure-color residual rows.**
- Kit BASE-VERIFY (shared /Users/scott/Hermes/tools/perm-tests/text_8020B47C): base.c (b4b0cee3 body) compiles byte-identical, 67/67 words, non-vacuous.

## Residual 14 rows (measured, slot-aligned)

- b1 = {n1 <-> d1} PAIR-SWAP (r29<->r26): slots 13,14,16,26,27,28
- b2 = {base2,n2,d2} 3-CYCLE (r29->r30->r26): slots 36,40,41,42,44,54,55,56
- Class: RA-PAIR mirror-tie family (ring itself SOLVED by v4 twin transcription — typed row-walk spellings are load-bearing, do not touch).

## Phase table (v5 census)

| phase | state | result |
|---|---|---|
| v0 hand-transcribe | e009191e | 96.268654, 38 rows |
| perm r1 | d-walker array merge | 97.16418 |
| perm r2 | output-130-1 | 98.0597 |
| perm r3 (gen-3) | output-115-1 decl-hoist {n1,i1} | 98.283585 |
| perm gen-4 (full-cap) | re-root 115-1, 26,367 iters | ZERO harvests |
| perm gen-5 (full-cap) | same base, 26,778 iters | ZERO harvests |
| v4 T0 hand grid | 8 cells P1-P10 | 1 inert-pair, 4 regress, rest inert |
| v4 twin-screen corpus | calibrated, 35/50 matched-unit hits | SPELLING GAP found → typed row-walk |
| v4 T1 twin-transcribe | Row tbl + &tbl[i] | 98.50746, 17 rows |
| v4 D2 i1-before-n1 | champion b4b0cee3 | **98.80597, 14 rows** |
| v4 post-D2 grid | 7 cells E1-F4,T2 | 2 byte-identical, 5 regress/inert |
| v4 perm gen-5b (T0 seed) | 17,184 iters full-cap | ZERO harvests |
| v5 control probe | c3efccca rebuild | 98.80597 CONFIRMED (MWCC line, 67/67) |
| v5 perm gen-6 | re-rooted b4b0cee3 base, 900s cap, 17,781 iters, -j2 | ZERO harvests (0 outputs) |
| v5 era-bank rosetta | 20 GC MWCC versions, verbatim flags | 0/20 era-emitter (sealed, table below) |

## Era-bank fingerprint rosetta (v5, receipt: scratch b47c_v5_rosetta/rosetta_table.json)

Fingerprint = binding dest regs {base1,n1,d1 | base2,n2,d2}; size 268 emitted by all 20 versions.

| fingerprint | emitters |
|---|---|
| era {30,29,26 \| 29,30,26} (decoded from dtk era .o — non-vacuity self-check) | **0 / 20** |
| champion {30,26,29 \| 30,26,29} | 13 (1.0, 1.1, 1.1p1, 1.2.5, 1.2.5n, 1.3, 1.3.2, 1.3.2r, 2.0, 2.0p1, 2.5, 2.6, 2.7) |
| 3.0x collapse (n1/d1/base keys absent, d1=29) | 7 (3.0a3, .2, .3, .4, a3p1, a5, a5.2) |

## v5 VERDICT — CENSUS-CLOSED FLOOR 98.80597

Residual 14 rows = RA-PAIR mirror-tie b1 {n1<->d1} pair-swap + b2 {base2,n2,d2} 3-cycle =
era-scheduler-preference bank-mirror PIN, sealed by 20/20 no-emitter fingerprint (method:
references/equip-bank-mirror-pin.md). Census-complete evidence: 4 honest full-cap permuter
rounds on this unit (26,367 + 26,778 + 17,184 + 17,781 = 88,110 iters, iters>0 receipts,
zero harvests each; gen-6 is the first on twin terrain); v4 hand grids 8+7 cells; twin-screen
corpus screen (calibrated, non-vacuous) that found and closed the ring spelling gap; 20-version
rosetta. Budget: 1/6 grind builds (control), 0 probe builds (harank showed no word-move =>
probes not armed), 0/1 confirm. v5 exhausted, no v6. Park push target @98.81v5.
