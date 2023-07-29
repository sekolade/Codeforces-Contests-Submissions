from math import ceil
for _ in range(int(input())):
    h,g,b=map(int,input().split())
    n=ceil(h/2)
    per=g+b
    tam=n//g
    res=(g+b)*tam
    kal=n-(g)*tam
    if tam > 0:
        if kal > 0:
            ans=res+kal
        else:
            ans=res-b
    else:
        ans=h
    print(max(ans,h))