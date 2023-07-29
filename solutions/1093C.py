n=int(input())
l=list(map(int,input().split()))
r=[0]*n

r[0]=0
r[-1]=l[0]
k=-1
p=1
for ii in range(1,len(l)):
    i=l[ii]
    low =r[p-1]
    high=i-low
    if high > r[k]:
        t=high-r[k]
        low+=t
        high-=t
    r[p]=low
    p+=1
    r[k-1]=high
    k-=1
print(*r)