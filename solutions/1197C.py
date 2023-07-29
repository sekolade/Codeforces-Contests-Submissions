n,k=map(int,input().split())
l=list(map(int,input().split()))
top=l[-1]-l[0]
ll=[]
for i in range(n-1):
    ll.append(l[i]-l[i+1])
hak=k-1
ll.sort()
t=sum(ll[:hak])
print(top+t)