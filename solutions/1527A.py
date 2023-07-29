from math import log2,floor
for _ in range(int(input())):
    k=int(input())
    t=log2(k)
    p=2**floor(t)
    print(p-1)