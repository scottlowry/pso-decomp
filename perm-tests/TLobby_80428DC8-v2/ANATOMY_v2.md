# TLobby__sub_80428DC8 — anatomy v2 (visit-3, fleet/f3, Oct 31)

## Ladder
- 6a8ad96c: v44 fold basin — official 99.67742, 4 residual loop-rotation words (39/40/44/45).
- 6b81d42a (this visit): **m4 basin — official 99.83871 (+0.161)**, size 0xF8 gnm exact,
  whole unit re-scored: 24 siblings 100.0, no regressions.
  Body: `entry = entry * 10; entry += ch; entry -= '0';` (inside `while ((ch = text[i]) != 0)`).

## Residual = ONE word: slot 40 `add r7,r7,r0` vs orig `add r7,r0,r7`
CLASS: regcanon coalescing-tiebreak (same family as camera-card "dest≡A invariant",
permuter.md § 2nd-visit; MWCC canonicalizes in-place compound assign `entry += ch`
to dest-first operand order `add rD,rD,rS`).

### 2-row anatomy correction (visit-2 doctrine said "2 rename rows")
The 2 weighted units at 6a8ad96c were NOT the `...bss.0` rename rows:
- rename rows (slots 12/16 `lobby_net_session_state@ha` vs `...bss.0@ha`) weigh ZERO —
  proved by sibling TLobby__sub_80428BB0 rendering identically at match=100.0.
- branch-target rows (19/34/38/46) weigh zero (offset-normalized pairing).
- the 4 register-role rows 39/40/44/45 carry 0.5 each = 2.0 units. The fold fixed the
  pool PHASE (n=r6, i=r3, acc=r7, subi in-place) leaving only register HOMES:
  ch wanted r0 (orig) but got r4; muli temp wanted "none" (in-place r7) but got r0.

### State enumeration (home-states of the loop pool, from battery fingerprints)
- S0 = v44 fold state: n6/i3/acc7/ch4/mulli→r0. (rS3v44 kit; also w04 same codegen)
- S1 = v41 lassoc: ch=r0 achieved but i=r4, body-order rotated (bad [36,40,41,42,43]).
- S2 = v10 basin: acc=r6 rotation (10 bad).
- S3 = w04: parenthesized fold — S0 codegen, distinct source topology.
- S4 = **m4 basin (NEW, this visit's winner)**: n6/i3/acc7 in-place/ch=r0 — ALL homes
  match orig; lone flip = add operand order (S0→S4 lever: compound-assign tokens
  `entry += ch`/`entry -= '0'` instead of fold-expression).

## What was run (with proof)
- Hand order-grid (offline compiles, zero repo builds):
  r2: fold topologies × pre-orders (90) → best = S4 basin, nbad=1.
  r3: add-token flips × pres × decls (108) → q1/ch-first ALWAYS flips basin to S-old(-v00) 11-bad.
  r4: q1 body × ALL 120 decl orders × 6 pre orders (720) → every one 11-bad. Dead.
  r5: m4 basin × cond-spelling(3) × i-token(2) × pre(6) × decl(4) (156) → frozen nbad=1.
  r6: pragma bisection opt_lifetimes/common_subs/dead_assignments/propagation/peep/
      strict_imaged ×on/off + pairs (14) → frozen nbad=1.
  ≈1,100 spellings; `add rD,rD,rS` dest-first invariant CONFIRMED in-basin;
  ch-first source token flips the whole pool (out-of-basin) under every context knob.
- Permuter waves (iters>0 + mtime proof per state, waves_f3.log):
  W1 rS4m4   27,606 iters PROOF=YES harvests 0   (m4 champ basin)
     rS3v44  27,652 iters PROOF=YES harvests 0   (v44 fold basin)
  W2 rS3w04  28,485 iters PROOF=YES harvests 0   (paren-fold topology)
     rS1v41  28,525 iters PROOF=YES harvests 3 → raw 98.95161/98.79032/98.46774, ALL < champ
  W3 rS2v10   8,523 iters PROOF=YES harvests 1 → raw 98.79032 < champ
     rS4m4_stack 3,288 iters PROOF=YES harvests 0 (--stack-diffs objective, brief item 2)
  WB rS5mc (compound=15/split=10 deviant profile — only mechanical bridge to q1 tokens)
     + rS4m4b second plain seed: (running ~19:27→~19:42)
- Compiler-version diagnostic probe (kit-local, read-only; promotion NOT in lane scope —
  config/ frozen): m4 + v44 spellings under GC/1.3.2, 2.6, 2.0, 1.3.2r. (running)

## Verdict (FINAL, visit-3)
HOLD at 6b81d42a (99.83871, +0.161 banked; supersedes prior HOLD target 6a8ad96c).
All 6 rotation-states + stack-diffs + compound-profile wave executed with iters>0 +
mtime proof (~122k iterations, 4 harvests total, ALL below champ).
Grid exhausted (~1,260 spellings): slot-40 `add r7,r7,r0` vs `add r7,r0,r7` is a
REGCANON COALESCING-TIEBREAK row (same class as camera-card dest≡A invariant,
mwcc-notes § 2nd-visit): MWCC 1.2.5n emits in-place compound-assign add dest-first
under every source token, decl order, pre-order, loop-condition spelling, i-token,
and pragma state/position tested; the ch-first source spelling that would emit
(r0,r7) flips the whole pool out of the matching basin (720-decl sweep, invariant).
RECOMMEND: RETIRE after 2nd visit. Ceiling from source at the pinned GC/1.2.5n is
99.83871. Unexplored classes named honestly:
  (1) per-unit compiler-pin — diagnostic only (1.3.2/2.0/2.6/1.3.2r all emit 66
      rows vs 62 = structural penalty before the add row even matters; full 19-version
      sweep not done; config/ is Scott-only territory — LOW expectation);
  (2) unit flag changes via configure.py — out of lane scope entirely.
NOT a UB case: m4 raise is pure arithmetic, NO-UB rule untouched.

## Infra notes (PATH truth verified this visit)
- gnm = /opt/homebrew/opt/binutils/bin/gnm (binutils nm symlink); repo build/binutils
  has powerpc-eabi-* only. run_round.sh now: GNM absolute + homebrew PATH export +
  preflight + per-round PROOF (mtime/iters/harvest delta).
- zsh no-match glob `rm -rf dir/output-*` on a FRESH dir aborts the WHOLE inline
  chain before the permuter line — waves must use find -maxdepth 1 -exec rm -form
  inside #!/bin/bash scripts. Two wave launches died this way before diagnosis
  (iters=0 from them; voided, re-run with proof, waves_f3.log PROOF lines are the
  authority).
