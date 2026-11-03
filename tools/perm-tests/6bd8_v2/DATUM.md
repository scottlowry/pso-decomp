# TLobby__sub_80406BD8 — card-lobby-6bd8-v2 PARK (visit-2, Nov-3)

Unit psov3/pso/misc/TLobby_804050DC, gate size 0x2E0 (736) — gate-exact in ALL variants (184/184 rows).
Champion F2 = tip: **99.51087** paired, 12 residual rows (6 x2 mirrored arms). NOT 100 — no battery/ship (byte-exact-only policy).

## LADDER (what-moved log)
| step | change | score | note |
|---|---|---|---|
| reland | frozen v1 body (1e5823fa..3551f078) on 7008688d, apply CLEAN vs 61FC shift; FREEZE half-probe (3-stmt addr split) was SYMMETRIC/complete -> kept | **98.83152** | first score ever (v1 died unscored) |
| V2 | full stmt-split row/off/lo/mbr | 93.50543 | BAD: off-split -> lhz disp fold + sched wreck |
| V3 | swap only: addr = (w&0xFFFF)+addr; addr = mbr+addr | 98.88587 | +0.05 |
| A5 | b1 s32->s16 | 98.91304 | era extsh r0,r0 lands |
| B1 | row decl LAST (before su; su stays last) | 98.96739 | decl-LAST=rank-UP axis (CB44 B1 analog) |
| C1 | row two-stage ((s8*)row + 60*tbl) | 99.23913 | arm rows 24->28 but % UP (frame path opens) |
| E1 | C1 + prop-off | 98.75000 | FRAME FIXED 0x38, w=r5/rows=r6 land; merge-dest flips |
| F1 | C1 with `+=` row form + prop-off | 99.02173 | |
| **F2** | **C1 with `row += 60 * tbl;` plain** | **99.51087** | **frame trio + w/rows/lha/mulli all land; CHAMPION** |
| G1/G2/G3 | named `off` any placement | 94.07609 | ALWAYS folds lhz 14(rB) -> off MUST stay inline |
| V5/E6 | prop-off on pre-C1 | 98.47826 | window alone: frame fix - arm rot |
| F3 | prop+peep window | 0x314 | GATE FAIL -80% |
| A1 | ptr decl last | 97.93478 | NEGATIVE — rank-UP is per-var |
| A4 | carry s32 | 97.58153 | NEGATIVE |
| B9/B10/B11 | i/cnt/sum decl last | -0.3..-1.5 | NEGATIVE |
| B2..B8 | tbl/lim/n/pairs/w/addr/row-last misc | inert|worse | grid exhausted |

## RESIDUAL CLASS TABLE (F2; all x2 mirrored arms, slots 46,48,49,50,51,52 + 124..130)
Ours: addi r0,r3,0xe(fresh) | clrlwi r3,r5,16 | lhzx r0,r6,r0 | add r3,r3,r4 | add r3,r3,r0 | addi r28,r3,0
Era:  addi r3,r3,0xe(IN-PLACE) | clrlwi r0,r5,16 | lhzx r3,r6,r3 | add r4,r0,r4 | add r4,r3,r4 | addi r28,r4,0
=> one color-permutation cluster: era homes off@r3/lo@r0/addr-merge@r4; ours mirror off@r0/lo@r3/merge@r3.
Root = slot46 in-place-vs-fresh; dest-merge rows follow the swap.
Class: DEF-BINDING / COPY-SURVIVAL PIN (EDC20 lineage). NOT arg-prep-sched (all hoists — extsh r0,r4 head bind, sth su, lis/addi r31 loop hoist, rows-between-extrwi-and-mulli — already era-exact).

## ROSETTA RECEIPT (6 versions x F2/G1, harness-validated)
F2 source, inline `6 * (s16)b1 + 14`: 1.2.5n,1.3.2,2.0p1,2.6,2.7 ALL emit `addi r0,r3,14` fresh-dest — NO version produces era's `addi r3,r3,14` in-place from any arm spelling. 3.0a5 shape collapses (no addi-14 row). G1 named-off: fold to lhz 14(rB) in every 1.x-2.x version. => version-independent allocator pin, NOT EXTSH-BIND version-class. Era r-ring (off@r3, lo dead-r0-reuse) unreachable from these spellings on installed versions.

## HARNESS LAWS (integrator-caught, cost 2 probes)
1. NEVER run rosetta on the FULL TU at 1.3+ — file's include chain user-breaks (7/11 'User break, cancelled'); self-contained probe (hand typedefs + extern decls + function only) compiles rc=0 at ALL versions. Control probe = sibling kit /tmp/ctrl_cb44.cpp (git show 9b355319:...probe_cb44.cpp) green at 1.3.2/2.6 on same driver.
2. Probe needs `extern "C" {` wrapper (real file body lives inside file-scope extern C region) — else mangled relocs.
3. objdump renders immediates DECIMAL: era-shape grep must match `,14` not `,0xe`.
4. NEVER rm build/GPOE8P/obj/** (era-extract = objdiff target_path, no ninja rule to regen; recovered via main-checkout copy + sha match de0b6e11). The compiled unit .o is build/GPOE8P/src/... (objdiff base_path) — scoring needs ONLY that; no full ninja required.

## TWIN-ORACLE: REFUTED
Parent brief's "twin sub_80341F20 100% 988B": 0x80341F20 is not a psov3 symbol start (falls inside free_child__9TWindowDDFv 0x80341EF4+0x54 span); no config/ symbols/splits/report/src receipt anywhere. Real structural twin = the unit's OWN forward/backward loop pair (slots 32-52 == 110-130). No external spelling source used; era .s (build/GPOE8P/asm/pso/misc/TLobby_804050DC.s lines ~2020-2200) was the oracle.

## DECODE CONFIRMED
Segmented-packet ones-complement checksum over 12B segment array (arg0+4 = cnt; seg = {s16 len, u16 f2, u32 word, u8 kind}). kind{1,4}=*wp direct, kind2=pool-relative addr build (pool=network_buffer_pool_state: s16 count@0, rows@4; row=60B @tbl, member u16 @ +6*b1+14), kind3=p[1].word, kind0/>=5 stale-ptr skip; byte-pair sum via su union slot 0x10(r1) w/ odd-carry, helper TUdpSocket__sub_80419864 partial-sum, final 16-bit fold, u16 result. arg1==1 selects backward (cnt..1) vs forward (i=1..cnt-1, NOTE skips seg0 head: p=arg0+12, kind@p[1]).

## NEXT VISIT
12-row pin cluster: try permuter sweep on arm-tail dest survival (opt_dead_assignments off window; limb-split lo computed before guard); else era-object-layout/def-binding memo entry. Battery (full link + report_delta vs regenerated 7008688d base + check_pr) NOT run — park, nothing to ship.
