for _ in range(int(input())):
    n,m=map(int,input().split())
    l=[]
    for i in range(n):
        l.append(list(map(int,input().split())))
    dp1,dp2=[0]*(n+m-1),[0]*(n+m-1)
    for i in range(n):
        for a in range(m):
            if l[i][a] == 1:
                dp1[i+a]+=1
            else:dp2[i+a]+=1
    ans=0
    for i in range((n+m-1)//2):
        ans+=(min(dp1[i]+dp1[n+m-1-i-1],dp2[i]+dp2[n+m-1-i-1]))
    print(ans)