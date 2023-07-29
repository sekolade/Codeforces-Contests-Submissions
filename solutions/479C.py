a=int(input())
l=[]
for _ in range(a):
    l.append(tuple(map(int,input().split())))
l.sort()


k=min(l[0])
for i in range(1,a):
    x,y=l[i]
    t=min(x,y)
    if t == x:
        if t >= k:
            k=t
        else:
            k=y
    else:
        if t>=k:
            k=t
        else:
            k=x
print(k)