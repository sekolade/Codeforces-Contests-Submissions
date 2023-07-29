n,m=map(int,input().split())
flag=True
for i in range(m):
    t=list(map(int,input().split()))
    if flag:
        del t[0]
        p=list(set(t))
        length=len(p)
        kk=set()
        for a in p:
            kk.add(abs(a))
        if len(kk) == length:
            flag=False
            print("YES")
if flag:
    print("NO")