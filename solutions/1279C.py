import io,os,sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
for _ in range(int(input())):
    n,m=map(int,input().split())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    kk=set(l2)
    px2=0
    px1=0
    s=set()
    res=0
    rem=0
    while px2 < m:
        el=l2[px2]
        if el not in s:
            t=set()
            for i in range(px1,n):
                if l1[i] != el:
                    t.add(l1[i])
                else:
                    px1=i+1
                    break
            res+=2*px1-1-2*rem
            rem+=1
            k=t.intersection(kk)
            for i in k:
                s.add(i)
                kk.remove(i)
            px2+=1
        else:
            res+=1
            rem+=1
            px2+=1
    sys.stdout.write(str(res) + "\n")