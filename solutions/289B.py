n,m,d=map(int,input().split())
l=[]
p=[]
for i in range(n):
    t=list(map(int,input().split()))
    l.append(t)
    for a in t:
        p.append(a)
t=set()
for i in p:
    kal= i % d
    t.add(kal)

if len(t) == 1:
    uz=len(p)
    p.sort()
    ort_ind=uz//2
    res=0
    for i in p:
        res+=abs(i-p[ort_ind])
    print(res//d)
else:
    print(-1)