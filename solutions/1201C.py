import io,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
n,k=map(int,input().split())
l=sorted(map(int,input().split()))
medi=n//2
ll=[]
ans=l[medi]
for i in range(medi+1,n):
    ll.append(l[i]-l[i-1])
for i in range(len(ll)):
    ger=i+1
    el=ll[i]
    y=k//ger
    if y >= el:
        k-=el*ger
        ans+=el
    else:
        k-=y*ger
        ans+=y
if k > 0:
    t=n-medi
    y=k//t
    ans+=y
print(ans)