import sys
input=sys.stdin.readline
s=list(input())
n=len(s)
dp=[0]*n
dp[0]=0
for i in range(1,n):
    dp[i]=dp[i-1]+(1 if s[i-1]==s[i] else 0)
pas=[]
t=0
for i in dp:
    t+=i
    pas.append(i)
pas.append(0)
for _ in range(int(input())):
    s,e=map(int,input().split())
    print(pas[e-1]-pas[s-1])