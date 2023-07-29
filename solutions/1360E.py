import sys
input=sys.stdin.readline
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
"*******************************************************************"
@bootstrap
def dfs(y,x):
    if 0<=y<=n-1 and 0<=x<=n-1:
        if grid[y][x] == 0:
            yield
        grid[y][x]=0
        yield dfs(y-1,x)
        yield dfs(y,x-1)
    yield
for _ in range(int(input())):
    n=int(input())
    grid=[]
    for i in range(n):
        grid.append(list(map(int,list(input().strip()))))

    for i in range(n):
        p1=grid[i][n-1]
        p2=grid[n-1][i]
        dfs(i,n-1)
        dfs(n-1,i)
    f=True
    for y in range(n):
        for x in range(n):
            if grid[y][x] == 1:
                print("NO")
                f=False
                break
        if f == False:
            break
    if f:
        print("YES")