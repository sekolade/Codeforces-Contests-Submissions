import io,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
n=int(input())
l=list(map(int,input().split()))
if n == 1:
    print(n,n)
    print(0)
    print(n,n)
    print(0)
    print(n,n)
    print(-l[-1])
elif n == 2:
    print(n-1,n-1)
    print(-l[-2])
    print(n,n)
    print(-l[-1])
    print(n,n)
    print(0)
else:
    res=[]
    for ii in range(n-1):
        i=l[ii]
        if i > 0:
            res.append([-(n)*i,+(n-1)*i])
        elif i < 0:
            res.append([+(n)*(-i),-(n-1)*(-i)])
        else:
            res.append([0,0])
    print(1,n)
    for i in res:
        print(i[0],end=" ")
    print(0)
    print(1,n-1)
    for i in res:
        print(i[1],end=" ")
    print()
    print(n,n)
    print(-l[-1])