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
| v5 control probe | c3efccca rebuild | 98.80597 CONFIRMED |
| v5 perm gen-6 | re-rooted b4b0cee3 base | (running) |
