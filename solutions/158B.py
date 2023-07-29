a=int(input())
l=list(map(int,input().split()))
dort=l.count(4)
uc=l.count(3)
iki=l.count(2)
bir=l.count(1)
r=dort




uc_bir=min(uc,bir)
r+=uc_bir
uc-=uc_bir
bir-=uc_bir


iki_iki=int(iki/2)
r+=iki_iki
iki-=iki_iki*2


if iki > 0 and bir > 1:
    k=min(int(bir/2),iki)
    r+=k
    bir-=k*2
    iki-=k
if bir  == 0:
    print(r+iki+uc)

elif uc == 0:
    if iki  == 0:
        tt=divmod(bir,4)
        r+=tt[0]

        if tt[1] == 0:
            print(r)
        else:
            print(r+1)
    else:
        if bir == 0:
            print(r+iki)
        else:
            print(r+iki)