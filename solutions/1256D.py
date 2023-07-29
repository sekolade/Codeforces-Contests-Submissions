for _ in range(int(input())):
    n,k=map(int,input().split())
    t=list(map(int,input()))
    l=[]
    for i in range(n):
        if t[i] == 0:
            l.append(i)
    p=0
    top=k
    res=[1]*n
    for i in range(len(l)):
        ind=i
        i=l[i]
        if top-(i-p)>=0:
            l[ind]=p
            top-=i-p
            p+=1

        else:
            new=i-top
            l[ind]=new
            break
    for i in l:
        res[i]=0
    print(*res,sep="")