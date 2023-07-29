from itertools import permutations
n=int(input())
l=list(map(int,input().split()))
d={}
d2={}
res=[]
c=0
def bf(x,indeks=0):
    global c
    if c < 3:
        if indeks == le:
            for i in res:
                print(*i,end=" ")
            print()
            c+=1
        else:
            for i in permutations(x[indeks],len(x[indeks])):
                res.append(i)
                bf(x,indeks+1)
                res.pop()
                if c >= 3:
                    break
for i in range(len(l)):
    try:
        d[l[i]].append(i+1)
        d2[l[i]]+=1
    except:
        d[l[i]]=[i+1]
        d2[l[i]]=1

r=1
for i in d2.values():
    r*=i
if r < 3:
    print("NO")
else:
    print("YES")
    p=dict(sorted(d.items(), key=lambda item: item[0]))
    k=list(p.values())
    le=len(k)
    bf(k)