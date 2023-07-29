a,b=map(int,input().split())
l=list(map(int,input().split()))
e=s=best=0
while e<a:
    if s == e:
        if l[s] <= b:
            top=l[s]
            e+=1
        else:
            s=e=s+1
    elif s < e:
        if top + l[e] <=b:
            top+=l[e]
            e+=1
        else:
            best=max(best,e-s)
            top-=l[s]
            s+=1


best=max(best,e-s)
print(best)