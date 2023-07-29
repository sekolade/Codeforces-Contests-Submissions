import io,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
n,m,k=map(int,input().split())
l=list(map(int,input().split()))
op=[]
for i in range(m):
    op.append(list(map(int,input().split())))
kk=[]
for i in range(k):
    kk.append(list(map(int,input().split())))
da1=[0]*(1+m)
for s,e in kk:
    da1[s]+=1
    if e+1 < m+1:
        da1[e+1]-=1
r=0
for i in range(1,m+1):
    r+=da1[i]
    op[i-1][2]*=r
da2=[-1]+[l[0]]
for i in range(n-1):
    da2.append(l[i+1]-l[i])
for s,e,w in op:
    da2[s]+=w
    if e+1 < n+1:
        da2[e+1]-=w
r=0
for i in range(1,n+1):
    r+=da2[i]
    print(r,end=" ")