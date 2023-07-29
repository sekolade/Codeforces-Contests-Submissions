from itertools import product
n,m=map(int,input().split())
l=[]
satir={i:[] for i in range(n)}
sutun={i:[] for i in range(m)}
for i in range(n):
    l.append(list(input()))
g=[["."]*m for _ in range(n)]
for i in range(n):
    for a in range(m):
        if l[i][a] == "#":
            satir[i].append(a)
            sutun[a].append(i)

for i in satir:
    sa=set()
    sa.add(i)

    su=set()
    for a in satir[i]:
        su.add(a)
        for k in sutun[a]:
            sa.add(k)
    res=product(sa,su)
    for a,b in res:
        g[a][b]="#"
if g==l:
    print("Yes")
else:
    print("No")