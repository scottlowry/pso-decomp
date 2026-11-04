# KIT_STATE — TLobby__sub_803C0238 (card t_180a8775, branch card-lobby-c0238-v1, base f4200fcb, tree f3)

GATE: symbols.txt row `.text:0x803C0238; type:function size:0x3F0` = 1008B = **252 insns** (counted, era block lines 365–632 of build/GPOE8P/asm/pso/misc/TLobby_803BFE50.s).

## CLASS TRIAGE — class B (moderate), NOT hard-wall
| Axis | Datum |
|---|---|
| Frame/bank | `stwu r1,-0x40` frame 0x40; LR@0x44; `stmw r23,0x1c(r1)` = 9 saves r23..r31; epilogue `lmw r23` mirror. Stack locals 0x8(r1),0xc(r1) (pair, D3130 out + read as 2 ints at f50-cb) and 0x10(r1) (address-only). |
| Args | 1: `mr r31,r3` = AudioStreamInputState* (caller process_audio_stream_input bl@803C00A4 passes r3=arg0 live; current skeleton decl `s32 fn()` is a stub lie — era reads fields of r3). Return: no r3 set before blr (falls on last bl result) → void. |
| Callees (bl, by address) | get_entry_id__6TLobbyFv@803C3A8C(×2), TLobby__sub_803C3ABC@803C3ABC(×3), get_field_a8__6TLobbyFv@803C3B4C(×2), TLobby__sub_803C3AC4@803C3AC4(1), init_scroll__6TLobbyFll@803C3A1C(1), TLobby__sub_803C3A04@803C3A04(1), TLobby__sub_803C34F4@803C34F4(1), get_field_0xa4__6TLobbyFv@803C397C(×2), get_field_a0__6TLobbyFv@803C3974(×2), TLobby__sub_803D3130@803D3130(×2), TLobby__sub_803C3B38@803C3B38(1), TLobby__sub_803C3984@803C3984(1) = 19 bl sites. 13 indirect bctrl. |
| Virtual slots | source(AudioStreamSource) vtable: 0x18 lock(s,1,0x7FFFFFFF,&f14), 0x1c unlock(s,mode,&chunk), 0x20 f20(s,mode,&chunk), 0x24 NEW f24(s,1,src->vt)->s32. rings[k] SjRingBuffer vtable (SjRingBufferInterface): 0x24 get_available(r,0,r->interface)->s32 (3-arg raw cast), 0x20 put_chunk(r,1,&locA), 0x1c unget_chunk(r,0,&locB). self+0x48(f4c ctx) 1-arg cb; self+0x50(f54 ctx) cb(f54,i,locA[0],locA[1]). |
| Data refs | **0 pool literals, 0 @sda21 refs** — ownership screen trivially clean; only literal built inline: `lis 0x8000; subi 1` = 0x7FFFFFFF (in-file precedent 312). No externs needed. |
| Control flow | 3-zone cascade, NO switch/jumptable, ONE pre-test counted loop (b→test; `blt body`): zone1 entry_id==0 handler (f3==1 probe, lock, a8==0&&rings[2]>=2&&u16@rings[1]==0x8001, f34>=3ABC, 3AC4/get_available half-compare, a8==10, init_scroll+3A04), join@803C03F8 (34F4, entry_id==3 big block + loop + 5-field accum + f3c/f40/f48 cb gate + 3984), zone3 @803C05AC (lha 0xa8(rec)==10 → min+3-accum twin). 6 exits converge on join. |
| ps-arith | **0** (0 psq/fp/vec) → not hard-wall (rule 9 clear). |
| Narrow-load tells | `lha r0,0(r3); clrlwi r0,r0,16; cmplwi 0x8001` = (u16)s16 read; zone3 `lha 0xa8(r27); cmpwi 10` = s16 raw field read (no extsh head-bind → 6328 EXTSH-BIND class NOT engaged here; s16-param pin inapplicable, arg is pointer). |
| Signed div2 | `srwi r0,r3,31; add; srawi` = C trunc `/2` of signed virtual-call result (named temp, one use). |

## ANATOMY — register homes (the bank contract: 9 saves = 9 long-lived values)
r31 self | r27 rec(TLobby*=self->f4) | r29 rec copy / later get_field_0xa4 | r30 src(self->f8) | r28 delta=min(a0, 3ABC-f34) | r26 loop i (rebound) | r25 p8 cursor(+8) | r24 p4 cursor(+4) | r23 n2=delta*2.

## STRUCT NOTES
- self = AudioStreamInputState (in-file, lines 109–116): f3 read `lbz;cmpwi` NO extsb → declare **u8 f3** (was s8; stores are stb-only in matched siblings — verify siblings byte-stable post-edit). state=3 = stb 0x1 ✓ s8 fine (never read in fn). rings[4]@0xc..0x1b: era uses rings[1](0x14) as s16* window, rings[2](0x18) as scalar count, &rings[1] as lock out; rings[0] virtual lock/avail; loop reads *(self+4k+0xc)=rings[k] — array walk via u8* p4 cursor.
- f2c/f30/f34/f3c/f40/f44/f48/f4c/f50/f54 all used as in-file decl.

## SUB-GOAL DECOMPOSITION
G1 skeleton+signature compiles, void 1-arg, caller updated, siblings stable.
G2 zone1 (79 insns: 803C0238–803C031C incl. f24 probe, lock, a8/0x8001, f34>=3ABC exits).
G3 zone1 tail (31C–3F8: 3AC4+get_available/2 compare, a8==10, init_scroll, 3A04).
G4 zone2 min+D3130+virtual pair (3F8–4A8).
G5 loop 803C04AC–803C0534 (test-first, 3 cursors, f50 gate cb, put/unget pair).
G6 accum 5 fields + f3c/f40/f48 cb gate + 3984 (538–5A8).
G7 zone3 twin 5AC–614 (lha 0xa8==10, min, 3-accum).
G8 epilogue bank lmw r23 + frame (auto if 9 homes land).

