import io,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
n=int(input())
l=list(map(int,input().split()))
hh,kk=False,10**6
t=0
for ii in range(n):
    i=l[ii]
    if i == 0:
        hh=True
        t=ii
        break

if t > 0:
    print(-1)
else:
    f=True
    for i in range(n):
        el=l[i]
        if el != 0:
            posmax=i+1
            if el > posmax:
                print(-1)
                f=False
                break

    if f:
        st=l[0]
        res=[-3]*n
        pp=set()
        for i in range(n):
            if l[i] != st:
                res[i]=st
                pp.add(st)
                st=l[i]
        t=max(l)
        px=0
        px2=0
        while px < t:
            if px in pp:
                px+=1
                continue
            if res[px2] != -3:
                px2+=1
                continue
            res[px2]=px
            px2+=1
            px+=1
        for i in res:
            if i == -3:
                print(kk,end=" ")
            else:
                print(i,end=" ")