import io,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
for _ in range(int(input())):
    k,n,a,b=map(int,input().split())
    if k % b == 0:
        d0= k // b -1
    else:
        d0= k// b
    if d0 < n:
        print(-1)
    else:
        t1=k/a
        if k%a == 0:
            d1=k//a-1
        else:
            d1=k//a
        if (k-(b*n)) % (a-b) == 0:
            d2=(k-(b*n)) // (a-b) -1
        else:
            d2=(k-(b*n)) // (a-b)
        print(min(min(d1,n),min(d2,n)))