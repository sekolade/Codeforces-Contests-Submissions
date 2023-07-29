import io,os,sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
from heapq import *
from math import log2
heap=[]
n,kk=map(int,input().split())
t=n
if kk>n:
    print("NO")
else:
    while t > 0:
        k=int(log2(t))

        h=2**k
        heappush(heap,-k)

        t-=h
    if len(heap) == kk:
        sys.stdout.write("YES" + "\n")
        for i in heap:
            sys.stdout.write(str(2**(-i)) + " ")
    elif len(heap) > kk:
        sys.stdout.write("NO" + "\n")
    else:
        while len(heap) < kk:
            k=-heappop(heap)
            heappush(heap,-(k-1))
            heappush(heap,-(k-1))
        sys.stdout.write("YES" + "\n")
        for i in heap:
            sys.stdout.write(str(2**(-i)) + " ")