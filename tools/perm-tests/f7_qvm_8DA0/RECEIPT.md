# PARK RECEIPT — TQuestVmDownLoadServer__sub_803E8DA0 (fleet/f7, card-qvm-8da0)

Unit `psov3/pso/misc/TQuestVmDownLoadServer_803E6970`, era row: `.text:0x803E8DA0 size:0x308`
= 776 B / 194 insns (verified against `symbols.txt:26992` AND the one_shot ORIG column — brief's
"~780 B ballpark" confirmed, not used as a number).

Supersede check: no local/remote branch for 8da0; symbol was forward-declared only
(`src/.../TQuestVmDownLoadServer_803E6970.cpp:392`) and absent from the base `.o`. Control probe on
the untouched base: sibling `TQuestVmDownLoadServer__sub_803E8C2C` pairs at 100.0 → toolchain sane.

## Semantics decoded (all from the era block, corpus-confirmed by matched siblings)

Replace-or-add a named message record:
1. `lbl_805D7868 = 1` (inlined `TQuestVmDownLoadServer__sub_803E8918`, 0xC B at 803E8918).
2. Bucket walk 1 over the sorted list at `(u8*)&lbl_80591EC8 + 0x2000 + (h<<2)`,
   `h = (u8)name[0] in [0xA0,0xF0) ? c-0xA0 : 0` — identical to matched `Hash_803E8B1C`/
   `Hash_803E8C2C`; exit on `(s16)ent->len == req->len` after `strncmp(ent->name,name,(s16)len)==0`,
   or on `strncmp > 0`.
3. Slot = `prev ? &prev->next : &tbl[h]`.
4. Re-verify (`ent->len == req->len` **unsigned-lbz vs signed-lha → `cmpw`**, then the FLIPPED-ARG
   `strncmp(name, ent->name, req->len)`), and on match: zero `ent->len`, unlink, `off = ent - base`,
   `bl invalidate_entries_by_id(((off/1024)<<12) | (off%1024))` (verbatim from
   `lookup_name_entry...:1745`), push node on the free list at `lbl_805D7878`.
5. Pop a node, grow via `sub_803E95BC` if the free list is empty, `tag = (req->x8||req->x7>=0x2D)?3:2`,
   `size = req->len + tag + calc_sjis_string_width(req->text) + 3`, bounds-grow check against
   `lbl_805D786C`/`lbl_805D7870`, write the record at the pool cursor (terminator pair written at the
   NEW cursor, read from the global twice = no local), `strncpy`, trailer bytes
   (`x7`, `arg2`, optional `x8`), `copy_sjis_string(req->text, p)`.
6. Bucket walk 2 (verbatim structural copy of walk 1, registers rotated) → insert the new node.
   Single `return 0`; one epilogue; `lmw r23,68(r1)`; frame 0x68.

## Result

**76.608246 unlinked, 748 B vs gate 776 B (−7 insns), 187/194 rows differing.**

## Sibling safety (vs TRUE base origin/master 1e5823fa, regenerated both sides)

`REGRESSED/CHANGED: [.mwcats.text 1216→1224]` only. 157 OURS symbols at 100.0 before and after.
The `@851/@964/@1835 → @928/@1041/@1912` delta is anonymous-pool renumbering (address-resolved in
report.json, display-only per SKILL § jumptable/pool rows). No matched function moved.

## CENSUS — 9 distinct spellings, all measured on the unit's own GC/1.2.5 `-O4,p` profile

| # | spelling delta | score | size |
|---|---|---|---|
| 1 | v1: single `s16 len` local, `const-first` addr `(u8*)&lbl + 0x2000 + (h<<2)` | 73.366 | 752 |
| 2 | **CHAMP**: `u8 *base` local, per-site `req->len`, `base + (h<<2) + 0x2000`, `[0x800]` index form for slot | **76.608** | 748 |
| 3 | #2 + per-walk `s16 len` local (assigned before each walk) | 74.253 | 768 |
| 4 | #3 + `#pragma opt_common_subs off` window | 73.247 | 768 |
| 5 | #4 + decl reorder (h,len,prev,blen,n,base first) | 73.428 | 768 |
| 6 | #4 + `len = req->len` before `h = Hash(name)` | 71.825 | 768 |
| 7 | #4 + both #5 and #6 | 72.031 | 768 |
| 8 | #4 − pragma (base-last, pad 0x20) | 74.505 | 752 |
| 9 | #8 + decl+stmt reorder | 73.577 | 752 |

## Wall diagnosis — ADDRESS-CSE POLICY PIN (QVM-family, sibling of DEF-CLAMP REMAT / DEF-BINDING PROLOGUE PIN)

Era bank = 9 callee saves: r23=h, r24=len, r25=prev, r26=name, r27=req, r28=arg2, r29=blen, r30=n,
r31=`&lbl_80591EC8`. Era keeps the **global address** in r31 and **re-materializes** the bucket
address at all four sites (`slwi r0,r23,2 ; add r3,r31,r0 ; lwz r30,0x2000(r3)` for the loads,
`add ; addi r,r,0x2000` for the slot forms).

Champ bank = 8 saves: it CSE-keeps the derived slot address (r29) instead of `h`, so `h` never gets
a home and two remat trios vanish → −7 insns, gate miss.

The dichotomy is emitter policy, not spelling:
* CSE on (any decl order, any def order, const-first vs const-last, `&arr[0x800]` vs `+0x2000`):
  the derived address is always shared, `h` is always transient, size lands 748–752.
* CSE off (`opt_common_subs off`): `h` and `base` both home (9 saves, 768 B — closest to gate) but
  the bucket load de-CSEs into `addi r0,r?,0x2000 ; lwzx rD,r31,r0` instead of era's
  `add r3,r31,r0 ; lwz rD,0x2000(r3)`, and the `@ha` pair re-materializes — net −2.4 rows.
* No installed spelling yields {9 saves} ∧ {`add`+`lwz disp`} simultaneously.
* Secondary rows of the same family: era binds arg2 as `addi r28,r5,0x0` where every spelling gives
  `mr r28,r5` (COLOR-SELECT-PIN sibling), and the 4-cycle home permutation
  {h,prev,blen,n} ↔ era {h,prev,blen,n} did not move under the decl/def grid.

Census law satisfied (9 ≥ 5). PARKED at 76.608 — no second visit unless an
address-remat-vs-CSE mechanism is found.

## LEAD FOR NEXT VISIT (the one axis NOT gridable by hand)

A permuter round seeded on the CHAMP body (gate = 776 B, rank = callee-bank vector
[23..31] with h∈bank) is the only untried axis: the target state needs `h` promoted into a
callee-saved home while the address stays unshared, which is a birth-rank/liveness question the
hand grid (decl × def × pragma) provably cannot express. Sizes say the era state is reachable
(768 with CSE off), so this is a permutation problem, not an impossible-shape fold wall.
Perm slot was NOT used this visit: call budget fell below the 25-call entry requirement.