## VISIT-2 FRONTIER (ranked)
1. **stmw r23 bank**: needs exactly the 9 homes live across calls; decl at top + assign before first bl (RX-PUMP law #1: early materialization of self/src/rec). Frame 0x40 comes free with bank+3 locals.
2. Per-site vtable reloads: era does `lwz r6,0(r30); lwz r12,0x1c(r6)` per call — spell `src->vt->slot(...)`, never cache vtable in a local (CSE law, inverse).
3. min() spellings era = bge-skip + mr (tail-li mirror ref: NEGATED polarity probes): `if (a0 < v) v = a0;` two sites (G4/G7 twins — TWIN-PARALLEL, verbatim second instance, no D3130/loop in twin).
4. f34>=3ABC exit as ONE if (cmpw+blt-to-next = era's blt skip layout; 427-429).
5. Loop = `while (i < TLobby__sub_803C3B38(rec))` with cursors u8* p8/p4 + i; era init mr r25,r31 / mr r24,r31 / slwi / li 0 / b-test.
6. `0x7FFFFFFF` literal lands lis+subi (in-file precedent).
7. u8 f3 decl flip — screen sibling bytes after (only byte-stores exist in matched fns).
8. Colors/bank-ring: residual expected = def-binding family; do NOT spend >1 probe per color class.

## FOLD-INTEL (TLobby tail cluster census@5: 6328/CB44/BA38/6BD8 pinned walls)
My block shows NO 6328-style extsh head-bind (pointer arg, raw lha loads), NO magic-division family (only srwi/add/srawi /2 = plain shift path, divisor 2), NO CB44 clrlwi-mask tests beyond the 0x8001 u16 check (decode: (u16)(s16)v == 0x8001 = live test, keep HIGH-16 mask semantics). Style = house virtual-cascade (in-file siblings process_audio_stream_input/sub_803C0628 matched) → per-function version markers of the tail walls do NOT claim my regions.

## STATE LOG
- visit-1: triage done (252 insns gate, class B, ps-arith 0, pool-refs 0); skeleton authored; control probe → see git log.

## V2 FRONTIER (cold-start for visit-2 — measured on committed tip 79ee0e85, clean rebuild)
- TIP STATE: probe-1 skeleton 0x3F8 (+2W) → probe-2 (era per-site ring reload inline; f3 s8 signed cmpwi) = **0x3F4, 253 insns, gate +1W; one_shot pair 97.53968; 35 siblings 100.0 stable; prologue byte-shape EXACT (stwu -0x40, stw LR 0x44, stmw r23,0x1c, mr r31,r3; epilogue lmw r23 mirror)**.
- ONLY residual size site: OURS 0x5dc–0x5e8 zone-2: `bl get_field_0xa4` → `mr r0,r3; mr r3,r30; mr r27,r0; bl get_field_a0` vs era `mr r29,r3; mr r3,r30; bl a0`. Extra = r0 hop: MWCC homes w→r27 (late reg) and splits the def-binding; era binds w→r29 in one mr because its zone-1 rec home is r27 (OURS rec→r28).
- ROOT MAP (rotate-by-one): era {self r31, rec r27, lobby r29, src r30} / zone2 {v r28, w r29}; ours {self r31, rec r28, lobby r29, src r30} / zone2 {v r29, w r27}. Fixing rec→r27 lands the whole chain.
- VISIT-2 RANKED:
  1. rec-home lever (ONE probe, then census): spell prologue rec def so MWCC binds r27: candidates — declare rec LAST in locals block (decl-order binding), `void *rec` + casts, rec = (TLobby*)((u8*)self+4) address-arithmetic def, init rec at top alongside self. If rec binds r27: expect v→r28,w→r29, r0 hop dies, gate 0x3F0.
  2. If +1W persists after 2 spellings → DEF-BINDING PROLOGUE PIN class (QVM-EDC20/CB44 law: register kw/chain-assign/prop-off all inert) → park at 253, write rosetta fingerprint receipt (era 253-1: installed 2.6 emits the hop; check 1.3.2/2.0p1 for hop-free binding) — 20-version sweep ONLY if 2 spells fail.
  3. Rows at 97.54 (~12 diff rows): expected color/label class — cmpw/blt label-render, `lis r5,-32768` (objdump signed render of 0x8000 = era `lis r5,0x8000` identical bytes), addi r5,r5,-1 vs subi (same bytes; objdump pseudo-diff), slot order locA@0xc/locB@0x8 vs era locA@0x8/locB@0x10 = D3130 out-param SWAP: era first out lands 0x8 (pair 0x8+0xc), second 0x10; OURS inverts → declare `s32 locB; s32 locA[2];` order flip (address-taken decl order = slot birth order, GC/1.2.5n FIRST-USE law RX-PUMP#slot-alloc; at 2.6 try decl swap 1 probe).
  4. DO NOT re-roll: pragma windows (mid-body pragma byte-ignored per RELBASE), struct spellings, ring kw. Loop/zone bodies verified multiset-identical to era.
- MEASURED: baseline-f4200fcb.json (in-tree); gate from symbols.txt row size:0x3F0.
- Files: src/pso/misc/TLobby_803BFE50.cpp (body lines 282–387); KIT_STATE.md. Commits: 16868123 (skeleton+triage), probe-2 commit (ring inline + f3 s8).
