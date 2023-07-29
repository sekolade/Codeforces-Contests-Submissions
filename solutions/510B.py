from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc
"*********************************************************"
n,m=map(int,input().split())
l=[]
for i in range(n):
    l.append(list(input()))
visited=[[0]*(m) for i in range(n)]
f=True
@bootstrap
def dfs(y,x,oldy,oldx,ch):
    global f
    if f:
        if visited[y][x] != 0:
            yield
        if l[y][x] != ch:
            yield
        visited[y][x]=ch
        if 0<=y+1<n and 0<=x<m and f:
            if (y+1,x) != (oldy,oldx) and visited[y+1][x] == ch and l[y+1][x] == ch:
                print("Yes")
                f=False
            yield dfs(y+1,x,y,x,ch)
        if 0<=y-1<n and 0<=x<m and f:
            if (y-1,x) != (oldy,oldx) and visited[y-1][x] == ch and l[y-1][x] == ch:
                print("Yes")
                f=False
            yield dfs(y-1,x,y,x,ch)
        if 0<=y<n and 0<=x+1<m and f:
            if (y,x+1) != (oldy,oldx) and visited[y][x+1] == ch and l[y][x+1] == ch:
                print("Yes")
                f=False
            yield dfs(y,x+1,y,x,ch)
        if 0<=y<n and 0<=x-1<m and f:
            if (y,x-1) != (oldy,oldx) and visited[y][x-1] == ch and l[y][x-1] == ch:
                print("Yes")
                f=False
            yield dfs(y,x-1,y,x,ch)

    yield
for y in range(n):
    for x in range(m):
        if f:
            if visited[y][x] == 0:
                dfs(y,x,-1,-1,l[y][x])
        else:
            break
if f:
    print("No")