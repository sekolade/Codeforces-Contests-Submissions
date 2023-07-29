import io,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    dp=[0]*(n)
    dp[n-1]=l[n-1]
    for i in range(n-1,-1,-1):
        if i+l[i] < n:
            dp[i]=l[i]+dp[i+l[i]]
        else:
            dp[i]=l[i]
    print(max(dp))