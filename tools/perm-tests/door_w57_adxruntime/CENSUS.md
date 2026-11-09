# door w57 — AdxStreamRuntime census (branch card-door-adxruntime-v1, tip after rung3)

Unit: psov3/pso/audio/AdxStreamRuntime. Base 00cda35c (#228 tip), DOL sha1
0d85744b51d7379efb025a943d0cd5aaae2191a3 (byte-identical at leaf — unit UNLINKED,
linked_units 0 hits; inertness = .o gate shas + report_delta +0/0).

Pin (live-cited build.ninja:55340): GC/2.6, -O4,p -inline off -lang=c++ -proc gekko
-char signed -use_lmw_stmw on.

## Seats (rungs committed)
1. TLobby__sub_803CA8B4 b1a4aa14 — park champion c503dc959 transplanted (diff
   7008688d3..c503dc95, path-remap system->audio, 2 hunks, offset -606).
   Gate 0x284 EXACT (nm -S int-parse). Echo ORIG=OURS 99.25466, 161/161 rows,
   644/644 — zero decay vs park. Residual 19 rows = two-loop def-binding color
   rings: zero-emitter (20-version rosetta, park census-5) = sealed def-ring,
   landed AS-IS, NO grind authority.
2. TLobby__sub_803CB858:
   - rung2 a0b89b1a — seed = relbase park v6 body + 8 extern decls + co-def move
     (b4f1fdd1^..9c77e5ce, 3 hunks). Gate 0x1CC (+3W), report row 92.97 = park
     92.97321 zero-decay. ProbeK transfer VALIDATED at repo terrain.
   - rung3 97beb657 — LEVER: drop `u8 *pool` local, spell &adxm_{worker,vblank,
     busy_wait}_thread handles inline (5 sites). GATE 0x1C0 EXACT (era 112w).
     one_shot ORIG=OURS 98.69643, 112/112 rows; report pairing 99.32.
     pool-dup trio dissolved: r31 anchor serves pool directly, param banks r30.

## b858 residual census (12 true rows + 2 pool-name rows) at rung3 = champion
Residual rows (slot: ORIG vs OURS):
- slots 2/6: `lis/addi ..., adxm_worker_thread@ha/@l` vs `...bss.0@ha/@l`
  = pool-name display class — ACCEPTED law, no action.
- slots 36-46 (10 rows): arg0-copy block — era load-pair low-first
  (lwz r3,0x0; lis r4; lwz r0,0x4; stwu r3; stw r0) vs OURS high-word-first
  (lwz r4,0x4; lis r3; lwz r0,0x0; stwu r0; stw r4); cfg base r4(era)/r3(ours).
- slots 84/85: era li r4,1; li r0,0 vs OURS li r0,0; li r4,1 (materialization swap).

Probe harness (scratch, exact pin `wibo build/compilers/GC/2.6/mwcceppc.exe`,
INERT-screen = .text function-bytes sha vs control; repo builds NOT consumed):
- v1 direct-5 stores (no temps): MOVED, gate 0x1C0; repo build = 95.42857 REGRESSION (-3.27) -> revert
- v3 3-temp rotation (load [2] hoist): MOVED, gate 0x1C0; repo build = 96.99107 REGRESSION (-1.71) -> revert
- v4 load5/store5: gate-BREAK 0x1C4 (+1W) — screened out, no repo build
- v5 li-pair explicit one/zero temps: INERT (byte-identical) — datum: li pair not spellable via temps
- v6 ptr-walk p=arg0: INERT
VERDICT: load-pair order + base-reg color + li-pair order = scheduler-pinned at
GC/2.6 -O4,p (def-order load swap unrepresentable across probed graph permutations;
cf. c8020 P1/P2 scheduler-pinned closers). Champion = rung3 97beb657.

## Battery (leaf)
full ninja rc=0; report_delta cache/base_report_w57.json --check: regressions 0,
new-exact 0, functions 27572 unchanged; check_pr.py PASS (linked 2871, AdxStreamRuntime
unlinked NOT candidate); DOL sha byte-identical vs base. Unit: fns 84/86 @100.0,
code 92.35722 -> 99.94513, data 100.0. Unit-completeness: NOT pair-complete (two
seats <100.0 paired, both gate-exact, both sealed/pinned residuals) — match wave,
not PR material per door law; next-visit = zero-emitter rosetta for load-pair family
if ever banked.

## Harness pitfall banked
MWCC ELF32 .o: e_shentsize@0x2e (=40), e_shnum@0x30, e_shstrndx@0x32; Xcode
llvm-objdump has NO ppc target (byte-compare via python ELF parse instead).
