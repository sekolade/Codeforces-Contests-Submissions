import io,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
n,a,b,k=map(int,input().split())
l=list(map(int,input().split()))
bou=a
for i in range(n):
    l[i]=l[i]%(a+b) if l[i]%(a+b) != 0 else a+b
ll=[]
ans=0
for i in l:
    if i-a > 0:
        ll.append(i-a)
    else:
        ans+=1
ll.sort()
for i in range(len(ll)):
    ll[i]=ll[i]//a + (1 if ll[i]%a != 0 else 0)
for i in ll:
    k-=i
    if k >= 0:
        ans+=1
    else:break
print(ans)