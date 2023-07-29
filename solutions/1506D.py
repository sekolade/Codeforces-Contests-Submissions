from heapq import *
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    q=[]
    heapify(q)
    dd={}
    for i in l:
        try:
            dd[i]+=1
        except:
            dd[i]=1
    for i in dd:
        el=-dd[i]
        heappush(q,el)
    while True:
        if len(q) == 1:
            k1=heappop(q)
            print(-k1)
            break
        else:
            k1=heappop(q)
            k2=heappop(q)
            if k1 != 0 and k2 != 0:
                k1+=1
                k2+=1
                heappush(q,k1)
                heappush(q,k2)
            elif k1 == 0 and k2 == 0:
                print(0)
                break
            else:
                print(-min(k1,k2))
                break