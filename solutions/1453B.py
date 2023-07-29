import io,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    res=0
    for i in range(n-1):
        res+=abs(l[i+1]-l[i])
    best=99**9
    best=min(best,res-abs(l[0]-l[1]))
    best=min(best,res-abs(l[-1]-l[-2]))
    for i in range(1,n-1):
        mid=l[i]
        left=l[i-1]
        right=l[i+1]
        if left>= mid and right >= mid:
            t=min(left,right)
            tt=(t-mid)*2
            best=min(best,res-tt)
        elif left <= mid and right <=mid:
            t=max(left,right)
            tt=(mid-t)*2
            best=min(best,res-tt)
    print(best)