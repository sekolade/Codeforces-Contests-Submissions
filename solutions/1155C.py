import io,os,sys
from functools import reduce

input = input


def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

n,m=map(int,input().split())
ev=list(map(int,input().split()))
ala=list(map(int,input().split()))

dif=[]

for i in range(n-1):
    dif.append(ev[i+1]-ev[i])
g = lambda a,b:a if b==0 else g(b,a%b)
gcd= (reduce(lambda x,y:g(x,y),dif))

flag=True



for ii in range(len(ala)):
    i=ala[ii]
    if gcd % i == 0:
        sys.stdout.write(str("YES") + "\n")
        sys.stdout.write(str(ev[0]) + " ")
        sys.stdout.write(str(ii+1) + "\n")
        flag=False
        break
if flag:
    sys.stdout.write(str("NO") + "\n")