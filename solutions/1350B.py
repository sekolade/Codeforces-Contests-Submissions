from functools import reduce
def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    dp=[1]*(n+1)
    dp[1]=1
    for i in range(1,n):
        el=l[i]
        ind=i+1
        k=factors(ind)
        for a in k:
            if a < ind and l[a-1] < el:
                dp[ind]=max(dp[ind],dp[a]+1)
    print(max(dp))