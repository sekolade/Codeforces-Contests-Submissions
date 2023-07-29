for _ in range(int(input())):
    x,y,a,b=map(int,input().split())
    if a == b:
        print(min(x//a,y//a))
    else:
        t=abs(x-y)
        t2=abs(a-b)
        k1= t//t2
        mi=min(a,b)
        ma=max(a,b)
        miel=min(x,y)
        mael=max(x,y)
        res=0
        k2= miel//mi
        k3= mael//ma
        tt=min(k1,k2,k3)
        miel-=tt*mi
        mael-=tt*ma
        res+=tt

        if k1 == 0:
            if abs(t2-t) < t2:
                if miel-mi>0 and mael-ma>0:
                    res+=1

                    miel-=mi
                    mael-=ma
        tot=mi+ma
        h1=miel//tot
        h2=mael//tot
        hh=min(h1,h2)
        res+=hh*2
        miel-=hh*tot
        mael-=hh*tot
        t1=max(min(mael//ma,miel//mi),min(mael//mi,miel//ma))
        res+=t1
        print(res)