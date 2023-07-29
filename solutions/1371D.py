import io,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
for _ in range(int(input())):
    n,k=map(int,input().split())
    l=[[0]*n for i in range(n)]
    x=0
    y=0
    t=0
    dd1={i:0 for i in range(n)}
    dd2={i:0 for i in range(n)}
    for a in range(k):
        if a % n == 0 and a !=0:
            t+=1
            x=t
            y=0
        x%=n
        y%=n
        l[y][x]=1
        dd1[y]+=1
        dd2[x]+=1
        x+=1
        y+=1
    k1ma=max(dd1.values())
    k1mi=min(dd1.values())
    k2ma=max(dd2.values())
    k2mi=min(dd2.values())
    print((k1ma-k1mi)**2 + (k2ma-k2mi)**2)
    for i in l:
        print(*i,sep="")