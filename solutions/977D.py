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

"-------------------------------------------------------------------------"

n=int(input())
l=list(map(int,input().split()))
@bootstrap
def dfs(node,old):
    global flag
    if flag:
        if node not in dd:
            yield
        distances[node]=distances[old]+1
        path[node]=old
        if distances[node] ==n:
            res.append(node)
            flag=False
            yield
        yield dfs(2*node,node)
        if node % 3 == 0:
            yield dfs(node//3,node)
    yield
flag2=True
for i in range(n):
    res=[]
    flag=True
    el=l[i]
    path={}
    distances={}
    path[el]=-1
    dd={l[i]:0 for i in range(n)}
    distances[el]=0
    res2=[0]*n
    dfs(el,el)
    if len(res) > 0:
        end=res[0]
        k=-1
        while path[end] != end:
            res2[k]=int(end)
            end=path[end]
            k-=1
        res2[k]=int(end)
        print(*res2)
        flag2=False
        break
if flag2:
    print("q")