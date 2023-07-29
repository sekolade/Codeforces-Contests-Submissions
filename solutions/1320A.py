n=int(input())
l=list(map(int,input().split()))
d={}
for i in range(n):
    try:
        d[l[i]-i].append(i)
    except:
        d[l[i]-i]=[i]
best=0
for i in d:
    res=0
    for a in d[i]:
        res+=l[a]
    best=max(best,res)
print(best)