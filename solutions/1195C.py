import sys
input=sys.stdin.readline
n=int(input())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
dp=[0]*n
dp[-1]=[l1[-1],l2[-1]]
if n >= 2:
    dp[-2]=[l1[-2]+l2[-1],l2[-2]+l1[-1]]
    for i in range(-3,-n-1,-1):
        ind=i
        # sec l1
        k=max(dp[ind+1][1]+l1[ind],dp[ind+2][1]+l1[ind])
        # sec l2
        kk=max(dp[ind+1][0]+l2[ind],dp[ind+2][0]+l2[ind])
        dp[ind]=[k,kk]
print(max(dp[0]))