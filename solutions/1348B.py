for _ in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))

    t=set(l)
    if len(t)>k:
        print(-1)
    else:
        ll=list(t)
        ll+=[1]*(k-len(ll))
        print(len(ll)*n)
        for i in range(n):
            print(*ll,end=" ")
    print()