for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    start=0
    while start < n:
        ll=[(l[i],i) for i in range(n)]
        k=sorted(ll[start:])[0]
        el=k[0]
        ind=k[1]
        ss=ind
        if ind == start:
            start+=1
        else:
            while ind != start:
                l[ind],l[ind-1]=l[ind-1],l[ind]
                ind-=1
            start=ss
    print(*l)