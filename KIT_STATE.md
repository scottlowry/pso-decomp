# KIT_STATE — card t_070a0f52 evaluate_ground_triangles (CsnQuery.cpp, 0x800791BC, 0x3C4)

Branch `card-csnquery-964` @ base 5695627b. Tip: authored floor, 83.06224, size gate exact,
26 siblings 100.0 (zero regressions), unit 81.99 -> NOT linked (26/27 fn exact).

## PS screen (GATE #1)
ps-arith (GSP family ps_add/ps_mul/ps_sum/lhf/2+reg): **0**. 8 hits are Gekko
`psq_l/psq_st` FPR-save quadword spills (base+disp(r1), QM=0), NOT the fleet ps wall.
In-unit twin precedent: same spill pairs inside 100%-matched siblings
intersect_wall_triangle_one_sided, TObjPlayer__sub_80079DE0, prepare_wall_query_polygons,
query_collision_segment_groups. Route taken: full twin+author (screen=0), not ps-wall floor.

## Anatomy (class A/B/C)
- Frame 0x90; lr@0x94; f31..f28 = stfd+psq_st pairs @0x80/0x70/0x60/0x50 (+0x88/0x78/0x68/0x58);
  stmw r18 (r18..r31, 14 GPR homes) @0x18; local sp8[12] @0x8 (vsub out, result dead).
- Bank: mask r18, groups-cursor r19, status-ptr r20, rec r21, recs-base r22, poly(org r23),
  verts r24, count r25, i r26, mrest r27, bit8 r28, bit2 r29, bit4 r30, bit16 r31.
  FPR: px f30, py f29, pz f28, cap f31.
- Callees: vsub__FPvPvPv (0x8039D8F0), TObjPlayer__sub_80079110 (0x80079110 stub),
  TObjPlayer__sub_8007910C (0x8007910C stub, rec+&debug_color_blue).
- Data map: lbl_80500140 = CsnHit{u32 status; CsnContact* contacts} (cleared at entry,
  per-block bits 0x10/0x4/0x2/0x8/0x1, return status&1); lbl_8050BF60 = raised origin temp
  {x, y+F8, z}; lbl_80500140[1] = CsnContact[5] slots idx 0..4; sdata2 F4=cap(f31),
  F8=scale/raise const (6x lfs remat, never homed), FC=plane-d eps, 200=edge eps;
  debug_color_blue @0x804A7458.
- Control: outer `for(;*gp;gp++)` over CsnGroup** -> model{verts@4,count@8,polys@0xc};
  inner poly(0x24 stride): flags&mask gate, XZ circle reject, d>=FC, all-verts-y>py reject,
  3 CCW edge cross rejects (fmsubs+eps), t = -((y0-py)*d + x0*a - z0*c)/(F8*d),
  5 bit-gated 28-byte record writes (slots bit0x10->+1, 0x4->+2, 0x2->+3, 0x8->+4, 0x1->+0
  w/ t<cap extra guard), shared tail calls 9110/910C per tri.

## Residual (40 rows, all color/order)
Identical instruction multiset; deltas = bank rotation (gp r30/r31 vs era r19; status r31 vs
r20; recs r29 vs r22; loop vars 19-22 vs 23-26; bits 23-27 vs 27-31) + clear region
(era: li r0; lis r7,lbl@ha; stwu r0,lbl@l(r7) — deferred materialization fused;
2.6 emits lis; addi; li; stw from every decl/stmt permutation tried incl. zero-local,
stfsu analog for lbl_8050BF60 DOES fuse). = def-binding prologue pin kin (QVM/EDC20 class).

## Closed classes (do NOT re-roll)
- decl-order/binding permutations: passes 2 vs 3 byte-identical .o (INERT).
- (mask>>N)&1 spellings -> extrwi; `mask & 0xX` (u32) -> era rlwinm 0,N,N. FIXED in pass2.
- k-as-local homes f31 -> 5th FPR spill, frame 0xA0. Inline-remat FIXED (gate size).
- `*p = 0` pointer form and `arr[0] = 0` index form both emit lis+addi+li+stw; no fusion.
- CLOSED list from brief honored (tiebreak wall, COPY-BIRTH-TOP, self-accum fmuls,
  MIRROR-BASIN, def-binding prologue pins, decl-order slot stratum).

