# KIT_STATE — campaign fn_803C8020 (AdxStreamRuntime 1200B giant) — card t_f0357fb8

Branch: card-adxr-c8020-v1. Base: d82be2a8 (origin/master, "Matchpass lane7 (#188)").
Unit: src/pso/system/AdxStreamRuntime.cpp. Era block: build/GPOE8P/asm/pso/system/AdxStreamRuntime.s
lines 2684-3027. Gate (symbols.txt 26230): `.text:0x803C8020 size:0x4B0` = 1200B = exactly 300 insns.
Unit pin: MWCC GC/2.6, `-O4,p -inline off -use_lmw_stmw on -char signed` (build.ninja:64271-64277).

## FUNCTION MODEL (fully decoded, visit-1 anatomy)

Two-pass ADX per-channel block encoder (leaf, no calls): pass 1 = analysis over source
samples writing clamped residuals to a ctx-side buffer + max-|residual| tracking;
mid-section = scale + inverse-scale derivation; pass 2 = quantize to ADX range
coefficients (bytes) with mirror-state reconstruction.

Caller (era adx_encode_available_blocks, .s:2349): `mr r3,r29(ctx); mr r4,r25(i); bl
fn_803C8020` per channel i < ctx->0x58; after return reads ch->0x7c (scale), ch->0x80
(double), ch->0x88 hist pair. Signature evidence: s32 fn(u8 *ctx, s32 ch_idx); returns 0.

### Frame / bank (class screen)
- Frame: `stwu r1,-0x30(r1)` = 0x30, epilogue `addi r1,r1,0x30`.
- Leaf: NO `bl`, NO mtlr, NO stmw/lmw/_savegpr — individual `stw r31,0x2c / r30,0x28 / r29,0x24`.
- Stack slots: 0x8/0xC = s32->f64 2^52+2^31 bias construction; 0x10/0x14 = fctiwz store+read.
- Callee-save roles (r29/r30/r31 recycled across regions):
  loop1: r29 = fill counter / c6 lha operand; r30 = fill cursor (mr r30,r9) / c4 operand;
         r31 = c6*hA mullw result.
  loop2: r29 = fill counter, extsh(cv) copy, then `lwz r29,0x88(r9)` hist pointer;
         r30 = fill dst, c4 operand, hist->8 copy; r31 = extsh coefficient operand.

### Callee map
Empty (leaf). No repo decls consumed.

### Data refs
| sym | section/size (symbols.txt) | decoded value | role |
|---|---|---|---|
| lbl_805D4660 | .sdata 4B, =0x00001000 | 4096 | scale upper clamp (writable global) |
| lbl_805E0D40 | .sdata2 8B align8 double | 0x4330000080000000 = 2^52+2^31 | compiler int->f64 bias const (auto from casts; also lfd 0x4330... via sda21 at 803C81E4/8218) |
| lbl_805E0D48 | .sdata2 8B align8 double | 0x40DFFFC000000000 = 32704.0 | full-scale value: inv = 32704.0/maxabs |
- All refs are `@sda21` 1-insn form (no @ha/@l, no pool base pair, no relbase class).

### ps-arith screen
`ps_(mul|add|sub|div|madd|sum...)` count = **0**. FP = scalar f64 only: lfd 7, stfd 3,
fsub 2, fmul 1, fdiv 1, fctiwz 1. Int mult chain: mullw 7, mulhw 3 — the Adx magic family.

### Magic chains (proved numerically over the full input domain, visit-1)
1. Scale seed: `mulhw(0x92492493, maxabs-1)` + add + `srawi 2` + sign-fix + 1
   = `(maxabs - 1) / 7 + 1` (4*2^32/0x92492493 = 7.0000000; signed-trunc, x>=0 domain).
   Single chain, shared-dividend form.
2. Coefficient: TWICE, per branch of `(s16)c < 0` (803C8388 / 803C83A8, full lis/addi
   0x38007001 + mulhw + srawi 10 + srwi/add sign-fix each):
   `if (cr < 0) co = (cr - 2340) / 4681; else co = (cr + 2340) / 4681;`
   (2^42/0x38007001 = 4681.0; 2340 = (4681-1)/2 -> trunc = round-to-nearest).
   VERIFIED identity over q in [-32768,32767] = trunc((q+sign*2340)/4681).
   = PER-BRANCH MAGIC-CHAIN DUPLICATION census row (mwcc-notes-2 line 10, sibling card
   adxr-c7df0, SAME FILE, proven spelling: spell the division twice).
