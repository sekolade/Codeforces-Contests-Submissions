def den(indeks,t):
    l=[0]*a
    l[0]=1
    while True:
        if sum(l) < b:

            if l[indeks] !=9:

                l[indeks]+=1
            else:
                if t:
                    indeks-=1
                else:indeks+=1
        elif sum(l) == b:
            print(*l," ",sep="",end="")

            break

a,b=map(int,input().split())
if (a,b)==(1,0):
    print(0,0)
elif b == 0:
    print(-1,-1)
elif a*9 < b:
    print(-1,-1)
else:
    den(a-1,1)
    den(0,0)