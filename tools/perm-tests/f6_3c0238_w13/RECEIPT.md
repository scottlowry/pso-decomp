# Receipt — card-lobby-c0238-w13 (lane f6) TLobby_803BFE50, seat TLobby__sub_803C0238 — VISIT-3 cite-seal

Card t_2d3f2c18. Branch card-lobby-c0238-w13 @ c1d7a52a (tree pso-decomp-f6). Door report-only. No config, no push, no board.

## Verdict: CITE-SEAL — FLOOR-CENSUS 98.05556 (tip, gate-exact). Zero grind used (0/4). New datum: 20-version rosetta matrix at today's source + exact flags — era self-bind UNREACHABLE on the whole installed toolchain.

## Intake
- Branch assertion PASS (card-lobby-c0238-w13 @ c1d7a52a, tracked-clean).
- Pin (live build.ninja:52103-52113): mw_version GC/2.6; cflags `-nodefaults -proc gekko -align powerpc -enum int -fp hardware -Cpp_exceptions off -RTTI off -str reuse -maxerrors 1 -nosyspath -i build/GPOE8P/include -i include -i src -i libs/dolphin/include -i libs/dolphin/include/dolphin -char signed -use_lmw_stmw on -O4,p -inline auto -lang=c++`. NOTE: `-inline auto` (f3/v7 lineage pinned `-inline off` — different shape; v7 fused blob NOT in this branch history, transplant not re-rolled).
- Row: symbols.txt:26112 `TLobby__sub_803C0238 = .text:0x803C0238; type:function size:0x3F0` — same name at origin/master (no rename). Body on master = WIP sub-100 (unit 35/36) = card target, NOT absorbed.
- Collision: gh open-PR file screen on TLobby_803BFE50 = 0 hits. rc=0.

## STEP-0 (committed tip, rm .o + ninja MWCC rc=0)
- one_shot PAIRED ORIG=OURS 98.05556, rows 252/252, sizes 1008/1008. Brief hypothesis 98.05556 CONFIRMED.
- gnm OURS `000003e8 000003f0 T` INT-parse == row 0x3F0. GATE-EXACT.
- Siblings: 36/36 T-syms (name+size) vs era extract — ZERO drift.
- Body lineage on this branch: fc62998f(#196) → dd7a1a2d(#240) → b0b44cbd(#246) master matchpasses; today's shape = helper-decomposition (inline feed/drain/skip_audio_stream_decoder + 5-line wrapper, re-inlined by -inline auto).

## Opener 2 — fresh residual partition vs v2 census (partition_v13.json)
94/94 diff rows = register renames ONLY; ZERO semantic rows.
- 81 rows = one global home rotation era→ours {r31→r27, r27→r28, r30→r31, r29→r30, r28→r30}: bind-to-home RANK stratum (sealed v8 INERT x3; v9 census; sibling LIVE-NEGATIVE d1f7c873).
- 13 rows = per-zone lobby/a4 home rank shifts (slots 75,85,118-133,196,205,219-234) — same family, per-zone rebinding.
- v2 census class migration (master edits changed the row set): A hop+transposition DEAD (zero `mr r0` insns anywhere; hop was OUR 253-row artifact, era never had it); B D3130-slot RESOLVED (no frame-disp diff rows); C loop-bank k-cycle RESOLVED (r23..r26 bank absent from diff entirely); D lobby-remat SUBSUMED into rank shifts; E cmp-polarity RESOLVED; F display-rows ABSENT (exact-size aligned).

## Opener 1 — 20-version hop rosetta at exact flags (zero-build: direct wibo+mwcceppc into scratch; probe GC/2.6 byte-stream == ninja .o stream VERIFIED)
Screens (byte-code level, render-proof; rosetta_table_v2.txt):
| band | versions | gate | hops | self-home | rings-trio | bytediff-vs-era |
|---|---|---|---|---|---|---|
| era (orig) | — | 0x3F0 | 0 | r31 | Y | 0 |
| 1.0 | 1 | 0x3EC (−1W) | 0 | r27 | N | 190 |
| 1.1–1.2.5n | 4 | 0x3F0 | 0 | r27 | N | 166–179 |
| 1.3–2.7 (pin 2.6) | 8 | 0x3F0 | 0 | r27 | Y | 113 (all) |
| 3.0a3* | 7 | 0x3E8 (−2W) | 0 | r27 | N | 129 |
- ZERO of 20 emit era self→r31 on today's source — the decisive rank screen has no emitter across the entire installed toolchain (upgrades v9's fused-shape datum to the current inline-auto body).
- ZERO byte-identical to era anywhere; GC/2.6 pin sits in the best band (8 versions tie at 113) — no pin migration can move the residual.
- Rings trio (lha+clrlwi+cmplwi 0x8001) era-exact on the whole 1.3–2.7 band incl. pin: P4 semantics hold.

## Battery (committed tip; no source edits this leg)
- Full ninja rc=0: Code 51452/51452 (144/144), Data 7224/7224 100.00%, Runtime 100% (58/58).
- report_delta vs build/GPOE8P/baseline.json (tree baseline, Nov-9; brief cites none): matched_functions 27448→27501 (+53 New exact / 0 regressions) = CHAIN-INHERITED from master #240–#250 matchpasses; LANE LEG DELTA = +0/+0 (zero edits).
- check_pr.py: PASS rc=0 (linked 2793, regressed 0, skipped 0, exact candidates to add 0).
- Grind budget: 0/4 grind builds, 1 confirm-equivalent (STEP-0 unit build) + battery link.

## Door state
35/36 exact + seat PAIRED 98.05556 <100: door NOT unlocked. Data 100.0. Unit unlinked; no linked_units candidate; config untouched. Seat closes into ask #16 (era-alloc/toolchain strata — now convicted across all 20 installed versions at today's exact flags, not merely by family). Re-open ONLY on: era MAP file, external toolchain supply (uninstalled version/era switch), or a non-source bind mechanism.

## Names
Row name kept (adopt master). Helpers feed/drain/skip_audio_stream_decoder already landed upstream — no new proposals from this datum (0 semantic rows ⇒ no new evidence).

## Archive (scratch, kept)
cache/scratch/f6-w13/: oneshot_tip.txt, era_block.s, ours_seat.s, partition_v13.json, rosetta/ (20 .o + logs + flags.txt), rosetta_table_v2.txt, delta.log, checkpr.log, ninja_full.log, b.log. Copies committed beside this receipt.