3. Prediction: `(c4*h8 >> 12) + (c6*hA >> 12)` in both loops — TWO mullw + TWO srawi +
   2x subf (loop1: shifted per term). Loop2 reconstruction: `(h->c4*h->h8 +
   h->c6*h->hA) >> 12` — ONE srawi after combined add. Two distinct term forms, both present.
4. s32->f64 via bias: stw 0x43300000 / stw (v^0x8000) / lfd / fsub C / (fmul) / fctiwz /
   stfd / lwz. `lis r0,0x4330` appears 3x: 803C81DC (inv branch), 803C8214 (pre-loop2
   hoist consumed by 803C8328 stw r0,0x8(r1) INSIDE loop2), f2 bias lfd hoisted at
   803C8218 (lifetime across loop2). d80 reloaded per-sample (lfd 0x80(r9) at 8330, NOT hoisted).

### Control-flow skeleton (78 BBs, 4 back-edges)
- Prologue 803C8020-803C8070 (21): scale i by 4/2/64; ch = lwz 0x80+i*4; hist = lwz
  ch->0x88; ch->h8/hA = ctx s16 pair @0x88+2i/0x8C+2i; cursors; `b` tail-test.
- Loop 1 (analysis): test 803C8158 `lwz r0,0x44(r3); cmpw r8,r0; blt` (bound RELOADED
  each iteration), j+=1; src+=2 (r4), out+=2 (r5). Body: `if (j==0)` fill loop
  (803C8090, span 0x18: sth zero, k+=1, bound `lwz 0x14(r9)` reloaded) + `stw r11,0x78(r9)`
  (li 0); `if (ch != 0)` (cmplwi+beq, every iter): quantize->clamp->`sth 0x18(r5)`->
  maxabs chain->history shift (lha/sth/sth raw r0).
- Mid-section 803C8164-803C8224: scale = clamp((maxabs-1)/7+1, 1, lbl_805D4660) via
  min-then-max (era: r0=g; if v<g r0=v; if r0<=1 ->1 else ->(v<g?v:g)); `sth 0x7c`;
  inv: if m78==0 d80 = C48 else d80 = C48/(double)m78 (fdiv); hist->h8/hA = ctx pair
  (RELOAD of the same two ctx s16s — second read); li k=0; `b` tail-test.
- Loop 2 (quantize): test 803C84AC (`lwz r6,0x44(r3)`, blt 803C8228). Head (every iter!):
  sample=src[k]; `b->h8 = h->h8; b->hA = h->hA` via lha/sth pairs on r10 (UNCONDITIONAL,
  before k==0 test); k==0: fill loop + m78=0; b-guard; quantize->`sth 0x18(r4)` (b->q[k]);
  maxabs; b history shift; qq guard: `(b!=0) ? lha 0x18(r4) : 0` (lha RELOADS just-stored);
  extsh; bias->fmul d80->fctiwz->clamp16; per-branch /4681; clamp[-8,7]; `stbx 0x58(r9,k)`;
  rec = clamp16(co*s7C); `lwz r29,0x88(r9)` (hist RELOAD from b, not r10!); h-guard;
  pred 1-shift form; `sth h->hA=h->h8; sth h->h8=rec`. Tail: src+=2, q+=2, k+=1.
- Epilogue 803C84B8-803C84CC: lwz r31/30/29, `li r3,0`, addi r1, blr.

### Struct layout (evidence: disps + caller + fill/coef bounds)
ctx (u8*, arg0): +0x18 residual s16 stream base (ch slots stride 4, len n44),
+0x44 s32 samples-per-block (loop bound), +0x58 s32 channel count (caller),
+0x80 ch[2] pointer array (stride 4), +0x88/+0x8C s16[2] predictor seeds,
+0x90 samples (ch slot stride 64, s16[n44]).
ch block (AdxEncBlock): +0x4/+0x6 s16 predictor coefficients (Q12 pair),
+0x8/+0xA s16 history (h2,h1), +0x14 s32 fill count (<=32), +0x18 s16[32] q out,
+0x58 s8[32] coef bytes, +0x78 s32 maxabs, +0x7C s16 scale, +0x80 double inv,
+0x88 u32 hist pointer (same-layout decoder mirror: consumes +4/+6/+8/+A).

