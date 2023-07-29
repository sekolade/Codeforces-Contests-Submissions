import io,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
def binary(data,target,low,high):
    if low > high:
        return low
    else:
        mid=(low+high)//2
        if data[mid] >= target:
            return binary(data,target,low,mid-1)
        else:
            return binary(data,target,mid+1,high)
"********************************************************************"
n=int(input())
mi=[]
ma=[]
res=0
cu=0
for i in range(n):
    hh=list(map(int,input().split()))
    kk=hh[0]
    yer_min=99**9
    yer_ma=-1
    for i in range(1,kk+1):
        el=hh[i]
        yer_min=min(yer_min,el)
        yer_ma=max(yer_ma,el)
    f=False
    for i in range(1,kk):
        if hh[i+1] > hh[i]:
            f=True
            cu+=1
            break
    if not f:
        mi.append(yer_min)
        ma.append(yer_ma)
ma.sort()
p=n**2-(n-cu)**2
res+=p
for i in mi:
    k=binary(ma,i+1,0,len(ma)-1)
    if k != n:
        res+=n-k-cu
print(res)