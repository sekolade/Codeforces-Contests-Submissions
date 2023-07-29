import io,os,sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
from math import log2
n=int(input())
l=sorted(map(int,input().split()),reverse=True)
t=pow(n,0.5)
c=int(log2(t))+1
ca=c
ans=0
cc=1
for i in range(n):
    if i+1 > cc:
        cc*=4
        ca-=1
    ans+=ca*l[i]
sys.stdout.write(str(ans) + "\n")