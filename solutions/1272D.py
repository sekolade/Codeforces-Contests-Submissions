n=int(input())
l=list(map(int,input().split()))
ll=[1]
for i in range(1,n):
    if l[i] > l[i-1]:
        ll[-1]+=1
    else:
        ll.append(1)
t=0
ans=max(ll)
for i in range(len(ll)-1):
    t+=ll[i]
    if ll[i] != 1:
        end=t-1
        bb=l[end-1]
        kk=l[end+1]
        if bb < kk:
            ans=max(ans,ll[i]+ll[i+1]-1)
    if ll[i+1] != 1:
        end=t
        bb=l[end-1]
        kk=l[end+1]
        if bb < kk:
            ans=max(ans,ll[i]+ll[i+1]-1)
print(ans)