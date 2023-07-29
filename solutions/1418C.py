import io,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    dp=[0]*(n+1)
    start=1
    dp[1] = 1 if l[n-1] == 1 else 0
    for i in range(n-2,-1,-1):
        start+=1
        el=l[i]
        dp[start]=99**9
        dp[start]=min(dp[start],dp[max(0,start-2)] + l[i])
        dp[start]=min(dp[start],dp[max(0,start-3)] + l[i])
        dp[start]=min(dp[start],dp[max(0,start-3)] + l[i]+l[i+1])
        dp[start]=min(dp[start],dp[max(0,start-4)] + l[i]+l[i+1])
    print(dp[-1])