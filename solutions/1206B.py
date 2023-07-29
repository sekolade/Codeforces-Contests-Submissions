import io,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
n=int(input())
l=list(map(int,input().split()))
p=99**9
t=1
k=0
for i in l:
    k1=abs(1-i)
    k2=abs(-1-i)
    if k1 < k2:
        t*=1
        k+=k1
    else:
        t*=-1
        k+=k2
    p=min(p,abs(k1-k2))
if t == 1:
    print(k)
else:
    print(k+p)