## Frontier for visit-2 (ranked)
1. stwu-deferral for lbl_80500140 base (4 rows + slot-shift cascade ~8 rows): try pool-read
   pragma window (references/pool-read-pragma-breach.md) and 2-symbol spelling screen.
2. Bank rotation: ring census (20-version equip-bank fingerprint method) before any grind;
   era bind seq gp,org,recs,mask,status@(clear-first) vs ours gp,org,mask,recs,status.
3. li r0,0 placement @12 (prologue-first) — rides on (1).

## Cold start
cd /Users/scott/Hermes/pso-decomp/pso-decomp-f7
git branch --show-current  # card-csnquery-964
rm -f build/GPOE8P/src/pso/map/CsnQuery.o && ninja build/GPOE8P/src/pso/map/CsnQuery.o
/opt/homebrew/opt/binutils/bin/nm -S build/GPOE8P/src/pso/map/CsnQuery.o | grep evaluate  # 0x3c4
<venv py3.14> ~/.hermes/profiles/pso-decomp/skills/pso-decomp/scripts/one_shot_diff.py psov3/pso/map/CsnQuery evaluate_ground_triangles

## V2 CAMPAIGN CLOSE (card t_ec3a4d84, branch card-csnquery-v2, base e175bcd9, Nov-4)
Seed 394a2bbf survival EXACT (83.06224 PAIRED 241/241, gnm 0x3C4, fresh control measure).
CHAMPION = b3a06cf2 (W2): named-temp crown (named zero-def + deferred store + recs/status
def-moved BELOW the clear store) + opt_propagation/opt_dead_assignments function window:
83.3112 (+0.249), gate 0x3C4 exact — status-home `mr r29,r7` lands era-exact def-slot.
Opener verdicts:
- pool-read-pragma trio function window (opt_common_subs+prop+dead, crawfish key): INERT
  against stwu fusion, +2W GATE KILL (0x3CC, 82.36514). Reverted.
- named-temp crown: PARTIAL WIN (+0.249, committed). stwu fusion itself NOT reached.
- bank census (one_shot rows): GPR color pairs ~42 rows (recs r22->r30 family=27, poly
  r23->r19, status r20->r29, gp r19->r31, bits era r28-31+mrest r27 vs ours r23-27) + FPR
  rank swaps ~27, ~0.5-weight => bank family ~34.5 of 40.8 deficit units; clear-site window
  slots 12-16 (5 shown rows) + full-value structural ~6. Era bank ascending =
  gp,status,rec,recs,poly,verts,count,i,mrest,bit8,bit2,bit4,bit16 (reverse-of-2.6-decl law).
- CLEAR-SITE FUSION SCREEN (stwu li;lis;stwu sym@l class): REPRESENTABLE at pin — repo's own
  text_803D31A4.cpp init_callback_tables__6TLobbyFv (co-DEFINED global + (s8*)&obj+K store
  chain) emits the fused shape at THIS profile (build .o: li r0;lis r3;stwu;stw 4(r3);8(r3)).
  Era corpus: 24 sym@l stwu, multi-field-clear family signature = update feeds disp chain.
  Transfer probes: typed extern view sized (s32 def) -> SDA21 remat fold (li rD,sym@sda21)
  -4W GATE DEAD (SIZED-EXTERN SDA21 law fires); in-TU def exact era size 0x8 -> same sda21
  fold -4W GATE DEAD (MWCC small-object .sbss placement vs era addr 0x80500140 far-sda).
  Remaining rung: def >8B (e.g. slots[35], 0x94 era-runtime-sized) to escape .sbss window —
  NOT built (grind cap 4/4 spent; carries data-pairing size risk vs symbols row 0x8).
  Successor micro (spelled, 1 build): def CsnHit{u32;u32;u32 slots[35]} lbl_80500140; +
  corpus store-chain spelling; verify matched_data + siblings gnm.
Campaign close-out: NOT double-negative (crown positive) => park at 83.3112, no v3 grind
from closed classes; successor exists ONLY as the size-risk def rung above.
Budget: 4 grind (W1 trio-bust, W2 crown-WIN, G3 typed-extern-bust, G4 def-bust) + 1 confirm.
