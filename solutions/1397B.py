import io,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
from math import ceil,floor
n=int(input())
l=list(map(int,input().split()))
l.sort()
k=l[-1]**(1/(n-1))
r=0
po1=ceil(k)
po2=floor(k)
for i in range(n):
    el=l[i]
    r+=abs(el-(po1**i))
r2=0
for i in range(n):
    el=l[i]
    r2+=abs(el-(po2**i))
print(min(r,r2))