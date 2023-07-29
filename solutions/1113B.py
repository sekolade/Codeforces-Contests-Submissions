from functools import reduce
def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
n=int(input())
l=list(map(int,input().split()))
low=min(l)
t=sum(l)
best=t
for i in l:
    fak=factors(i)
    for x in fak:
        new=t
        if i > x*low:
            new-=low
            new+=x*low
            new-=i
            new+=int(i/x)
        best=min(best,new)
print(best)