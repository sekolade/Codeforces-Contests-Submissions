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
"********************************************************"
n=int(input())
adj=[[] for i in range(n+1)]
for i in range(n-1):
    s,e=map(int,input().split())
    adj[s].append(e)
    adj[e].append(s)

po=[0]*(n+1)
po[0]=1
@bootstrap
def dfs(node,old,kkk,dist):
    global res
    po[node]=po[old]/kkk
    if len(adj[node]) == 1 and adj[node][0] == old:
            res+=dist*po[node]
    else:
        tt=len(adj[node])- (1 if old != 0 else 0)
        for i in adj[node]:
            if i != old:
                yield dfs(i,node,tt,dist+1)
    yield
res=0
dfs(1,0,1,0)
print(res)