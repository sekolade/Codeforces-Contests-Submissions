n,m=map(int,input().split())
def check(x,y):
    po=[(x,y),(x+1,y),(x+2,y),(x,y+1),(x,y+2),(x+1,y+2),(x+2,y+1),(x+2,y+2)]
    flag=True
    for x,y in po:
        if g[y][x]== ".":
            flag=False
            break
    if flag:
        for x,y in po:
            l[y][x]="#"
l=[["."]*m for _ in range(n)]
g=[0]*n
for i in range(n):
    t=list(input())
    g[i]=t
for y in range(n-2):
    for x in range(m-2):
        check(x,y)
if l == g:
    print("YES")
else:
    print("NO")