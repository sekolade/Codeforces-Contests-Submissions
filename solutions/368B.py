import io,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
n,m=map(int,input().split())
l=list(map(int,input().split()))
pas=[]
t={}
for i in l:
    if i not in t:
        t[i]=1
    else:
        t[i]+=1
res=len(t.keys())
p=[res]
for i in range(n):
    el=l[i]
    t[el]-=1
    if t[el] == 0:
        res-=1
    p.append(res)
for i in range(m):
    print(p[int(input())-1])