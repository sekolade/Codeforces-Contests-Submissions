n,k=map(int,input().split())
l=list(map(int,input().split()))+[0]
INF=99**9
dp=[[INF,INF,INF] for i in range(n)]
h=sum(l[:k])
dp[k-1]=[h,h,1]
for i in range(k,n):
    el=dp[i-1][1]-l[i-k]+l[i]
    if el < dp[i-1][0]:
        dp[i]=[el,el,i-(k-1)+1]
    else:
        dp[i]=[dp[i-1][0],el,dp[i-1][2]]
print(min(dp)[2])