n=int(input())
l=list(map(int,input().split()))
from functools import reduce
from math import gcd
c=reduce(gcd,l)
t=0
p=sum(l)
dp=[[False]*(p+1) for i in range(n+1)]
dp[0][0]=True
for i in range(1,n+1):
    for po in range(p+1):
        if dp[i-1][po] or dp[i-1][po-l[i-1]]:
            dp[i][po]=True
if p % 2 != 0:
    print(0)
else:
    if dp[-1][p//2]:
        while c % 2 == 0:
            c//=2
            t+=1
        for ii in range(len(l)):
            h=0
            i=l[ii]
            while i % 2 == 0:
                h+=1
                i//=2
            if h <= t:
                print(1)
                print(ii+1)
                break
    else:
        print(0)