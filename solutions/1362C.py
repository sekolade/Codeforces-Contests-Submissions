
from math import floor
INF=99**9
for _ in range(int(input())):
    n=int(input())

    res=0
    for i in range(INF):
        ek = i+1
        t=2**ek
        bas=2**(i)
        if bas <= n:
            kk=(n-bas)//t
            res= res + ek + kk*ek
        else:
            break
    print(res)