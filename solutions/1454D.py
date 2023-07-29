import collections


def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)
            n //= d

        d += 1
    if n > 1:
       primfac.append(n)
    return primfac


for _ in range(int(input())):
    a=int(input())
    l=collections.Counter(primes(a)).most_common()
    result=[l[0][0]]*l[0][1]
    for r in range(1,len(l)):
        k,t=l[r]
        for i in range(t):
            result[i]*=k
    print(len(result))
    print(*result[::-1])