# KIT_STATE — TLobby__sub_803C61C4 (AdxStreamRuntime) campaign spine
Card t_68fd1e46 · lane f7 · branch card-adxr-c61c4-v1 · base f4200fcb
Gate: symbols.txt:26222 `TLobby__sub_803C61C4 = .text:0x803C61C4; size:0x63C` (1596B = 399 insns).
Largest remaining open in Adx-linkage family (105+/112). Era .s block: build/GPOE8P/asm/pso/system/AdxStreamRuntime.s lines 565–991.

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
| region A | 6468–6608 | 16-cap 8×-unroll scan stride 0xc @pool+0x900 (name tbl, count r9); i>=16→name=0; name!=0 → 16-cap scan stride 0x90 @pool+0 (ctx tbl, count r5); ctx[0x14]= **lwz f54 r7(=4)**; ctx[0x88]=name; j<16→mark *ctx=1 else ctx=0; slot[0x80]=ctx | acquire name slot + ctx slot, link, mark. ctx[0x14] is STRUCT READBACK (slot+0x54), not literal |
| region B | 661C–67BC | mirror of A: name walk r5-count, ctx walk r3-count; ctx2[0x14]= **lwz f44 r6**; ctx2[0x88]=name2; slot[0x84]=ctx2 | second ctx; +0x14 = slot+0x44 |
| tail | 67BC–67DC | stw 0x84; li0/li1; mr r3,slot; 4×sth 0 → **2cc,2c8,2ce,2ca** (era order); stb 1→+0 | arm slot, return slot ptr |
| epilogue | 67E0–67FC | lwz lr,31,30,29,28; mtlr; addi; blr | shared by busy-return path |

Data: `adx_encoder_channel_work_pools` .bss 0x80573100 size 0x9C0 (defined cpp:2753, u32[0x9C0/4]) — claimed 0x9C0 = ctx tbl 16×0x90 + name tbl 16×0xc EXACTLY; work slots (8×0x2d0 @ +0x9c0) ride raw .bss PAST the claimed size. `lbl_805D4664` .sdata char* (extern cpp:468).
Layouts: ctx (0x90): +0 s8 inuse, +0x14 s32 (rate/bs), +0x88 ptr name. name (0xc): +0 s8. slot (0x2d0): table above.

## V2+ RANKED FRONTIER (cold-visit-2 start here)
1. **Size gate first** (visit-1 prize target): gnm -S OURS must read 0x63C. V1 lever risks: (a) slot-scan must FULL-UNROLL (8-iter constant-bound while + break → era chain; if we emit bdnz, re-spell as `if` chain per stride — family c7df0 per-branch law); (b) the 4 scan loops (16-iter) must 8×-unroll into 2 bdnz sets with the mr-walker copies (era has `mr rW,walker` per elem — that is MWCC unroll artifact of index-walk `p+=K`, do NOT hand-add copies); (c) word-copy: era unroll fires only from plain `for(j=0;j<n;j++) dst[j+1]=src[j]` (s32 index math) — `*++pd` walk spellings are -1W phantom (c7df0 law).
2. **Store-reload fidelity** (family law): every `lwz +C(r4)` in era init = source RE-READ the struct field (`*(s32*)(slot+C)`), 8 sites: 48×3, 50, 54, 60, 44. Do NOT keep values in locals (fuses −6W, dead code per byte-exact law).
3. **early `li r3,0xe`** at 637C (clamp constant materialized 10 insns early, clamped via mr r3,r0 form, era clamp-result lands in r3 not r0) — clamp spelling `v=(t>14)?t:14` with v=14-init (TAIL-LI mirror: era has NO tail-li here, inline cmpwi/ble+mr = positive ternary layout, do NOT negate).
4. Colors after gate: bank r28–r31 should land from arg-use density; r31 = pool (declare+assign first stmt, TWIN-PARALLEL law). Residual scheduler pins (addi r0,r3,0x20 sunk between stw r6,0x28 region; mr-walker placement) = def-binding kin — census, don't grind (LI-ZERO-COPY + c8020 TAIL-LI + qvm-edc20 def-binding walls DOCUMENTED — do not re-roll inert spellings).
5. ctx[0x14] A-region: era reads r7 = lwz f54 (line 6408) — spell `*(s32*)(ctx+0x14) = *(s32*)(slot+0x54)` — verify divw r7 consumer doesn't CSE (lwz 54 at 6408 feeds BOTH divw and stw 0x14: ONE reload, two consumers).

