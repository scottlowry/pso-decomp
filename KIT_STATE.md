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

## COLD-START COMMANDS (visit-3)
cd /Users/scott/Hermes/pso-decomp/pso-decomp-f3
git log --oneline -3   # tip = visit2 c4 (87.92)
rm -f build/GPOE8P/src/pso/system/AdxStreamRuntime.o
ninja build/GPOE8P/src/pso/system/AdxStreamRuntime.o   # require MWCC line
/Users/scott/.hermes/installs/60d8a79da6991a71/environments/28d86d1068e44adc8d1a5d2ca8c63c2c/venv/bin/python3.14 \
  /Users/scott/.hermes/profiles/pso-decomp/skills/pso-decomp/scripts/one_shot_diff.py \
  psov3/pso/system/AdxStreamRuntime fn_803C8020 | head -4
# expect 87.92 / 300 / 300 / size 1200; then control receipt commit.
