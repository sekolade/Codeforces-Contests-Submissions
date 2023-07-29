import sys
input=sys.stdin.readline
for _ in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    ll={}
    for i in l:
        t=i%k
        if t != 0:
            try:
                ll[t]+=1
            except:
                ll[t]=1
    if ll:
        hh=dict(sorted(ll.items(), key=lambda item: item[1],reverse=True))
        qq=next(iter(hh))
        q=hh[qq]
        pp=[]
        for i in hh:
            if hh[i] ==q:
                pp.append(i)
        pp.sort()
        res=(q-1)*k+k-pp[0]+1
        print(res)
    else:
        print(0)