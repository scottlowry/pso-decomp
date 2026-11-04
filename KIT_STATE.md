# KIT_STATE — TLobby__sub_803C61C4 (AdxStreamRuntime) campaign spine
Card t_68fd1e46 / visit-2 card t_9036b67d · lane f7 · branch card-adxr-c61c4-v1 · base f4200fcb
Gate: symbols.txt:26222 `TLobby__sub_803C61C4 = .text:0x803C61C4; size:0x63C` (1596B = 399 insns).
Champion @ tip d5d6b274: gnm **0x634** (397/399 = 99.5% size), one_shot **89.36591**, full battery green.

## CLASS TRIAGE (visit-1)
- **A/B hybrid, NO hardwall**: ps-arith count = **0** (zero psq_*/ps_* ops). Single callee: `bl strlen` (1 call). No vtable/PTMF, no 4681-magic chains (the two divisions are `divw` on RELOADED struct fields = variable divisor, not constant magic).
- Frame 0x20 (`stwu r1,-0x20`), lr@0x24, bank **r28–r31** (mr copies: r28=a1, r29=a2, r30=a3; r31 = pool base lis@ha/addi@l, materialized in prologue, lives across everything).
- Signature (in-file caller evidence, fn_803C5B50 @ 803C5BD4: `ctx = TLobby__sub_803C61C4(2, arr, src)`, existing fwd decl line 245): `u8 *TLobby__sub_803C61C4(s32 n, Strm_803C5B50 **arr, Strm_803C5B50 *extra)`.

## ANATOMY (era decode, by address region)
| Region | Addrs | Shape | Semantics |
|---|---|---|---|
| prologue+strlen | 61C4–61F8 | 12 + lwz lbl_805D4664@sda21 + bl strlen | pool=(u8*)adx_encoder_channel_work_pools →r31; len=strlen(lbl_805D4664) raw in r3 across the scan (no intervening writes) |
| slot scan | 61FC–629C | FULL-UNROLL if-chain 8×(lbz,extsb,beq,li k,addi 0x2d0) | i = count of leading busy slots in 8×0x2d0 array @ pool+0x9c0; byte0 s8 test |
| busy return | 629C–62A8 | cmpwi i,8; bne; li r3,0; b epilogue | all busy → return 0 |
| slot head | 62AC–62C4 | mulli i,0x2d0; base re-addi 0x9c0; cmpwi n,0; stb n,+2 | slot=pool+0x9c0+i*0x2d0; slot[2]=s8 n; n<=0 skips copy |
| chunk copy | 62C8–6338 | (n-8+7)>>3 ctr; 8×(lwz,addi r8,8,stw@+4..+0x1c, lwz, stwu +0x20) bdnz | MWCC -O4,p 8×-unroll of word-copy loop d[j+1]=a[j] (words) |
| tail copy | 633C–6364 | slwi r8,2; subf rem; ptr bump; cmpw/bge; 3-insn bdnz | remaining words |
| init A | 6368–63C0 | stw r30→+0xc; stb0→+1; 0s→28/2c/30; 0x7fff→34; **len+0x20→+0x48; lwz reload; (v+3)/4*4 trio (srawi/addze/slwi); stw; lwz reload; subi4; cmpwi 0xe; li r3,0xe EARLY(637c); mr-if; stw** | store-RELOAD chains (family law): +0x48 = max(align4(len+0x20)-4, 14) |
| init B | 63C4–6460 | 3→4c; **n→+0x58**; 0xAC44(44100 via lis1+subi)→5c; 4→54; 18→50; lwz 50,lwz 54; subi2,slwi3,**divw**→44; 0x7fff→60; 500→64; 6×0→68..7c; 2×0→38,3c; lwz 60,lwz 44; subi1,divw,addi1,**mullw**→40 | +0x44=(f50-2)*8/f54; +0x40=((f60-1)/f44+1)*f44 — real divw (var divisor), readbacks as stores+lwz |
| region A | 6468–6608 | 16-cap 8×-unroll scan stride 0xc @pool+0x900 (name tbl, walker r10, snapshot r8, count r9); join: cmpwi r9,0x10; bge TAIL; b JOIN; **TAIL 651C: li r8,0 (IN-PLACE on snapshot home, zero-copy)**; JOIN 6520: cmplwi r8; bne body; li r6,0; b END; body = ctx walk 8×-unroll (walker r9, snapshot r6, count r5); stw r7,0x14(r6); cmpwi r5,0x10; stw r8,0x88(r6) INTERLEAVED; bge 6604; li r0,1; stb r0,0(r6); b 6608; 6604: li r6,0; END: stw r6,0x80(r4) | acquire name slot + ctx slot, link, mark. ctx[0x14] is STRUCT READBACK (slot+0x54), not literal |
| region B | 661C–67BC | mirror of A: name walk r5-count, ctx walk r3-count; ctx2[0x14]= lwz f44 r6; ctx2[0x88]=name2; slot[0x84]=ctx2 | second ctx; +0x14 = slot+0x44 |
| tail | 67BC–67DC | stw 0x84; li0/li1; mr r3,slot; 4×sth 0 → **2cc,2c8,2ce,2ca** (era order); stb 1→+0 | arm slot, return slot ptr |
| epilogue | 67E0–67FC | lwz lr,31,30,29,28; mtlr; addi; blr | shared by busy-return path |

