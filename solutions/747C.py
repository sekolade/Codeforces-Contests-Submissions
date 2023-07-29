n,q=map(int,input().split())
l=[[i,0] for i in range(1,n+1)]
for i in range(q):
    s,k,t=map(int,input().split())
    old=[]
    kk=0
    for i in range(n):
        el=l[i]
        if el[1] <= s:
            old.append(i)
            kk+=1
        if kk == k:
            break
    if kk == k:
        top=0
        for ind in old:
            l[ind][1]=s+t
            top+=l[ind][0]
        print(top)
    else:
        print(-1)