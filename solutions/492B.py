a,b=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
maks=-1
for i in range(a-1):
    maks=max(l[i+1]-l[i],maks)
maks=max(maks/2,l[0],b-l[-1])
print(maks)