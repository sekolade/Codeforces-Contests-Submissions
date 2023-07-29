INF=99**9
p,x,y=map(int,input().split())
kat_x=x//50
kat_y=y//50
kat_high=999999990
if y > x:
    t=-1
    res=-1
    for i in range(kat_y,kat_high):
        if res>0:
            break
        t+=1
        k=i%475
        for _ in range(25):
            k=(k*96+42)%475
            if k +26 == p:
                res=t
                break

    print((res-kat_x+1)//2)
else:
    t=-1
    res=INF
    if x % 50 < y % 50: kat_y+=1
    for i in range(kat_x,kat_y-1,-1):
        if res!= INF:
            break
        t+=1
        k=i%475
        for _ in range(25):
            k=(k*96+42)%475
            if k +26 == p:
                res=t
                print(0)
                break
    t=-1
    if res == INF:
        pp=True
        for i in range(kat_x,kat_high):
            if pp == False:
                break
            t+=1
            k=i%475
            for _ in range(25):
                k=(k*96+42)%475
                if k +26 == p:
                    res=min(res,t)
                    pp=False
                    break
        print((res+1)//2)