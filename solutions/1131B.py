n=int(input())
l=[[0,0]]
for _ in range(n):
    l+=[list(map(int,input().split()))]
r=1
for i in range(n):
    k=max(l[i][0],l[i][1])
    t=min(l[i+1][0],l[i+1][1])
    k = k+1 if l[i][0]==l[i][1] else k
    r = r+t-k+1 if t>=k else r
print(r)