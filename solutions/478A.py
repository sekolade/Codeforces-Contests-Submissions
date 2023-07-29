t=list(map(int,input().split()))
k=sum(t)/len(t)
if sum(t) >0:
    if k.is_integer():
        print(int(k))
    else:
        print(-1)
else:
    print(-1)