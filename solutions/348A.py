n=int(input())
l=list(map(int,input().split()))
t=max(l)
tt=sum(l)
k= tt//(n-1) + (1 if tt % (n-1) != 0 else 0)
if k >= t:
    print(k)
else:
    print(t)