Data: `adx_encoder_channel_work_pools` .bss 0x80573100 size 0x9C0 (defined cpp:2753, u32[0x9C0/4]) — claimed 0x9C0 = ctx tbl 16×0x90 + name tbl 16×0xc EXACTLY; work slots (8×0x2d0 @ +0x9c0) ride raw .bss PAST the claimed size. `lbl_805D4664` .sdata char* (extern cpp:468).
Layouts: ctx (0x90): +0 s8 inuse, +0x14 s32 (rate/bs), +0x88 ptr name. name (0xc): +0 s8. slot (0x2d0): table above.

## SIZE GATE DISPOSITION (visit-2 — CLOSED at this pin)
- Floor = **0x634 (397/399)**. The −2W gap = the era join's extra unconditional `b` at 2 sites (era 4-insn layout `cmpwi; bge TAIL; b JOIN; TAIL: li r8,0` with the zero landing IN the snapshot register home = zero-copy PHI).
- V5 (609dbb6a, 0x644): ternary join fires the era 4-insn layout + era-parity `b`, pays +1 `mr`/site (result allocated in FRESH home; seed copied in via `mr r3,r6`). 401 = 399 + 2 mr.
- **V7 walker-bind probe (b2862b01): REFUTED — 0x600 (384 insns, −13W AWAY).** Dropping `name = w;` and binding the ternary to the walker var destroys the 16 per-arm `mr` copies per site (the V2→V3 +32 chain). The era mr-chain is carried by the SNAPSHOT TEMP WRITE-BACK (`name = w;`), NOT by an in-place walker walk. Visit-1 frontier-1(b) "unroll artifact of p+=K" reading is WRONG — V3 form is load-bearing.
- Verdict: gate-exact needs the era 4-insn join layout WITHOUT the PHI copy = def-binding / era block-placement class (qvm-edc20 + c7df0 TAIL-LI census kin). Across 2 visits, 6 join spellings probed (V3/V4/V5/V6/V7 + polarity). **Do NOT re-roll the name-join spelling grid; no 2nd size visit absent a NEW mechanism** (era MAP, context-binding, rosetta). Ship-park = floor 0x634 / 99.5% size.

