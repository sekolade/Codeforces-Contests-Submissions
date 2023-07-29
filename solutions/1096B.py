n=int(input())
l=list(input())
r=0
# len 0
r+=1
if len(set(l))== 1:
    print(int((n*(n+1))/2)%998244353)
else:
    if l[0] != l[-1]:
        t=l[0]
        flag=True
        flag2=False
        ll=[]
        for i in range(n):
            if flag and l[i] != t:
                ll.append(i)
                flag=False
                flag2=True
            if flag2 and l[i] != t:
                try:
                    ll[1]=i
                except:
                    ll.append(i)
        start=ll[0]

        end=ll[1%(len(ll))]
        start2=start


        t=l[-1]
        flag=True
        flag2=False
        ll=[]
        for i in range(n):
            if flag and l[i] != t:
                ll.append(i)
                flag=False
                flag2=True
            if flag2 and l[i] != t:
                try:
                    ll[1]=i
                except:
                    ll.append(i)
        start=ll[0]
        end=ll[1%(len(ll))]

        end2=len(l)-1-end
        r+=end2+start2
        r%=998244353
    else:
        t=l[0]
        flag=True
        flag2=False
        ll=[]
        for i in range(n):
            if flag and l[i] != t:
                ll.append(i)
                flag=False
                flag2=True
            if flag2 and l[i] != t:
                try:
                    ll[1]=i
                except:
                    ll.append(i)
        start=ll[0]
        start2=start-0+1
        end=ll[1%(len(ll))]
        end2=len(l)-1-end+1
        r+=end2*start2-1
        r%=998244353

    print(r%998244353)