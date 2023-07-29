import sys
input=sys.stdin.readline
INF=99**9
n,m,l=map(int,input().split())
ini=[-INF]+list(map(int,input().split()))+[-INF]
r=0
px=0
start=-1
while px<len(ini):
    if ini[px] >l:
        if start == -1:
            start=px
    else:
        if start != -1:
            r+=1
            start=-1
    px+=1
for _ in range(m):
    k=list(map(int,input().split()))
    if k[0] == 0:
        print(r)
    else:
        t,q=k[1],k[2]
        ind=t
        if ini[ind]<=l:
            q1=ini[ind-1]>l
            q2=ini[ind+1]>l
            ini[ind]+=q
            if ini[ind]>l:
                if q1 and q2:
                    r-=1
                elif not q1 and not q2:
                    r+=1