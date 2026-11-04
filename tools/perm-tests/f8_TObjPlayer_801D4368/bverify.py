import subprocess
REPO="/Users/scott/Hermes/pso-decomp/pso-decomp-f8"; D=REPO+"/tools/perm-tests/f8_TObjPlayer_801D4368"
ODB=REPO+"/build/binutils/powerpc-eabi-objdump"
def words(o,lo=None,hi=None):
    cmd=[ODB,"-d",o]
    if lo: cmd+=["--start-address="+lo,"--stop-address="+hi]
    out=subprocess.run(cmd,capture_output=True,text=True).stdout
    ws=[]
    for l in out.splitlines():
        p=l.split("\t")
        if len(p)>=3 and p[0].strip().endswith(":"):
            ws.append(p[1].replace(" ",""))
    return ws
a=words(D+"/base_direct.o")
b=words(REPO+"/build/GPOE8P/src/pso/unk/text_801D40D4.o","0x294","0x4dc")
print(len(a),len(b),"BASE-VERIFY",("PASS" if a==b and len(a)==146 else "FAIL"))
