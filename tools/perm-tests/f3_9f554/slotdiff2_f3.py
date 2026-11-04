import re, subprocess, sys

def parse_era(path):
    rows=[]
    for line in open(path):
        m=re.match(r"/\* ([0-9A-F]{8}) [0-9A-F]{8}\s+((?:[0-9A-F]{2}\s){3}[0-9A-F]{2})\s*\*/\s*(.*)$", line.strip())
        if m:
            t=m.group(3).strip()
            if t.endswith(':'): continue
            rows.append(t)
    return rows

def parse_ours(path):
    out=subprocess.run(['/opt/homebrew/opt/binutils/bin/objdump','-dr',path],capture_output=True,text=True).stdout
    rows=[]; relocs=[]
    for line in out.splitlines():
        m=re.match(r"\s*[0-9a-f]+:\s+((?:[0-9a-f]{2} ){4})\s+(\S.*?)\s*$", line)
        r=re.match(r"\s*[0-9a-f]+:\s+(R_PPC\S*)\t(\S+)", line)
        if m:
            t=m.group(2).strip()
            t=re.sub(r"\s+<[^>]*>","",t)
            t=re.sub(r"\s+"," ",t).strip()
            rows.append(t); relocs.append([])
        elif r and rows:
            relocs[-1].append((r.group(1),r.group(2)))
    res=[]
    for t,rl in zip(rows,relocs):
        mn=t.split(' ',1)[0]
        ops=t.split(' ',1)[1] if ' ' in t else ''
        if rl:
            typ,sym=rl[0]
            if mn in ('bl','b','ba','blrl','bcl') and typ=='R_PPC_REL24':
                t=mn+' '+sym
            elif typ=='R_PPC_ADDR16_HA':
                t=mn+' '+ops.rsplit(',',1)[0]+', '+sym+'@ha'
            elif typ=='R_PPC_ADDR16_LO' and mn in ('addi','addis','ori','oris'):
                t=mn+' '+ops.rsplit(',',1)[0]+', '+sym+'@l'
            elif typ=='R_PPC_EMB_SDA21':
                mo=re.search(r'^(\S+?),(-?\d+)\((r?\d+)\)$',ops)
                if mo: t=mn+' '+mo.group(1)+', '+sym+'@sda21(r0)'
        res.append(t)
    return res

def norm(t):
    t=t.split('#')[0].strip()
    t=re.sub(r'\s*,\s*',',',t)
    t=re.sub(r'\s+',' ',t)
    t=re.sub(r'\br13\b','r0',t)
    t=re.sub(r'\br2\b','r0',t)
    def hexd(m): return '(0x%X)'%int(m.group(1)) if int(m.group(1))>=0 else '(-0x%X)'%-int(m.group(1))
    t=re.sub(r'\((-?\d+)\)',hexd,t)
    def hexd3(m):
        v=int(m.group(1))
        return (',0x%X(' % v) if v>=0 else (',-0X%X(' % -v)
    t=re.sub(r',(-?\d+)\(',hexd3,t)
    def hexd2(m):
        v=int(m.group(1))
        return ',0x%X'%v if v>=0 else ',-0x%X'%-v
    t=re.sub(r',(-?\d+)$',hexd2,t)
    t=t.lower()
    mb=re.match(r'^(b|beq|bne|blt|bgt|bge|ble|bns|bso|bdz|bnz)\s+\S+$',t)
    if mb: t=mb.group(1)+' T'
    return t

era=[norm(x) for x in parse_era(sys.argv[1])]
ours=[norm(x) for x in parse_ours(sys.argv[2])]
print("era rows:",len(era),"ours rows:",len(ours))
import difflib
sm=difflib.SequenceMatcher(None,era,ours,autojunk=False)
same=0
for tag,i1,i2,j1,j2 in sm.get_opcodes():
    if tag=='equal':
        same+=(i2-i1)
    elif tag=='replace':
        for k in range(max(i2-i1,j2-j1)):
            e=era[i1+k] if i1+k<i2 else '<del>'
            o=ours[j1+k] if j1+k<j2 else '<ins>'
            print("R",i1+k,"O:",e,"|N:",o)
    elif tag=='delete':
        for k in range(i1,i2): print("D",k,"O:",era[k],"|N:<missing>")
    elif tag=='insert':
        for k in range(j1,j2): print("I",i1,"N:",ours[k],"|O:<absent>")
print("same:",same,"of era",len(era),"=> pct %.2f"%(100.0*same/len(era)))
