import io,os,sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
for _ in range(int(input())):
    n=int(input())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    tt=[]+[(l1[i],l2[i]) for i in range(n)]
    tt.sort()
    px = -1
    old=tt[-1][0]
    rp=0
    flag=True
    while px >= -n +1:
        k=tt[px][1]
        t=max(tt[px-1][0],rp+k)
        if t <= old:
            rp+=k
            px-=1
            old=t
        else:
            flag=False
            sys.stdout.write(str(old) + "\n") # == > print(n)
            break
    if flag:
        sys.stdout.write(str(min(old,rp+tt[0][1])) + "\n")