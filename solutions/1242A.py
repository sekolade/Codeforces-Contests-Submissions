def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return set(primfac)
n=int(input())
k=primes(n)
if n == 1 :
    print(1)
else:
    if len(k) == 1:
        print(next(iter(k)))
    else:
        print(1)