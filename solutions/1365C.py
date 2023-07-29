
n=int(input())
fp=list(map(int,input().split()))
sp=list(map(int,input().split()))
ffp= {fp[i]:i for i in range(n)}
ssp={sp[i]:i for i in range(n)}
dd={}
for i in range(1,n+1):
    el1,el1_ind=i,ffp[i]
    el2,el2_ind=i,ssp[i]
    if el1_ind > el2_ind:
        try:
            dd[el2_ind+n-el1_ind]+=1
        except:
            dd[el2_ind+n-el1_ind]=1
    else:
        try:
            dd[el2_ind-el1_ind]+=1
        except:
            dd[el2_ind-el1_ind]=1
print(max(dd.values()))