import io,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
def solve(ind):
    pp=0
    x=l3[ind][0]
    for i in range(0,ind):
        tam,kal,ger=l3[i]
        if tam < x:
            t=ger-kal+(x-tam-1)*ger
        else:
            t=0
        pp+=t
    if pp <=k:
        return True
    else:
        return False
def binary(data,low,high):
    if low > high:
        return high
    else:
        mid=int((low+high)/2)
        st=solve(mid)
        if st == True:
            return binary(data,mid+1,high)
        else:
            return binary(data,low,mid-1)
n,k=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l3=[]
for i in range(n):
    tam,kal=divmod(l2[i],l1[i])
    l3.append([tam,kal,l1[i]])
l3.sort()
res=binary(l3,0,n-1)
x=l3[res][0]
pp=0
ss=0
hh=0
for i in range(res+1):
    tam,kal,ger=l3[i]
    ss+=ger
    if tam < x:
        t=ger-kal+(x-tam-1)*ger
    else:
        t=0
        hh+=l3[i][1]
    pp+=t
kal=k-pp
p1=ss-hh
if kal - p1 > 0:
    kal-=p1
    print(x+1+kal//ss)
elif kal - p1 == 0:
    print(x+1)
elif kal - p1 < 0:
    print(x)