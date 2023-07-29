import io,os,sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    dd={}
    for i in l:
        try:
            dd[i]+=1
        except:
            dd[i]=1
    kk=sorted(dd.values())
    res=0
    old=kk[-1]
    px=-1
    while px >=-len(kk) and old >0:
        el=kk[px]
        if el >= old:
            res+=old
            px-=1
        old-=1
    sys.stdout.write(str(res) + "\n")