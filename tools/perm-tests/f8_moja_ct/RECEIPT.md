# f8-16 TObjEneMoja__ct disposition — card t_23a3b249 (FLOOR 94.082275)

Base e175bcd9, branch card-moja-ct, tip 2bb8919e (cand3).
Gate 0x278 (632B / 158 insns) EXACT from first build; 158/158 rows paired;
gates on committed tip: gnm T 0x278; full ninja green; report_delta vs
baseline-e175bcd9.json: regressions 0; check_pr PASS, link_units check OK (3309).

## Anatomy (all evidence-bound, era asm/pso/unk/text_800AF8B0.s)
- ctor(self@r30, ctrl@r4 unused, arg2@r29) — caller create__11TObjEneMojaFPv:
  __nw(0x40c) -> TObjEneMoja__ct(o2, o, arg0). Returns self.
- desc = lbl_80491828 (U in era .o; single-sym base, fused plain-addi offsets
  0x194=vptr __vt__11TObjEneMoja, 0xa0 motion-spec, 0x130 movement tbl, 0x168
  collision body parts) — prop-off REQUIRED (prop-on remats @ha pair +1W gate-dead).
- __construct_array(self+0x39c, RenderFadeState ct/dt, 0x1c, 4); vptr then name
  (TObjEneMoja__name lwz sda21 value -> self+0).
- vcall 0x144=apply_set_data__9TObjEnemyFPv (MojaVObj view, arg2), tail vcall
  0x148=clear_lobby_object_state__9TObjEnemyFv (names from __vt__ rows 81/82).
- clamp x2: f390=lbl_805D9C60+f358, f394=lbl_805D9C64+f35c, clamped
  [lbl_805D9BD8, lbl_805D9BDC] via store-then-reload-if pair.
- bind_enemy_combat_stats self tbl1=lbl_805D50C8[i], tbl3=lbl_805D50CC[0x380+i*3],
  tbl2=lbl_805D50D0[i], i=self->0x368 (0x380=0 store + reload survives prop-off).
- 0x350 = (desc+0x130) + i*0x1c (tbl named-temp fused addi form = era assoc).
- tail flags 0x33a/0x33c/0x37c/0x384/0x388, add_flags_2e4(1), 0x30 |= 0x40000
  (oris imm 0x4), f38c=MIN, 0x398 = create__13TUnk_80494968FUlUl(0xff303030,0x0a303030),
  dispatch loop x4 activate_and_dispatch(self+0x39c+off).

## Probe ladder (8 grinds + 1 confirm, teeth honored)
1. cand1 full transcribe w/ push{common_subs off,prop off}: 91.58 gate-exact.
2. drop common_subs off: bind tbl/index swap lands: 91.74. (CHAMP window = prop off only)
3. drop all pragmas: 0x280 GATE DEAD (+1W desc @ha remat) — prop-off conviction.
4. parts-tbl loop trio: parts temp -2 (mr/addi order), tbl +1, loop-init-swap
   li-order +2: 91.46.
5. revert parts: 94.08 (cand3 = tip).
6. create-block stmt hoist (0x38c above |=): 90.79 — lfs over-shoves to slot127;
   era slot130 mid-GPR-cluster = interior lowering, no source boundary (CONVICT).
7. loop tail order swap: byte-identical binding, inert.
8. named mul temp (0x350): inert — operand roles naming-invisible (RA class-rank).

## Residual 27 rows = closed families (no grind budget left; classes on card list)
- slots 2/7: prologue lis scratch r4 vs era r6 (COLOR-SELECT-PIN kin).
- slots 30-51, 130-134: FPR pool-load hoist positions + K/sum/field FPR mirror
  {f2/f1/f0 vs f1/f0/f1} (def-binding FPR rank, f27c closed; head-block cluster).
- slots 102-106: {r0<->r4} operand roles in 0x350 block (P8 negative datum).
- slots 140-145: loop IV ring {i<->off} = {r29<->r31} mirror swap.

## TWIN-RUNG SEAL (free, zero-build) -> SUCCESSOR PLAY (+~2.0 expected)
Era twin Bm5GibonU__ct dispatch loop is structurally identical (li r29,0; li r31,0;
addi r3,r31,0x3f4; ... cmpwi r29,4) and OUR committed 2.6 twin .o emits it
BYTE-IDENTICAL (i->r29 ascending). Twin source spelling:
  for (i = 0; i < 4; i++) { ((RenderFadeState*)(&(...)->subs[i]))->activate_and_dispatch(); }
= single IV + array-index -> strength reduction emits the era pair.
SUCCESSOR: replace 2-induction spelling with single-IV stride spelling:
  for (i = 0; i < 4; i++) { activate_and_dispatch__15RenderFadeStateFv(self + i * 0x1c + 0x39c); }
(one build, 4 rows at stake, era binding proven emitted at this pin).
Remaining ring-adjacent closed classes above bound ~5.9 pts absent a bind mechanism.

## SUCCESSOR PLAY v2 (card t_907b8fcd) — PARTIAL LAND +0.19 -> FLOOR 94.27215
Single-IV strength-reduction spelling (twin Bm5GibonU__ct form; `off` decl dropped
under prop-off phantom-slot law) landed at cand4 f7b63377: loop-IV ring slots
140-145 ALL pair (era li r29/li r31 -> cmpwi r29,4 emitted byte-identical,
i->r29 ascending proven at real-TU scale). Official scorer 94.082275 -> 94.27215:
ring family = 2 scorer rows (27->25), NOT ~6 — the +2.0 expectation was
slot-count-inflated (slots != rows on the weighted scorer).
Gates on committed tip: gnm T 0x278; 158/158; full ninja rc=0; report_delta vs
baseline-e175bcd9.json regressions 0 (New exact 19 = whole-branch cumulative);
check_pr PASS; link_units check OK (3309).
Residual 25 slots = 3 closed families (prologue lis {r4<->r6}; FPR pool-hoist +
{f2/f1/f0} mirror 30-37/46-51/130-134; {r0<->r4} operand roles 102-106) —
def-binding lineage. Budget 2 grind + 1 confirm: used 1 grind + 1 confirm;
grind 2 deliberately SPARED (closed-class law, no open plays).
Unit linkage: pso/unk/text_800AF8B0 NOT complete (symbol pair 94.27215) — no
linked_units row, 3309 stands. Campaign CLOSED at floor 94.27215.
