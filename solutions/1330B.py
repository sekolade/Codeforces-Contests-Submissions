for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    t=set()
    px=0
    ma=-1
    left=set()
    while px < n:
        old=len(t)
        t.add(l[px])
        if len(t) > old:
            ma=max(l[px],ma)
            if ma == len(t):
                left.add(px)
                px+=1
            else:
                px+=1
        else:
            break
    t=set()
    px=-1
    ma=-1
    right=set()
    while px >= -n :
        old=len(t)
        t.add(l[px])
        if len(t)>old:
            ma=max(l[px],ma)
            if ma == len(t):
                right.add(n+px)
                px-=1
            else:
                px-=1
        else:
            break
    res=0
    ans=[]
    for i in left:
        t1=i+1
        t2=n-t1
        ar=n-t2
        if ar in right:
            res+=1
            ans.append((t1,t2))
    print(res)
    for i in ans:
        print(*i)