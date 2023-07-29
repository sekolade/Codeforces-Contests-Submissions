import io,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
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
n,m=map(int,input().split())
adj=[[] for i in range(n+1)]
edge_co={i:0 for i in range(1,n+1)}
for i in range(m):
    s,e=map(int,input().split())
    adj[s].append(e)
    adj[e].append(s)
    edge_co[s]+=1
    edge_co[e]+=1
visited=[0]*(n+1)
@bootstrap
def dfs(node):
    if visited[node]:
        yield
    visited[node]=1
    for i in adj[node]:
        yield dfs(i)
    res.append(node)
    yield
ans=0
for i in range(1,n+1):
    if visited[i] == 0:
        res=[]
        dfs(i)
        f=True
        for i in res:
            if edge_co[i] != 2:
                f=False
                break
        if f:
            ans+=1
print(ans)