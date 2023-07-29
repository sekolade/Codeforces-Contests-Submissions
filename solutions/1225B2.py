for _ in range(int(input())):
    n,k,d=map(int,input().split())
    l=list(map(int,input().split()))
    dict={}
    t=set()
    for i in range(d):
        eleman=l[i]
        t.add(eleman)
        try:
            dict[eleman]+=1
        except:
            dict[eleman]=1
    best=len(t)
    p=d
    kk=0
    while p < n:
        pre=l[kk]
        if dict[pre] >1:
            dict[pre]-=1
        else:
            t.remove(pre)
            dict[pre]-=1
        t.add(l[p])
        try:
            dict[l[p]]+=1
        except:
            dict[l[p]]=1
        best=min(best,len(t))
        p+=1
        kk+=1

    print(best)