import io,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
for _ in range(int(input())):
    n,m=map(int,input().split())
    l=[]
    for i in range(n):
        l.append(list(map(int,input().split())))
    l.sort()
    px=0
    f=True
    old=0
    ran=[m,m]
    while px < n and f:
        kk=l[px][0]-old
        left=ran[0]-kk
        right=ran[1]+kk
        if l[px][1] > right or l[px][2] < left:
            print("NO")
            f=False
            break
        else:
            new_left=max(left,l[px][1])
            new_right=min(right,l[px][2])
            ran=[new_left,new_right]
            old=l[px][0]
            px+=1
    if f:
        print("YES")