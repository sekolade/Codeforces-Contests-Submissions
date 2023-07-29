def check1(a,b):
    po1=[(i+a,b) for i in range(k)]
    flag=True
    for i in range(k):
        x,y=po1[i][0],po1[i][1]
        if field[y][x]=="#":
            flag=False
            break
    if flag:
        for a in range(k):
            x,y=po1[a][0],po1[a][1]
            t[y][x]+=1
def check2(a,b):
    po1=[(a,b+i) for i in range(k)]
    flag=True
    for i in range(k):
        x,y=po1[i][0],po1[i][1]
        if field[y][x]=="#":
            flag=False
    if flag:
        for a in range(k):
            x,y=po1[a][0],po1[a][1]
            t[y][x]+=1
n,k=map(int,input().split())
field=[]
t=[[0]*n for i in range(n)]
for i in range(n):
    field.append(list(input()))
for x in range(n-k+1):
    for y in range(n):
        check1(x,y)
for x in range(n):
    for y in range(n-k+1):
        check2(x,y)
best=-1
best_cor=[-1,-1]
for x in range(n):
    for y in range(n):
        if t[y][x] > best:
            best=t[y][x]
            best_cor=[y+1,x+1]
print(*best_cor)