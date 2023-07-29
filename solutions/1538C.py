def binary1(data,target,low,high):
    if low > high:
        return high
    else:
        mid=(low+high)//2
        if data[mid] <= target:
            return binary1(data,target,mid+1,high)
        else:
            return binary1(data,target,low,mid-1)
def binary2(data,target,low,high):
    if low > high:
        return low
    else:
        mid=(low+high)//2
        if data[mid] >= target:
            return binary2(data,target,low,mid-1)
        else:
            return binary2(data,target,mid+1,high)


for _ in range(int(input())):
    n,l,r=map(int,input().split())
    dd=list(map(int,input().split()))
    d2=sorted(dd)
    res=0
    for i in range(n):
        el=d2[i]
        left=l-el
        right=r-el
        t1=binary2(d2,left,0,n-1) #t1 ......
        t2=binary1(d2,right,0,n-1) # ....... t2
        if t1 == n:
            c=0
        elif t2 == -1:
            c=0
        else:
            c=t2-t1+1
        res+=c
    for i in d2:
        if l<=2*i<=r:
            res-=1
    if res <=0:
        print(0)
    else:
        print(res//2)