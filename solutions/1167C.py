from types import GeneratorType
import io,os,sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
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


n,m=map(int,input().split())
adj=[[] for i in range(n+1)]
for i in range(m):
    t=list(map(int,input().split()))
    for a in range(1,t[0]+1-1):
        s,e=t[a],t[a+1]
        adj[s].append(e)
        adj[e].append(s)
@bootstrap
def dfs(node,old):
    global ma
    if visited[node]:
        yield
    visited[node]=1
    ma=old+1
    visits.append(node)
    for i in adj[node]:
        yield dfs(i,ma)
    yield
visited=[0]*(n+1)
dist=[0]*(n+1)
for i in range(1,n+1):
    if visited[i] == 0:
        ma=0
        visits=[]
        dfs(i,ma)
        for a in visits:
            dist[a]=ma
for i in range(1,n+1):
    print(dist[i],end=" ")