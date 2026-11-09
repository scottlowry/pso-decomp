# Campaign: test_box_sphere_contact (TObjPlayer_803DF7A8 seat 0x803E112C) — v2 PARK receipt (visit-3)

- Lane: branch `card-boxsphere-v2`, tree `pso-decomp-f3`, base master `00cda35c`. v1 park (fe591833, 97.32684) seeded VERBATIM as rung0 `c15856fd` (blob-identity 31f61f39 ✓).
- **Tip state: PARK at official 97.39178 / one_shot 97.25108, 122/462 rows, gate 0x738 exact, size 1848.** Unit UNLINKED (DOL expected-constant `0d85744b51d7379efb025a943d0cd5aaae2191a3` ✓ full ninja rc=0).
- PIN (verified via kit proxy, GC/2.6 -O3,p -inline off -opt nopeephole -use_lmw_stmw on -fp hardware -char signed -lang=c++).

## v2 ladder (this visit)
| rung | knob | official | one-shot | rows | verdict |
|---|---|---|---|---|---|
| r0 seed | v1 park tip verbatim | 97.32684 | 97.18615 | 124 | gate-exact, DOL const ✓ |
| r8 | permuter **round 3** harvest output-1215-1 (base score 1235 chain-law ✓, 9151 iters, 19 harvests, 5 clean) — operand-swap `(dz²)+((dy²)+(dx²))`→`((dx²)+(dy²))` | 97.37013 | 97.22944 | 122 | LANDED 8994598f; gate 0x738, siblings 37 sym 0 drift, regressions 0, check_pr PASS |
| r9 | permuter **round 4** re-rooted on r8 (BASE-VERIFY byte-ident, base score 1215 chain-law ✓, ~9.4k iters, 16 harvests, 3 clean) output-1205-1 (4-line restructure) | **97.39178** | **97.25108** | 122 | LANDED c6806347; full battery green |

Kit budget consumed: 2/2 rounds (rounds 3+4), both promoted via --better-only. No hand rungs needed. No zero-harvest round fired => saturation NOT tested; kit stays ARMED.

## Residual at r9 (122 rows)
- ~77 fp color-ring (def-binding home ring SEALED — era prologue-binds 0.025f@f4/0.0f@f5 function-live; v1 root cause, perm-invariant, never re-roll).
- 13 pool-name display (`lbl_805E10xx@sda21` vs `@NN@sda21`) — ACCEPTED class (twin-proven).
- ~25 pure-GPR renumber (era 7-slot window r25–r31; source-order-opaque at pin; broken only by permuter re-homing).
- ~7 rotation/operand-swap (kit territory — r8/r9 consumed 2 of ~8; remaining ones tied to sealed fp-ring slots).
- Ceiling: stratum projection ~97.5-98 CONFIRMED REACHED on official pairing (97.39 → next sub-100 headroom is fp-ring dominated; per-row +0.0021/row official: ring-only gains require the def-binding class — source-lever-inert). Sub-100 official = ledger inventory, NOT PR material (100.0-paired gate-exact rule).

## Sealed datums added this visit
- **Permuter-score inversion datum**: lowest permuter scores do NOT harvest clean. Round 3 best 1185 (x4 ties) + round 4 best 1165 (x4 ties) ALL died at size/newsym gates; every landed winner ranked by objdiff-clean (97.22944 = perm score 1215; 97.25108 = 1205). Rank harvests by bs_rank.py objdiff, never by permuter score order.
- **BASE-VERIFY law refinement (multi-function unit)**: proxy .o sha == unit .o sha is IMPOSSIBLE (proxy compiles seat-only, unit .o 16880 B vs proxy 3520 B; whole-file shas will always differ). Canonical test = sha1 of the seat .text 1848-byte window: proxy `dd bs=1 skip=52 count=1848` (file offset 0x34 + vaddr 0) vs official `skip=0x34+0x1984 count=1848`. v2: r8-root d684a31a ✓, r3-base 03ce6ae6 ✓ both byte-ident.
- Kit reroot drift: 23:46 f4 base.c had fx-before-fy statement order (f4 worktree drift, semantically inert); repo blob = fy-first. reroot_base.py from the AUTHORITATIVE tree is the base.c source of truth, not the kit file.
- Full ninja runs from REPO ROOT (build.ninja at root; `ninja -C build/GPOE8P` fails).
- BSD mktemp poison guard: compile.sh uses `$$.$RANDOM` suffix + wibo .cpp extension — proven again this visit (0 cfail across 2 rounds).

## Kit state after visit-3
- Kit `/Users/scott/Hermes/tools/perm-tests/TObjPlayer_803DF7A8_test_box_sphere_contact` retargeted REPO=f3 (compile.sh, bs_rank.py, bs_splice.py, reroot_base.py); bs_rank.py takes harvest-suffix arg.
- base.c = r8 body (re-rooted at round-4 prep); round-4 winner r9 is NOT yet re-rooted. VISIT-4 STARTER: `python3 reroot_base.py` (f3), BASE-VERIFY window-sha, PURGE (`rm -f base_direct.o /tmp/bs_asm.*`, archive r4 output-* dirs), harvest rank `python3 bs_rank.py 5`, round cap 935s `bs_round5.sh`.
- Archives: archive-r12/ (556 dirs), archive-r3/ (19). run3.log/run4.log/rank3.out/rank4.out/harvest3.json/harvest4.json kept.

## Files
- lane f3: `src/pso/player/TObjPlayer_803DF7A8.cpp` (r9 tip), `KIT_STATE.md` (this), `cache/base_report_w65.json` (rung0 base snapshot), scratch `bs_v2_r0_oneshot.txt`, `bs_v2_r0_nm.txt`, `bs_v2_r9_oneshot.txt`; ninja logs /tmp/w65_*.log.
- battery at tip: full ninja rc=0; report_delta cache/base_report_w65.json → report.json: "New exact functions: 0; regressions: 0; source_bearing_units 2965->2965 (+0); linked_units 2871->2871 (+0)"; check_pr PASS; DOL const.
