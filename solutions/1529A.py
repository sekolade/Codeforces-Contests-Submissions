for _ in range(int(input())):
    n=int(input())
    l=sorted(map(int,input().split()))
    res=0
    while len(l) >0:
        if l[0] < l[-1]:
            del l[-1]
            res+=1
        else:
            break
    print(res)