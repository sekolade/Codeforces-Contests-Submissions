for _ in range(int(input())):
    a=int(input())
    l=list(map(int,input().split()))
    k=sorted(l)
    for i in range(a-1):
        if k[i] != k[i+1]:
            if i == 0:
                print(l.index(k[i])+1)
            else:
                print(l.index(k[i+1])+1)