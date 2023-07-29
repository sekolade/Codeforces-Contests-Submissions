from math import ceil
for _ in range(int(input())):
    n,m=map(int,input().split())
    MAX=ceil(m/2)
    dd={i:[] for i in range(1,n+1)}
    p=[]
    for i in range(m):
        t=list(map(int,input().split()))
        uz=t[0]
        p.append(set())
        for a in range(1,uz+1):
            el=t[a]
            dd[el].append(i)
            p[-1].add(el)
    for i in dd:
        el=dd[i]
        c=[]
        for a in el:
            le=len(p[a])
            c.append((le,a))
        c.sort(reverse=True)
        for a in range(len(c)-MAX):
            tek,ind=c[a]
            p[ind].remove(i)
    ans=[]
    f=True
    for i in p:
        if len(i) == 0:
            f=False
            print("NO")
            break
        else:
            ans.append(next(iter(i)))
    if f:
        print("YES")
        print(*ans)