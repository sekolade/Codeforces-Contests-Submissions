MOD=10**9+7
n,k=map(int,input().split())
dd={}
for i in range(1,n+1):
    dd[i]=[]
    for a in range(i,n+1,i):
        dd[i].append(a)
dp=[[0]*(n+1) for i in range(k+1)]
dp[1]=[0]+[1]*(n)
 
for i in range(2,k+1):
    for a in dd:
        h=dp[i-1][a]
        for c in dd[a]:
            dp[i][c]+=h
            dp[i][c]%=MOD
print(sum(dp[-1])%(MOD))