## VISIT-2 LOG (grinds used: V7, S1, S2 = 3 of 8; + confirm battery)
- V7: single-var walk + `w = (i<16)?w:0` both sites → 0x600. Committed as datum (b2862b01), reverted with datum (06798eec).
- S1 (d5d6b274 = CHAMPION): slot-scan walker temp: `w = pool+0x9c0;` test on w, `w = w+0x2d0` in-place walk (slot scan only; region-A/B walks untouched) → size holds 0x634, one_shot 89.2406 → **89.36591** (+0.125). Residual scan rows: era arms `lbz 0x2d0(r4); li r5,k; addi r4,r4,0x2d0` (walker r4, counter r5, head `addi r4,r31,0x9c0; lbz 0(r4)`) vs ours `li r4,k; lbz 0x2d0(r5); addi r5,r5,0x2d0` (counter r4 / walker r5 ROLE SWAP) + head `lbz 0x9c0(r31)` big-disp remat (walker materialized late at 0xc90). Allocation-rank def-binding census.
- S2: dropping the dead alias `slot = w;` → BYTE-IDENTICAL .o (dead-assign fold, inert). 2-spelling budget for the scan SPENT.
- 44100 row RESOLVED-FAVORABLE: champion emits era's 2-insn form `lis r3,1; addi r8,r3,-21436` (= subi 0x53BC) — visit-1 note "ours emitted li@72c" is STALE; residual is dest-reg color only (r8 vs era r0) = census.
- Full battery on committed tip (after clean rebuild + full ninja): report_delta --check vs REGENERATED f4200fcb base: all deltas +0, New exact 0, **regressions: 0**, RC=0. check_pr.py: **PASS** (RC=0), link_units 3303 all-exact, regressed(drop) 0, exact-candidates-to-add 1 (pre-existing TLobby__sub_80423298, foreign to this card).
- Unit linkage state (report.json, fresh): psov3/pso/system/AdxStreamRuntime — fns **105/112 matched (7 open**, c61c4 among them), code 78.029%, data 100.0%, fuzzy 83.7583, complete=false. 105 → 105 (89.37 is not a match; expected mid-campaign).

## V3+ RANKED FRONTIER (cold-visit-3 start here)
1. SIZE: gate-unreachable at this pin (disposition above). Only sanctioned size experiment: 20-version rosetta fingerprint of the name-join region at the V5 spelling (609dbb6a) — check if any era-class version emits the era 4-insn layout with the result bound to the seed home; record table, do not grind spellings. If no emitter: EXTSH-BIND/def-binding pin class confirmed, park.
2. Color census rows (ALL documented classes, NO grind): (a) prologue slots 4–12 pool-base via r0 + bank shift = def-binding prologue pin (qvm-edc20); (b) scan walker/counter role swap + head big-disp remat (S1 residual, budget spent); (c) 44100 dest-color r8-vs-r0; (d) region-A store interleave (`stw r7,0x14; cmpwi; stw r8,0x88` — era slots cmpwi BETWEEN the two stores; ours emits them adjacent) = scheduler pin kin.
3. Sibling safety: 0 regressions at every commit this visit; regenerate the base report before any delta gate (stale-base hazard, f4200fcb copy at /tmp/base_report_f4200fcb.json this visit).
4. DO NOT RE-ROLL (cumulative closed list): while-&& scan form (never unrolls); empty-then negated if/else (V4); forward-goto chain arm (V6); **V7 walker-bind var-fold (refuted, −13W)**; **slot-scan alias/statement-split (S2 inert)**; decl-order/prop windows for prologue split; LI-ZERO-COPY m2c fold (25+ spellings); 4681-magic chains (absent in fn); per-branch magic duplication (n/a); encode comma-def copy-restorer seed (unused, seed retained for loop-A head copy class).

## VISIT-1 LOG (complete — 6 probes)
- V1 skeleton (plain while-loops): 224 insns — scans rolled.
- V2 `for(i=0;i<N;i++){if(*p==0)break; p+=S;}` + TAIL-LI negated mark/zero + negated name==0 if/else: **365** — unrolls FIRED (for-break form = era bdnz sets; while-&& form does NOT unroll at 2.6).
- V3 walker-snapshot temps (`w` hidden walker + per-iter `name = w;` write-back; early `k54/k44` bound readbacks): **397 (0x634)**. Copy-chain/init/slot-scan/chunks ALL region-parity.
- V4 negated empty-then if/else joins: INERT (folds to 3, same as V3).
- V5 `name = (i < 16) ? name : 0;` ternary joins: **401 (0x644)** = era tail-layout FIRES (cmpwi; bge TAIL; b; li@tail) +1 `mr r3,r6` copy per site (2 sites).
- V6 `if(goto arm)/goto join/label:` forward-goto chain: INERT (folds to 3).
- Champion state = tip (V6==V3 size, 397/399). one_shot (unlinked): **89.2406**, rows orig 399/ours 397.
- Commits: 84ca1111 V1, (V2), 283031a2 V3, 609dbb6a V5, b95f0425 V6, 9064a18c disp-1.
- Visit-2 commits: b2862b01 V7-datum, 06798eec champion-restore-datum, d5d6b274 S1 tip.
