n=int(input())
dd={}
l=sorted(map(int,input().split()))
for i in range(n-1,-1,-1):
    dd[l[i]]=i
dp1=[0]*(n+1)
dp1[0]=l[0]
dp1[-1]=0
for i in range(1,n):
    if l[i]-1 in dd:
        dp1[i]=max(dp1[i-1],l[i]*(i-dd[l[i]]+1)+dp1[dd[l[i]-1]-1])
    else:
        dp1[i]=dp1[i-1]+l[i]
print(max(dp1))