## CLOSED-CLASS / DO-NOT-RE-ROLL (visit-1 baseline)
- LI-ZERO-COPY m2c fold wall (c5ed4/encode census): any `li X,0; mr Y,X` from adjacent zero+copy — inert, 25+ spellings.
- 4681-magic chains: NOT PRESENT in this fn (divw-on-reload class only).
- Per-branch magic duplication (c7df0): not applicable (no constant divisors in the scan/copy).
- encode comma-def copy-restorer (0x803C7978 census): available as probe seed for loop-A head copy if walker-init copy missing.

## VISIT-1 LOG (complete — 6 probes)
- V1 skeleton (plain while-loops): 224 insns — scans rolled.
- V2 `for(i=0;i<N;i++){if(*p==0)break; p+=S;}` + TAIL-LI negated mark/zero + negated name==0 if/else: **365** — unrolls FIRED (for-break form = era bdnz sets; while-&& form does NOT unroll at 2.6).
- V3 walker-snapshot temps (`w` hidden walker + per-iter `name = w;` write-back; early `k54/k44` bound readbacks): **397 (0x634)**. Copy-chain/init/slot-scan/chunks ALL region-parity.
- V4 negated empty-then if/else joins: INERT (folds to 3, same as V3).
- V5 `name = (i < 16) ? name : 0;` ternary joins: **401 (0x644)** = era tail-layout FIRES (cmpwi; bge TAIL; b; li@tail) +1 `mr r3,r6` copy per site (2 sites).
- V6 `if(goto arm)/goto join/label:` forward-goto chain: INERT (folds to 3).
- Champion state = tip (V6==V3 size, 397/399). one_shot (unlinked): **89.2406**, rows orig 399/ours 397.
- Commits: 84ca1111 V1, (V2), 283031a2 V3, 609dbb6a V5, b95f0425 V6 tip.

## V2+ VISIT-2 FRONTIER (ranked, UPDATED post visit-1)
1. SIZE +2W close attempt: kill V5's 2 `mr r3,r6` copies. V5 (609dbb6a, 0x644) has the era join layout; V3 (0x634) lacks the 2 `b` arms. Opening play: bind the ternary result to the WALKER register home (era li r8,0 = in-place write to the snapshot reg): spell `w = (i < 16) ? w : 0;` and consume `w` directly (drop separate `name` home in that region) — 1 probe. If INERT → era block-placement layout census (def-binding scheduler kin, LI-ZERO-COPY family), gate floor 0x634 (397/399 = 99.5% size).
2. Full gates on champion: `ninja && ninja changes && report_delta --check && check_pr.py` + regenerating baseline-report if stale-base hazard (skill).
3. Color rows @89.24 (one_shot unlinked view): (a) prologue slots 4-6 = our `addi r0+mr r31` vs era in-place `addi r31, r6, @l` = def-binding prologue pin (qvm-edc20 census, documented — do NOT grind decl orders); (b) slot-scan walk materialization: era walks `addi r4,0x9c0` then `lbz 0(r4)`; ours `lbz 0x9c0(r31)` big-disp first tests = scheduler split — screen 2 spellings max (rx-pump lever (2) hoist), census if inert; (c) init region colors (lis r5,1/subi AC44 vs li 44100 — check era's 2-insn form survives our li folding: era shows lis+subi = value materialized wide; ours emitted li@72c — +0/-0 size, COLOR row).
4. Sibling safety: report_delta regressions must = 0 (family census method: regenerated-base gnm diff).
5. DO NOT RE-ROLL (closed classes, visit-1 census): while-&& scan form (never unrolls); empty-then negated if/else (folds); forward-goto chain arm (folds); decl-order/prop windows for prologue split (family walls).
