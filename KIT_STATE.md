# KIT_STATE — card-fd88-vt4 (t_9e53b40d) vt4__20TWindowSubStatusDispFv (0x8027FF6C, gate 0x544, 337 insns)

Visit-1, base 5695627b, tree f7. TIP 19edffd3: **98.78339 gate-exact (337/337 rows)**, unit code 100% (141/141 fns, 51356/51356B). NOT 100% row-exact => no unit completion claim this visit; linked stays 3308.

## Anatomy (validated, all 5 classes)
- Frame 0x30, bank stmw r26 (6 callee saves r26..r31), lr 0x34. r31=arg0, r30=mode, r26-r29 rotating entry/v homes.
- Guard twin: `(f32) *(s32*)(arg0+0x5C) > TWindowSubStatusDisp__data_805DD708` == vt7/vt1/vt2/vt3 byte-shape (proven).
- init_window_layout_entries(arg0+0x24, TWindowSubStatusDisp__rank_time_records_layout, *(s16*)(arg0+0x20)) == vt7 twin shape.
- Dead call: get_type__20TWindowSubStatusDispFv(*(s32*)(arg0+0x68)) — result NOT consumed (r3 overwritten; era discards).
- 5 row blocks, 3 entries each (1..15), + e0 label block (0x90/0x93 ternary tail-dup).
  - A(1,2,3): win=get_status_window((u16)slot); guard chain mode!=0||win==0||*(s8*)win==0 -> |=2x3; else &~2x3, msg 0x9B, set_text(e3,(u32)win,0x20), stw get_status_index((u16)slot) @ e3+0x24.
  - B(4,5,6): v=TWindowSubStatusDisp__sub_80071868((u16)slot,mode); v==0 |=2x3; else &~2x3; mode?0x9A:0x98 tail-dup set_text(e1); set_text(e3,lbl_804D2B20[v],0).
  - C(7,8,9): v=sub_80071988(...); 0x95/0x97; then text_builder_reset(); append_play_time(v); set_text(e3,get_shared_text_buffer(),0x20).
  - mode2 = 1; if((s16)0x60==2) mode2=3 (direct home write, NO scratch).
  - D(A,B,C=10,11,12): sub_80071868(...,mode2); msg 0x99 CONST (no mode test); table text.
  - E(13,14,15): sub_80071988(...,mode2); msg 0x96 CONST; play_time tail.
- mode1 = 0; if((s16)0x60==2) t=2; mode=t — ternary `?:` form emits 8-insn arithmetic (subi/subic/subfe/and) = +2W. STATEMENT form = branch 5W; scratch+copy = 6W = era.

## Winning levers (committed)
1. mode statement-form (not ternary): 96.09 -> 98.47, kills arith chain.
2. `#pragma push / opt_propagation off / <fn> / pop` FUNCTION WINDOW (RELBASE law: statement windows byte-ignored — use function window): keeps `mode = t` copy (mr r30,r26) = GATE 0x544, 98.47->98.78, zero sibling effect (all 17 gnm gate-stable).

## Residual (84 rows) — visit-2 frontier
- slots 9/10: TWindowSubStatusDisp__data_8044FB00 @53@ha — link-gated pool-name display class, NOT source-beatable (report: paired at same %; resolves only at link/claim).
- 82 rows: PURE SWAP RING in homes {r26,r27,r28,r29} (+mode2 r30-yes/r29-ours). Multiset-identical, all mnemonics+immediates equal, only reg numbers rotate. Era home map per block: A(e1=29,e2=27,e3=28,win=26,t=27-vacated) B(26,28,29,v=27) C(26,27,29,v=28) D(26,27,29,v=28,mode2=30) E(27,28,29,v=26).
- INERT probes (banked): decl-order swap x2 (win-first, t-before-mode) = byte-identical ring. Allocation binds at DEF points, decl INERT (RX-pump law confirmed).
- Open idea for visit-2 (pressure-rank bisect admissible, pure swap ring): inject live-pressure at t-def site to push t r26->r27: e.g. bind e0(get_array_entry(0)) def BEFORE t (hoist get_array_entry(0) above mode computation), then test on mode; era e0->r26 + t->r27. Ring cascade may fix blocks B-E homes too. DO NOT re-roll: closed classes COPY-BIRTH-TOP-PIN, self-accum fmuls(WSSD), MIRROR-BASIN, def-binding prologue pins (edc20/ba38) — this ring is def-binding kin; if e0-hoist probe inert => census floor 98.78 (beats WSSD 98.2 precedent), recommend no 2nd visit absent new mechanism.

## Cold-start commands
```
cd /Users/scott/Hermes/pso-decomp/pso-decomp-f7 && git branch --show-current  # card-fd88-vt4
rm -f build/GPOE8P/src/pso/unk/text_8027FD88.o && ninja -C . build/GPOE8P/src/pso/unk/text_8027FD88.o
/opt/homebrew/opt/binutils/bin/gnm -S build/GPOE8P/src/pso/unk/text_8027FD88.o | grep ' vt4'   # gate 0x544
PY=/Users/scott/.hermes/installs/60d8a79da6991a71/environments/28d86d1068e44adc8d1a5d2ca8c63c2c/venv/bin/python3.14
$PY ~/.hermes/profiles/pso-decomp/skills/pso-decomp/scripts/one_shot_diff.py psov3/pso/unk/text_8027FD88 vt4
```
Era block: build/GPOE8P/asm/pso/unk/text_8027FD88.s lines 166-524. ps-arith screen: 0 hits (f64 guard only, twin-matched).
