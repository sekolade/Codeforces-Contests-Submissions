n=int(input())
l=list(map(int,input().split()))
mem=[[0]*n for i in range(n)]
aa=l.count(1)
best=-1
for s in range(n):
    for e in range(s,n):
        if s == e:
            mem[s][e]=(-1 if l[s] == 1 else 1)
        else:
            mem[s][e]=mem[s][e-1] + (-1 if l[e]== 1 else 1)
        best=max(best,mem[s][e])
print(aa+best)