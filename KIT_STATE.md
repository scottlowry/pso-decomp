# KIT_STATE — TLobby__sub_803C0238 (unit psov3/pso/unk/TLobby_803BFE50, door w59 card-door-bfe50-v1)

## Status: SEALED CEILING — max-meter landed 1dbaab39, visit-3 receipt closed
Seat: TLobby__sub_803C0238 @ .text+0x3e8, gate 0x3F0 (era 1008B, 252 insns, era .fn 0x803C0238..0x803C0624 RE-DERIVED v7).
Unit: 35/36 byte-exact + seat PAIRED 98.4127 GATE-EXACT. Data 100.0. Unit UNLINKED (linked_units absent; seat <100 no candidate row; DOL 0d85744b51d7379efb025a943d0cd5aaae2191a3 expected-const, verified pre/post).
Pin (live build.ninja:55188-55197): GC/2.6 -char signed -use_lmw_stmw on -O4,p -inline off -lang=c++ -enum int -fp hardware -nodefaults.

## Max-meter lineage (all gate-verified, NEVER re-roll)
v1 e03d92fe 96.90476 (+3W) -> v2 af5dc0f5 GATE-EXACT 97.61508 -> v7 42556ea4 98.4127 (P@4 interleave FUSE) -> v8 525b57c1 census-park.
Visit-3 (this lane, 1dbaab39 @ 00cda35c): blob-identity transplant of edfad9c6 (HEAD==v7-parent 1d4e1d2b, zero drift); sealed echo ZERO decay 98.4127 252/252 rows; 36/36 T-syms drift 0 vs era .o; battery green (ninja rc=0 141/141 + Data 100, report_delta 0/0, check_pr PASS 2871).

## Residual census (visit-3, cache/scratch/w59_3c0238_rows.txt)
78/78 rows = register renames ONLY (skeleton-identical; 0 semantic rows).
Class = def-binding allocation RANK stratum: era homes {r31 self@rank1, r27, r29} vs GC/2.6 {r27, r31, r28}; 71 rows pure {r31<->r27, r29<->r28} shift + 7 rows wider {r31,r29}<->{r27,r31} bind-rank shift at home materialize sites.
Def ORDER identical both sides (self@4 lb@5 h@11 st@13 avail@75) — v8 datum.

## Sealed classes (census-5+ done; re-roll banned)
1. bind-to-home RANK stratum: v8 525b57c1 INERT x3 (cast-purity B2, decl-init def-site B3, u32->s32 lineage B4) — .o seat invulnerable to decl-order/def-position/cast/type. 20-version rosetta (receipts 6328/EB4D4/3c0238/80184df4): era ring emitted by ZERO versions.
2. HOME-INSERTION / clobber-hoist / RA-spill: lane law sealed list.
3. Sibling datum d1f7c873 (dhcp v3, GC/2.6-adjacent 1.2.5n terrain): rank class LIVE-NEGATIVE — all 3 directions convicted (def-late=rank-down). Do NOT probe def-position.
=> era self=rank1 not expressible at fused shape GC/2.6. Seat = ask #16 family (era-alloc/toolchain strata, INTEGRATOR).

## Kit eligibility
252 insns < 400i kit lifecycle bar (TWindowDD 3cdeb200 precedent) = NOT kit-eligible. No permuter round: residual = pure color RANK (byte-pure screen trivially positive but liveness-bound by construction: homes are allocation-rank, mutators cannot free liveness-bound homes at pinned gate size).

## Cold-start commands (verbatim)
cd /Users/scott/Hermes/pso-decomp/pso-decomp-f7
git show 42556ea4:src/pso/unk/TLobby_803BFE50.cpp > src/pso/unk/TLobby_803BFE50.cpp
rm -f build/GPOE8P/src/pso/unk/TLobby_803BFE50.o && ninja build/GPOE8P/src/pso/unk/TLobby_803BFE50.o
xcrun llvm-nm -S build/GPOE8P/src/pso/unk/TLobby_803BFE50.o | grep C0238   # expect 000003e8 000003f0 T
python3 /Users/scott/.hermes/profiles/pso-decomp/skills/pso-decomp/scripts/one_shot_diff.py psov3/pso/unk/TLobby_803BFE50 sub_803C0238  # expect PAIRED 98.4127 252/252
Receipt: tools/perm-tests/f7_3c0238_v9/RECEIPT.md
