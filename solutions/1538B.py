for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    k=sum(l)
    if k % n != 0:
        print(-1)
    else:
        p=0
        ort=k//n
        for i in l:
            if i > ort:
                p+=1
        print(p)