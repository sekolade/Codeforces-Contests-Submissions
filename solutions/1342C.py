from math import gcd
import io,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
def lcm(a, b):
    return abs(a*b) // gcd(a, b)
for _ in range(int(input())):
    a,b,q=map(int,input().split())
    l=[]
    for i in range(q):
        l.append(list(map(int,input().split())))
    fr1,fr2=lcm(a,b),max(a,b)
    for s,e in l:
        ans=0
        t1=(s//fr1 +(1 if s % fr1 != 0 else 0))*fr1
        t2=t1-fr1
        if t1 < e:
            kk=max(s,fr2+t2)
            ans+=t1-kk
            t3=(e//fr1 + (1 if e % fr1 != 0 else 0 ))*fr1
            t4=t3-fr1
            if e % fr1 == 0:
                e-=1
            tt=e-(fr2+t4)
            if tt >=0:
                ans+=tt+1
            ans+=((t4-t1)//fr1)*(fr1-fr2)
 
        else:
            if e % fr1 == 0:
                e-=1
            kk=max(s,fr2+t2)
            kk2=min(e,t1-1)
            ans+=max(kk2-kk+1,0)
        print(ans,end=" ")
    print()