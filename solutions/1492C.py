n,m=map(int,input().split())
sn=list(input())
sm=list(input())
dd={}
dd2=set(sm)
px=0
for i in range(len(sm)):
    el=sm[i]
    while px < n:
        c=sn[px]
        if i not in dd and c== el:
            dd[i]=[px,-1]
            px+=1
            break
        px+=1
px=n-1
for i in range(m-1,-1,-1):
    el=sm[i]
    while px > -1:
        c=sn[px]
        if c == el and dd[i][1] == -1:
            dd[i][1]=px
            px-=1
            break
        px-=1
p=0
c=dd[0][0]
best=0
for i in dd:
    p+=1
    if p ==1:
        pass
    elif p == m:
        best=max(best,dd[i][1]-c)
    else:
        best=max(best,dd[i][1]-c)
        c=dd[i][0]
print(best)