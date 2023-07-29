n,k=map(int,input().split())
l11=[]
l10=[]
l01=[]
l00=[]
for i in range(n):
    a,b,c=map(int,input().split())
    if b == 1 and c == 1:
        l11.append(a)
    elif b==1 and c == 0:
        l10.append(a)
    elif b == 0 and c == 1:
        l01.append(a)
    else:
        l00.append(a)
l11.sort()
l10.sort()
l01.sort()
l00.sort()
px=0
px2=0
alice=k
bob=k
ans=0

while px < len(l11) and px2 < len(l10) and px2 < len(l01):
    if alice <= 0 and bob <= 0:
        break
    p1=l11[px]
    p2=l10[px2]+l01[px2]
    if p1 < p2:
        ans+=p1
        alice-=1
        bob-=1
        px+=1
    else:
        ans+=p2
        alice-=1
        bob-=1
        px2+=1
if alice <= 0 and bob<= 0:
    print(ans)
else:
    if px == len(l11):
        while px2 < len(l10) and px2 < len(l01):
            if alice <= 0 and bob <= 0:
                break
            p2=l10[px2]+l01[px2]
            ans+=p2
            alice-=1
            bob-=1
            px2+=1
        if alice <= 0 and bob<= 0:
            print(ans)
        else:
            print(-1)
    elif px2 == len(l10) or px2 == len(l01):
        while px < len(l11):
            if alice <= 0 and bob <= 0:
                break
            p1=l11[px]
            ans+=p1
            alice-=1
            bob-=1
            px+=1
        if alice <= 0 and bob<= 0:
            print(ans)
        else:
            print(-1)