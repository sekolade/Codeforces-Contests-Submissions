t = int(input())
for i in range(t):
    y=list(map(int,input().split()))
    k=[]
    for i in range(4):
        k.append((y[i],i))
    k.sort()
    c1,c2=k[-1][1],k[-2][1]
    t=[c1,c2]
    if  t == [0,1] or t== [1,0] or t == [2,3] or t==[3,2] :
        print("NO")
    else:
        print("YES")