import io,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
h,w=map(int,input().split())
lh=list(map(int,input().split()))
lw=list(map(int,input().split()))
flag=True
gr=[]
MOD=10**9+7
for a in range(len(lh)):
    i=lh[a]
    end_ind=i-1
    gr.append([1]*i+[0]*(w-i))
    if end_ind+1 < w:
        gr[-1][end_ind+1]=2
for a in range(len(lw)):
    i=lw[a]
    end_ind=i-1
    for k in range(i):
        if gr[k][a] == 1:
            pass
        elif gr[k][a] == 2:
            flag=False
            break
        else:
            gr[k][a]=1

    if end_ind+1 < h:
        if gr[end_ind+1][a] == 1:
            flag=False
            break
        elif gr[end_ind+1][a] == 2:
            pass
        else:
            gr[end_ind+1][a]=2
        gr[end_ind+1][a]=1
if flag:
    res=0
    for y in range(h):
        for x in range(w):
            if gr[y][x] == 0:
                res+=1
                res%=MOD
    print((2**res)%(10**9+7))
else:
    print(0)