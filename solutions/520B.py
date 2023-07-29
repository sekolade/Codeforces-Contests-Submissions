from math import log,ceil
c,d=map(int,input().split())
a=2**ceil(log(d/c,2))
b=a*c-d
if c<d:
    t=0
    while a!=0 and b!=0 :
        if (a/2).is_integer() and (b/2).is_integer():
            a/=2
            b/=2
        else:
            b-=1
        t+=1
    print(int(b+t+log(a,2)))
else:
    print(c-d)