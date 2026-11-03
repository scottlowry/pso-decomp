void f4(short *, void *, unsigned, int);
void f1(int);
void g1(short a) { f1(a == 2); }
void g4(short *l, int buf, int info, short op) {
    f4(l, (void *)buf, info, op == 66);
    f4(l, (void *)buf, info, op == 65);
}
