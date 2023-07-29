for _ in range(int(input())):
    k=int(input())
    l1=list(map(int,input().split()))
    sifir=0
    bir=0
    iki=0
    n=0
    for k in l1:
        if k %3 == 0:
            sifir+=1
        elif k%3 == 1:
            bir+=1
        else:
            iki+=1
    each=int(len(l1)/3)
    l2=[each-sifir,each-bir,each-iki]

    while len(set(l2)) != 1:
        if l2[0] >0:
            for x in range(l2[0]):
                l2[2]+=1
                l2[0]-=1
                n+=1
        if l2[1] >0:
            for x in range(l2[1]):
                l2[0]+=1
                l2[1]-=1
                n+=1
        if l2[2] >0:
            for x in range(l2[2]):
                l2[1]+=1
                l2[2]-=1
                n+=1
    print(n)