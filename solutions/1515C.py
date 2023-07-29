import io,os,sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
for _ in range(int(input())):
    n,m,x=map(int,input().split())
    l=list(map(int,input().split()))
    t=[[l[i],i,-1] for i in range(n)]
    t.sort()
    p=0
    mod=m
    dd={i:0 for i in range(1,m+1)}
    for i in range(n):
        t[i][2]=p+1
        dd[p+1]+=t[i][0]
        p+=1
        p%=mod
    k=sorted(dd.values())
    if k[-1] - k[0] > x:
        sys.stdout.write("NO" + "\n")
    else:
        sys.stdout.write("YES" + "\n")
        t.sort(key=lambda x:x[1])
        for i in range(n):
            sys.stdout.write(str(t[i][2]) + " ")