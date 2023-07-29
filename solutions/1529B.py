for _ in range(int(input())):
    n=int(input())
    l=sorted(map(int,input().split()))
    poz_say=0
    for i in l:
        if i > 0:
            poz_say+=1
    if poz_say > 0:
        poz_ilk_ind=n-1-(poz_say-1)
        kk=poz_ilk_ind
        gerek=l[kk]
        ans=n-poz_say
        te=1
        for i in range(poz_ilk_ind-1,-1,-1):

            el=l[i]
            fark=abs(l[kk]-el)
            if fark >= gerek:
                te+=1
                kk=i
            else:
                pass
        print(max(ans,te))
    else:
       print(n)