## CLASS TRIAGE per block group
- A (transcribe-and-land): prologue scale chain; epilogue; loop tests (bound reload);
  mid-section scale/inv; coef/recon clamps (standard MWCC 2.6 clamp expansion).
- B (census levers, proven in-file): per-branch magic 4681 (c7df0 row); walker
  mr-alias inits (C5ED4 row: `mr r30,r9` fill cursor, `mr r4,r7` src cursor);
  tail-test for-form; sth->lha store-reload (twin row: `b->q[k]` read-back form).
- C (pin risk, census-flagged):
  1. LI-ZERO-COPY fill loops: `li r29,0; mr r30,r9; mr r12,r29` + sth r12 = hoisted-zero
     loop-seed form — loop-IV seed class (banked-allowed precedent exists; fold wall hits
     NON-loop spellings). Spell `s16 z = 0; for(k...) q[k] = z;`? Era r12 never increments.
  2. Bias lis hoist: single `lis r0,0x4330` at 8214 with lifetime across loop2 (stw r0
     inside loop) = scheduler materialization — C risk; 803C81DC's copy is branch-local.
  3. Loop2 head b->h copy every iter (reads h, writes b, b shift dead by next iter) —
     transcription order must match: copy BEFORE k==0 fill.
  4. r29/r30/r31 def-binding ring (two-loop shared bank) — census kin: qvm-edc20/C5ED4
     pure-ring floor class; expect residual rows, not gate loss.
  5. fdiv with f2=C48 loaded AFTER building denom (f0=denom; fdiv f2,f0 = C48/denom).

## VISIT PLAN
- V1 (this): anatomy + skeleton + control probe. DONE: model decoded, magic verified.
- V2: first block group (prologue + loop1) to structure parity; size trajectory;
  check bias/scale-chain emission; confirm siblings byte-stable (gnm word compare).
- V3: mid-section scale/inv exactness (min-max clamp spelling, fdiv operand order).
- V4: loop2 head (h-copy tempo + fill + LI-ZERO-COPY wall screen) + coef magic pair.
- V5: reconstruction tail + epilogue; full size gate 300/300.
- V6: color-ring residuals: birth-order levers (walker temps before counter, C5ED4);
  rosetta only if gate-exact + floor. Park classes per census (no re-roll).
Budget law: 3+ builds remaining before touching a C-class row.

## STATE LOG (append per visit)
- V1 d82be2a8+...: KIT_STATE authored; skeleton in-file (decl @ extern-C block 214,
  structs, body full-transcription draft); control probe score -> record in commit msg.
  ps_screen_count = 0.
- V1 probe trail (all on clean rebuild, rm .o first, MWCC line required):
  * f1e2c4e5 indexed draft: 64.973335, 242 rows, frame 0x20. LATER FOUND WRONG:
    loop-1 store target. Era slot 8 `add r5,r3,r0` (ctx+i*4) is REASSIGNED at slot 17
    `mr r5,r9` = b BEFORE the first store -> loop-1 residual stream lands at
    b+0x18+2j (b->f18), NOT ctx+0x18+i*4. ctx+0x18 is never written. Indexed draft's
    64.97 = row-pairing artifact of the wrong 38-insn-shorter head; score truth =
    semantic-first (no lies in code).
  * walker draft (pd/resw/pd2/qw + fill-walkers, loop1->b->f18 fix): 60.183334, 245
    rows, size 0x3D4 (gate 0x4B0, -58 insns).
  * Walker birth-order reorder (pcm,pd,b,h,resw = era slots 6-17): +0.01, INERT —
    C5ED4 birth-order lever measured non-transferable on this unit (per-unit law).
  * Siblings: gnm -S per-symbol vs REGENERATED d82be2a8 base .o: ALL function sizes
    byte-stable; only anonymous pool `@NNN` renumber (link-gated class) + our 2 new
    U externs.
