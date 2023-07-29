
from time import time


def num_factors(n):
    results = set()
    for i in range(1, int(n**(1/2)) + 1):
        if n % i == 0: results.update([i,int(n/i)])
    return results

n,k=map(int,input().split())
ttt=time()
t=num_factors(n)

if len(t) < k:
    print(-1)
else:
    tt=list(t)
    tt.sort()
    print(tt[k-1])