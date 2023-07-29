from functools import reduce
def allFactors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
def m(x,y,z):
    for i in x:
        ar=i
        te=y[:i]
        f=True
        for a in range(0,len(y),ar):
            ce=y[a:a+i]
            if te != ce:
              f=False
        if f:
            z.add(te)
s1=(input())
s2=(input())
k1=allFactors(len(s1))
k2=allFactors(len(s1))
d1=set()
d2=set()
m(k1,s1,d1)
m(k2,s2,d2)
print(len(d1.intersection(d2)))