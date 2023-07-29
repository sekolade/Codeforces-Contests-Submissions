for _ in range(int(input())):
    n,m=map(int,input().split())
    l1=[] #satr n
    l2=[] #sutun m
    l=[]
    INF=99**9
    for i in range(n):
        t=list(input())
        l.append(t)
        l1.append(t.count("."))
    for i in range(m):
        l2.append(0)
        for a in range(n):
            t=l[a][i]
            if t == ".":
                l2[-1]+=1

    best=INF
    for i in range(n):
        for a in range(m):
            if l[i][a] == ".":
                r=0
                r+=l2[a]
                r+=l1[i]
                r-=1



            else:
                r=0
                r+=l2[a]
                r+=l1[i]
            best=min(r,best)
    print(best)