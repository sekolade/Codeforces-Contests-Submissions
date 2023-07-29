bas="FRCFCRFFRCFCRF"
dd=[]
for a in range(7):
    for i in range(a,7+a):
            for e in range(i+1,7+a):
                kk=bas[i:e]
                p=[kk.count("F"),kk.count("R"),kk.count("C")]
                dd.append((p,sum(p)))
a,b,c=map(int,input().split())
t=min(a//3,b//2,c//2)
best=0
for i in dd:
    s,uz=i
    fs,rs,cs=s
    if fs <= a-3*t and rs <= b-2*t and cs <= c-2*t:
        best=max(best,uz)
print(7*t+best )