
a=int(input())
l=list(map(int,input().split()))

t1=min(l)
t2=max(l)
if t1 == t2:
    print(0,int((a*(a-1))/2))
else:

    n1=l.count(t1)
    n2=l.count(t2)
    print(t2-t1,n1*n2)