for _ in range(int(input())):
    n=int(input())
    l=list(input())
    pas=[]
    t1=0
    t2=0
    dd={}
    for i in range(len(l)):
        el=l[i]
        if el == "D":
            t1+=1
        else:
            t2+=1
        if t1 == 0:
            if -1 not in dd:
                dd[-1]=[i]
            else:
                dd[-1].append(i)
            #kkkk
        elif t2 == 0:
            if -2 not in dd:
                dd[-2]=[i]
            else:
                dd[-2].append(i)
            #dddd
        else:
            c=t1/t2
            if c not in dd:
                dd[c]=[i]
            else:
                dd[c].append(i)
    res=[0]*(n)
    for i in dd:
        k=dd[i]
        for a in range(len(k)):
            res[k[a]]=a+1
    print(*res)