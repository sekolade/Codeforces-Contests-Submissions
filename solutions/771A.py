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
import io,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
"**************************************************"
n,m=map(int,input().split())
adj=[[] for i in range(n+1)]
for i in range(m):
    s,e=map(int,input().split())
    adj[s].append(e)
    adj[e].append(s)
@bootstrap
def dfs(node):
    global res,cou
    if visited[node]:
        yield
    res+=len(adj[node])
    cou+=1
    visited[node]=1
    for i in adj[node]:
        yield dfs(i)
    yield
visited=[0]*(n+1)
f=True
for a in range(1,n+1):
    if visited[a] == 0:
        cou=0
        res=0
        dfs(a)
        if cou*(cou-1) != res:
            print("NO")
            f=False
            break
if f:
    print("YES")