# TLobby__sub_803CC578 — card-lobby-cc578 park (Nov-3 night)

## Row truth
- symbols.txt:26354 `TLobby__sub_803CC578 = .text:0x803CC578; type:function size:0x30C` (780B, brief ballpark verified)
- Unit pso/unk/text_803CC294 (.text 0x803CC294-0x803CD804). Base: 12/14 fns at 100.0; CC578 + CCB98 unlinked.
- Supersede-check: no prior attempt (only adjacency mention in f7 61fc checkpoint doc).

## Function identity (decode)
ADXF_Seek — era strings at .rodata anchor lbl_8047C818:
- +0x174 = "E9040825:'adxf' is NULL.(ADXF_Seek)"
- +0x198 = "E9040822:'adxf' is NULL.(ADXF_Stop)"   (reused Stop string — copy-paste body!)
- +0x1bc = "E9040823:'adxf->stm' is NULL.(ADXF_Stop)"
- +0x1e8 = "E9040826:'type' is illigal.(ADXF_Seek)"
Sole caller: open__8TGStreamFPvPvi @0x800FE224 (bl, return ignored). No vtable ref anywhere in era asm corpus.
Structure: log(type6,phase0,seq@hdr+0xC incremented) -> null->return -3 -> if(s8 f1==2){ log5/0 seq@+0xA++,
dead re-tests (!null notify; state==1; state==3->set1; f4==0 notify) else full adxf_stop body (init_once,
sub_803C89C4/85AC, f20=sp8, f8 vtable slot3 (lwz 0xc off *f8) + f8=0 under f2==0 & lbl_805D75E4==1, state=1,
release_ref, log5/1) } -> type if/else-chain (0:set f14, 1:+=, 2:=f12+, default notify+return -3) ->
clamp if(f14<0)f14=0 else if(f14>f12)f14=f12 -> log6/1 -> return f14. NO jumptable (3-case if-chain era too).
Object = adxf file-handle entry: f1 state(s8, gate cmpwi SIGNED, extsb elided by era single-cmp peephole),
f12 size, f14 pos (f12@0xC, pad@0x10, f14@0x14, f20@0x20, f24/f28 cache region).

## State achieved
- 3-iteration draft (twin-transcribe of matched sibling adxf_stop + `s32 base=(s32)lbl_8047C818;` anchor
  spelling from read_afs_toc — pool anchor+plain-disp `addi r3,r30,0x174` reproduced at gate).
- Gate-exact: size 780/780, rows 195/195, paired match 95.30769.
- ALL displacement/branch/string/sda21 rows CLEAN. Residual = 30 rows, ALL register colors in the two
  phase-0 log blocks (slots 2-63):
  * Era head binds pool FIRST half in prologue (lis r9 pool@ha slot5 + addi r30 slot11) and defers
    table pair-completion (addi r8, r7, tbl@l @slot19); ours mirrors exactly INVERTED (table pair
    completes @5, pool pair lands @19/23).
  * Era homes i-derived slot ptr in r6/r10 tempo, ours in r10/r9/r7; phase-const li r7,0 @21 vs our
    li r6,0 @9; block2 add r6 vs r8, add r8 (tbl base+) vs r7.
  * Instruction MULTISET is identical per block (pure color ring) => COLOR-SELECT-PIN / def-binding
    birth-rank class (regcanon-walls family).
- Inert: head decl-order flip (base/sp8 swap + seq/i decl swap) — byte-identical diff set v2 vs v3.

## Next-visit levers (not attempted, per time-law)
- Permuter on the 195-insn body, rank targets: {r6/r7 @ha swap at head; pool pair early (5+11);
  table@l late (19); slot-ptr r10-tempo; li0 at 21; block2 r6/r8 ring}. Two linked sub-blocks move
  together (195-row alignment constraint) — treat head 2-33 and 49-63 as one splice unit.
- Check sibling `close_803CCE9C`/`sub_803CC884` era heads for a source shape that binds the pool EARLY
  (adxf_stop has no anchor local; read_afs_toc binds base late like ours) — era-early-anchor spelling
  may need base's FIRST use positioned before the first log block (e.g. pass `(const char*)(base+...)`
  somewhere early, or declare `const char *`-typed view used by error paths).
- rosetta decl-qualification: not reached (no pool-section wall; refs are .bss/.data globals + anchor).

## Naming proposal (config rename = integrator)
`adxf_seek__6TLobbyFii` — evidence: era debug strings name ADXF_Seek directly; args ('adxf','offset','type'),
returns clamped new position s32. Keep symbol TLobby__sub_803CC578 until config claim lands.

## Files
- src/pso/unk/text_803CC294.cpp: +Adxf_803CC578/+LogHdr_803CC578 structs, extern-C proto, body between
  sub_803CC53C and sub_803CC884 (address order preserved).
