import math,sys,io,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
def SieveOfEratosthenes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    arr=[]
    for i in range(len(prime)):
        if prime[i]:
            arr.append(i)
    return arr
c=SieveOfEratosthenes(int((10**9)**(1/2)))
def primeFactors(n):
    fact={}
    while n % 2 == 0:
        if 2 in fact:
            fact[2]+=1
        else:
            fact[2]=1
        n //= 2
    t=int(math.sqrt(n))+2
    for i in c:
        if t < i:
            break
        while n % i== 0:
            if i in fact:
                fact[i]+=1
            else:
                fact[i]=1
            n//= i
    if n > 2:
        if n in fact:
            fact[n]+=1
        else:
            fact[n]=1
    return fact

for _ in range(int(input())):
    a,b,k=map(int,input().split())
    t1=primeFactors(a)
    t2=primeFactors(b)
    k1=0
    k3=0
    for i in t1:
        if i in t2:
            h=min(t1[i],t2[i])
            t1[i]-=h
            t2[i]-=h
            k3+=h
        k1+=t1[i]
    k2=0
    for i in t2:
        k2+=t2[i]
    t=True
    if k1 == 0 and k2 == 0:
        ma=2*k3
        mi=0
        if k == 1:
            sys.stdout.write("NO" + "\n")
            t=False
    elif k1 != 0 and k2 != 0:
        mi=2
        ma=k1+k2+2*k3
    else:
        mi=1
        ma=k2+2*k3+k1
    if t:
        if mi<=k<=ma:
            sys.stdout.write("YES" + "\n")
        else:
            sys.stdout.write("NO" + "\n")