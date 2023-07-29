for _ in range(int(input())):
    x=int(input())
    l1=list(map(int,input().split()))
    y=len(l1)
    ac=True
    for k in range(len(l1)):
        c=sum(l1[0:k+1])
        y=len(l1[0:k+1])
        z=y-1
        d= int((z*(z+1))/2)
        if c < d:
            ac = False

    if ac:
        print("YES")
    else :print("NO")