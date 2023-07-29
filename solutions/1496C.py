import io,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
from math import sqrt
for _ in range(int(input())):
    n=int(input())
    l1=[]
    l2=[]
    for i in range(2*n):
        s,e=map(int,input().split())
        if s == 0:
            l1.append(pow(e,2))
        else:
            l2.append(pow(s,2))
    l1.sort()
    l2.sort()
    px=0
    ans=0
    while px < n:
        ans+=sqrt(l1[px]+l2[px])
        px+=1
    print(ans)