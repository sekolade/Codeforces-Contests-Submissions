n,m=map(int,input().split())
l1=set()
l2=set()
for i in range(m):
    k,t=sorted(map(int,input().split()))
    l1.add(k)
    l2.add(t)
if m == 0:
    print(n-1)
else:
    q1,q2=l1.intersection(l2),l1.union(l2)
    if len(q1):
        print(0)
    else:
        maxl=max(l1)
        minh=min(l2)
        if maxl > minh:
            print(0)
        else:
            if len(q2) == n:
                    print(1)
            else:
               t=0
               for i in range(1,n+1):
                   if i not in q2:
                       if minh > i > maxl and i < minh:
                           t+=1
               print(t+1)