- V1 FINAL (committed tip): match=60.183334, status=visit1-frontier.
- V2 probe trail (card t_a938d5a4, branch card-adxr-c8020-v1, all clean rebuilds):
  * control probe on 03553df8: 60.183334 CONFIRMED (receipt commit 7e425fc9).
  * FRONTIER-1 CLOSED: dual-4681 chains — tip 03553df8 ALREADY emitted BOTH full
    8-insn per-branch magic chains (verified in .o: neg = lis 14336/addi -2340/addi
    28673/mulhw/srawi 10/srwi/add + b; pos = same with addi +2340). The 55-insn gap
    was NOT CSE; it was CLAMP FORMS (below).
  * c1 (7ffa6640) 60.18 -> 74.28667, 268 rows: era clamp anatomy decoded from .s:
    era 13-insn "two-site" clamp = MIN SPELLED TWICE:
    `t = (v < -0x8000) ? -0x8000 : v;  cl = (t > 0x7fff) ? 0x7fff : ((v < -0x8000) ? -0x8000 : v);`
    (region-3 remat survives at pin; a single fused nested-ternary emits 8, and
    destructive if-if emits 7). Applied at v(x2)/cv/w sites + abs() spelled twice +
    bias extsh + qq guard + hn = (AdxEncBlock*)b->f88 per-iter reload.
  * c2 (642e7268) 74.29 -> 79.09, 300 rows = SIZE GATE EXACT 0x4B0: same two-spelling
    form at co (with >= 7), rec (<=/>=, bge-layout), mid scale. Era maxabs chain =
    `if ((cv<0?-cv:cv) > b->f78) b->f78 = (cv<0?-cv:cv);` (srawi/xor/subf remat x2).
  * c3 79.09 -> 84.473335, 302 (+2 over): era walker forms — fill/resw/qw as b-ALIAS
    `s16 *qz = (s16*)b; qz[0xC] = z; qz++;` (era sth 0x18(rD) on b-copy, NOT
    materialized b+24 + zero-disp); prologue bind trio; batched h-copy head
    (lha fA,lha f8,sth f8,sth fA); loop2-prep RELOAD seeds `sa2/sb2 = cf[4]/cf[0]`
    (2nd ctx read, era lha 0x8c/0x88(r6)); mid `lwz r8,g` early + `mr r0,r8` seed;
    unified temps. +2 came from: scale-clamp 2 seed mrs + pd2-binding mr.
  * c4 (tip) 84.47 -> 87.92, 300, GATE RESTORED. Three fixes: (1) `s16 *pd2 = (pcm
    expr); s16 *pd = pd2;` — era binds the pcm MATERIALIZATION to loop2-walker r7 and
    the mr-COPY to loop1-pd (removes loop2-prep `mr r10,r0` copy); (2) mid scale
    clamp = IN-PLACE g MUTATION, no seeds: `ts = g; if (sv < g) ts = sv;` then
    `if (ts <= 1) { g = 1; } else if (sv < g) { g = sv; } b->f7C = (s16)g;` (result
    lands in g's reg = era mr r0,r8 seed @8180 + region-3 cmpw remat + bge/mr/b/li-tail,
    exactly 11 rows; the ternary spelling adds 2 seed mrs); (3) qq guard = FULL
    if/else `s32 qq; if (b==0) qq=0; else qq=qw[0xC];` (era 6 rows incl. join b;
    `s32 qq=0; if(b!=0)` emits 5, missing the b).
  * c5 REVERTED (87.92 -> 85.35667, size 300): named raw byte-bases
    `u8 *cb=(u8*)ctx+i4; b=*(cb+0x80); u8 *cw=(u8*)ctx+i2; sa=*(s16*)(cw+0x8C);`
    (era lha 0x8c(r6)/lwz 0x80(r5) pure-base+big-disp form) REGRESSED 2.6 pts —
    MWCC 2.6 at pin folds `bp[0x20]`/`cf[4]` (addi-fused base + lwzx/disp-8) on this
    unit; that fold is a SCHEDULER STRATUM, not a spelling gap. DO NOT RE-ROLL.
  * Siblings re-check (V2): regenerated d82be2a8 base .o, gnm -S text symbols:
    base 105, ours 106, diff = ONLY `fn_803C8020 000004b0` added. All siblings stable.
  * FRONTIER-2 CLOSED: frame 0x30 + stw r29/30/31@0x24-0x2c landed with c1/c2
    (clamp-form pressure = slot demand, per AdPlayer F2F4 law). Bias per-iter
    `stw r0,0x8(r1)` on hoisted `lis r0,0x4330` = CONFIRMED emitted (loop2-prep hoist
    + per-iter store, era 803C8214->803C8328 kin). Residual: OURS homes 4 callee
    saves (stw r28,0x20) — era 3. Slot 0x20 r28 = 1 def-binding row + epilogue lwz
    r28 (2 rows); era 0x18-0x20 reserved-dead class = frame-size parity already exact
    (0x30 = stwu -48). r28 eviction = color ring class (see 5), not slot demand.
  * FRONTIER-3 CENSUSED (parked): LI-ZERO-COPY — both fill loops emit folded
    `li;li` zero pair (counter + value, independent lis) where era shows hoisted-zero
    copy `li r29,0; mr r30,r9; mr r12,r29` (z = (s16)k with k=0 folds to li under
    2.6; era keeps the mr). 2 sites x 2 rows, SIZE-NEUTRAL (3 rows = 3 rows).
    Encode-card fold law applies: census, don't grind.
