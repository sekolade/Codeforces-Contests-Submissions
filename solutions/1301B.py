import io,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    mi=99**9
    ma=-5
    for i in range(n-1):
        if l[i] != -1 and l[i+1] == -1:
            mi=min(mi,l[i])
            ma=max(ma,l[i])
        elif l[i] != -1 and l[i+1] != -1:
            pass
        elif l[i] == -1 and l[i+1] != -1:
            mi=min(mi,l[i+1])
            ma=max(ma,l[i+1])
        elif l[i] == -1 and l[i+1] == -1:
            pass
    if ma == -5:
        print(0,1)
    else:
        k=(mi+ma)//2
        res=-5
        for i in range(n-1):
            res=max(res,abs((l[i] if l[i] != -1 else k) - (l[i+1] if l[i+1] != -1 else k)))
        print(res,k)