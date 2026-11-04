# f8 prepare_tool_purchase__19TShopItemListWindowFv — ring census (2026-11-03)

Card t_7e2a71fa. Branch card-shop-purchase, committed tip 87341c04.
Gate: 0x1C4 (452B, symbols.txt row) — HIT, byte-count exact, 113/113 insns.
Committed-tip match (clean rebuild, report.json linked): 91.23894.
Unlinked one_shot: identical 91.23894 -> zero pool-name noise; residual = pure binding/color.

## ps-arith screen
ps_(mul|add|sub|div|madd|sum) count in era .fn block = 0. (psq_st/psq_l pair in
prologue/epilogue are float stores; f32 spill via stfd+psq_st double-slot form.)

## Twin screen
No same-size 100%-paired sibling (452 unique; closest 460/584).
Structural twin USED: build_item_list 100%-matched new/ctor/nullcheck/camera/set_position
idiom (transcribed statement-for-statement; right-to-left arg eval reproduces
get_child_field1c-before-get_window_layout_position order + extsh/clrlwi materialization).

## Era callee disambiguation (transfer: dual-name callees)
era file calls BOTH set_position__18TCheckRoomSequenceFff (0x80211614, prepare) AND
set_position__6TLobbyFff (0x8021B268, handle_amount_confirm). TLobby.h declares
set_position ONLY on TLobby; the TCheckRoomSequence spelling lives in
include/pso/misc/TCheckRoomSequence.h (precedent TShopDeleteItemWindow.cpp:230).
Casting via TLobby in prepare mangles to __6TLobby = wrong callee. Screen symbols
by ADDRESS per call site, not by name.

## Residual classes (all rows keyed by ONE binding rotation + two chain splits)
era  homes: self=r31, off=r29(+obj chain), maxQty=r30(+ent/child1c chain), count=r28
ours homes: self=r30, off=r29(+count chain), maxQty=r31(+ent/child1c), obj=r28
Head: era binds self (mr r31,r3) BEFORE the self->list load (load dest r3, test r3,
bl feeds r3 directly, cursor materialized mr r0,r3 then mulli); MWCC GC/2.6 emits
load-into-scratch r0 first, binds self after (DEF-BINDING PROLOGUE PIN kin, qvm-edc20
fingerprint). use1/use2 address arithmetic: era = addi(off,0x58)+add(self) /
add(self,off)+lwz 0x68 (two distinct assoc forms); MWCC canonicalizes both
(add+addi / addi+lwzx indexed).

## Inert levers (census; byte-identical or hunk-identical)
- function-window #pragma opt_propagation off: byte-identical .o
- named temps cursor/recOff/pi (force two-stage address + cursor materialization): inert
- decl-order grid: (self,maxQty) swap inert; obj declared 1st rotates self->r29/obj->r30
  (rotation confirmed reachable; era k-rotation NOT reachable)

## Verdict
floor 91.23894 at gate-exact size. Era allocator bind-stratum (self-edge vs self-center
packing + chain-reuse tiebreak at divw bind). No convicted era compiler-version wall:
all era head shapes here ARE emitted by installed MWCC for the 4 sibling 100% fns.
Suggested next-visit levers: none in spelling space; if a bind mechanism is found for
self-edge-packing (era widest-liveness -> bank edge), this row unlocks in one step.
