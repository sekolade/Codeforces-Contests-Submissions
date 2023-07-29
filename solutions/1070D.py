n,k=map(int,input().split())
l=list(map(int,input().split()))
p=0
r=0
flag=0
while p < n-1:
    el=l[p]
    k1=el//k
    k2=el%k
    if k1 !=0:
        r+=k1
        if k2 >0:
            l[p+1]+=k2
            flag=1
        else:
            flag=0
    else:
        if not flag:
            if k2 >0:
                l[p+1]+=k2
                flag=1
        else:
            r+=1
            flag=0
    p+=1
r+=l[-1]//k
if l[-1] % k != 0:
    print(r+1)
else:
    print(r)