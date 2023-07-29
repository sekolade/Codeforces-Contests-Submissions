import math,sys,io,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
from heapq import *
n=int(input())
l=list(map(int,input().split()))
q=[]
heapify(q)
t=0
res=0
best=-99**9
neg_top=0
for i in l:
    if i >= 0:
        res+=i
        t+=1
        best=max(best,t)
    else:
        res+=i
        heappush(q,i)
        t+=1
        neg_top+=i
        while  res < 0:
            h=heappop(q)
            res-=h
            t-=1
            neg_top-=h
        best=max(best,t)
print(max(best,0))