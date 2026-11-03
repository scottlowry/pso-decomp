
build/GPOE8P/src/pso/object/TObjCMName.o:     file format elf32-powerpc


Disassembly of section .text:

00000000 <TObjCMName__sub_802948F4>:
       0:	38 60 00 00 	li      r3,0
       4:	4e 80 00 20 	blr

00000008 <run_task__10TObjCMNameFv>:
       8:	94 21 ff c0 	stwu    r1,-64(r1)
       c:	7c 08 02 a6 	mflr    r0
      10:	90 01 00 44 	stw     r0,68(r1)
      14:	db e1 00 30 	stfd    f31,48(r1)
      18:	f3 e1 00 38 	xxsel   vs31,vs1,vs0,vs32
      1c:	bf a1 00 24 	stmw    r29,36(r1)
      20:	7c 7f 1b 78 	mr      r31,r3
      24:	80 83 00 28 	lwz     r4,40(r3)
      28:	38 04 00 01 	addi    r0,r4,1
      2c:	90 03 00 28 	stw     r0,40(r3)
      30:	80 03 00 20 	lwz     r0,32(r3)
      34:	2c 00 00 00 	cmpwi   r0,0
      38:	40 82 00 a8 	bne     e0 <run_task__10TObjCMNameFv+0xd8>
      3c:	80 1f 00 28 	lwz     r0,40(r31)
      40:	2c 00 00 01 	cmpwi   r0,1
      44:	40 81 01 d4 	ble     218 <run_task__10TObjCMNameFv+0x210>
      48:	38 60 00 2c 	li      r3,44
      4c:	48 00 00 01 	bl      4c <run_task__10TObjCMNameFv+0x44>
			4c: R_PPC_REL24	__nw__7TObjectFUl
      50:	7c 7e 1b 79 	mr.     r30,r3
      54:	41 82 00 28 	beq     7c <run_task__10TObjCMNameFv+0x74>
      58:	48 00 00 01 	bl      58 <run_task__10TObjCMNameFv+0x50>
			58: R_PPC_REL24	get_clamped_player_index__14TChCrEffCtrlPlFv
      5c:	7c 68 1b 78 	mr      r8,r3
      60:	7f c3 f3 78 	mr      r3,r30
      64:	7f e4 fb 78 	mr      r4,r31
      68:	38 a0 00 0c 	li      r5,12
      6c:	38 c0 00 00 	li      r6,0
      70:	38 e0 00 00 	li      r7,0
      74:	48 00 00 01 	bl      74 <run_task__10TObjCMNameFv+0x6c>
			74: R_PPC_REL24	TKeyBoardControl__ct
      78:	7c 7e 1b 78 	mr      r30,r3
      7c:	93 df 00 24 	stw     r30,36(r31)
      80:	80 7f 00 24 	lwz     r3,36(r31)
      84:	80 9f 00 1c 	lwz     r4,28(r31)
      88:	48 00 00 01 	bl      88 <run_task__10TObjCMNameFv+0x80>
			88: R_PPC_REL24	get_keyboard_field_6c__15TWindowMakeTeamFv
      8c:	48 00 00 01 	bl      8c <run_task__10TObjCMNameFv+0x84>
			8c: R_PPC_REL24	get_scale__14TObjCMMainMenuFv
      90:	ff e0 08 90 	fmr     f31,f1
      94:	c0 00 00 00 	lfs     f0,0(0)
			94: R_PPC_EMB_SDA21	@50
      98:	c0 20 00 00 	lfs     f1,0(0)
			98: R_PPC_EMB_SDA21	@49
      9c:	38 81 00 08 	addi    r4,r1,8
      a0:	ec 00 07 f2 	fmuls   f0,f0,f31
      a4:	d0 21 00 08 	stfs    f1,8(r1)
      a8:	d0 01 00 0c 	stfs    f0,12(r1)
      ac:	80 7f 00 24 	lwz     r3,36(r31)
      b0:	48 00 00 01 	bl      b0 <run_task__10TObjCMNameFv+0xa8>
			b0: R_PPC_REL24	set_sub_position__15TWindowMakeTeamFPUc
      b4:	c0 00 00 00 	lfs     f0,0(0)
			b4: R_PPC_EMB_SDA21	@52
      b8:	38 81 00 08 	addi    r4,r1,8
      bc:	c0 20 00 00 	lfs     f1,0(0)
			bc: R_PPC_EMB_SDA21	@51
      c0:	ec 00 07 f2 	fmuls   f0,f0,f31
      c4:	d0 21 00 08 	stfs    f1,8(r1)
      c8:	d0 01 00 0c 	stfs    f0,12(r1)
      cc:	80 7f 00 24 	lwz     r3,36(r31)
      d0:	48 00 00 01 	bl      d0 <run_task__10TObjCMNameFv+0xc8>
			d0: R_PPC_REL24	fn_80131ADC
      d4:	38 00 00 01 	li      r0,1
      d8:	90 1f 00 20 	stw     r0,32(r31)
      dc:	48 00 01 3c 	b       218 <run_task__10TObjCMNameFv+0x210>
      e0:	80 1f 00 2c 	lwz     r0,44(r31)
      e4:	2c 00 00 00 	cmpwi   r0,0
      e8:	40 82 00 30 	bne     118 <run_task__10TObjCMNameFv+0x110>
      ec:	c0 5f 00 30 	lfs     f2,48(r31)
      f0:	c0 20 00 00 	lfs     f1,0(0)
			f0: R_PPC_EMB_SDA21	@53
      f4:	c0 00 00 00 	lfs     f0,0(0)
			f4: R_PPC_EMB_SDA21	@54
      f8:	ec 22 08 2a 	fadds   f1,f2,f1
      fc:	fc 01 00 40 	fcmpo   cr0,f1,f0
     100:	d0 3f 00 30 	stfs    f1,48(r31)
     104:	4c 40 13 82 	cror    eq,lt,eq
     108:	40 82 01 10 	bne     218 <run_task__10TObjCMNameFv+0x210>
     10c:	d0 1f 00 30 	stfs    f0,48(r31)
     110:	48 00 00 01 	bl      110 <run_task__10TObjCMNameFv+0x108>
			110: R_PPC_REL24	queue_destruction__7TObjectFv
     114:	48 00 01 04 	b       218 <run_task__10TObjCMNameFv+0x210>
     118:	c0 5f 00 30 	lfs     f2,48(r31)
     11c:	c0 20 00 00 	lfs     f1,0(0)
			11c: R_PPC_EMB_SDA21	@55
     120:	c0 00 00 00 	lfs     f0,0(0)
			120: R_PPC_EMB_SDA21	@56
     124:	ec 22 08 2a 	fadds   f1,f2,f1
     128:	fc 01 00 40 	fcmpo   cr0,f1,f0
     12c:	d0 3f 00 30 	stfs    f1,48(r31)
     130:	40 81 00 08 	ble     138 <run_task__10TObjCMNameFv+0x130>
     134:	d0 1f 00 30 	stfs    f0,48(r31)
     138:	80 7f 00 24 	lwz     r3,36(r31)
     13c:	48 00 00 01 	bl      13c <run_task__10TObjCMNameFv+0x134>
			13c: R_PPC_REL24	update_keyboard__17TWindowSubComCardFv
     140:	2c 03 00 00 	cmpwi   r3,0
     144:	41 82 00 d4 	beq     218 <run_task__10TObjCMNameFv+0x210>
     148:	80 7f 00 24 	lwz     r3,36(r31)
     14c:	48 00 00 01 	bl      14c <run_task__10TObjCMNameFv+0x144>
			14c: R_PPC_REL24	realloc_buffer__17TWindowSubComCardFv
     150:	7c 7e 1b 78 	mr      r30,r3
     154:	3c a0 00 05 	lis     r5,5
     158:	3b a5 37 04 	addi    r29,r5,14084
     15c:	38 61 00 10 	addi    r3,r1,16
     160:	7f c4 f3 78 	mr      r4,r30
     164:	38 a0 00 0c 	li      r5,12
     168:	48 00 00 01 	bl      168 <run_task__10TObjCMNameFv+0x160>
			168: R_PPC_REL24	strncpy
     16c:	38 00 00 00 	li      r0,0
     170:	38 61 00 10 	addi    r3,r1,16
     174:	98 01 00 1c 	stb     r0,28(r1)
     178:	48 00 00 01 	bl      178 <run_task__10TObjCMNameFv+0x170>
			178: R_PPC_REL24	validate_character_name__14TObjCMMainMenuFPSc
     17c:	2c 03 00 00 	cmpwi   r3,0
     180:	40 82 00 0c 	bne     18c <run_task__10TObjCMNameFv+0x184>
     184:	3c 60 00 05 	lis     r3,5
     188:	3b a3 28 0d 	addi    r29,r3,10253
     18c:	7f e3 fb 78 	mr      r3,r31
     190:	38 81 00 10 	addi    r4,r1,16
     194:	48 00 00 01 	bl      194 <run_task__10TObjCMNameFv+0x18c>
			194: R_PPC_REL24	TObjCMName__sub_802948F4
     198:	2c 03 00 00 	cmpwi   r3,0
     19c:	41 82 00 24 	beq     1c0 <run_task__10TObjCMNameFv+0x1b8>
     1a0:	3c 60 00 05 	lis     r3,5
     1a4:	80 9f 00 1c 	lwz     r4,28(r31)
     1a8:	3b a3 26 08 	addi    r29,r3,9736
     1ac:	38 61 00 10 	addi    r3,r1,16
     1b0:	38 a0 00 0c 	li      r5,12
     1b4:	48 00 00 01 	bl      1b4 <run_task__10TObjCMNameFv+0x1ac>
			1b4: R_PPC_REL24	strncpy
     1b8:	38 00 00 00 	li      r0,0
     1bc:	98 01 00 1c 	stb     r0,28(r1)
     1c0:	38 61 00 10 	addi    r3,r1,16
     1c4:	48 00 00 01 	bl      1c4 <run_task__10TObjCMNameFv+0x1bc>
			1c4: R_PPC_REL24	copy_char_name__14TObjCMMainMenuFv
     1c8:	80 7f 00 1c 	lwz     r3,28(r31)
     1cc:	38 81 00 10 	addi    r4,r1,16
     1d0:	38 a0 00 0c 	li      r5,12
     1d4:	48 00 00 01 	bl      1d4 <run_task__10TObjCMNameFv+0x1cc>
			1d4: R_PPC_REL24	strncpy
     1d8:	80 9f 00 1c 	lwz     r4,28(r31)
     1dc:	38 00 00 00 	li      r0,0
     1e0:	7f c3 f3 78 	mr      r3,r30
     1e4:	98 04 00 0c 	stb     r0,12(r4)
     1e8:	48 00 00 01 	bl      1e8 <run_task__10TObjCMNameFv+0x1e0>
			1e8: R_PPC_REL24	mem_free
     1ec:	7f a3 eb 78 	mr      r3,r29
     1f0:	38 80 00 00 	li      r4,0
     1f4:	38 a0 00 00 	li      r5,0
     1f8:	38 c0 00 00 	li      r6,0
     1fc:	48 00 00 01 	bl      1fc <run_task__10TObjCMNameFv+0x1f4>
			1fc: R_PPC_REL24	play_sound_effect
     200:	48 00 00 01 	bl      200 <run_task__10TObjCMNameFv+0x1f8>
			200: R_PPC_REL24	clear_task_state__14TObjCMMainMenuFv
     204:	80 7f 00 24 	lwz     r3,36(r31)
     208:	48 00 00 01 	bl      208 <run_task__10TObjCMNameFv+0x200>
			208: R_PPC_REL24	queue_destruction__7TObjectFv
     20c:	38 00 00 00 	li      r0,0
     210:	90 1f 00 24 	stw     r0,36(r31)
     214:	90 1f 00 2c 	stw     r0,44(r31)
     218:	e3 e1 00 38 	psq_l   f31,56(r1),0,0
     21c:	cb e1 00 30 	lfd     f31,48(r1)
     220:	bb a1 00 24 	lmw     r29,36(r1)
     224:	80 01 00 44 	lwz     r0,68(r1)
     228:	7c 08 03 a6 	mtlr    r0
     22c:	38 21 00 40 	addi    r1,r1,64
     230:	4e 80 00 20 	blr

00000234 <create__10TObjCMNameFPv>:
     234:	94 21 ff f0 	stwu    r1,-16(r1)
     238:	7c 08 02 a6 	mflr    r0
     23c:	90 01 00 14 	stw     r0,20(r1)
     240:	93 e1 00 0c 	stw     r31,12(r1)
     244:	7c 7f 1b 78 	mr      r31,r3
     248:	38 60 00 34 	li      r3,52
     24c:	48 00 00 01 	bl      24c <create__10TObjCMNameFPv+0x18>
			24c: R_PPC_REL24	__nw__7TObjectFUl
     250:	7c 60 1b 79 	mr.     r0,r3
     254:	41 82 00 10 	beq     264 <create__10TObjCMNameFPv+0x30>
     258:	7f e4 fb 78 	mr      r4,r31
     25c:	48 00 00 01 	bl      25c <create__10TObjCMNameFPv+0x28>
			25c: R_PPC_REL24	__ct__10TObjCMNameFv
     260:	7c 60 1b 78 	mr      r0,r3
     264:	7c 03 03 78 	mr      r3,r0
     268:	80 01 00 14 	lwz     r0,20(r1)
     26c:	83 e1 00 0c 	lwz     r31,12(r1)
     270:	7c 08 03 a6 	mtlr    r0
     274:	38 21 00 10 	addi    r1,r1,16
     278:	4e 80 00 20 	blr

0000027c <__dt__10TObjCMNameFv>:
     27c:	94 21 ff f0 	stwu    r1,-16(r1)
     280:	7c 08 02 a6 	mflr    r0
     284:	90 01 00 14 	stw     r0,20(r1)
     288:	bf c1 00 08 	stmw    r30,8(r1)
     28c:	7c 7e 1b 79 	mr.     r30,r3
     290:	7c 9f 23 78 	mr      r31,r4
     294:	41 82 00 28 	beq     2bc <__dt__10TObjCMNameFv+0x40>
     298:	3c a0 00 00 	lis     r5,0
			29a: R_PPC_ADDR16_HA	__vt__10TObjCMName
     29c:	38 80 00 00 	li      r4,0
     2a0:	38 05 00 00 	addi    r0,r5,0
			2a2: R_PPC_ADDR16_LO	__vt__10TObjCMName
     2a4:	90 1e 00 18 	stw     r0,24(r30)
     2a8:	48 00 00 01 	bl      2a8 <__dt__10TObjCMNameFv+0x2c>
			2a8: R_PPC_REL24	__dt__7TObjectFv
     2ac:	7f e0 07 35 	extsh.  r0,r31
     2b0:	40 81 00 0c 	ble     2bc <__dt__10TObjCMNameFv+0x40>
     2b4:	7f c3 f3 78 	mr      r3,r30
     2b8:	48 00 00 01 	bl      2b8 <__dt__10TObjCMNameFv+0x3c>
			2b8: R_PPC_REL24	__dl__7TObjectFPv
     2bc:	7f c3 f3 78 	mr      r3,r30
     2c0:	bb c1 00 08 	lmw     r30,8(r1)
     2c4:	80 01 00 14 	lwz     r0,20(r1)
     2c8:	7c 08 03 a6 	mtlr    r0
     2cc:	38 21 00 10 	addi    r1,r1,16
     2d0:	4e 80 00 20 	blr

000002d4 <render__10TObjCMNameFv>:
     2d4:	94 21 ff d0 	stwu    r1,-48(r1)
     2d8:	7c 08 02 a6 	mflr    r0
     2dc:	90 01 00 34 	stw     r0,52(r1)
     2e0:	db e1 00 20 	stfd    f31,32(r1)
     2e4:	f3 e1 00 28 	psq_st  f31,40(r1),0,0
     2e8:	93 e1 00 1c 	stw     r31,28(r1)
     2ec:	7c 7f 1b 78 	mr      r31,r3
     2f0:	c0 20 00 00 	lfs     f1,0(0)
			2f0: R_PPC_EMB_SDA21	@85
     2f4:	c0 43 00 30 	lfs     f2,48(r3)
     2f8:	fc 02 08 40 	fcmpo   cr0,f2,f1
     2fc:	4c 40 13 82 	cror    eq,lt,eq
     300:	41 82 00 a4 	beq     3a4 <render__10TObjCMNameFv+0xd0>
     304:	c0 00 00 00 	lfs     f0,0(0)
			304: R_PPC_EMB_SDA21	@86
     308:	fc 02 00 40 	fcmpo   cr0,f2,f0
     30c:	4c 41 13 82 	cror    eq,gt,eq
     310:	40 82 00 0c 	bne     31c <render__10TObjCMNameFv+0x48>
     314:	c0 80 00 00 	lfs     f4,0(0)
			314: R_PPC_EMB_SDA21	@56
     318:	48 00 00 0c 	b       324 <render__10TObjCMNameFv+0x50>
     31c:	ec 02 08 28 	fsubs   f0,f2,f1
     320:	ec 80 08 24 	fdivs   f4,f0,f1
     324:	c0 60 00 00 	lfs     f3,0(0)
			324: R_PPC_EMB_SDA21	@56
     328:	c0 40 00 00 	lfs     f2,0(0)
			328: R_PPC_EMB_SDA21	@87
     32c:	c0 00 00 00 	lfs     f0,0(0)
			32c: R_PPC_EMB_SDA21	@88
     330:	c0 20 00 00 	lfs     f1,0(0)
			330: R_PPC_EMB_SDA21	@89
     334:	d0 61 00 0c 	stfs    f3,12(r1)
     338:	ef e1 01 3a 	fmadds  f31,f1,f4,f0
     33c:	d0 41 00 14 	stfs    f2,20(r1)
     340:	d0 01 00 10 	stfs    f0,16(r1)
     344:	80 1f 00 28 	lwz     r0,40(r31)
     348:	54 03 50 2a 	slwi    r3,r0,10
     34c:	48 00 00 01 	bl      34c <render__10TObjCMNameFv+0x78>
			34c: R_PPC_REL24	sin_table_lookup
     350:	c0 60 00 00 	lfs     f3,0(0)
			350: R_PPC_EMB_SDA21	@90
     354:	38 81 00 10 	addi    r4,r1,16
     358:	c0 41 00 10 	lfs     f2,16(r1)
     35c:	38 a1 00 08 	addi    r5,r1,8
     360:	c0 00 00 00 	lfs     f0,0(0)
			360: R_PPC_EMB_SDA21	@91
     364:	38 60 00 08 	li      r3,8
     368:	ec 63 10 7a 	fmadds  f3,f3,f1,f2
     36c:	c0 20 00 00 	lfs     f1,0(0)
			36c: R_PPC_EMB_SDA21	@92
     370:	ec 5f 18 28 	fsubs   f2,f31,f3
     374:	d0 61 00 10 	stfs    f3,16(r1)
     378:	ec 02 00 24 	fdivs   f0,f2,f0
     37c:	d0 01 00 08 	stfs    f0,8(r1)
     380:	48 00 00 01 	bl      380 <render__10TObjCMNameFv+0xac>
			380: R_PPC_REL24	draw_ui_sprite_opaque
     384:	c0 00 00 00 	lfs     f0,0(0)
			384: R_PPC_EMB_SDA21	@56
     388:	38 81 00 10 	addi    r4,r1,16
     38c:	d3 e1 00 10 	stfs    f31,16(r1)
     390:	38 a1 00 08 	addi    r5,r1,8
     394:	c0 20 00 00 	lfs     f1,0(0)
			394: R_PPC_EMB_SDA21	@92
     398:	38 60 00 09 	li      r3,9
     39c:	d0 01 00 08 	stfs    f0,8(r1)
     3a0:	48 00 00 01 	bl      3a0 <render__10TObjCMNameFv+0xcc>
			3a0: R_PPC_REL24	draw_ui_sprite_opaque
     3a4:	c0 5f 00 30 	lfs     f2,48(r31)
     3a8:	c0 00 00 00 	lfs     f0,0(0)
			3a8: R_PPC_EMB_SDA21	@54
     3ac:	fc 02 00 40 	fcmpo   cr0,f2,f0
     3b0:	4c 40 13 82 	cror    eq,lt,eq
     3b4:	41 82 00 34 	beq     3e8 <render__10TObjCMNameFv+0x114>
     3b8:	c0 00 00 00 	lfs     f0,0(0)
			3b8: R_PPC_EMB_SDA21	@85
     3bc:	3c 60 00 00 	lis     r3,0
			3be: R_PPC_ADDR16_HA	creation_name_panel_position
     3c0:	38 83 00 00 	addi    r4,r3,0
			3c2: R_PPC_ADDR16_LO	creation_name_panel_position
     3c4:	c0 20 00 00 	lfs     f1,0(0)
			3c4: R_PPC_EMB_SDA21	@93
     3c8:	fc 02 00 40 	fcmpo   cr0,f2,f0
     3cc:	38 60 00 00 	li      r3,0
     3d0:	4c 41 13 82 	cror    eq,gt,eq
     3d4:	40 82 00 0c 	bne     3e0 <render__10TObjCMNameFv+0x10c>
     3d8:	c0 40 00 00 	lfs     f2,0(0)
			3d8: R_PPC_EMB_SDA21	@56
     3dc:	48 00 00 08 	b       3e4 <render__10TObjCMNameFv+0x110>
     3e0:	ec 42 00 24 	fdivs   f2,f2,f0
     3e4:	48 00 00 01 	bl      3e4 <render__10TObjCMNameFv+0x110>
			3e4: R_PPC_REL24	draw_ui_sprite
     3e8:	e3 e1 00 28 	psq_l   f31,40(r1),0,0
     3ec:	80 01 00 34 	lwz     r0,52(r1)
     3f0:	cb e1 00 20 	lfd     f31,32(r1)
     3f4:	83 e1 00 1c 	lwz     r31,28(r1)
     3f8:	7c 08 03 a6 	mtlr    r0
     3fc:	38 21 00 30 	addi    r1,r1,48
     400:	4e 80 00 20 	blr

00000404 <__ct__10TObjCMNameFv>:
     404:	94 21 ff f0 	stwu    r1,-16(r1)
     408:	7c 08 02 a6 	mflr    r0
     40c:	90 01 00 14 	stw     r0,20(r1)
     410:	93 e1 00 0c 	stw     r31,12(r1)
     414:	7c 7f 1b 78 	mr      r31,r3
     418:	48 00 00 01 	bl      418 <__ct__10TObjCMNameFv+0x14>
			418: R_PPC_REL24	__ct__7TObjectFP7TObject
     41c:	3c 60 00 00 	lis     r3,0
			41e: R_PPC_ADDR16_HA	__vt__10TObjCMName
     420:	38 80 00 00 	li      r4,0
     424:	38 63 00 00 	addi    r3,r3,0
			426: R_PPC_ADDR16_LO	__vt__10TObjCMName
     428:	38 00 00 01 	li      r0,1
     42c:	90 7f 00 18 	stw     r3,24(r31)
     430:	38 60 00 0a 	li      r3,10
     434:	c0 00 00 00 	lfs     f0,0(0)
			434: R_PPC_EMB_SDA21	lbl_805DDA90
     438:	80 a0 00 00 	lwz     r5,0(0)
			438: R_PPC_EMB_SDA21	lbl_805D3CEC
     43c:	90 bf 00 00 	stw     r5,0(r31)
     440:	80 a0 00 00 	lwz     r5,0(0)
			440: R_PPC_EMB_SDA21	creation_player_character
     444:	90 bf 00 1c 	stw     r5,28(r31)
     448:	90 9f 00 20 	stw     r4,32(r31)
     44c:	90 9f 00 28 	stw     r4,40(r31)
     450:	90 9f 00 24 	stw     r4,36(r31)
     454:	90 1f 00 2c 	stw     r0,44(r31)
     458:	d0 1f 00 30 	stfs    f0,48(r31)
     45c:	48 00 00 01 	bl      45c <__ct__10TObjCMNameFv+0x58>
			45c: R_PPC_REL24	set_eff_tag__11TChCrEffTagFi
     460:	80 01 00 14 	lwz     r0,20(r1)
     464:	7f e3 fb 78 	mr      r3,r31
     468:	83 e1 00 0c 	lwz     r31,12(r1)
     46c:	7c 08 03 a6 	mtlr    r0
     470:	38 21 00 10 	addi    r1,r1,16
     474:	4e 80 00 20 	blr

00000478 <render__16TObjCMProportionFv>:
     478:	94 21 ff c0 	stwu    r1,-64(r1)
     47c:	7c 08 02 a6 	mflr    r0
     480:	90 01 00 44 	stw     r0,68(r1)
     484:	db e1 00 30 	stfd    f31,48(r1)
     488:	f3 e1 00 38 	xxsel   vs31,vs1,vs0,vs32
     48c:	bf a1 00 24 	stmw    r29,36(r1)
     490:	7c 7f 1b 78 	mr      r31,r3
     494:	3c 60 00 00 	lis     r3,0
			496: R_PPC_ADDR16_HA	...bss.0
     498:	c0 3f 00 28 	lfs     f1,40(r31)
     49c:	3b c3 00 00 	addi    r30,r3,0
			49e: R_PPC_ADDR16_LO	...bss.0
     4a0:	3c 60 00 00 	lis     r3,0
			4a2: R_PPC_ADDR16_HA	lbl_804DBD08
     4a4:	c0 00 00 00 	lfs     f0,0(0)
			4a4: R_PPC_EMB_SDA21	@114
     4a8:	ef e1 00 72 	fmuls   f31,f1,f1
     4ac:	38 de 00 00 	addi    r6,r30,0
     4b0:	c0 20 00 00 	lfs     f1,0(0)
			4b0: R_PPC_EMB_SDA21	@115
     4b4:	38 63 00 00 	addi    r3,r3,0
			4b6: R_PPC_ADDR16_LO	lbl_804DBD08
     4b8:	38 80 00 04 	li      r4,4
     4bc:	38 a0 00 05 	li      r5,5
     4c0:	ec 00 07 f2 	fmuls   f0,f0,f31
     4c4:	fc 00 00 1e 	fctiwz  f0,f0
     4c8:	d8 01 00 08 	stfd    f0,8(r1)
     4cc:	80 01 00 0c 	lwz     r0,12(r1)
     4d0:	54 00 c0 0e 	slwi    r0,r0,24
     4d4:	64 00 00 ff 	oris    r0,r0,255
     4d8:	60 00 ff ff 	ori     r0,r0,65535
     4dc:	90 06 00 0c 	stw     r0,12(r6)
     4e0:	90 06 00 08 	stw     r0,8(r6)
     4e4:	90 06 00 04 	stw     r0,4(r6)
     4e8:	90 1e 00 00 	stw     r0,0(r30)
     4ec:	48 00 00 01 	bl      4ec <render__16TObjCMProportionFv+0x74>
			4ec: R_PPC_REL24	draw_strip_swap_color__15TWindowCtrlMainFllf
     4f0:	c0 00 00 00 	lfs     f0,0(0)
			4f0: R_PPC_EMB_SDA21	@116
     4f4:	3c 60 00 00 	lis     r3,0
			4f6: R_PPC_ADDR16_HA	lbl_804DBD18
     4f8:	38 de 00 30 	addi    r6,r30,48
     4fc:	c0 e0 00 00 	lfs     f7,0(0)
			4fc: R_PPC_EMB_SDA21	@120
     500:	ec 00 07 f2 	fmuls   f0,f0,f31
     504:	c1 00 00 00 	lfs     f8,0(0)
			504: R_PPC_EMB_SDA21	@119
     508:	c1 20 00 00 	lfs     f9,0(0)
			508: R_PPC_EMB_SDA21	@118
     50c:	3b be 00 10 	addi    r29,r30,16
     510:	c0 a0 00 00 	lfs     f5,0(0)
			510: R_PPC_EMB_SDA21	@117
     514:	38 63 00 00 	addi    r3,r3,0
			516: R_PPC_ADDR16_LO	lbl_804DBD18
     518:	fc 00 00 1e 	fctiwz  f0,f0
     51c:	c0 40 00 00 	lfs     f2,0(0)
			51c: R_PPC_EMB_SDA21	@122
     520:	c0 60 00 00 	lfs     f3,0(0)
			520: R_PPC_EMB_SDA21	@121
     524:	38 80 00 04 	li      r4,4
     528:	c0 20 00 00 	lfs     f1,0(0)
			528: R_PPC_EMB_SDA21	@115
     52c:	38 a0 00 06 	li      r5,6
     530:	d8 01 00 10 	stfd    f0,16(r1)
     534:	c0 00 00 00 	lfs     f0,0(0)
			534: R_PPC_EMB_SDA21	@123
     538:	80 01 00 14 	lwz     r0,20(r1)
     53c:	54 00 c0 0e 	slwi    r0,r0,24
     540:	64 00 00 ff 	oris    r0,r0,255
     544:	60 00 ff ff 	ori     r0,r0,65535
     548:	90 06 00 0c 	stw     r0,12(r6)
     54c:	90 06 00 08 	stw     r0,8(r6)
     550:	90 06 00 04 	stw     r0,4(r6)
     554:	90 1e 00 30 	stw     r0,48(r30)
     558:	80 df 00 1c 	lwz     r6,28(r31)
     55c:	c0 c6 00 48 	lfs     f6,72(r6)
     560:	c0 86 00 4c 	lfs     f4,76(r6)
     564:	ec c6 38 28 	fsubs   f6,f6,f7
     568:	ec 84 38 28 	fsubs   f4,f4,f7
     56c:	d0 5d 00 0c 	stfs    f2,12(r29)
     570:	d0 5d 00 04 	stfs    f2,4(r29)
     574:	ec c8 01 b2 	fmuls   f6,f8,f6
     578:	ec 48 01 32 	fmuls   f2,f8,f4
     57c:	d0 1d 00 1c 	stfs    f0,28(r29)
     580:	ec 89 29 ba 	fmadds  f4,f9,f6,f5
     584:	ef e9 18 ba 	fmadds  f31,f9,f2,f3
     588:	d0 1d 00 14 	stfs    f0,20(r29)
     58c:	ec 04 40 28 	fsubs   f0,f4,f8
     590:	ec 48 20 2a 	fadds   f2,f8,f4
     594:	d0 1e 00 10 	stfs    f0,16(r30)
     598:	d0 5d 00 08 	stfs    f2,8(r29)
     59c:	d0 5d 00 10 	stfs    f2,16(r29)
     5a0:	d0 1d 00 18 	stfs    f0,24(r29)
     5a4:	48 00 00 01 	bl      5a4 <render__16TObjCMProportionFv+0x12c>
			5a4: R_PPC_REL24	draw_strip_swap_color__15TWindowCtrlMainFllf
     5a8:	c0 20 00 00 	lfs     f1,0(0)
			5a8: R_PPC_EMB_SDA21	@119
     5ac:	3c 60 00 00 	lis     r3,0
			5ae: R_PPC_ADDR16_HA	lbl_804DBD18
     5b0:	c0 40 00 00 	lfs     f2,0(0)
			5b0: R_PPC_EMB_SDA21	@124
     5b4:	38 63 00 00 	addi    r3,r3,0
			5b6: R_PPC_ADDR16_LO	lbl_804DBD18
     5b8:	ec 7f 08 28 	fsubs   f3,f31,f1
     5bc:	c0 00 00 00 	lfs     f0,0(0)
			5bc: R_PPC_EMB_SDA21	@125
     5c0:	ec 81 f8 2a 	fadds   f4,f1,f31
     5c4:	d0 5d 00 08 	stfs    f2,8(r29)
     5c8:	c0 20 00 00 	lfs     f1,0(0)
			5c8: R_PPC_EMB_SDA21	@115
     5cc:	38 80 00 04 	li      r4,4
     5d0:	d0 7d 00 04 	stfs    f3,4(r29)
     5d4:	38 a0 00 06 	li      r5,6
     5d8:	d0 9d 00 0c 	stfs    f4,12(r29)
     5dc:	d0 5e 00 10 	stfs    f2,16(r30)
     5e0:	d0 9d 00 14 	stfs    f4,20(r29)
     5e4:	d0 7d 00 1c 	stfs    f3,28(r29)
     5e8:	d0 1d 00 18 	stfs    f0,24(r29)
     5ec:	d0 1d 00 10 	stfs    f0,16(r29)
     5f0:	48 00 00 01 	bl      5f0 <render__16TObjCMProportionFv+0x178>
			5f0: R_PPC_REL24	draw_strip_swap_color__15TWindowCtrlMainFllf
     5f4:	c0 3f 00 28 	lfs     f1,40(r31)
     5f8:	48 00 00 01 	bl      5f8 <render__16TObjCMProportionFv+0x180>
			5f8: R_PPC_REL24	draw_creation_ruler_lines__Ff
     5fc:	e3 e1 00 38 	psq_l   f31,56(r1),0,0
     600:	cb e1 00 30 	lfd     f31,48(r1)
     604:	bb a1 00 24 	lmw     r29,36(r1)
     608:	80 01 00 44 	lwz     r0,68(r1)
     60c:	7c 08 03 a6 	mtlr    r0
     610:	38 21 00 40 	addi    r1,r1,64
     614:	4e 80 00 20 	blr

00000618 <run_task__16TObjCMProportionFv>:
     618:	94 21 ff b0 	stwu    r1,-80(r1)
     61c:	7c 08 02 a6 	mflr    r0
     620:	90 01 00 54 	stw     r0,84(r1)
     624:	db e1 00 40 	stfd    f31,64(r1)
     628:	f3 e1 00 48 	xsmaddmsp vs31,vs1,vs0
     62c:	db c1 00 30 	stfd    f30,48(r1)
     630:	f3 c1 00 38 	xxsel   vs30,vs1,vs0,vs32
     634:	db a1 00 20 	stfd    f29,32(r1)
     638:	f3 a1 00 28 	psq_st  f29,40(r1),0,0
     63c:	93 e1 00 1c 	stw     r31,28(r1)
     640:	7c 7f 1b 78 	mr      r31,r3
     644:	48 00 00 01 	bl      644 <run_task__16TObjCMProportionFv+0x2c>
			644: R_PPC_REL24	get_proportion__14TObjCMMainMenuFv
     648:	80 1f 00 24 	lwz     r0,36(r31)
     64c:	2c 00 00 00 	cmpwi   r0,0
     650:	41 82 00 30 	beq     680 <run_task__16TObjCMProportionFv+0x68>
     654:	c0 40 00 00 	lfs     f2,0(0)
			654: R_PPC_EMB_SDA21	lbl_805DDA70
     658:	c0 1f 00 28 	lfs     f0,40(r31)
     65c:	fc 02 00 00 	fcmpu   cr0,f2,f0
     660:	40 82 00 3c 	bne     69c <run_task__16TObjCMProportionFv+0x84>
     664:	c0 40 00 00 	lfs     f2,0(0)
			664: R_PPC_EMB_SDA21	lbl_805DDAE0
     668:	c0 00 00 00 	lfs     f0,0(0)
			668: R_PPC_EMB_SDA21	@54
     66c:	ec 21 10 2a 	fadds   f1,f1,f2
     670:	fc 01 00 40 	fcmpo   cr0,f1,f0
     674:	40 80 00 28 	bge     69c <run_task__16TObjCMProportionFv+0x84>
     678:	fc 20 00 90 	fmr     f1,f0
     67c:	48 00 00 20 	b       69c <run_task__16TObjCMProportionFv+0x84>
     680:	c0 40 00 00 	lfs     f2,0(0)
			680: R_PPC_EMB_SDA21	lbl_805DDA70
     684:	c0 1f 00 28 	lfs     f0,40(r31)
     688:	ec 02 00 28 	fsubs   f0,f2,f0
     68c:	fc 01 00 40 	fcmpo   cr0,f1,f0
     690:	40 81 00 08 	ble     698 <run_task__16TObjCMProportionFv+0x80>
     694:	48 00 00 08 	b       69c <run_task__16TObjCMProportionFv+0x84>
     698:	fc 20 00 90 	fmr     f1,f0
     69c:	48 00 00 01 	bl      69c <run_task__16TObjCMProportionFv+0x84>
			69c: R_PPC_REL24	set_creation_projection_center__Ff
     6a0:	80 1f 00 20 	lwz     r0,32(r31)
     6a4:	2c 00 00 00 	cmpwi   r0,0
     6a8:	40 82 00 10 	bne     6b8 <run_task__16TObjCMProportionFv+0xa0>
     6ac:	38 00 00 01 	li      r0,1
     6b0:	90 1f 00 20 	stw     r0,32(r31)
     6b4:	48 00 01 d0 	b       884 <run_task__16TObjCMProportionFv+0x26c>
     6b8:	80 1f 00 24 	lwz     r0,36(r31)
     6bc:	2c 00 00 00 	cmpwi   r0,0
     6c0:	40 82 00 34 	bne     6f4 <run_task__16TObjCMProportionFv+0xdc>
     6c4:	c0 5f 00 28 	lfs     f2,40(r31)
     6c8:	c0 20 00 00 	lfs     f1,0(0)
			6c8: R_PPC_EMB_SDA21	lbl_805DDAA8
     6cc:	c0 00 00 00 	lfs     f0,0(0)
			6cc: R_PPC_EMB_SDA21	@54
     6d0:	ec 22 08 2a 	fadds   f1,f2,f1
     6d4:	fc 01 00 40 	fcmpo   cr0,f1,f0
     6d8:	d0 3f 00 28 	stfs    f1,40(r31)
     6dc:	4c 40 13 82 	cror    eq,lt,eq
     6e0:	40 82 01 a4 	bne     884 <run_task__16TObjCMProportionFv+0x26c>
     6e4:	d0 1f 00 28 	stfs    f0,40(r31)
     6e8:	7f e3 fb 78 	mr      r3,r31
     6ec:	48 00 00 01 	bl      6ec <run_task__16TObjCMProportionFv+0xd4>
			6ec: R_PPC_REL24	queue_destruction__7TObjectFv
     6f0:	48 00 01 94 	b       884 <run_task__16TObjCMProportionFv+0x26c>
     6f4:	c0 5f 00 28 	lfs     f2,40(r31)
     6f8:	c0 20 00 00 	lfs     f1,0(0)
			6f8: R_PPC_EMB_SDA21	lbl_805DDAAC
     6fc:	c0 00 00 00 	lfs     f0,0(0)
			6fc: R_PPC_EMB_SDA21	@56
     700:	ec 22 08 2a 	fadds   f1,f2,f1
     704:	fc 01 00 40 	fcmpo   cr0,f1,f0
     708:	d0 3f 00 28 	stfs    f1,40(r31)
     70c:	40 81 00 08 	ble     714 <run_task__16TObjCMProportionFv+0xfc>
     710:	d0 1f 00 28 	stfs    f0,40(r31)
     714:	38 61 00 0c 	addi    r3,r1,12
     718:	38 81 00 08 	addi    r4,r1,8
     71c:	48 00 00 01 	bl      71c <run_task__16TObjCMProportionFv+0x104>
			71c: R_PPC_REL24	get_creation_pad_stick__FPlPf
     720:	80 61 00 0c 	lwz     r3,12(r1)
     724:	48 00 00 01 	bl      724 <run_task__16TObjCMProportionFv+0x10c>
			724: R_PPC_REL24	sin_table_lookup
     728:	c0 41 00 08 	lfs     f2,8(r1)
     72c:	c0 00 00 00 	lfs     f0,0(0)
			72c: R_PPC_EMB_SDA21	lbl_805DDAE4
     730:	ec 22 00 72 	fmuls   f1,f2,f1
     734:	80 61 00 0c 	lwz     r3,12(r1)
     738:	ef c0 00 72 	fmuls   f30,f0,f1
     73c:	48 00 00 01 	bl      73c <run_task__16TObjCMProportionFv+0x124>
			73c: R_PPC_REL24	cos_table_lookup
     740:	fc 40 08 50 	fneg    f2,f1
     744:	c0 21 00 08 	lfs     f1,8(r1)
     748:	c0 00 00 00 	lfs     f0,0(0)
			748: R_PPC_EMB_SDA21	lbl_805DDAE4
     74c:	ec 21 00 b2 	fmuls   f1,f1,f2
     750:	ef a0 00 72 	fmuls   f29,f0,f1
     754:	fc 20 e8 90 	fmr     f1,f29
     758:	48 00 00 01 	bl      758 <run_task__16TObjCMProportionFv+0x140>
			758: R_PPC_REL24	fabs_float
     75c:	ff e0 08 90 	fmr     f31,f1
     760:	fc 20 f0 90 	fmr     f1,f30
     764:	48 00 00 01 	bl      764 <run_task__16TObjCMProportionFv+0x14c>
			764: R_PPC_REL24	fabs_float
     768:	ec 21 f8 2a 	fadds   f1,f1,f31
     76c:	c0 00 00 00 	lfs     f0,0(0)
			76c: R_PPC_EMB_SDA21	lbl_805DDA90
     770:	fc 00 08 00 	fcmpu   cr0,f0,f1
     774:	40 82 00 5c 	bne     7d0 <run_task__16TObjCMProportionFv+0x1b8>
     778:	38 60 00 80 	li      r3,128
     77c:	48 00 00 01 	bl      77c <run_task__16TObjCMProportionFv+0x164>
			77c: R_PPC_REL24	creation_buttons_held__Fl
     780:	2c 03 00 00 	cmpwi   r3,0
     784:	41 82 00 0c 	beq     790 <run_task__16TObjCMProportionFv+0x178>
     788:	c3 c0 00 00 	lfs     f30,0(0)
			788: R_PPC_EMB_SDA21	lbl_805DDAE8
     78c:	48 00 00 18 	b       7a4 <run_task__16TObjCMProportionFv+0x18c>
     790:	38 60 00 40 	li      r3,64
     794:	48 00 00 01 	bl      794 <run_task__16TObjCMProportionFv+0x17c>
			794: R_PPC_REL24	creation_buttons_held__Fl
     798:	2c 03 00 00 	cmpwi   r3,0
     79c:	41 82 00 08 	beq     7a4 <run_task__16TObjCMProportionFv+0x18c>
     7a0:	c3 c0 00 00 	lfs     f30,0(0)
			7a0: R_PPC_EMB_SDA21	lbl_805DDAEC
     7a4:	38 60 00 20 	li      r3,32
     7a8:	48 00 00 01 	bl      7a8 <run_task__16TObjCMProportionFv+0x190>
			7a8: R_PPC_REL24	creation_buttons_held__Fl
     7ac:	2c 03 00 00 	cmpwi   r3,0
     7b0:	41 82 00 0c 	beq     7bc <run_task__16TObjCMProportionFv+0x1a4>
     7b4:	c3 a0 00 00 	lfs     f29,0(0)
			7b4: R_PPC_EMB_SDA21	lbl_805DDAE8
     7b8:	48 00 00 18 	b       7d0 <run_task__16TObjCMProportionFv+0x1b8>
     7bc:	38 60 00 10 	li      r3,16
     7c0:	48 00 00 01 	bl      7c0 <run_task__16TObjCMProportionFv+0x1a8>
			7c0: R_PPC_REL24	creation_buttons_held__Fl
     7c4:	2c 03 00 00 	cmpwi   r3,0
     7c8:	41 82 00 08 	beq     7d0 <run_task__16TObjCMProportionFv+0x1b8>
     7cc:	c3 a0 00 00 	lfs     f29,0(0)
			7cc: R_PPC_EMB_SDA21	lbl_805DDAEC
     7d0:	80 7f 00 1c 	lwz     r3,28(r31)
     7d4:	c0 20 00 00 	lfs     f1,0(0)
			7d4: R_PPC_EMB_SDA21	lbl_805DDAF0
     7d8:	c0 03 00 48 	lfs     f0,72(r3)
     7dc:	ec 00 f0 2a 	fadds   f0,f0,f30
     7e0:	d0 03 00 48 	stfs    f0,72(r3)
     7e4:	80 7f 00 1c 	lwz     r3,28(r31)
     7e8:	c0 03 00 4c 	lfs     f0,76(r3)
     7ec:	ec 00 e8 2a 	fadds   f0,f0,f29
     7f0:	d0 03 00 4c 	stfs    f0,76(r3)
     7f4:	80 7f 00 1c 	lwz     r3,28(r31)
     7f8:	c0 43 00 48 	lfs     f2,72(r3)
     7fc:	fc 02 08 40 	fcmpo   cr0,f2,f1
     800:	40 81 00 10 	ble     810 <run_task__16TObjCMProportionFv+0x1f8>
     804:	ec 02 08 28 	fsubs   f0,f2,f1
     808:	d0 03 00 48 	stfs    f0,72(r3)
     80c:	48 00 00 18 	b       824 <run_task__16TObjCMProportionFv+0x20c>
     810:	c0 00 00 00 	lfs     f0,0(0)
			810: R_PPC_EMB_SDA21	lbl_805DDA90
     814:	fc 02 00 40 	fcmpo   cr0,f2,f0
     818:	40 80 00 0c 	bge     824 <run_task__16TObjCMProportionFv+0x20c>
     81c:	ec 02 08 2a 	fadds   f0,f2,f1
     820:	d0 03 00 48 	stfs    f0,72(r3)
     824:	80 7f 00 1c 	lwz     r3,28(r31)
     828:	c0 00 00 00 	lfs     f0,0(0)
			828: R_PPC_EMB_SDA21	lbl_805DDAF0
     82c:	c0 23 00 4c 	lfs     f1,76(r3)
     830:	fc 01 00 40 	fcmpo   cr0,f1,f0
     834:	40 81 00 0c 	ble     840 <run_task__16TObjCMProportionFv+0x228>
     838:	d0 03 00 4c 	stfs    f0,76(r3)
     83c:	48 00 00 14 	b       850 <run_task__16TObjCMProportionFv+0x238>
     840:	c0 00 00 00 	lfs     f0,0(0)
			840: R_PPC_EMB_SDA21	lbl_805DDA90
     844:	fc 01 00 40 	fcmpo   cr0,f1,f0
     848:	40 80 00 08 	bge     850 <run_task__16TObjCMProportionFv+0x238>
     84c:	d0 03 00 4c 	stfs    f0,76(r3)
     850:	38 60 00 06 	li      r3,6
     854:	48 00 00 01 	bl      854 <run_task__16TObjCMProportionFv+0x23c>
			854: R_PPC_REL24	creation_buttons_pressed__Fl
     858:	2c 03 00 00 	cmpwi   r3,0
     85c:	41 82 00 28 	beq     884 <run_task__16TObjCMProportionFv+0x26c>
     860:	3c 60 00 05 	lis     r3,5
     864:	38 80 00 00 	li      r4,0
     868:	38 63 37 04 	addi    r3,r3,14084
     86c:	38 a0 00 00 	li      r5,0
     870:	38 c0 00 00 	li      r6,0
     874:	48 00 00 01 	bl      874 <run_task__16TObjCMProportionFv+0x25c>
			874: R_PPC_REL24	play_sound_effect
     878:	48 00 00 01 	bl      878 <run_task__16TObjCMProportionFv+0x260>
			878: R_PPC_REL24	clear_task_state__14TObjCMMainMenuFv
     87c:	38 00 00 00 	li      r0,0
     880:	90 1f 00 24 	stw     r0,36(r31)
     884:	e3 e1 00 48 	psq_l   f31,72(r1),0,0
     888:	cb e1 00 40 	lfd     f31,64(r1)
     88c:	e3 c1 00 38 	lq      r30,48(r1)
     890:	cb c1 00 30 	lfd     f30,48(r1)
     894:	e3 a1 00 28 	psq_l   f29,40(r1),0,0
     898:	cb a1 00 20 	lfd     f29,32(r1)
     89c:	80 01 00 54 	lwz     r0,84(r1)
     8a0:	83 e1 00 1c 	lwz     r31,28(r1)
     8a4:	7c 08 03 a6 	mtlr    r0
     8a8:	38 21 00 50 	addi    r1,r1,80
     8ac:	4e 80 00 20 	blr

000008b0 <create__16TObjCMProportionFPv>:
     8b0:	94 21 ff f0 	stwu    r1,-16(r1)
     8b4:	7c 08 02 a6 	mflr    r0
     8b8:	90 01 00 14 	stw     r0,20(r1)
     8bc:	93 e1 00 0c 	stw     r31,12(r1)
     8c0:	7c 7f 1b 78 	mr      r31,r3
     8c4:	38 60 00 2c 	li      r3,44
     8c8:	48 00 00 01 	bl      8c8 <create__16TObjCMProportionFPv+0x18>
			8c8: R_PPC_REL24	__nw__7TObjectFUl
     8cc:	7c 60 1b 79 	mr.     r0,r3
     8d0:	41 82 00 10 	beq     8e0 <create__16TObjCMProportionFPv+0x30>
     8d4:	7f e4 fb 78 	mr      r4,r31
     8d8:	48 00 00 01 	bl      8d8 <create__16TObjCMProportionFPv+0x28>
			8d8: R_PPC_REL24	TObjCMProportion__ct
     8dc:	7c 60 1b 78 	mr      r0,r3
     8e0:	7c 03 03 78 	mr      r3,r0
     8e4:	80 01 00 14 	lwz     r0,20(r1)
     8e8:	83 e1 00 0c 	lwz     r31,12(r1)
     8ec:	7c 08 03 a6 	mtlr    r0
     8f0:	38 21 00 10 	addi    r1,r1,16
     8f4:	4e 80 00 20 	blr

000008f8 <__dt__16TObjCMProportionFv>:
     8f8:	94 21 ff f0 	stwu    r1,-16(r1)
     8fc:	7c 08 02 a6 	mflr    r0
     900:	90 01 00 14 	stw     r0,20(r1)
     904:	bf c1 00 08 	stmw    r30,8(r1)
     908:	7c 7e 1b 79 	mr.     r30,r3
     90c:	7c 9f 23 78 	mr      r31,r4
     910:	41 82 00 34 	beq     944 <__dt__16TObjCMProportionFv+0x4c>
     914:	3c 60 00 00 	lis     r3,0
			916: R_PPC_ADDR16_HA	__vt__16TObjCMProportion
     918:	c0 20 00 00 	lfs     f1,0(0)
			918: R_PPC_EMB_SDA21	lbl_805DDA70
     91c:	38 03 00 00 	addi    r0,r3,0
			91e: R_PPC_ADDR16_LO	__vt__16TObjCMProportion
     920:	90 1e 00 18 	stw     r0,24(r30)
     924:	48 00 00 01 	bl      924 <__dt__16TObjCMProportionFv+0x2c>
			924: R_PPC_REL24	set_creation_projection_center__Ff
     928:	7f c3 f3 78 	mr      r3,r30
     92c:	38 80 00 00 	li      r4,0
     930:	48 00 00 01 	bl      930 <__dt__16TObjCMProportionFv+0x38>
			930: R_PPC_REL24	__dt__7TObjectFv
     934:	7f e0 07 35 	extsh.  r0,r31
     938:	40 81 00 0c 	ble     944 <__dt__16TObjCMProportionFv+0x4c>
     93c:	7f c3 f3 78 	mr      r3,r30
     940:	48 00 00 01 	bl      940 <__dt__16TObjCMProportionFv+0x48>
			940: R_PPC_REL24	__dl__7TObjectFPv
     944:	7f c3 f3 78 	mr      r3,r30
     948:	bb c1 00 08 	lmw     r30,8(r1)
     94c:	80 01 00 14 	lwz     r0,20(r1)
     950:	7c 08 03 a6 	mtlr    r0
     954:	38 21 00 10 	addi    r1,r1,16
     958:	4e 80 00 20 	blr

0000095c <TObjCMProportion__ct>:
     95c:	94 21 ff f0 	stwu    r1,-16(r1)
     960:	7c 08 02 a6 	mflr    r0
     964:	90 01 00 14 	stw     r0,20(r1)
     968:	93 e1 00 0c 	stw     r31,12(r1)
     96c:	7c 7f 1b 78 	mr      r31,r3
     970:	48 00 00 01 	bl      970 <TObjCMProportion__ct+0x14>
			970: R_PPC_REL24	__ct__7TObjectFP7TObject
     974:	3c 60 00 00 	lis     r3,0
			976: R_PPC_ADDR16_HA	__vt__16TObjCMProportion
     978:	38 80 00 00 	li      r4,0
     97c:	38 63 00 00 	addi    r3,r3,0
			97e: R_PPC_ADDR16_LO	__vt__16TObjCMProportion
     980:	38 00 00 01 	li      r0,1
     984:	90 7f 00 18 	stw     r3,24(r31)
     988:	38 60 00 09 	li      r3,9
     98c:	c0 00 00 00 	lfs     f0,0(0)
			98c: R_PPC_EMB_SDA21	lbl_805DDA90
     990:	80 a0 00 00 	lwz     r5,0(0)
			990: R_PPC_EMB_SDA21	lbl_805D3CE8
     994:	90 bf 00 00 	stw     r5,0(r31)
     998:	80 a0 00 00 	lwz     r5,0(0)
			998: R_PPC_EMB_SDA21	creation_player_character
     99c:	90 bf 00 1c 	stw     r5,28(r31)
     9a0:	90 9f 00 20 	stw     r4,32(r31)
     9a4:	90 1f 00 24 	stw     r0,36(r31)
     9a8:	d0 1f 00 28 	stfs    f0,40(r31)
     9ac:	48 00 00 01 	bl      9ac <TObjCMProportion__ct+0x50>
			9ac: R_PPC_REL24	set_eff_tag__11TChCrEffTagFi
     9b0:	80 01 00 14 	lwz     r0,20(r1)
     9b4:	7f e3 fb 78 	mr      r3,r31
     9b8:	83 e1 00 0c 	lwz     r31,12(r1)
     9bc:	7c 08 03 a6 	mtlr    r0
     9c0:	38 21 00 10 	addi    r1,r1,16
     9c4:	4e 80 00 20 	blr

000009c8 <render__16TObjCMAutoMkDataFv>:
     9c8:	94 21 ff f0 	stwu    r1,-16(r1)
     9cc:	7c 08 02 a6 	mflr    r0
     9d0:	90 01 00 14 	stw     r0,20(r1)
     9d4:	c0 23 00 38 	lfs     f1,56(r3)
     9d8:	48 00 00 01 	bl      9d8 <render__16TObjCMAutoMkDataFv+0x10>
			9d8: R_PPC_REL24	draw_creation_ruler_lines__Ff
     9dc:	80 01 00 14 	lwz     r0,20(r1)
     9e0:	7c 08 03 a6 	mtlr    r0
     9e4:	38 21 00 10 	addi    r1,r1,16
     9e8:	4e 80 00 20 	blr

000009ec <run_task__16TObjCMAutoMkDataFv>:
     9ec:	94 21 ff 90 	stwu    r1,-112(r1)
     9f0:	7c 08 02 a6 	mflr    r0
     9f4:	90 01 00 74 	stw     r0,116(r1)
     9f8:	bf 81 00 60 	stmw    r28,96(r1)
     9fc:	7c 7f 1b 78 	mr      r31,r3
     a00:	48 00 00 01 	bl      a00 <run_task__16TObjCMAutoMkDataFv+0x14>
			a00: R_PPC_REL24	get_proportion__14TObjCMMainMenuFv
     a04:	80 1f 00 20 	lwz     r0,32(r31)
     a08:	2c 00 00 02 	cmpwi   r0,2
     a0c:	41 82 00 30 	beq     a3c <run_task__16TObjCMAutoMkDataFv+0x50>
     a10:	c0 40 00 00 	lfs     f2,0(0)
			a10: R_PPC_EMB_SDA21	@56
     a14:	c0 1f 00 38 	lfs     f0,56(r31)
     a18:	fc 02 00 00 	fcmpu   cr0,f2,f0
     a1c:	40 82 00 3c 	bne     a58 <run_task__16TObjCMAutoMkDataFv+0x6c>
     a20:	c0 40 00 00 	lfs     f2,0(0)
			a20: R_PPC_EMB_SDA21	lbl_805DDAE0
     a24:	c0 00 00 00 	lfs     f0,0(0)
			a24: R_PPC_EMB_SDA21	@54
     a28:	ec 21 10 2a 	fadds   f1,f1,f2
     a2c:	fc 01 00 40 	fcmpo   cr0,f1,f0
     a30:	40 80 00 28 	bge     a58 <run_task__16TObjCMAutoMkDataFv+0x6c>
     a34:	fc 20 00 90 	fmr     f1,f0
     a38:	48 00 00 20 	b       a58 <run_task__16TObjCMAutoMkDataFv+0x6c>
     a3c:	c0 40 00 00 	lfs     f2,0(0)
			a3c: R_PPC_EMB_SDA21	@56
     a40:	c0 1f 00 38 	lfs     f0,56(r31)
     a44:	ec 02 00 28 	fsubs   f0,f2,f0
     a48:	fc 01 00 40 	fcmpo   cr0,f1,f0
     a4c:	40 81 00 08 	ble     a54 <run_task__16TObjCMAutoMkDataFv+0x68>
     a50:	48 00 00 08 	b       a58 <run_task__16TObjCMAutoMkDataFv+0x6c>
     a54:	fc 20 00 90 	fmr     f1,f0
     a58:	48 00 00 01 	bl      a58 <run_task__16TObjCMAutoMkDataFv+0x6c>
			a58: R_PPC_REL24	set_creation_projection_center__Ff
     a5c:	80 1f 00 20 	lwz     r0,32(r31)
     a60:	2c 00 00 02 	cmpwi   r0,2
     a64:	40 82 00 34 	bne     a98 <run_task__16TObjCMAutoMkDataFv+0xac>
     a68:	c0 5f 00 38 	lfs     f2,56(r31)
     a6c:	c0 20 00 00 	lfs     f1,0(0)
			a6c: R_PPC_EMB_SDA21	lbl_805DDAA8
     a70:	c0 00 00 00 	lfs     f0,0(0)
			a70: R_PPC_EMB_SDA21	@54
     a74:	ec 22 08 2a 	fadds   f1,f2,f1
     a78:	fc 01 00 40 	fcmpo   cr0,f1,f0
     a7c:	d0 3f 00 38 	stfs    f1,56(r31)
     a80:	4c 40 13 82 	cror    eq,lt,eq
     a84:	40 82 05 74 	bne     ff8 <run_task__16TObjCMAutoMkDataFv+0x60c>
     a88:	d0 1f 00 38 	stfs    f0,56(r31)
     a8c:	7f e3 fb 78 	mr      r3,r31
     a90:	48 00 00 01 	bl      a90 <run_task__16TObjCMAutoMkDataFv+0xa4>
			a90: R_PPC_REL24	queue_destruction__7TObjectFv
     a94:	48 00 05 64 	b       ff8 <run_task__16TObjCMAutoMkDataFv+0x60c>
     a98:	c0 5f 00 38 	lfs     f2,56(r31)
     a9c:	c0 20 00 00 	lfs     f1,0(0)
			a9c: R_PPC_EMB_SDA21	lbl_805DDAAC
     aa0:	c0 00 00 00 	lfs     f0,0(0)
			aa0: R_PPC_EMB_SDA21	@56
     aa4:	ec 22 08 2a 	fadds   f1,f2,f1
     aa8:	fc 01 00 40 	fcmpo   cr0,f1,f0
     aac:	d0 3f 00 38 	stfs    f1,56(r31)
     ab0:	40 81 00 08 	ble     ab8 <run_task__16TObjCMAutoMkDataFv+0xcc>
     ab4:	d0 1f 00 38 	stfs    f0,56(r31)
     ab8:	80 1f 00 20 	lwz     r0,32(r31)
     abc:	2c 00 00 02 	cmpwi   r0,2
     ac0:	41 82 00 4c 	beq     b0c <run_task__16TObjCMAutoMkDataFv+0x120>
     ac4:	40 80 00 10 	bge     ad4 <run_task__16TObjCMAutoMkDataFv+0xe8>
     ac8:	2c 00 00 01 	cmpwi   r0,1
     acc:	40 80 00 14 	bge     ae0 <run_task__16TObjCMAutoMkDataFv+0xf4>
     ad0:	48 00 00 3c 	b       b0c <run_task__16TObjCMAutoMkDataFv+0x120>
     ad4:	2c 00 00 04 	cmpwi   r0,4
     ad8:	40 80 00 34 	bge     b0c <run_task__16TObjCMAutoMkDataFv+0x120>
     adc:	48 00 00 2c 	b       b08 <run_task__16TObjCMAutoMkDataFv+0x11c>
     ae0:	3c 60 00 00 	lis     r3,0
			ae2: R_PPC_ADDR16_HA	lbl_80465118
     ae4:	38 81 00 08 	addi    r4,r1,8
     ae8:	38 c3 00 00 	addi    r6,r3,0
			aea: R_PPC_ADDR16_LO	lbl_80465118
     aec:	38 60 00 02 	li      r3,2
     af0:	80 a6 00 00 	lwz     r5,0(r6)
     af4:	80 06 00 04 	lwz     r0,4(r6)
     af8:	90 a1 00 08 	stw     r5,8(r1)
     afc:	90 01 00 0c 	stw     r0,12(r1)
     b00:	48 00 00 01 	bl      b00 <run_task__16TObjCMAutoMkDataFv+0x114>
			b00: R_PPC_REL24	TObjCMIcon__sub_802994C8
     b04:	48 00 00 08 	b       b0c <run_task__16TObjCMAutoMkDataFv+0x120>
     b08:	48 00 00 01 	bl      b08 <run_task__16TObjCMAutoMkDataFv+0x11c>
			b08: R_PPC_REL24	reset_icon_flags__10TObjCMIconFv
     b0c:	80 1f 00 20 	lwz     r0,32(r31)
     b10:	2c 00 00 02 	cmpwi   r0,2
     b14:	41 82 04 e4 	beq     ff8 <run_task__16TObjCMAutoMkDataFv+0x60c>
     b18:	40 80 00 14 	bge     b2c <run_task__16TObjCMAutoMkDataFv+0x140>
     b1c:	2c 00 00 00 	cmpwi   r0,0
     b20:	41 82 00 18 	beq     b38 <run_task__16TObjCMAutoMkDataFv+0x14c>
     b24:	40 80 00 20 	bge     b44 <run_task__16TObjCMAutoMkDataFv+0x158>
     b28:	48 00 04 d0 	b       ff8 <run_task__16TObjCMAutoMkDataFv+0x60c>
     b2c:	2c 00 00 04 	cmpwi   r0,4
     b30:	40 80 04 c8 	bge     ff8 <run_task__16TObjCMAutoMkDataFv+0x60c>
     b34:	48 00 03 38 	b       e6c <run_task__16TObjCMAutoMkDataFv+0x480>
     b38:	38 00 00 01 	li      r0,1
     b3c:	90 1f 00 20 	stw     r0,32(r31)
     b40:	48 00 04 b8 	b       ff8 <run_task__16TObjCMAutoMkDataFv+0x60c>
     b44:	38 60 00 02 	li      r3,2
     b48:	48 00 00 01 	bl      b48 <run_task__16TObjCMAutoMkDataFv+0x15c>
			b48: R_PPC_REL24	creation_buttons_pressed__Fl
     b4c:	2c 03 00 00 	cmpwi   r3,0
     b50:	41 82 00 2c 	beq     b7c <run_task__16TObjCMAutoMkDataFv+0x190>
     b54:	3c 60 00 05 	lis     r3,5
     b58:	38 80 00 00 	li      r4,0
     b5c:	38 63 37 04 	addi    r3,r3,14084
     b60:	38 a0 00 00 	li      r5,0
     b64:	38 c0 00 00 	li      r6,0
     b68:	48 00 00 01 	bl      b68 <run_task__16TObjCMAutoMkDataFv+0x17c>
			b68: R_PPC_REL24	play_sound_effect
     b6c:	48 00 00 01 	bl      b6c <run_task__16TObjCMAutoMkDataFv+0x180>
			b6c: R_PPC_REL24	clear_task_state__14TObjCMMainMenuFv
     b70:	38 00 00 02 	li      r0,2
     b74:	90 1f 00 20 	stw     r0,32(r31)
     b78:	48 00 04 80 	b       ff8 <run_task__16TObjCMAutoMkDataFv+0x60c>
     b7c:	38 60 00 04 	li      r3,4
     b80:	48 00 00 01 	bl      b80 <run_task__16TObjCMAutoMkDataFv+0x194>
			b80: R_PPC_REL24	creation_buttons_pressed__Fl
     b84:	2c 03 00 00 	cmpwi   r3,0
     b88:	41 82 04 70 	beq     ff8 <run_task__16TObjCMAutoMkDataFv+0x60c>
     b8c:	80 7f 00 1c 	lwz     r3,28(r31)
     b90:	48 00 00 01 	bl      b90 <run_task__16TObjCMAutoMkDataFv+0x1a4>
			b90: R_PPC_REL24	get_display_index__12TCharaMakingFv
     b94:	1c a3 00 2c 	mulli   r5,r3,44
     b98:	80 7f 00 1c 	lwz     r3,28(r31)
     b9c:	3c 80 00 00 	lis     r4,0
			b9e: R_PPC_ADDR16_HA	class_appearance_table
     ba0:	3b a3 00 38 	addi    r29,r3,56
     ba4:	38 04 00 00 	addi    r0,r4,0
			ba6: R_PPC_ADDR16_LO	class_appearance_table
     ba8:	3b 80 00 00 	li      r28,0
     bac:	7f c0 2a 14 	add     r30,r0,r5
     bb0:	a8 1e 00 00 	lha     r0,0(r30)
     bb4:	2c 00 00 02 	cmpwi   r0,2
     bb8:	41 80 00 88 	blt     c40 <run_task__16TObjCMAutoMkDataFv+0x254>
     bbc:	48 00 00 01 	bl      bbc <run_task__16TObjCMAutoMkDataFv+0x1d0>
			bbc: R_PPC_REL24	rand
     bc0:	3c 80 43 30 	lis     r4,17200
     bc4:	a8 de 00 00 	lha     r6,0(r30)
     bc8:	6c 63 80 00 	xoris   r3,r3,32768
     bcc:	90 81 00 10 	stw     r4,16(r1)
     bd0:	3c a0 00 00 	lis     r5,0
			bd2: R_PPC_ADDR16_HA	@268
     bd4:	6c c0 80 00 	xoris   r0,r6,32768
     bd8:	90 61 00 14 	stw     r3,20(r1)
     bdc:	c8 85 00 00 	lfd     f4,0(r5)
			bde: R_PPC_ADDR16_LO	@268
     be0:	c8 01 00 10 	lfd     f0,16(r1)
     be4:	90 01 00 1c 	stw     r0,28(r1)
     be8:	ec 60 20 28 	fsubs   f3,f0,f4
     bec:	c0 40 00 00 	lfs     f2,0(0)
			bec: R_PPC_EMB_SDA21	lbl_805DDAF4
     bf0:	90 81 00 18 	stw     r4,24(r1)
     bf4:	c0 20 00 00 	lfs     f1,0(0)
			bf4: R_PPC_EMB_SDA21	lbl_805DDAF0
     bf8:	c8 01 00 18 	lfd     f0,24(r1)
     bfc:	ec 42 00 f2 	fmuls   f2,f2,f3
     c00:	a8 7d 00 00 	lha     r3,0(r29)
     c04:	ec 00 20 28 	fsubs   f0,f0,f4
     c08:	ec 01 00 32 	fmuls   f0,f1,f0
     c0c:	ec 00 00 b2 	fmuls   f0,f0,f2
     c10:	fc 00 00 1e 	fctiwz  f0,f0
     c14:	d8 01 00 20 	stfd    f0,32(r1)
     c18:	80 01 00 24 	lwz     r0,36(r1)
     c1c:	7c 04 07 34 	extsh   r4,r0
     c20:	48 00 00 14 	b       c34 <run_task__16TObjCMAutoMkDataFv+0x248>
     c24:	38 84 00 01 	addi    r4,r4,1
     c28:	7c 04 30 00 	cmpw    r4,r6
     c2c:	41 80 00 08 	blt     c34 <run_task__16TObjCMAutoMkDataFv+0x248>
     c30:	38 80 00 00 	li      r4,0
     c34:	7c 04 18 00 	cmpw    r4,r3
     c38:	41 82 ff ec 	beq     c24 <run_task__16TObjCMAutoMkDataFv+0x238>
     c3c:	b0 9d 00 00 	sth     r4,0(r29)
     c40:	3b 9c 00 01 	addi    r28,r28,1
     c44:	3b bd 00 02 	addi    r29,r29,2
     c48:	2c 1c 00 04 	cmpwi   r28,4
     c4c:	3b de 00 02 	addi    r30,r30,2
     c50:	40 81 ff 60 	ble     bb0 <run_task__16TObjCMAutoMkDataFv+0x1c4>
     c54:	48 00 00 01 	bl      c54 <run_task__16TObjCMAutoMkDataFv+0x268>
			c54: R_PPC_REL24	rand
     c58:	3c 80 43 30 	lis     r4,17200
     c5c:	6c 60 80 00 	xoris   r0,r3,32768
     c60:	a8 7f 00 28 	lha     r3,40(r31)
     c64:	3c a0 00 00 	lis     r5,0
			c66: R_PPC_ADDR16_HA	@268
     c68:	90 01 00 24 	stw     r0,36(r1)
     c6c:	38 03 00 40 	addi    r0,r3,64
     c70:	c8 85 00 00 	lfd     f4,0(r5)
			c72: R_PPC_ADDR16_LO	@268
     c74:	90 81 00 20 	stw     r4,32(r1)
     c78:	6c 00 80 00 	xoris   r0,r0,32768
     c7c:	c0 40 00 00 	lfs     f2,0(0)
			c7c: R_PPC_EMB_SDA21	lbl_805DDAF4
     c80:	c8 01 00 20 	lfd     f0,32(r1)
     c84:	90 01 00 1c 	stw     r0,28(r1)
     c88:	ec 60 20 28 	fsubs   f3,f0,f4
     c8c:	c0 20 00 00 	lfs     f1,0(0)
			c8c: R_PPC_EMB_SDA21	lbl_805DDAF8
     c90:	90 81 00 18 	stw     r4,24(r1)
     c94:	c8 01 00 18 	lfd     f0,24(r1)
     c98:	ec 42 00 f2 	fmuls   f2,f2,f3
     c9c:	ec 00 20 28 	fsubs   f0,f0,f4
     ca0:	ec 01 00 ba 	fmadds  f0,f1,f2,f0
     ca4:	fc 00 00 1e 	fctiwz  f0,f0
     ca8:	d8 01 00 10 	stfd    f0,16(r1)
     cac:	80 01 00 14 	lwz     r0,20(r1)
     cb0:	54 00 06 3e 	clrlwi  r0,r0,24
     cb4:	b0 1f 00 28 	sth     r0,40(r31)
     cb8:	48 00 00 01 	bl      cb8 <run_task__16TObjCMAutoMkDataFv+0x2cc>
			cb8: R_PPC_REL24	rand
     cbc:	3c 80 43 30 	lis     r4,17200
     cc0:	6c 60 80 00 	xoris   r0,r3,32768
     cc4:	a8 7f 00 2a 	lha     r3,42(r31)
     cc8:	3c a0 00 00 	lis     r5,0
			cca: R_PPC_ADDR16_HA	@268
     ccc:	90 01 00 2c 	stw     r0,44(r1)
     cd0:	38 03 00 40 	addi    r0,r3,64
     cd4:	c8 85 00 00 	lfd     f4,0(r5)
			cd6: R_PPC_ADDR16_LO	@268
     cd8:	90 81 00 28 	stw     r4,40(r1)
     cdc:	6c 00 80 00 	xoris   r0,r0,32768
     ce0:	c0 40 00 00 	lfs     f2,0(0)
			ce0: R_PPC_EMB_SDA21	lbl_805DDAF4
     ce4:	c8 01 00 28 	lfd     f0,40(r1)
     ce8:	90 01 00 34 	stw     r0,52(r1)
     cec:	ec 60 20 28 	fsubs   f3,f0,f4
     cf0:	c0 20 00 00 	lfs     f1,0(0)
			cf0: R_PPC_EMB_SDA21	lbl_805DDAF8
     cf4:	90 81 00 30 	stw     r4,48(r1)
     cf8:	c8 01 00 30 	lfd     f0,48(r1)
     cfc:	ec 42 00 f2 	fmuls   f2,f2,f3
     d00:	ec 00 20 28 	fsubs   f0,f0,f4
     d04:	ec 01 00 ba 	fmadds  f0,f1,f2,f0
     d08:	fc 00 00 1e 	fctiwz  f0,f0
     d0c:	d8 01 00 38 	stfd    f0,56(r1)
     d10:	80 01 00 3c 	lwz     r0,60(r1)
     d14:	54 00 06 3e 	clrlwi  r0,r0,24
     d18:	b0 1f 00 2a 	sth     r0,42(r31)
     d1c:	48 00 00 01 	bl      d1c <run_task__16TObjCMAutoMkDataFv+0x330>
			d1c: R_PPC_REL24	rand
     d20:	3c 80 43 30 	lis     r4,17200
     d24:	6c 60 80 00 	xoris   r0,r3,32768
     d28:	a8 7f 00 2c 	lha     r3,44(r31)
     d2c:	3c a0 00 00 	lis     r5,0
			d2e: R_PPC_ADDR16_HA	@268
     d30:	90 01 00 44 	stw     r0,68(r1)
     d34:	38 03 00 40 	addi    r0,r3,64
     d38:	c8 85 00 00 	lfd     f4,0(r5)
			d3a: R_PPC_ADDR16_LO	@268
     d3c:	90 81 00 40 	stw     r4,64(r1)
     d40:	6c 00 80 00 	xoris   r0,r0,32768
     d44:	c0 40 00 00 	lfs     f2,0(0)
			d44: R_PPC_EMB_SDA21	lbl_805DDAF4
     d48:	c8 01 00 40 	lfd     f0,64(r1)
     d4c:	90 01 00 4c 	stw     r0,76(r1)
     d50:	ec 60 20 28 	fsubs   f3,f0,f4
     d54:	c0 20 00 00 	lfs     f1,0(0)
			d54: R_PPC_EMB_SDA21	lbl_805DDAF8
     d58:	90 81 00 48 	stw     r4,72(r1)
     d5c:	c8 01 00 48 	lfd     f0,72(r1)
     d60:	ec 42 00 f2 	fmuls   f2,f2,f3
     d64:	ec 00 20 28 	fsubs   f0,f0,f4
     d68:	ec 01 00 ba 	fmadds  f0,f1,f2,f0
     d6c:	fc 00 00 1e 	fctiwz  f0,f0
     d70:	d8 01 00 50 	stfd    f0,80(r1)
     d74:	80 01 00 54 	lwz     r0,84(r1)
     d78:	54 00 06 3e 	clrlwi  r0,r0,24
     d7c:	b0 1f 00 2c 	sth     r0,44(r31)
     d80:	48 00 00 01 	bl      d80 <run_task__16TObjCMAutoMkDataFv+0x394>
			d80: R_PPC_REL24	rand
     d84:	6c 63 80 00 	xoris   r3,r3,32768
     d88:	3c 00 43 30 	lis     r0,17200
     d8c:	90 61 00 5c 	stw     r3,92(r1)
     d90:	3c 80 00 00 	lis     r4,0
			d92: R_PPC_ADDR16_HA	@268
     d94:	c8 24 00 00 	lfd     f1,0(r4)
			d96: R_PPC_ADDR16_LO	@268
     d98:	90 01 00 58 	stw     r0,88(r1)
     d9c:	c0 80 00 00 	lfs     f4,0(0)
			d9c: R_PPC_EMB_SDA21	lbl_805DDAF4
     da0:	c8 01 00 58 	lfd     f0,88(r1)
     da4:	c0 60 00 00 	lfs     f3,0(0)
			da4: R_PPC_EMB_SDA21	lbl_805DDAC8
     da8:	ec a0 08 28 	fsubs   f5,f0,f1
     dac:	c0 40 00 00 	lfs     f2,0(0)
			dac: R_PPC_EMB_SDA21	lbl_805DDAFC
     db0:	c0 1f 00 30 	lfs     f0,48(r31)
     db4:	c0 20 00 00 	lfs     f1,0(0)
			db4: R_PPC_EMB_SDA21	@56
     db8:	ec 84 01 72 	fmuls   f4,f4,f5
     dbc:	ec 43 11 3a 	fmadds  f2,f3,f4,f2
     dc0:	ec 00 10 2a 	fadds   f0,f0,f2
     dc4:	fc 00 08 40 	fcmpo   cr0,f0,f1
     dc8:	d0 1f 00 30 	stfs    f0,48(r31)
     dcc:	4c 41 13 82 	cror    eq,gt,eq
     dd0:	40 82 00 10 	bne     de0 <run_task__16TObjCMAutoMkDataFv+0x3f4>
     dd4:	c0 1f 00 30 	lfs     f0,48(r31)
     dd8:	ec 00 08 28 	fsubs   f0,f0,f1
     ddc:	d0 1f 00 30 	stfs    f0,48(r31)
     de0:	48 00 00 01 	bl      de0 <run_task__16TObjCMAutoMkDataFv+0x3f4>
			de0: R_PPC_REL24	rand
     de4:	6c 63 80 00 	xoris   r3,r3,32768
     de8:	3c 00 43 30 	lis     r0,17200
     dec:	90 61 00 5c 	stw     r3,92(r1)
     df0:	3c 80 00 00 	lis     r4,0
			df2: R_PPC_ADDR16_HA	@268
     df4:	c8 24 00 00 	lfd     f1,0(r4)
			df6: R_PPC_ADDR16_LO	@268
     df8:	90 01 00 58 	stw     r0,88(r1)
     dfc:	c0 80 00 00 	lfs     f4,0(0)
			dfc: R_PPC_EMB_SDA21	lbl_805DDAF4
     e00:	c8 01 00 58 	lfd     f0,88(r1)
     e04:	c0 60 00 00 	lfs     f3,0(0)
			e04: R_PPC_EMB_SDA21	lbl_805DDAC8
     e08:	ec a0 08 28 	fsubs   f5,f0,f1
     e0c:	c0 40 00 00 	lfs     f2,0(0)
			e0c: R_PPC_EMB_SDA21	lbl_805DDAFC
     e10:	c0 1f 00 34 	lfs     f0,52(r31)
     e14:	c0 20 00 00 	lfs     f1,0(0)
			e14: R_PPC_EMB_SDA21	@56
     e18:	ec 84 01 72 	fmuls   f4,f4,f5
     e1c:	ec 43 11 3a 	fmadds  f2,f3,f4,f2
     e20:	ec 00 10 2a 	fadds   f0,f0,f2
     e24:	fc 00 08 40 	fcmpo   cr0,f0,f1
     e28:	d0 1f 00 34 	stfs    f0,52(r31)
     e2c:	4c 41 13 82 	cror    eq,gt,eq
     e30:	40 82 00 10 	bne     e40 <run_task__16TObjCMAutoMkDataFv+0x454>
     e34:	c0 1f 00 34 	lfs     f0,52(r31)
     e38:	ec 00 08 28 	fsubs   f0,f0,f1
     e3c:	d0 1f 00 34 	stfs    f0,52(r31)
     e40:	3c 60 00 05 	lis     r3,5
     e44:	38 80 00 00 	li      r4,0
     e48:	38 63 2d 01 	addi    r3,r3,11521
     e4c:	38 a0 00 00 	li      r5,0
     e50:	38 c0 00 00 	li      r6,0
     e54:	48 00 00 01 	bl      e54 <run_task__16TObjCMAutoMkDataFv+0x468>
			e54: R_PPC_REL24	play_sound_effect
     e58:	38 60 00 00 	li      r3,0
     e5c:	38 00 00 03 	li      r0,3
     e60:	90 7f 00 24 	stw     r3,36(r31)
     e64:	90 1f 00 20 	stw     r0,32(r31)
     e68:	48 00 01 90 	b       ff8 <run_task__16TObjCMAutoMkDataFv+0x60c>
     e6c:	80 9f 00 24 	lwz     r4,36(r31)
     e70:	3c c0 43 30 	lis     r6,17200
     e74:	3c 60 00 00 	lis     r3,0
			e76: R_PPC_ADDR16_HA	@268
     e78:	90 c1 00 58 	stw     r6,88(r1)
     e7c:	38 04 00 01 	addi    r0,r4,1
     e80:	c8 43 00 00 	lfd     f2,0(r3)
			e82: R_PPC_ADDR16_LO	@268
     e84:	90 1f 00 24 	stw     r0,36(r31)
     e88:	c0 00 00 00 	lfs     f0,0(0)
			e88: R_PPC_EMB_SDA21	lbl_805DDB00
     e8c:	80 1f 00 24 	lwz     r0,36(r31)
     e90:	80 bf 00 1c 	lwz     r5,28(r31)
     e94:	6c 03 80 00 	xoris   r3,r0,32768
     e98:	a8 1f 00 28 	lha     r0,40(r31)
     e9c:	90 61 00 5c 	stw     r3,92(r1)
     ea0:	a8 85 00 42 	lha     r4,66(r5)
     ea4:	c8 21 00 58 	lfd     f1,88(r1)
     ea8:	7c 64 00 50 	subf    r3,r4,r0
     eac:	6c 80 80 00 	xoris   r0,r4,32768
     eb0:	ec 21 10 28 	fsubs   f1,f1,f2
     eb4:	6c 63 80 00 	xoris   r3,r3,32768
     eb8:	90 61 00 54 	stw     r3,84(r1)
     ebc:	ec 61 00 24 	fdivs   f3,f1,f0
     ec0:	90 c1 00 50 	stw     r6,80(r1)
     ec4:	c8 21 00 50 	lfd     f1,80(r1)
     ec8:	90 01 00 4c 	stw     r0,76(r1)
     ecc:	90 c1 00 48 	stw     r6,72(r1)
     ed0:	c8 01 00 48 	lfd     f0,72(r1)
     ed4:	ec 21 10 28 	fsubs   f1,f1,f2
     ed8:	90 c1 00 38 	stw     r6,56(r1)
     edc:	ec 00 10 28 	fsubs   f0,f0,f2
     ee0:	90 c1 00 30 	stw     r6,48(r1)
     ee4:	ec 03 00 7a 	fmadds  f0,f3,f1,f0
     ee8:	90 c1 00 20 	stw     r6,32(r1)
     eec:	90 c1 00 18 	stw     r6,24(r1)
     ef0:	fc 00 00 1e 	fctiwz  f0,f0
     ef4:	d8 01 00 40 	stfd    f0,64(r1)
     ef8:	80 01 00 44 	lwz     r0,68(r1)
     efc:	b0 05 00 42 	sth     r0,66(r5)
     f00:	80 bf 00 1c 	lwz     r5,28(r31)
     f04:	a8 1f 00 2a 	lha     r0,42(r31)
     f08:	a8 85 00 44 	lha     r4,68(r5)
     f0c:	7c 64 00 50 	subf    r3,r4,r0
     f10:	6c 80 80 00 	xoris   r0,r4,32768
     f14:	6c 63 80 00 	xoris   r3,r3,32768
     f18:	90 01 00 34 	stw     r0,52(r1)
     f1c:	90 61 00 3c 	stw     r3,60(r1)
     f20:	c8 01 00 30 	lfd     f0,48(r1)
     f24:	c8 21 00 38 	lfd     f1,56(r1)
     f28:	ec 00 10 28 	fsubs   f0,f0,f2
     f2c:	ec 21 10 28 	fsubs   f1,f1,f2
     f30:	ec 03 00 7a 	fmadds  f0,f3,f1,f0
     f34:	fc 00 00 1e 	fctiwz  f0,f0
     f38:	d8 01 00 28 	stfd    f0,40(r1)
     f3c:	80 01 00 2c 	lwz     r0,44(r1)
     f40:	b0 05 00 44 	sth     r0,68(r5)
     f44:	80 bf 00 1c 	lwz     r5,28(r31)
     f48:	a8 1f 00 2c 	lha     r0,44(r31)
     f4c:	a8 85 00 46 	lha     r4,70(r5)
     f50:	7c 64 00 50 	subf    r3,r4,r0
     f54:	6c 80 80 00 	xoris   r0,r4,32768
     f58:	6c 63 80 00 	xoris   r3,r3,32768
     f5c:	90 01 00 1c 	stw     r0,28(r1)
     f60:	90 61 00 24 	stw     r3,36(r1)
     f64:	c8 01 00 18 	lfd     f0,24(r1)
     f68:	c8 21 00 20 	lfd     f1,32(r1)
     f6c:	ec 00 10 28 	fsubs   f0,f0,f2
     f70:	ec 21 10 28 	fsubs   f1,f1,f2
     f74:	ec 03 00 7a 	fmadds  f0,f3,f1,f0
     f78:	fc 00 00 1e 	fctiwz  f0,f0
     f7c:	d8 01 00 10 	stfd    f0,16(r1)
     f80:	80 01 00 14 	lwz     r0,20(r1)
     f84:	b0 05 00 46 	sth     r0,70(r5)
     f88:	80 7f 00 1c 	lwz     r3,28(r31)
     f8c:	c0 1f 00 30 	lfs     f0,48(r31)
     f90:	c0 23 00 48 	lfs     f1,72(r3)
     f94:	ec 00 08 28 	fsubs   f0,f0,f1
     f98:	ec 03 08 3a 	fmadds  f0,f3,f0,f1
     f9c:	d0 03 00 48 	stfs    f0,72(r3)
     fa0:	80 7f 00 1c 	lwz     r3,28(r31)
     fa4:	c0 1f 00 34 	lfs     f0,52(r31)
     fa8:	c0 23 00 4c 	lfs     f1,76(r3)
     fac:	ec 00 08 28 	fsubs   f0,f0,f1
     fb0:	ec 03 08 3a 	fmadds  f0,f3,f0,f1
     fb4:	d0 03 00 4c 	stfs    f0,76(r3)
     fb8:	80 7f 00 24 	lwz     r3,36(r31)
     fbc:	2c 03 00 1e 	cmpwi   r3,30
     fc0:	41 80 00 38 	blt     ff8 <run_task__16TObjCMAutoMkDataFv+0x60c>
     fc4:	80 00 00 00 	lwz     r0,0(0)
			fc4: R_PPC_EMB_SDA21	creation_resource_ready_state
     fc8:	2c 00 00 02 	cmpwi   r0,2
     fcc:	40 82 00 28 	bne     ff4 <run_task__16TObjCMAutoMkDataFv+0x608>
     fd0:	3c 60 00 05 	lis     r3,5
     fd4:	38 80 00 00 	li      r4,0
     fd8:	38 63 28 02 	addi    r3,r3,10242
     fdc:	38 a0 00 00 	li      r5,0
     fe0:	38 c0 00 00 	li      r6,0
     fe4:	48 00 00 01 	bl      fe4 <run_task__16TObjCMAutoMkDataFv+0x5f8>
			fe4: R_PPC_REL24	play_sound_effect
     fe8:	38 00 00 01 	li      r0,1
     fec:	90 1f 00 20 	stw     r0,32(r31)
     ff0:	48 00 00 08 	b       ff8 <run_task__16TObjCMAutoMkDataFv+0x60c>
     ff4:	2c 03 00 96 	cmpwi   r3,150
     ff8:	bb 81 00 60 	lmw     r28,96(r1)
     ffc:	80 01 00 74 	lwz     r0,116(r1)
    1000:	7c 08 03 a6 	mtlr    r0
    1004:	38 21 00 70 	addi    r1,r1,112
    1008:	4e 80 00 20 	blr

0000100c <create__16TObjCMAutoMkDataFPv>:
    100c:	94 21 ff f0 	stwu    r1,-16(r1)
    1010:	7c 08 02 a6 	mflr    r0
    1014:	90 01 00 14 	stw     r0,20(r1)
    1018:	93 e1 00 0c 	stw     r31,12(r1)
    101c:	7c 7f 1b 78 	mr      r31,r3
    1020:	38 60 00 3c 	li      r3,60
    1024:	48 00 00 01 	bl      1024 <create__16TObjCMAutoMkDataFPv+0x18>
			1024: R_PPC_REL24	__nw__7TObjectFUl
    1028:	7c 60 1b 79 	mr.     r0,r3
    102c:	41 82 00 10 	beq     103c <create__16TObjCMAutoMkDataFPv+0x30>
    1030:	7f e4 fb 78 	mr      r4,r31
    1034:	48 00 00 01 	bl      1034 <create__16TObjCMAutoMkDataFPv+0x28>
			1034: R_PPC_REL24	TObjCMAutoMkData__ct
    1038:	7c 60 1b 78 	mr      r0,r3
    103c:	7c 03 03 78 	mr      r3,r0
    1040:	80 01 00 14 	lwz     r0,20(r1)
    1044:	83 e1 00 0c 	lwz     r31,12(r1)
    1048:	7c 08 03 a6 	mtlr    r0
    104c:	38 21 00 10 	addi    r1,r1,16
    1050:	4e 80 00 20 	blr

00001054 <__dt__16TObjCMAutoMkDataFv>:
    1054:	94 21 ff f0 	stwu    r1,-16(r1)
    1058:	7c 08 02 a6 	mflr    r0
    105c:	90 01 00 14 	stw     r0,20(r1)
    1060:	bf c1 00 08 	stmw    r30,8(r1)
    1064:	7c 7e 1b 79 	mr.     r30,r3
    1068:	7c 9f 23 78 	mr      r31,r4
    106c:	41 82 00 34 	beq     10a0 <__dt__16TObjCMAutoMkDataFv+0x4c>
    1070:	3c 60 00 00 	lis     r3,0
			1072: R_PPC_ADDR16_HA	__vt__16TObjCMAutoMkData
    1074:	c0 20 00 00 	lfs     f1,0(0)
			1074: R_PPC_EMB_SDA21	lbl_805DDA70
    1078:	38 03 00 00 	addi    r0,r3,0
			107a: R_PPC_ADDR16_LO	__vt__16TObjCMAutoMkData
    107c:	90 1e 00 18 	stw     r0,24(r30)
    1080:	48 00 00 01 	bl      1080 <__dt__16TObjCMAutoMkDataFv+0x2c>
			1080: R_PPC_REL24	set_creation_projection_center__Ff
    1084:	7f c3 f3 78 	mr      r3,r30
    1088:	38 80 00 00 	li      r4,0
    108c:	48 00 00 01 	bl      108c <__dt__16TObjCMAutoMkDataFv+0x38>
			108c: R_PPC_REL24	__dt__7TObjectFv
    1090:	7f e0 07 35 	extsh.  r0,r31
    1094:	40 81 00 0c 	ble     10a0 <__dt__16TObjCMAutoMkDataFv+0x4c>
    1098:	7f c3 f3 78 	mr      r3,r30
    109c:	48 00 00 01 	bl      109c <__dt__16TObjCMAutoMkDataFv+0x48>
			109c: R_PPC_REL24	__dl__7TObjectFPv
    10a0:	7f c3 f3 78 	mr      r3,r30
    10a4:	bb c1 00 08 	lmw     r30,8(r1)
    10a8:	80 01 00 14 	lwz     r0,20(r1)
    10ac:	7c 08 03 a6 	mtlr    r0
    10b0:	38 21 00 10 	addi    r1,r1,16
    10b4:	4e 80 00 20 	blr

000010b8 <TObjCMAutoMkData__ct>:
    10b8:	94 21 ff f0 	stwu    r1,-16(r1)
    10bc:	7c 08 02 a6 	mflr    r0
    10c0:	90 01 00 14 	stw     r0,20(r1)
    10c4:	93 e1 00 0c 	stw     r31,12(r1)
    10c8:	7c 7f 1b 78 	mr      r31,r3
    10cc:	48 00 00 01 	bl      10cc <TObjCMAutoMkData__ct+0x14>
			10cc: R_PPC_REL24	__ct__7TObjectFP7TObject
    10d0:	3c 80 00 00 	lis     r4,0
			10d2: R_PPC_ADDR16_HA	__vt__16TObjCMAutoMkData
    10d4:	38 7f 00 30 	addi    r3,r31,48
    10d8:	38 04 00 00 	addi    r0,r4,0
			10da: R_PPC_ADDR16_LO	__vt__16TObjCMAutoMkData
    10dc:	90 1f 00 18 	stw     r0,24(r31)
    10e0:	80 00 00 00 	lwz     r0,0(0)
			10e0: R_PPC_EMB_SDA21	lbl_805D3CE4
    10e4:	90 1f 00 00 	stw     r0,0(r31)
    10e8:	80 00 00 00 	lwz     r0,0(0)
			10e8: R_PPC_EMB_SDA21	creation_player_character
    10ec:	90 1f 00 1c 	stw     r0,28(r31)
    10f0:	80 9f 00 1c 	lwz     r4,28(r31)
    10f4:	38 84 00 48 	addi    r4,r4,72
    10f8:	48 00 00 01 	bl      10f8 <TObjCMAutoMkData__ct+0x40>
			10f8: R_PPC_REL24	copy_vec2__28TWindowSubSymbolChatPartsSetFPv
    10fc:	c0 00 00 00 	lfs     f0,0(0)
			10fc: R_PPC_EMB_SDA21	lbl_805DDA90
    1100:	38 00 00 00 	li      r0,0
    1104:	38 60 00 0b 	li      r3,11
    1108:	d0 1f 00 38 	stfs    f0,56(r31)
    110c:	90 1f 00 20 	stw     r0,32(r31)
    1110:	48 00 00 01 	bl      1110 <TObjCMAutoMkData__ct+0x58>
			1110: R_PPC_REL24	set_eff_tag__11TChCrEffTagFi
    1114:	80 01 00 14 	lwz     r0,20(r1)
    1118:	7f e3 fb 78 	mr      r3,r31
    111c:	83 e1 00 0c 	lwz     r31,12(r1)
    1120:	7c 08 03 a6 	mtlr    r0
    1124:	38 21 00 10 	addi    r1,r1,16
    1128:	4e 80 00 20 	blr

0000112c <render__14TObjCMHairMenuFv>:
    112c:	94 21 fe c0 	stwu    r1,-320(r1)
    1130:	7c 08 02 a6 	mflr    r0
    1134:	90 01 01 44 	stw     r0,324(r1)
    1138:	db e1 01 30 	stfd    f31,304(r1)
    113c:	f3 e1 01 38 	xxsel   vs31,vs1,vs0,vs36
    1140:	db c1 01 20 	stfd    f30,288(r1)
    1144:	f3 c1 01 28 	psq_st  f30,296(r1),0,0
    1148:	db a1 01 10 	stfd    f29,272(r1)
    114c:	f3 a1 01 18 	psq_st  f29,280(r1),0,0
    1150:	db 81 01 00 	stfd    f28,256(r1)
    1154:	f3 81 01 08 	xsmaddadp vs28,vs1,vs0
    1158:	db 61 00 f0 	stfd    f27,240(r1)
    115c:	f3 61 00 f8 	xxsel   vs27,vs1,vs0,vs35
    1160:	db 41 00 e0 	stfd    f26,224(r1)
    1164:	f3 41 00 e8 	psq_st  f26,232(r1),0,0
    1168:	db 21 00 d0 	stfd    f25,208(r1)
    116c:	f3 21 00 d8 	psq_st  f25,216(r1),0,0
    1170:	db 01 00 c0 	stfd    f24,192(r1)
    1174:	f3 01 00 c8 	xsmsubmsp vs24,vs1,vs0
    1178:	da e1 00 b0 	stfd    f23,176(r1)
    117c:	f2 e1 00 b8 	xxsel   vs23,vs1,vs0,vs34
    1180:	be e1 00 8c 	stmw    r23,140(r1)
    1184:	7c 79 1b 78 	mr      r25,r3
    1188:	80 63 00 1c 	lwz     r3,28(r3)
    118c:	80 19 00 2c 	lwz     r0,44(r25)
    1190:	ab 63 00 40 	lha     r27,64(r3)
    1194:	54 03 50 2a 	slwi    r3,r0,10
    1198:	48 00 00 01 	bl      1198 <render__14TObjCMHairMenuFv+0x6c>
			1198: R_PPC_REL24	sin_table_lookup
    119c:	c0 40 00 00 	lfs     f2,0(0)
			119c: R_PPC_EMB_SDA21	@407
    11a0:	c0 00 00 00 	lfs     f0,0(0)
			11a0: R_PPC_EMB_SDA21	@56
    11a4:	ef a2 00 7a 	fmadds  f29,f2,f1,f0
    11a8:	fc 1d 00 40 	fcmpo   cr0,f29,f0
    11ac:	40 81 00 08 	ble     11b4 <render__14TObjCMHairMenuFv+0x88>
    11b0:	ff a0 00 90 	fmr     f29,f0
    11b4:	80 79 00 28 	lwz     r3,40(r25)
    11b8:	34 03 ff ff 	addic.  r0,r3,-1
    11bc:	40 80 00 0c 	bge     11c8 <render__14TObjCMHairMenuFv+0x9c>
    11c0:	38 00 00 00 	li      r0,0
    11c4:	48 00 00 10 	b       11d4 <render__14TObjCMHairMenuFv+0xa8>
    11c8:	2c 00 00 0a 	cmpwi   r0,10
    11cc:	41 80 00 08 	blt     11d4 <render__14TObjCMHairMenuFv+0xa8>
    11d0:	38 00 00 09 	li      r0,9
    11d4:	c0 59 00 34 	lfs     f2,52(r25)
    11d8:	3c 60 00 00 	lis     r3,0
			11da: R_PPC_ADDR16_HA	lbl_8046509C
    11dc:	c0 20 00 00 	lfs     f1,0(0)
			11dc: R_PPC_EMB_SDA21	@85
    11e0:	54 00 10 3a 	slwi    r0,r0,2
    11e4:	38 63 00 00 	addi    r3,r3,0
			11e6: R_PPC_ADDR16_LO	lbl_8046509C
    11e8:	fc 02 08 40 	fcmpo   cr0,f2,f1
    11ec:	7f 83 04 2e 	lfsx    f28,r3,r0
    11f0:	4c 40 13 82 	cror    eq,lt,eq
    11f4:	41 82 01 08 	beq     12fc <render__14TObjCMHairMenuFv+0x1d0>
    11f8:	c0 00 00 00 	lfs     f0,0(0)
			11f8: R_PPC_EMB_SDA21	@86
    11fc:	fc 02 00 40 	fcmpo   cr0,f2,f0
    1200:	4c 41 13 82 	cror    eq,gt,eq
    1204:	40 82 00 0c 	bne     1210 <render__14TObjCMHairMenuFv+0xe4>
    1208:	c3 40 00 00 	lfs     f26,0(0)
			1208: R_PPC_EMB_SDA21	@56
    120c:	48 00 00 0c 	b       1218 <render__14TObjCMHairMenuFv+0xec>
    1210:	ec 02 08 28 	fsubs   f0,f2,f1
    1214:	ef 40 08 24 	fdivs   f26,f0,f1
    1218:	c3 c0 00 00 	lfs     f30,0(0)
			1218: R_PPC_EMB_SDA21	@118
    121c:	3b 00 00 00 	li      r24,0
    1220:	c3 e0 00 00 	lfs     f31,0(0)
			1220: R_PPC_EMB_SDA21	@56
    1224:	3a e0 00 00 	li      r23,0
    1228:	ec 1c f0 28 	fsubs   f0,f28,f30
    122c:	c0 20 00 00 	lfs     f1,0(0)
			122c: R_PPC_EMB_SDA21	@408
    1230:	d3 e1 00 2c 	stfs    f31,44(r1)
    1234:	c3 00 00 00 	lfs     f24,0(0)
			1234: R_PPC_EMB_SDA21	@91
    1238:	ef 7a f0 3a 	fmadds  f27,f26,f0,f30
    123c:	d0 21 00 34 	stfs    f1,52(r1)
    1240:	c3 20 00 00 	lfs     f25,0(0)
			1240: R_PPC_EMB_SDA21	@409
    1244:	2c 18 00 00 	cmpwi   r24,0
    1248:	3b 40 00 00 	li      r26,0
    124c:	40 82 00 0c 	bne     1258 <render__14TObjCMHairMenuFv+0x12c>
    1250:	fe e0 d8 90 	fmr     f23,f27
    1254:	48 00 00 1c 	b       1270 <render__14TObjCMHairMenuFv+0x144>
    1258:	3c 60 00 00 	lis     r3,0
			125a: R_PPC_ADDR16_HA	lbl_804650C4
    125c:	c0 20 00 00 	lfs     f1,0(0)
			125c: R_PPC_EMB_SDA21	@118
    1260:	38 63 00 00 	addi    r3,r3,0
			1262: R_PPC_ADDR16_LO	lbl_804650C4
    1264:	7c 03 bc 2e 	lfsx    f0,r3,r23
    1268:	ec 00 08 28 	fsubs   f0,f0,f1
    126c:	ee fa 08 3a 	fmadds  f23,f26,f0,f1
    1270:	d3 c1 00 30 	stfs    f30,48(r1)
    1274:	80 19 00 24 	lwz     r0,36(r25)
    1278:	7c 18 00 00 	cmpw    r24,r0
    127c:	40 82 00 24 	bne     12a0 <render__14TObjCMHairMenuFv+0x174>
    1280:	80 19 00 2c 	lwz     r0,44(r25)
    1284:	3b 40 00 02 	li      r26,2
    1288:	54 03 50 2a 	slwi    r3,r0,10
    128c:	48 00 00 01 	bl      128c <render__14TObjCMHairMenuFv+0x160>
			128c: R_PPC_REL24	sin_table_lookup
    1290:	c0 40 00 00 	lfs     f2,0(0)
			1290: R_PPC_EMB_SDA21	@90
    1294:	c0 01 00 30 	lfs     f0,48(r1)
    1298:	ec 02 00 7a 	fmadds  f0,f2,f1,f0
    129c:	d0 01 00 30 	stfs    f0,48(r1)
    12a0:	c0 01 00 30 	lfs     f0,48(r1)
    12a4:	38 7a 00 06 	addi    r3,r26,6
    12a8:	c0 20 00 00 	lfs     f1,0(0)
			12a8: R_PPC_EMB_SDA21	@92
    12ac:	38 81 00 30 	addi    r4,r1,48
    12b0:	ec 17 00 28 	fsubs   f0,f23,f0
    12b4:	38 a1 00 28 	addi    r5,r1,40
    12b8:	ec 00 c0 24 	fdivs   f0,f0,f24
    12bc:	d0 01 00 28 	stfs    f0,40(r1)
    12c0:	48 00 00 01 	bl      12c0 <render__14TObjCMHairMenuFv+0x194>
			12c0: R_PPC_REL24	draw_ui_sprite_opaque
    12c4:	d2 e1 00 30 	stfs    f23,48(r1)
    12c8:	38 7a 00 07 	addi    r3,r26,7
    12cc:	c0 20 00 00 	lfs     f1,0(0)
			12cc: R_PPC_EMB_SDA21	@92
    12d0:	38 81 00 30 	addi    r4,r1,48
    12d4:	d3 e1 00 28 	stfs    f31,40(r1)
    12d8:	38 a1 00 28 	addi    r5,r1,40
    12dc:	48 00 00 01 	bl      12dc <render__14TObjCMHairMenuFv+0x1b0>
			12dc: R_PPC_REL24	draw_ui_sprite_opaque
    12e0:	c0 01 00 34 	lfs     f0,52(r1)
    12e4:	3b 18 00 01 	addi    r24,r24,1
    12e8:	2c 18 00 04 	cmpwi   r24,4
    12ec:	3a f7 00 04 	addi    r23,r23,4
    12f0:	ec 00 c8 2a 	fadds   f0,f0,f25
    12f4:	d0 01 00 34 	stfs    f0,52(r1)
    12f8:	41 80 ff 4c 	blt     1244 <render__14TObjCMHairMenuFv+0x118>
    12fc:	c0 39 00 34 	lfs     f1,52(r25)
    1300:	c0 00 00 00 	lfs     f0,0(0)
			1300: R_PPC_EMB_SDA21	@54
    1304:	fc 01 00 40 	fcmpo   cr0,f1,f0
    1308:	4c 40 13 82 	cror    eq,lt,eq
    130c:	41 82 00 78 	beq     1384 <render__14TObjCMHairMenuFv+0x258>
    1310:	c0 00 00 00 	lfs     f0,0(0)
			1310: R_PPC_EMB_SDA21	@86
    1314:	fc 01 00 40 	fcmpo   cr0,f1,f0
    1318:	4c 41 13 82 	cror    eq,gt,eq
    131c:	40 82 00 0c 	bne     1328 <render__14TObjCMHairMenuFv+0x1fc>
    1320:	c2 e0 00 00 	lfs     f23,0(0)
			1320: R_PPC_EMB_SDA21	@56
    1324:	48 00 00 08 	b       132c <render__14TObjCMHairMenuFv+0x200>
    1328:	ee e1 00 24 	fdivs   f23,f1,f0
    132c:	c0 20 00 00 	lfs     f1,0(0)
			132c: R_PPC_EMB_SDA21	@410
    1330:	3a e0 00 00 	li      r23,0
    1334:	c0 00 00 00 	lfs     f0,0(0)
			1334: R_PPC_EMB_SDA21	@408
    1338:	d0 21 00 20 	stfs    f1,32(r1)
    133c:	c3 40 00 00 	lfs     f26,0(0)
			133c: R_PPC_EMB_SDA21	@409
    1340:	d0 01 00 24 	stfs    f0,36(r1)
    1344:	80 19 00 24 	lwz     r0,36(r25)
    1348:	38 60 00 00 	li      r3,0
    134c:	7c 17 00 00 	cmpw    r23,r0
    1350:	40 82 00 08 	bne     1358 <render__14TObjCMHairMenuFv+0x22c>
    1354:	38 60 ff ff 	li      r3,-1
    1358:	fc 40 b8 90 	fmr     f2,f23
    135c:	c0 20 00 00 	lfs     f1,0(0)
			135c: R_PPC_EMB_SDA21	@93
    1360:	38 63 00 01 	addi    r3,r3,1
    1364:	38 81 00 20 	addi    r4,r1,32
    1368:	48 00 00 01 	bl      1368 <render__14TObjCMHairMenuFv+0x23c>
			1368: R_PPC_REL24	draw_ui_sprite
    136c:	c0 01 00 24 	lfs     f0,36(r1)
    1370:	3a f7 00 01 	addi    r23,r23,1
    1374:	2c 17 00 04 	cmpwi   r23,4
    1378:	ec 00 d0 2a 	fadds   f0,f0,f26
    137c:	d0 01 00 24 	stfs    f0,36(r1)
    1380:	41 80 ff c4 	blt     1344 <render__14TObjCMHairMenuFv+0x218>
    1384:	c0 39 00 34 	lfs     f1,52(r25)
    1388:	c0 00 00 00 	lfs     f0,0(0)
			1388: R_PPC_EMB_SDA21	@86
    138c:	fc 01 00 40 	fcmpo   cr0,f1,f0
    1390:	4c 40 13 82 	cror    eq,lt,eq
    1394:	41 82 04 6c 	beq     1800 <render__14TObjCMHairMenuFv+0x6d4>
    1398:	ec 61 00 28 	fsubs   f3,f1,f0
    139c:	c0 00 00 00 	lfs     f0,0(0)
			139c: R_PPC_EMB_SDA21	@411
    13a0:	c0 40 00 00 	lfs     f2,0(0)
			13a0: R_PPC_EMB_SDA21	@412
    13a4:	3a e0 00 00 	li      r23,0
    13a8:	c0 20 00 00 	lfs     f1,0(0)
			13a8: R_PPC_EMB_SDA21	@122
    13ac:	ef e3 00 24 	fdivs   f31,f3,f0
    13b0:	c0 00 00 00 	lfs     f0,0(0)
			13b0: R_PPC_EMB_SDA21	@413
    13b4:	d0 41 00 18 	stfs    f2,24(r1)
    13b8:	c3 40 00 00 	lfs     f26,0(0)
			13b8: R_PPC_EMB_SDA21	@415
    13bc:	d0 21 00 1c 	stfs    f1,28(r1)
    13c0:	ef 7f 07 f2 	fmuls   f27,f31,f31
    13c4:	ef 00 06 f2 	fmuls   f24,f0,f27
    13c8:	48 00 00 88 	b       1450 <render__14TObjCMHairMenuFv+0x324>
    13cc:	80 19 00 24 	lwz     r0,36(r25)
    13d0:	fe e0 d8 90 	fmr     f23,f27
    13d4:	2c 00 00 00 	cmpwi   r0,0
    13d8:	41 82 00 08 	beq     13e0 <render__14TObjCMHairMenuFv+0x2b4>
    13dc:	fe e0 c0 90 	fmr     f23,f24
    13e0:	7c 17 d8 00 	cmpw    r23,r27
    13e4:	3b 00 00 1f 	li      r24,31
    13e8:	40 82 00 44 	bne     142c <render__14TObjCMHairMenuFv+0x300>
    13ec:	80 00 00 00 	lwz     r0,0(0)
			13ec: R_PPC_EMB_SDA21	creation_resource_ready_state
    13f0:	3b 00 00 20 	li      r24,32
    13f4:	2c 00 00 02 	cmpwi   r0,2
    13f8:	41 82 00 24 	beq     141c <render__14TObjCMHairMenuFv+0x2f0>
    13fc:	80 19 00 2c 	lwz     r0,44(r25)
    1400:	54 03 60 26 	slwi    r3,r0,12
    1404:	48 00 00 01 	bl      1404 <render__14TObjCMHairMenuFv+0x2d8>
			1404: R_PPC_REL24	sin_table_lookup
    1408:	48 00 00 01 	bl      1408 <render__14TObjCMHairMenuFv+0x2dc>
			1408: R_PPC_REL24	fabs_float
    140c:	c0 00 00 00 	lfs     f0,0(0)
			140c: R_PPC_EMB_SDA21	@414
    1410:	ec 00 00 7a 	fmadds  f0,f0,f1,f0
    1414:	ee f7 00 32 	fmuls   f23,f23,f0
    1418:	48 00 00 14 	b       142c <render__14TObjCMHairMenuFv+0x300>
    141c:	80 19 00 24 	lwz     r0,36(r25)
    1420:	2c 00 00 00 	cmpwi   r0,0
    1424:	40 82 00 08 	bne     142c <render__14TObjCMHairMenuFv+0x300>
    1428:	ee f7 07 72 	fmuls   f23,f23,f29
    142c:	fc 40 b8 90 	fmr     f2,f23
    1430:	c0 20 00 00 	lfs     f1,0(0)
			1430: R_PPC_EMB_SDA21	@93
    1434:	7f 03 c3 78 	mr      r3,r24
    1438:	38 81 00 18 	addi    r4,r1,24
    143c:	48 00 00 01 	bl      143c <render__14TObjCMHairMenuFv+0x310>
			143c: R_PPC_REL24	draw_ui_sprite
    1440:	c0 01 00 18 	lfs     f0,24(r1)
    1444:	3a f7 00 01 	addi    r23,r23,1
    1448:	ec 00 d0 2a 	fadds   f0,f0,f26
    144c:	d0 01 00 18 	stfs    f0,24(r1)
    1450:	80 19 00 28 	lwz     r0,40(r25)
    1454:	7c 17 00 00 	cmpw    r23,r0
    1458:	41 80 ff 74 	blt     13cc <render__14TObjCMHairMenuFv+0x2a0>
    145c:	c0 00 00 00 	lfs     f0,0(0)
			145c: R_PPC_EMB_SDA21	@416
    1460:	fe e0 d8 90 	fmr     f23,f27
    1464:	80 19 00 24 	lwz     r0,36(r25)
    1468:	ef 1c 00 28 	fsubs   f24,f28,f0
    146c:	2c 00 00 00 	cmpwi   r0,0
    1470:	40 82 00 0c 	bne     147c <render__14TObjCMHairMenuFv+0x350>
    1474:	ec 5b 07 72 	fmuls   f2,f27,f29
    1478:	48 00 00 10 	b       1488 <render__14TObjCMHairMenuFv+0x35c>
    147c:	c0 00 00 00 	lfs     f0,0(0)
			147c: R_PPC_EMB_SDA21	@413
    1480:	ec 40 06 f2 	fmuls   f2,f0,f27
    1484:	fe e0 10 90 	fmr     f23,f2
    1488:	c0 20 00 00 	lfs     f1,0(0)
			1488: R_PPC_EMB_SDA21	@417
    148c:	38 7b 00 14 	addi    r3,r27,20
    1490:	c0 00 00 00 	lfs     f0,0(0)
			1490: R_PPC_EMB_SDA21	@418
    1494:	38 81 00 10 	addi    r4,r1,16
    1498:	ec 61 c0 2a 	fadds   f3,f1,f24
    149c:	c0 20 00 00 	lfs     f1,0(0)
			149c: R_PPC_EMB_SDA21	@93
    14a0:	d0 01 00 14 	stfs    f0,20(r1)
    14a4:	d0 61 00 10 	stfs    f3,16(r1)
    14a8:	48 00 00 01 	bl      14a8 <render__14TObjCMHairMenuFv+0x37c>
			14a8: R_PPC_REL24	draw_ui_sprite
    14ac:	c0 00 00 00 	lfs     f0,0(0)
			14ac: R_PPC_EMB_SDA21	@419
    14b0:	fc 40 b8 90 	fmr     f2,f23
    14b4:	c0 20 00 00 	lfs     f1,0(0)
			14b4: R_PPC_EMB_SDA21	@93
    14b8:	38 81 00 10 	addi    r4,r1,16
    14bc:	ec 00 c0 2a 	fadds   f0,f0,f24
    14c0:	38 60 00 1e 	li      r3,30
    14c4:	d0 01 00 10 	stfs    f0,16(r1)
    14c8:	48 00 00 01 	bl      14c8 <render__14TObjCMHairMenuFv+0x39c>
			14c8: R_PPC_REL24	draw_ui_sprite
    14cc:	c0 20 00 00 	lfs     f1,0(0)
			14cc: R_PPC_EMB_SDA21	@420
    14d0:	fc 40 b8 90 	fmr     f2,f23
    14d4:	c0 00 00 00 	lfs     f0,0(0)
			14d4: R_PPC_EMB_SDA21	@421
    14d8:	38 81 00 10 	addi    r4,r1,16
    14dc:	ec 61 c0 2a 	fadds   f3,f1,f24
    14e0:	c0 20 00 00 	lfs     f1,0(0)
			14e0: R_PPC_EMB_SDA21	@93
    14e4:	d0 01 00 14 	stfs    f0,20(r1)
    14e8:	d0 61 00 10 	stfs    f3,16(r1)
    14ec:	80 79 00 28 	lwz     r3,40(r25)
    14f0:	38 63 00 13 	addi    r3,r3,19
    14f4:	48 00 00 01 	bl      14f4 <render__14TObjCMHairMenuFv+0x3c8>
			14f4: R_PPC_REL24	draw_ui_sprite
    14f8:	c0 00 00 00 	lfs     f0,0(0)
			14f8: R_PPC_EMB_SDA21	@413
    14fc:	3c 60 00 00 	lis     r3,0
			14fe: R_PPC_ADDR16_HA	lbl_804DBCD0
    1500:	ef 1b 07 72 	fmuls   f24,f27,f29
    1504:	c3 40 00 00 	lfs     f26,0(0)
			1504: R_PPC_EMB_SDA21	@122
    1508:	ef 20 06 f2 	fmuls   f25,f0,f27
    150c:	3a e3 00 00 	addi    r23,r3,0
			150e: R_PPC_ADDR16_LO	lbl_804DBCD0
    1510:	3b 00 00 01 	li      r24,1
    1514:	80 19 00 24 	lwz     r0,36(r25)
    1518:	7c 18 00 00 	cmpw    r24,r0
    151c:	40 82 00 0c 	bne     1528 <render__14TObjCMHairMenuFv+0x3fc>
    1520:	fc 40 c0 90 	fmr     f2,f24
    1524:	48 00 00 0c 	b       1530 <render__14TObjCMHairMenuFv+0x404>
    1528:	d3 41 00 14 	stfs    f26,20(r1)
    152c:	fc 40 c8 90 	fmr     f2,f25
    1530:	38 18 ff ff 	addi    r0,r24,-1
    1534:	c0 20 00 00 	lfs     f1,0(0)
			1534: R_PPC_EMB_SDA21	@93
    1538:	54 00 18 38 	slwi    r0,r0,3
    153c:	38 78 00 0f 	addi    r3,r24,15
    1540:	7c 97 02 14 	add     r4,r23,r0
    1544:	48 00 00 01 	bl      1544 <render__14TObjCMHairMenuFv+0x418>
			1544: R_PPC_REL24	draw_ui_sprite
    1548:	3b 18 00 01 	addi    r24,r24,1
    154c:	2c 18 00 04 	cmpwi   r24,4
    1550:	41 80 ff c4 	blt     1514 <render__14TObjCMHairMenuFv+0x3e8>
    1554:	48 00 00 01 	bl      1554 <render__14TObjCMHairMenuFv+0x428>
			1554: R_PPC_REL24	get_scale__14TObjCMMainMenuFv
    1558:	ff c0 08 90 	fmr     f30,f1
    155c:	48 00 00 01 	bl      155c <render__14TObjCMHairMenuFv+0x430>
			155c: R_PPC_REL24	restore_full_screen_view__11TCameraCtrlFv
    1560:	3c 60 00 00 	lis     r3,0
			1562: R_PPC_ADDR16_HA	lbl_804650D4
    1564:	c0 00 00 00 	lfs     f0,0(0)
			1564: R_PPC_EMB_SDA21	@424
    1568:	3b c3 00 00 	addi    r30,r3,0
			156a: R_PPC_ADDR16_LO	lbl_804650D4
    156c:	c0 20 00 00 	lfs     f1,0(0)
			156c: R_PPC_EMB_SDA21	@409
    1570:	c0 7e 00 0c 	lfs     f3,12(r30)
    1574:	ec 00 07 f2 	fmuls   f0,f0,f31
    1578:	c0 5e 00 04 	lfs     f2,4(r30)
    157c:	ef 41 07 b2 	fmuls   f26,f1,f30
    1580:	3c 60 00 00 	lis     r3,0
			1582: R_PPC_ADDR16_HA	lbl_804650F4
    1584:	38 e1 00 58 	addi    r7,r1,88
    1588:	ec 63 10 28 	fsubs   f3,f3,f2
    158c:	c0 e0 00 00 	lfs     f7,0(0)
			158c: R_PPC_EMB_SDA21	@423
    1590:	fc 00 00 1e 	fctiwz  f0,f0
    1594:	c1 00 00 00 	lfs     f8,0(0)
			1594: R_PPC_EMB_SDA21	@422
    1598:	38 63 00 00 	addi    r3,r3,0
			159a: R_PPC_ADDR16_LO	lbl_804650F4
    159c:	ed 67 10 fa 	fmadds  f11,f7,f3,f2
    15a0:	ed 28 10 fa 	fmadds  f9,f8,f3,f2
    15a4:	d8 01 00 78 	stfd    f0,120(r1)
    15a8:	c0 3e 00 10 	lfs     f1,16(r30)
    15ac:	38 c1 00 48 	addi    r6,r1,72
    15b0:	c0 5e 00 18 	lfs     f2,24(r30)
    15b4:	80 63 00 0c 	lwz     r3,12(r3)
    15b8:	ec 01 10 28 	fsubs   f0,f1,f2
    15bc:	c0 de 00 08 	lfs     f6,8(r30)
    15c0:	c0 be 00 00 	lfs     f5,0(r30)
    15c4:	38 a0 00 00 	li      r5,0
    15c8:	90 61 00 0c 	stw     r3,12(r1)
    15cc:	ec 2b d0 2a 	fadds   f1,f11,f26
    15d0:	ed 46 28 28 	fsubs   f10,f6,f5
    15d4:	d1 61 00 64 	stfs    f11,100(r1)
    15d8:	ec 88 10 3a 	fmadds  f4,f8,f0,f2
    15dc:	80 01 00 7c 	lwz     r0,124(r1)
    15e0:	ec 67 10 3a 	fmadds  f3,f7,f0,f2
    15e4:	d1 21 00 74 	stfs    f9,116(r1)
    15e8:	ec c8 2a ba 	fmadds  f6,f8,f10,f5
    15ec:	d1 21 00 5c 	stfs    f9,92(r1)
    15f0:	ec 49 07 b2 	fmuls   f2,f9,f30
    15f4:	3b 41 00 4c 	addi    r26,r1,76
    15f8:	ec a7 2a ba 	fmadds  f5,f7,f10,f5
    15fc:	d1 61 00 6c 	stfs    f11,108(r1)
    1600:	ec 0b 07 b2 	fmuls   f0,f11,f30
    1604:	d0 21 00 64 	stfs    f1,100(r1)
    1608:	38 61 00 54 	addi    r3,r1,84
    160c:	38 81 00 0c 	addi    r4,r1,12
    1610:	d0 c1 00 58 	stfs    f6,88(r1)
    1614:	d0 a1 00 60 	stfs    f5,96(r1)
    1618:	d0 81 00 70 	stfs    f4,112(r1)
    161c:	d0 61 00 68 	stfs    f3,104(r1)
    1620:	d0 41 00 5c 	stfs    f2,92(r1)
    1624:	d0 01 00 64 	stfs    f0,100(r1)
    1628:	d0 01 00 6c 	stfs    f0,108(r1)
    162c:	d0 41 00 74 	stfs    f2,116(r1)
    1630:	90 e1 00 38 	stw     r7,56(r1)
    1634:	90 c1 00 3c 	stw     r6,60(r1)
    1638:	90 a1 00 40 	stw     r5,64(r1)
    163c:	98 01 00 0f 	stb     r0,15(r1)
    1640:	48 00 00 01 	bl      1640 <render__14TObjCMHairMenuFv+0x514>
			1640: R_PPC_REL24	TObjCMHairMenu__sub_801E3F54
    1644:	7c 64 1b 78 	mr      r4,r3
    1648:	38 61 00 50 	addi    r3,r1,80
    164c:	48 00 00 01 	bl      164c <render__14TObjCMHairMenuFv+0x520>
			164c: R_PPC_REL24	TObjCMHairMenu__sub_801E3F54
    1650:	7c 64 1b 78 	mr      r4,r3
    1654:	7f 43 d3 78 	mr      r3,r26
    1658:	48 00 00 01 	bl      1658 <render__14TObjCMHairMenuFv+0x52c>
			1658: R_PPC_REL24	TObjCMHairMenu__sub_801E3F54
    165c:	7c 64 1b 78 	mr      r4,r3
    1660:	38 61 00 48 	addi    r3,r1,72
    1664:	48 00 00 01 	bl      1664 <render__14TObjCMHairMenuFv+0x538>
			1664: R_PPC_REL24	TObjCMHairMenu__sub_801E3F54
    1668:	3a e0 00 00 	li      r23,0
    166c:	c0 20 00 00 	lfs     f1,0(0)
			166c: R_PPC_EMB_SDA21	@93
    1670:	38 61 00 38 	addi    r3,r1,56
    1674:	38 80 00 04 	li      r4,4
    1678:	38 a0 00 06 	li      r5,6
    167c:	48 00 00 01 	bl      167c <render__14TObjCMHairMenuFv+0x550>
			167c: R_PPC_REL24	draw_tri_fan_2d__14TObjCMHairMenuFllf
    1680:	c0 41 00 5c 	lfs     f2,92(r1)
    1684:	3a f7 00 01 	addi    r23,r23,1
    1688:	c0 21 00 6c 	lfs     f1,108(r1)
    168c:	2c 17 00 03 	cmpwi   r23,3
    1690:	c0 01 00 74 	lfs     f0,116(r1)
    1694:	ec 42 d0 2a 	fadds   f2,f2,f26
    1698:	ec 21 d0 2a 	fadds   f1,f1,f26
    169c:	ec 00 d0 2a 	fadds   f0,f0,f26
    16a0:	d0 41 00 5c 	stfs    f2,92(r1)
    16a4:	d0 21 00 6c 	stfs    f1,108(r1)
    16a8:	d0 01 00 74 	stfs    f0,116(r1)
    16ac:	41 80 ff c0 	blt     166c <render__14TObjCMHairMenuFv+0x540>
    16b0:	3c 60 00 00 	lis     r3,0
			16b2: R_PPC_ADDR16_HA	@268
    16b4:	c3 80 00 00 	lfs     f28,0(0)
			16b4: R_PPC_EMB_SDA21	@424
    16b8:	c3 60 00 00 	lfs     f27,0(0)
			16b8: R_PPC_EMB_SDA21	@54
    16bc:	3b a1 00 54 	addi    r29,r1,84
    16c0:	cb e3 00 00 	lfd     f31,0(r3)
			16c2: R_PPC_ADDR16_LO	@268
    16c4:	3b 81 00 50 	addi    r28,r1,80
    16c8:	3b 60 00 00 	li      r27,0
    16cc:	3b 00 00 00 	li      r24,0
    16d0:	3a e0 00 00 	li      r23,0
    16d4:	3f e0 43 30 	lis     r31,17200
    16d8:	80 79 00 1c 	lwz     r3,28(r25)
    16dc:	38 17 00 42 	addi    r0,r23,66
    16e0:	93 e1 00 78 	stw     r31,120(r1)
    16e4:	7c 03 02 ae 	lhax    r0,r3,r0
    16e8:	6c 00 80 00 	xoris   r0,r0,32768
    16ec:	90 01 00 7c 	stw     r0,124(r1)
    16f0:	c8 01 00 78 	lfd     f0,120(r1)
    16f4:	ec 00 f8 28 	fsubs   f0,f0,f31
    16f8:	ec c0 e0 24 	fdivs   f6,f0,f28
    16fc:	fc 1b 30 00 	fcmpu   cr0,f27,f6
    1700:	41 82 00 e8 	beq     17e8 <render__14TObjCMHairMenuFv+0x6bc>
    1704:	3c 60 00 00 	lis     r3,0
			1706: R_PPC_ADDR16_HA	lbl_804650D4
    1708:	6f 65 80 00 	xoris   r5,r27,32768
    170c:	38 83 00 00 	addi    r4,r3,0
			170e: R_PPC_ADDR16_LO	lbl_804650D4
    1710:	3c 60 43 30 	lis     r3,17200
    1714:	c0 a4 00 00 	lfs     f5,0(r4)
    1718:	3c 80 00 00 	lis     r4,0
			171a: R_PPC_ADDR16_HA	@268
    171c:	c0 9e 00 08 	lfs     f4,8(r30)
    1720:	38 c4 00 00 	addi    r6,r4,0
			1722: R_PPC_ADDR16_LO	@268
    1724:	c0 3e 00 10 	lfs     f1,16(r30)
    1728:	38 00 00 04 	li      r0,4
    172c:	c0 1e 00 18 	lfs     f0,24(r30)
    1730:	38 81 00 58 	addi    r4,r1,88
    1734:	ec 61 20 28 	fsubs   f3,f1,f4
    1738:	90 a1 00 7c 	stw     r5,124(r1)
    173c:	ec 40 28 28 	fsubs   f2,f0,f5
    1740:	c8 26 00 00 	lfd     f1,0(r6)
    1744:	90 61 00 78 	stw     r3,120(r1)
    1748:	38 60 00 00 	li      r3,0
    174c:	c8 01 00 78 	lfd     f0,120(r1)
    1750:	ec 66 20 fa 	fmadds  f3,f6,f3,f4
    1754:	ec 46 28 ba 	fmadds  f2,f6,f2,f5
    1758:	d0 a1 00 58 	stfs    f5,88(r1)
    175c:	ec 00 08 28 	fsubs   f0,f0,f1
    1760:	d0 81 00 60 	stfs    f4,96(r1)
    1764:	ec 20 06 b2 	fmuls   f1,f0,f26
    1768:	d0 61 00 68 	stfs    f3,104(r1)
    176c:	d0 41 00 70 	stfs    f2,112(r1)
    1770:	7c 09 03 a6 	mtctr   r0
    1774:	38 03 00 04 	addi    r0,r3,4
    1778:	38 63 00 08 	addi    r3,r3,8
    177c:	7c 1e 04 2e 	lfsx    f0,r30,r0
    1780:	ec 1e 08 3a 	fmadds  f0,f30,f0,f1
    1784:	7c 04 05 2e 	stfsx   f0,r4,r0
    1788:	42 00 ff ec 	bdnz    1774 <render__14TObjCMHairMenuFv+0x648>
    178c:	3c 60 00 00 	lis     r3,0
			178e: R_PPC_ADDR16_HA	lbl_804650F4
    1790:	88 01 00 0f 	lbz     r0,15(r1)
    1794:	38 83 00 00 	addi    r4,r3,0
			1796: R_PPC_ADDR16_LO	lbl_804650F4
    1798:	7f a3 eb 78 	mr      r3,r29
    179c:	7c a4 c0 2e 	lwzx    r5,r4,r24
    17a0:	38 81 00 08 	addi    r4,r1,8
    17a4:	90 a1 00 08 	stw     r5,8(r1)
    17a8:	98 01 00 0b 	stb     r0,11(r1)
    17ac:	48 00 00 01 	bl      17ac <render__14TObjCMHairMenuFv+0x680>
			17ac: R_PPC_REL24	TObjCMHairMenu__sub_801E3F54
    17b0:	7c 64 1b 78 	mr      r4,r3
    17b4:	7f 83 e3 78 	mr      r3,r28
    17b8:	48 00 00 01 	bl      17b8 <render__14TObjCMHairMenuFv+0x68c>
			17b8: R_PPC_REL24	TObjCMHairMenu__sub_801E3F54
    17bc:	7c 64 1b 78 	mr      r4,r3
    17c0:	7f 43 d3 78 	mr      r3,r26
    17c4:	48 00 00 01 	bl      17c4 <render__14TObjCMHairMenuFv+0x698>
			17c4: R_PPC_REL24	TObjCMHairMenu__sub_801E3F54
    17c8:	7c 64 1b 78 	mr      r4,r3
    17cc:	38 61 00 48 	addi    r3,r1,72
    17d0:	48 00 00 01 	bl      17d0 <render__14TObjCMHairMenuFv+0x6a4>
			17d0: R_PPC_REL24	TObjCMHairMenu__sub_801E3F54
    17d4:	c0 20 00 00 	lfs     f1,0(0)
			17d4: R_PPC_EMB_SDA21	@93
    17d8:	38 61 00 38 	addi    r3,r1,56
    17dc:	38 80 00 04 	li      r4,4
    17e0:	38 a0 00 06 	li      r5,6
    17e4:	48 00 00 01 	bl      17e4 <render__14TObjCMHairMenuFv+0x6b8>
			17e4: R_PPC_REL24	draw_tri_fan_2d__14TObjCMHairMenuFllf
    17e8:	3b 7b 00 01 	addi    r27,r27,1
    17ec:	3a f7 00 02 	addi    r23,r23,2
    17f0:	2c 1b 00 03 	cmpwi   r27,3
    17f4:	3b 18 00 04 	addi    r24,r24,4
    17f8:	41 80 fe e0 	blt     16d8 <render__14TObjCMHairMenuFv+0x5ac>
    17fc:	48 00 00 01 	bl      17fc <render__14TObjCMHairMenuFv+0x6d0>
			17fc: R_PPC_REL24	TCameraCtrl__sub_80068EF0
    1800:	e3 e1 01 38 	psq_l   f31,312(r1),0,0
    1804:	cb e1 01 30 	lfd     f31,304(r1)
    1808:	e3 c1 01 28 	lq      r30,288(r1)
    180c:	cb c1 01 20 	lfd     f30,288(r1)
    1810:	e3 a1 01 18 	psq_l   f29,280(r1),0,0
    1814:	cb a1 01 10 	lfd     f29,272(r1)
    1818:	e3 81 01 08 	lq      r28,256(r1)
    181c:	cb 81 01 00 	lfd     f28,256(r1)
    1820:	e3 61 00 f8 	psq_l   f27,248(r1),0,0
    1824:	cb 61 00 f0 	lfd     f27,240(r1)
    1828:	e3 41 00 e8 	lq      r26,224(r1)
    182c:	cb 41 00 e0 	lfd     f26,224(r1)
    1830:	e3 21 00 d8 	psq_l   f25,216(r1),0,0
    1834:	cb 21 00 d0 	lfd     f25,208(r1)
    1838:	e3 01 00 c8 	lq      r24,192(r1)
    183c:	cb 01 00 c0 	lfd     f24,192(r1)
    1840:	e2 e1 00 b8 	psq_l   f23,184(r1),0,0
    1844:	ca e1 00 b0 	lfd     f23,176(r1)
    1848:	ba e1 00 8c 	lmw     r23,140(r1)
    184c:	80 01 01 44 	lwz     r0,324(r1)
    1850:	7c 08 03 a6 	mtlr    r0
    1854:	38 21 01 40 	addi    r1,r1,320
    1858:	4e 80 00 20 	blr

0000185c <run_task__14TObjCMHairMenuFv>:
    185c:	94 21 ff e0 	stwu    r1,-32(r1)
    1860:	7c 08 02 a6 	mflr    r0
    1864:	90 01 00 24 	stw     r0,36(r1)
    1868:	bf a1 00 14 	stmw    r29,20(r1)
    186c:	7c 7f 1b 78 	mr      r31,r3
    1870:	80 83 00 2c 	lwz     r4,44(r3)
    1874:	38 04 00 01 	addi    r0,r4,1
    1878:	90 03 00 2c 	stw     r0,44(r3)
    187c:	80 03 00 20 	lwz     r0,32(r3)
    1880:	2c 00 00 00 	cmpwi   r0,0
    1884:	40 82 00 10 	bne     1894 <run_task__14TObjCMHairMenuFv+0x38>
    1888:	38 00 00 01 	li      r0,1
    188c:	90 1f 00 20 	stw     r0,32(r31)
    1890:	48 00 02 78 	b       1b08 <run_task__14TObjCMHairMenuFv+0x2ac>
    1894:	80 1f 00 30 	lwz     r0,48(r31)
    1898:	2c 00 00 00 	cmpwi   r0,0
    189c:	40 82 00 30 	bne     18cc <run_task__14TObjCMHairMenuFv+0x70>
    18a0:	c0 5f 00 34 	lfs     f2,52(r31)
    18a4:	c0 20 00 00 	lfs     f1,0(0)
			18a4: R_PPC_EMB_SDA21	lbl_805DDAA8
    18a8:	c0 00 00 00 	lfs     f0,0(0)
			18a8: R_PPC_EMB_SDA21	lbl_805DDA90
    18ac:	ec 22 08 2a 	fadds   f1,f2,f1
    18b0:	fc 01 00 40 	fcmpo   cr0,f1,f0
    18b4:	d0 3f 00 34 	stfs    f1,52(r31)
    18b8:	4c 40 13 82 	cror    eq,lt,eq
    18bc:	40 82 02 4c 	bne     1b08 <run_task__14TObjCMHairMenuFv+0x2ac>
    18c0:	d0 1f 00 34 	stfs    f0,52(r31)
    18c4:	48 00 00 01 	bl      18c4 <run_task__14TObjCMHairMenuFv+0x68>
			18c4: R_PPC_REL24	queue_destruction__7TObjectFv
    18c8:	48 00 02 40 	b       1b08 <run_task__14TObjCMHairMenuFv+0x2ac>
    18cc:	c0 5f 00 34 	lfs     f2,52(r31)
    18d0:	c0 20 00 00 	lfs     f1,0(0)
			18d0: R_PPC_EMB_SDA21	lbl_805DDAAC
    18d4:	c0 00 00 00 	lfs     f0,0(0)
			18d4: R_PPC_EMB_SDA21	lbl_805DDA70
    18d8:	ec 22 08 2a 	fadds   f1,f2,f1
    18dc:	fc 01 00 40 	fcmpo   cr0,f1,f0
    18e0:	d0 3f 00 34 	stfs    f1,52(r31)
    18e4:	40 81 00 08 	ble     18ec <run_task__14TObjCMHairMenuFv+0x90>
    18e8:	d0 1f 00 34 	stfs    f0,52(r31)
    18ec:	38 60 00 20 	li      r3,32
    18f0:	48 00 00 01 	bl      18f0 <run_task__14TObjCMHairMenuFv+0x94>
			18f0: R_PPC_REL24	creation_direction_repeated__Fl
    18f4:	2c 03 00 00 	cmpwi   r3,0
    18f8:	41 82 00 3c 	beq     1934 <run_task__14TObjCMHairMenuFv+0xd8>
    18fc:	80 7f 00 24 	lwz     r3,36(r31)
    1900:	38 03 00 01 	addi    r0,r3,1
    1904:	2c 00 00 04 	cmpwi   r0,4
    1908:	90 1f 00 24 	stw     r0,36(r31)
    190c:	41 80 00 0c 	blt     1918 <run_task__14TObjCMHairMenuFv+0xbc>
    1910:	38 00 00 00 	li      r0,0
    1914:	90 1f 00 24 	stw     r0,36(r31)
    1918:	3c 60 00 05 	lis     r3,5
    191c:	38 80 00 00 	li      r4,0
    1920:	38 63 41 00 	addi    r3,r3,16640
    1924:	38 a0 00 00 	li      r5,0
    1928:	38 c0 00 00 	li      r6,0
    192c:	48 00 00 01 	bl      192c <run_task__14TObjCMHairMenuFv+0xd0>
			192c: R_PPC_REL24	play_sound_effect
    1930:	48 00 00 44 	b       1974 <run_task__14TObjCMHairMenuFv+0x118>
    1934:	38 60 00 10 	li      r3,16
    1938:	48 00 00 01 	bl      1938 <run_task__14TObjCMHairMenuFv+0xdc>
			1938: R_PPC_REL24	creation_direction_repeated__Fl
    193c:	2c 03 00 00 	cmpwi   r3,0
    1940:	41 82 00 34 	beq     1974 <run_task__14TObjCMHairMenuFv+0x118>
    1944:	80 7f 00 24 	lwz     r3,36(r31)
    1948:	34 03 ff ff 	addic.  r0,r3,-1
    194c:	90 1f 00 24 	stw     r0,36(r31)
    1950:	40 80 00 0c 	bge     195c <run_task__14TObjCMHairMenuFv+0x100>
    1954:	38 00 00 03 	li      r0,3
    1958:	90 1f 00 24 	stw     r0,36(r31)
    195c:	3c 60 00 05 	lis     r3,5
    1960:	38 80 00 00 	li      r4,0
    1964:	38 63 41 00 	addi    r3,r3,16640
    1968:	38 a0 00 00 	li      r5,0
    196c:	38 c0 00 00 	li      r6,0
    1970:	48 00 00 01 	bl      1970 <run_task__14TObjCMHairMenuFv+0x114>
			1970: R_PPC_REL24	play_sound_effect
    1974:	80 7f 00 24 	lwz     r3,36(r31)
    1978:	2c 03 00 00 	cmpwi   r3,0
    197c:	40 82 00 a4 	bne     1a20 <run_task__14TObjCMHairMenuFv+0x1c4>
    1980:	83 df 00 1c 	lwz     r30,28(r31)
    1984:	38 60 00 80 	li      r3,128
    1988:	48 00 00 01 	bl      1988 <run_task__14TObjCMHairMenuFv+0x12c>
			1988: R_PPC_REL24	creation_direction_repeated__Fl
    198c:	2c 03 00 00 	cmpwi   r3,0
    1990:	41 82 00 44 	beq     19d4 <run_task__14TObjCMHairMenuFv+0x178>
    1994:	a8 7e 00 40 	lha     r3,64(r30)
    1998:	38 03 00 01 	addi    r0,r3,1
    199c:	b0 1e 00 40 	sth     r0,64(r30)
    19a0:	7c 03 07 34 	extsh   r3,r0
    19a4:	80 1f 00 28 	lwz     r0,40(r31)
    19a8:	7c 03 00 00 	cmpw    r3,r0
    19ac:	41 80 00 0c 	blt     19b8 <run_task__14TObjCMHairMenuFv+0x15c>
    19b0:	38 00 00 00 	li      r0,0
    19b4:	b0 1e 00 40 	sth     r0,64(r30)
    19b8:	3c 60 00 05 	lis     r3,5
    19bc:	38 80 00 00 	li      r4,0
    19c0:	38 63 41 00 	addi    r3,r3,16640
    19c4:	38 a0 00 00 	li      r5,0
    19c8:	38 c0 00 00 	li      r6,0
    19cc:	48 00 00 01 	bl      19cc <run_task__14TObjCMHairMenuFv+0x170>
			19cc: R_PPC_REL24	play_sound_effect
    19d0:	48 00 01 04 	b       1ad4 <run_task__14TObjCMHairMenuFv+0x278>
    19d4:	38 60 00 40 	li      r3,64
    19d8:	48 00 00 01 	bl      19d8 <run_task__14TObjCMHairMenuFv+0x17c>
			19d8: R_PPC_REL24	creation_direction_repeated__Fl
    19dc:	2c 03 00 00 	cmpwi   r3,0
    19e0:	41 82 00 f4 	beq     1ad4 <run_task__14TObjCMHairMenuFv+0x278>
    19e4:	a8 7e 00 40 	lha     r3,64(r30)
    19e8:	38 63 ff ff 	addi    r3,r3,-1
    19ec:	7c 60 07 35 	extsh.  r0,r3
    19f0:	b0 7e 00 40 	sth     r3,64(r30)
    19f4:	40 80 00 10 	bge     1a04 <run_task__14TObjCMHairMenuFv+0x1a8>
    19f8:	80 7f 00 28 	lwz     r3,40(r31)
    19fc:	38 03 ff ff 	addi    r0,r3,-1
    1a00:	b0 1e 00 40 	sth     r0,64(r30)
    1a04:	3c 60 00 05 	lis     r3,5
    1a08:	38 80 00 00 	li      r4,0
    1a0c:	38 63 41 00 	addi    r3,r3,16640
    1a10:	38 a0 00 00 	li      r5,0
    1a14:	38 c0 00 00 	li      r6,0
    1a18:	48 00 00 01 	bl      1a18 <run_task__14TObjCMHairMenuFv+0x1bc>
			1a18: R_PPC_REL24	play_sound_effect
    1a1c:	48 00 00 b8 	b       1ad4 <run_task__14TObjCMHairMenuFv+0x278>
    1a20:	38 03 00 04 	addi    r0,r3,4
    1a24:	83 df 00 1c 	lwz     r30,28(r31)
    1a28:	54 04 08 3c 	slwi    r4,r0,1
    1a2c:	38 60 00 80 	li      r3,128
    1a30:	3b a4 00 38 	addi    r29,r4,56
    1a34:	48 00 00 01 	bl      1a34 <run_task__14TObjCMHairMenuFv+0x1d8>
			1a34: R_PPC_REL24	creation_buttons_pressed__Fl
    1a38:	2c 03 00 00 	cmpwi   r3,0
    1a3c:	41 82 00 14 	beq     1a50 <run_task__14TObjCMHairMenuFv+0x1f4>
    1a40:	7c 7e ea ae 	lhax    r3,r30,r29
    1a44:	38 03 00 01 	addi    r0,r3,1
    1a48:	7c 1e eb 2e 	sthx    r0,r30,r29
    1a4c:	48 00 00 60 	b       1aac <run_task__14TObjCMHairMenuFv+0x250>
    1a50:	38 60 00 40 	li      r3,64
    1a54:	48 00 00 01 	bl      1a54 <run_task__14TObjCMHairMenuFv+0x1f8>
			1a54: R_PPC_REL24	creation_buttons_pressed__Fl
    1a58:	2c 03 00 00 	cmpwi   r3,0
    1a5c:	41 82 00 14 	beq     1a70 <run_task__14TObjCMHairMenuFv+0x214>
    1a60:	7c 7e ea ae 	lhax    r3,r30,r29
    1a64:	38 03 ff ff 	addi    r0,r3,-1
    1a68:	7c 1e eb 2e 	sthx    r0,r30,r29
    1a6c:	48 00 00 40 	b       1aac <run_task__14TObjCMHairMenuFv+0x250>
    1a70:	38 60 00 80 	li      r3,128
    1a74:	48 00 00 01 	bl      1a74 <run_task__14TObjCMHairMenuFv+0x218>
			1a74: R_PPC_REL24	creation_buttons_held__Fl
    1a78:	2c 03 00 00 	cmpwi   r3,0
    1a7c:	41 82 00 14 	beq     1a90 <run_task__14TObjCMHairMenuFv+0x234>
    1a80:	7c 7e ea ae 	lhax    r3,r30,r29
    1a84:	38 03 00 05 	addi    r0,r3,5
    1a88:	7c 1e eb 2e 	sthx    r0,r30,r29
    1a8c:	48 00 00 20 	b       1aac <run_task__14TObjCMHairMenuFv+0x250>
    1a90:	38 60 00 40 	li      r3,64
    1a94:	48 00 00 01 	bl      1a94 <run_task__14TObjCMHairMenuFv+0x238>
			1a94: R_PPC_REL24	creation_buttons_held__Fl
    1a98:	2c 03 00 00 	cmpwi   r3,0
    1a9c:	41 82 00 10 	beq     1aac <run_task__14TObjCMHairMenuFv+0x250>
    1aa0:	7c 7e ea ae 	lhax    r3,r30,r29
    1aa4:	38 03 ff fb 	addi    r0,r3,-5
    1aa8:	7c 1e eb 2e 	sthx    r0,r30,r29
    1aac:	7c 1e ea ae 	lhax    r0,r30,r29
    1ab0:	2c 00 00 ff 	cmpwi   r0,255
    1ab4:	40 81 00 10 	ble     1ac4 <run_task__14TObjCMHairMenuFv+0x268>
    1ab8:	38 00 00 ff 	li      r0,255
    1abc:	7c 1e eb 2e 	sthx    r0,r30,r29
    1ac0:	48 00 00 14 	b       1ad4 <run_task__14TObjCMHairMenuFv+0x278>
    1ac4:	7c 00 07 35 	extsh.  r0,r0
    1ac8:	40 80 00 0c 	bge     1ad4 <run_task__14TObjCMHairMenuFv+0x278>
    1acc:	38 00 00 00 	li      r0,0
    1ad0:	7c 1e eb 2e 	sthx    r0,r30,r29
    1ad4:	38 60 00 06 	li      r3,6
    1ad8:	48 00 00 01 	bl      1ad8 <run_task__14TObjCMHairMenuFv+0x27c>
			1ad8: R_PPC_REL24	creation_buttons_pressed__Fl
    1adc:	2c 03 00 00 	cmpwi   r3,0
    1ae0:	41 82 00 28 	beq     1b08 <run_task__14TObjCMHairMenuFv+0x2ac>
    1ae4:	3c 60 00 05 	lis     r3,5
    1ae8:	38 80 00 00 	li      r4,0
    1aec:	38 63 37 04 	addi    r3,r3,14084
    1af0:	38 a0 00 00 	li      r5,0
    1af4:	38 c0 00 00 	li      r6,0
    1af8:	48 00 00 01 	bl      1af8 <run_task__14TObjCMHairMenuFv+0x29c>
			1af8: R_PPC_REL24	play_sound_effect
    1afc:	48 00 00 01 	bl      1afc <run_task__14TObjCMHairMenuFv+0x2a0>
			1afc: R_PPC_REL24	clear_task_state__14TObjCMMainMenuFv
    1b00:	38 00 00 00 	li      r0,0
    1b04:	90 1f 00 30 	stw     r0,48(r31)
    1b08:	bb a1 00 14 	lmw     r29,20(r1)
    1b0c:	80 01 00 24 	lwz     r0,36(r1)
    1b10:	7c 08 03 a6 	mtlr    r0
    1b14:	38 21 00 20 	addi    r1,r1,32
    1b18:	4e 80 00 20 	blr

00001b1c <create__14TObjCMHairMenuFv>:
    1b1c:	94 21 ff f0 	stwu    r1,-16(r1)
    1b20:	7c 08 02 a6 	mflr    r0
    1b24:	90 01 00 14 	stw     r0,20(r1)
    1b28:	93 e1 00 0c 	stw     r31,12(r1)
    1b2c:	7c 7f 1b 78 	mr      r31,r3
    1b30:	38 60 00 44 	li      r3,68
    1b34:	48 00 00 01 	bl      1b34 <create__14TObjCMHairMenuFv+0x18>
			1b34: R_PPC_REL24	__nw__7TObjectFUl
    1b38:	7c 60 1b 79 	mr.     r0,r3
    1b3c:	41 82 00 10 	beq     1b4c <create__14TObjCMHairMenuFv+0x30>
    1b40:	7f e4 fb 78 	mr      r4,r31
    1b44:	48 00 00 01 	bl      1b44 <create__14TObjCMHairMenuFv+0x28>
			1b44: R_PPC_REL24	__ct__14TObjCMHairMenuFv
    1b48:	7c 60 1b 78 	mr      r0,r3
    1b4c:	7c 03 03 78 	mr      r3,r0
    1b50:	80 01 00 14 	lwz     r0,20(r1)
    1b54:	83 e1 00 0c 	lwz     r31,12(r1)
    1b58:	7c 08 03 a6 	mtlr    r0
    1b5c:	38 21 00 10 	addi    r1,r1,16
    1b60:	4e 80 00 20 	blr

00001b64 <__dt__14TObjCMHairMenuFv>:
    1b64:	94 21 ff f0 	stwu    r1,-16(r1)
    1b68:	7c 08 02 a6 	mflr    r0
    1b6c:	90 01 00 14 	stw     r0,20(r1)
    1b70:	bf c1 00 08 	stmw    r30,8(r1)
    1b74:	7c 7e 1b 79 	mr.     r30,r3
    1b78:	7c 9f 23 78 	mr      r31,r4
    1b7c:	41 82 00 28 	beq     1ba4 <__dt__14TObjCMHairMenuFv+0x40>
    1b80:	3c a0 00 00 	lis     r5,0
			1b82: R_PPC_ADDR16_HA	__vt__14TObjCMHairMenu
    1b84:	38 80 00 00 	li      r4,0
    1b88:	38 05 00 00 	addi    r0,r5,0
			1b8a: R_PPC_ADDR16_LO	__vt__14TObjCMHairMenu
    1b8c:	90 1e 00 18 	stw     r0,24(r30)
    1b90:	48 00 00 01 	bl      1b90 <__dt__14TObjCMHairMenuFv+0x2c>
			1b90: R_PPC_REL24	__dt__7TObjectFv
    1b94:	7f e0 07 35 	extsh.  r0,r31
    1b98:	40 81 00 0c 	ble     1ba4 <__dt__14TObjCMHairMenuFv+0x40>
    1b9c:	7f c3 f3 78 	mr      r3,r30
    1ba0:	48 00 00 01 	bl      1ba0 <__dt__14TObjCMHairMenuFv+0x3c>
			1ba0: R_PPC_REL24	__dl__7TObjectFPv
    1ba4:	7f c3 f3 78 	mr      r3,r30
    1ba8:	bb c1 00 08 	lmw     r30,8(r1)
    1bac:	80 01 00 14 	lwz     r0,20(r1)
    1bb0:	7c 08 03 a6 	mtlr    r0
    1bb4:	38 21 00 10 	addi    r1,r1,16
    1bb8:	4e 80 00 20 	blr

00001bbc <__ct__14TObjCMHairMenuFv>:
    1bbc:	94 21 ff f0 	stwu    r1,-16(r1)
    1bc0:	7c 08 02 a6 	mflr    r0
    1bc4:	90 01 00 14 	stw     r0,20(r1)
    1bc8:	93 e1 00 0c 	stw     r31,12(r1)
    1bcc:	7c 7f 1b 78 	mr      r31,r3
    1bd0:	48 00 00 01 	bl      1bd0 <__ct__14TObjCMHairMenuFv+0x14>
			1bd0: R_PPC_REL24	__ct__7TObjectFP7TObject
    1bd4:	3c 60 00 00 	lis     r3,0
			1bd6: R_PPC_ADDR16_HA	__vt__14TObjCMHairMenu
    1bd8:	38 00 00 00 	li      r0,0
    1bdc:	38 63 00 00 	addi    r3,r3,0
			1bde: R_PPC_ADDR16_LO	__vt__14TObjCMHairMenu
    1be0:	90 7f 00 18 	stw     r3,24(r31)
    1be4:	80 60 00 00 	lwz     r3,0(0)
			1be4: R_PPC_EMB_SDA21	lbl_805D3CE0
    1be8:	90 7f 00 00 	stw     r3,0(r31)
    1bec:	80 60 00 00 	lwz     r3,0(0)
			1bec: R_PPC_EMB_SDA21	creation_player_character
    1bf0:	90 7f 00 1c 	stw     r3,28(r31)
    1bf4:	90 1f 00 20 	stw     r0,32(r31)
    1bf8:	90 1f 00 24 	stw     r0,36(r31)
    1bfc:	80 7f 00 1c 	lwz     r3,28(r31)
    1c00:	48 00 00 01 	bl      1c00 <__ct__14TObjCMHairMenuFv+0x44>
			1c00: R_PPC_REL24	get_display_index__12TCharaMakingFv
    1c04:	1c a3 00 2c 	mulli   r5,r3,44
    1c08:	3c 80 00 00 	lis     r4,0
			1c0a: R_PPC_ADDR16_HA	class_appearance_table
    1c0c:	c0 00 00 00 	lfs     f0,0(0)
			1c0c: R_PPC_EMB_SDA21	lbl_805DDA90
    1c10:	38 60 00 00 	li      r3,0
    1c14:	38 04 00 00 	addi    r0,r4,0
			1c16: R_PPC_ADDR16_LO	class_appearance_table
    1c18:	7c 80 2a 14 	add     r4,r0,r5
    1c1c:	a8 c4 00 08 	lha     r6,8(r4)
    1c20:	38 a0 00 01 	li      r5,1
    1c24:	38 00 00 03 	li      r0,3
    1c28:	7c 64 1b 78 	mr      r4,r3
    1c2c:	90 df 00 28 	stw     r6,40(r31)
    1c30:	90 bf 00 30 	stw     r5,48(r31)
    1c34:	d0 1f 00 34 	stfs    f0,52(r31)
    1c38:	7c 09 03 a6 	mtctr   r0
    1c3c:	38 03 00 38 	addi    r0,r3,56
    1c40:	38 63 00 04 	addi    r3,r3,4
    1c44:	7c 9f 01 2e 	stwx    r4,r31,r0
    1c48:	42 00 ff f4 	bdnz    1c3c <__ct__14TObjCMHairMenuFv+0x80>
    1c4c:	38 60 00 05 	li      r3,5
    1c50:	48 00 00 01 	bl      1c50 <__ct__14TObjCMHairMenuFv+0x94>
			1c50: R_PPC_REL24	set_eff_tag__11TChCrEffTagFi
    1c54:	80 01 00 14 	lwz     r0,20(r1)
    1c58:	7f e3 fb 78 	mr      r3,r31
    1c5c:	83 e1 00 0c 	lwz     r31,12(r1)
    1c60:	7c 08 03 a6 	mtlr    r0
    1c64:	38 21 00 10 	addi    r1,r1,16
    1c68:	4e 80 00 20 	blr

00001c6c <draw_assign_icons__16TObjCMAssignMenuFv>:
    1c6c:	94 21 ff b0 	stwu    r1,-80(r1)
    1c70:	7c 08 02 a6 	mflr    r0
    1c74:	90 01 00 54 	stw     r0,84(r1)
    1c78:	db e1 00 40 	stfd    f31,64(r1)
    1c7c:	f3 e1 00 48 	xsmaddmsp vs31,vs1,vs0
    1c80:	db c1 00 30 	stfd    f30,48(r1)
    1c84:	f3 c1 00 38 	xxsel   vs30,vs1,vs0,vs32
    1c88:	bf 61 00 1c 	stmw    r27,28(r1)
    1c8c:	7c 7b 1b 78 	mr      r27,r3
    1c90:	c0 00 00 00 	lfs     f0,0(0)
			1c90: R_PPC_EMB_SDA21	lbl_805DDA74
    1c94:	c0 23 00 40 	lfs     f1,64(r3)
    1c98:	fc 01 00 40 	fcmpo   cr0,f1,f0
    1c9c:	4c 40 13 82 	cror    eq,lt,eq
    1ca0:	41 82 00 90 	beq     1d30 <draw_assign_icons__16TObjCMAssignMenuFv+0xc4>
    1ca4:	ec 61 00 28 	fsubs   f3,f1,f0
    1ca8:	c0 40 00 00 	lfs     f2,0(0)
			1ca8: R_PPC_EMB_SDA21	lbl_805DDB10
    1cac:	c0 20 00 00 	lfs     f1,0(0)
			1cac: R_PPC_EMB_SDA21	lbl_805DDB48
    1cb0:	3c 60 00 00 	lis     r3,0
			1cb2: R_PPC_ADDR16_HA	char_creation_assign_icon_sprite_id_table
    1cb4:	c0 00 00 00 	lfs     f0,0(0)
			1cb4: R_PPC_EMB_SDA21	lbl_805DDB4C
    1cb8:	3b c3 00 00 	addi    r30,r3,0
			1cba: R_PPC_ADDR16_LO	char_creation_assign_icon_sprite_id_table
    1cbc:	ec 43 10 24 	fdivs   f2,f3,f2
    1cc0:	d0 21 00 08 	stfs    f1,8(r1)
    1cc4:	c3 e0 00 00 	lfs     f31,0(0)
			1cc4: R_PPC_EMB_SDA21	TObjCMAssignMenu__data_805DDB20
    1cc8:	3b e0 00 00 	li      r31,0
    1ccc:	d0 01 00 0c 	stfs    f0,12(r1)
    1cd0:	3b a0 00 01 	li      r29,1
    1cd4:	ef c2 00 b2 	fmuls   f30,f2,f2
    1cd8:	3b 80 00 00 	li      r28,0
    1cdc:	48 00 00 48 	b       1d24 <draw_assign_icons__16TObjCMAssignMenuFv+0xb8>
    1ce0:	80 7b 00 34 	lwz     r3,52(r27)
    1ce4:	48 00 00 0c 	b       1cf0 <draw_assign_icons__16TObjCMAssignMenuFv+0x84>
    1ce8:	57 bd 08 3c 	slwi    r29,r29,1
    1cec:	3b ff 00 04 	addi    r31,r31,4
    1cf0:	7f a0 18 39 	and.    r0,r29,r3
    1cf4:	41 82 ff f4 	beq     1ce8 <draw_assign_icons__16TObjCMAssignMenuFv+0x7c>
    1cf8:	fc 40 f0 90 	fmr     f2,f30
    1cfc:	7c 7e f8 2e 	lwzx    r3,r30,r31
    1d00:	c0 20 00 00 	lfs     f1,0(0)
			1d00: R_PPC_EMB_SDA21	lbl_805DDA94
    1d04:	38 81 00 08 	addi    r4,r1,8
    1d08:	48 00 00 01 	bl      1d08 <draw_assign_icons__16TObjCMAssignMenuFv+0x9c>
			1d08: R_PPC_REL24	draw_ui_sprite
    1d0c:	c0 01 00 08 	lfs     f0,8(r1)
    1d10:	57 bd 08 3c 	slwi    r29,r29,1
    1d14:	3b ff 00 04 	addi    r31,r31,4
    1d18:	3b 9c 00 01 	addi    r28,r28,1
    1d1c:	ec 00 f8 2a 	fadds   f0,f0,f31
    1d20:	d0 01 00 08 	stfs    f0,8(r1)
    1d24:	80 1b 00 30 	lwz     r0,48(r27)
    1d28:	7c 1c 00 00 	cmpw    r28,r0
    1d2c:	41 80 ff b4 	blt     1ce0 <draw_assign_icons__16TObjCMAssignMenuFv+0x74>
    1d30:	e3 e1 00 48 	psq_l   f31,72(r1),0,0
    1d34:	cb e1 00 40 	lfd     f31,64(r1)
    1d38:	e3 c1 00 38 	lq      r30,48(r1)
    1d3c:	cb c1 00 30 	lfd     f30,48(r1)
    1d40:	bb 61 00 1c 	lmw     r27,28(r1)
    1d44:	80 01 00 54 	lwz     r0,84(r1)
    1d48:	7c 08 03 a6 	mtlr    r0
    1d4c:	38 21 00 50 	addi    r1,r1,80
    1d50:	4e 80 00 20 	blr

00001d54 <sub_80296648__16TObjCMAssignMenuFv>:
    1d54:	94 21 ff b0 	stwu    r1,-80(r1)
    1d58:	7c 08 02 a6 	mflr    r0
    1d5c:	90 01 00 54 	stw     r0,84(r1)
    1d60:	db e1 00 40 	stfd    f31,64(r1)
    1d64:	f3 e1 00 48 	xsmaddmsp vs31,vs1,vs0
    1d68:	db c1 00 30 	stfd    f30,48(r1)
    1d6c:	f3 c1 00 38 	xxsel   vs30,vs1,vs0,vs32
    1d70:	bf 61 00 1c 	stmw    r27,28(r1)
    1d74:	7c 7b 1b 78 	mr      r27,r3
    1d78:	c0 00 00 00 	lfs     f0,0(0)
			1d78: R_PPC_EMB_SDA21	lbl_805DDA74
    1d7c:	c0 23 00 40 	lfs     f1,64(r3)
    1d80:	fc 01 00 40 	fcmpo   cr0,f1,f0
    1d84:	4c 40 13 82 	cror    eq,lt,eq
    1d88:	41 82 00 a4 	beq     1e2c <sub_80296648__16TObjCMAssignMenuFv+0xd8>
    1d8c:	ec 61 00 28 	fsubs   f3,f1,f0
    1d90:	c0 40 00 00 	lfs     f2,0(0)
			1d90: R_PPC_EMB_SDA21	lbl_805DDB10
    1d94:	c0 20 00 00 	lfs     f1,0(0)
			1d94: R_PPC_EMB_SDA21	lbl_805DDB48
    1d98:	3b c0 00 00 	li      r30,0
    1d9c:	c0 00 00 00 	lfs     f0,0(0)
			1d9c: R_PPC_EMB_SDA21	lbl_805DDB4C
    1da0:	3b e0 00 00 	li      r31,0
    1da4:	ec 43 10 24 	fdivs   f2,f3,f2
    1da8:	d0 21 00 08 	stfs    f1,8(r1)
    1dac:	c3 e0 00 00 	lfs     f31,0(0)
			1dac: R_PPC_EMB_SDA21	TObjCMAssignMenu__data_805DDB20
    1db0:	3b a0 00 01 	li      r29,1
    1db4:	d0 01 00 0c 	stfs    f0,12(r1)
    1db8:	3b 80 00 00 	li      r28,0
    1dbc:	ef c2 00 b2 	fmuls   f30,f2,f2
    1dc0:	48 00 00 60 	b       1e20 <sub_80296648__16TObjCMAssignMenuFv+0xcc>
    1dc4:	80 7b 00 34 	lwz     r3,52(r27)
    1dc8:	48 00 00 10 	b       1dd8 <sub_80296648__16TObjCMAssignMenuFv+0x84>
    1dcc:	57 bd 08 3c 	slwi    r29,r29,1
    1dd0:	3b de 00 01 	addi    r30,r30,1
    1dd4:	3b ff 00 04 	addi    r31,r31,4
    1dd8:	7f a0 18 39 	and.    r0,r29,r3
    1ddc:	41 82 ff f0 	beq     1dcc <sub_80296648__16TObjCMAssignMenuFv+0x78>
    1de0:	2c 1e 00 07 	cmpwi   r30,7
    1de4:	40 80 00 20 	bge     1e04 <sub_80296648__16TObjCMAssignMenuFv+0xb0>
    1de8:	3c 60 00 00 	lis     r3,0
			1dea: R_PPC_ADDR16_HA	char_creation_assign_sprite_id_table
    1dec:	fc 40 f0 90 	fmr     f2,f30
    1df0:	38 63 00 00 	addi    r3,r3,0
			1df2: R_PPC_ADDR16_LO	char_creation_assign_sprite_id_table
    1df4:	c0 20 00 00 	lfs     f1,0(0)
			1df4: R_PPC_EMB_SDA21	lbl_805DDA94
    1df8:	7c 63 f8 2e 	lwzx    r3,r3,r31
    1dfc:	38 81 00 08 	addi    r4,r1,8
    1e00:	48 00 00 01 	bl      1e00 <sub_80296648__16TObjCMAssignMenuFv+0xac>
			1e00: R_PPC_REL24	draw_ui_sprite
    1e04:	c0 01 00 08 	lfs     f0,8(r1)
    1e08:	57 bd 08 3c 	slwi    r29,r29,1
    1e0c:	3b ff 00 04 	addi    r31,r31,4
    1e10:	3b de 00 01 	addi    r30,r30,1
    1e14:	ec 00 f8 2a 	fadds   f0,f0,f31
    1e18:	3b 9c 00 01 	addi    r28,r28,1
    1e1c:	d0 01 00 08 	stfs    f0,8(r1)
    1e20:	80 1b 00 30 	lwz     r0,48(r27)
    1e24:	7c 1c 00 00 	cmpw    r28,r0
    1e28:	41 80 ff 9c 	blt     1dc4 <sub_80296648__16TObjCMAssignMenuFv+0x70>
    1e2c:	e3 e1 00 48 	psq_l   f31,72(r1),0,0
    1e30:	cb e1 00 40 	lfd     f31,64(r1)
    1e34:	e3 c1 00 38 	lq      r30,48(r1)
    1e38:	cb c1 00 30 	lfd     f30,48(r1)
    1e3c:	bb 61 00 1c 	lmw     r27,28(r1)
    1e40:	80 01 00 54 	lwz     r0,84(r1)
    1e44:	7c 08 03 a6 	mtlr    r0
    1e48:	38 21 00 50 	addi    r1,r1,80
    1e4c:	4e 80 00 20 	blr

00001e50 <render_assign_slots__16TObjCMAssignMenuFv>:
    1e50:	94 21 ff 90 	stwu    r1,-112(r1)
    1e54:	7c 08 02 a6 	mflr    r0
    1e58:	90 01 00 74 	stw     r0,116(r1)
    1e5c:	db e1 00 60 	stfd    f31,96(r1)
    1e60:	f3 e1 00 68 	psq_st  f31,104(r1),0,0
    1e64:	db c1 00 50 	stfd    f30,80(r1)
    1e68:	f3 c1 00 58 	xscmpgtdp vs30,vs1,vs0
    1e6c:	db a1 00 40 	stfd    f29,64(r1)
    1e70:	f3 a1 00 48 	xsmaddmsp vs29,vs1,vs0
    1e74:	db 81 00 30 	stfd    f28,48(r1)
    1e78:	f3 81 00 38 	xxsel   vs28,vs1,vs0,vs32
    1e7c:	bf 41 00 18 	stmw    r26,24(r1)
    1e80:	7c 7f 1b 78 	mr      r31,r3
    1e84:	80 03 00 4c 	lwz     r0,76(r3)
    1e88:	2c 00 00 01 	cmpwi   r0,1
    1e8c:	41 82 01 74 	beq     2000 <render_assign_slots__16TObjCMAssignMenuFv+0x1b0>
    1e90:	c0 5f 00 40 	lfs     f2,64(r31)
    1e94:	c0 20 00 00 	lfs     f1,0(0)
			1e94: R_PPC_EMB_SDA21	lbl_805DDB50
    1e98:	c0 00 00 00 	lfs     f0,0(0)
			1e98: R_PPC_EMB_SDA21	lbl_805DDB54
    1e9c:	ec 21 00 b2 	fmuls   f1,f1,f2
    1ea0:	ec 22 00 72 	fmuls   f1,f2,f1
    1ea4:	ef a2 00 72 	fmuls   f29,f2,f1
    1ea8:	fc 1d 00 40 	fcmpo   cr0,f29,f0
    1eac:	4c 40 13 82 	cror    eq,lt,eq
    1eb0:	41 82 01 50 	beq     2000 <render_assign_slots__16TObjCMAssignMenuFv+0x1b0>
    1eb4:	3c 60 00 00 	lis     r3,0
			1eb6: R_PPC_ADDR16_HA	@268
    1eb8:	c3 e0 00 00 	lfs     f31,0(0)
			1eb8: R_PPC_EMB_SDA21	@54
    1ebc:	cb c3 00 00 	lfd     f30,0(r3)
			1ebe: R_PPC_ADDR16_LO	@268
    1ec0:	3b 80 00 00 	li      r28,0
    1ec4:	3f a0 43 30 	lis     r29,17200
    1ec8:	48 00 01 2c 	b       1ff4 <render_assign_slots__16TObjCMAssignMenuFv+0x1a4>
    1ecc:	6f 83 80 00 	xoris   r3,r28,32768
    1ed0:	38 04 ff ff 	addi    r0,r4,-1
    1ed4:	90 61 00 14 	stw     r3,20(r1)
    1ed8:	7c 1c 00 00 	cmpw    r28,r0
    1edc:	80 1f 00 44 	lwz     r0,68(r31)
    1ee0:	93 a1 00 10 	stw     r29,16(r1)
    1ee4:	c0 1f 00 58 	lfs     f0,88(r31)
    1ee8:	7c 1b 03 78 	mr      r27,r0
    1eec:	c8 21 00 10 	lfd     f1,16(r1)
    1ef0:	ec 21 f0 28 	fsubs   f1,f1,f30
    1ef4:	ec 21 00 28 	fsubs   f1,f1,f0
    1ef8:	40 82 00 10 	bne     1f08 <render_assign_slots__16TObjCMAssignMenuFv+0xb8>
    1efc:	7c 7c 01 d6 	mullw   r3,r28,r0
    1f00:	80 1f 00 30 	lwz     r0,48(r31)
    1f04:	7f 63 00 50 	subf    r27,r3,r0
    1f08:	fc 1f 08 00 	fcmpu   cr0,f31,f1
    1f0c:	41 82 00 e4 	beq     1ff0 <render_assign_slots__16TObjCMAssignMenuFv+0x1a0>
    1f10:	fc 01 f8 40 	fcmpo   cr0,f1,f31
    1f14:	40 80 00 30 	bge     1f44 <render_assign_slots__16TObjCMAssignMenuFv+0xf4>
    1f18:	c0 00 00 00 	lfs     f0,0(0)
			1f18: R_PPC_EMB_SDA21	lbl_805DDA70
    1f1c:	c0 60 00 00 	lfs     f3,0(0)
			1f1c: R_PPC_EMB_SDA21	lbl_805DDB5C
    1f20:	ec 80 08 28 	fsubs   f4,f0,f1
    1f24:	c0 40 00 00 	lfs     f2,0(0)
			1f24: R_PPC_EMB_SDA21	lbl_805DDB58
    1f28:	c0 20 00 00 	lfs     f1,0(0)
			1f28: R_PPC_EMB_SDA21	lbl_805DDB64
    1f2c:	c0 00 00 00 	lfs     f0,0(0)
			1f2c: R_PPC_EMB_SDA21	lbl_805DDB60
    1f30:	ec 43 11 3a 	fmadds  f2,f3,f4,f2
    1f34:	ec 01 01 3a 	fmadds  f0,f1,f4,f0
    1f38:	d0 41 00 08 	stfs    f2,8(r1)
    1f3c:	d0 01 00 0c 	stfs    f0,12(r1)
    1f40:	48 00 00 30 	b       1f70 <render_assign_slots__16TObjCMAssignMenuFv+0x120>
    1f44:	40 81 00 2c 	ble     1f70 <render_assign_slots__16TObjCMAssignMenuFv+0x120>
    1f48:	c0 00 00 00 	lfs     f0,0(0)
			1f48: R_PPC_EMB_SDA21	lbl_805DDA70
    1f4c:	c0 60 00 00 	lfs     f3,0(0)
			1f4c: R_PPC_EMB_SDA21	lbl_805DDB68
    1f50:	ec 80 08 2a 	fadds   f4,f0,f1
    1f54:	c0 40 00 00 	lfs     f2,0(0)
			1f54: R_PPC_EMB_SDA21	lbl_805DDA78
    1f58:	c0 20 00 00 	lfs     f1,0(0)
			1f58: R_PPC_EMB_SDA21	lbl_805DDB6C
    1f5c:	c0 00 00 00 	lfs     f0,0(0)
			1f5c: R_PPC_EMB_SDA21	lbl_805DDA98
    1f60:	ec 43 11 3a 	fmadds  f2,f3,f4,f2
    1f64:	ec 01 01 3a 	fmadds  f0,f1,f4,f0
    1f68:	d0 41 00 08 	stfs    f2,8(r1)
    1f6c:	d0 01 00 0c 	stfs    f0,12(r1)
    1f70:	3c 60 00 00 	lis     r3,0
			1f72: R_PPC_ADDR16_HA	lbl_80465050
    1f74:	c3 80 00 00 	lfs     f28,0(0)
			1f74: R_PPC_EMB_SDA21	TObjCMAssignMenu__data_805DDB20
    1f78:	3b c3 00 00 	addi    r30,r3,0
			1f7a: R_PPC_ADDR16_LO	lbl_80465050
    1f7c:	3b 40 00 00 	li      r26,0
    1f80:	48 00 00 2c 	b       1fac <render_assign_slots__16TObjCMAssignMenuFv+0x15c>
    1f84:	fc 40 e8 90 	fmr     f2,f29
    1f88:	c0 20 00 00 	lfs     f1,0(0)
			1f88: R_PPC_EMB_SDA21	lbl_805DDB70
    1f8c:	7f c5 f3 78 	mr      r5,r30
    1f90:	38 81 00 08 	addi    r4,r1,8
    1f94:	38 60 00 1f 	li      r3,31
    1f98:	48 00 00 01 	bl      1f98 <render_assign_slots__16TObjCMAssignMenuFv+0x148>
			1f98: R_PPC_REL24	draw_ui_sprite_scaled
    1f9c:	c0 01 00 08 	lfs     f0,8(r1)
    1fa0:	3b 5a 00 01 	addi    r26,r26,1
    1fa4:	ec 00 e0 2a 	fadds   f0,f0,f28
    1fa8:	d0 01 00 08 	stfs    f0,8(r1)
    1fac:	7c 1a d8 00 	cmpw    r26,r27
    1fb0:	41 80 ff d4 	blt     1f84 <render_assign_slots__16TObjCMAssignMenuFv+0x134>
    1fb4:	c0 81 00 08 	lfs     f4,8(r1)
    1fb8:	3c 60 00 00 	lis     r3,0
			1fba: R_PPC_ADDR16_HA	lbl_80465058
    1fbc:	c0 20 00 00 	lfs     f1,0(0)
			1fbc: R_PPC_EMB_SDA21	lbl_805DDB74
    1fc0:	38 a3 00 00 	addi    r5,r3,0
			1fc2: R_PPC_ADDR16_LO	lbl_80465058
    1fc4:	c0 61 00 0c 	lfs     f3,12(r1)
    1fc8:	fc 40 e8 90 	fmr     f2,f29
    1fcc:	ec 84 08 2a 	fadds   f4,f4,f1
    1fd0:	c0 00 00 00 	lfs     f0,0(0)
			1fd0: R_PPC_EMB_SDA21	lbl_805DDB78
    1fd4:	c0 20 00 00 	lfs     f1,0(0)
			1fd4: R_PPC_EMB_SDA21	lbl_805DDB70
    1fd8:	38 7c 00 14 	addi    r3,r28,20
    1fdc:	ec 03 00 2a 	fadds   f0,f3,f0
    1fe0:	d0 81 00 08 	stfs    f4,8(r1)
    1fe4:	38 81 00 08 	addi    r4,r1,8
    1fe8:	d0 01 00 0c 	stfs    f0,12(r1)
    1fec:	48 00 00 01 	bl      1fec <render_assign_slots__16TObjCMAssignMenuFv+0x19c>
			1fec: R_PPC_REL24	draw_ui_sprite_scaled
    1ff0:	3b 9c 00 01 	addi    r28,r28,1
    1ff4:	80 9f 00 4c 	lwz     r4,76(r31)
    1ff8:	7c 1c 20 00 	cmpw    r28,r4
    1ffc:	41 80 fe d0 	blt     1ecc <render_assign_slots__16TObjCMAssignMenuFv+0x7c>
    2000:	e3 e1 00 68 	psq_l   f31,104(r1),0,0
    2004:	cb e1 00 60 	lfd     f31,96(r1)
    2008:	e3 c1 00 58 	lq      r30,80(r1)
    200c:	cb c1 00 50 	lfd     f30,80(r1)
    2010:	e3 a1 00 48 	psq_l   f29,72(r1),0,0
    2014:	cb a1 00 40 	lfd     f29,64(r1)
    2018:	e3 81 00 38 	lq      r28,48(r1)
    201c:	cb 81 00 30 	lfd     f28,48(r1)
    2020:	bb 41 00 18 	lmw     r26,24(r1)
    2024:	80 01 00 74 	lwz     r0,116(r1)
    2028:	7c 08 03 a6 	mtlr    r0
    202c:	38 21 00 70 	addi    r1,r1,112
    2030:	4e 80 00 20 	blr

00002034 <render__16TObjCMAssignMenuFv>:
    2034:	94 21 ff 80 	stwu    r1,-128(r1)
    2038:	7c 08 02 a6 	mflr    r0
    203c:	90 01 00 84 	stw     r0,132(r1)
    2040:	db e1 00 70 	stfd    f31,112(r1)
    2044:	f3 e1 00 78 	xxsel   vs31,vs1,vs0,vs33
    2048:	db c1 00 60 	stfd    f30,96(r1)
    204c:	f3 c1 00 68 	psq_st  f30,104(r1),0,0
    2050:	db a1 00 50 	stfd    f29,80(r1)
    2054:	f3 a1 00 58 	xscmpgtdp vs29,vs1,vs0
    2058:	db 81 00 40 	stfd    f28,64(r1)
    205c:	f3 81 00 48 	xsmaddmsp vs28,vs1,vs0
    2060:	bf a1 00 34 	stmw    r29,52(r1)
    2064:	7c 7f 1b 78 	mr      r31,r3
    2068:	48 00 00 01 	bl      2068 <render__16TObjCMAssignMenuFv+0x34>
			2068: R_PPC_REL24	render_assign_slots__16TObjCMAssignMenuFv
    206c:	80 1f 00 38 	lwz     r0,56(r31)
    2070:	54 03 50 2a 	slwi    r3,r0,10
    2074:	48 00 00 01 	bl      2074 <render__16TObjCMAssignMenuFv+0x40>
			2074: R_PPC_REL24	sin_table_lookup
    2078:	c0 40 00 00 	lfs     f2,0(0)
			2078: R_PPC_EMB_SDA21	@407
    207c:	c0 00 00 00 	lfs     f0,0(0)
			207c: R_PPC_EMB_SDA21	@56
    2080:	ef e2 00 7a 	fmadds  f31,f2,f1,f0
    2084:	fc 1f 00 40 	fcmpo   cr0,f31,f0
    2088:	40 81 00 08 	ble     2090 <render__16TObjCMAssignMenuFv+0x5c>
    208c:	ff e0 00 90 	fmr     f31,f0
    2090:	80 7f 00 44 	lwz     r3,68(r31)
    2094:	34 03 ff ff 	addic.  r0,r3,-1
    2098:	40 80 00 0c 	bge     20a4 <render__16TObjCMAssignMenuFv+0x70>
    209c:	38 00 00 00 	li      r0,0
    20a0:	48 00 00 10 	b       20b0 <render__16TObjCMAssignMenuFv+0x7c>
    20a4:	2c 00 00 0a 	cmpwi   r0,10
    20a8:	41 80 00 08 	blt     20b0 <render__16TObjCMAssignMenuFv+0x7c>
    20ac:	38 00 00 09 	li      r0,9
    20b0:	c0 5f 00 40 	lfs     f2,64(r31)
    20b4:	3c 60 00 00 	lis     r3,0
			20b6: R_PPC_ADDR16_HA	char_creation_assign_menu_tab_positions
    20b8:	c0 20 00 00 	lfs     f1,0(0)
			20b8: R_PPC_EMB_SDA21	@85
    20bc:	54 00 10 3a 	slwi    r0,r0,2
    20c0:	38 63 00 00 	addi    r3,r3,0
			20c2: R_PPC_ADDR16_LO	char_creation_assign_menu_tab_positions
    20c4:	fc 02 08 40 	fcmpo   cr0,f2,f1
    20c8:	7f c3 04 2e 	lfsx    f30,r3,r0
    20cc:	4c 40 13 82 	cror    eq,lt,eq
    20d0:	41 82 00 a4 	beq     2174 <render__16TObjCMAssignMenuFv+0x140>
    20d4:	c0 00 00 00 	lfs     f0,0(0)
			20d4: R_PPC_EMB_SDA21	@86
    20d8:	fc 02 00 40 	fcmpo   cr0,f2,f0
    20dc:	4c 41 13 82 	cror    eq,gt,eq
    20e0:	40 82 00 0c 	bne     20ec <render__16TObjCMAssignMenuFv+0xb8>
    20e4:	c0 80 00 00 	lfs     f4,0(0)
			20e4: R_PPC_EMB_SDA21	@56
    20e8:	48 00 00 0c 	b       20f4 <render__16TObjCMAssignMenuFv+0xc0>
    20ec:	ec 02 08 28 	fsubs   f0,f2,f1
    20f0:	ec 80 08 24 	fdivs   f4,f0,f1
    20f4:	c0 20 00 00 	lfs     f1,0(0)
			20f4: R_PPC_EMB_SDA21	@118
    20f8:	c0 60 00 00 	lfs     f3,0(0)
			20f8: R_PPC_EMB_SDA21	@56
    20fc:	c0 40 00 00 	lfs     f2,0(0)
			20fc: R_PPC_EMB_SDA21	@408
    2100:	ec 1e 08 28 	fsubs   f0,f30,f1
    2104:	d0 61 00 1c 	stfs    f3,28(r1)
    2108:	d0 41 00 24 	stfs    f2,36(r1)
    210c:	ef 84 08 3a 	fmadds  f28,f4,f0,f1
    2110:	d0 21 00 20 	stfs    f1,32(r1)
    2114:	80 1f 00 38 	lwz     r0,56(r31)
    2118:	54 03 50 2a 	slwi    r3,r0,10
    211c:	48 00 00 01 	bl      211c <render__16TObjCMAssignMenuFv+0xe8>
			211c: R_PPC_REL24	sin_table_lookup
    2120:	c0 60 00 00 	lfs     f3,0(0)
			2120: R_PPC_EMB_SDA21	@90
    2124:	38 81 00 20 	addi    r4,r1,32
    2128:	c0 41 00 20 	lfs     f2,32(r1)
    212c:	38 a1 00 18 	addi    r5,r1,24
    2130:	c0 00 00 00 	lfs     f0,0(0)
			2130: R_PPC_EMB_SDA21	@91
    2134:	38 60 00 08 	li      r3,8
    2138:	ec 63 10 7a 	fmadds  f3,f3,f1,f2
    213c:	c0 20 00 00 	lfs     f1,0(0)
			213c: R_PPC_EMB_SDA21	@92
    2140:	ec 5c 18 28 	fsubs   f2,f28,f3
    2144:	d0 61 00 20 	stfs    f3,32(r1)
    2148:	ec 02 00 24 	fdivs   f0,f2,f0
    214c:	d0 01 00 18 	stfs    f0,24(r1)
    2150:	48 00 00 01 	bl      2150 <render__16TObjCMAssignMenuFv+0x11c>
			2150: R_PPC_REL24	draw_ui_sprite_opaque
    2154:	c0 00 00 00 	lfs     f0,0(0)
			2154: R_PPC_EMB_SDA21	@56
    2158:	38 81 00 20 	addi    r4,r1,32
    215c:	d3 81 00 20 	stfs    f28,32(r1)
    2160:	38 a1 00 18 	addi    r5,r1,24
    2164:	c0 20 00 00 	lfs     f1,0(0)
			2164: R_PPC_EMB_SDA21	@92
    2168:	38 60 00 09 	li      r3,9
    216c:	d0 01 00 18 	stfs    f0,24(r1)
    2170:	48 00 00 01 	bl      2170 <render__16TObjCMAssignMenuFv+0x13c>
			2170: R_PPC_REL24	draw_ui_sprite_opaque
    2174:	c0 5f 00 40 	lfs     f2,64(r31)
    2178:	c0 00 00 00 	lfs     f0,0(0)
			2178: R_PPC_EMB_SDA21	@54
    217c:	fc 02 00 40 	fcmpo   cr0,f2,f0
    2180:	4c 40 13 82 	cror    eq,lt,eq
    2184:	41 82 00 34 	beq     21b8 <render__16TObjCMAssignMenuFv+0x184>
    2188:	c0 00 00 00 	lfs     f0,0(0)
			2188: R_PPC_EMB_SDA21	@85
    218c:	3c 60 00 00 	lis     r3,0
			218e: R_PPC_ADDR16_HA	lbl_804DBCC8
    2190:	38 83 00 00 	addi    r4,r3,0
			2192: R_PPC_ADDR16_LO	lbl_804DBCC8
    2194:	c0 20 00 00 	lfs     f1,0(0)
			2194: R_PPC_EMB_SDA21	@93
    2198:	fc 02 00 40 	fcmpo   cr0,f2,f0
    219c:	38 60 00 00 	li      r3,0
    21a0:	4c 41 13 82 	cror    eq,gt,eq
    21a4:	40 82 00 0c 	bne     21b0 <render__16TObjCMAssignMenuFv+0x17c>
    21a8:	c0 40 00 00 	lfs     f2,0(0)
			21a8: R_PPC_EMB_SDA21	@56
    21ac:	48 00 00 08 	b       21b4 <render__16TObjCMAssignMenuFv+0x180>
    21b0:	ec 42 00 24 	fdivs   f2,f2,f0
    21b4:	48 00 00 01 	bl      21b4 <render__16TObjCMAssignMenuFv+0x180>
			21b4: R_PPC_REL24	draw_ui_sprite
    21b8:	c0 3f 00 40 	lfs     f1,64(r31)
    21bc:	c0 00 00 00 	lfs     f0,0(0)
			21bc: R_PPC_EMB_SDA21	@86
    21c0:	fc 01 00 40 	fcmpo   cr0,f1,f0
    21c4:	4c 40 13 82 	cror    eq,lt,eq
    21c8:	41 82 01 78 	beq     2340 <render__16TObjCMAssignMenuFv+0x30c>
    21cc:	ec 61 00 28 	fsubs   f3,f1,f0
    21d0:	c0 40 00 00 	lfs     f2,0(0)
			21d0: R_PPC_EMB_SDA21	@411
    21d4:	c0 20 00 00 	lfs     f1,0(0)
			21d4: R_PPC_EMB_SDA21	@412
    21d8:	3b c0 00 00 	li      r30,0
    21dc:	c0 00 00 00 	lfs     f0,0(0)
			21dc: R_PPC_EMB_SDA21	@122
    21e0:	ec 43 10 24 	fdivs   f2,f3,f2
    21e4:	d0 21 00 10 	stfs    f1,16(r1)
    21e8:	c3 80 00 00 	lfs     f28,0(0)
			21e8: R_PPC_EMB_SDA21	@415
    21ec:	d0 01 00 14 	stfs    f0,20(r1)
    21f0:	ef a2 00 b2 	fmuls   f29,f2,f2
    21f4:	48 00 00 6c 	b       2260 <render__16TObjCMAssignMenuFv+0x22c>
    21f8:	80 1f 00 54 	lwz     r0,84(r31)
    21fc:	fc 40 e8 90 	fmr     f2,f29
    2200:	3b a0 00 1f 	li      r29,31
    2204:	7c 1e 00 00 	cmpw    r30,r0
    2208:	40 82 00 38 	bne     2240 <render__16TObjCMAssignMenuFv+0x20c>
    220c:	80 00 00 00 	lwz     r0,0(0)
			220c: R_PPC_EMB_SDA21	creation_resource_ready_state
    2210:	3b a0 00 20 	li      r29,32
    2214:	2c 00 00 02 	cmpwi   r0,2
    2218:	41 82 00 24 	beq     223c <render__16TObjCMAssignMenuFv+0x208>
    221c:	80 1f 00 38 	lwz     r0,56(r31)
    2220:	54 03 60 26 	slwi    r3,r0,12
    2224:	48 00 00 01 	bl      2224 <render__16TObjCMAssignMenuFv+0x1f0>
			2224: R_PPC_REL24	sin_table_lookup
    2228:	48 00 00 01 	bl      2228 <render__16TObjCMAssignMenuFv+0x1f4>
			2228: R_PPC_REL24	fabs_float
    222c:	c0 00 00 00 	lfs     f0,0(0)
			222c: R_PPC_EMB_SDA21	@414
    2230:	ec 00 00 7a 	fmadds  f0,f0,f1,f0
    2234:	ec 5d 00 32 	fmuls   f2,f29,f0
    2238:	48 00 00 08 	b       2240 <render__16TObjCMAssignMenuFv+0x20c>
    223c:	ec 5d 07 f2 	fmuls   f2,f29,f31
    2240:	c0 20 00 00 	lfs     f1,0(0)
			2240: R_PPC_EMB_SDA21	@93
    2244:	7f a3 eb 78 	mr      r3,r29
    2248:	38 81 00 10 	addi    r4,r1,16
    224c:	48 00 00 01 	bl      224c <render__16TObjCMAssignMenuFv+0x218>
			224c: R_PPC_REL24	draw_ui_sprite
    2250:	c0 01 00 10 	lfs     f0,16(r1)
    2254:	3b de 00 01 	addi    r30,r30,1
    2258:	ec 00 e0 2a 	fadds   f0,f0,f28
    225c:	d0 01 00 10 	stfs    f0,16(r1)
    2260:	80 1f 00 50 	lwz     r0,80(r31)
    2264:	7c 1e 00 00 	cmpw    r30,r0
    2268:	41 80 ff 90 	blt     21f8 <render__16TObjCMAssignMenuFv+0x1c4>
    226c:	80 1f 00 4c 	lwz     r0,76(r31)
    2270:	2c 00 00 01 	cmpwi   r0,1
    2274:	40 81 00 44 	ble     22b8 <render__16TObjCMAssignMenuFv+0x284>
    2278:	c0 81 00 10 	lfs     f4,16(r1)
    227c:	3c 60 00 00 	lis     r3,0
			227e: R_PPC_ADDR16_HA	lbl_80465048
    2280:	c0 60 00 00 	lfs     f3,0(0)
			2280: R_PPC_EMB_SDA21	@622
    2284:	38 a3 00 00 	addi    r5,r3,0
			2286: R_PPC_ADDR16_LO	lbl_80465048
    2288:	c0 21 00 14 	lfs     f1,20(r1)
    228c:	fc 40 e8 90 	fmr     f2,f29
    2290:	c0 00 00 00 	lfs     f0,0(0)
			2290: R_PPC_EMB_SDA21	@623
    2294:	ec 64 18 2a 	fadds   f3,f4,f3
    2298:	80 7f 00 48 	lwz     r3,72(r31)
    229c:	38 81 00 10 	addi    r4,r1,16
    22a0:	ec 01 00 2a 	fadds   f0,f1,f0
    22a4:	d0 61 00 10 	stfs    f3,16(r1)
    22a8:	38 63 00 14 	addi    r3,r3,20
    22ac:	c0 20 00 00 	lfs     f1,0(0)
			22ac: R_PPC_EMB_SDA21	@93
    22b0:	d0 01 00 14 	stfs    f0,20(r1)
    22b4:	48 00 00 01 	bl      22b4 <render__16TObjCMAssignMenuFv+0x280>
			22b4: R_PPC_REL24	draw_ui_sprite_scaled
    22b8:	c0 20 00 00 	lfs     f1,0(0)
			22b8: R_PPC_EMB_SDA21	@416
    22bc:	ec 5d 07 f2 	fmuls   f2,f29,f31
    22c0:	c0 00 00 00 	lfs     f0,0(0)
			22c0: R_PPC_EMB_SDA21	@418
    22c4:	38 81 00 08 	addi    r4,r1,8
    22c8:	ef 9e 08 28 	fsubs   f28,f30,f1
    22cc:	c0 60 00 00 	lfs     f3,0(0)
			22cc: R_PPC_EMB_SDA21	@417
    22d0:	d0 01 00 0c 	stfs    f0,12(r1)
    22d4:	c0 20 00 00 	lfs     f1,0(0)
			22d4: R_PPC_EMB_SDA21	@93
    22d8:	ec 03 e0 2a 	fadds   f0,f3,f28
    22dc:	d0 01 00 08 	stfs    f0,8(r1)
    22e0:	80 7f 00 54 	lwz     r3,84(r31)
    22e4:	38 63 00 14 	addi    r3,r3,20
    22e8:	48 00 00 01 	bl      22e8 <render__16TObjCMAssignMenuFv+0x2b4>
			22e8: R_PPC_REL24	draw_ui_sprite
    22ec:	c0 20 00 00 	lfs     f1,0(0)
			22ec: R_PPC_EMB_SDA21	@419
    22f0:	fc 40 e8 90 	fmr     f2,f29
    22f4:	c0 00 00 00 	lfs     f0,0(0)
			22f4: R_PPC_EMB_SDA21	@122
    22f8:	38 81 00 08 	addi    r4,r1,8
    22fc:	ec 61 e0 2a 	fadds   f3,f1,f28
    2300:	c0 20 00 00 	lfs     f1,0(0)
			2300: R_PPC_EMB_SDA21	@93
    2304:	d0 01 00 0c 	stfs    f0,12(r1)
    2308:	38 60 00 1e 	li      r3,30
    230c:	d0 61 00 08 	stfs    f3,8(r1)
    2310:	48 00 00 01 	bl      2310 <render__16TObjCMAssignMenuFv+0x2dc>
			2310: R_PPC_REL24	draw_ui_sprite
    2314:	c0 20 00 00 	lfs     f1,0(0)
			2314: R_PPC_EMB_SDA21	@420
    2318:	fc 40 e8 90 	fmr     f2,f29
    231c:	c0 00 00 00 	lfs     f0,0(0)
			231c: R_PPC_EMB_SDA21	@421
    2320:	38 81 00 08 	addi    r4,r1,8
    2324:	ec 61 e0 2a 	fadds   f3,f1,f28
    2328:	c0 20 00 00 	lfs     f1,0(0)
			2328: R_PPC_EMB_SDA21	@93
    232c:	d0 01 00 0c 	stfs    f0,12(r1)
    2330:	d0 61 00 08 	stfs    f3,8(r1)
    2334:	80 7f 00 50 	lwz     r3,80(r31)
    2338:	38 63 00 13 	addi    r3,r3,19
    233c:	48 00 00 01 	bl      233c <render__16TObjCMAssignMenuFv+0x308>
			233c: R_PPC_REL24	draw_ui_sprite
    2340:	80 1f 00 24 	lwz     r0,36(r31)
    2344:	2c 00 00 01 	cmpwi   r0,1
    2348:	41 82 00 20 	beq     2368 <render__16TObjCMAssignMenuFv+0x334>
    234c:	40 80 00 40 	bge     238c <render__16TObjCMAssignMenuFv+0x358>
    2350:	2c 00 00 00 	cmpwi   r0,0
    2354:	40 80 00 08 	bge     235c <render__16TObjCMAssignMenuFv+0x328>
    2358:	48 00 00 34 	b       238c <render__16TObjCMAssignMenuFv+0x358>
    235c:	7f e3 fb 78 	mr      r3,r31
    2360:	48 00 00 01 	bl      2360 <render__16TObjCMAssignMenuFv+0x32c>
			2360: R_PPC_REL24	sub_80296648__16TObjCMAssignMenuFv
    2364:	48 00 00 28 	b       238c <render__16TObjCMAssignMenuFv+0x358>
    2368:	80 7f 00 1c 	lwz     r3,28(r31)
    236c:	80 03 00 34 	lwz     r0,52(r3)
    2370:	54 00 06 f7 	rlwinm. r0,r0,0,27,27
    2374:	41 82 00 10 	beq     2384 <render__16TObjCMAssignMenuFv+0x350>
    2378:	7f e3 fb 78 	mr      r3,r31
    237c:	48 00 00 01 	bl      237c <render__16TObjCMAssignMenuFv+0x348>
			237c: R_PPC_REL24	sub_80296648__16TObjCMAssignMenuFv
    2380:	48 00 00 0c 	b       238c <render__16TObjCMAssignMenuFv+0x358>
    2384:	7f e3 fb 78 	mr      r3,r31
    2388:	48 00 00 01 	bl      2388 <render__16TObjCMAssignMenuFv+0x354>
			2388: R_PPC_REL24	draw_assign_icons__16TObjCMAssignMenuFv
    238c:	e3 e1 00 78 	psq_l   f31,120(r1),0,0
    2390:	cb e1 00 70 	lfd     f31,112(r1)
    2394:	e3 c1 00 68 	lq      r30,96(r1)
    2398:	cb c1 00 60 	lfd     f30,96(r1)
    239c:	e3 a1 00 58 	psq_l   f29,88(r1),0,0
    23a0:	cb a1 00 50 	lfd     f29,80(r1)
    23a4:	e3 81 00 48 	lq      r28,64(r1)
    23a8:	cb 81 00 40 	lfd     f28,64(r1)
    23ac:	bb a1 00 34 	lmw     r29,52(r1)
    23b0:	80 01 00 84 	lwz     r0,132(r1)
    23b4:	7c 08 03 a6 	mtlr    r0
    23b8:	38 21 00 80 	addi    r1,r1,128
    23bc:	4e 80 00 20 	blr

000023c0 <calc_grid_layout__16TObjCMAssignMenuFv>:
    23c0:	80 03 00 2c 	lwz     r0,44(r3)
    23c4:	38 c0 00 00 	li      r6,0
    23c8:	38 80 00 00 	li      r4,0
    23cc:	7c 09 03 a6 	mtctr   r0
    23d0:	2c 00 00 00 	cmpwi   r0,0
    23d4:	40 81 00 1c 	ble     23f0 <calc_grid_layout__16TObjCMAssignMenuFv+0x30>
    23d8:	80 03 00 28 	lwz     r0,40(r3)
    23dc:	7c 04 00 00 	cmpw    r4,r0
    23e0:	41 82 00 10 	beq     23f0 <calc_grid_layout__16TObjCMAssignMenuFv+0x30>
    23e4:	38 c6 00 01 	addi    r6,r6,1
    23e8:	38 84 00 01 	addi    r4,r4,1
    23ec:	42 00 ff ec 	bdnz    23d8 <calc_grid_layout__16TObjCMAssignMenuFv+0x18>
    23f0:	80 a3 00 30 	lwz     r5,48(r3)
    23f4:	38 80 00 00 	li      r4,0
    23f8:	38 00 00 01 	li      r0,1
    23fc:	90 a3 00 44 	stw     r5,68(r3)
    2400:	90 83 00 48 	stw     r4,72(r3)
    2404:	90 03 00 4c 	stw     r0,76(r3)
    2408:	80 03 00 30 	lwz     r0,48(r3)
    240c:	90 03 00 50 	stw     r0,80(r3)
    2410:	90 c3 00 54 	stw     r6,84(r3)
    2414:	80 03 00 30 	lwz     r0,48(r3)
    2418:	2c 00 00 0a 	cmpwi   r0,10
    241c:	4c 81 00 20 	blelr
    2420:	38 a0 00 09 	li      r5,9
    2424:	7c 06 2b d6 	divw    r0,r6,r5
    2428:	90 a3 00 44 	stw     r5,68(r3)
    242c:	90 03 00 48 	stw     r0,72(r3)
    2430:	7c 00 29 d6 	mullw   r0,r0,r5
    2434:	80 83 00 30 	lwz     r4,48(r3)
    2438:	38 84 00 08 	addi    r4,r4,8
    243c:	7c 84 2b d6 	divw    r4,r4,r5
    2440:	7c 00 30 50 	subf    r0,r0,r6
    2444:	90 83 00 4c 	stw     r4,76(r3)
    2448:	90 03 00 54 	stw     r0,84(r3)
    244c:	80 83 00 48 	lwz     r4,72(r3)
    2450:	80 03 00 30 	lwz     r0,48(r3)
    2454:	1c 84 00 09 	mulli   r4,r4,9
    2458:	7c 04 00 50 	subf    r0,r4,r0
    245c:	90 03 00 50 	stw     r0,80(r3)
    2460:	80 03 00 50 	lwz     r0,80(r3)
    2464:	2c 00 00 09 	cmpwi   r0,9
    2468:	4c 81 00 20 	blelr
    246c:	90 a3 00 50 	stw     r5,80(r3)
    2470:	4e 80 00 20 	blr

00002474 <run_task__16TObjCMAssignMenuFv>:
    2474:	94 21 ff e0 	stwu    r1,-32(r1)
    2478:	7c 08 02 a6 	mflr    r0
    247c:	90 01 00 24 	stw     r0,36(r1)
    2480:	bf 81 00 10 	stmw    r28,16(r1)
    2484:	7c 7e 1b 78 	mr      r30,r3
    2488:	80 83 00 38 	lwz     r4,56(r3)
    248c:	38 04 00 01 	addi    r0,r4,1
    2490:	90 03 00 38 	stw     r0,56(r3)
    2494:	80 03 00 3c 	lwz     r0,60(r3)
    2498:	2c 00 00 00 	cmpwi   r0,0
    249c:	40 82 00 30 	bne     24cc <run_task__16TObjCMAssignMenuFv+0x58>
    24a0:	c0 5e 00 40 	lfs     f2,64(r30)
    24a4:	c0 20 00 00 	lfs     f1,0(0)
			24a4: R_PPC_EMB_SDA21	lbl_805DDAA8
    24a8:	c0 00 00 00 	lfs     f0,0(0)
			24a8: R_PPC_EMB_SDA21	lbl_805DDA90
    24ac:	ec 22 08 2a 	fadds   f1,f2,f1
    24b0:	fc 01 00 40 	fcmpo   cr0,f1,f0
    24b4:	d0 3e 00 40 	stfs    f1,64(r30)
    24b8:	4c 40 13 82 	cror    eq,lt,eq
    24bc:	40 82 02 bc 	bne     2778 <run_task__16TObjCMAssignMenuFv+0x304>
    24c0:	d0 1e 00 40 	stfs    f0,64(r30)
    24c4:	48 00 00 01 	bl      24c4 <run_task__16TObjCMAssignMenuFv+0x50>
			24c4: R_PPC_REL24	queue_destruction__7TObjectFv
    24c8:	48 00 02 b0 	b       2778 <run_task__16TObjCMAssignMenuFv+0x304>
    24cc:	c0 5e 00 40 	lfs     f2,64(r30)
    24d0:	c0 20 00 00 	lfs     f1,0(0)
			24d0: R_PPC_EMB_SDA21	lbl_805DDAAC
    24d4:	c0 00 00 00 	lfs     f0,0(0)
			24d4: R_PPC_EMB_SDA21	lbl_805DDA70
    24d8:	ec 22 08 2a 	fadds   f1,f2,f1
    24dc:	fc 01 00 40 	fcmpo   cr0,f1,f0
    24e0:	d0 3e 00 40 	stfs    f1,64(r30)
    24e4:	40 81 00 08 	ble     24ec <run_task__16TObjCMAssignMenuFv+0x78>
    24e8:	d0 1e 00 40 	stfs    f0,64(r30)
    24ec:	80 1e 00 20 	lwz     r0,32(r30)
    24f0:	3b 80 00 00 	li      r28,0
    24f4:	2c 00 00 00 	cmpwi   r0,0
    24f8:	41 82 00 6c 	beq     2564 <run_task__16TObjCMAssignMenuFv+0xf0>
    24fc:	38 60 00 80 	li      r3,128
    2500:	48 00 00 01 	bl      2500 <run_task__16TObjCMAssignMenuFv+0x8c>
			2500: R_PPC_REL24	creation_direction_repeated__Fl
    2504:	2c 03 00 00 	cmpwi   r3,0
    2508:	41 82 00 0c 	beq     2514 <run_task__16TObjCMAssignMenuFv+0xa0>
    250c:	3b 80 00 01 	li      r28,1
    2510:	48 00 00 18 	b       2528 <run_task__16TObjCMAssignMenuFv+0xb4>
    2514:	38 60 00 40 	li      r3,64
    2518:	48 00 00 01 	bl      2518 <run_task__16TObjCMAssignMenuFv+0xa4>
			2518: R_PPC_REL24	creation_direction_repeated__Fl
    251c:	2c 03 00 00 	cmpwi   r3,0
    2520:	41 82 00 08 	beq     2528 <run_task__16TObjCMAssignMenuFv+0xb4>
    2524:	3b 80 ff ff 	li      r28,-1
    2528:	80 1e 00 4c 	lwz     r0,76(r30)
    252c:	2c 00 00 01 	cmpwi   r0,1
    2530:	40 81 00 34 	ble     2564 <run_task__16TObjCMAssignMenuFv+0xf0>
    2534:	38 60 00 20 	li      r3,32
    2538:	48 00 00 01 	bl      2538 <run_task__16TObjCMAssignMenuFv+0xc4>
			2538: R_PPC_REL24	creation_direction_repeated__Fl
    253c:	2c 03 00 00 	cmpwi   r3,0
    2540:	41 82 00 0c 	beq     254c <run_task__16TObjCMAssignMenuFv+0xd8>
    2544:	83 9e 00 44 	lwz     r28,68(r30)
    2548:	48 00 00 1c 	b       2564 <run_task__16TObjCMAssignMenuFv+0xf0>
    254c:	38 60 00 10 	li      r3,16
    2550:	48 00 00 01 	bl      2550 <run_task__16TObjCMAssignMenuFv+0xdc>
			2550: R_PPC_REL24	creation_direction_repeated__Fl
    2554:	2c 03 00 00 	cmpwi   r3,0
    2558:	41 82 00 0c 	beq     2564 <run_task__16TObjCMAssignMenuFv+0xf0>
    255c:	80 1e 00 44 	lwz     r0,68(r30)
    2560:	7f 80 00 d0 	neg     r28,r0
    2564:	2c 1c 00 00 	cmpwi   r28,0
    2568:	41 82 00 dc 	beq     2644 <run_task__16TObjCMAssignMenuFv+0x1d0>
    256c:	80 1e 00 24 	lwz     r0,36(r30)
    2570:	2c 1c 00 01 	cmpwi   r28,1
    2574:	83 be 00 1c 	lwz     r29,28(r30)
    2578:	54 03 08 3c 	slwi    r3,r0,1
    257c:	3b e3 00 38 	addi    r31,r3,56
    2580:	7c dd fa ae 	lhax    r6,r29,r31
    2584:	7c 06 e2 14 	add     r0,r6,r28
    2588:	7c 1d fb 2e 	sthx    r0,r29,r31
    258c:	41 82 00 0c 	beq     2598 <run_task__16TObjCMAssignMenuFv+0x124>
    2590:	2c 1c ff ff 	cmpwi   r28,-1
    2594:	40 82 00 34 	bne     25c8 <run_task__16TObjCMAssignMenuFv+0x154>
    2598:	7c 1d fa ae 	lhax    r0,r29,r31
    259c:	80 7e 00 2c 	lwz     r3,44(r30)
    25a0:	7c 00 18 00 	cmpw    r0,r3
    25a4:	41 80 00 10 	blt     25b4 <run_task__16TObjCMAssignMenuFv+0x140>
    25a8:	38 00 00 00 	li      r0,0
    25ac:	7c 1d fb 2e 	sthx    r0,r29,r31
    25b0:	48 00 00 68 	b       2618 <run_task__16TObjCMAssignMenuFv+0x1a4>
    25b4:	7c 00 07 35 	extsh.  r0,r0
    25b8:	40 80 00 60 	bge     2618 <run_task__16TObjCMAssignMenuFv+0x1a4>
    25bc:	38 03 ff ff 	addi    r0,r3,-1
    25c0:	7c 1d fb 2e 	sthx    r0,r29,r31
    25c4:	48 00 00 54 	b       2618 <run_task__16TObjCMAssignMenuFv+0x1a4>
    25c8:	80 9e 00 44 	lwz     r4,68(r30)
    25cc:	7c 7d fa ae 	lhax    r3,r29,r31
    25d0:	7c 06 23 d6 	divw    r0,r6,r4
    25d4:	80 be 00 30 	lwz     r5,48(r30)
    25d8:	7c 03 28 00 	cmpw    r3,r5
    25dc:	7c 00 21 d6 	mullw   r0,r0,r4
    25e0:	7c 00 30 50 	subf    r0,r0,r6
    25e4:	7c 07 07 34 	extsh   r7,r0
    25e8:	41 80 00 0c 	blt     25f4 <run_task__16TObjCMAssignMenuFv+0x180>
    25ec:	7c fd fb 2e 	sthx    r7,r29,r31
    25f0:	48 00 00 28 	b       2618 <run_task__16TObjCMAssignMenuFv+0x1a4>
    25f4:	7c 60 07 35 	extsh.  r0,r3
    25f8:	40 80 00 20 	bge     2618 <run_task__16TObjCMAssignMenuFv+0x1a4>
    25fc:	7c e3 3b 78 	mr      r3,r7
    2600:	48 00 00 08 	b       2608 <run_task__16TObjCMAssignMenuFv+0x194>
    2604:	7c 63 22 14 	add     r3,r3,r4
    2608:	7c 03 22 14 	add     r0,r3,r4
    260c:	7c 00 28 00 	cmpw    r0,r5
    2610:	41 80 ff f4 	blt     2604 <run_task__16TObjCMAssignMenuFv+0x190>
    2614:	7c 7d fb 2e 	sthx    r3,r29,r31
    2618:	7c 1d fa ae 	lhax    r0,r29,r31
    261c:	7c 00 30 00 	cmpw    r0,r6
    2620:	41 82 00 1c 	beq     263c <run_task__16TObjCMAssignMenuFv+0x1c8>
    2624:	3c 60 00 05 	lis     r3,5
    2628:	38 80 00 00 	li      r4,0
    262c:	38 63 41 00 	addi    r3,r3,16640
    2630:	38 a0 00 00 	li      r5,0
    2634:	38 c0 00 00 	li      r6,0
    2638:	48 00 00 01 	bl      2638 <run_task__16TObjCMAssignMenuFv+0x1c4>
			2638: R_PPC_REL24	play_sound_effect
    263c:	7c 1d fa ae 	lhax    r0,r29,r31
    2640:	90 1e 00 28 	stw     r0,40(r30)
    2644:	7f c3 f3 78 	mr      r3,r30
    2648:	48 00 00 01 	bl      2648 <run_task__16TObjCMAssignMenuFv+0x1d4>
			2648: R_PPC_REL24	calc_grid_layout__16TObjCMAssignMenuFv
    264c:	80 1e 00 48 	lwz     r0,72(r30)
    2650:	3c 60 43 30 	lis     r3,17200
    2654:	3c 80 00 00 	lis     r4,0
			2656: R_PPC_ADDR16_HA	@268
    2658:	90 61 00 08 	stw     r3,8(r1)
    265c:	6c 00 80 00 	xoris   r0,r0,32768
    2660:	c8 44 00 00 	lfd     f2,0(r4)
			2662: R_PPC_ADDR16_LO	@268
    2664:	90 01 00 0c 	stw     r0,12(r1)
    2668:	c0 3e 00 58 	lfs     f1,88(r30)
    266c:	c8 01 00 08 	lfd     f0,8(r1)
    2670:	ec 00 10 28 	fsubs   f0,f0,f2
    2674:	fc 01 00 40 	fcmpo   cr0,f1,f0
    2678:	40 80 00 4c 	bge     26c4 <run_task__16TObjCMAssignMenuFv+0x250>
    267c:	c0 00 00 00 	lfs     f0,0(0)
			267c: R_PPC_EMB_SDA21	lbl_805DDB80
    2680:	90 61 00 08 	stw     r3,8(r1)
    2684:	ec 01 00 2a 	fadds   f0,f1,f0
    2688:	d0 1e 00 58 	stfs    f0,88(r30)
    268c:	80 1e 00 48 	lwz     r0,72(r30)
    2690:	c0 3e 00 58 	lfs     f1,88(r30)
    2694:	6c 00 80 00 	xoris   r0,r0,32768
    2698:	90 01 00 0c 	stw     r0,12(r1)
    269c:	c8 01 00 08 	lfd     f0,8(r1)
    26a0:	ec 00 10 28 	fsubs   f0,f0,f2
    26a4:	fc 01 00 40 	fcmpo   cr0,f1,f0
    26a8:	40 81 00 78 	ble     2720 <run_task__16TObjCMAssignMenuFv+0x2ac>
    26ac:	90 01 00 0c 	stw     r0,12(r1)
    26b0:	90 61 00 08 	stw     r3,8(r1)
    26b4:	c8 01 00 08 	lfd     f0,8(r1)
    26b8:	ec 00 10 28 	fsubs   f0,f0,f2
    26bc:	d0 1e 00 58 	stfs    f0,88(r30)
    26c0:	48 00 00 60 	b       2720 <run_task__16TObjCMAssignMenuFv+0x2ac>
    26c4:	90 01 00 0c 	stw     r0,12(r1)
    26c8:	90 61 00 08 	stw     r3,8(r1)
    26cc:	c8 01 00 08 	lfd     f0,8(r1)
    26d0:	ec 00 10 28 	fsubs   f0,f0,f2
    26d4:	fc 01 00 40 	fcmpo   cr0,f1,f0
    26d8:	40 81 00 48 	ble     2720 <run_task__16TObjCMAssignMenuFv+0x2ac>
    26dc:	c0 00 00 00 	lfs     f0,0(0)
			26dc: R_PPC_EMB_SDA21	lbl_805DDB80
    26e0:	90 61 00 08 	stw     r3,8(r1)
    26e4:	ec 01 00 28 	fsubs   f0,f1,f0
    26e8:	d0 1e 00 58 	stfs    f0,88(r30)
    26ec:	80 1e 00 48 	lwz     r0,72(r30)
    26f0:	c0 3e 00 58 	lfs     f1,88(r30)
    26f4:	6c 00 80 00 	xoris   r0,r0,32768
    26f8:	90 01 00 0c 	stw     r0,12(r1)
    26fc:	c8 01 00 08 	lfd     f0,8(r1)
    2700:	ec 00 10 28 	fsubs   f0,f0,f2
    2704:	fc 01 00 40 	fcmpo   cr0,f1,f0
    2708:	40 80 00 18 	bge     2720 <run_task__16TObjCMAssignMenuFv+0x2ac>
    270c:	90 01 00 0c 	stw     r0,12(r1)
    2710:	90 61 00 08 	stw     r3,8(r1)
    2714:	c8 01 00 08 	lfd     f0,8(r1)
    2718:	ec 00 10 28 	fsubs   f0,f0,f2
    271c:	d0 1e 00 58 	stfs    f0,88(r30)
    2720:	80 1e 00 20 	lwz     r0,32(r30)
    2724:	2c 00 00 00 	cmpwi   r0,0
    2728:	41 82 00 3c 	beq     2764 <run_task__16TObjCMAssignMenuFv+0x2f0>
    272c:	38 60 00 06 	li      r3,6
    2730:	48 00 00 01 	bl      2730 <run_task__16TObjCMAssignMenuFv+0x2bc>
			2730: R_PPC_REL24	creation_buttons_pressed__Fl
    2734:	2c 03 00 00 	cmpwi   r3,0
    2738:	41 82 00 2c 	beq     2764 <run_task__16TObjCMAssignMenuFv+0x2f0>
    273c:	3c 60 00 05 	lis     r3,5
    2740:	38 80 00 00 	li      r4,0
    2744:	38 63 37 04 	addi    r3,r3,14084
    2748:	38 a0 00 00 	li      r5,0
    274c:	38 c0 00 00 	li      r6,0
    2750:	48 00 00 01 	bl      2750 <run_task__16TObjCMAssignMenuFv+0x2dc>
			2750: R_PPC_REL24	play_sound_effect
    2754:	48 00 00 01 	bl      2754 <run_task__16TObjCMAssignMenuFv+0x2e0>
			2754: R_PPC_REL24	clear_task_state__14TObjCMMainMenuFv
    2758:	38 00 00 00 	li      r0,0
    275c:	90 1e 00 3c 	stw     r0,60(r30)
    2760:	48 00 00 18 	b       2778 <run_task__16TObjCMAssignMenuFv+0x304>
    2764:	80 1e 00 20 	lwz     r0,32(r30)
    2768:	2c 00 00 00 	cmpwi   r0,0
    276c:	40 82 00 0c 	bne     2778 <run_task__16TObjCMAssignMenuFv+0x304>
    2770:	38 00 00 01 	li      r0,1
    2774:	90 1e 00 20 	stw     r0,32(r30)
    2778:	bb 81 00 10 	lmw     r28,16(r1)
    277c:	80 01 00 24 	lwz     r0,36(r1)
    2780:	7c 08 03 a6 	mtlr    r0
    2784:	38 21 00 20 	addi    r1,r1,32
    2788:	4e 80 00 20 	blr

0000278c <create__16TObjCMAssignMenuFPvPv>:
    278c:	94 21 ff f0 	stwu    r1,-16(r1)
    2790:	7c 08 02 a6 	mflr    r0
    2794:	90 01 00 14 	stw     r0,20(r1)
    2798:	bf c1 00 08 	stmw    r30,8(r1)
    279c:	7c 7e 1b 78 	mr      r30,r3
    27a0:	7c 9f 23 78 	mr      r31,r4
    27a4:	38 60 00 5c 	li      r3,92
    27a8:	48 00 00 01 	bl      27a8 <create__16TObjCMAssignMenuFPvPv+0x1c>
			27a8: R_PPC_REL24	__nw__7TObjectFUl
    27ac:	7c 60 1b 79 	mr.     r0,r3
    27b0:	41 82 00 14 	beq     27c4 <create__16TObjCMAssignMenuFPvPv+0x38>
    27b4:	7f c4 f3 78 	mr      r4,r30
    27b8:	7f e5 fb 78 	mr      r5,r31
    27bc:	48 00 00 01 	bl      27bc <create__16TObjCMAssignMenuFPvPv+0x30>
			27bc: R_PPC_REL24	__ct__16TObjCMAssignMenuFv
    27c0:	7c 60 1b 78 	mr      r0,r3
    27c4:	7c 03 03 78 	mr      r3,r0
    27c8:	bb c1 00 08 	lmw     r30,8(r1)
    27cc:	80 01 00 14 	lwz     r0,20(r1)
    27d0:	7c 08 03 a6 	mtlr    r0
    27d4:	38 21 00 10 	addi    r1,r1,16
    27d8:	4e 80 00 20 	blr

000027dc <__dt__16TObjCMAssignMenuFv>:
    27dc:	94 21 ff f0 	stwu    r1,-16(r1)
    27e0:	7c 08 02 a6 	mflr    r0
    27e4:	90 01 00 14 	stw     r0,20(r1)
    27e8:	bf c1 00 08 	stmw    r30,8(r1)
    27ec:	7c 7e 1b 79 	mr.     r30,r3
    27f0:	7c 9f 23 78 	mr      r31,r4
    27f4:	41 82 00 28 	beq     281c <__dt__16TObjCMAssignMenuFv+0x40>
    27f8:	3c a0 00 00 	lis     r5,0
			27fa: R_PPC_ADDR16_HA	__vt__16TObjCMAssignMenu
    27fc:	38 80 00 00 	li      r4,0
    2800:	38 05 00 00 	addi    r0,r5,0
			2802: R_PPC_ADDR16_LO	__vt__16TObjCMAssignMenu
    2804:	90 1e 00 18 	stw     r0,24(r30)
    2808:	48 00 00 01 	bl      2808 <__dt__16TObjCMAssignMenuFv+0x2c>
			2808: R_PPC_REL24	__dt__7TObjectFv
    280c:	7f e0 07 35 	extsh.  r0,r31
    2810:	40 81 00 0c 	ble     281c <__dt__16TObjCMAssignMenuFv+0x40>
    2814:	7f c3 f3 78 	mr      r3,r30
    2818:	48 00 00 01 	bl      2818 <__dt__16TObjCMAssignMenuFv+0x3c>
			2818: R_PPC_REL24	__dl__7TObjectFPv
    281c:	7f c3 f3 78 	mr      r3,r30
    2820:	bb c1 00 08 	lmw     r30,8(r1)
    2824:	80 01 00 14 	lwz     r0,20(r1)
    2828:	7c 08 03 a6 	mtlr    r0
    282c:	38 21 00 10 	addi    r1,r1,16
    2830:	4e 80 00 20 	blr

00002834 <__ct__16TObjCMAssignMenuFv>:
    2834:	94 21 ff e0 	stwu    r1,-32(r1)
    2838:	7c 08 02 a6 	mflr    r0
    283c:	90 01 00 24 	stw     r0,36(r1)
    2840:	bf c1 00 18 	stmw    r30,24(r1)
    2844:	7c 7f 1b 78 	mr      r31,r3
    2848:	7c be 2b 78 	mr      r30,r5
    284c:	48 00 00 01 	bl      284c <__ct__16TObjCMAssignMenuFv+0x18>
			284c: R_PPC_REL24	__ct__7TObjectFP7TObject
    2850:	3c 60 00 00 	lis     r3,0
			2852: R_PPC_ADDR16_HA	__vt__16TObjCMAssignMenu
    2854:	38 00 00 00 	li      r0,0
    2858:	38 63 00 00 	addi    r3,r3,0
			285a: R_PPC_ADDR16_LO	__vt__16TObjCMAssignMenu
    285c:	90 7f 00 18 	stw     r3,24(r31)
    2860:	80 60 00 00 	lwz     r3,0(0)
			2860: R_PPC_EMB_SDA21	lbl_805D3CDC
    2864:	90 7f 00 00 	stw     r3,0(r31)
    2868:	80 60 00 00 	lwz     r3,0(0)
			2868: R_PPC_EMB_SDA21	creation_player_character
    286c:	90 7f 00 1c 	stw     r3,28(r31)
    2870:	90 1f 00 20 	stw     r0,32(r31)
    2874:	93 df 00 24 	stw     r30,36(r31)
    2878:	80 7f 00 1c 	lwz     r3,28(r31)
    287c:	48 00 00 01 	bl      287c <__ct__16TObjCMAssignMenuFv+0x48>
			287c: R_PPC_REL24	get_display_index__12TCharaMakingFv
    2880:	1c a3 00 2c 	mulli   r5,r3,44
    2884:	80 1f 00 24 	lwz     r0,36(r31)
    2888:	3c 80 00 00 	lis     r4,0
			288a: R_PPC_ADDR16_HA	class_appearance_table
    288c:	54 03 08 3c 	slwi    r3,r0,1
    2890:	38 84 00 00 	addi    r4,r4,0
			2892: R_PPC_ADDR16_LO	class_appearance_table
    2894:	38 00 00 00 	li      r0,0
    2898:	7c 84 2a 14 	add     r4,r4,r5
    289c:	38 a0 00 01 	li      r5,1
    28a0:	7c 64 1a ae 	lhax    r3,r4,r3
    28a4:	38 c0 00 00 	li      r6,0
    28a8:	90 7f 00 2c 	stw     r3,44(r31)
    28ac:	80 7f 00 24 	lwz     r3,36(r31)
    28b0:	80 9f 00 1c 	lwz     r4,28(r31)
    28b4:	54 63 08 3c 	slwi    r3,r3,1
    28b8:	7c 64 1a 14 	add     r3,r4,r3
    28bc:	a8 63 00 38 	lha     r3,56(r3)
    28c0:	90 7f 00 28 	stw     r3,40(r31)
    28c4:	90 1f 00 30 	stw     r0,48(r31)
    28c8:	90 1f 00 34 	stw     r0,52(r31)
    28cc:	48 00 00 24 	b       28f0 <__ct__16TObjCMAssignMenuFv+0xbc>
    28d0:	80 7f 00 30 	lwz     r3,48(r31)
    28d4:	38 c6 00 01 	addi    r6,r6,1
    28d8:	38 03 00 01 	addi    r0,r3,1
    28dc:	90 1f 00 30 	stw     r0,48(r31)
    28e0:	80 1f 00 34 	lwz     r0,52(r31)
    28e4:	7c 00 2b 78 	or      r0,r0,r5
    28e8:	54 a5 08 3c 	slwi    r5,r5,1
    28ec:	90 1f 00 34 	stw     r0,52(r31)
    28f0:	80 1f 00 2c 	lwz     r0,44(r31)
    28f4:	7c 06 00 00 	cmpw    r6,r0
    28f8:	41 80 ff d8 	blt     28d0 <__ct__16TObjCMAssignMenuFv+0x9c>
    28fc:	7f e3 fb 78 	mr      r3,r31
    2900:	48 00 00 01 	bl      2900 <__ct__16TObjCMAssignMenuFv+0xcc>
			2900: R_PPC_REL24	calc_grid_layout__16TObjCMAssignMenuFv
    2904:	80 7f 00 48 	lwz     r3,72(r31)
    2908:	3c 00 43 30 	lis     r0,17200
    290c:	90 01 00 08 	stw     r0,8(r1)
    2910:	3c 80 00 00 	lis     r4,0
			2912: R_PPC_ADDR16_HA	@268
    2914:	6c 63 80 00 	xoris   r3,r3,32768
    2918:	c8 44 00 00 	lfd     f2,0(r4)
			291a: R_PPC_ADDR16_LO	@268
    291c:	90 61 00 0c 	stw     r3,12(r1)
    2920:	38 00 00 01 	li      r0,1
    2924:	c0 00 00 00 	lfs     f0,0(0)
			2924: R_PPC_EMB_SDA21	lbl_805DDA90
    2928:	c8 21 00 08 	lfd     f1,8(r1)
    292c:	ec 21 10 28 	fsubs   f1,f1,f2
    2930:	d0 3f 00 58 	stfs    f1,88(r31)
    2934:	90 1f 00 3c 	stw     r0,60(r31)
    2938:	d0 1f 00 40 	stfs    f0,64(r31)
    293c:	80 1f 00 24 	lwz     r0,36(r31)
    2940:	2c 00 00 02 	cmpwi   r0,2
    2944:	41 82 00 58 	beq     299c <__ct__16TObjCMAssignMenuFv+0x168>
    2948:	40 80 00 14 	bge     295c <__ct__16TObjCMAssignMenuFv+0x128>
    294c:	2c 00 00 00 	cmpwi   r0,0
    2950:	41 82 00 18 	beq     2968 <__ct__16TObjCMAssignMenuFv+0x134>
    2954:	40 80 00 20 	bge     2974 <__ct__16TObjCMAssignMenuFv+0x140>
    2958:	48 00 00 58 	b       29b0 <__ct__16TObjCMAssignMenuFv+0x17c>
    295c:	2c 00 00 04 	cmpwi   r0,4
    2960:	40 80 00 50 	bge     29b0 <__ct__16TObjCMAssignMenuFv+0x17c>
    2964:	48 00 00 44 	b       29a8 <__ct__16TObjCMAssignMenuFv+0x174>
    2968:	38 60 00 06 	li      r3,6
    296c:	48 00 00 01 	bl      296c <__ct__16TObjCMAssignMenuFv+0x138>
			296c: R_PPC_REL24	set_eff_tag__11TChCrEffTagFi
    2970:	48 00 00 40 	b       29b0 <__ct__16TObjCMAssignMenuFv+0x17c>
    2974:	80 7f 00 1c 	lwz     r3,28(r31)
    2978:	80 03 00 34 	lwz     r0,52(r3)
    297c:	54 00 06 f7 	rlwinm. r0,r0,0,27,27
    2980:	41 82 00 10 	beq     2990 <__ct__16TObjCMAssignMenuFv+0x15c>
    2984:	38 60 00 08 	li      r3,8
    2988:	48 00 00 01 	bl      2988 <__ct__16TObjCMAssignMenuFv+0x154>
			2988: R_PPC_REL24	set_eff_tag__11TChCrEffTagFi
    298c:	48 00 00 24 	b       29b0 <__ct__16TObjCMAssignMenuFv+0x17c>
    2990:	38 60 00 07 	li      r3,7
    2994:	48 00 00 01 	bl      2994 <__ct__16TObjCMAssignMenuFv+0x160>
			2994: R_PPC_REL24	set_eff_tag__11TChCrEffTagFi
    2998:	48 00 00 18 	b       29b0 <__ct__16TObjCMAssignMenuFv+0x17c>
    299c:	38 60 00 04 	li      r3,4
    29a0:	48 00 00 01 	bl      29a0 <__ct__16TObjCMAssignMenuFv+0x16c>
			29a0: R_PPC_REL24	set_eff_tag__11TChCrEffTagFi
    29a4:	48 00 00 0c 	b       29b0 <__ct__16TObjCMAssignMenuFv+0x17c>
    29a8:	38 60 00 03 	li      r3,3
    29ac:	48 00 00 01 	bl      29ac <__ct__16TObjCMAssignMenuFv+0x178>
			29ac: R_PPC_REL24	set_eff_tag__11TChCrEffTagFi
    29b0:	7f e3 fb 78 	mr      r3,r31
    29b4:	bb c1 00 18 	lmw     r30,24(r1)
    29b8:	80 01 00 24 	lwz     r0,36(r1)
    29bc:	7c 08 03 a6 	mtlr    r0
    29c0:	38 21 00 20 	addi    r1,r1,32
    29c4:	4e 80 00 20 	blr

000029c8 <fn_802972BC>:
    29c8:	4e 80 00 20 	blr

000029cc <fn_802972C0>:
    29cc:	4e 80 00 20 	blr

000029d0 <TObjCMMainMenu__sub_802972C4>:
    29d0:	4e 80 00 20 	blr

000029d4 <try_pay_fee__14TObjCMMainMenuFv>:
    29d4:	94 21 ff f0 	stwu    r1,-16(r1)
    29d8:	7c 08 02 a6 	mflr    r0
    29dc:	3c 60 00 01 	lis     r3,1
    29e0:	90 01 00 14 	stw     r0,20(r1)
    29e4:	38 63 ff ff 	addi    r3,r3,-1
    29e8:	48 00 00 01 	bl      29e8 <try_pay_fee__14TObjCMMainMenuFv+0x14>
			29e8: R_PPC_REL24	get_char_index__23TAdSinglePlyChrSelectGCFUi
    29ec:	28 03 00 00 	cmplwi  r3,0
    29f0:	40 82 00 24 	bne     2a14 <try_pay_fee__14TObjCMMainMenuFv+0x40>
    29f4:	3c 60 40 02 	lis     r3,16386
    29f8:	38 80 00 00 	li      r4,0
    29fc:	38 63 85 19 	addi    r3,r3,-31463
    2a00:	38 a0 00 00 	li      r5,0
    2a04:	38 c0 00 00 	li      r6,0
    2a08:	48 00 00 01 	bl      2a08 <try_pay_fee__14TObjCMMainMenuFv+0x34>
			2a08: R_PPC_REL24	play_sound_effect
    2a0c:	38 60 00 00 	li      r3,0
    2a10:	48 00 00 68 	b       2a78 <try_pay_fee__14TObjCMMainMenuFv+0xa4>
    2a14:	3c 60 00 01 	lis     r3,1
    2a18:	38 63 ff ff 	addi    r3,r3,-1
    2a1c:	48 00 00 01 	bl      2a1c <try_pay_fee__14TObjCMMainMenuFv+0x48>
			2a1c: R_PPC_REL24	get_char_index__23TAdSinglePlyChrSelectGCFUi
    2a20:	80 83 03 6c 	lwz     r4,876(r3)
    2a24:	2c 04 27 10 	cmpwi   r4,10000
    2a28:	40 80 00 2c 	bge     2a54 <try_pay_fee__14TObjCMMainMenuFv+0x80>
    2a2c:	38 00 00 00 	li      r0,0
    2a30:	3c 80 00 01 	lis     r4,1
    2a34:	90 03 03 6c 	stw     r0,876(r3)
    2a38:	38 64 b2 0c 	addi    r3,r4,-19956
    2a3c:	38 80 00 00 	li      r4,0
    2a40:	38 a0 00 00 	li      r5,0
    2a44:	38 c0 00 00 	li      r6,0
    2a48:	48 00 00 01 	bl      2a48 <try_pay_fee__14TObjCMMainMenuFv+0x74>
			2a48: R_PPC_REL24	play_sound_effect
    2a4c:	38 60 00 00 	li      r3,0
    2a50:	48 00 00 28 	b       2a78 <try_pay_fee__14TObjCMMainMenuFv+0xa4>
    2a54:	38 04 d8 f0 	addi    r0,r4,-10000
    2a58:	3c 80 00 04 	lis     r4,4
    2a5c:	90 03 03 6c 	stw     r0,876(r3)
    2a60:	38 64 4e 03 	addi    r3,r4,19971
    2a64:	38 80 00 00 	li      r4,0
    2a68:	38 a0 00 00 	li      r5,0
    2a6c:	38 c0 00 00 	li      r6,0
    2a70:	48 00 00 01 	bl      2a70 <try_pay_fee__14TObjCMMainMenuFv+0x9c>
			2a70: R_PPC_REL24	play_sound_effect
    2a74:	38 60 00 01 	li      r3,1
    2a78:	80 01 00 14 	lwz     r0,20(r1)
    2a7c:	7c 08 03 a6 	mtlr    r0
    2a80:	38 21 00 10 	addi    r1,r1,16
    2a84:	4e 80 00 20 	blr

00002a88 <confirm_selection__14TObjCMMainMenuFPv>:
    2a88:	94 21 ff f0 	stwu    r1,-16(r1)
    2a8c:	7c 08 02 a6 	mflr    r0
    2a90:	90 01 00 14 	stw     r0,20(r1)
    2a94:	93 e1 00 0c 	stw     r31,12(r1)
    2a98:	7c 7f 1b 78 	mr      r31,r3
    2a9c:	80 63 00 1c 	lwz     r3,28(r3)
    2aa0:	48 00 00 01 	bl      2aa0 <confirm_selection__14TObjCMMainMenuFPv+0x18>
			2aa0: R_PPC_REL24	validate_character_name__14TObjCMMainMenuFPSc
    2aa4:	2c 03 00 00 	cmpwi   r3,0
    2aa8:	40 82 00 20 	bne     2ac8 <confirm_selection__14TObjCMMainMenuFPv+0x40>
    2aac:	3c 60 00 05 	lis     r3,5
    2ab0:	38 80 00 00 	li      r4,0
    2ab4:	38 63 3f 06 	addi    r3,r3,16134
    2ab8:	38 a0 00 00 	li      r5,0
    2abc:	38 c0 00 00 	li      r6,0
    2ac0:	48 00 00 01 	bl      2ac0 <confirm_selection__14TObjCMMainMenuFPv+0x38>
			2ac0: R_PPC_REL24	play_sound_effect
    2ac4:	48 00 00 60 	b       2b24 <confirm_selection__14TObjCMMainMenuFPv+0x9c>
    2ac8:	3c 60 00 05 	lis     r3,5
    2acc:	38 80 00 00 	li      r4,0
    2ad0:	38 63 2d 01 	addi    r3,r3,11521
    2ad4:	38 a0 00 00 	li      r5,0
    2ad8:	38 c0 00 00 	li      r6,0
    2adc:	48 00 00 01 	bl      2adc <confirm_selection__14TObjCMMainMenuFPv+0x54>
			2adc: R_PPC_REL24	play_sound_effect
    2ae0:	80 7f 00 1c 	lwz     r3,28(r31)
    2ae4:	88 03 00 30 	lbz     r0,48(r3)
    2ae8:	7c 00 07 74 	extsb   r0,r0
    2aec:	2c 00 ff ff 	cmpwi   r0,-1
    2af0:	40 82 00 14 	bne     2b04 <confirm_selection__14TObjCMMainMenuFPv+0x7c>
    2af4:	48 00 00 01 	bl      2af4 <confirm_selection__14TObjCMMainMenuFPv+0x6c>
			2af4: R_PPC_REL24	calc_section_id_from_name
    2af8:	80 9f 00 1c 	lwz     r4,28(r31)
    2afc:	98 64 00 30 	stb     r3,48(r4)
    2b00:	48 00 00 08 	b       2b08 <confirm_selection__14TObjCMMainMenuFPv+0x80>
    2b04:	48 00 00 01 	bl      2b04 <confirm_selection__14TObjCMMainMenuFPv+0x7c>
			2b04: R_PPC_REL24	try_pay_fee__14TObjCMMainMenuFv
    2b08:	38 60 00 01 	li      r3,1
    2b0c:	48 00 00 01 	bl      2b0c <confirm_selection__14TObjCMMainMenuFPv+0x84>
			2b0c: R_PPC_REL24	set_selection__14TObjCMMainMenuFi
    2b10:	48 00 00 01 	bl      2b10 <confirm_selection__14TObjCMMainMenuFPv+0x88>
			2b10: R_PPC_REL24	reset_character_creation_figure_rotation__Fv
    2b14:	38 60 00 3c 	li      r3,60
    2b18:	38 00 00 02 	li      r0,2
    2b1c:	90 7f 00 30 	stw     r3,48(r31)
    2b20:	90 00 00 00 	stw     r0,0(0)
			2b20: R_PPC_EMB_SDA21	TObjCMMainMenu__data_805D659C
    2b24:	80 01 00 14 	lwz     r0,20(r1)
    2b28:	83 e1 00 0c 	lwz     r31,12(r1)
    2b2c:	7c 08 03 a6 	mtlr    r0
    2b30:	38 21 00 10 	addi    r1,r1,16
    2b34:	4e 80 00 20 	blr

00002b38 <open_name_menu__14TObjCMMainMenuFPv>:
    2b38:	94 21 ff f0 	stwu    r1,-16(r1)
    2b3c:	7c 08 02 a6 	mflr    r0
    2b40:	3c 80 00 05 	lis     r4,5
    2b44:	38 a0 00 00 	li      r5,0
    2b48:	90 01 00 14 	stw     r0,20(r1)
    2b4c:	38 c0 00 00 	li      r6,0
    2b50:	93 e1 00 0c 	stw     r31,12(r1)
    2b54:	7c 7f 1b 78 	mr      r31,r3
    2b58:	38 64 2d 01 	addi    r3,r4,11521
    2b5c:	38 80 00 00 	li      r4,0
    2b60:	48 00 00 01 	bl      2b60 <open_name_menu__14TObjCMMainMenuFPv+0x28>
			2b60: R_PPC_REL24	play_sound_effect
    2b64:	38 00 00 01 	li      r0,1
    2b68:	90 00 00 00 	stw     r0,0(0)
			2b68: R_PPC_EMB_SDA21	TObjCMMainMenu__data_805D659C
    2b6c:	80 7f 00 50 	lwz     r3,80(r31)
    2b70:	48 00 00 01 	bl      2b70 <open_name_menu__14TObjCMMainMenuFPv+0x38>
			2b70: R_PPC_REL24	create__10TObjCMNameFPv
    2b74:	80 01 00 14 	lwz     r0,20(r1)
    2b78:	83 e1 00 0c 	lwz     r31,12(r1)
    2b7c:	7c 08 03 a6 	mtlr    r0
    2b80:	38 21 00 10 	addi    r1,r1,16
    2b84:	4e 80 00 20 	blr

00002b88 <open_proportion_menu__14TObjCMMainMenuFPv>:
    2b88:	94 21 ff f0 	stwu    r1,-16(r1)
    2b8c:	7c 08 02 a6 	mflr    r0
    2b90:	3c 80 00 05 	lis     r4,5
    2b94:	38 a0 00 00 	li      r5,0
    2b98:	90 01 00 14 	stw     r0,20(r1)
    2b9c:	38 c0 00 00 	li      r6,0
    2ba0:	93 e1 00 0c 	stw     r31,12(r1)
    2ba4:	7c 7f 1b 78 	mr      r31,r3
    2ba8:	38 64 2d 01 	addi    r3,r4,11521
    2bac:	38 80 00 00 	li      r4,0
    2bb0:	48 00 00 01 	bl      2bb0 <open_proportion_menu__14TObjCMMainMenuFPv+0x28>
			2bb0: R_PPC_REL24	play_sound_effect
    2bb4:	38 00 00 01 	li      r0,1
    2bb8:	90 00 00 00 	stw     r0,0(0)
			2bb8: R_PPC_EMB_SDA21	TObjCMMainMenu__data_805D659C
    2bbc:	80 7f 00 50 	lwz     r3,80(r31)
    2bc0:	48 00 00 01 	bl      2bc0 <open_proportion_menu__14TObjCMMainMenuFPv+0x38>
			2bc0: R_PPC_REL24	create__16TObjCMProportionFPv
    2bc4:	80 01 00 14 	lwz     r0,20(r1)
    2bc8:	83 e1 00 0c 	lwz     r31,12(r1)
    2bcc:	7c 08 03 a6 	mtlr    r0
    2bd0:	38 21 00 10 	addi    r1,r1,16
    2bd4:	4e 80 00 20 	blr

00002bd8 <open_auto_mk_menu__14TObjCMMainMenuFPv>:
    2bd8:	94 21 ff f0 	stwu    r1,-16(r1)
    2bdc:	7c 08 02 a6 	mflr    r0
    2be0:	3c 80 00 05 	lis     r4,5
    2be4:	38 a0 00 00 	li      r5,0
    2be8:	90 01 00 14 	stw     r0,20(r1)
    2bec:	38 c0 00 00 	li      r6,0
    2bf0:	93 e1 00 0c 	stw     r31,12(r1)
    2bf4:	7c 7f 1b 78 	mr      r31,r3
    2bf8:	38 64 2d 01 	addi    r3,r4,11521
    2bfc:	38 80 00 00 	li      r4,0
    2c00:	48 00 00 01 	bl      2c00 <open_auto_mk_menu__14TObjCMMainMenuFPv+0x28>
			2c00: R_PPC_REL24	play_sound_effect
    2c04:	38 00 00 01 	li      r0,1
    2c08:	90 00 00 00 	stw     r0,0(0)
			2c08: R_PPC_EMB_SDA21	TObjCMMainMenu__data_805D659C
    2c0c:	80 7f 00 50 	lwz     r3,80(r31)
    2c10:	48 00 00 01 	bl      2c10 <open_auto_mk_menu__14TObjCMMainMenuFPv+0x38>
			2c10: R_PPC_REL24	create__16TObjCMAutoMkDataFPv
    2c14:	80 01 00 14 	lwz     r0,20(r1)
    2c18:	83 e1 00 0c 	lwz     r31,12(r1)
    2c1c:	7c 08 03 a6 	mtlr    r0
    2c20:	38 21 00 10 	addi    r1,r1,16
    2c24:	4e 80 00 20 	blr

00002c28 <open_hair_menu__14TObjCMMainMenuFPv>:
    2c28:	94 21 ff f0 	stwu    r1,-16(r1)
    2c2c:	7c 08 02 a6 	mflr    r0
    2c30:	3c 80 00 05 	lis     r4,5
    2c34:	38 a0 00 00 	li      r5,0
    2c38:	90 01 00 14 	stw     r0,20(r1)
    2c3c:	38 c0 00 00 	li      r6,0
    2c40:	93 e1 00 0c 	stw     r31,12(r1)
    2c44:	7c 7f 1b 78 	mr      r31,r3
    2c48:	38 64 2d 01 	addi    r3,r4,11521
    2c4c:	38 80 00 00 	li      r4,0
    2c50:	48 00 00 01 	bl      2c50 <open_hair_menu__14TObjCMMainMenuFPv+0x28>
			2c50: R_PPC_REL24	play_sound_effect
    2c54:	38 00 00 01 	li      r0,1
    2c58:	90 00 00 00 	stw     r0,0(0)
			2c58: R_PPC_EMB_SDA21	TObjCMMainMenu__data_805D659C
    2c5c:	80 7f 00 50 	lwz     r3,80(r31)
    2c60:	48 00 00 01 	bl      2c60 <open_hair_menu__14TObjCMMainMenuFPv+0x38>
			2c60: R_PPC_REL24	create__14TObjCMHairMenuFv
    2c64:	80 01 00 14 	lwz     r0,20(r1)
    2c68:	83 e1 00 0c 	lwz     r31,12(r1)
    2c6c:	7c 08 03 a6 	mtlr    r0
    2c70:	38 21 00 10 	addi    r1,r1,16
    2c74:	4e 80 00 20 	blr

00002c78 <open_assign_menu__14TObjCMMainMenuFPv>:
    2c78:	94 21 ff f0 	stwu    r1,-16(r1)
    2c7c:	7c 08 02 a6 	mflr    r0
    2c80:	3c 80 00 05 	lis     r4,5
    2c84:	38 a0 00 00 	li      r5,0
    2c88:	90 01 00 14 	stw     r0,20(r1)
    2c8c:	38 c0 00 00 	li      r6,0
    2c90:	93 e1 00 0c 	stw     r31,12(r1)
    2c94:	7c 7f 1b 78 	mr      r31,r3
    2c98:	38 64 2d 01 	addi    r3,r4,11521
    2c9c:	38 80 00 00 	li      r4,0
    2ca0:	48 00 00 01 	bl      2ca0 <open_assign_menu__14TObjCMMainMenuFPv+0x28>
			2ca0: R_PPC_REL24	play_sound_effect
    2ca4:	38 00 00 01 	li      r0,1
    2ca8:	3c 60 00 00 	lis     r3,0
			2caa: R_PPC_ADDR16_HA	TObjCMMainMenu__data_804DB9C8
    2cac:	90 00 00 00 	stw     r0,0(0)
			2cac: R_PPC_EMB_SDA21	TObjCMMainMenu__data_805D659C
    2cb0:	38 83 00 00 	addi    r4,r3,0
			2cb2: R_PPC_ADDR16_LO	TObjCMMainMenu__data_804DB9C8
    2cb4:	80 1f 00 2c 	lwz     r0,44(r31)
    2cb8:	80 bf 00 24 	lwz     r5,36(r31)
    2cbc:	54 00 10 3a 	slwi    r0,r0,2
    2cc0:	80 7f 00 50 	lwz     r3,80(r31)
    2cc4:	7c 05 00 2e 	lwzx    r0,r5,r0
    2cc8:	54 00 20 36 	slwi    r0,r0,4
    2ccc:	7c 84 00 2e 	lwzx    r4,r4,r0
    2cd0:	48 00 00 01 	bl      2cd0 <open_assign_menu__14TObjCMMainMenuFPv+0x58>
			2cd0: R_PPC_REL24	create__16TObjCMAssignMenuFPvPv
    2cd4:	80 01 00 14 	lwz     r0,20(r1)
    2cd8:	83 e1 00 0c 	lwz     r31,12(r1)
    2cdc:	7c 08 03 a6 	mtlr    r0
    2ce0:	38 21 00 10 	addi    r1,r1,16
    2ce4:	4e 80 00 20 	blr

00002ce8 <draw_root_menu__14TObjCMMainMenuFv>:
    2ce8:	94 21 ff 30 	stwu    r1,-208(r1)
    2cec:	7c 08 02 a6 	mflr    r0
    2cf0:	90 01 00 d4 	stw     r0,212(r1)
    2cf4:	db e1 00 c0 	stfd    f31,192(r1)
    2cf8:	f3 e1 00 c8 	xsmsubmsp vs31,vs1,vs0
    2cfc:	db c1 00 b0 	stfd    f30,176(r1)
    2d00:	f3 c1 00 b8 	xxsel   vs30,vs1,vs0,vs34
    2d04:	db a1 00 a0 	stfd    f29,160(r1)
    2d08:	f3 a1 00 a8 	psq_st  f29,168(r1),0,0
    2d0c:	db 81 00 90 	stfd    f28,144(r1)
    2d10:	f3 81 00 98 	xscmpgedp vs28,vs1,vs0
    2d14:	db 61 00 80 	stfd    f27,128(r1)
    2d18:	f3 61 00 88 	xsmsubasp vs27,vs1,vs0
    2d1c:	db 41 00 70 	stfd    f26,112(r1)
    2d20:	f3 41 00 78 	xxsel   vs26,vs1,vs0,vs33
    2d24:	db 21 00 60 	stfd    f25,96(r1)
    2d28:	f3 21 00 68 	psq_st  f25,104(r1),0,0
    2d2c:	db 01 00 50 	stfd    f24,80(r1)
    2d30:	f3 01 00 58 	xscmpgtdp vs24,vs1,vs0
    2d34:	bf 41 00 38 	stmw    r26,56(r1)
    2d38:	7c 7f 1b 78 	mr      r31,r3
    2d3c:	c3 a3 00 38 	lfs     f29,56(r3)
    2d40:	c0 03 00 3c 	lfs     f0,60(r3)
    2d44:	fc 1d 00 40 	fcmpo   cr0,f29,f0
    2d48:	40 80 00 08 	bge     2d50 <draw_root_menu__14TObjCMMainMenuFv+0x68>
    2d4c:	48 00 00 08 	b       2d54 <draw_root_menu__14TObjCMMainMenuFv+0x6c>
    2d50:	ff a0 00 90 	fmr     f29,f0
    2d54:	c0 20 00 00 	lfs     f1,0(0)
			2d54: R_PPC_EMB_SDA21	@85
    2d58:	fc 1d 08 40 	fcmpo   cr0,f29,f1
    2d5c:	4c 40 13 82 	cror    eq,lt,eq
    2d60:	41 82 01 50 	beq     2eb0 <draw_root_menu__14TObjCMMainMenuFv+0x1c8>
    2d64:	c0 00 00 00 	lfs     f0,0(0)
			2d64: R_PPC_EMB_SDA21	@86
    2d68:	fc 1d 00 40 	fcmpo   cr0,f29,f0
    2d6c:	4c 41 13 82 	cror    eq,gt,eq
    2d70:	40 82 00 0c 	bne     2d7c <draw_root_menu__14TObjCMMainMenuFv+0x94>
    2d74:	c3 80 00 00 	lfs     f28,0(0)
			2d74: R_PPC_EMB_SDA21	@56
    2d78:	48 00 00 0c 	b       2d84 <draw_root_menu__14TObjCMMainMenuFv+0x9c>
    2d7c:	ec 1d 08 28 	fsubs   f0,f29,f1
    2d80:	ef 80 08 24 	fdivs   f28,f0,f1
    2d84:	c3 c0 00 00 	lfs     f30,0(0)
			2d84: R_PPC_EMB_SDA21	@56
    2d88:	3c 60 00 00 	lis     r3,0
			2d8a: R_PPC_ADDR16_HA	@268
    2d8c:	c0 00 00 00 	lfs     f0,0(0)
			2d8c: R_PPC_EMB_SDA21	@874
    2d90:	3c 80 00 00 	lis     r4,0
			2d92: R_PPC_ADDR16_HA	char_creation_root_menu_tab_table
    2d94:	d3 c1 00 1c 	stfs    f30,28(r1)
    2d98:	3b 84 00 00 	addi    r28,r4,0
			2d9a: R_PPC_ADDR16_LO	char_creation_root_menu_tab_table
    2d9c:	cb e3 00 00 	lfd     f31,0(r3)
			2d9e: R_PPC_ADDR16_LO	@268
    2da0:	3b 60 00 00 	li      r27,0
    2da4:	d0 01 00 24 	stfs    f0,36(r1)
    2da8:	3b c0 00 00 	li      r30,0
    2dac:	c3 20 00 00 	lfs     f25,0(0)
			2dac: R_PPC_EMB_SDA21	@88
    2db0:	3f a0 43 30 	lis     r29,17200
    2db4:	c3 40 00 00 	lfs     f26,0(0)
			2db4: R_PPC_EMB_SDA21	@91
    2db8:	c3 60 00 00 	lfs     f27,0(0)
			2db8: R_PPC_EMB_SDA21	@409
    2dbc:	48 00 00 e8 	b       2ea4 <draw_root_menu__14TObjCMMainMenuFv+0x1bc>
    2dc0:	80 7f 00 24 	lwz     r3,36(r31)
    2dc4:	3b 40 00 00 	li      r26,0
    2dc8:	7c 63 f0 2e 	lwzx    r3,r3,r30
    2dcc:	38 63 00 8f 	addi    r3,r3,143
    2dd0:	48 00 00 01 	bl      2dd0 <draw_root_menu__14TObjCMMainMenuFv+0xe8>
			2dd0: R_PPC_REL24	get_creation_sprite_id__14TObjCMMainMenuFl
    2dd4:	38 00 00 0f 	li      r0,15
    2dd8:	38 83 00 90 	addi    r4,r3,144
    2ddc:	38 60 00 00 	li      r3,0
    2de0:	7c 09 03 a6 	mtctr   r0
    2de4:	7c 1c 18 2e 	lwzx    r0,r28,r3
    2de8:	7c 04 00 00 	cmpw    r4,r0
    2dec:	41 80 00 0c 	blt     2df8 <draw_root_menu__14TObjCMMainMenuFv+0x110>
    2df0:	38 63 00 04 	addi    r3,r3,4
    2df4:	42 00 ff f0 	bdnz    2de4 <draw_root_menu__14TObjCMMainMenuFv+0xfc>
    2df8:	6c 00 80 00 	xoris   r0,r0,32768
    2dfc:	93 a1 00 28 	stw     r29,40(r1)
    2e00:	90 01 00 2c 	stw     r0,44(r1)
    2e04:	c8 01 00 28 	lfd     f0,40(r1)
    2e08:	d3 21 00 20 	stfs    f25,32(r1)
    2e0c:	ec 00 f8 28 	fsubs   f0,f0,f31
    2e10:	ec 00 c8 28 	fsubs   f0,f0,f25
    2e14:	ef 1c c8 3a 	fmadds  f24,f28,f0,f25
    2e18:	48 00 00 01 	bl      2e18 <draw_root_menu__14TObjCMMainMenuFv+0x130>
			2e18: R_PPC_REL24	is_active__23TAdSinglePlyChrSelectGCFv
    2e1c:	2c 03 00 00 	cmpwi   r3,0
    2e20:	41 82 00 30 	beq     2e50 <draw_root_menu__14TObjCMMainMenuFv+0x168>
    2e24:	80 1f 00 2c 	lwz     r0,44(r31)
    2e28:	7c 1b 00 00 	cmpw    r27,r0
    2e2c:	40 82 00 24 	bne     2e50 <draw_root_menu__14TObjCMMainMenuFv+0x168>
    2e30:	80 1f 00 34 	lwz     r0,52(r31)
    2e34:	3b 40 00 02 	li      r26,2
    2e38:	54 03 50 2a 	slwi    r3,r0,10
    2e3c:	48 00 00 01 	bl      2e3c <draw_root_menu__14TObjCMMainMenuFv+0x154>
			2e3c: R_PPC_REL24	sin_table_lookup
    2e40:	c0 40 00 00 	lfs     f2,0(0)
			2e40: R_PPC_EMB_SDA21	@90
    2e44:	c0 01 00 20 	lfs     f0,32(r1)
    2e48:	ec 02 00 7a 	fmadds  f0,f2,f1,f0
    2e4c:	d0 01 00 20 	stfs    f0,32(r1)
    2e50:	c0 01 00 20 	lfs     f0,32(r1)
    2e54:	38 7a 00 06 	addi    r3,r26,6
    2e58:	c0 20 00 00 	lfs     f1,0(0)
			2e58: R_PPC_EMB_SDA21	@875
    2e5c:	38 81 00 20 	addi    r4,r1,32
    2e60:	ec 18 00 28 	fsubs   f0,f24,f0
    2e64:	38 a1 00 18 	addi    r5,r1,24
    2e68:	ec 00 d0 24 	fdivs   f0,f0,f26
    2e6c:	d0 01 00 18 	stfs    f0,24(r1)
    2e70:	48 00 00 01 	bl      2e70 <draw_root_menu__14TObjCMMainMenuFv+0x188>
			2e70: R_PPC_REL24	draw_ui_sprite_opaque
    2e74:	d3 01 00 20 	stfs    f24,32(r1)
    2e78:	38 7a 00 07 	addi    r3,r26,7
    2e7c:	c0 20 00 00 	lfs     f1,0(0)
			2e7c: R_PPC_EMB_SDA21	@875
    2e80:	38 81 00 20 	addi    r4,r1,32
    2e84:	d3 c1 00 18 	stfs    f30,24(r1)
    2e88:	38 a1 00 18 	addi    r5,r1,24
    2e8c:	48 00 00 01 	bl      2e8c <draw_root_menu__14TObjCMMainMenuFv+0x1a4>
			2e8c: R_PPC_REL24	draw_ui_sprite_opaque
    2e90:	c0 01 00 24 	lfs     f0,36(r1)
    2e94:	3b 7b 00 01 	addi    r27,r27,1
    2e98:	3b de 00 04 	addi    r30,r30,4
    2e9c:	ec 00 d8 2a 	fadds   f0,f0,f27
    2ea0:	d0 01 00 24 	stfs    f0,36(r1)
    2ea4:	80 1f 00 28 	lwz     r0,40(r31)
    2ea8:	7c 1b 00 00 	cmpw    r27,r0
    2eac:	41 80 ff 14 	blt     2dc0 <draw_root_menu__14TObjCMMainMenuFv+0xd8>
    2eb0:	c0 00 00 00 	lfs     f0,0(0)
			2eb0: R_PPC_EMB_SDA21	@54
    2eb4:	fc 1d 00 40 	fcmpo   cr0,f29,f0
    2eb8:	4c 40 13 82 	cror    eq,lt,eq
    2ebc:	41 82 00 8c 	beq     2f48 <draw_root_menu__14TObjCMMainMenuFv+0x260>
    2ec0:	c0 00 00 00 	lfs     f0,0(0)
			2ec0: R_PPC_EMB_SDA21	@85
    2ec4:	fc 1d 00 40 	fcmpo   cr0,f29,f0
    2ec8:	4c 41 13 82 	cror    eq,gt,eq
    2ecc:	40 82 00 0c 	bne     2ed8 <draw_root_menu__14TObjCMMainMenuFv+0x1f0>
    2ed0:	c3 00 00 00 	lfs     f24,0(0)
			2ed0: R_PPC_EMB_SDA21	@56
    2ed4:	48 00 00 08 	b       2edc <draw_root_menu__14TObjCMMainMenuFv+0x1f4>
    2ed8:	ef 1d 00 24 	fdivs   f24,f29,f0
    2edc:	c0 20 00 00 	lfs     f1,0(0)
			2edc: R_PPC_EMB_SDA21	@876
    2ee0:	3b 40 00 00 	li      r26,0
    2ee4:	c0 00 00 00 	lfs     f0,0(0)
			2ee4: R_PPC_EMB_SDA21	@874
    2ee8:	d0 21 00 10 	stfs    f1,16(r1)
    2eec:	c3 80 00 00 	lfs     f28,0(0)
			2eec: R_PPC_EMB_SDA21	@409
    2ef0:	d0 01 00 14 	stfs    f0,20(r1)
    2ef4:	48 00 00 48 	b       2f3c <draw_root_menu__14TObjCMMainMenuFv+0x254>
    2ef8:	3b 60 00 00 	li      r27,0
    2efc:	48 00 00 01 	bl      2efc <draw_root_menu__14TObjCMMainMenuFv+0x214>
			2efc: R_PPC_REL24	is_active__23TAdSinglePlyChrSelectGCFv
    2f00:	2c 03 00 00 	cmpwi   r3,0
    2f04:	41 82 00 14 	beq     2f18 <draw_root_menu__14TObjCMMainMenuFv+0x230>
    2f08:	80 1f 00 2c 	lwz     r0,44(r31)
    2f0c:	7c 1a 00 00 	cmpw    r26,r0
    2f10:	40 82 00 08 	bne     2f18 <draw_root_menu__14TObjCMMainMenuFv+0x230>
    2f14:	3b 60 ff ff 	li      r27,-1
    2f18:	fc 40 c0 90 	fmr     f2,f24
    2f1c:	c0 20 00 00 	lfs     f1,0(0)
			2f1c: R_PPC_EMB_SDA21	@877
    2f20:	38 7b 00 01 	addi    r3,r27,1
    2f24:	38 81 00 10 	addi    r4,r1,16
    2f28:	48 00 00 01 	bl      2f28 <draw_root_menu__14TObjCMMainMenuFv+0x240>
			2f28: R_PPC_REL24	draw_ui_sprite
    2f2c:	c0 01 00 14 	lfs     f0,20(r1)
    2f30:	3b 5a 00 01 	addi    r26,r26,1
    2f34:	ec 00 e0 2a 	fadds   f0,f0,f28
    2f38:	d0 01 00 14 	stfs    f0,20(r1)
    2f3c:	80 1f 00 28 	lwz     r0,40(r31)
    2f40:	7c 1a 00 00 	cmpw    r26,r0
    2f44:	41 80 ff b4 	blt     2ef8 <draw_root_menu__14TObjCMMainMenuFv+0x210>
    2f48:	c0 00 00 00 	lfs     f0,0(0)
			2f48: R_PPC_EMB_SDA21	@86
    2f4c:	fc 1d 00 40 	fcmpo   cr0,f29,f0
    2f50:	4c 40 13 82 	cror    eq,lt,eq
    2f54:	41 82 01 20 	beq     3074 <draw_root_menu__14TObjCMMainMenuFv+0x38c>
    2f58:	ec 7d 00 28 	fsubs   f3,f29,f0
    2f5c:	c0 00 00 00 	lfs     f0,0(0)
			2f5c: R_PPC_EMB_SDA21	@411
    2f60:	c0 40 00 00 	lfs     f2,0(0)
			2f60: R_PPC_EMB_SDA21	@878
    2f64:	3b 40 00 00 	li      r26,0
    2f68:	c0 20 00 00 	lfs     f1,0(0)
			2f68: R_PPC_EMB_SDA21	@879
    2f6c:	3b c0 00 00 	li      r30,0
    2f70:	ec 63 00 24 	fdivs   f3,f3,f0
    2f74:	c0 00 00 00 	lfs     f0,0(0)
			2f74: R_PPC_EMB_SDA21	@413
    2f78:	d0 41 00 08 	stfs    f2,8(r1)
    2f7c:	c3 80 00 00 	lfs     f28,0(0)
			2f7c: R_PPC_EMB_SDA21	@409
    2f80:	d0 21 00 0c 	stfs    f1,12(r1)
    2f84:	ef 03 00 f2 	fmuls   f24,f3,f3
    2f88:	ef 20 06 32 	fmuls   f25,f0,f24
    2f8c:	48 00 00 dc 	b       3068 <draw_root_menu__14TObjCMMainMenuFv+0x380>
    2f90:	80 7f 00 24 	lwz     r3,36(r31)
    2f94:	3b a0 00 00 	li      r29,0
    2f98:	7c 03 f0 2e 	lwzx    r0,r3,r30
    2f9c:	2c 00 00 09 	cmpwi   r0,9
    2fa0:	40 82 00 18 	bne     2fb8 <draw_root_menu__14TObjCMMainMenuFv+0x2d0>
    2fa4:	80 7f 00 1c 	lwz     r3,28(r31)
    2fa8:	48 00 00 01 	bl      2fa8 <draw_root_menu__14TObjCMMainMenuFv+0x2c0>
			2fa8: R_PPC_REL24	validate_character_name__14TObjCMMainMenuFPSc
    2fac:	2c 03 00 00 	cmpwi   r3,0
    2fb0:	40 82 00 08 	bne     2fb8 <draw_root_menu__14TObjCMMainMenuFv+0x2d0>
    2fb4:	3b a0 00 01 	li      r29,1
    2fb8:	57 bb 06 3e 	clrlwi  r27,r29,24
    2fbc:	48 00 00 01 	bl      2fbc <draw_root_menu__14TObjCMMainMenuFv+0x2d4>
			2fbc: R_PPC_REL24	is_active__23TAdSinglePlyChrSelectGCFv
    2fc0:	2c 03 00 00 	cmpwi   r3,0
    2fc4:	41 82 00 64 	beq     3028 <draw_root_menu__14TObjCMMainMenuFv+0x340>
    2fc8:	80 1f 00 2c 	lwz     r0,44(r31)
    2fcc:	7c 1a 00 00 	cmpw    r26,r0
    2fd0:	40 82 00 58 	bne     3028 <draw_root_menu__14TObjCMMainMenuFv+0x340>
    2fd4:	80 1f 00 34 	lwz     r0,52(r31)
    2fd8:	54 03 50 2a 	slwi    r3,r0,10
    2fdc:	48 00 00 01 	bl      2fdc <draw_root_menu__14TObjCMMainMenuFv+0x2f4>
			2fdc: R_PPC_REL24	sin_table_lookup
    2fe0:	c0 40 00 00 	lfs     f2,0(0)
			2fe0: R_PPC_EMB_SDA21	@407
    2fe4:	c0 00 00 00 	lfs     f0,0(0)
			2fe4: R_PPC_EMB_SDA21	@56
    2fe8:	ec 22 00 7a 	fmadds  f1,f2,f1,f0
    2fec:	fc 01 00 40 	fcmpo   cr0,f1,f0
    2ff0:	40 81 00 08 	ble     2ff8 <draw_root_menu__14TObjCMMainMenuFv+0x310>
    2ff4:	fc 20 00 90 	fmr     f1,f0
    2ff8:	2c 1b 00 00 	cmpwi   r27,0
    2ffc:	ec 41 06 32 	fmuls   f2,f1,f24
    3000:	41 82 00 0c 	beq     300c <draw_root_menu__14TObjCMMainMenuFv+0x324>
    3004:	c0 00 00 00 	lfs     f0,0(0)
			3004: R_PPC_EMB_SDA21	lbl_805DDB50
    3008:	ec 42 00 32 	fmuls   f2,f2,f0
    300c:	80 7f 00 24 	lwz     r3,36(r31)
    3010:	38 81 00 08 	addi    r4,r1,8
    3014:	c0 20 00 00 	lfs     f1,0(0)
			3014: R_PPC_EMB_SDA21	@877
    3018:	7c 63 f0 2e 	lwzx    r3,r3,r30
    301c:	38 63 00 8f 	addi    r3,r3,143
    3020:	48 00 00 01 	bl      3020 <draw_root_menu__14TObjCMMainMenuFv+0x338>
			3020: R_PPC_REL24	draw_ui_sprite
    3024:	48 00 00 30 	b       3054 <draw_root_menu__14TObjCMMainMenuFv+0x36c>
    3028:	fc 40 c8 90 	fmr     f2,f25
    302c:	2c 1b 00 00 	cmpwi   r27,0
    3030:	41 82 00 0c 	beq     303c <draw_root_menu__14TObjCMMainMenuFv+0x354>
    3034:	c0 00 00 00 	lfs     f0,0(0)
			3034: R_PPC_EMB_SDA21	lbl_805DDB50
    3038:	ec 59 00 32 	fmuls   f2,f25,f0
    303c:	80 7f 00 24 	lwz     r3,36(r31)
    3040:	38 81 00 08 	addi    r4,r1,8
    3044:	c0 20 00 00 	lfs     f1,0(0)
			3044: R_PPC_EMB_SDA21	@877
    3048:	7c 63 f0 2e 	lwzx    r3,r3,r30
    304c:	38 63 00 8f 	addi    r3,r3,143
    3050:	48 00 00 01 	bl      3050 <draw_root_menu__14TObjCMMainMenuFv+0x368>
			3050: R_PPC_REL24	draw_ui_sprite
    3054:	c0 01 00 0c 	lfs     f0,12(r1)
    3058:	3b 5a 00 01 	addi    r26,r26,1
    305c:	3b de 00 04 	addi    r30,r30,4
    3060:	ec 00 e0 2a 	fadds   f0,f0,f28
    3064:	d0 01 00 0c 	stfs    f0,12(r1)
    3068:	80 1f 00 28 	lwz     r0,40(r31)
    306c:	7c 1a 00 00 	cmpw    r26,r0
    3070:	41 80 ff 20 	blt     2f90 <draw_root_menu__14TObjCMMainMenuFv+0x2a8>
    3074:	e3 e1 00 c8 	psq_l   f31,200(r1),0,0
    3078:	cb e1 00 c0 	lfd     f31,192(r1)
    307c:	e3 c1 00 b8 	lq      r30,176(r1)
    3080:	cb c1 00 b0 	lfd     f30,176(r1)
    3084:	e3 a1 00 a8 	psq_l   f29,168(r1),0,0
    3088:	cb a1 00 a0 	lfd     f29,160(r1)
    308c:	e3 81 00 98 	lq      r28,144(r1)
    3090:	cb 81 00 90 	lfd     f28,144(r1)
    3094:	e3 61 00 88 	psq_l   f27,136(r1),0,0
    3098:	cb 61 00 80 	lfd     f27,128(r1)
    309c:	e3 41 00 78 	lq      r26,112(r1)
    30a0:	cb 41 00 70 	lfd     f26,112(r1)
    30a4:	e3 21 00 68 	psq_l   f25,104(r1),0,0
    30a8:	cb 21 00 60 	lfd     f25,96(r1)
    30ac:	e3 01 00 58 	lq      r24,80(r1)
    30b0:	cb 01 00 50 	lfd     f24,80(r1)
    30b4:	bb 41 00 38 	lmw     r26,56(r1)
    30b8:	80 01 00 d4 	lwz     r0,212(r1)
    30bc:	7c 08 03 a6 	mtlr    r0
    30c0:	38 21 00 d0 	addi    r1,r1,208
    30c4:	4e 80 00 20 	blr

000030c8 <sub_80297B18__14TObjCMMainMenuFv>:
    30c8:	94 21 ff 70 	stwu    r1,-144(r1)
    30cc:	7c 08 02 a6 	mflr    r0
    30d0:	90 01 00 94 	stw     r0,148(r1)
    30d4:	db e1 00 80 	stfd    f31,128(r1)
    30d8:	f3 e1 00 88 	xsmsubasp vs31,vs1,vs0
    30dc:	db c1 00 70 	stfd    f30,112(r1)
    30e0:	f3 c1 00 78 	xxsel   vs30,vs1,vs0,vs33
    30e4:	db a1 00 60 	stfd    f29,96(r1)
    30e8:	f3 a1 00 68 	psq_st  f29,104(r1),0,0
    30ec:	db 81 00 50 	stfd    f28,80(r1)
    30f0:	f3 81 00 58 	xscmpgtdp vs28,vs1,vs0
    30f4:	db 61 00 40 	stfd    f27,64(r1)
    30f8:	f3 61 00 48 	xsmaddmsp vs27,vs1,vs0
    30fc:	bf 61 00 2c 	stmw    r27,44(r1)
    3100:	7c 7f 1b 78 	mr      r31,r3
    3104:	80 03 00 2c 	lwz     r0,44(r3)
    3108:	80 63 00 24 	lwz     r3,36(r3)
    310c:	54 00 10 3a 	slwi    r0,r0,2
    3110:	7c 03 00 2e 	lwzx    r0,r3,r0
    3114:	2c 00 00 09 	cmpwi   r0,9
    3118:	40 82 00 c0 	bne     31d8 <sub_80297B18__14TObjCMMainMenuFv+0x110>
    311c:	80 7f 00 1c 	lwz     r3,28(r31)
    3120:	48 00 00 01 	bl      3120 <sub_80297B18__14TObjCMMainMenuFv+0x58>
			3120: R_PPC_REL24	validate_character_name__14TObjCMMainMenuFPSc
    3124:	2c 03 00 00 	cmpwi   r3,0
    3128:	40 82 00 b0 	bne     31d8 <sub_80297B18__14TObjCMMainMenuFv+0x110>
    312c:	80 1f 00 34 	lwz     r0,52(r31)
    3130:	54 03 50 2a 	slwi    r3,r0,10
    3134:	48 00 00 01 	bl      3134 <sub_80297B18__14TObjCMMainMenuFv+0x6c>
			3134: R_PPC_REL24	sin_table_lookup
    3138:	48 00 00 01 	bl      3138 <sub_80297B18__14TObjCMMainMenuFv+0x70>
			3138: R_PPC_REL24	fabs_float
    313c:	c0 60 00 00 	lfs     f3,0(0)
			313c: R_PPC_EMB_SDA21	lbl_805DDBA8
    3140:	c0 40 00 00 	lfs     f2,0(0)
			3140: R_PPC_EMB_SDA21	lbl_805DDA70
    3144:	c0 00 00 00 	lfs     f0,0(0)
			3144: R_PPC_EMB_SDA21	TObjCMMainMenu__data_805DDB44
    3148:	ec 23 10 7c 	fnmsubs f1,f3,f1,f2
    314c:	ec 20 00 72 	fmuls   f1,f0,f1
    3150:	48 00 00 01 	bl      3150 <sub_80297B18__14TObjCMMainMenuFv+0x88>
			3150: R_PPC_REL24	__cvt_fp2unsigned
    3154:	54 60 c0 0e 	slwi    r0,r3,24
    3158:	64 1d 00 ff 	oris    r29,r0,255
    315c:	63 bd ff ff 	ori     r29,r29,65535
    3160:	48 00 00 01 	bl      3160 <sub_80297B18__14TObjCMMainMenuFv+0x98>
			3160: R_PPC_REL24	get_scale__14TObjCMMainMenuFv
    3164:	c0 40 00 00 	lfs     f2,0(0)
			3164: R_PPC_EMB_SDA21	lbl_805DDBAC
    3168:	3c 60 00 00 	lis     r3,0
			316a: R_PPC_ADDR16_HA	@917
    316c:	c0 00 00 00 	lfs     f0,0(0)
			316c: R_PPC_EMB_SDA21	lbl_805DDBA4
    3170:	3b 80 00 00 	li      r28,0
    3174:	ef a2 00 72 	fmuls   f29,f2,f1
    3178:	cb c3 00 00 	lfd     f30,0(r3)
			317a: R_PPC_ADDR16_LO	@917
    317c:	c3 e0 00 00 	lfs     f31,0(0)
			317c: R_PPC_EMB_SDA21	lbl_805DDBA0
    3180:	3f c0 43 30 	lis     r30,17200
    3184:	ef 80 e8 78 	fmsubs  f28,f0,f1,f29
    3188:	38 7c 00 3b 	addi    r3,r28,59
    318c:	48 00 00 01 	bl      318c <sub_80297B18__14TObjCMMainMenuFv+0xc4>
			318c: R_PPC_REL24	TQuestVmDownLoadServer__sub_8006EF6C
    3190:	7c 7b 1b 78 	mr      r27,r3
    3194:	48 00 00 01 	bl      3194 <sub_80297B18__14TObjCMMainMenuFv+0xcc>
			3194: R_PPC_REL24	calc_text_width
    3198:	90 61 00 24 	stw     r3,36(r1)
    319c:	93 c1 00 20 	stw     r30,32(r1)
    31a0:	c8 01 00 20 	lfd     f0,32(r1)
    31a4:	ec 00 f0 28 	fsubs   f0,f0,f30
    31a8:	ef 7f 00 28 	fsubs   f27,f31,f0
    31ac:	48 00 00 01 	bl      31ac <sub_80297B18__14TObjCMMainMenuFv+0xe4>
			31ac: R_PPC_REL24	restore_full_screen_view__11TCameraCtrlFv
    31b0:	fc 20 d8 90 	fmr     f1,f27
    31b4:	7f 63 db 78 	mr      r3,r27
    31b8:	fc 40 e0 90 	fmr     f2,f28
    31bc:	7f a4 eb 78 	mr      r4,r29
    31c0:	48 00 00 01 	bl      31c0 <sub_80297B18__14TObjCMMainMenuFv+0xf8>
			31c0: R_PPC_REL24	draw_menu_text__FffPCcUl
    31c4:	48 00 00 01 	bl      31c4 <sub_80297B18__14TObjCMMainMenuFv+0xfc>
			31c4: R_PPC_REL24	TCameraCtrl__sub_80068EF0
    31c8:	3b 9c 00 01 	addi    r28,r28,1
    31cc:	ef 9c e8 2a 	fadds   f28,f28,f29
    31d0:	2c 1c 00 02 	cmpwi   r28,2
    31d4:	41 80 ff b4 	blt     3188 <sub_80297B18__14TObjCMMainMenuFv+0xc0>
    31d8:	80 00 00 00 	lwz     r0,0(0)
			31d8: R_PPC_EMB_SDA21	TObjCMMainMenu__data_805D659C
    31dc:	2c 00 00 01 	cmpwi   r0,1
    31e0:	41 82 00 c8 	beq     32a8 <sub_80297B18__14TObjCMMainMenuFv+0x1e0>
    31e4:	40 80 00 10 	bge     31f4 <sub_80297B18__14TObjCMMainMenuFv+0x12c>
    31e8:	2c 00 00 00 	cmpwi   r0,0
    31ec:	40 80 00 14 	bge     3200 <sub_80297B18__14TObjCMMainMenuFv+0x138>
    31f0:	48 00 01 38 	b       3328 <sub_80297B18__14TObjCMMainMenuFv+0x260>
    31f4:	2c 00 00 03 	cmpwi   r0,3
    31f8:	40 80 01 30 	bge     3328 <sub_80297B18__14TObjCMMainMenuFv+0x260>
    31fc:	48 00 00 f4 	b       32f0 <sub_80297B18__14TObjCMMainMenuFv+0x228>
    3200:	48 00 00 01 	bl      3200 <sub_80297B18__14TObjCMMainMenuFv+0x138>
			3200: R_PPC_REL24	is_active__23TAdSinglePlyChrSelectGCFv
    3204:	2c 03 00 00 	cmpwi   r3,0
    3208:	41 82 00 98 	beq     32a0 <sub_80297B18__14TObjCMMainMenuFv+0x1d8>
    320c:	80 1f 00 2c 	lwz     r0,44(r31)
    3210:	80 7f 00 24 	lwz     r3,36(r31)
    3214:	54 00 10 3a 	slwi    r0,r0,2
    3218:	7c 03 00 2e 	lwzx    r0,r3,r0
    321c:	2c 00 00 09 	cmpwi   r0,9
    3220:	40 82 00 2c 	bne     324c <sub_80297B18__14TObjCMMainMenuFv+0x184>
    3224:	80 7f 00 1c 	lwz     r3,28(r31)
    3228:	48 00 00 01 	bl      3228 <sub_80297B18__14TObjCMMainMenuFv+0x160>
			3228: R_PPC_REL24	validate_character_name__14TObjCMMainMenuFPSc
    322c:	2c 03 00 00 	cmpwi   r3,0
    3230:	40 82 00 1c 	bne     324c <sub_80297B18__14TObjCMMainMenuFv+0x184>
    3234:	80 00 00 00 	lwz     r0,0(0)
			3234: R_PPC_EMB_SDA21	lbl_805DDA5C
    3238:	38 81 00 14 	addi    r4,r1,20
    323c:	38 60 00 01 	li      r3,1
    3240:	90 01 00 14 	stw     r0,20(r1)
    3244:	48 00 00 01 	bl      3244 <sub_80297B18__14TObjCMMainMenuFv+0x17c>
			3244: R_PPC_REL24	TObjCMIcon__sub_802994C8
    3248:	48 00 00 e4 	b       332c <sub_80297B18__14TObjCMMainMenuFv+0x264>
    324c:	80 7f 00 1c 	lwz     r3,28(r31)
    3250:	88 03 00 30 	lbz     r0,48(r3)
    3254:	7c 00 07 74 	extsb   r0,r0
    3258:	2c 00 ff ff 	cmpwi   r0,-1
    325c:	40 82 00 2c 	bne     3288 <sub_80297B18__14TObjCMMainMenuFv+0x1c0>
    3260:	3c 60 00 00 	lis     r3,0
			3262: R_PPC_ADDR16_HA	lbl_80464FC8
    3264:	38 81 00 18 	addi    r4,r1,24
    3268:	38 c3 00 00 	addi    r6,r3,0
			326a: R_PPC_ADDR16_LO	lbl_80464FC8
    326c:	38 60 00 02 	li      r3,2
    3270:	80 a6 00 00 	lwz     r5,0(r6)
    3274:	80 06 00 04 	lwz     r0,4(r6)
    3278:	90 a1 00 18 	stw     r5,24(r1)
    327c:	90 01 00 1c 	stw     r0,28(r1)
    3280:	48 00 00 01 	bl      3280 <sub_80297B18__14TObjCMMainMenuFv+0x1b8>
			3280: R_PPC_REL24	TObjCMIcon__sub_802994C8
    3284:	48 00 00 a8 	b       332c <sub_80297B18__14TObjCMMainMenuFv+0x264>
    3288:	80 00 00 00 	lwz     r0,0(0)
			3288: R_PPC_EMB_SDA21	lbl_805DDA60
    328c:	38 81 00 10 	addi    r4,r1,16
    3290:	38 60 00 01 	li      r3,1
    3294:	90 01 00 10 	stw     r0,16(r1)
    3298:	48 00 00 01 	bl      3298 <sub_80297B18__14TObjCMMainMenuFv+0x1d0>
			3298: R_PPC_REL24	TObjCMIcon__sub_802994C8
    329c:	48 00 00 90 	b       332c <sub_80297B18__14TObjCMMainMenuFv+0x264>
    32a0:	48 00 00 01 	bl      32a0 <sub_80297B18__14TObjCMMainMenuFv+0x1d8>
			32a0: R_PPC_REL24	reset_icon_flags__10TObjCMIconFv
    32a4:	48 00 00 88 	b       332c <sub_80297B18__14TObjCMMainMenuFv+0x264>
    32a8:	80 1f 00 2c 	lwz     r0,44(r31)
    32ac:	80 7f 00 24 	lwz     r3,36(r31)
    32b0:	54 00 10 3a 	slwi    r0,r0,2
    32b4:	7c 03 00 2e 	lwzx    r0,r3,r0
    32b8:	2c 00 00 08 	cmpwi   r0,8
    32bc:	41 82 00 70 	beq     332c <sub_80297B18__14TObjCMMainMenuFv+0x264>
    32c0:	40 80 00 18 	bge     32d8 <sub_80297B18__14TObjCMMainMenuFv+0x210>
    32c4:	2c 00 00 07 	cmpwi   r0,7
    32c8:	40 80 00 08 	bge     32d0 <sub_80297B18__14TObjCMMainMenuFv+0x208>
    32cc:	48 00 00 0c 	b       32d8 <sub_80297B18__14TObjCMMainMenuFv+0x210>
    32d0:	48 00 00 01 	bl      32d0 <sub_80297B18__14TObjCMMainMenuFv+0x208>
			32d0: R_PPC_REL24	reset_icon_flags__10TObjCMIconFv
    32d4:	48 00 00 58 	b       332c <sub_80297B18__14TObjCMMainMenuFv+0x264>
    32d8:	80 00 00 00 	lwz     r0,0(0)
			32d8: R_PPC_EMB_SDA21	lbl_805DDA64
    32dc:	38 81 00 0c 	addi    r4,r1,12
    32e0:	38 60 00 01 	li      r3,1
    32e4:	90 01 00 0c 	stw     r0,12(r1)
    32e8:	48 00 00 01 	bl      32e8 <sub_80297B18__14TObjCMMainMenuFv+0x220>
			32e8: R_PPC_REL24	TObjCMIcon__sub_802994C8
    32ec:	48 00 00 40 	b       332c <sub_80297B18__14TObjCMMainMenuFv+0x264>
    32f0:	80 1f 00 30 	lwz     r0,48(r31)
    32f4:	2c 00 00 00 	cmpwi   r0,0
    32f8:	41 82 00 10 	beq     3308 <sub_80297B18__14TObjCMMainMenuFv+0x240>
    32fc:	80 00 00 00 	lwz     r0,0(0)
			32fc: R_PPC_EMB_SDA21	creation_resource_ready_state
    3300:	2c 00 00 02 	cmpwi   r0,2
    3304:	40 82 00 1c 	bne     3320 <sub_80297B18__14TObjCMMainMenuFv+0x258>
    3308:	80 00 00 00 	lwz     r0,0(0)
			3308: R_PPC_EMB_SDA21	lbl_805DDA68
    330c:	38 81 00 08 	addi    r4,r1,8
    3310:	38 60 00 01 	li      r3,1
    3314:	90 01 00 08 	stw     r0,8(r1)
    3318:	48 00 00 01 	bl      3318 <sub_80297B18__14TObjCMMainMenuFv+0x250>
			3318: R_PPC_REL24	TObjCMIcon__sub_802994C8
    331c:	48 00 00 10 	b       332c <sub_80297B18__14TObjCMMainMenuFv+0x264>
    3320:	48 00 00 01 	bl      3320 <sub_80297B18__14TObjCMMainMenuFv+0x258>
			3320: R_PPC_REL24	reset_icon_flags__10TObjCMIconFv
    3324:	48 00 00 08 	b       332c <sub_80297B18__14TObjCMMainMenuFv+0x264>
    3328:	48 00 00 01 	bl      3328 <sub_80297B18__14TObjCMMainMenuFv+0x260>
			3328: R_PPC_REL24	reset_icon_flags__10TObjCMIconFv
    332c:	e3 e1 00 88 	psq_l   f31,136(r1),0,0
    3330:	cb e1 00 80 	lfd     f31,128(r1)
    3334:	e3 c1 00 78 	lq      r30,112(r1)
    3338:	cb c1 00 70 	lfd     f30,112(r1)
    333c:	e3 a1 00 68 	psq_l   f29,104(r1),0,0
    3340:	cb a1 00 60 	lfd     f29,96(r1)
    3344:	e3 81 00 58 	lq      r28,80(r1)
    3348:	cb 81 00 50 	lfd     f28,80(r1)
    334c:	e3 61 00 48 	psq_l   f27,72(r1),0,0
    3350:	cb 61 00 40 	lfd     f27,64(r1)
    3354:	bb 61 00 2c 	lmw     r27,44(r1)
    3358:	80 01 00 94 	lwz     r0,148(r1)
    335c:	7c 08 03 a6 	mtlr    r0
    3360:	38 21 00 90 	addi    r1,r1,144
    3364:	4e 80 00 20 	blr

00003368 <draw_footer_divider__14TObjCMMainMenuFv>:
    3368:	94 21 ff 60 	stwu    r1,-160(r1)
    336c:	7c 08 02 a6 	mflr    r0
    3370:	90 01 00 a4 	stw     r0,164(r1)
    3374:	db e1 00 90 	stfd    f31,144(r1)
    3378:	f3 e1 00 98 	xscmpgedp vs31,vs1,vs0
    337c:	db c1 00 80 	stfd    f30,128(r1)
    3380:	f3 c1 00 88 	xsmsubasp vs30,vs1,vs0
    3384:	db a1 00 70 	stfd    f29,112(r1)
    3388:	f3 a1 00 78 	xxsel   vs29,vs1,vs0,vs33
    338c:	be 61 00 3c 	stmw    r19,60(r1)
    3390:	7c 7f 1b 78 	mr      r31,r3
    3394:	48 00 00 01 	bl      3394 <draw_footer_divider__14TObjCMMainMenuFv+0x2c>
			3394: R_PPC_REL24	get_scale__14TObjCMMainMenuFv
    3398:	c0 40 00 00 	lfs     f2,0(0)
			3398: R_PPC_EMB_SDA21	lbl_805DDBB0
    339c:	3c 60 00 00 	lis     r3,0
			339e: R_PPC_ADDR16_HA	@917
    33a0:	c0 00 00 00 	lfs     f0,0(0)
			33a0: R_PPC_EMB_SDA21	lbl_805DDBB4
    33a4:	38 c0 00 00 	li      r6,0
    33a8:	ef c2 00 72 	fmuls   f30,f2,f1
    33ac:	38 00 00 04 	li      r0,4
    33b0:	ec 00 00 72 	fmuls   f0,f0,f1
    33b4:	3c a0 00 00 	lis     r5,0
			33b6: R_PPC_ADDR16_HA	footer_divider_vertices
    33b8:	3c 80 00 00 	lis     r4,0
			33ba: R_PPC_ADDR16_HA	footer_divider_colors
    33bc:	90 c1 00 20 	stw     r6,32(r1)
    33c0:	ef be 00 2a 	fadds   f29,f30,f0
    33c4:	cb e3 00 00 	lfd     f31,0(r3)
			33c6: R_PPC_ADDR16_LO	@917
    33c8:	90 01 00 24 	stw     r0,36(r1)
    33cc:	3b 61 00 08 	addi    r27,r1,8
    33d0:	3b 05 00 00 	addi    r24,r5,0
			33d2: R_PPC_ADDR16_LO	footer_divider_vertices
    33d4:	3b 24 00 00 	addi    r25,r4,0
			33d6: R_PPC_ADDR16_LO	footer_divider_colors
    33d8:	3a a0 00 00 	li      r21,0
    33dc:	3b c0 00 00 	li      r30,0
    33e0:	3b a0 00 00 	li      r29,0
    33e4:	3f 40 43 30 	lis     r26,17200
    33e8:	7e d8 ea 14 	add     r22,r24,r29
    33ec:	7e f9 f2 14 	add     r23,r25,r30
    33f0:	d3 d6 00 0c 	stfs    f30,12(r22)
    33f4:	3a 80 00 00 	li      r20,0
    33f8:	3b 80 00 00 	li      r28,0
    33fc:	d3 d6 00 04 	stfs    f30,4(r22)
    3400:	d3 b6 00 1c 	stfs    f29,28(r22)
    3404:	d3 b6 00 14 	stfs    f29,20(r22)
    3408:	7e 77 e0 2e 	lwzx    r19,r23,r28
    340c:	93 41 00 28 	stw     r26,40(r1)
    3410:	56 60 46 3e 	srwi    r0,r19,24
    3414:	c0 1f 00 38 	lfs     f0,56(r31)
    3418:	90 01 00 2c 	stw     r0,44(r1)
    341c:	c8 21 00 28 	lfd     f1,40(r1)
    3420:	ec 21 f8 28 	fsubs   f1,f1,f31
    3424:	ec 21 00 32 	fmuls   f1,f1,f0
    3428:	48 00 00 01 	bl      3428 <draw_footer_divider__14TObjCMMainMenuFv+0xc0>
			3428: R_PPC_REL24	__cvt_fp2unsigned
    342c:	3a 94 00 01 	addi    r20,r20,1
    3430:	7e 60 9b 78 	mr      r0,r19
    3434:	50 60 c0 0e 	rlwimi  r0,r3,24,0,7
    3438:	7c 1b e1 2e 	stwx    r0,r27,r28
    343c:	2c 14 00 04 	cmpwi   r20,4
    3440:	3b 9c 00 04 	addi    r28,r28,4
    3444:	41 80 ff c4 	blt     3408 <draw_footer_divider__14TObjCMMainMenuFv+0xa0>
    3448:	93 61 00 1c 	stw     r27,28(r1)
    344c:	38 61 00 18 	addi    r3,r1,24
    3450:	c0 20 00 00 	lfs     f1,0(0)
			3450: R_PPC_EMB_SDA21	lbl_805DDB90
    3454:	38 80 00 04 	li      r4,4
    3458:	92 c1 00 18 	stw     r22,24(r1)
    345c:	38 a0 00 06 	li      r5,6
    3460:	48 00 00 01 	bl      3460 <draw_footer_divider__14TObjCMMainMenuFv+0xf8>
			3460: R_PPC_REL24	draw_strip_swap_color__15TWindowCtrlMainFllf
    3464:	3a b5 00 01 	addi    r21,r21,1
    3468:	3b bd 00 20 	addi    r29,r29,32
    346c:	2c 15 00 02 	cmpwi   r21,2
    3470:	3b de 00 10 	addi    r30,r30,16
    3474:	41 80 ff 74 	blt     33e8 <draw_footer_divider__14TObjCMMainMenuFv+0x80>
    3478:	e3 e1 00 98 	psq_l   f31,152(r1),0,0
    347c:	cb e1 00 90 	lfd     f31,144(r1)
    3480:	e3 c1 00 88 	lq      r30,128(r1)
    3484:	cb c1 00 80 	lfd     f30,128(r1)
    3488:	e3 a1 00 78 	psq_l   f29,120(r1),0,0
    348c:	cb a1 00 70 	lfd     f29,112(r1)
    3490:	ba 61 00 3c 	lmw     r19,60(r1)
    3494:	80 01 00 a4 	lwz     r0,164(r1)
    3498:	7c 08 03 a6 	mtlr    r0
    349c:	38 21 00 a0 	addi    r1,r1,160
    34a0:	4e 80 00 20 	blr

000034a4 <sub_802981BC__14TObjCMMainMenuFv>:
    34a4:	4e 80 00 20 	blr

000034a8 <sub_80297EF4__14TObjCMMainMenuFv>:
    34a8:	94 21 ff a0 	stwu    r1,-96(r1)
    34ac:	7c 08 02 a6 	mflr    r0
    34b0:	90 01 00 64 	stw     r0,100(r1)
    34b4:	db e1 00 50 	stfd    f31,80(r1)
    34b8:	f3 e1 00 58 	xscmpgtdp vs31,vs1,vs0
    34bc:	db c1 00 40 	stfd    f30,64(r1)
    34c0:	f3 c1 00 48 	xsmaddmsp vs30,vs1,vs0
    34c4:	bf a1 00 34 	stmw    r29,52(r1)
    34c8:	7c 7f 1b 78 	mr      r31,r3
    34cc:	48 00 00 01 	bl      34cc <sub_80297EF4__14TObjCMMainMenuFv+0x24>
			34cc: R_PPC_REL24	get_scale__14TObjCMMainMenuFv
    34d0:	c0 5f 00 48 	lfs     f2,72(r31)
    34d4:	ff e0 08 90 	fmr     f31,f1
    34d8:	c0 00 00 00 	lfs     f0,0(0)
			34d8: R_PPC_EMB_SDA21	@1129
    34dc:	fc 02 00 40 	fcmpo   cr0,f2,f0
    34e0:	4c 41 13 82 	cror    eq,gt,eq
    34e4:	40 82 00 0c 	bne     34f0 <sub_80297EF4__14TObjCMMainMenuFv+0x48>
    34e8:	c3 c0 00 00 	lfs     f30,0(0)
			34e8: R_PPC_EMB_SDA21	@56
    34ec:	48 00 00 08 	b       34f4 <sub_80297EF4__14TObjCMMainMenuFv+0x4c>
    34f0:	ef c2 00 24 	fdivs   f30,f2,f0
    34f4:	38 60 00 9a 	li      r3,154
    34f8:	48 00 00 01 	bl      34f8 <sub_80297EF4__14TObjCMMainMenuFv+0x50>
			34f8: R_PPC_REL24	get_creation_sprite_id__14TObjCMMainMenuFl
    34fc:	6c 63 80 00 	xoris   r3,r3,32768
    3500:	3c 00 43 30 	lis     r0,17200
    3504:	90 61 00 1c 	stw     r3,28(r1)
    3508:	3c 80 00 00 	lis     r4,0
			350a: R_PPC_ADDR16_HA	@268
    350c:	c8 84 00 00 	lfd     f4,0(r4)
			350e: R_PPC_ADDR16_LO	@268
    3510:	fc 40 f0 90 	fmr     f2,f30
    3514:	90 01 00 18 	stw     r0,24(r1)
    3518:	38 81 00 10 	addi    r4,r1,16
    351c:	c0 00 00 00 	lfs     f0,0(0)
			351c: R_PPC_EMB_SDA21	@1131
    3520:	38 60 00 9a 	li      r3,154
    3524:	c8 21 00 18 	lfd     f1,24(r1)
    3528:	c0 60 00 00 	lfs     f3,0(0)
			3528: R_PPC_EMB_SDA21	@1130
    352c:	ec 81 20 28 	fsubs   f4,f1,f4
    3530:	d0 01 00 14 	stfs    f0,20(r1)
    3534:	c0 20 00 00 	lfs     f1,0(0)
			3534: R_PPC_EMB_SDA21	@1132
    3538:	ec 03 20 28 	fsubs   f0,f3,f4
    353c:	d0 01 00 10 	stfs    f0,16(r1)
    3540:	48 00 00 01 	bl      3540 <sub_80297EF4__14TObjCMMainMenuFv+0x98>
			3540: R_PPC_REL24	draw_ui_sprite
    3544:	38 60 00 96 	li      r3,150
    3548:	48 00 00 01 	bl      3548 <sub_80297EF4__14TObjCMMainMenuFv+0xa0>
			3548: R_PPC_REL24	get_creation_sprite_id__14TObjCMMainMenuFl
    354c:	6c 63 80 00 	xoris   r3,r3,32768
    3550:	3c 00 43 30 	lis     r0,17200
    3554:	90 61 00 24 	stw     r3,36(r1)
    3558:	3c 80 00 00 	lis     r4,0
			355a: R_PPC_ADDR16_HA	@268
    355c:	c8 84 00 00 	lfd     f4,0(r4)
			355e: R_PPC_ADDR16_LO	@268
    3560:	fc 40 f0 90 	fmr     f2,f30
    3564:	90 01 00 20 	stw     r0,32(r1)
    3568:	38 81 00 10 	addi    r4,r1,16
    356c:	c0 00 00 00 	lfs     f0,0(0)
			356c: R_PPC_EMB_SDA21	@1134
    3570:	38 60 00 96 	li      r3,150
    3574:	c8 21 00 20 	lfd     f1,32(r1)
    3578:	c0 60 00 00 	lfs     f3,0(0)
			3578: R_PPC_EMB_SDA21	@1133
    357c:	ec 81 20 28 	fsubs   f4,f1,f4
    3580:	d0 01 00 14 	stfs    f0,20(r1)
    3584:	c0 20 00 00 	lfs     f1,0(0)
			3584: R_PPC_EMB_SDA21	@1132
    3588:	ec 03 20 28 	fsubs   f0,f3,f4
    358c:	d0 01 00 10 	stfs    f0,16(r1)
    3590:	48 00 00 01 	bl      3590 <sub_80297EF4__14TObjCMMainMenuFv+0xe8>
			3590: R_PPC_REL24	draw_ui_sprite
    3594:	38 60 00 99 	li      r3,153
    3598:	48 00 00 01 	bl      3598 <sub_80297EF4__14TObjCMMainMenuFv+0xf0>
			3598: R_PPC_REL24	get_creation_sprite_id__14TObjCMMainMenuFl
    359c:	6c 63 80 00 	xoris   r3,r3,32768
    35a0:	3c 00 43 30 	lis     r0,17200
    35a4:	90 61 00 2c 	stw     r3,44(r1)
    35a8:	3c 80 00 00 	lis     r4,0
			35aa: R_PPC_ADDR16_HA	@268
    35ac:	c8 84 00 00 	lfd     f4,0(r4)
			35ae: R_PPC_ADDR16_LO	@268
    35b0:	fc 40 f0 90 	fmr     f2,f30
    35b4:	90 01 00 28 	stw     r0,40(r1)
    35b8:	38 81 00 10 	addi    r4,r1,16
    35bc:	c0 00 00 00 	lfs     f0,0(0)
			35bc: R_PPC_EMB_SDA21	@1136
    35c0:	38 60 00 99 	li      r3,153
    35c4:	c8 21 00 28 	lfd     f1,40(r1)
    35c8:	c0 60 00 00 	lfs     f3,0(0)
			35c8: R_PPC_EMB_SDA21	@1135
    35cc:	ec 81 20 28 	fsubs   f4,f1,f4
    35d0:	d0 01 00 14 	stfs    f0,20(r1)
    35d4:	c0 20 00 00 	lfs     f1,0(0)
			35d4: R_PPC_EMB_SDA21	@1132
    35d8:	ec 03 20 28 	fsubs   f0,f3,f4
    35dc:	d0 01 00 10 	stfs    f0,16(r1)
    35e0:	48 00 00 01 	bl      35e0 <sub_80297EF4__14TObjCMMainMenuFv+0x138>
			35e0: R_PPC_REL24	draw_ui_sprite
    35e4:	c0 00 00 00 	lfs     f0,0(0)
			35e4: R_PPC_EMB_SDA21	@424
    35e8:	ec 20 07 b2 	fmuls   f1,f0,f30
    35ec:	48 00 00 01 	bl      35ec <sub_80297EF4__14TObjCMMainMenuFv+0x144>
			35ec: R_PPC_REL24	__cvt_fp2unsigned
    35f0:	80 9f 00 1c 	lwz     r4,28(r31)
    35f4:	54 60 c0 0e 	slwi    r0,r3,24
    35f8:	64 1e 00 ff 	oris    r30,r0,255
    35fc:	88 04 00 32 	lbz     r0,50(r4)
    3600:	63 de ff ff 	ori     r30,r30,65535
    3604:	8b a4 00 31 	lbz     r29,49(r4)
    3608:	54 00 07 bd 	rlwinm. r0,r0,0,30,30
    360c:	7f bd 07 74 	extsb   r29,r29
    3610:	41 82 00 08 	beq     3618 <sub_80297EF4__14TObjCMMainMenuFv+0x170>
    3614:	3b a0 00 0c 	li      r29,12
    3618:	48 00 00 01 	bl      3618 <sub_80297EF4__14TObjCMMainMenuFv+0x170>
			3618: R_PPC_REL24	restore_full_screen_view__11TCameraCtrlFv
    361c:	c0 00 00 00 	lfs     f0,0(0)
			361c: R_PPC_EMB_SDA21	@1138
    3620:	3c 60 00 00 	lis     r3,0
			3622: R_PPC_ADDR16_HA	lbl_804DBC0C
    3624:	57 a0 10 3a 	slwi    r0,r29,2
    3628:	c0 20 00 00 	lfs     f1,0(0)
			3628: R_PPC_EMB_SDA21	@1137
    362c:	38 63 00 00 	addi    r3,r3,0
			362e: R_PPC_ADDR16_LO	lbl_804DBC0C
    3630:	ec 40 07 f2 	fmuls   f2,f0,f31
    3634:	7c 63 00 2e 	lwzx    r3,r3,r0
    3638:	7f c4 f3 78 	mr      r4,r30
    363c:	48 00 00 01 	bl      363c <sub_80297EF4__14TObjCMMainMenuFv+0x194>
			363c: R_PPC_REL24	draw_menu_text__FffPCcUl
    3640:	48 00 00 01 	bl      3640 <sub_80297EF4__14TObjCMMainMenuFv+0x198>
			3640: R_PPC_REL24	TCameraCtrl__sub_80068EF0
    3644:	80 7f 00 1c 	lwz     r3,28(r31)
    3648:	80 63 00 18 	lwz     r3,24(r3)
    364c:	54 60 00 0f 	clrrwi. r0,r3,24
    3650:	7c 7d 1b 78 	mr      r29,r3
    3654:	40 82 00 08 	bne     365c <sub_80297EF4__14TObjCMMainMenuFv+0x1b4>
    3658:	3b a0 ff ff 	li      r29,-1
    365c:	80 00 00 00 	lwz     r0,0(0)
			365c: R_PPC_EMB_SDA21	lbl_805DDBB8
    3660:	7f bd 00 38 	and     r29,r29,r0
    3664:	48 00 00 01 	bl      3664 <sub_80297EF4__14TObjCMMainMenuFv+0x1bc>
			3664: R_PPC_REL24	restore_full_screen_view__11TCameraCtrlFv
    3668:	c0 00 00 00 	lfs     f0,0(0)
			3668: R_PPC_EMB_SDA21	@1139
    366c:	57 c0 00 0e 	clrrwi  r0,r30,24
    3670:	c0 20 00 00 	lfs     f1,0(0)
			3670: R_PPC_EMB_SDA21	@1137
    3674:	7f a4 03 78 	or      r4,r29,r0
    3678:	ec 40 07 f2 	fmuls   f2,f0,f31
    367c:	80 7f 00 1c 	lwz     r3,28(r31)
    3680:	48 00 00 01 	bl      3680 <sub_80297EF4__14TObjCMMainMenuFv+0x1d8>
			3680: R_PPC_REL24	draw_menu_text__FffPCcUl
    3684:	48 00 00 01 	bl      3684 <sub_80297EF4__14TObjCMMainMenuFv+0x1dc>
			3684: R_PPC_REL24	TCameraCtrl__sub_80068EF0
    3688:	c0 3f 00 48 	lfs     f1,72(r31)
    368c:	c0 00 00 00 	lfs     f0,0(0)
			368c: R_PPC_EMB_SDA21	@1129
    3690:	fc 01 00 40 	fcmpo   cr0,f1,f0
    3694:	4c 40 13 82 	cror    eq,lt,eq
    3698:	41 82 00 b4 	beq     374c <sub_80297EF4__14TObjCMMainMenuFv+0x2a4>
    369c:	ec 21 00 28 	fsubs   f1,f1,f0
    36a0:	c0 00 00 00 	lfs     f0,0(0)
			36a0: R_PPC_EMB_SDA21	@1140
    36a4:	80 bf 00 1c 	lwz     r5,28(r31)
    36a8:	ef c1 00 24 	fdivs   f30,f1,f0
    36ac:	88 05 00 32 	lbz     r0,50(r5)
    36b0:	54 00 07 ff 	clrlwi. r0,r0,31
    36b4:	40 82 00 3c 	bne     36f0 <sub_80297EF4__14TObjCMMainMenuFv+0x248>
    36b8:	c0 20 00 00 	lfs     f1,0(0)
			36b8: R_PPC_EMB_SDA21	@1141
    36bc:	3c 60 00 00 	lis     r3,0
			36be: R_PPC_ADDR16_HA	lbl_804DBC40
    36c0:	c0 00 00 00 	lfs     f0,0(0)
			36c0: R_PPC_EMB_SDA21	@1142
    36c4:	fc 40 f0 90 	fmr     f2,f30
    36c8:	d0 21 00 08 	stfs    f1,8(r1)
    36cc:	38 63 00 00 	addi    r3,r3,0
			36ce: R_PPC_ADDR16_LO	lbl_804DBC40
    36d0:	c0 20 00 00 	lfs     f1,0(0)
			36d0: R_PPC_EMB_SDA21	@1132
    36d4:	38 81 00 08 	addi    r4,r1,8
    36d8:	d0 01 00 0c 	stfs    f0,12(r1)
    36dc:	88 05 00 30 	lbz     r0,48(r5)
    36e0:	7c 00 07 74 	extsb   r0,r0
    36e4:	54 00 10 3a 	slwi    r0,r0,2
    36e8:	7c 63 00 2e 	lwzx    r3,r3,r0
    36ec:	48 00 00 01 	bl      36ec <sub_80297EF4__14TObjCMMainMenuFv+0x244>
			36ec: R_PPC_REL24	draw_ui_sprite
    36f0:	80 7f 00 1c 	lwz     r3,28(r31)
    36f4:	88 63 00 30 	lbz     r3,48(r3)
    36f8:	7c 63 07 74 	extsb   r3,r3
    36fc:	48 00 00 01 	bl      36fc <sub_80297EF4__14TObjCMMainMenuFv+0x254>
			36fc: R_PPC_REL24	get_stat_table_entry__9TObjLukerFi
    3700:	80 9f 00 1c 	lwz     r4,28(r31)
    3704:	7c 7d 1b 78 	mr      r29,r3
    3708:	88 04 00 32 	lbz     r0,50(r4)
    370c:	54 00 07 ff 	clrlwi. r0,r0,31
    3710:	41 82 00 08 	beq     3718 <sub_80297EF4__14TObjCMMainMenuFv+0x270>
    3714:	3b a0 00 00 	li      r29,0
			3714: R_PPC_EMB_SDA21	lbl_805D3CD8
    3718:	48 00 00 01 	bl      3718 <sub_80297EF4__14TObjCMMainMenuFv+0x270>
			3718: R_PPC_REL24	restore_full_screen_view__11TCameraCtrlFv
    371c:	c0 00 00 00 	lfs     f0,0(0)
			371c: R_PPC_EMB_SDA21	@424
    3720:	ec 20 07 b2 	fmuls   f1,f0,f30
    3724:	48 00 00 01 	bl      3724 <sub_80297EF4__14TObjCMMainMenuFv+0x27c>
			3724: R_PPC_REL24	__cvt_fp2unsigned
    3728:	c0 00 00 00 	lfs     f0,0(0)
			3728: R_PPC_EMB_SDA21	@1143
    372c:	54 60 c0 0e 	slwi    r0,r3,24
    3730:	64 04 00 ff 	oris    r4,r0,255
    3734:	c0 20 00 00 	lfs     f1,0(0)
			3734: R_PPC_EMB_SDA21	@1137
    3738:	ec 40 07 f2 	fmuls   f2,f0,f31
    373c:	60 84 ff ff 	ori     r4,r4,65535
    3740:	7f a3 eb 78 	mr      r3,r29
    3744:	48 00 00 01 	bl      3744 <sub_80297EF4__14TObjCMMainMenuFv+0x29c>
			3744: R_PPC_REL24	draw_menu_text__FffPCcUl
    3748:	48 00 00 01 	bl      3748 <sub_80297EF4__14TObjCMMainMenuFv+0x2a0>
			3748: R_PPC_REL24	TCameraCtrl__sub_80068EF0
    374c:	e3 e1 00 58 	psq_l   f31,88(r1),0,0
    3750:	cb e1 00 50 	lfd     f31,80(r1)
    3754:	e3 c1 00 48 	lq      r30,64(r1)
    3758:	cb c1 00 40 	lfd     f30,64(r1)
    375c:	bb a1 00 34 	lmw     r29,52(r1)
    3760:	80 01 00 64 	lwz     r0,100(r1)
    3764:	7c 08 03 a6 	mtlr    r0
    3768:	38 21 00 60 	addi    r1,r1,96
    376c:	4e 80 00 20 	blr

00003770 <render__14TObjCMMainMenuFv>:
    3770:	94 21 ff d0 	stwu    r1,-48(r1)
    3774:	7c 08 02 a6 	mflr    r0
    3778:	3c 80 00 00 	lis     r4,0
			377a: R_PPC_ADDR16_HA	...data.0
    377c:	90 01 00 34 	stw     r0,52(r1)
    3780:	bf c1 00 28 	stmw    r30,40(r1)
    3784:	7c 7e 1b 78 	mr      r30,r3
    3788:	3b e4 00 00 	addi    r31,r4,0
			378a: R_PPC_ADDR16_LO	...data.0
    378c:	48 00 00 01 	bl      378c <render__14TObjCMMainMenuFv+0x1c>
			378c: R_PPC_REL24	set_depth_buffer_settings_1__Fv
    3790:	7f c3 f3 78 	mr      r3,r30
    3794:	48 00 00 01 	bl      3794 <render__14TObjCMMainMenuFv+0x24>
			3794: R_PPC_REL24	draw_footer_divider__14TObjCMMainMenuFv
    3798:	7f c3 f3 78 	mr      r3,r30
    379c:	48 00 00 01 	bl      379c <render__14TObjCMMainMenuFv+0x2c>
			379c: R_PPC_REL24	sub_80297B18__14TObjCMMainMenuFv
    37a0:	7f c3 f3 78 	mr      r3,r30
    37a4:	48 00 00 01 	bl      37a4 <render__14TObjCMMainMenuFv+0x34>
			37a4: R_PPC_REL24	TObjCMMainMenu__sub_802979BC
    37a8:	80 7e 00 50 	lwz     r3,80(r30)
    37ac:	48 00 00 01 	bl      37ac <render__14TObjCMMainMenuFv+0x3c>
			37ac: R_PPC_REL24	render_nodes__7TObjectFv
    37b0:	7f c3 f3 78 	mr      r3,r30
    37b4:	48 00 00 01 	bl      37b4 <render__14TObjCMMainMenuFv+0x44>
			37b4: R_PPC_REL24	draw_root_menu__14TObjCMMainMenuFv
    37b8:	88 00 00 00 	lbz     r0,0(0)
			37b8: R_PPC_EMB_SDA21	init$1086
    37bc:	7c 00 07 75 	extsb.  r0,r0
    37c0:	40 82 00 98 	bne     3858 <render__14TObjCMMainMenuFv+0xe8>
    37c4:	80 1f 02 50 	lwz     r0,592(r31)
    37c8:	3c 60 00 00 	lis     r3,0
			37ca: R_PPC_ADDR16_HA	__ptmf_null
    37cc:	80 bf 02 54 	lwz     r5,596(r31)
    37d0:	38 df 02 68 	addi    r6,r31,616
    37d4:	80 9f 02 58 	lwz     r4,600(r31)
    37d8:	90 1f 02 68 	stw     r0,616(r31)
    37dc:	38 00 00 01 	li      r0,1
    37e0:	85 23 00 00 	lwzu    r9,0(r3)
			37e2: R_PPC_ADDR16_LO	__ptmf_null
    37e4:	90 bf 02 6c 	stw     r5,620(r31)
    37e8:	80 bf 02 5c 	lwz     r5,604(r31)
    37ec:	90 9f 02 70 	stw     r4,624(r31)
    37f0:	80 9f 02 60 	lwz     r4,608(r31)
    37f4:	81 03 00 04 	lwz     r8,4(r3)
    37f8:	80 e3 00 08 	lwz     r7,8(r3)
    37fc:	80 7f 02 64 	lwz     r3,612(r31)
    3800:	91 21 00 08 	stw     r9,8(r1)
    3804:	91 01 00 0c 	stw     r8,12(r1)
    3808:	90 e1 00 10 	stw     r7,16(r1)
    380c:	91 26 00 0c 	stw     r9,12(r6)
    3810:	91 06 00 10 	stw     r8,16(r6)
    3814:	90 e6 00 14 	stw     r7,20(r6)
    3818:	90 a6 00 18 	stw     r5,24(r6)
    381c:	90 86 00 1c 	stw     r4,28(r6)
    3820:	90 66 00 20 	stw     r3,32(r6)
    3824:	91 26 00 24 	stw     r9,36(r6)
    3828:	91 06 00 28 	stw     r8,40(r6)
    382c:	90 e6 00 2c 	stw     r7,44(r6)
    3830:	91 26 00 30 	stw     r9,48(r6)
    3834:	91 06 00 34 	stw     r8,52(r6)
    3838:	90 e6 00 38 	stw     r7,56(r6)
    383c:	91 26 00 3c 	stw     r9,60(r6)
    3840:	91 06 00 40 	stw     r8,64(r6)
    3844:	90 e6 00 44 	stw     r7,68(r6)
    3848:	91 26 00 48 	stw     r9,72(r6)
    384c:	91 06 00 4c 	stw     r8,76(r6)
    3850:	90 e6 00 50 	stw     r7,80(r6)
    3854:	98 00 00 00 	stb     r0,0(0)
			3854: R_PPC_EMB_SDA21	init$1086
    3858:	80 80 00 00 	lwz     r4,0(0)
			3858: R_PPC_EMB_SDA21	TObjCMMainMenu__data_805D659C
    385c:	38 1f 02 68 	addi    r0,r31,616
    3860:	38 61 00 14 	addi    r3,r1,20
    3864:	1c 84 00 0c 	mulli   r4,r4,12
    3868:	7c c0 22 14 	add     r6,r0,r4
    386c:	80 a6 00 00 	lwz     r5,0(r6)
    3870:	80 86 00 04 	lwz     r4,4(r6)
    3874:	80 06 00 08 	lwz     r0,8(r6)
    3878:	90 a1 00 14 	stw     r5,20(r1)
    387c:	90 81 00 18 	stw     r4,24(r1)
    3880:	90 01 00 1c 	stw     r0,28(r1)
    3884:	48 00 00 01 	bl      3884 <render__14TObjCMMainMenuFv+0x114>
			3884: R_PPC_REL24	__ptmf_test
    3888:	2c 03 00 00 	cmpwi   r3,0
    388c:	41 82 00 14 	beq     38a0 <render__14TObjCMMainMenuFv+0x130>
    3890:	7f c3 f3 78 	mr      r3,r30
    3894:	39 81 00 14 	addi    r12,r1,20
    3898:	48 00 00 01 	bl      3898 <render__14TObjCMMainMenuFv+0x128>
			3898: R_PPC_REL24	__ptmf_scall
    389c:	60 00 00 00 	nop
    38a0:	48 00 00 01 	bl      38a0 <render__14TObjCMMainMenuFv+0x130>
			38a0: R_PPC_REL24	restore_saved_depth_alpha_state
    38a4:	7f c3 f3 78 	mr      r3,r30
    38a8:	48 00 00 01 	bl      38a8 <render__14TObjCMMainMenuFv+0x138>
			38a8: R_PPC_REL24	fn_802972BC
    38ac:	bb c1 00 28 	lmw     r30,40(r1)
    38b0:	80 01 00 34 	lwz     r0,52(r1)
    38b4:	7c 08 03 a6 	mtlr    r0
    38b8:	38 21 00 30 	addi    r1,r1,48
    38bc:	4e 80 00 20 	blr

000038c0 <TObjCMMainMenu__sub_80298310>:
    38c0:	4e 80 00 20 	blr

000038c4 <update_random_proportion_action__14TObjCMMainMenuFPv>:
    38c4:	94 21 ff e0 	stwu    r1,-32(r1)
    38c8:	7c 08 02 a6 	mflr    r0
    38cc:	90 01 00 24 	stw     r0,36(r1)
    38d0:	db e1 00 10 	stfd    f31,16(r1)
    38d4:	f3 e1 00 18 	xscmpeqdp vs31,vs1,vs0
    38d8:	48 00 00 01 	bl      38d8 <update_random_proportion_action__14TObjCMMainMenuFPv+0x14>
			38d8: R_PPC_REL24	is_active__23TAdSinglePlyChrSelectGCFv
    38dc:	2c 03 00 00 	cmpwi   r3,0
    38e0:	41 82 00 58 	beq     3938 <update_random_proportion_action__14TObjCMMainMenuFPv+0x74>
    38e4:	80 00 00 00 	lwz     r0,0(0)
			38e4: R_PPC_EMB_SDA21	TObjCMMainMenu__data_805D659C
    38e8:	2c 00 00 02 	cmpwi   r0,2
    38ec:	40 80 00 4c 	bge     3938 <update_random_proportion_action__14TObjCMMainMenuFPv+0x74>
    38f0:	2c 00 00 00 	cmpwi   r0,0
    38f4:	40 80 00 08 	bge     38fc <update_random_proportion_action__14TObjCMMainMenuFPv+0x38>
    38f8:	48 00 00 40 	b       3938 <update_random_proportion_action__14TObjCMMainMenuFPv+0x74>
    38fc:	48 00 00 01 	bl      38fc <update_random_proportion_action__14TObjCMMainMenuFPv+0x38>
			38fc: R_PPC_REL24	get_right_trigger_ratio__16TObjCMProportionFv
    3900:	ff e0 08 90 	fmr     f31,f1
    3904:	48 00 00 01 	bl      3904 <update_random_proportion_action__14TObjCMMainMenuFPv+0x40>
			3904: R_PPC_REL24	get_ratio__16TObjCMProportionFv
    3908:	ef e1 f8 28 	fsubs   f31,f1,f31
    390c:	fc 20 f8 90 	fmr     f1,f31
    3910:	48 00 00 01 	bl      3910 <update_random_proportion_action__14TObjCMMainMenuFPv+0x4c>
			3910: R_PPC_REL24	fabs_float
    3914:	c0 00 00 00 	lfs     f0,0(0)
			3914: R_PPC_EMB_SDA21	lbl_805DDBF4
    3918:	fc 01 00 40 	fcmpo   cr0,f1,f0
    391c:	40 81 00 1c 	ble     3938 <update_random_proportion_action__14TObjCMMainMenuFPv+0x74>
    3920:	c0 00 00 00 	lfs     f0,0(0)
			3920: R_PPC_EMB_SDA21	lbl_805DDBF8
    3924:	ec 00 07 f2 	fmuls   f0,f0,f31
    3928:	fc 00 00 1e 	fctiwz  f0,f0
    392c:	d8 01 00 08 	stfd    f0,8(r1)
    3930:	80 61 00 0c 	lwz     r3,12(r1)
    3934:	48 00 00 01 	bl      3934 <update_random_proportion_action__14TObjCMMainMenuFPv+0x70>
			3934: R_PPC_REL24	TObjCMMainMenu__sub_80298DA0
    3938:	e3 e1 00 18 	psq_l   f31,24(r1),0,0
    393c:	80 01 00 24 	lwz     r0,36(r1)
    3940:	cb e1 00 10 	lfd     f31,16(r1)
    3944:	7c 08 03 a6 	mtlr    r0
    3948:	38 21 00 20 	addi    r1,r1,32
    394c:	4e 80 00 20 	blr

00003950 <update_slide_offset__14TObjCMMainMenuFv>:
    3950:	80 00 00 00 	lwz     r0,0(0)
			3950: R_PPC_EMB_SDA21	TObjCMMainMenu__data_805D659C
    3954:	2c 00 00 01 	cmpwi   r0,1
    3958:	41 82 00 08 	beq     3960 <update_slide_offset__14TObjCMMainMenuFv+0x10>
    395c:	48 00 00 28 	b       3984 <update_slide_offset__14TObjCMMainMenuFv+0x34>
    3960:	c0 43 00 40 	lfs     f2,64(r3)
    3964:	c0 20 00 00 	lfs     f1,0(0)
			3964: R_PPC_EMB_SDA21	lbl_805DDBFC
    3968:	c0 00 00 00 	lfs     f0,0(0)
			3968: R_PPC_EMB_SDA21	lbl_805DDA90
    396c:	ec 22 08 2a 	fadds   f1,f2,f1
    3970:	fc 01 00 40 	fcmpo   cr0,f1,f0
    3974:	d0 23 00 40 	stfs    f1,64(r3)
    3978:	4c 80 00 20 	bgelr
    397c:	d0 03 00 40 	stfs    f0,64(r3)
    3980:	4e 80 00 20 	blr
    3984:	c0 43 00 40 	lfs     f2,64(r3)
    3988:	c0 20 00 00 	lfs     f1,0(0)
			3988: R_PPC_EMB_SDA21	TObjCMMainMenu__data_805DDC00
    398c:	c0 00 00 00 	lfs     f0,0(0)
			398c: R_PPC_EMB_SDA21	lbl_805DDA70
    3990:	ec 22 08 2a 	fadds   f1,f2,f1
    3994:	fc 01 00 40 	fcmpo   cr0,f1,f0
    3998:	d0 23 00 40 	stfs    f1,64(r3)
    399c:	4c 81 00 20 	blelr
    39a0:	d0 03 00 40 	stfs    f0,64(r3)
    39a4:	4e 80 00 20 	blr

000039a8 <update_submenu_fade__14TObjCMMainMenuFv>:
    39a8:	80 00 00 00 	lwz     r0,0(0)
			39a8: R_PPC_EMB_SDA21	TObjCMMainMenu__data_805D659C
    39ac:	2c 00 00 00 	cmpwi   r0,0
    39b0:	41 82 00 08 	beq     39b8 <update_submenu_fade__14TObjCMMainMenuFv+0x10>
    39b4:	48 00 00 28 	b       39dc <update_submenu_fade__14TObjCMMainMenuFv+0x34>
    39b8:	c0 43 00 3c 	lfs     f2,60(r3)
    39bc:	c0 20 00 00 	lfs     f1,0(0)
			39bc: R_PPC_EMB_SDA21	TObjCMMainMenu__data_805DDC00
    39c0:	c0 00 00 00 	lfs     f0,0(0)
			39c0: R_PPC_EMB_SDA21	@56
    39c4:	ec 22 08 2a 	fadds   f1,f2,f1
    39c8:	fc 01 00 40 	fcmpo   cr0,f1,f0
    39cc:	d0 23 00 3c 	stfs    f1,60(r3)
    39d0:	4c 81 00 20 	blelr
    39d4:	d0 03 00 3c 	stfs    f0,60(r3)
    39d8:	4e 80 00 20 	blr
    39dc:	c0 43 00 3c 	lfs     f2,60(r3)
    39e0:	c0 20 00 00 	lfs     f1,0(0)
			39e0: R_PPC_EMB_SDA21	lbl_805DDBFC
    39e4:	c0 00 00 00 	lfs     f0,0(0)
			39e4: R_PPC_EMB_SDA21	@54
    39e8:	ec 22 08 2a 	fadds   f1,f2,f1
    39ec:	fc 01 00 40 	fcmpo   cr0,f1,f0
    39f0:	d0 23 00 3c 	stfs    f1,60(r3)
    39f4:	4c 80 00 20 	bgelr
    39f8:	d0 03 00 3c 	stfs    f0,60(r3)
    39fc:	4e 80 00 20 	blr

00003a00 <update_menu_reveal__14TObjCMMainMenuFv>:
    3a00:	94 21 ff f0 	stwu    r1,-16(r1)
    3a04:	7c 08 02 a6 	mflr    r0
    3a08:	90 01 00 14 	stw     r0,20(r1)
    3a0c:	93 e1 00 0c 	stw     r31,12(r1)
    3a10:	7c 7f 1b 78 	mr      r31,r3
    3a14:	80 00 00 00 	lwz     r0,0(0)
			3a14: R_PPC_EMB_SDA21	TObjCMMainMenu__data_805D659C
    3a18:	2c 00 00 07 	cmpwi   r0,7
    3a1c:	40 80 00 34 	bge     3a50 <update_menu_reveal__14TObjCMMainMenuFv+0x50>
    3a20:	2c 00 00 03 	cmpwi   r0,3
    3a24:	40 80 00 08 	bge     3a2c <update_menu_reveal__14TObjCMMainMenuFv+0x2c>
    3a28:	48 00 00 28 	b       3a50 <update_menu_reveal__14TObjCMMainMenuFv+0x50>
    3a2c:	c0 5f 00 38 	lfs     f2,56(r31)
    3a30:	c0 20 00 00 	lfs     f1,0(0)
			3a30: R_PPC_EMB_SDA21	lbl_805DDC04
    3a34:	c0 00 00 00 	lfs     f0,0(0)
			3a34: R_PPC_EMB_SDA21	@54
    3a38:	ec 22 08 2a 	fadds   f1,f2,f1
    3a3c:	fc 01 00 40 	fcmpo   cr0,f1,f0
    3a40:	d0 3f 00 38 	stfs    f1,56(r31)
    3a44:	40 80 00 54 	bge     3a98 <update_menu_reveal__14TObjCMMainMenuFv+0x98>
    3a48:	d0 1f 00 38 	stfs    f0,56(r31)
    3a4c:	48 00 00 4c 	b       3a98 <update_menu_reveal__14TObjCMMainMenuFv+0x98>
    3a50:	c0 3f 00 38 	lfs     f1,56(r31)
    3a54:	c0 00 00 00 	lfs     f0,0(0)
			3a54: R_PPC_EMB_SDA21	lbl_805DDC08
    3a58:	ec 01 00 2a 	fadds   f0,f1,f0
    3a5c:	d0 1f 00 38 	stfs    f0,56(r31)
    3a60:	48 00 00 01 	bl      3a60 <update_menu_reveal__14TObjCMMainMenuFv+0x60>
			3a60: R_PPC_REL24	is_active__23TAdSinglePlyChrSelectGCFv
    3a64:	2c 03 00 00 	cmpwi   r3,0
    3a68:	41 82 00 1c 	beq     3a84 <update_menu_reveal__14TObjCMMainMenuFv+0x84>
    3a6c:	c0 00 00 00 	lfs     f0,0(0)
			3a6c: R_PPC_EMB_SDA21	lbl_805DDA70
    3a70:	c0 3f 00 38 	lfs     f1,56(r31)
    3a74:	c0 40 00 00 	lfs     f2,0(0)
			3a74: R_PPC_EMB_SDA21	lbl_805DDAFC
    3a78:	ec 00 08 28 	fsubs   f0,f0,f1
    3a7c:	ec 02 08 3a 	fmadds  f0,f2,f0,f1
    3a80:	d0 1f 00 38 	stfs    f0,56(r31)
    3a84:	c0 3f 00 38 	lfs     f1,56(r31)
    3a88:	c0 00 00 00 	lfs     f0,0(0)
			3a88: R_PPC_EMB_SDA21	@56
    3a8c:	fc 01 00 40 	fcmpo   cr0,f1,f0
    3a90:	40 81 00 08 	ble     3a98 <update_menu_reveal__14TObjCMMainMenuFv+0x98>
    3a94:	d0 1f 00 38 	stfs    f0,56(r31)
    3a98:	80 01 00 14 	lwz     r0,20(r1)
    3a9c:	83 e1 00 0c 	lwz     r31,12(r1)
    3aa0:	7c 08 03 a6 	mtlr    r0
    3aa4:	38 21 00 10 	addi    r1,r1,16
    3aa8:	4e 80 00 20 	blr

00003aac <sub_802984FC__14TObjCMMainMenuFv>:
    3aac:	80 83 00 30 	lwz     r4,48(r3)
    3ab0:	34 04 ff ff 	addic.  r0,r4,-1
    3ab4:	90 03 00 30 	stw     r0,48(r3)
    3ab8:	4c 80 00 20 	bgelr
    3abc:	38 00 00 04 	li      r0,4
    3ac0:	90 00 00 00 	stw     r0,0(0)
			3ac0: R_PPC_EMB_SDA21	TObjCMMainMenu__data_805D659C
    3ac4:	4e 80 00 20 	blr

00003ac8 <sub_80298518__14TObjCMMainMenuFv>:
    3ac8:	80 83 00 30 	lwz     r4,48(r3)
    3acc:	34 04 ff ff 	addic.  r0,r4,-1
    3ad0:	90 03 00 30 	stw     r0,48(r3)
    3ad4:	4c 80 00 20 	bgelr
    3ad8:	38 00 00 03 	li      r0,3
    3adc:	90 00 00 00 	stw     r0,0(0)
			3adc: R_PPC_EMB_SDA21	TObjCMMainMenu__data_805D659C
    3ae0:	4e 80 00 20 	blr

00003ae4 <sub_80298534__14TObjCMMainMenuFv>:
    3ae4:	94 21 ff f0 	stwu    r1,-16(r1)
    3ae8:	7c 08 02 a6 	mflr    r0
    3aec:	c0 00 00 00 	lfs     f0,0(0)
			3aec: R_PPC_EMB_SDA21	lbl_805DDC0C
    3af0:	90 01 00 14 	stw     r0,20(r1)
    3af4:	93 e1 00 0c 	stw     r31,12(r1)
    3af8:	7c 7f 1b 78 	mr      r31,r3
    3afc:	c0 23 00 48 	lfs     f1,72(r3)
    3b00:	ec 01 00 2a 	fadds   f0,f1,f0
    3b04:	d0 03 00 48 	stfs    f0,72(r3)
    3b08:	80 63 00 30 	lwz     r3,48(r3)
    3b0c:	34 03 ff ff 	addic.  r0,r3,-1
    3b10:	90 1f 00 30 	stw     r0,48(r31)
    3b14:	40 80 00 0c 	bge     3b20 <sub_80298534__14TObjCMMainMenuFv+0x3c>
    3b18:	38 00 00 00 	li      r0,0
    3b1c:	90 1f 00 30 	stw     r0,48(r31)
    3b20:	80 00 00 00 	lwz     r0,0(0)
			3b20: R_PPC_EMB_SDA21	creation_resource_ready_state
    3b24:	2c 00 00 02 	cmpwi   r0,2
    3b28:	41 82 00 10 	beq     3b38 <sub_80298534__14TObjCMMainMenuFv+0x54>
    3b2c:	80 1f 00 30 	lwz     r0,48(r31)
    3b30:	2c 00 00 00 	cmpwi   r0,0
    3b34:	40 82 00 80 	bne     3bb4 <sub_80298534__14TObjCMMainMenuFv+0xd0>
    3b38:	c0 5f 00 48 	lfs     f2,72(r31)
    3b3c:	c0 00 00 00 	lfs     f0,0(0)
			3b3c: R_PPC_EMB_SDA21	lbl_805DDBBC
    3b40:	fc 02 00 40 	fcmpo   cr0,f2,f0
    3b44:	40 80 00 14 	bge     3b58 <sub_80298534__14TObjCMMainMenuFv+0x74>
    3b48:	ec 00 10 28 	fsubs   f0,f0,f2
    3b4c:	c0 20 00 00 	lfs     f1,0(0)
			3b4c: R_PPC_EMB_SDA21	lbl_805DDAFC
    3b50:	ec 01 10 3a 	fmadds  f0,f1,f0,f2
    3b54:	d0 1f 00 48 	stfs    f0,72(r31)
    3b58:	c0 3f 00 48 	lfs     f1,72(r31)
    3b5c:	c0 00 00 00 	lfs     f0,0(0)
			3b5c: R_PPC_EMB_SDA21	lbl_805DDA70
    3b60:	fc 01 00 40 	fcmpo   cr0,f1,f0
    3b64:	40 81 00 08 	ble     3b6c <sub_80298534__14TObjCMMainMenuFv+0x88>
    3b68:	d0 1f 00 48 	stfs    f0,72(r31)
    3b6c:	38 60 00 04 	li      r3,4
    3b70:	48 00 00 01 	bl      3b70 <sub_80298534__14TObjCMMainMenuFv+0x8c>
			3b70: R_PPC_REL24	creation_buttons_pressed__Fl
    3b74:	2c 03 00 00 	cmpwi   r3,0
    3b78:	41 82 00 50 	beq     3bc8 <sub_80298534__14TObjCMMainMenuFv+0xe4>
    3b7c:	3c 60 00 05 	lis     r3,5
    3b80:	38 80 00 00 	li      r4,0
    3b84:	38 63 2d 01 	addi    r3,r3,11521
    3b88:	38 a0 00 00 	li      r5,0
    3b8c:	38 c0 00 00 	li      r6,0
    3b90:	48 00 00 01 	bl      3b90 <sub_80298534__14TObjCMMainMenuFv+0xac>
			3b90: R_PPC_REL24	play_sound_effect
    3b94:	38 60 00 07 	li      r3,7
    3b98:	38 00 00 05 	li      r0,5
    3b9c:	90 7f 00 30 	stw     r3,48(r31)
    3ba0:	38 60 00 07 	li      r3,7
    3ba4:	38 80 00 01 	li      r4,1
    3ba8:	90 00 00 00 	stw     r0,0(0)
			3ba8: R_PPC_EMB_SDA21	TObjCMMainMenu__data_805D659C
    3bac:	48 00 00 01 	bl      3bac <sub_80298534__14TObjCMMainMenuFv+0xc8>
			3bac: R_PPC_REL24	create_fade__14TObjCMMainMenuFPvPv
    3bb0:	48 00 00 18 	b       3bc8 <sub_80298534__14TObjCMMainMenuFv+0xe4>
    3bb4:	c0 3f 00 48 	lfs     f1,72(r31)
    3bb8:	c0 00 00 00 	lfs     f0,0(0)
			3bb8: R_PPC_EMB_SDA21	lbl_805DDBBC
    3bbc:	fc 01 00 40 	fcmpo   cr0,f1,f0
    3bc0:	40 81 00 08 	ble     3bc8 <sub_80298534__14TObjCMMainMenuFv+0xe4>
    3bc4:	d0 1f 00 48 	stfs    f0,72(r31)
    3bc8:	80 01 00 14 	lwz     r0,20(r1)
    3bcc:	83 e1 00 0c 	lwz     r31,12(r1)
    3bd0:	7c 08 03 a6 	mtlr    r0
    3bd4:	38 21 00 10 	addi    r1,r1,16
    3bd8:	4e 80 00 20 	blr

00003bdc <sub_8029862C__14TObjCMMainMenuFv>:
    3bdc:	4e 80 00 20 	blr

00003be0 <handle_creation_input__14TObjCMMainMenuFv>:
    3be0:	94 21 ff f0 	stwu    r1,-16(r1)
    3be4:	7c 08 02 a6 	mflr    r0
    3be8:	90 01 00 14 	stw     r0,20(r1)
    3bec:	93 e1 00 0c 	stw     r31,12(r1)
    3bf0:	7c 7f 1b 78 	mr      r31,r3
    3bf4:	48 00 00 01 	bl      3bf4 <handle_creation_input__14TObjCMMainMenuFv+0x14>
			3bf4: R_PPC_REL24	is_not_dressing_room_mode__14TObjCMMainMenuFv
    3bf8:	2c 03 00 00 	cmpwi   r3,0
    3bfc:	41 82 00 10 	beq     3c0c <handle_creation_input__14TObjCMMainMenuFv+0x2c>
    3c00:	38 60 00 01 	li      r3,1
    3c04:	48 00 00 01 	bl      3c04 <handle_creation_input__14TObjCMMainMenuFv+0x24>
			3c04: R_PPC_REL24	set_eff_tag__11TChCrEffTagFi
    3c08:	48 00 00 0c 	b       3c14 <handle_creation_input__14TObjCMMainMenuFv+0x34>
    3c0c:	38 60 00 02 	li      r3,2
    3c10:	48 00 00 01 	bl      3c10 <handle_creation_input__14TObjCMMainMenuFv+0x30>
			3c10: R_PPC_REL24	set_eff_tag__11TChCrEffTagFi
    3c14:	48 00 00 01 	bl      3c14 <handle_creation_input__14TObjCMMainMenuFv+0x34>
			3c14: R_PPC_REL24	is_active__23TAdSinglePlyChrSelectGCFv
    3c18:	2c 03 00 00 	cmpwi   r3,0
    3c1c:	41 82 01 2c 	beq     3d48 <handle_creation_input__14TObjCMMainMenuFv+0x168>
    3c20:	80 7f 00 1c 	lwz     r3,28(r31)
    3c24:	88 03 00 30 	lbz     r0,48(r3)
    3c28:	7c 00 07 74 	extsb   r0,r0
    3c2c:	2c 00 ff ff 	cmpwi   r0,-1
    3c30:	40 82 00 48 	bne     3c78 <handle_creation_input__14TObjCMMainMenuFv+0x98>
    3c34:	38 60 00 02 	li      r3,2
    3c38:	48 00 00 01 	bl      3c38 <handle_creation_input__14TObjCMMainMenuFv+0x58>
			3c38: R_PPC_REL24	creation_buttons_pressed__Fl
    3c3c:	2c 03 00 00 	cmpwi   r3,0
    3c40:	41 82 00 38 	beq     3c78 <handle_creation_input__14TObjCMMainMenuFv+0x98>
    3c44:	3c 60 00 05 	lis     r3,5
    3c48:	38 80 00 00 	li      r4,0
    3c4c:	38 63 37 04 	addi    r3,r3,14084
    3c50:	38 a0 00 00 	li      r5,0
    3c54:	38 c0 00 00 	li      r6,0
    3c58:	48 00 00 01 	bl      3c58 <handle_creation_input__14TObjCMMainMenuFv+0x78>
			3c58: R_PPC_REL24	play_sound_effect
    3c5c:	80 7f 00 1c 	lwz     r3,28(r31)
    3c60:	48 00 00 01 	bl      3c60 <handle_creation_input__14TObjCMMainMenuFv+0x80>
			3c60: R_PPC_REL24	TObjCMMainMenu__sub_8028D9B4
    3c64:	38 60 00 07 	li      r3,7
    3c68:	38 00 00 06 	li      r0,6
    3c6c:	90 7f 00 30 	stw     r3,48(r31)
    3c70:	90 00 00 00 	stw     r0,0(0)
			3c70: R_PPC_EMB_SDA21	TObjCMMainMenu__data_805D659C
    3c74:	48 00 00 d4 	b       3d48 <handle_creation_input__14TObjCMMainMenuFv+0x168>
    3c78:	38 60 00 20 	li      r3,32
    3c7c:	48 00 00 01 	bl      3c7c <handle_creation_input__14TObjCMMainMenuFv+0x9c>
			3c7c: R_PPC_REL24	creation_direction_repeated__Fl
    3c80:	2c 03 00 00 	cmpwi   r3,0
    3c84:	41 82 00 40 	beq     3cc4 <handle_creation_input__14TObjCMMainMenuFv+0xe4>
    3c88:	80 7f 00 2c 	lwz     r3,44(r31)
    3c8c:	38 63 00 01 	addi    r3,r3,1
    3c90:	90 7f 00 2c 	stw     r3,44(r31)
    3c94:	80 1f 00 28 	lwz     r0,40(r31)
    3c98:	7c 03 00 00 	cmpw    r3,r0
    3c9c:	41 80 00 0c 	blt     3ca8 <handle_creation_input__14TObjCMMainMenuFv+0xc8>
    3ca0:	38 00 00 00 	li      r0,0
    3ca4:	90 1f 00 2c 	stw     r0,44(r31)
    3ca8:	3c 60 00 05 	lis     r3,5
    3cac:	38 80 00 00 	li      r4,0
    3cb0:	38 63 41 00 	addi    r3,r3,16640
    3cb4:	38 a0 00 00 	li      r5,0
    3cb8:	38 c0 00 00 	li      r6,0
    3cbc:	48 00 00 01 	bl      3cbc <handle_creation_input__14TObjCMMainMenuFv+0xdc>
			3cbc: R_PPC_REL24	play_sound_effect
    3cc0:	48 00 00 48 	b       3d08 <handle_creation_input__14TObjCMMainMenuFv+0x128>
    3cc4:	38 60 00 10 	li      r3,16
    3cc8:	48 00 00 01 	bl      3cc8 <handle_creation_input__14TObjCMMainMenuFv+0xe8>
			3cc8: R_PPC_REL24	creation_direction_repeated__Fl
    3ccc:	2c 03 00 00 	cmpwi   r3,0
    3cd0:	41 82 00 38 	beq     3d08 <handle_creation_input__14TObjCMMainMenuFv+0x128>
    3cd4:	80 7f 00 2c 	lwz     r3,44(r31)
    3cd8:	34 03 ff ff 	addic.  r0,r3,-1
    3cdc:	90 1f 00 2c 	stw     r0,44(r31)
    3ce0:	40 80 00 10 	bge     3cf0 <handle_creation_input__14TObjCMMainMenuFv+0x110>
    3ce4:	80 7f 00 28 	lwz     r3,40(r31)
    3ce8:	38 03 ff ff 	addi    r0,r3,-1
    3cec:	90 1f 00 2c 	stw     r0,44(r31)
    3cf0:	3c 60 00 05 	lis     r3,5
    3cf4:	38 80 00 00 	li      r4,0
    3cf8:	38 63 41 00 	addi    r3,r3,16640
    3cfc:	38 a0 00 00 	li      r5,0
    3d00:	38 c0 00 00 	li      r6,0
    3d04:	48 00 00 01 	bl      3d04 <handle_creation_input__14TObjCMMainMenuFv+0x124>
			3d04: R_PPC_REL24	play_sound_effect
    3d08:	38 60 00 04 	li      r3,4
    3d0c:	48 00 00 01 	bl      3d0c <handle_creation_input__14TObjCMMainMenuFv+0x12c>
			3d0c: R_PPC_REL24	creation_buttons_pressed__Fl
    3d10:	2c 03 00 00 	cmpwi   r3,0
    3d14:	41 82 00 34 	beq     3d48 <handle_creation_input__14TObjCMMainMenuFv+0x168>
    3d18:	80 9f 00 2c 	lwz     r4,44(r31)
    3d1c:	3c 60 00 00 	lis     r3,0
			3d1e: R_PPC_ADDR16_HA	TObjCMMainMenu__data_804DB9C8
    3d20:	80 bf 00 24 	lwz     r5,36(r31)
    3d24:	38 03 00 00 	addi    r0,r3,0
			3d26: R_PPC_ADDR16_LO	TObjCMMainMenu__data_804DB9C8
    3d28:	54 84 10 3a 	slwi    r4,r4,2
    3d2c:	7f e3 fb 78 	mr      r3,r31
    3d30:	7c 85 20 2e 	lwzx    r4,r5,r4
    3d34:	54 84 20 36 	slwi    r4,r4,4
    3d38:	7c 80 22 14 	add     r4,r0,r4
    3d3c:	39 84 00 04 	addi    r12,r4,4
    3d40:	48 00 00 01 	bl      3d40 <handle_creation_input__14TObjCMMainMenuFv+0x160>
			3d40: R_PPC_REL24	__ptmf_scall
    3d44:	60 00 00 00 	nop
    3d48:	80 01 00 14 	lwz     r0,20(r1)
    3d4c:	83 e1 00 0c 	lwz     r31,12(r1)
    3d50:	7c 08 03 a6 	mtlr    r0
    3d54:	38 21 00 10 	addi    r1,r1,16
    3d58:	4e 80 00 20 	blr

00003d5c <run_task__14TObjCMMainMenuFv>:
    3d5c:	94 21 ff b0 	stwu    r1,-80(r1)
    3d60:	7c 08 02 a6 	mflr    r0
    3d64:	3c 80 00 00 	lis     r4,0
			3d66: R_PPC_ADDR16_HA	...data.0
    3d68:	90 01 00 54 	stw     r0,84(r1)
    3d6c:	be 41 00 18 	stmw    r18,24(r1)
    3d70:	7c 7e 1b 78 	mr      r30,r3
    3d74:	3b e4 00 00 	addi    r31,r4,0
			3d76: R_PPC_ADDR16_LO	...data.0
    3d78:	48 00 00 01 	bl      3d78 <run_task__14TObjCMMainMenuFv+0x1c>
			3d78: R_PPC_REL24	reset_proportions__15TChCrCharSelectFv
    3d7c:	48 00 00 01 	bl      3d7c <run_task__14TObjCMMainMenuFv+0x20>
			3d7c: R_PPC_REL24	rand
    3d80:	80 9e 00 34 	lwz     r4,52(r30)
    3d84:	7f c3 f3 78 	mr      r3,r30
    3d88:	38 04 00 01 	addi    r0,r4,1
    3d8c:	90 1e 00 34 	stw     r0,52(r30)
    3d90:	48 00 00 01 	bl      3d90 <run_task__14TObjCMMainMenuFv+0x34>
			3d90: R_PPC_REL24	update_menu_reveal__14TObjCMMainMenuFv
    3d94:	7f c3 f3 78 	mr      r3,r30
    3d98:	48 00 00 01 	bl      3d98 <run_task__14TObjCMMainMenuFv+0x3c>
			3d98: R_PPC_REL24	update_submenu_fade__14TObjCMMainMenuFv
    3d9c:	7f c3 f3 78 	mr      r3,r30
    3da0:	48 00 00 01 	bl      3da0 <run_task__14TObjCMMainMenuFv+0x44>
			3da0: R_PPC_REL24	update_slide_offset__14TObjCMMainMenuFv
    3da4:	88 00 00 00 	lbz     r0,0(0)
			3da4: R_PPC_EMB_SDA21	init$946
    3da8:	7c 00 07 75 	extsb.  r0,r0
    3dac:	40 82 00 b8 	bne     3e64 <run_task__14TObjCMMainMenuFv+0x108>
    3db0:	82 5f 01 a8 	lwz     r18,424(r31)
    3db4:	38 00 00 01 	li      r0,1
    3db8:	82 7f 01 ac 	lwz     r19,428(r31)
    3dbc:	3a bf 01 fc 	addi    r21,r31,508
    3dc0:	82 9f 01 b0 	lwz     r20,432(r31)
    3dc4:	82 df 01 b4 	lwz     r22,436(r31)
    3dc8:	82 ff 01 b8 	lwz     r23,440(r31)
    3dcc:	83 1f 01 bc 	lwz     r24,444(r31)
    3dd0:	83 3f 01 c0 	lwz     r25,448(r31)
    3dd4:	83 5f 01 c4 	lwz     r26,452(r31)
    3dd8:	83 7f 01 c8 	lwz     r27,456(r31)
    3ddc:	83 9f 01 cc 	lwz     r28,460(r31)
    3de0:	83 bf 01 d0 	lwz     r29,464(r31)
    3de4:	81 9f 01 d4 	lwz     r12,468(r31)
    3de8:	81 7f 01 d8 	lwz     r11,472(r31)
    3dec:	81 5f 01 dc 	lwz     r10,476(r31)
    3df0:	81 3f 01 e0 	lwz     r9,480(r31)
    3df4:	81 1f 01 e4 	lwz     r8,484(r31)
    3df8:	80 ff 01 e8 	lwz     r7,488(r31)
    3dfc:	80 df 01 ec 	lwz     r6,492(r31)
    3e00:	80 bf 01 f0 	lwz     r5,496(r31)
    3e04:	80 9f 01 f4 	lwz     r4,500(r31)
    3e08:	80 7f 01 f8 	lwz     r3,504(r31)
    3e0c:	92 5f 01 fc 	stw     r18,508(r31)
    3e10:	92 7f 02 00 	stw     r19,512(r31)
    3e14:	92 9f 02 04 	stw     r20,516(r31)
    3e18:	92 d5 00 0c 	stw     r22,12(r21)
    3e1c:	92 f5 00 10 	stw     r23,16(r21)
    3e20:	93 15 00 14 	stw     r24,20(r21)
    3e24:	93 35 00 18 	stw     r25,24(r21)
    3e28:	93 55 00 1c 	stw     r26,28(r21)
    3e2c:	93 75 00 20 	stw     r27,32(r21)
    3e30:	93 95 00 24 	stw     r28,36(r21)
    3e34:	93 b5 00 28 	stw     r29,40(r21)
    3e38:	91 95 00 2c 	stw     r12,44(r21)
    3e3c:	91 75 00 30 	stw     r11,48(r21)
    3e40:	91 55 00 34 	stw     r10,52(r21)
    3e44:	91 35 00 38 	stw     r9,56(r21)
    3e48:	91 15 00 3c 	stw     r8,60(r21)
    3e4c:	90 f5 00 40 	stw     r7,64(r21)
    3e50:	90 d5 00 44 	stw     r6,68(r21)
    3e54:	90 b5 00 48 	stw     r5,72(r21)
    3e58:	90 95 00 4c 	stw     r4,76(r21)
    3e5c:	90 75 00 50 	stw     r3,80(r21)
    3e60:	98 00 00 00 	stb     r0,0(0)
			3e60: R_PPC_EMB_SDA21	init$946
    3e64:	80 00 00 00 	lwz     r0,0(0)
			3e64: R_PPC_EMB_SDA21	TObjCMMainMenu__data_805D659C
    3e68:	39 9f 01 fc 	addi    r12,r31,508
    3e6c:	7f c3 f3 78 	mr      r3,r30
    3e70:	1c 00 00 0c 	mulli   r0,r0,12
    3e74:	7d 8c 02 14 	add     r12,r12,r0
    3e78:	48 00 00 01 	bl      3e78 <run_task__14TObjCMMainMenuFv+0x11c>
			3e78: R_PPC_REL24	__ptmf_scall
    3e7c:	60 00 00 00 	nop
    3e80:	80 1e 00 2c 	lwz     r0,44(r30)
    3e84:	7f c3 f3 78 	mr      r3,r30
    3e88:	80 9e 00 24 	lwz     r4,36(r30)
    3e8c:	54 00 10 3a 	slwi    r0,r0,2
    3e90:	7c 04 00 2e 	lwzx    r0,r4,r0
    3e94:	90 00 00 00 	stw     r0,0(0)
			3e94: R_PPC_EMB_SDA21	creation_menu_selected_entry
    3e98:	48 00 00 01 	bl      3e98 <run_task__14TObjCMMainMenuFv+0x13c>
			3e98: R_PPC_REL24	update_random_proportion_action__14TObjCMMainMenuFPv
    3e9c:	7f c3 f3 78 	mr      r3,r30
    3ea0:	48 00 00 01 	bl      3ea0 <run_task__14TObjCMMainMenuFv+0x144>
			3ea0: R_PPC_REL24	TObjCMMainMenu__sub_80298310
    3ea4:	80 00 00 00 	lwz     r0,0(0)
			3ea4: R_PPC_EMB_SDA21	TObjCMMainMenu__data_805D659C
    3ea8:	2c 00 00 05 	cmpwi   r0,5
    3eac:	41 82 00 48 	beq     3ef4 <run_task__14TObjCMMainMenuFv+0x198>
    3eb0:	40 80 00 10 	bge     3ec0 <run_task__14TObjCMMainMenuFv+0x164>
    3eb4:	2c 00 00 04 	cmpwi   r0,4
    3eb8:	40 80 00 10 	bge     3ec8 <run_task__14TObjCMMainMenuFv+0x16c>
    3ebc:	48 00 00 38 	b       3ef4 <run_task__14TObjCMMainMenuFv+0x198>
    3ec0:	2c 00 00 07 	cmpwi   r0,7
    3ec4:	40 80 00 30 	bge     3ef4 <run_task__14TObjCMMainMenuFv+0x198>
    3ec8:	c0 5e 00 54 	lfs     f2,84(r30)
    3ecc:	c0 20 00 00 	lfs     f1,0(0)
			3ecc: R_PPC_EMB_SDA21	lbl_805DDA90
    3ed0:	fc 02 08 40 	fcmpo   cr0,f2,f1
    3ed4:	40 81 00 98 	ble     3f6c <run_task__14TObjCMMainMenuFv+0x210>
    3ed8:	c0 00 00 00 	lfs     f0,0(0)
			3ed8: R_PPC_EMB_SDA21	lbl_805DDC10
    3edc:	ec 02 00 2a 	fadds   f0,f2,f0
    3ee0:	fc 00 08 40 	fcmpo   cr0,f0,f1
    3ee4:	d0 1e 00 54 	stfs    f0,84(r30)
    3ee8:	40 80 00 84 	bge     3f6c <run_task__14TObjCMMainMenuFv+0x210>
    3eec:	d0 3e 00 54 	stfs    f1,84(r30)
    3ef0:	48 00 00 7c 	b       3f6c <run_task__14TObjCMMainMenuFv+0x210>
    3ef4:	48 00 00 01 	bl      3ef4 <run_task__14TObjCMMainMenuFv+0x198>
			3ef4: R_PPC_REL24	is_active__23TAdSinglePlyChrSelectGCFv
    3ef8:	2c 03 00 00 	cmpwi   r3,0
    3efc:	41 82 00 68 	beq     3f64 <run_task__14TObjCMMainMenuFv+0x208>
    3f00:	48 00 00 01 	bl      3f00 <run_task__14TObjCMMainMenuFv+0x1a4>
			3f00: R_PPC_REL24	TAdSinglePlyChrSelectGC__sub_802905B8
    3f04:	2c 03 00 00 	cmpwi   r3,0
    3f08:	41 82 00 5c 	beq     3f64 <run_task__14TObjCMMainMenuFv+0x208>
    3f0c:	c0 3e 00 54 	lfs     f1,84(r30)
    3f10:	c0 60 00 00 	lfs     f3,0(0)
			3f10: R_PPC_EMB_SDA21	@56
    3f14:	fc 01 18 40 	fcmpo   cr0,f1,f3
    3f18:	40 80 00 54 	bge     3f6c <run_task__14TObjCMMainMenuFv+0x210>
    3f1c:	c0 00 00 00 	lfs     f0,0(0)
			3f1c: R_PPC_EMB_SDA21	@1277
    3f20:	c0 80 00 00 	lfs     f4,0(0)
			3f20: R_PPC_EMB_SDA21	@1275
    3f24:	fc 01 00 40 	fcmpo   cr0,f1,f0
    3f28:	40 81 00 1c 	ble     3f44 <run_task__14TObjCMMainMenuFv+0x1e8>
    3f2c:	ec 21 00 28 	fsubs   f1,f1,f0
    3f30:	c0 00 00 00 	lfs     f0,0(0)
			3f30: R_PPC_EMB_SDA21	@1278
    3f34:	c0 40 00 00 	lfs     f2,0(0)
			3f34: R_PPC_EMB_SDA21	@1276
    3f38:	ec 01 00 24 	fdivs   f0,f1,f0
    3f3c:	ec 02 18 3a 	fmadds  f0,f2,f0,f3
    3f40:	ec 84 00 32 	fmuls   f4,f4,f0
    3f44:	c0 3e 00 54 	lfs     f1,84(r30)
    3f48:	c0 00 00 00 	lfs     f0,0(0)
			3f48: R_PPC_EMB_SDA21	@56
    3f4c:	ec 21 20 2a 	fadds   f1,f1,f4
    3f50:	fc 01 00 40 	fcmpo   cr0,f1,f0
    3f54:	d0 3e 00 54 	stfs    f1,84(r30)
    3f58:	40 81 00 14 	ble     3f6c <run_task__14TObjCMMainMenuFv+0x210>
    3f5c:	d0 1e 00 54 	stfs    f0,84(r30)
    3f60:	48 00 00 0c 	b       3f6c <run_task__14TObjCMMainMenuFv+0x210>
    3f64:	c0 00 00 00 	lfs     f0,0(0)
			3f64: R_PPC_EMB_SDA21	lbl_805DDA90
    3f68:	d0 1e 00 54 	stfs    f0,84(r30)
    3f6c:	c0 20 00 00 	lfs     f1,0(0)
			3f6c: R_PPC_EMB_SDA21	lbl_805DDA70
    3f70:	c0 1e 00 54 	lfs     f0,84(r30)
    3f74:	c0 40 00 00 	lfs     f2,0(0)
			3f74: R_PPC_EMB_SDA21	lbl_805DDB00
    3f78:	ec 01 00 28 	fsubs   f0,f1,f0
    3f7c:	ec 22 00 32 	fmuls   f1,f2,f0
    3f80:	48 00 00 01 	bl      3f80 <run_task__14TObjCMMainMenuFv+0x224>
			3f80: R_PPC_REL24	set_speed__14TObjCMMainMenuFf
    3f84:	38 81 00 08 	addi    r4,r1,8
    3f88:	38 60 00 00 	li      r3,0
    3f8c:	48 00 00 01 	bl      3f8c <run_task__14TObjCMMainMenuFv+0x230>
			3f8c: R_PPC_REL24	get_creation_pad_stick__FPlPf
    3f90:	c0 21 00 08 	lfs     f1,8(r1)
    3f94:	c0 00 00 00 	lfs     f0,0(0)
			3f94: R_PPC_EMB_SDA21	lbl_805DDA90
    3f98:	fc 01 00 40 	fcmpo   cr0,f1,f0
    3f9c:	41 81 00 14 	bgt     3fb0 <run_task__14TObjCMMainMenuFv+0x254>
    3fa0:	38 60 00 f0 	li      r3,240
    3fa4:	48 00 00 01 	bl      3fa4 <run_task__14TObjCMMainMenuFv+0x248>
			3fa4: R_PPC_REL24	creation_buttons_held__Fl
    3fa8:	2c 03 00 00 	cmpwi   r3,0
    3fac:	41 82 00 24 	beq     3fd0 <run_task__14TObjCMMainMenuFv+0x274>
    3fb0:	80 1e 00 4c 	lwz     r0,76(r30)
    3fb4:	2c 00 00 00 	cmpwi   r0,0
    3fb8:	40 81 00 0c 	ble     3fc4 <run_task__14TObjCMMainMenuFv+0x268>
    3fbc:	38 60 00 00 	li      r3,0
    3fc0:	48 00 00 01 	bl      3fc0 <run_task__14TObjCMMainMenuFv+0x264>
			3fc0: R_PPC_REL24	request_creation_motion__Fl
    3fc4:	38 00 00 00 	li      r0,0
    3fc8:	90 1e 00 4c 	stw     r0,76(r30)
    3fcc:	48 00 00 48 	b       4014 <run_task__14TObjCMMainMenuFv+0x2b8>
    3fd0:	80 7e 00 4c 	lwz     r3,76(r30)
    3fd4:	38 03 00 01 	addi    r0,r3,1
    3fd8:	90 1e 00 4c 	stw     r0,76(r30)
    3fdc:	80 1e 00 4c 	lwz     r0,76(r30)
    3fe0:	2c 00 03 84 	cmpwi   r0,900
    3fe4:	40 82 00 10 	bne     3ff4 <run_task__14TObjCMMainMenuFv+0x298>
    3fe8:	38 60 00 01 	li      r3,1
    3fec:	48 00 00 01 	bl      3fec <run_task__14TObjCMMainMenuFv+0x290>
			3fec: R_PPC_REL24	request_creation_motion__Fl
    3ff0:	48 00 00 24 	b       4014 <run_task__14TObjCMMainMenuFv+0x2b8>
    3ff4:	2c 00 05 46 	cmpwi   r0,1350
    3ff8:	40 82 00 10 	bne     4008 <run_task__14TObjCMMainMenuFv+0x2ac>
    3ffc:	38 60 00 02 	li      r3,2
    4000:	48 00 00 01 	bl      4000 <run_task__14TObjCMMainMenuFv+0x2a4>
			4000: R_PPC_REL24	request_creation_motion__Fl
    4004:	48 00 00 10 	b       4014 <run_task__14TObjCMMainMenuFv+0x2b8>
    4008:	40 81 00 0c 	ble     4014 <run_task__14TObjCMMainMenuFv+0x2b8>
    400c:	38 00 05 46 	li      r0,1350
    4010:	90 1e 00 4c 	stw     r0,76(r30)
    4014:	80 7e 00 50 	lwz     r3,80(r30)
    4018:	48 00 00 01 	bl      4018 <run_task__14TObjCMMainMenuFv+0x2bc>
			4018: R_PPC_REL24	run_tasks__7TObjectFv
    401c:	7f c3 f3 78 	mr      r3,r30
    4020:	48 00 00 01 	bl      4020 <run_task__14TObjCMMainMenuFv+0x2c4>
			4020: R_PPC_REL24	fn_802972C0
    4024:	ba 41 00 18 	lmw     r18,24(r1)
    4028:	80 01 00 54 	lwz     r0,84(r1)
    402c:	7c 08 03 a6 	mtlr    r0
    4030:	38 21 00 50 	addi    r1,r1,80
    4034:	4e 80 00 20 	blr

00004038 <create__14TObjCMMainMenuFv>:
    4038:	94 21 ff f0 	stwu    r1,-16(r1)
    403c:	7c 08 02 a6 	mflr    r0
    4040:	90 01 00 14 	stw     r0,20(r1)
    4044:	93 e1 00 0c 	stw     r31,12(r1)
    4048:	7c 7f 1b 78 	mr      r31,r3
    404c:	38 60 00 58 	li      r3,88
    4050:	48 00 00 01 	bl      4050 <create__14TObjCMMainMenuFv+0x18>
			4050: R_PPC_REL24	__nw__7TObjectFUl
    4054:	7c 60 1b 79 	mr.     r0,r3
    4058:	41 82 00 10 	beq     4068 <create__14TObjCMMainMenuFv+0x30>
    405c:	7f e4 fb 78 	mr      r4,r31
    4060:	48 00 00 01 	bl      4060 <create__14TObjCMMainMenuFv+0x28>
			4060: R_PPC_REL24	TObjCMMainMenu__ct
    4064:	7c 60 1b 78 	mr      r0,r3
    4068:	7c 03 03 78 	mr      r3,r0
    406c:	80 01 00 14 	lwz     r0,20(r1)
    4070:	83 e1 00 0c 	lwz     r31,12(r1)
    4074:	7c 08 03 a6 	mtlr    r0
    4078:	38 21 00 10 	addi    r1,r1,16
    407c:	4e 80 00 20 	blr

00004080 <destroy__14TObjCMMainMenuFs>:
    4080:	94 21 ff f0 	stwu    r1,-16(r1)
    4084:	7c 08 02 a6 	mflr    r0
    4088:	90 01 00 14 	stw     r0,20(r1)
    408c:	bf c1 00 08 	stmw    r30,8(r1)
    4090:	7c 7e 1b 79 	mr.     r30,r3
    4094:	7c 9f 23 78 	mr      r31,r4
    4098:	41 82 00 70 	beq     4108 <destroy__14TObjCMMainMenuFs+0x88>
    409c:	3c 60 00 00 	lis     r3,0
			409e: R_PPC_ADDR16_HA	lbl_804DBDA8
    40a0:	38 03 00 00 	addi    r0,r3,0
			40a2: R_PPC_ADDR16_LO	lbl_804DBDA8
    40a4:	90 1e 00 18 	stw     r0,24(r30)
    40a8:	80 7e 00 50 	lwz     r3,80(r30)
    40ac:	28 03 00 00 	cmplwi  r3,0
    40b0:	41 82 00 24 	beq     40d4 <destroy__14TObjCMMainMenuFs+0x54>
    40b4:	41 82 00 18 	beq     40cc <destroy__14TObjCMMainMenuFs+0x4c>
    40b8:	81 83 00 18 	lwz     r12,24(r3)
    40bc:	38 80 00 01 	li      r4,1
    40c0:	81 8c 00 08 	lwz     r12,8(r12)
    40c4:	7d 89 03 a6 	mtctr   r12
    40c8:	4e 80 04 21 	bctrl
    40cc:	38 00 00 00 	li      r0,0
    40d0:	90 1e 00 50 	stw     r0,80(r30)
    40d4:	80 9e 00 1c 	lwz     r4,28(r30)
    40d8:	38 a0 ff ff 	li      r5,-1
    40dc:	38 00 00 02 	li      r0,2
    40e0:	7f c3 f3 78 	mr      r3,r30
    40e4:	90 a4 00 18 	stw     r5,24(r4)
    40e8:	38 80 00 00 	li      r4,0
    40ec:	80 be 00 1c 	lwz     r5,28(r30)
    40f0:	98 05 00 33 	stb     r0,51(r5)
    40f4:	48 00 00 01 	bl      40f4 <destroy__14TObjCMMainMenuFs+0x74>
			40f4: R_PPC_REL24	__dt__7TObjectFv
    40f8:	7f e0 07 35 	extsh.  r0,r31
    40fc:	40 81 00 0c 	ble     4108 <destroy__14TObjCMMainMenuFs+0x88>
    4100:	7f c3 f3 78 	mr      r3,r30
    4104:	48 00 00 01 	bl      4104 <destroy__14TObjCMMainMenuFs+0x84>
			4104: R_PPC_REL24	__dl__7TObjectFPv
    4108:	7f c3 f3 78 	mr      r3,r30
    410c:	bb c1 00 08 	lmw     r30,8(r1)
    4110:	80 01 00 14 	lwz     r0,20(r1)
    4114:	7c 08 03 a6 	mtlr    r0
    4118:	38 21 00 10 	addi    r1,r1,16
    411c:	4e 80 00 20 	blr

00004120 <TObjCMMainMenu__ct>:
    4120:	94 21 ff f0 	stwu    r1,-16(r1)
    4124:	7c 08 02 a6 	mflr    r0
    4128:	90 01 00 14 	stw     r0,20(r1)
    412c:	93 e1 00 0c 	stw     r31,12(r1)
    4130:	7c 7f 1b 78 	mr      r31,r3
    4134:	48 00 00 01 	bl      4134 <TObjCMMainMenu__ct+0x14>
			4134: R_PPC_REL24	__ct__7TObjectFP7TObject
    4138:	3c 60 00 00 	lis     r3,0
			413a: R_PPC_ADDR16_HA	lbl_804DBDA8
    413c:	38 03 00 00 	addi    r0,r3,0
			413e: R_PPC_ADDR16_LO	lbl_804DBDA8
    4140:	90 1f 00 18 	stw     r0,24(r31)
    4144:	80 00 00 00 	lwz     r0,0(0)
			4144: R_PPC_EMB_SDA21	lbl_805D3CD0
    4148:	90 1f 00 00 	stw     r0,0(r31)
    414c:	80 00 00 00 	lwz     r0,0(0)
			414c: R_PPC_EMB_SDA21	creation_player_character
    4150:	90 1f 00 1c 	stw     r0,28(r31)
    4154:	80 7f 00 1c 	lwz     r3,28(r31)
    4158:	88 03 00 32 	lbz     r0,50(r3)
    415c:	7c 00 07 74 	extsb   r0,r0
    4160:	70 00 00 0a 	andi.   r0,r0,10
    4164:	40 82 00 34 	bne     4198 <TObjCMMainMenu__ct+0x78>
    4168:	48 00 00 01 	bl      4168 <TObjCMMainMenu__ct+0x48>
			4168: R_PPC_REL24	TObjCMMainMenu__sub_8028D9A8
    416c:	80 9f 00 1c 	lwz     r4,28(r31)
    4170:	88 63 00 31 	lbz     r3,49(r3)
    4174:	88 04 00 31 	lbz     r0,49(r4)
    4178:	7c 63 07 74 	extsb   r3,r3
    417c:	7c 00 07 74 	extsb   r0,r0
    4180:	7c 00 18 00 	cmpw    r0,r3
    4184:	40 82 00 14 	bne     4198 <TObjCMMainMenu__ct+0x78>
    4188:	48 00 00 01 	bl      4188 <TObjCMMainMenu__ct+0x68>
			4188: R_PPC_REL24	TObjCMMainMenu__sub_8028D9A8
    418c:	7c 64 1b 78 	mr      r4,r3
    4190:	80 7f 00 1c 	lwz     r3,28(r31)
    4194:	48 00 00 01 	bl      4194 <TObjCMMainMenu__ct+0x74>
			4194: R_PPC_REL24	copy_player_visual_record
    4198:	48 00 00 01 	bl      4198 <TObjCMMainMenu__ct+0x78>
			4198: R_PPC_REL24	TObjCMMainMenu__sub_80298DD4
    419c:	7c 64 1b 78 	mr      r4,r3
    41a0:	80 7f 00 1c 	lwz     r3,28(r31)
    41a4:	38 a0 00 0c 	li      r5,12
    41a8:	48 00 00 01 	bl      41a8 <TObjCMMainMenu__ct+0x88>
			41a8: R_PPC_REL24	strncpy
    41ac:	80 7f 00 1c 	lwz     r3,28(r31)
    41b0:	38 a0 00 00 	li      r5,0
    41b4:	38 00 ff f5 	li      r0,-11
    41b8:	98 a3 00 0c 	stb     r5,12(r3)
    41bc:	80 7f 00 1c 	lwz     r3,28(r31)
    41c0:	98 a3 00 1c 	stb     r5,28(r3)
    41c4:	80 9f 00 1c 	lwz     r4,28(r31)
    41c8:	88 64 00 32 	lbz     r3,50(r4)
    41cc:	7c 60 00 38 	and     r0,r3,r0
    41d0:	98 04 00 32 	stb     r0,50(r4)
    41d4:	80 7f 00 1c 	lwz     r3,28(r31)
    41d8:	88 03 00 30 	lbz     r0,48(r3)
    41dc:	7c 00 07 74 	extsb   r0,r0
    41e0:	2c 00 ff ff 	cmpwi   r0,-1
    41e4:	40 82 00 40 	bne     4224 <TObjCMMainMenu__ct+0x104>
    41e8:	88 03 00 32 	lbz     r0,50(r3)
    41ec:	7c 00 07 74 	extsb   r0,r0
    41f0:	70 00 00 0a 	andi.   r0,r0,10
    41f4:	41 82 00 10 	beq     4204 <TObjCMMainMenu__ct+0xe4>
    41f8:	38 00 00 02 	li      r0,2
    41fc:	90 1f 00 20 	stw     r0,32(r31)
    4200:	48 00 00 60 	b       4260 <TObjCMMainMenu__ct+0x140>
    4204:	80 03 00 34 	lwz     r0,52(r3)
    4208:	54 00 06 f7 	rlwinm. r0,r0,0,27,27
    420c:	40 82 00 0c 	bne     4218 <TObjCMMainMenu__ct+0xf8>
    4210:	90 bf 00 20 	stw     r5,32(r31)
    4214:	48 00 00 4c 	b       4260 <TObjCMMainMenu__ct+0x140>
    4218:	38 00 00 01 	li      r0,1
    421c:	90 1f 00 20 	stw     r0,32(r31)
    4220:	48 00 00 40 	b       4260 <TObjCMMainMenu__ct+0x140>
    4224:	88 03 00 32 	lbz     r0,50(r3)
    4228:	7c 00 07 74 	extsb   r0,r0
    422c:	70 00 00 0a 	andi.   r0,r0,10
    4230:	41 82 00 10 	beq     4240 <TObjCMMainMenu__ct+0x120>
    4234:	38 00 00 05 	li      r0,5
    4238:	90 1f 00 20 	stw     r0,32(r31)
    423c:	48 00 00 24 	b       4260 <TObjCMMainMenu__ct+0x140>
    4240:	80 03 00 34 	lwz     r0,52(r3)
    4244:	54 00 06 f7 	rlwinm. r0,r0,0,27,27
    4248:	40 82 00 10 	bne     4258 <TObjCMMainMenu__ct+0x138>
    424c:	38 00 00 03 	li      r0,3
    4250:	90 1f 00 20 	stw     r0,32(r31)
    4254:	48 00 00 0c 	b       4260 <TObjCMMainMenu__ct+0x140>
    4258:	38 00 00 04 	li      r0,4
    425c:	90 1f 00 20 	stw     r0,32(r31)
    4260:	80 bf 00 20 	lwz     r5,32(r31)
    4264:	3c 60 00 00 	lis     r3,0
			4266: R_PPC_ADDR16_HA	creation_menu_mode_lists
    4268:	38 83 00 00 	addi    r4,r3,0
			426a: R_PPC_ADDR16_LO	creation_menu_mode_lists
    426c:	38 00 00 00 	li      r0,0
    4270:	54 a3 18 38 	slwi    r3,r5,3
    4274:	7c 64 18 2e 	lwzx    r3,r4,r3
    4278:	90 7f 00 28 	stw     r3,40(r31)
    427c:	80 7f 00 20 	lwz     r3,32(r31)
    4280:	54 63 18 38 	slwi    r3,r3,3
    4284:	7c 64 1a 14 	add     r3,r4,r3
    4288:	80 63 00 04 	lwz     r3,4(r3)
    428c:	90 7f 00 24 	stw     r3,36(r31)
    4290:	90 00 00 00 	stw     r0,0(0)
			4290: R_PPC_EMB_SDA21	TObjCMMainMenu__data_805D659C
    4294:	90 1f 00 2c 	stw     r0,44(r31)
    4298:	80 1f 00 2c 	lwz     r0,44(r31)
    429c:	80 7f 00 24 	lwz     r3,36(r31)
    42a0:	54 00 10 3a 	slwi    r0,r0,2
    42a4:	7c 03 00 2e 	lwzx    r0,r3,r0
    42a8:	90 00 00 00 	stw     r0,0(0)
			42a8: R_PPC_EMB_SDA21	creation_menu_selected_entry
    42ac:	48 00 00 01 	bl      42ac <TObjCMMainMenu__ct+0x18c>
			42ac: R_PPC_REL24	fn_802993F0
    42b0:	c0 00 00 00 	lfs     f0,0(0)
			42b0: R_PPC_EMB_SDA21	lbl_805DDA90
    42b4:	38 00 00 00 	li      r0,0
    42b8:	c0 20 00 00 	lfs     f1,0(0)
			42b8: R_PPC_EMB_SDA21	lbl_805DDB00
    42bc:	d0 1f 00 38 	stfs    f0,56(r31)
    42c0:	d0 1f 00 3c 	stfs    f0,60(r31)
    42c4:	d0 1f 00 40 	stfs    f0,64(r31)
    42c8:	d0 1f 00 44 	stfs    f0,68(r31)
    42cc:	d0 1f 00 48 	stfs    f0,72(r31)
    42d0:	90 1f 00 4c 	stw     r0,76(r31)
    42d4:	d0 1f 00 54 	stfs    f0,84(r31)
    42d8:	48 00 00 01 	bl      42d8 <TObjCMMainMenu__ct+0x1b8>
			42d8: R_PPC_REL24	set_speed__14TObjCMMainMenuFf
    42dc:	38 60 00 1c 	li      r3,28
    42e0:	48 00 00 01 	bl      42e0 <TObjCMMainMenu__ct+0x1c0>
			42e0: R_PPC_REL24	__nw__7TObjectFUl
    42e4:	7c 60 1b 79 	mr.     r0,r3
    42e8:	41 82 00 10 	beq     42f8 <TObjCMMainMenu__ct+0x1d8>
    42ec:	38 80 00 00 	li      r4,0
    42f0:	48 00 00 01 	bl      42f0 <TObjCMMainMenu__ct+0x1d0>
			42f0: R_PPC_REL24	__ct__7TObjectFP7TObject
    42f4:	7c 60 1b 78 	mr      r0,r3
    42f8:	90 1f 00 50 	stw     r0,80(r31)
    42fc:	48 00 00 01 	bl      42fc <TObjCMMainMenu__ct+0x1dc>
			42fc: R_PPC_REL24	fn_802947A8
    4300:	3c 60 00 00 	lis     r3,0
			4302: R_PPC_ADDR16_HA	lbl_80464F50
    4304:	38 63 00 00 	addi    r3,r3,0
			4306: R_PPC_ADDR16_LO	lbl_80464F50
    4308:	48 00 00 01 	bl      4308 <TObjCMMainMenu__ct+0x1e8>
			4308: R_PPC_REL24	fn_8029945C
    430c:	7f e3 fb 78 	mr      r3,r31
    4310:	48 00 00 01 	bl      4310 <TObjCMMainMenu__ct+0x1f0>
			4310: R_PPC_REL24	TObjCMMainMenu__sub_802972C4
    4314:	80 01 00 14 	lwz     r0,20(r1)
    4318:	7f e3 fb 78 	mr      r3,r31
    431c:	83 e1 00 0c 	lwz     r31,12(r1)
    4320:	7c 08 03 a6 	mtlr    r0
    4324:	38 21 00 10 	addi    r1,r1,16
    4328:	4e 80 00 20 	blr

0000432c <clear_task_state__14TObjCMMainMenuFv>:
    432c:	38 00 00 00 	li      r0,0
    4330:	90 00 00 00 	stw     r0,0(0)
			4330: R_PPC_EMB_SDA21	TObjCMMainMenu__data_805D659C
    4334:	4e 80 00 20 	blr

00004338 <get_scale__14TObjCMMainMenuFv>:
    4338:	c0 20 00 00 	lfs     f1,0(0)
			4338: R_PPC_EMB_SDA21	ui_sprite_scale
    433c:	4e 80 00 20 	blr

00004340 <get_proportion__14TObjCMMainMenuFv>:
    4340:	c0 20 00 00 	lfs     f1,0(0)
			4340: R_PPC_EMB_SDA21	creation_view_shift
    4344:	4e 80 00 20 	blr

00004348 <set_selection__14TObjCMMainMenuFi>:
    4348:	90 60 00 00 	stw     r3,0(0)
			4348: R_PPC_EMB_SDA21	creation_camera_mode
    434c:	4e 80 00 20 	blr

00004350 <TObjCMMainMenu__sub_80298DA0>:
    4350:	80 00 00 00 	lwz     r0,0(0)
			4350: R_PPC_EMB_SDA21	creation_figure_rotation_y
    4354:	7c 00 1a 14 	add     r0,r0,r3
    4358:	90 00 00 00 	stw     r0,0(0)
			4358: R_PPC_EMB_SDA21	creation_figure_rotation_y
    435c:	4e 80 00 20 	blr

00004360 <set_speed__14TObjCMMainMenuFf>:
    4360:	80 60 00 00 	lwz     r3,0(0)
			4360: R_PPC_EMB_SDA21	creation_figure_object
    4364:	28 03 00 00 	cmplwi  r3,0
    4368:	4d 82 00 20 	beqlr
    436c:	d0 23 00 38 	stfs    f1,56(r3)
    4370:	4e 80 00 20 	blr

00004374 <is_not_dressing_room_mode__14TObjCMMainMenuFv>:
    4374:	80 00 00 00 	lwz     r0,0(0)
			4374: R_PPC_EMB_SDA21	creation_dressing_room_mode_flag
    4378:	7c 00 00 34 	cntlzw  r0,r0
    437c:	54 03 de 3e 	rlwinm  r3,r0,27,24,31
    4380:	4e 80 00 20 	blr

00004384 <TObjCMMainMenu__sub_80298DD4>:
    4384:	3c 60 00 00 	lis     r3,0
			4386: R_PPC_ADDR16_HA	character_creation_name_buffer
    4388:	38 63 00 00 	addi    r3,r3,0
			438a: R_PPC_ADDR16_LO	character_creation_name_buffer
    438c:	4e 80 00 20 	blr

00004390 <get_creation_pad>:
    4390:	94 21 ff f0 	stwu    r1,-16(r1)
    4394:	7c 08 02 a6 	mflr    r0
    4398:	90 01 00 14 	stw     r0,20(r1)
    439c:	48 00 00 01 	bl      439c <get_creation_pad+0xc>
			439c: R_PPC_REL24	get_clamped_player_index__14TChCrEffCtrlPlFv
    43a0:	3c 80 00 00 	lis     r4,0
			43a2: R_PPC_ADDR16_HA	controller_physical_port_bank
    43a4:	54 60 10 3a 	slwi    r0,r3,2
    43a8:	38 64 00 00 	addi    r3,r4,0
			43aa: R_PPC_ADDR16_LO	controller_physical_port_bank
    43ac:	7c 63 00 2e 	lwzx    r3,r3,r0
    43b0:	80 01 00 14 	lwz     r0,20(r1)
    43b4:	7c 08 03 a6 	mtlr    r0
    43b8:	38 21 00 10 	addi    r1,r1,16
    43bc:	4e 80 00 20 	blr

000043c0 <__sinit_TObjCMName_cpp>:
    43c0:	94 21 ff a0 	stwu    r1,-96(r1)
    43c4:	3c 60 00 00 	lis     r3,0
			43c6: R_PPC_ADDR16_HA	...data.0
    43c8:	bd c1 00 18 	stmw    r14,24(r1)
    43cc:	3a 03 00 00 	addi    r16,r3,0
			43ce: R_PPC_ADDR16_LO	...data.0
    43d0:	3a 30 00 78 	addi    r17,r16,120
    43d4:	81 f0 00 68 	lwz     r15,104(r16)
    43d8:	80 10 00 60 	lwz     r0,96(r16)
    43dc:	91 e1 00 10 	stw     r15,16(r1)
    43e0:	81 f0 00 6c 	lwz     r15,108(r16)
    43e4:	90 11 00 84 	stw     r0,132(r17)
    43e8:	80 01 00 10 	lwz     r0,16(r1)
    43ec:	91 e1 00 08 	stw     r15,8(r1)
    43f0:	81 f0 00 70 	lwz     r15,112(r16)
    43f4:	90 11 00 8c 	stw     r0,140(r17)
    43f8:	80 01 00 08 	lwz     r0,8(r1)
    43fc:	91 e1 00 0c 	stw     r15,12(r1)
    4400:	82 50 00 00 	lwz     r18,0(r16)
    4404:	82 70 00 04 	lwz     r19,4(r16)
    4408:	82 90 00 08 	lwz     r20,8(r16)
    440c:	82 b0 00 0c 	lwz     r21,12(r16)
    4410:	82 d0 00 10 	lwz     r22,16(r16)
    4414:	82 f0 00 14 	lwz     r23,20(r16)
    4418:	83 10 00 18 	lwz     r24,24(r16)
    441c:	83 30 00 1c 	lwz     r25,28(r16)
    4420:	83 50 00 20 	lwz     r26,32(r16)
    4424:	83 70 00 24 	lwz     r27,36(r16)
    4428:	83 90 00 28 	lwz     r28,40(r16)
    442c:	83 b0 00 2c 	lwz     r29,44(r16)
    4430:	83 d0 00 30 	lwz     r30,48(r16)
    4434:	83 f0 00 34 	lwz     r31,52(r16)
    4438:	81 90 00 38 	lwz     r12,56(r16)
    443c:	81 70 00 3c 	lwz     r11,60(r16)
    4440:	81 50 00 40 	lwz     r10,64(r16)
    4444:	81 30 00 44 	lwz     r9,68(r16)
    4448:	81 10 00 48 	lwz     r8,72(r16)
    444c:	80 f0 00 4c 	lwz     r7,76(r16)
    4450:	80 d0 00 50 	lwz     r6,80(r16)
    4454:	80 b0 00 54 	lwz     r5,84(r16)
    4458:	80 90 00 58 	lwz     r4,88(r16)
    445c:	80 70 00 5c 	lwz     r3,92(r16)
    4460:	81 d0 00 64 	lwz     r14,100(r16)
    4464:	81 f0 00 74 	lwz     r15,116(r16)
    4468:	90 11 00 94 	stw     r0,148(r17)
    446c:	80 01 00 0c 	lwz     r0,12(r1)
    4470:	92 51 00 04 	stw     r18,4(r17)
    4474:	92 71 00 08 	stw     r19,8(r17)
    4478:	92 91 00 0c 	stw     r20,12(r17)
    447c:	92 b1 00 14 	stw     r21,20(r17)
    4480:	92 d1 00 18 	stw     r22,24(r17)
    4484:	92 f1 00 1c 	stw     r23,28(r17)
    4488:	93 11 00 24 	stw     r24,36(r17)
    448c:	93 31 00 28 	stw     r25,40(r17)
    4490:	93 51 00 2c 	stw     r26,44(r17)
    4494:	93 71 00 34 	stw     r27,52(r17)
    4498:	93 91 00 38 	stw     r28,56(r17)
    449c:	93 b1 00 3c 	stw     r29,60(r17)
    44a0:	93 d1 00 44 	stw     r30,68(r17)
    44a4:	93 f1 00 48 	stw     r31,72(r17)
    44a8:	91 91 00 4c 	stw     r12,76(r17)
    44ac:	91 71 00 54 	stw     r11,84(r17)
    44b0:	91 51 00 58 	stw     r10,88(r17)
    44b4:	91 31 00 5c 	stw     r9,92(r17)
    44b8:	91 11 00 64 	stw     r8,100(r17)
    44bc:	90 f1 00 68 	stw     r7,104(r17)
    44c0:	90 d1 00 6c 	stw     r6,108(r17)
    44c4:	90 b1 00 74 	stw     r5,116(r17)
    44c8:	90 91 00 78 	stw     r4,120(r17)
    44cc:	90 71 00 7c 	stw     r3,124(r17)
    44d0:	91 d1 00 88 	stw     r14,136(r17)
    44d4:	90 11 00 98 	stw     r0,152(r17)
    44d8:	91 f1 00 9c 	stw     r15,156(r17)
    44dc:	b9 c1 00 18 	lmw     r14,24(r1)
    44e0:	38 21 00 60 	addi    r1,r1,96
    44e4:	4e 80 00 20 	blr
