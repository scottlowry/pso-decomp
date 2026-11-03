.fn transform_chunk_vertices_pos_normal, global
/* 803E3390 003D6270  80 A3 00 00 */	lwz r5, 0x0(r3)
/* 803E3394 003D6274  80 C3 00 04 */	lwz r6, 0x4(r3)
/* 803E3398 003D6278  80 E3 00 08 */	lwz r7, 0x8(r3)
/* 803E339C 003D627C  94 21 FF C0 */	stwu r1, -0x40(r1)
/* 803E33A0 003D6280  D9 C1 00 08 */	stfd f14, 0x8(r1)
/* 803E33A4 003D6284  D9 E1 00 10 */	stfd f15, 0x10(r1)
/* 803E33A8 003D6288  38 E7 FF FF */	subi r7, r7, 0x1
/* 803E33AC 003D628C  DA 01 00 18 */	stfd f16, 0x18(r1)
/* 803E33B0 003D6290  DA 21 00 20 */	stfd f17, 0x20(r1)
/* 803E33B4 003D6294  DA 41 00 28 */	stfd f18, 0x28(r1)
/* 803E33B8 003D6298  7C E9 03 A6 */	mtctr r7
/* 803E33BC 003D629C  E0 04 00 00 */	psq_l f0, 0x0(r4), 0, qr0
/* 803E33C0 003D62A0  38 C6 FF F8 */	subi r6, r6, 0x8
/* 803E33C4 003D62A4  E0 24 80 08 */	psq_l f1, 0x8(r4), 1, qr0
/* 803E33C8 003D62A8  38 A5 FF F4 */	subi r5, r5, 0xc
/* 803E33CC 003D62AC  E0 C4 00 24 */	psq_l f6, 0x24(r4), 0, qr0
/* 803E33D0 003D62B0  E5 06 00 08 */	psq_lu f8, 0x8(r6), 0, qr0
/* 803E33D4 003D62B4  E0 E4 80 2C */	psq_l f7, 0x2c(r4), 1, qr0
/* 803E33D8 003D62B8  E5 26 00 08 */	psq_lu f9, 0x8(r6), 0, qr0
/* 803E33DC 003D62BC  11 60 32 1C */	ps_madds0 f11, f0, f8, f6
/* 803E33E0 003D62C0  E0 44 00 0C */	psq_l f2, 0xc(r4), 0, qr0
/* 803E33E4 003D62C4  11 81 3A 1C */	ps_madds0 f12, f1, f8, f7
/* 803E33E8 003D62C8  E0 64 80 14 */	psq_l f3, 0x14(r4), 1, qr0
/* 803E33EC 003D62CC  11 A0 02 5A */	ps_muls1 f13, f0, f9
/* 803E33F0 003D62D0  E5 46 00 08 */	psq_lu f10, 0x8(r6), 0, qr0
/* 803E33F4 003D62D4  11 C1 02 5A */	ps_muls1 f14, f1, f9
/* 803E33F8 003D62D8  E0 A4 80 20 */	psq_l f5, 0x20(r4), 1, qr0
/* 803E33FC 003D62DC  11 62 5A 1E */	ps_madds1 f11, f2, f8, f11
/* 803E3400 003D62E0  11 83 62 1E */	ps_madds1 f12, f3, f8, f12
/* 803E3404 003D62E4  E0 84 00 18 */	psq_l f4, 0x18(r4), 0, qr0
/* 803E3408 003D62E8  11 A2 6A 9C */	ps_madds0 f13, f2, f10, f13
/* 803E340C 003D62EC  E5 06 00 08 */	psq_lu f8, 0x8(r6), 0, qr0
/* 803E3410 003D62F0  11 C3 72 9C */	ps_madds0 f14, f3, f10, f14
/* 803E3414 003D62F4  11 E4 5A 5C */	ps_madds0 f15, f4, f9, f11
/* 803E3418 003D62F8  12 05 62 5C */	ps_madds0 f16, f5, f9, f12
/* 803E341C 003D62FC  E5 26 00 08 */	psq_lu f9, 0x8(r6), 0, qr0
/* 803E3420 003D6300  12 24 6A 9E */	ps_madds1 f17, f4, f10, f13
/* 803E3424 003D6304  12 45 72 9E */	ps_madds1 f18, f5, f10, f14
/* 803E3428 003D6308  E5 46 00 08 */	psq_lu f10, 0x8(r6), 0, qr0
/* 803E342C 003D630C  2C 07 00 00 */	cmpwi r7, 0x0
/* 803E3430 003D6310  41 82 00 54 */	beq .L_803E3484
.L_803E3434:
/* 803E3434 003D6314  11 60 32 1C */	ps_madds0 f11, f0, f8, f6
/* 803E3438 003D6318  F5 E5 00 0C */	psq_stu f15, 0xc(r5), 0, qr0
/* 803E343C 003D631C  11 81 3A 1C */	ps_madds0 f12, f1, f8, f7
/* 803E3440 003D6320  F6 05 80 08 */	psq_stu f16, 0x8(r5), 1, qr0
/* 803E3444 003D6324  11 A0 02 5A */	ps_muls1 f13, f0, f9
/* 803E3448 003D6328  F6 25 00 04 */	psq_stu f17, 0x4(r5), 0, qr0
/* 803E344C 003D632C  11 C1 02 5A */	ps_muls1 f14, f1, f9
/* 803E3450 003D6330  F6 45 80 08 */	psq_stu f18, 0x8(r5), 1, qr0
/* 803E3454 003D6334  11 62 5A 1E */	ps_madds1 f11, f2, f8, f11
/* 803E3458 003D6338  11 83 62 1E */	ps_madds1 f12, f3, f8, f12
/* 803E345C 003D633C  E5 06 00 08 */	psq_lu f8, 0x8(r6), 0, qr0
/* 803E3460 003D6340  11 A2 6A 9C */	ps_madds0 f13, f2, f10, f13
/* 803E3464 003D6344  11 C3 72 9C */	ps_madds0 f14, f3, f10, f14
/* 803E3468 003D6348  11 E4 5A 5C */	ps_madds0 f15, f4, f9, f11
/* 803E346C 003D634C  12 05 62 5C */	ps_madds0 f16, f5, f9, f12
/* 803E3470 003D6350  E5 26 00 08 */	psq_lu f9, 0x8(r6), 0, qr0
/* 803E3474 003D6354  12 24 6A 9E */	ps_madds1 f17, f4, f10, f13
/* 803E3478 003D6358  12 45 72 9E */	ps_madds1 f18, f5, f10, f14
/* 803E347C 003D635C  E5 46 00 08 */	psq_lu f10, 0x8(r6), 0, qr0
/* 803E3480 003D6360  42 00 FF B4 */	bdnz .L_803E3434
.L_803E3484:
/* 803E3484 003D6364  F5 E5 00 0C */	psq_stu f15, 0xc(r5), 0, qr0
/* 803E3488 003D6368  F6 05 80 08 */	psq_stu f16, 0x8(r5), 1, qr0
/* 803E348C 003D636C  F6 25 00 04 */	psq_stu f17, 0x4(r5), 0, qr0
/* 803E3490 003D6370  F6 45 80 08 */	psq_stu f18, 0x8(r5), 1, qr0
/* 803E3494 003D6374  C9 C1 00 08 */	lfd f14, 0x8(r1)
/* 803E3498 003D6378  C9 E1 00 10 */	lfd f15, 0x10(r1)
/* 803E349C 003D637C  CA 01 00 18 */	lfd f16, 0x18(r1)
/* 803E34A0 003D6380  CA 21 00 20 */	lfd f17, 0x20(r1)
/* 803E34A4 003D6384  CA 41 00 28 */	lfd f18, 0x28(r1)
/* 803E34A8 003D6388  38 21 00 40 */	addi r1, r1, 0x40
/* 803E34AC 003D638C  4E 80 00 20 */	blr
.endfn transform_chunk_vertices_pos_normal
