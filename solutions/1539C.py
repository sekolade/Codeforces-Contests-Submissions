import io,os,sys,math
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
n,k,x=map(int,input().split())
l=sorted(map(int,input().split()))
dd=[]
for i in range(n-1):
    el1=l[i]
    el2=l[i+1]
    t=abs(el2-el1)
    if t > x:
        if t % x == 0:
            kkk= t//x -1
        else:
            kkk = t//x
        dd.append(kkk)
dd.sort()
kk=k
c=0
f=True
for i in range(len(dd)):
    el=dd[i]
    c+=el
    if c > kk:
        ccc=(len(dd)-1)-i +1
        ans=ccc+1
        f=False
        break
if f:
    print(1)
else:
    print(ans)