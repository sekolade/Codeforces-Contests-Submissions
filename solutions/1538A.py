for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    k=min(l)
    kk=l.index(k)
    p=max(l)
    pp=l.index(p)
    if kk < pp:
        t1=kk
        t2=pp-kk-1
        t3=n-pp-1

    else:
        t1=pp
        t2=kk-pp-1
        t3=n-kk-1
    print(min(t1+min(t2,t3),t3+min(t1,t2))+2)