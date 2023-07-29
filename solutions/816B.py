import io,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
n,k,q=map(int,input().split())
lim=2*(10**5)+1
pas=[]
dif_arr=[0]*(lim)
for i in range(n):
    s,e=map(int,input().split())
    dif_arr[s]+=1
    if e+1 < len(dif_arr):
        dif_arr[e+1]-=1
t=0
for i in range(lim):
    t+=dif_arr[i]
    pas.append(t)
pas2=[]
t=0
for i in pas:
    if i >=k:
        t+=1
    pas2.append(t)
for i in range(q):
    s,e=map(int,input().split())
    if s-1 > -1:
        print(pas2[e]-pas2[s-1])
    else:
        print(pas2[e])