- V2 FINAL (committed tip): match=87.92, status=visit2-frontier.
- V3 probe trail (card t_ab52ac54->t_ab52ac5c, branch card-adxr-c8020-v1, tip 541b900f start):
  * control probe: 87.92 / 300 / 300 / gnm 0x4B0 CONFIRMED on committed tip.
  * P1 g-decl position probe (frontier-3): `s32 g` decl after `s32 m` — INERT
    (slots 83/84 unchanged: scheduler pins magic-addi `addi rD,rM-hi,0x2493`
    before the global load; 87.92, 209 rows identical). REVERTED.
  * P2 rec-clamp if/else-if destructure (no-else form): GATE-BUST 0x4AC (-1 insn:
    destructure DROPS era's `mr r6,r8` fresh-result copy, emits 283 bgt/li tail
    with no raw-copy) + 87.58. REVERTED. Law: era rec region = 8-slot tail-li
    ternary-remat; destructive if/else-if is size-dead.
  * P3 ring lever (a) decl-order eviction: `cv` declared before `t`/`cl` — INERT
    (extsh r31 persists at 61; c6-home r29 bind is NOT decl-rank-owned). REVERTED.
  * P4 ring lever (b) reverse-decl bank: whole temp block reversed — BYTE-IDENTICAL
    .o to champ (cmp proof). Ring INERT to decl order in both directions.
  * RING CENSUS COMPLETE (5 rows banked: birth-order V1, decl-eviction P3,
    reverse-decl P4, clamp-slot-demand V2-c1..c4 (WON), r28-eviction V2-c4 (WON,
    3 saves now era-matching at tip) — def-binding stratum, do-not-re-roll.
    Both census-permitted levers spent -> per law the ring is CLOSED.
  * P5 = c1 (cf582ea6) WIN +1.35: mid-scale region3 tail-li mirror
    `if (ts > 1) { if (sv < g) g = sv; } else { g = 1; }` (replaces `if(ts<=1)
    {g=1;} else if`): era ble->tail-li + cmpw remat + bge/mr/b/li-tail pair
    FULLY; slots 93-102 now color-only. 87.92 -> 89.27, gate held.
  * P6 = c2 (ed4390d2) WIN +1.37: co-clamp mirror `if (t < 7) { co = (co<-8)?-8:co;
    } else { co = 7; }` (replaces ternary `(t>=7)?7:remat`): era region 238-244
    bge-skip/tail-li fully paired. 89.27 -> 90.636665, gate held.
  * P7 = c3 (2614927a) WIN +1.35: rec-clamp mirror `if (t < 0x7fff) { rec =
    (rec<=-0x8000)?-0x8000:rec; } else { rec = 0x7fff; }`: era region 280-285
    fully paired. 90.64 -> 91.986664, gate held.
  * TAIL-LI CLASS LAW (visit-3 discovery): when era clamp region = `cmp; bge/ble
    SKIP-to-TAIL-literal; remat-region; tail: li; join:`, spell the OUTER test
    NEGATED with the literal-assigned arm as `else { }` block:
    `if (t < K) { x = remat; } else { x = K; }` — the same-armed ternary
    `x = (t >= K) ? K : remat` emits the INLINE-literal layout (blt + li + b) =
    7-9 mirror rows per site. Positive-armed-ternary `(t > hi) ? hi : remat` DOES
    emit era ble-inline form when era is ble-inline (v/w regions: matched in V2) —
    the polarity of the source test follows the era BRANCH, not the clamp sense.
  * Residual at tip (204 rows): 137 pure COLOR (r9<->r7 b-home + scratch r6<->r4
    r0<->r4 r5<->r10 chains + hist r29<->r30/h8 r30<->r29 loop2-tail transpose —
    def-binding stratum, census above), ~40 branch-target RENDER (display),
    2 pool-name rows (113/126 lbl_805E0D40 vs @549 = unlinked-pool display),
    form rows ALL in parked classes: slots 7/11-17/120-124 = c5 REJECTED fold,
    11-13 = era `li r8,0` j-seed placement (early, before stw r29 + b-load),
    24-26/137-139 = LI-ZERO-COPY census, 83-84 = P1 g-addi swap (inert).
  * P8 (grind 9) prologue j-seed decl move (`s32 j=0` before bp decl) — INERT:
    slots 11-13 unchanged (stw29/lwzx/li), score 91.986664, rows 204 identical.
    Era's early `li r8,0` is scheduler-pinned placement, decl-inert (like P1).
    REVERTED; tip rebuilt clean: 91.986664 / 300 / 300 / gnm 0x4B0 CONFIRMED.
  * Sibling screen (gnm -S on tip .o): 106 T symbols = V2 base 105 + fn_803C8020,
    sizes per V2 regenerated-base table; edits body-only, no decl/extern/pragma.
  * BUILD LEDGER: control, P1, P2, P3, P4, P4-verify(cmp), P5, P6, P7, P8,
    final-confirm = 9 grinds + 1 confirm, budget-exact.
- V3 FINAL (committed tip 2614927a): match=91.986664, status=visit3-frontier.
- V4 probe trail (card t_98c68c69, branch card-adxr-c8020-v1, tip a9d427cd start,
  all clean rebuilds, rm .o + MWCC line):
  * control probe: 91.986664 / 300 / 300 / gnm 0x4B0 CONFIRMED (receipt c3a1feef).
  * SCREENS (no builds — law verification on the control .o, per brief scope):
    (1) LOOP2 HEAD h-copy tempo: batched lha(fA)/lha(f8)/sth(f8)/sth(fA) at slots
      130-135 = era order EXACT, rows are pure color (r9<->r7 b-home, r6<->r4) —
      C-class row 3 (copy-before-fill transcription order) CONFIRMED LANDED.
    (2) LI-ZERO-COPY: fold re-verified at slots 26/139 (ours `li r12,0`/`li r11,0`
      vs era `mr r12,r29`/`mr r11,r12` hoisted-zero copy), 2 sites x 1 row,
      size-neutral. Census row, NOT grinded (encode-card fold law).
    (3) COEF MAGIC PAIR: PER-BRANCH 4681 chains fully emitted per branch (slots
      216-232: extsh. Rc bge + lis/addi(-2340)/mulhw/srawi/srwi/add + b +
      lis/addi(+2340) chain — all residuals pure color r6<->r4); TAIL-LI co-clamp
      mirror (234-244) and stbx coef store `addi r6,r5,0x58; stbx` (245-246,
      color-only) LANDED. ZERO form rows in the coef region: both in-file laws
      are VERIFIED APPLIED at tip, nothing left to spell there.
  * P1 fill-seed order flip (frontier-3, both twins: `*qz=(s16*)b;` before `k=0;`):
    loop1 EMIT-IDENTICAL (slots 24-26 unchanged — head is scheduler-ordered there);
    loop2 twin FLIPPED 137/138 AND transposed cursor<->counter REG roles through the
    fill body (141-145: era cursor r29/counter r12, ours flipped to r12/r29):
    91.986664 -> 91.886665, +4 rows, gate held. BUST. REVERTED. Datum: era's
    li-first head tempo is NOT source-order-owned on this unit; the statement-order
    axis moves register ROLES, not emission order. Frontier 3 CLOSED.
  * P2 j-seed decl/stmt split (`s32 j;` + `j = 0;` as last pre-store statement):
    .o diff 204 rows IDENTICAL to champ, 91.986664. INERT (byte-shape).
    Frontier 2 CLOSED on second axis (P8 decl-move + P2 stmt-split both inert):
    era `li r8,0` at slot 11 = scheduler-pinned placement.
  * BUILD LEDGER: control + P1 + P2 + final-confirm = 4 builds of 9+1 budget.
  * Final confirm on committed tip: 91.986664 / 300 / 300 / gnm 0x4B0 CONFIRMED.
  * Siblings: body-only probes, both reverted -> stable by construction.
- V4 FINAL (committed tip): match=91.986664, status=floor-census.

## V5 ENTRY LIST (campaign closure table — residual census COMPLETE, V4)
Every V1-V4 entry-list class is landed, screened, or closed with a datum. The
204-row residual at 91.986664 partitions fully into non-source classes:
| class | rows | slots | status |
|---|---|---|---|
| def-binding COLOR ring (b-home r9<->r7, cv r29<->r31, hist r29<->r30 loop2-tail transpose, scratch chains) | ~137 | 1-2,5-6,9-10,14-19,21,23,31-42,50-92,104-135,144-293 (color parts) | RING CLOSED (V3 census 5 rows, both levers spent, reverse-decl byte-identical) |
| branch-target RENDER (era .L vs ours +offset; display-only) | ~40 | every b*/bl*/beq/ble/bge row | unfixable in source |
| pool-name display (lbl_805E0D40 vs @549) | 2 | 113, 126 | unlinked-pool naming = config class, not source |
| j-seed placement era `li r8,0` slot 11 | 3 | 11-13 | scheduler-pinned (P8 decl + V4-P2 stmt both inert) |
| fill-seed tempo + LI-ZERO-COPY | 4 | 24-26, 137-139 | CLOSED V4-P1 (stmt axis moves reg roles, bust) + V2 FRONTIER-3 census |
| g-load/magic-addi swap | 2 | 83-84 | scheduler-pinned (V3-P1 inert) |
| c5 fold stratum (pure-base+big-disp lha/lwz; lwzx/addi fold) | ~12 | 7,12,14,16-17,120-124 | REJECTED V2-c5 (-2.6), do-not-re-roll |
No unspent form classes remain. Per VISIT PLAN: V5 = "reconstruction tail +
epilogue; full size gate 300/300" — TAIL-LI rec-clamp landed V3-P7, epilogue
matches exactly (zero diff rows 294-300), gate EXACT since V2-c2. CAMPAIGN
STATE: census-complete floor 91.986664 (gate 0x4B0 EXACT, 300/300 rows).
Remaining gap = def-binding lineage (qvm-edc20/C5ED4 kin) + display classes.
RETIRE the form-class pursuit; next act for this function = integrator merge of
the branch as-is, not visit-5. If a future tool/era-map surfaces a def-binding
mechanism, the 137-color ring is the single reservoir (~92.3 predicted cap
per V4 entry-list #4 arithmetic, all classes above at their measured floor).
COLD-START V5: nothing to probe; run control battery once on tip, confirm,
hand to integrator (kit: rm .o + ninja + one_shot + gnm 0x4B0).

## V3 ENTRY LIST (frontier, ranked; from c4 tip = 87.92, 300 rows, gate exact)
Residual anatomy at c4 tip (209 objdiff diff rows): ~25 = branch-target RENDER
(era .L_803C vs ours +offset — display-only, unfixable); ~131 = pure COLOR
(same mnemonic+imm, reg diff); ~25 real form rows.
1. COLOR RING r29/30/31 + r28 (131 rows = biggest pool): era binds loop1 cv->r29
   (extsh), fill-IV->r29, hist->r29; cursor->r30; mullw->r31; ours rotates
   r28/29/30/31. Kin: qvm-edc20/C5ED4 def-binding ring (park-after-2-levers per
   brief; visit-1 birth-order INERT datum already banked — the 2 levers allowed are
   NOT yet spent on this terrain: (a) era binds sample raw r0/r6 and keeps cv
   extsh-home across maxabs remat — ours same shape, colors shift by the r28 save
   cascade: try evicting r28 with ONE merged temp in cv-chain (unify t/cl/cv names —
   partially done c3; check `lwz r10,120` scratch), (b) `mr r11,r12` fill value copy
   — era seeds store-value by COPYING zeroed counter: spell `s16 z = (s16)k;` NOW
   (c4 has it; c5 regression may have been cb/cw, NOT this — isolate z=(s16)k-only
   birth tweaks if budget allows). If both inert: PARK as def-binding stratum with
   receipt, census row contributed.
2. FORM rows ~25: prologue/loop2-prep cf/bp fold stratum (c5 = REJECTED datum, do
   not re-roll); scale/co/rec region layout mirrors (bge-skip vs blt-take =
   scheduler polarity, era region2 `cmpwi t,7; bge tail-li`; ours inlines) —
   ternary-vs-if/else polarity probes are the remaining class-A candidates:
   co/rec/v/cv/w clamps all land counts; layout mirror rows pair partially.
   Era rec region2/3 layout = if/else-if with remat spelled:
   `if (tr >= 0x7fff) rec = 0x7fff; else if (rec <= -0x8000) rec = -0x8000;`
   (era tail li at L2 after region3 — probe as ONE site first, gate check, then
   replicate; +0 => park class).
3. Era mid `lwz r8,g`@83 BEFORE magic addi (ours 84): g-decl position probe (cheap,
   batch with 2).
4. Bias `lis r0`/`mr r10,r0` pair at loop2-prep (ours slot 125 `mr r10,r0` = era
   slot 124 `lha r6,0x88(r6)` pairing shift): era consumes cw(=r6) at 124; ours
   pd2 binds r10 — check c4 disasm 1ad0-1af0: if `mr r10,r0` = pd2 copy remains,
   era binds pd2=pcm to r7 in PROLOGUE — ours prologue 192c `mr r10,r7` ✓ c4 fixed;
   leftover = color.
HARD CONSTRAINT: gate is EXACT 0x4B0=300 rows. Any lever must be size-neutral.
Probe ONLY one class per commit; rm .o + ninja + one_shot per rule.
Budget law: 3+ builds remaining before touching a C-class row (V2 spent all on A).
Suggested sequence: 2(lever a/b each 1 commit) -> layout probes (2) -> census+park.

## V4 ENTRY LIST (frontier, ranked; from tip 2614927a = 91.986664, 204 rows, gate exact)
The tail-li layout class MOVED +4.07 this visit -> visit-4 exists. Ranking:
1. TAIL-LI REPLICATION SCREEN (cheap, law already proven): v-clamp (814-815/871-872)
   and w-clamp (902) already pair era ble-inline form — CONFIRMED matched V2, skip.
   qq guard + b/h guards = era full-if/else, landed c4. No untried tail-li sites remain.
2. PROLOGUE j-SEED placement (3 rows: 11/12/13): era emits `li r8,0` (j) at slot 11 =
   after `mr r4,r7` (pd2 copy), BEFORE `stw r29,0x24` (slot 12) and b-load (13).
   DECL-MOVE PROBE DONE V3-P8: INERT (scheduler-pinned). Only untried axis: split
   `s32 j = 0;` into bare decl + statement `j = 0;` as last prologue statement
   before b->f8 store (statement-position grid, 1 build; low expectation).
3. FILL-SEED order (2 rows: 24/25, twin 137/138): era loop1 `li r29,0` (k) slot 24
   then `mr r30,r9` (cursor) 25; ours cursor-first (24) li-second (25). Loop2 twin
   era 137 `li r12,0` 138 `mr r29,r9` vs ours 137 `mr r29,r7` 138 `li r12,0`.
   Probe: swap the two statements (k=0 AFTER qz=(s16*)b assignment? NO — era LI
   FIRST: ours has k=0 before qz (803-804) yet emits mr-first. Reorder to
   `s16 *qz = (s16*)b; k = 0;` = emit-order probe, 1 build. Slot 26/139 =
   LI-ZERO-COPY wall (censused, do-not-reroll).
4. RESIDUAL = def-binding COLOR (137 rows: b-home r9<->r7, hist r29<->r30
   transpose, scratch r6<->r4/r0<->r4/r5<->r10 chains) + 40 RENDER + 2 pool-display
   + c5-fold class (REJECTED) + P1 g-addi swap (INERT) -> FLOOR. Ring CLOSED by
   census law (5 rows banked, both levers spent, reverse-decl byte-identical).
   If 2/3 inert: census-complete floor ~92.3 expected; document + retire the
   form-class pursuit, remaining gap is def-binding lineage (qvm-edc20/C5ED4 kin).
Budget note V4: 2-3 builds suffice for frontiers 2+3 + confirm.

## COLD-START COMMANDS (visit-4)
cd /Users/scott/Hermes/pso-decomp/pso-decomp-f3
git log --oneline -3   # tip = visit3 c3 2614927a (91.986664)
rm -f build/GPOE8P/src/pso/system/AdxStreamRuntime.o
ninja build/GPOE8P/src/pso/system/AdxStreamRuntime.o   # require MWCC line
/Users/scott/.hermes/installs/60d8a79da6991a71/environments/28d86d1068e44adc8d1a5d2ca8c63c2c/venv/bin/python3.14 \
  /Users/scott/.hermes/profiles/pso-decomp/skills/pso-decomp/scripts/one_shot_diff.py \
  psov3/pso/system/AdxStreamRuntime fn_803C8020 | head -4
# expect 91.986664 / 300 / 300 / size 1200 (gate 0x4B0); then probe frontier 2.
# Sibling safety at tip: V3 edits are BODY-ONLY inside fn_803C8020 (no decls,
# no externs, no pragmas) -> siblings stable by construction; gnm 0x4B0 row.
