for _ in range(int(input())):
    x=int(input())
    l1=list(map(int,input().split()))
    n=0
    for k in range(len(l1)-1):
        maxx=max(l1[k],l1[k+1])
        minn=min(l1[k],l1[k+1])
        if maxx > minn*2:


            while not maxx <= minn*2:
                maxx = maxx/2
                n+=1
    print(n)