
build/GPOE8P/src/pso/object/TObjCMName.o:     file format elf32-powerpc


Disassembly of section .text:

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
    1180:	be c1 00 88 	stmw    r22,136(r1)
    1184:	7c 78 1b 78 	mr      r24,r3
    1188:	80 03 00 2c 	lwz     r0,44(r3)
    118c:	ab 23 00 40 	lha     r25,64(r3)
    1190:	54 03 50 2a 	slwi    r3,r0,10
    1194:	48 00 00 01 	bl      1194 <render__14TObjCMHairMenuFv+0x68>
			1194: R_PPC_REL24	sin_table_lookup
    1198:	c0 40 00 00 	lfs     f2,0(0)
			1198: R_PPC_EMB_SDA21	@409
    119c:	c0 00 00 00 	lfs     f0,0(0)
			119c: R_PPC_EMB_SDA21	@56
    11a0:	ef a2 00 7a 	fmadds  f29,f2,f1,f0
    11a4:	fc 1d 00 40 	fcmpo   cr0,f29,f0
    11a8:	40 81 00 08 	ble     11b0 <render__14TObjCMHairMenuFv+0x84>
    11ac:	ff a0 00 90 	fmr     f29,f0
    11b0:	80 78 00 28 	lwz     r3,40(r24)
    11b4:	34 03 ff ff 	addic.  r0,r3,-1
    11b8:	40 80 00 0c 	bge     11c4 <render__14TObjCMHairMenuFv+0x98>
    11bc:	38 00 00 00 	li      r0,0
    11c0:	48 00 00 10 	b       11d0 <render__14TObjCMHairMenuFv+0xa4>
    11c4:	2c 00 00 0a 	cmpwi   r0,10
    11c8:	41 80 00 08 	blt     11d0 <render__14TObjCMHairMenuFv+0xa4>
    11cc:	38 00 00 09 	li      r0,9
    11d0:	c0 58 00 34 	lfs     f2,52(r24)
    11d4:	3c 60 00 00 	lis     r3,0
			11d6: R_PPC_ADDR16_HA	lbl_8046509C
    11d8:	c0 20 00 00 	lfs     f1,0(0)
			11d8: R_PPC_EMB_SDA21	@85
    11dc:	54 00 10 3a 	slwi    r0,r0,2
    11e0:	38 63 00 00 	addi    r3,r3,0
			11e2: R_PPC_ADDR16_LO	lbl_8046509C
    11e4:	fc 02 08 40 	fcmpo   cr0,f2,f1
    11e8:	7f 83 04 2e 	lfsx    f28,r3,r0
    11ec:	4c 40 13 82 	cror    eq,lt,eq
    11f0:	41 82 01 08 	beq     12f8 <render__14TObjCMHairMenuFv+0x1cc>
    11f4:	c0 00 00 00 	lfs     f0,0(0)
			11f4: R_PPC_EMB_SDA21	@86
    11f8:	fc 02 00 40 	fcmpo   cr0,f2,f0
    11fc:	4c 41 13 82 	cror    eq,gt,eq
    1200:	40 82 00 0c 	bne     120c <render__14TObjCMHairMenuFv+0xe0>
    1204:	c3 60 00 00 	lfs     f27,0(0)
			1204: R_PPC_EMB_SDA21	@56
    1208:	48 00 00 0c 	b       1214 <render__14TObjCMHairMenuFv+0xe8>
    120c:	ec 02 08 28 	fsubs   f0,f2,f1
    1210:	ef 60 08 24 	fdivs   f27,f0,f1
    1214:	c3 c0 00 00 	lfs     f30,0(0)
			1214: R_PPC_EMB_SDA21	@118
    1218:	3a e0 00 00 	li      r23,0
    121c:	c3 e0 00 00 	lfs     f31,0(0)
			121c: R_PPC_EMB_SDA21	@56
    1220:	3a c0 00 00 	li      r22,0
    1224:	ec 1c f0 28 	fsubs   f0,f28,f30
    1228:	c0 20 00 00 	lfs     f1,0(0)
			1228: R_PPC_EMB_SDA21	@410
    122c:	d3 e1 00 2c 	stfs    f31,44(r1)
    1230:	c3 00 00 00 	lfs     f24,0(0)
			1230: R_PPC_EMB_SDA21	@91
    1234:	ef 5b f0 3a 	fmadds  f26,f27,f0,f30
    1238:	d0 21 00 34 	stfs    f1,52(r1)
    123c:	c3 20 00 00 	lfs     f25,0(0)
			123c: R_PPC_EMB_SDA21	@411
    1240:	2c 17 00 00 	cmpwi   r23,0
    1244:	3b 40 00 00 	li      r26,0
    1248:	40 82 00 0c 	bne     1254 <render__14TObjCMHairMenuFv+0x128>
    124c:	fe e0 d0 90 	fmr     f23,f26
    1250:	48 00 00 1c 	b       126c <render__14TObjCMHairMenuFv+0x140>
    1254:	3c 60 00 00 	lis     r3,0
			1256: R_PPC_ADDR16_HA	lbl_804650C4
    1258:	c0 20 00 00 	lfs     f1,0(0)
			1258: R_PPC_EMB_SDA21	@118
    125c:	38 63 00 00 	addi    r3,r3,0
			125e: R_PPC_ADDR16_LO	lbl_804650C4
    1260:	7c 03 b4 2e 	lfsx    f0,r3,r22
    1264:	ec 00 08 28 	fsubs   f0,f0,f1
    1268:	ee fb 08 3a 	fmadds  f23,f27,f0,f1
    126c:	d3 c1 00 30 	stfs    f30,48(r1)
    1270:	80 18 00 24 	lwz     r0,36(r24)
    1274:	7c 17 00 00 	cmpw    r23,r0
    1278:	40 82 00 24 	bne     129c <render__14TObjCMHairMenuFv+0x170>
    127c:	80 18 00 2c 	lwz     r0,44(r24)
    1280:	3b 40 00 02 	li      r26,2
    1284:	54 03 50 2a 	slwi    r3,r0,10
    1288:	48 00 00 01 	bl      1288 <render__14TObjCMHairMenuFv+0x15c>
			1288: R_PPC_REL24	sin_table_lookup
    128c:	c0 40 00 00 	lfs     f2,0(0)
			128c: R_PPC_EMB_SDA21	@90
    1290:	c0 01 00 30 	lfs     f0,48(r1)
    1294:	ec 02 00 7a 	fmadds  f0,f2,f1,f0
    1298:	d0 01 00 30 	stfs    f0,48(r1)
    129c:	c0 01 00 30 	lfs     f0,48(r1)
    12a0:	38 7a 00 06 	addi    r3,r26,6
    12a4:	c0 20 00 00 	lfs     f1,0(0)
			12a4: R_PPC_EMB_SDA21	@92
    12a8:	38 81 00 30 	addi    r4,r1,48
    12ac:	ec 17 00 28 	fsubs   f0,f23,f0
    12b0:	38 a1 00 28 	addi    r5,r1,40
    12b4:	ec 00 c0 24 	fdivs   f0,f0,f24
    12b8:	d0 01 00 28 	stfs    f0,40(r1)
    12bc:	48 00 00 01 	bl      12bc <render__14TObjCMHairMenuFv+0x190>
			12bc: R_PPC_REL24	draw_ui_sprite_opaque
    12c0:	d2 e1 00 30 	stfs    f23,48(r1)
    12c4:	38 7a 00 07 	addi    r3,r26,7
    12c8:	c0 20 00 00 	lfs     f1,0(0)
			12c8: R_PPC_EMB_SDA21	@92
    12cc:	38 81 00 30 	addi    r4,r1,48
    12d0:	d3 e1 00 28 	stfs    f31,40(r1)
    12d4:	38 a1 00 28 	addi    r5,r1,40
    12d8:	48 00 00 01 	bl      12d8 <render__14TObjCMHairMenuFv+0x1ac>
			12d8: R_PPC_REL24	draw_ui_sprite_opaque
    12dc:	c0 01 00 34 	lfs     f0,52(r1)
    12e0:	3a f7 00 01 	addi    r23,r23,1
    12e4:	2c 17 00 04 	cmpwi   r23,4
    12e8:	3a d6 00 04 	addi    r22,r22,4
    12ec:	ec 00 c8 2a 	fadds   f0,f0,f25
    12f0:	d0 01 00 34 	stfs    f0,52(r1)
    12f4:	41 80 ff 4c 	blt     1240 <render__14TObjCMHairMenuFv+0x114>
    12f8:	c0 38 00 34 	lfs     f1,52(r24)
    12fc:	c0 00 00 00 	lfs     f0,0(0)
			12fc: R_PPC_EMB_SDA21	@54
    1300:	fc 01 00 40 	fcmpo   cr0,f1,f0
    1304:	4c 40 13 82 	cror    eq,lt,eq
    1308:	41 82 00 78 	beq     1380 <render__14TObjCMHairMenuFv+0x254>
    130c:	c0 00 00 00 	lfs     f0,0(0)
			130c: R_PPC_EMB_SDA21	@86
    1310:	fc 01 00 40 	fcmpo   cr0,f1,f0
    1314:	4c 41 13 82 	cror    eq,gt,eq
    1318:	40 82 00 0c 	bne     1324 <render__14TObjCMHairMenuFv+0x1f8>
    131c:	c2 e0 00 00 	lfs     f23,0(0)
			131c: R_PPC_EMB_SDA21	@56
    1320:	48 00 00 08 	b       1328 <render__14TObjCMHairMenuFv+0x1fc>
    1324:	ee e1 00 24 	fdivs   f23,f1,f0
    1328:	c0 20 00 00 	lfs     f1,0(0)
			1328: R_PPC_EMB_SDA21	@412
    132c:	3a c0 00 00 	li      r22,0
    1330:	c0 00 00 00 	lfs     f0,0(0)
			1330: R_PPC_EMB_SDA21	@410
    1334:	d0 21 00 20 	stfs    f1,32(r1)
    1338:	c3 40 00 00 	lfs     f26,0(0)
			1338: R_PPC_EMB_SDA21	@411
    133c:	d0 01 00 24 	stfs    f0,36(r1)
    1340:	80 18 00 24 	lwz     r0,36(r24)
    1344:	38 60 00 00 	li      r3,0
    1348:	7c 16 00 00 	cmpw    r22,r0
    134c:	40 82 00 08 	bne     1354 <render__14TObjCMHairMenuFv+0x228>
    1350:	38 60 ff ff 	li      r3,-1
    1354:	fc 40 b8 90 	fmr     f2,f23
    1358:	c0 20 00 00 	lfs     f1,0(0)
			1358: R_PPC_EMB_SDA21	@93
    135c:	38 63 00 01 	addi    r3,r3,1
    1360:	38 81 00 20 	addi    r4,r1,32
    1364:	48 00 00 01 	bl      1364 <render__14TObjCMHairMenuFv+0x238>
			1364: R_PPC_REL24	draw_ui_sprite
    1368:	c0 01 00 24 	lfs     f0,36(r1)
    136c:	3a d6 00 01 	addi    r22,r22,1
    1370:	2c 16 00 04 	cmpwi   r22,4
    1374:	ec 00 d0 2a 	fadds   f0,f0,f26
    1378:	d0 01 00 24 	stfs    f0,36(r1)
    137c:	41 80 ff c4 	blt     1340 <render__14TObjCMHairMenuFv+0x214>
    1380:	c0 38 00 34 	lfs     f1,52(r24)
    1384:	c0 00 00 00 	lfs     f0,0(0)
			1384: R_PPC_EMB_SDA21	@86
    1388:	fc 01 00 40 	fcmpo   cr0,f1,f0
    138c:	4c 40 13 82 	cror    eq,lt,eq
    1390:	41 82 04 84 	beq     1814 <render__14TObjCMHairMenuFv+0x6e8>
    1394:	ec 61 00 28 	fsubs   f3,f1,f0
    1398:	c0 00 00 00 	lfs     f0,0(0)
			1398: R_PPC_EMB_SDA21	@413
    139c:	c0 40 00 00 	lfs     f2,0(0)
			139c: R_PPC_EMB_SDA21	@414
    13a0:	3a c0 00 00 	li      r22,0
    13a4:	c0 20 00 00 	lfs     f1,0(0)
			13a4: R_PPC_EMB_SDA21	@122
    13a8:	ef c3 00 24 	fdivs   f30,f3,f0
    13ac:	c0 00 00 00 	lfs     f0,0(0)
			13ac: R_PPC_EMB_SDA21	@415
    13b0:	d0 41 00 18 	stfs    f2,24(r1)
    13b4:	c3 60 00 00 	lfs     f27,0(0)
			13b4: R_PPC_EMB_SDA21	@417
    13b8:	d0 21 00 1c 	stfs    f1,28(r1)
    13bc:	ef 5e 07 b2 	fmuls   f26,f30,f30
    13c0:	ef 00 06 b2 	fmuls   f24,f0,f26
    13c4:	48 00 00 88 	b       144c <render__14TObjCMHairMenuFv+0x320>
    13c8:	80 18 00 24 	lwz     r0,36(r24)
    13cc:	fe e0 d0 90 	fmr     f23,f26
    13d0:	2c 00 00 00 	cmpwi   r0,0
    13d4:	41 82 00 08 	beq     13dc <render__14TObjCMHairMenuFv+0x2b0>
    13d8:	fe e0 c0 90 	fmr     f23,f24
    13dc:	7c 16 c8 00 	cmpw    r22,r25
    13e0:	3a e0 00 1f 	li      r23,31
    13e4:	40 82 00 44 	bne     1428 <render__14TObjCMHairMenuFv+0x2fc>
    13e8:	80 00 00 00 	lwz     r0,0(0)
			13e8: R_PPC_EMB_SDA21	creation_resource_ready_state
    13ec:	3a e0 00 20 	li      r23,32
    13f0:	2c 00 00 02 	cmpwi   r0,2
    13f4:	41 82 00 24 	beq     1418 <render__14TObjCMHairMenuFv+0x2ec>
    13f8:	80 18 00 2c 	lwz     r0,44(r24)
    13fc:	54 03 60 26 	slwi    r3,r0,12
    1400:	48 00 00 01 	bl      1400 <render__14TObjCMHairMenuFv+0x2d4>
			1400: R_PPC_REL24	sin_table_lookup
    1404:	48 00 00 01 	bl      1404 <render__14TObjCMHairMenuFv+0x2d8>
			1404: R_PPC_REL24	fabs_float
    1408:	c0 00 00 00 	lfs     f0,0(0)
			1408: R_PPC_EMB_SDA21	@416
    140c:	ec 00 00 7a 	fmadds  f0,f0,f1,f0
    1410:	ee f7 00 32 	fmuls   f23,f23,f0
    1414:	48 00 00 14 	b       1428 <render__14TObjCMHairMenuFv+0x2fc>
    1418:	80 18 00 24 	lwz     r0,36(r24)
    141c:	2c 00 00 00 	cmpwi   r0,0
    1420:	40 82 00 08 	bne     1428 <render__14TObjCMHairMenuFv+0x2fc>
    1424:	ee f7 07 72 	fmuls   f23,f23,f29
    1428:	fc 40 b8 90 	fmr     f2,f23
    142c:	c0 20 00 00 	lfs     f1,0(0)
			142c: R_PPC_EMB_SDA21	@93
    1430:	7e e3 bb 78 	mr      r3,r23
    1434:	38 81 00 18 	addi    r4,r1,24
    1438:	48 00 00 01 	bl      1438 <render__14TObjCMHairMenuFv+0x30c>
			1438: R_PPC_REL24	draw_ui_sprite
    143c:	c0 01 00 18 	lfs     f0,24(r1)
    1440:	3a d6 00 01 	addi    r22,r22,1
    1444:	ec 00 d8 2a 	fadds   f0,f0,f27
    1448:	d0 01 00 18 	stfs    f0,24(r1)
    144c:	80 18 00 28 	lwz     r0,40(r24)
    1450:	7c 16 00 00 	cmpw    r22,r0
    1454:	41 80 ff 74 	blt     13c8 <render__14TObjCMHairMenuFv+0x29c>
    1458:	c0 00 00 00 	lfs     f0,0(0)
			1458: R_PPC_EMB_SDA21	@418
    145c:	fe e0 d0 90 	fmr     f23,f26
    1460:	80 18 00 24 	lwz     r0,36(r24)
    1464:	ef 1c 00 28 	fsubs   f24,f28,f0
    1468:	2c 00 00 00 	cmpwi   r0,0
    146c:	40 82 00 0c 	bne     1478 <render__14TObjCMHairMenuFv+0x34c>
    1470:	ec 5a 07 72 	fmuls   f2,f26,f29
    1474:	48 00 00 10 	b       1484 <render__14TObjCMHairMenuFv+0x358>
    1478:	c0 00 00 00 	lfs     f0,0(0)
			1478: R_PPC_EMB_SDA21	@415
    147c:	ec 40 06 b2 	fmuls   f2,f0,f26
    1480:	fe e0 10 90 	fmr     f23,f2
    1484:	c0 20 00 00 	lfs     f1,0(0)
			1484: R_PPC_EMB_SDA21	@419
    1488:	38 79 00 14 	addi    r3,r25,20
    148c:	c0 00 00 00 	lfs     f0,0(0)
			148c: R_PPC_EMB_SDA21	@420
    1490:	38 81 00 10 	addi    r4,r1,16
    1494:	ec 61 c0 2a 	fadds   f3,f1,f24
    1498:	c0 20 00 00 	lfs     f1,0(0)
			1498: R_PPC_EMB_SDA21	@93
    149c:	d0 01 00 14 	stfs    f0,20(r1)
    14a0:	d0 61 00 10 	stfs    f3,16(r1)
    14a4:	48 00 00 01 	bl      14a4 <render__14TObjCMHairMenuFv+0x378>
			14a4: R_PPC_REL24	draw_ui_sprite
    14a8:	c0 20 00 00 	lfs     f1,0(0)
			14a8: R_PPC_EMB_SDA21	@421
    14ac:	fc 40 b8 90 	fmr     f2,f23
    14b0:	c0 00 00 00 	lfs     f0,0(0)
			14b0: R_PPC_EMB_SDA21	@122
    14b4:	38 81 00 10 	addi    r4,r1,16
    14b8:	ec 61 c0 2a 	fadds   f3,f1,f24
    14bc:	c0 20 00 00 	lfs     f1,0(0)
			14bc: R_PPC_EMB_SDA21	@93
    14c0:	d0 01 00 14 	stfs    f0,20(r1)
    14c4:	38 60 00 1e 	li      r3,30
    14c8:	d0 61 00 10 	stfs    f3,16(r1)
    14cc:	48 00 00 01 	bl      14cc <render__14TObjCMHairMenuFv+0x3a0>
			14cc: R_PPC_REL24	draw_ui_sprite
    14d0:	c0 20 00 00 	lfs     f1,0(0)
			14d0: R_PPC_EMB_SDA21	@422
    14d4:	fc 40 b8 90 	fmr     f2,f23
    14d8:	c0 00 00 00 	lfs     f0,0(0)
			14d8: R_PPC_EMB_SDA21	@423
    14dc:	38 81 00 10 	addi    r4,r1,16
    14e0:	ec 61 c0 2a 	fadds   f3,f1,f24
    14e4:	c0 20 00 00 	lfs     f1,0(0)
			14e4: R_PPC_EMB_SDA21	@93
    14e8:	d0 01 00 14 	stfs    f0,20(r1)
    14ec:	d0 61 00 10 	stfs    f3,16(r1)
    14f0:	80 78 00 28 	lwz     r3,40(r24)
    14f4:	38 63 00 13 	addi    r3,r3,19
    14f8:	48 00 00 01 	bl      14f8 <render__14TObjCMHairMenuFv+0x3cc>
			14f8: R_PPC_REL24	draw_ui_sprite
    14fc:	c0 00 00 00 	lfs     f0,0(0)
			14fc: R_PPC_EMB_SDA21	@415
    1500:	3c 60 00 00 	lis     r3,0
			1502: R_PPC_ADDR16_HA	lbl_804DBCD0
    1504:	ef 1a 07 72 	fmuls   f24,f26,f29
    1508:	3a c3 00 00 	addi    r22,r3,0
			150a: R_PPC_ADDR16_LO	lbl_804DBCD0
    150c:	ef 20 06 b2 	fmuls   f25,f0,f26
    1510:	3a e0 00 01 	li      r23,1
    1514:	80 18 00 24 	lwz     r0,36(r24)
    1518:	38 77 ff ff 	addi    r3,r23,-1
    151c:	54 64 18 38 	slwi    r4,r3,3
    1520:	c0 20 00 00 	lfs     f1,0(0)
			1520: R_PPC_EMB_SDA21	@93
    1524:	7c 17 00 00 	cmpw    r23,r0
    1528:	38 77 00 0f 	addi    r3,r23,15
    152c:	7c 96 22 14 	add     r4,r22,r4
    1530:	40 82 00 0c 	bne     153c <render__14TObjCMHairMenuFv+0x410>
    1534:	fc 40 c0 90 	fmr     f2,f24
    1538:	48 00 00 08 	b       1540 <render__14TObjCMHairMenuFv+0x414>
    153c:	fc 40 c8 90 	fmr     f2,f25
    1540:	48 00 00 01 	bl      1540 <render__14TObjCMHairMenuFv+0x414>
			1540: R_PPC_REL24	draw_ui_sprite
    1544:	3a f7 00 01 	addi    r23,r23,1
    1548:	2c 17 00 04 	cmpwi   r23,4
    154c:	41 80 ff c8 	blt     1514 <render__14TObjCMHairMenuFv+0x3e8>
    1550:	48 00 00 01 	bl      1550 <render__14TObjCMHairMenuFv+0x424>
			1550: R_PPC_REL24	restore_full_screen_view__11TCameraCtrlFv
    1554:	48 00 00 01 	bl      1554 <render__14TObjCMHairMenuFv+0x428>
			1554: R_PPC_REL24	get_scale__14TObjCMMainMenuFv
    1558:	3c 60 00 00 	lis     r3,0
			155a: R_PPC_ADDR16_HA	lbl_804650D4
    155c:	c0 40 00 00 	lfs     f2,0(0)
			155c: R_PPC_EMB_SDA21	@424
    1560:	38 63 00 00 	addi    r3,r3,0
			1562: R_PPC_ADDR16_LO	lbl_804650D4
    1564:	3c 80 00 00 	lis     r4,0
			1566: R_PPC_ADDR16_HA	lbl_804650F4
    1568:	ef 62 07 b2 	fmuls   f27,f2,f30
    156c:	c0 03 00 0c 	lfs     f0,12(r3)
    1570:	c0 43 00 04 	lfs     f2,4(r3)
    1574:	38 84 00 00 	addi    r4,r4,0
			1576: R_PPC_ADDR16_LO	lbl_804650F4
    1578:	80 84 00 0c 	lwz     r4,12(r4)
    157c:	38 e1 00 58 	addi    r7,r1,88
    1580:	ec 60 10 28 	fsubs   f3,f0,f2
    1584:	c1 00 00 00 	lfs     f8,0(0)
			1584: R_PPC_EMB_SDA21	@425
    1588:	c0 e0 00 00 	lfs     f7,0(0)
			1588: R_PPC_EMB_SDA21	@426
    158c:	fc 00 d8 1e 	fctiwz  f0,f27
    1590:	c0 83 00 00 	lfs     f4,0(r3)
    1594:	ff c0 08 90 	fmr     f30,f1
    1598:	ec a8 10 fa 	fmadds  f5,f8,f3,f2
    159c:	c0 c3 00 18 	lfs     f6,24(r3)
    15a0:	ed 27 10 fa 	fmadds  f9,f7,f3,f2
    15a4:	c0 63 00 08 	lfs     f3,8(r3)
    15a8:	c0 40 00 00 	lfs     f2,0(0)
			15a8: R_PPC_EMB_SDA21	@411
    15ac:	38 c1 00 48 	addi    r6,r1,72
    15b0:	d8 01 00 78 	stfd    f0,120(r1)
    15b4:	ed 43 20 28 	fsubs   f10,f3,f4
    15b8:	c0 63 00 10 	lfs     f3,16(r3)
    15bc:	ef 42 07 b2 	fmuls   f26,f2,f30
    15c0:	90 81 00 08 	stw     r4,8(r1)
    15c4:	38 a0 00 00 	li      r5,0
    15c8:	ec 43 30 28 	fsubs   f2,f3,f6
    15cc:	80 01 00 7c 	lwz     r0,124(r1)
    15d0:	ec 25 07 b2 	fmuls   f1,f5,f30
    15d4:	d0 a1 00 74 	stfs    f5,116(r1)
    15d8:	ec 09 07 b2 	fmuls   f0,f9,f30
    15dc:	ec 67 30 ba 	fmadds  f3,f7,f2,f6
    15e0:	d0 a1 00 5c 	stfs    f5,92(r1)
    15e4:	ec a8 22 ba 	fmadds  f5,f8,f10,f4
    15e8:	ec 87 22 ba 	fmadds  f4,f7,f10,f4
    15ec:	38 61 00 54 	addi    r3,r1,84
    15f0:	ec 48 30 ba 	fmadds  f2,f8,f2,f6
    15f4:	d1 21 00 6c 	stfs    f9,108(r1)
    15f8:	38 81 00 08 	addi    r4,r1,8
    15fc:	d1 21 00 64 	stfs    f9,100(r1)
    1600:	d0 a1 00 58 	stfs    f5,88(r1)
    1604:	d0 81 00 60 	stfs    f4,96(r1)
    1608:	d0 61 00 68 	stfs    f3,104(r1)
    160c:	d0 41 00 70 	stfs    f2,112(r1)
    1610:	d0 21 00 5c 	stfs    f1,92(r1)
    1614:	d0 01 00 64 	stfs    f0,100(r1)
    1618:	d0 01 00 6c 	stfs    f0,108(r1)
    161c:	d0 21 00 74 	stfs    f1,116(r1)
    1620:	90 e1 00 38 	stw     r7,56(r1)
    1624:	90 c1 00 3c 	stw     r6,60(r1)
    1628:	90 a1 00 40 	stw     r5,64(r1)
    162c:	98 01 00 0b 	stb     r0,11(r1)
    1630:	48 00 00 01 	bl      1630 <render__14TObjCMHairMenuFv+0x504>
			1630: R_PPC_REL24	TObjCMHairMenu__sub_801E3F54
    1634:	7c 64 1b 78 	mr      r4,r3
    1638:	38 61 00 50 	addi    r3,r1,80
    163c:	48 00 00 01 	bl      163c <render__14TObjCMHairMenuFv+0x510>
			163c: R_PPC_REL24	TObjCMHairMenu__sub_801E3F54
    1640:	7c 64 1b 78 	mr      r4,r3
    1644:	38 61 00 4c 	addi    r3,r1,76
    1648:	48 00 00 01 	bl      1648 <render__14TObjCMHairMenuFv+0x51c>
			1648: R_PPC_REL24	TObjCMHairMenu__sub_801E3F54
    164c:	7c 64 1b 78 	mr      r4,r3
    1650:	38 61 00 48 	addi    r3,r1,72
    1654:	48 00 00 01 	bl      1654 <render__14TObjCMHairMenuFv+0x528>
			1654: R_PPC_REL24	TObjCMHairMenu__sub_801E3F54
    1658:	3a c0 00 00 	li      r22,0
    165c:	c0 20 00 00 	lfs     f1,0(0)
			165c: R_PPC_EMB_SDA21	@93
    1660:	38 61 00 38 	addi    r3,r1,56
    1664:	38 80 00 04 	li      r4,4
    1668:	38 a0 00 06 	li      r5,6
    166c:	48 00 00 01 	bl      166c <render__14TObjCMHairMenuFv+0x540>
			166c: R_PPC_REL24	draw_tri_fan_2d__14TObjCMHairMenuFllf
    1670:	c0 01 00 5c 	lfs     f0,92(r1)
    1674:	3a d6 00 01 	addi    r22,r22,1
    1678:	c0 41 00 64 	lfs     f2,100(r1)
    167c:	2c 16 00 03 	cmpwi   r22,3
    1680:	ec 60 d0 2a 	fadds   f3,f0,f26
    1684:	c0 21 00 6c 	lfs     f1,108(r1)
    1688:	c0 01 00 74 	lfs     f0,116(r1)
    168c:	ec 42 d0 2a 	fadds   f2,f2,f26
    1690:	ec 21 d0 2a 	fadds   f1,f1,f26
    1694:	ec 00 d0 2a 	fadds   f0,f0,f26
    1698:	d0 61 00 5c 	stfs    f3,92(r1)
    169c:	d0 41 00 64 	stfs    f2,100(r1)
    16a0:	d0 21 00 6c 	stfs    f1,108(r1)
    16a4:	d0 01 00 74 	stfs    f0,116(r1)
    16a8:	41 80 ff b4 	blt     165c <render__14TObjCMHairMenuFv+0x530>
    16ac:	fc 00 d8 1e 	fctiwz  f0,f27
    16b0:	3c 60 00 00 	lis     r3,0
			16b2: R_PPC_ADDR16_HA	@268
    16b4:	3c 80 00 00 	lis     r4,0
			16b6: R_PPC_ADDR16_HA	lbl_804650D4
    16b8:	cb e3 00 00 	lfd     f31,0(r3)
			16ba: R_PPC_ADDR16_LO	@268
    16bc:	c3 80 00 00 	lfs     f28,0(0)
			16bc: R_PPC_EMB_SDA21	@424
    16c0:	3b c4 00 00 	addi    r30,r4,0
			16c2: R_PPC_ADDR16_LO	lbl_804650D4
    16c4:	d8 01 00 78 	stfd    f0,120(r1)
    16c8:	3b 81 00 54 	addi    r28,r1,84
    16cc:	c3 60 00 00 	lfs     f27,0(0)
			16cc: R_PPC_EMB_SDA21	@54
    16d0:	3b 61 00 50 	addi    r27,r1,80
    16d4:	83 a1 00 7c 	lwz     r29,124(r1)
    16d8:	3b 41 00 4c 	addi    r26,r1,76
    16dc:	3b 20 00 00 	li      r25,0
    16e0:	3a e0 00 00 	li      r23,0
    16e4:	3a c0 00 00 	li      r22,0
    16e8:	3f e0 43 30 	lis     r31,17200
    16ec:	80 78 00 1c 	lwz     r3,28(r24)
    16f0:	38 16 00 42 	addi    r0,r22,66
    16f4:	93 e1 00 78 	stw     r31,120(r1)
    16f8:	7c 03 02 ae 	lhax    r0,r3,r0
    16fc:	6c 00 80 00 	xoris   r0,r0,32768
    1700:	90 01 00 7c 	stw     r0,124(r1)
    1704:	c8 01 00 78 	lfd     f0,120(r1)
    1708:	ec 00 f8 28 	fsubs   f0,f0,f31
    170c:	ec c0 e0 24 	fdivs   f6,f0,f28
    1710:	fc 1b 30 00 	fcmpu   cr0,f27,f6
    1714:	41 82 00 e8 	beq     17fc <render__14TObjCMHairMenuFv+0x6d0>
    1718:	3c 60 00 00 	lis     r3,0
			171a: R_PPC_ADDR16_HA	lbl_804650D4
    171c:	6f 25 80 00 	xoris   r5,r25,32768
    1720:	38 e3 00 00 	addi    r7,r3,0
			1722: R_PPC_ADDR16_LO	lbl_804650D4
    1724:	3c 80 00 00 	lis     r4,0
			1726: R_PPC_ADDR16_HA	@268
    1728:	3c 60 43 30 	lis     r3,17200
    172c:	c0 a7 00 00 	lfs     f5,0(r7)
    1730:	c0 9e 00 08 	lfs     f4,8(r30)
    1734:	38 c4 00 00 	addi    r6,r4,0
			1736: R_PPC_ADDR16_LO	@268
    1738:	c0 3e 00 10 	lfs     f1,16(r30)
    173c:	38 00 00 04 	li      r0,4
    1740:	c0 1e 00 18 	lfs     f0,24(r30)
    1744:	38 81 00 58 	addi    r4,r1,88
    1748:	ec 61 20 28 	fsubs   f3,f1,f4
    174c:	90 61 00 78 	stw     r3,120(r1)
    1750:	ec 40 28 28 	fsubs   f2,f0,f5
    1754:	c8 26 00 00 	lfd     f1,0(r6)
    1758:	90 a1 00 7c 	stw     r5,124(r1)
    175c:	38 60 00 00 	li      r3,0
    1760:	c8 01 00 78 	lfd     f0,120(r1)
    1764:	ec 66 20 fa 	fmadds  f3,f6,f3,f4
    1768:	ec 46 28 ba 	fmadds  f2,f6,f2,f5
    176c:	d0 a1 00 58 	stfs    f5,88(r1)
    1770:	ec 00 08 28 	fsubs   f0,f0,f1
    1774:	d0 81 00 60 	stfs    f4,96(r1)
    1778:	ec 20 06 b2 	fmuls   f1,f0,f26
    177c:	d0 61 00 68 	stfs    f3,104(r1)
    1780:	d0 41 00 70 	stfs    f2,112(r1)
    1784:	7c 09 03 a6 	mtctr   r0
    1788:	7c a7 1a 14 	add     r5,r7,r3
    178c:	38 03 00 04 	addi    r0,r3,4
    1790:	c0 05 00 04 	lfs     f0,4(r5)
    1794:	38 63 00 08 	addi    r3,r3,8
    1798:	ec 1e 08 3a 	fmadds  f0,f30,f0,f1
    179c:	7c 04 05 2e 	stfsx   f0,r4,r0
    17a0:	42 00 ff e8 	bdnz    1788 <render__14TObjCMHairMenuFv+0x65c>
    17a4:	3c 80 00 00 	lis     r4,0
			17a6: R_PPC_ADDR16_HA	lbl_804650F4
    17a8:	7f 83 e3 78 	mr      r3,r28
    17ac:	38 84 00 00 	addi    r4,r4,0
			17ae: R_PPC_ADDR16_LO	lbl_804650F4
    17b0:	7c 04 b8 2e 	lwzx    r0,r4,r23
    17b4:	38 81 00 0c 	addi    r4,r1,12
    17b8:	90 01 00 0c 	stw     r0,12(r1)
    17bc:	9b a1 00 0f 	stb     r29,15(r1)
    17c0:	48 00 00 01 	bl      17c0 <render__14TObjCMHairMenuFv+0x694>
			17c0: R_PPC_REL24	TObjCMHairMenu__sub_801E3F54
    17c4:	7c 64 1b 78 	mr      r4,r3
    17c8:	7f 63 db 78 	mr      r3,r27
    17cc:	48 00 00 01 	bl      17cc <render__14TObjCMHairMenuFv+0x6a0>
			17cc: R_PPC_REL24	TObjCMHairMenu__sub_801E3F54
    17d0:	7c 64 1b 78 	mr      r4,r3
    17d4:	7f 43 d3 78 	mr      r3,r26
    17d8:	48 00 00 01 	bl      17d8 <render__14TObjCMHairMenuFv+0x6ac>
			17d8: R_PPC_REL24	TObjCMHairMenu__sub_801E3F54
    17dc:	7c 64 1b 78 	mr      r4,r3
    17e0:	38 61 00 48 	addi    r3,r1,72
    17e4:	48 00 00 01 	bl      17e4 <render__14TObjCMHairMenuFv+0x6b8>
			17e4: R_PPC_REL24	TObjCMHairMenu__sub_801E3F54
    17e8:	c0 20 00 00 	lfs     f1,0(0)
			17e8: R_PPC_EMB_SDA21	@93
    17ec:	38 61 00 38 	addi    r3,r1,56
    17f0:	38 80 00 04 	li      r4,4
    17f4:	38 a0 00 06 	li      r5,6
    17f8:	48 00 00 01 	bl      17f8 <render__14TObjCMHairMenuFv+0x6cc>
			17f8: R_PPC_REL24	draw_tri_fan_2d__14TObjCMHairMenuFllf
    17fc:	3b 39 00 01 	addi    r25,r25,1
    1800:	3a d6 00 02 	addi    r22,r22,2
    1804:	2c 19 00 03 	cmpwi   r25,3
    1808:	3a f7 00 04 	addi    r23,r23,4
    180c:	41 80 fe e0 	blt     16ec <render__14TObjCMHairMenuFv+0x5c0>
    1810:	48 00 00 01 	bl      1810 <render__14TObjCMHairMenuFv+0x6e4>
			1810: R_PPC_REL24	TCameraCtrl__sub_80068EF0
    1814:	e3 e1 01 38 	psq_l   f31,312(r1),0,0
    1818:	cb e1 01 30 	lfd     f31,304(r1)
    181c:	e3 c1 01 28 	lq      r30,288(r1)
    1820:	cb c1 01 20 	lfd     f30,288(r1)
    1824:	e3 a1 01 18 	psq_l   f29,280(r1),0,0
    1828:	cb a1 01 10 	lfd     f29,272(r1)
    182c:	e3 81 01 08 	lq      r28,256(r1)
    1830:	cb 81 01 00 	lfd     f28,256(r1)
    1834:	e3 61 00 f8 	psq_l   f27,248(r1),0,0
    1838:	cb 61 00 f0 	lfd     f27,240(r1)
    183c:	e3 41 00 e8 	lq      r26,224(r1)
    1840:	cb 41 00 e0 	lfd     f26,224(r1)
    1844:	e3 21 00 d8 	psq_l   f25,216(r1),0,0
    1848:	cb 21 00 d0 	lfd     f25,208(r1)
    184c:	e3 01 00 c8 	lq      r24,192(r1)
    1850:	cb 01 00 c0 	lfd     f24,192(r1)
    1854:	e2 e1 00 b8 	psq_l   f23,184(r1),0,0
    1858:	ca e1 00 b0 	lfd     f23,176(r1)
    185c:	ba c1 00 88 	lmw     r22,136(r1)
    1860:	80 01 01 44 	lwz     r0,324(r1)
    1864:	7c 08 03 a6 	mtlr    r0
    1868:	38 21 01 40 	addi    r1,r1,320
    186c:	4e 80 00 20 	blr
