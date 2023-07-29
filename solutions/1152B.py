from math import log2
n=int(input())
p=0
l=[]
while not log2(n+1).is_integer():
    p+=2

    k=int(log2(n))
    l.append(k+1)
    tam=2**k
    kalan=n-2**k
    n-=(2*kalan)
    if log2(n).is_integer():
        p-=1
        break


print(p)
if l:
    print(*l)