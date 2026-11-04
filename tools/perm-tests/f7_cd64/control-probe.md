# f7-2 control probe — tip ba1d9730 (Nov-3, m5u)

Clean rebuild: rm build/GPOE8P/src/pso/network/ModemRuntime.o; ninja rc=0
(MWCC line printed). one_shot psov3/pso/network/ModemRuntime sub_8042CD64:

  ORIG size=404  OURS size=420  match=78.92079  rows 101/105 (+4 insn)

Confirms inherited brief state (78.92079, +4).

## Diff anatomy vs era
1. HEAD ORDER: era emits `lis r4,0x2300` (slot1) and
   `lis r3,modem_command_response_state@ha` (slot3) around/before
   `stw r0,4(r1)`; ours sinks both below the handshake loop
   (our slots 34-37: lis/addi pair AFTER bl OSYieldThread region).
   Prologue chain era: addi r30,r4,0x100; addi r31 pool; li r27 flag=0;
   li r26 match=0; li r25 tbl@sda21. Ours: li r27,0 then straight into
   handshake; match/tbl/addr inits land post-handshake.
2. STACK SLOTS: era cmd@0xc, value@0x10, inlined-regcmd@0x18/0x1a.
   Ours: regcmd@0x10/0x12, cmd@0x14, value@0x18. Slot order follows
   DECL order: era declared outer cmd,value before the inlined
   ModemReadRegister locals -> flatten inner block to function scope,
   cmd+value declared early.
3. BODY: era `lwz r3,0x10(r31); lbz r4,0x10(r1); addi r0; stw r0,0x10(r31);
   add r3,r31,r3; stb r4,0x14(r3)` — direct disp off pool base.
   Ours: extra `addi r28,r31,0x10` length-pointer (+1) and
   `li r3,lbl_805D487C@sda21` INSIDE loop (+1 tbl remat).
4. Era match init (li r26,0) and flag init (li r27,0) BOTH in prologue;
   era loop-prep is only `li r28,0; b test`.

## Opening play (brief-named)
Early-materialization hoist: assign cmd = 0x23000000|1<<8, pool base
(via &modem_command_response_state use), flag=0, match=0 as the FIRST
statements of the function (function-scope decls), inner u8 value/idx
declared at function scope after cmd; handshake loop last.
