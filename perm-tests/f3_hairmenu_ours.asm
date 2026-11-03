
/Users/scott/Hermes/pso-decomp/pso-decomp-f3/build/GPOE8P/src/pso/object/TObjCMName.o:     file format elf32-powerpc


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
    1188:	80 63 00 1c 	lwz     r3,28(r3)
    118c:	80 18 00 2c 	lwz     r0,44(r24)
    1190:	ab 23 00 40 	lha     r25,64(r3)
    1194:	54 03 50 2a 	slwi    r3,r0,10
    1198:	48 00 00 01 	bl      1198 <render__14TObjCMHairMenuFv+0x6c>
    119c:	c0 40 00 00 	lfs     f2,0(0)
    11a0:	c0 00 00 00 	lfs     f0,0(0)
    11a4:	ef a2 00 7a 	fmadds  f29,f2,f1,f0
    11a8:	fc 1d 00 40 	fcmpo   cr0,f29,f0
    11ac:	40 81 00 08 	ble     11b4 <render__14TObjCMHairMenuFv+0x88>
    11b0:	ff a0 00 90 	fmr     f29,f0
    11b4:	80 78 00 28 	lwz     r3,40(r24)
    11b8:	34 03 ff ff 	addic.  r0,r3,-1
    11bc:	40 80 00 0c 	bge     11c8 <render__14TObjCMHairMenuFv+0x9c>
    11c0:	38 00 00 00 	li      r0,0
    11c4:	48 00 00 10 	b       11d4 <render__14TObjCMHairMenuFv+0xa8>
    11c8:	2c 00 00 0a 	cmpwi   r0,10
    11cc:	41 80 00 08 	blt     11d4 <render__14TObjCMHairMenuFv+0xa8>
    11d0:	38 00 00 09 	li      r0,9
    11d4:	c0 58 00 34 	lfs     f2,52(r24)
    11d8:	3c 60 00 00 	lis     r3,0
    11dc:	c0 20 00 00 	lfs     f1,0(0)
    11e0:	54 00 10 3a 	slwi    r0,r0,2
    11e4:	38 63 00 00 	addi    r3,r3,0
    11e8:	fc 02 08 40 	fcmpo   cr0,f2,f1
    11ec:	7f 83 04 2e 	lfsx    f28,r3,r0
    11f0:	4c 40 13 82 	cror    eq,lt,eq
    11f4:	41 82 01 08 	beq     12fc <render__14TObjCMHairMenuFv+0x1d0>
    11f8:	c0 00 00 00 	lfs     f0,0(0)
    11fc:	fc 02 00 40 	fcmpo   cr0,f2,f0
    1200:	4c 41 13 82 	cror    eq,gt,eq
    1204:	40 82 00 0c 	bne     1210 <render__14TObjCMHairMenuFv+0xe4>
    1208:	c3 60 00 00 	lfs     f27,0(0)
    120c:	48 00 00 0c 	b       1218 <render__14TObjCMHairMenuFv+0xec>
    1210:	ec 02 08 28 	fsubs   f0,f2,f1
    1214:	ef 60 08 24 	fdivs   f27,f0,f1
    1218:	c3 c0 00 00 	lfs     f30,0(0)
    121c:	3a e0 00 00 	li      r23,0
    1220:	c3 e0 00 00 	lfs     f31,0(0)
    1224:	3a c0 00 00 	li      r22,0
    1228:	ec 1c f0 28 	fsubs   f0,f28,f30
    122c:	c0 20 00 00 	lfs     f1,0(0)
    1230:	d3 e1 00 2c 	stfs    f31,44(r1)
    1234:	c3 00 00 00 	lfs     f24,0(0)
    1238:	ef 5b f0 3a 	fmadds  f26,f27,f0,f30
    123c:	d0 21 00 34 	stfs    f1,52(r1)
    1240:	c3 20 00 00 	lfs     f25,0(0)
    1244:	2c 17 00 00 	cmpwi   r23,0
    1248:	3b 40 00 00 	li      r26,0
    124c:	40 82 00 0c 	bne     1258 <render__14TObjCMHairMenuFv+0x12c>
    1250:	fe e0 d0 90 	fmr     f23,f26
    1254:	48 00 00 1c 	b       1270 <render__14TObjCMHairMenuFv+0x144>
    1258:	3c 60 00 00 	lis     r3,0
    125c:	c0 20 00 00 	lfs     f1,0(0)
    1260:	38 63 00 00 	addi    r3,r3,0
    1264:	7c 03 b4 2e 	lfsx    f0,r3,r22
    1268:	ec 00 08 28 	fsubs   f0,f0,f1
    126c:	ee fb 08 3a 	fmadds  f23,f27,f0,f1
    1270:	d3 c1 00 30 	stfs    f30,48(r1)
    1274:	80 18 00 24 	lwz     r0,36(r24)
    1278:	7c 17 00 00 	cmpw    r23,r0
    127c:	40 82 00 24 	bne     12a0 <render__14TObjCMHairMenuFv+0x174>
    1280:	80 18 00 2c 	lwz     r0,44(r24)
    1284:	3b 40 00 02 	li      r26,2
    1288:	54 03 50 2a 	slwi    r3,r0,10
    128c:	48 00 00 01 	bl      128c <render__14TObjCMHairMenuFv+0x160>
    1290:	c0 40 00 00 	lfs     f2,0(0)
    1294:	c0 01 00 30 	lfs     f0,48(r1)
    1298:	ec 02 00 7a 	fmadds  f0,f2,f1,f0
    129c:	d0 01 00 30 	stfs    f0,48(r1)
    12a0:	c0 01 00 30 	lfs     f0,48(r1)
    12a4:	38 7a 00 06 	addi    r3,r26,6
    12a8:	c0 20 00 00 	lfs     f1,0(0)
    12ac:	38 81 00 30 	addi    r4,r1,48
    12b0:	ec 17 00 28 	fsubs   f0,f23,f0
    12b4:	38 a1 00 28 	addi    r5,r1,40
    12b8:	ec 00 c0 24 	fdivs   f0,f0,f24
    12bc:	d0 01 00 28 	stfs    f0,40(r1)
    12c0:	48 00 00 01 	bl      12c0 <render__14TObjCMHairMenuFv+0x194>
    12c4:	d2 e1 00 30 	stfs    f23,48(r1)
    12c8:	38 7a 00 07 	addi    r3,r26,7
    12cc:	c0 20 00 00 	lfs     f1,0(0)
    12d0:	38 81 00 30 	addi    r4,r1,48
    12d4:	d3 e1 00 28 	stfs    f31,40(r1)
    12d8:	38 a1 00 28 	addi    r5,r1,40
    12dc:	48 00 00 01 	bl      12dc <render__14TObjCMHairMenuFv+0x1b0>
    12e0:	c0 01 00 34 	lfs     f0,52(r1)
    12e4:	3a f7 00 01 	addi    r23,r23,1
    12e8:	2c 17 00 04 	cmpwi   r23,4
    12ec:	3a d6 00 04 	addi    r22,r22,4
    12f0:	ec 00 c8 2a 	fadds   f0,f0,f25
    12f4:	d0 01 00 34 	stfs    f0,52(r1)
    12f8:	41 80 ff 4c 	blt     1244 <render__14TObjCMHairMenuFv+0x118>
    12fc:	c0 38 00 34 	lfs     f1,52(r24)
    1300:	c0 00 00 00 	lfs     f0,0(0)
    1304:	fc 01 00 40 	fcmpo   cr0,f1,f0
    1308:	4c 40 13 82 	cror    eq,lt,eq
    130c:	41 82 00 78 	beq     1384 <render__14TObjCMHairMenuFv+0x258>
    1310:	c0 00 00 00 	lfs     f0,0(0)
    1314:	fc 01 00 40 	fcmpo   cr0,f1,f0
    1318:	4c 41 13 82 	cror    eq,gt,eq
    131c:	40 82 00 0c 	bne     1328 <render__14TObjCMHairMenuFv+0x1fc>
    1320:	c2 e0 00 00 	lfs     f23,0(0)
    1324:	48 00 00 08 	b       132c <render__14TObjCMHairMenuFv+0x200>
    1328:	ee e1 00 24 	fdivs   f23,f1,f0
    132c:	c0 20 00 00 	lfs     f1,0(0)
    1330:	3a c0 00 00 	li      r22,0
    1334:	c0 00 00 00 	lfs     f0,0(0)
    1338:	d0 21 00 20 	stfs    f1,32(r1)
    133c:	c3 40 00 00 	lfs     f26,0(0)
    1340:	d0 01 00 24 	stfs    f0,36(r1)
    1344:	80 18 00 24 	lwz     r0,36(r24)
    1348:	38 60 00 00 	li      r3,0
    134c:	7c 16 00 00 	cmpw    r22,r0
    1350:	40 82 00 08 	bne     1358 <render__14TObjCMHairMenuFv+0x22c>
    1354:	38 60 ff ff 	li      r3,-1
    1358:	fc 40 b8 90 	fmr     f2,f23
    135c:	c0 20 00 00 	lfs     f1,0(0)
    1360:	38 63 00 01 	addi    r3,r3,1
    1364:	38 81 00 20 	addi    r4,r1,32
    1368:	48 00 00 01 	bl      1368 <render__14TObjCMHairMenuFv+0x23c>
    136c:	c0 01 00 24 	lfs     f0,36(r1)
    1370:	3a d6 00 01 	addi    r22,r22,1
    1374:	2c 16 00 04 	cmpwi   r22,4
    1378:	ec 00 d0 2a 	fadds   f0,f0,f26
    137c:	d0 01 00 24 	stfs    f0,36(r1)
    1380:	41 80 ff c4 	blt     1344 <render__14TObjCMHairMenuFv+0x218>
    1384:	c0 38 00 34 	lfs     f1,52(r24)
    1388:	c0 00 00 00 	lfs     f0,0(0)
    138c:	fc 01 00 40 	fcmpo   cr0,f1,f0
    1390:	4c 40 13 82 	cror    eq,lt,eq
    1394:	41 82 04 84 	beq     1818 <render__14TObjCMHairMenuFv+0x6ec>
    1398:	ec 61 00 28 	fsubs   f3,f1,f0
    139c:	c0 00 00 00 	lfs     f0,0(0)
    13a0:	c0 40 00 00 	lfs     f2,0(0)
    13a4:	3a c0 00 00 	li      r22,0
    13a8:	c0 20 00 00 	lfs     f1,0(0)
    13ac:	ef c3 00 24 	fdivs   f30,f3,f0
    13b0:	c0 00 00 00 	lfs     f0,0(0)
    13b4:	d0 41 00 18 	stfs    f2,24(r1)
    13b8:	c3 60 00 00 	lfs     f27,0(0)
    13bc:	d0 21 00 1c 	stfs    f1,28(r1)
    13c0:	ef 5e 07 b2 	fmuls   f26,f30,f30
    13c4:	ef 00 06 b2 	fmuls   f24,f0,f26
    13c8:	48 00 00 88 	b       1450 <render__14TObjCMHairMenuFv+0x324>
    13cc:	80 18 00 24 	lwz     r0,36(r24)
    13d0:	fe e0 d0 90 	fmr     f23,f26
    13d4:	2c 00 00 00 	cmpwi   r0,0
    13d8:	41 82 00 08 	beq     13e0 <render__14TObjCMHairMenuFv+0x2b4>
    13dc:	fe e0 c0 90 	fmr     f23,f24
    13e0:	7c 16 c8 00 	cmpw    r22,r25
    13e4:	3a e0 00 1f 	li      r23,31
    13e8:	40 82 00 44 	bne     142c <render__14TObjCMHairMenuFv+0x300>
    13ec:	80 00 00 00 	lwz     r0,0(0)
    13f0:	3a e0 00 20 	li      r23,32
    13f4:	2c 00 00 02 	cmpwi   r0,2
    13f8:	41 82 00 24 	beq     141c <render__14TObjCMHairMenuFv+0x2f0>
    13fc:	80 18 00 2c 	lwz     r0,44(r24)
    1400:	54 03 60 26 	slwi    r3,r0,12
    1404:	48 00 00 01 	bl      1404 <render__14TObjCMHairMenuFv+0x2d8>
    1408:	48 00 00 01 	bl      1408 <render__14TObjCMHairMenuFv+0x2dc>
    140c:	c0 00 00 00 	lfs     f0,0(0)
    1410:	ec 00 00 7a 	fmadds  f0,f0,f1,f0
    1414:	ee f7 00 32 	fmuls   f23,f23,f0
    1418:	48 00 00 14 	b       142c <render__14TObjCMHairMenuFv+0x300>
    141c:	80 18 00 24 	lwz     r0,36(r24)
    1420:	2c 00 00 00 	cmpwi   r0,0
    1424:	40 82 00 08 	bne     142c <render__14TObjCMHairMenuFv+0x300>
    1428:	ee f7 07 72 	fmuls   f23,f23,f29
    142c:	fc 40 b8 90 	fmr     f2,f23
    1430:	c0 20 00 00 	lfs     f1,0(0)
    1434:	7e e3 bb 78 	mr      r3,r23
    1438:	38 81 00 18 	addi    r4,r1,24
    143c:	48 00 00 01 	bl      143c <render__14TObjCMHairMenuFv+0x310>
    1440:	c0 01 00 18 	lfs     f0,24(r1)
    1444:	3a d6 00 01 	addi    r22,r22,1
    1448:	ec 00 d8 2a 	fadds   f0,f0,f27
    144c:	d0 01 00 18 	stfs    f0,24(r1)
    1450:	80 18 00 28 	lwz     r0,40(r24)
    1454:	7c 16 00 00 	cmpw    r22,r0
    1458:	41 80 ff 74 	blt     13cc <render__14TObjCMHairMenuFv+0x2a0>
    145c:	c0 00 00 00 	lfs     f0,0(0)
    1460:	fe e0 d0 90 	fmr     f23,f26
    1464:	80 18 00 24 	lwz     r0,36(r24)
    1468:	ef 1c 00 28 	fsubs   f24,f28,f0
    146c:	2c 00 00 00 	cmpwi   r0,0
    1470:	40 82 00 0c 	bne     147c <render__14TObjCMHairMenuFv+0x350>
    1474:	ec 5a 07 72 	fmuls   f2,f26,f29
    1478:	48 00 00 10 	b       1488 <render__14TObjCMHairMenuFv+0x35c>
    147c:	c0 00 00 00 	lfs     f0,0(0)
    1480:	ec 40 06 b2 	fmuls   f2,f0,f26
    1484:	fe e0 10 90 	fmr     f23,f2
    1488:	c0 20 00 00 	lfs     f1,0(0)
    148c:	38 79 00 14 	addi    r3,r25,20
    1490:	c0 00 00 00 	lfs     f0,0(0)
    1494:	38 81 00 10 	addi    r4,r1,16
    1498:	ec 61 c0 2a 	fadds   f3,f1,f24
    149c:	c0 20 00 00 	lfs     f1,0(0)
    14a0:	d0 01 00 14 	stfs    f0,20(r1)
    14a4:	d0 61 00 10 	stfs    f3,16(r1)
    14a8:	48 00 00 01 	bl      14a8 <render__14TObjCMHairMenuFv+0x37c>
    14ac:	c0 20 00 00 	lfs     f1,0(0)
    14b0:	fc 40 b8 90 	fmr     f2,f23
    14b4:	c0 00 00 00 	lfs     f0,0(0)
    14b8:	38 81 00 10 	addi    r4,r1,16
    14bc:	ec 61 c0 2a 	fadds   f3,f1,f24
    14c0:	c0 20 00 00 	lfs     f1,0(0)
    14c4:	d0 01 00 14 	stfs    f0,20(r1)
    14c8:	38 60 00 1e 	li      r3,30
    14cc:	d0 61 00 10 	stfs    f3,16(r1)
    14d0:	48 00 00 01 	bl      14d0 <render__14TObjCMHairMenuFv+0x3a4>
    14d4:	c0 20 00 00 	lfs     f1,0(0)
    14d8:	fc 40 b8 90 	fmr     f2,f23
    14dc:	c0 00 00 00 	lfs     f0,0(0)
    14e0:	38 81 00 10 	addi    r4,r1,16
    14e4:	ec 61 c0 2a 	fadds   f3,f1,f24
    14e8:	c0 20 00 00 	lfs     f1,0(0)
    14ec:	d0 01 00 14 	stfs    f0,20(r1)
    14f0:	d0 61 00 10 	stfs    f3,16(r1)
    14f4:	80 78 00 28 	lwz     r3,40(r24)
    14f8:	38 63 00 13 	addi    r3,r3,19
    14fc:	48 00 00 01 	bl      14fc <render__14TObjCMHairMenuFv+0x3d0>
    1500:	c0 00 00 00 	lfs     f0,0(0)
    1504:	3c 60 00 00 	lis     r3,0
    1508:	ef 1a 07 72 	fmuls   f24,f26,f29
    150c:	3a c3 00 00 	addi    r22,r3,0
    1510:	ef 20 06 b2 	fmuls   f25,f0,f26
    1514:	3a e0 00 01 	li      r23,1
    1518:	80 18 00 24 	lwz     r0,36(r24)
    151c:	38 77 ff ff 	addi    r3,r23,-1
    1520:	54 64 18 38 	slwi    r4,r3,3
    1524:	c0 20 00 00 	lfs     f1,0(0)
    1528:	7c 17 00 00 	cmpw    r23,r0
    152c:	38 77 00 0f 	addi    r3,r23,15
    1530:	7c 96 22 14 	add     r4,r22,r4
    1534:	40 82 00 0c 	bne     1540 <render__14TObjCMHairMenuFv+0x414>
    1538:	fc 40 c0 90 	fmr     f2,f24
    153c:	48 00 00 08 	b       1544 <render__14TObjCMHairMenuFv+0x418>
    1540:	fc 40 c8 90 	fmr     f2,f25
    1544:	48 00 00 01 	bl      1544 <render__14TObjCMHairMenuFv+0x418>
    1548:	3a f7 00 01 	addi    r23,r23,1
    154c:	2c 17 00 04 	cmpwi   r23,4
    1550:	41 80 ff c8 	blt     1518 <render__14TObjCMHairMenuFv+0x3ec>
    1554:	48 00 00 01 	bl      1554 <render__14TObjCMHairMenuFv+0x428>
    1558:	48 00 00 01 	bl      1558 <render__14TObjCMHairMenuFv+0x42c>
    155c:	3c 60 00 00 	lis     r3,0
    1560:	c0 40 00 00 	lfs     f2,0(0)
    1564:	38 63 00 00 	addi    r3,r3,0
    1568:	3c 80 00 00 	lis     r4,0
    156c:	ef 62 07 b2 	fmuls   f27,f2,f30
    1570:	c0 03 00 0c 	lfs     f0,12(r3)
    1574:	c0 43 00 04 	lfs     f2,4(r3)
    1578:	38 84 00 00 	addi    r4,r4,0
    157c:	80 84 00 0c 	lwz     r4,12(r4)
    1580:	38 e1 00 58 	addi    r7,r1,88
    1584:	ec 60 10 28 	fsubs   f3,f0,f2
    1588:	c1 00 00 00 	lfs     f8,0(0)
    158c:	c0 e0 00 00 	lfs     f7,0(0)
    1590:	fc 00 d8 1e 	fctiwz  f0,f27
    1594:	c0 83 00 00 	lfs     f4,0(r3)
    1598:	ff c0 08 90 	fmr     f30,f1
    159c:	ec a8 10 fa 	fmadds  f5,f8,f3,f2
    15a0:	c0 c3 00 18 	lfs     f6,24(r3)
    15a4:	ed 27 10 fa 	fmadds  f9,f7,f3,f2
    15a8:	c0 63 00 08 	lfs     f3,8(r3)
    15ac:	c0 40 00 00 	lfs     f2,0(0)
    15b0:	38 c1 00 48 	addi    r6,r1,72
    15b4:	d8 01 00 78 	stfd    f0,120(r1)
    15b8:	ed 43 20 28 	fsubs   f10,f3,f4
    15bc:	c0 63 00 10 	lfs     f3,16(r3)
    15c0:	ef 42 07 b2 	fmuls   f26,f2,f30
    15c4:	90 81 00 08 	stw     r4,8(r1)
    15c8:	38 a0 00 00 	li      r5,0
    15cc:	ec 43 30 28 	fsubs   f2,f3,f6
    15d0:	80 01 00 7c 	lwz     r0,124(r1)
    15d4:	ec 25 07 b2 	fmuls   f1,f5,f30
    15d8:	d0 a1 00 74 	stfs    f5,116(r1)
    15dc:	ec 09 07 b2 	fmuls   f0,f9,f30
    15e0:	ec 67 30 ba 	fmadds  f3,f7,f2,f6
    15e4:	d0 a1 00 5c 	stfs    f5,92(r1)
    15e8:	ec a8 22 ba 	fmadds  f5,f8,f10,f4
    15ec:	ec 87 22 ba 	fmadds  f4,f7,f10,f4
    15f0:	38 61 00 54 	addi    r3,r1,84
    15f4:	ec 48 30 ba 	fmadds  f2,f8,f2,f6
    15f8:	d1 21 00 6c 	stfs    f9,108(r1)
    15fc:	38 81 00 08 	addi    r4,r1,8
    1600:	d1 21 00 64 	stfs    f9,100(r1)
    1604:	d0 a1 00 58 	stfs    f5,88(r1)
    1608:	d0 81 00 60 	stfs    f4,96(r1)
    160c:	d0 61 00 68 	stfs    f3,104(r1)
    1610:	d0 41 00 70 	stfs    f2,112(r1)
    1614:	d0 21 00 5c 	stfs    f1,92(r1)
    1618:	d0 01 00 64 	stfs    f0,100(r1)
    161c:	d0 01 00 6c 	stfs    f0,108(r1)
    1620:	d0 21 00 74 	stfs    f1,116(r1)
    1624:	90 e1 00 38 	stw     r7,56(r1)
    1628:	90 c1 00 3c 	stw     r6,60(r1)
    162c:	90 a1 00 40 	stw     r5,64(r1)
    1630:	98 01 00 0b 	stb     r0,11(r1)
    1634:	48 00 00 01 	bl      1634 <render__14TObjCMHairMenuFv+0x508>
    1638:	38 61 00 50 	addi    r3,r1,80
    163c:	38 81 00 54 	addi    r4,r1,84
    1640:	48 00 00 01 	bl      1640 <render__14TObjCMHairMenuFv+0x514>
    1644:	38 61 00 4c 	addi    r3,r1,76
    1648:	38 81 00 50 	addi    r4,r1,80
    164c:	48 00 00 01 	bl      164c <render__14TObjCMHairMenuFv+0x520>
    1650:	38 61 00 48 	addi    r3,r1,72
    1654:	38 81 00 4c 	addi    r4,r1,76
    1658:	48 00 00 01 	bl      1658 <render__14TObjCMHairMenuFv+0x52c>
    165c:	3a c0 00 00 	li      r22,0
    1660:	c0 20 00 00 	lfs     f1,0(0)
    1664:	38 61 00 38 	addi    r3,r1,56
    1668:	38 80 00 04 	li      r4,4
    166c:	38 a0 00 06 	li      r5,6
    1670:	48 00 00 01 	bl      1670 <render__14TObjCMHairMenuFv+0x544>
    1674:	c0 01 00 5c 	lfs     f0,92(r1)
    1678:	3a d6 00 01 	addi    r22,r22,1
    167c:	c0 41 00 64 	lfs     f2,100(r1)
    1680:	2c 16 00 03 	cmpwi   r22,3
    1684:	ec 60 d0 2a 	fadds   f3,f0,f26
    1688:	c0 21 00 6c 	lfs     f1,108(r1)
    168c:	c0 01 00 74 	lfs     f0,116(r1)
    1690:	ec 42 d0 2a 	fadds   f2,f2,f26
    1694:	ec 21 d0 2a 	fadds   f1,f1,f26
    1698:	ec 00 d0 2a 	fadds   f0,f0,f26
    169c:	d0 61 00 5c 	stfs    f3,92(r1)
    16a0:	d0 41 00 64 	stfs    f2,100(r1)
    16a4:	d0 21 00 6c 	stfs    f1,108(r1)
    16a8:	d0 01 00 74 	stfs    f0,116(r1)
    16ac:	41 80 ff b4 	blt     1660 <render__14TObjCMHairMenuFv+0x534>
    16b0:	fc 00 d8 1e 	fctiwz  f0,f27
    16b4:	3c 60 00 00 	lis     r3,0
    16b8:	3c 80 00 00 	lis     r4,0
    16bc:	cb e3 00 00 	lfd     f31,0(r3)
    16c0:	c3 80 00 00 	lfs     f28,0(0)
    16c4:	3b c4 00 00 	addi    r30,r4,0
    16c8:	d8 01 00 78 	stfd    f0,120(r1)
    16cc:	3b 81 00 54 	addi    r28,r1,84
    16d0:	c3 60 00 00 	lfs     f27,0(0)
    16d4:	3b 61 00 50 	addi    r27,r1,80
    16d8:	83 a1 00 7c 	lwz     r29,124(r1)
    16dc:	3b 41 00 4c 	addi    r26,r1,76
    16e0:	3b 20 00 00 	li      r25,0
    16e4:	3a e0 00 00 	li      r23,0
    16e8:	3a c0 00 00 	li      r22,0
    16ec:	3f e0 43 30 	lis     r31,17200
    16f0:	80 78 00 1c 	lwz     r3,28(r24)
    16f4:	38 16 00 42 	addi    r0,r22,66
    16f8:	93 e1 00 78 	stw     r31,120(r1)
    16fc:	7c 03 02 ae 	lhax    r0,r3,r0
    1700:	6c 00 80 00 	xoris   r0,r0,32768
    1704:	90 01 00 7c 	stw     r0,124(r1)
    1708:	c8 01 00 78 	lfd     f0,120(r1)
    170c:	ec 00 f8 28 	fsubs   f0,f0,f31
    1710:	ec c0 e0 24 	fdivs   f6,f0,f28
    1714:	fc 1b 30 00 	fcmpu   cr0,f27,f6
    1718:	41 82 00 e8 	beq     1800 <render__14TObjCMHairMenuFv+0x6d4>
    171c:	3c 60 00 00 	lis     r3,0
    1720:	6f 25 80 00 	xoris   r5,r25,32768
    1724:	38 e3 00 00 	addi    r7,r3,0
    1728:	3c 80 00 00 	lis     r4,0
    172c:	3c 60 43 30 	lis     r3,17200
    1730:	c0 a7 00 00 	lfs     f5,0(r7)
    1734:	c0 9e 00 08 	lfs     f4,8(r30)
    1738:	38 c4 00 00 	addi    r6,r4,0
    173c:	c0 3e 00 10 	lfs     f1,16(r30)
    1740:	38 00 00 04 	li      r0,4
    1744:	c0 1e 00 18 	lfs     f0,24(r30)
    1748:	38 81 00 58 	addi    r4,r1,88
    174c:	ec 61 20 28 	fsubs   f3,f1,f4
    1750:	90 61 00 78 	stw     r3,120(r1)
    1754:	ec 40 28 28 	fsubs   f2,f0,f5
    1758:	c8 26 00 00 	lfd     f1,0(r6)
    175c:	90 a1 00 7c 	stw     r5,124(r1)
    1760:	38 60 00 00 	li      r3,0
    1764:	c8 01 00 78 	lfd     f0,120(r1)
    1768:	ec 66 20 fa 	fmadds  f3,f6,f3,f4
    176c:	ec 46 28 ba 	fmadds  f2,f6,f2,f5
    1770:	d0 a1 00 58 	stfs    f5,88(r1)
    1774:	ec 00 08 28 	fsubs   f0,f0,f1
    1778:	d0 81 00 60 	stfs    f4,96(r1)
    177c:	ec 20 06 b2 	fmuls   f1,f0,f26
    1780:	d0 61 00 68 	stfs    f3,104(r1)
    1784:	d0 41 00 70 	stfs    f2,112(r1)
    1788:	7c 09 03 a6 	mtctr   r0
    178c:	7c a7 1a 14 	add     r5,r7,r3
    1790:	38 03 00 04 	addi    r0,r3,4
    1794:	c0 05 00 04 	lfs     f0,4(r5)
    1798:	38 63 00 08 	addi    r3,r3,8
    179c:	ec 1e 08 3a 	fmadds  f0,f30,f0,f1
    17a0:	7c 04 05 2e 	stfsx   f0,r4,r0
    17a4:	42 00 ff e8 	bdnz    178c <render__14TObjCMHairMenuFv+0x660>
    17a8:	3c 80 00 00 	lis     r4,0
    17ac:	7f 83 e3 78 	mr      r3,r28
    17b0:	38 84 00 00 	addi    r4,r4,0
    17b4:	7c 04 b8 2e 	lwzx    r0,r4,r23
    17b8:	38 81 00 0c 	addi    r4,r1,12
    17bc:	90 01 00 0c 	stw     r0,12(r1)
    17c0:	9b a1 00 0f 	stb     r29,15(r1)
    17c4:	48 00 00 01 	bl      17c4 <render__14TObjCMHairMenuFv+0x698>
    17c8:	7f 63 db 78 	mr      r3,r27
    17cc:	7f 84 e3 78 	mr      r4,r28
    17d0:	48 00 00 01 	bl      17d0 <render__14TObjCMHairMenuFv+0x6a4>
    17d4:	7f 43 d3 78 	mr      r3,r26
    17d8:	7f 64 db 78 	mr      r4,r27
    17dc:	48 00 00 01 	bl      17dc <render__14TObjCMHairMenuFv+0x6b0>
    17e0:	7f 44 d3 78 	mr      r4,r26
    17e4:	38 61 00 48 	addi    r3,r1,72
    17e8:	48 00 00 01 	bl      17e8 <render__14TObjCMHairMenuFv+0x6bc>
    17ec:	c0 20 00 00 	lfs     f1,0(0)
    17f0:	38 61 00 38 	addi    r3,r1,56
    17f4:	38 80 00 04 	li      r4,4
    17f8:	38 a0 00 06 	li      r5,6
    17fc:	48 00 00 01 	bl      17fc <render__14TObjCMHairMenuFv+0x6d0>
    1800:	3b 39 00 01 	addi    r25,r25,1
    1804:	3a d6 00 02 	addi    r22,r22,2
    1808:	2c 19 00 03 	cmpwi   r25,3
    180c:	3a f7 00 04 	addi    r23,r23,4
    1810:	41 80 fe e0 	blt     16f0 <render__14TObjCMHairMenuFv+0x5c4>
    1814:	48 00 00 01 	bl      1814 <render__14TObjCMHairMenuFv+0x6e8>
    1818:	e3 e1 01 38 	psq_l   f31,312(r1),0,0
    181c:	cb e1 01 30 	lfd     f31,304(r1)
    1820:	e3 c1 01 28 	lq      r30,288(r1)
    1824:	cb c1 01 20 	lfd     f30,288(r1)
    1828:	e3 a1 01 18 	psq_l   f29,280(r1),0,0
    182c:	cb a1 01 10 	lfd     f29,272(r1)
    1830:	e3 81 01 08 	lq      r28,256(r1)
    1834:	cb 81 01 00 	lfd     f28,256(r1)
    1838:	e3 61 00 f8 	psq_l   f27,248(r1),0,0
    183c:	cb 61 00 f0 	lfd     f27,240(r1)
    1840:	e3 41 00 e8 	lq      r26,224(r1)
    1844:	cb 41 00 e0 	lfd     f26,224(r1)
    1848:	e3 21 00 d8 	psq_l   f25,216(r1),0,0
    184c:	cb 21 00 d0 	lfd     f25,208(r1)
    1850:	e3 01 00 c8 	lq      r24,192(r1)
    1854:	cb 01 00 c0 	lfd     f24,192(r1)
    1858:	e2 e1 00 b8 	psq_l   f23,184(r1),0,0
    185c:	ca e1 00 b0 	lfd     f23,176(r1)
    1860:	ba c1 00 88 	lmw     r22,136(r1)
    1864:	80 01 01 44 	lwz     r0,324(r1)
    1868:	7c 08 03 a6 	mtlr    r0
    186c:	38 21 01 40 	addi    r1,r1,320
    1870:	4e 80 00 20 	blr
