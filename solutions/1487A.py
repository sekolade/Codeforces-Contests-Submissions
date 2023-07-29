for _ in range(int(input())):
    x=int(input())
    y=list(map(int,input().split()))
    y_set=set(y)
    n=0
    for k in y_set:
        t=y.count(k)
        if k != min(y):
            n+= t
    print(n)