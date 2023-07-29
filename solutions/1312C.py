import io,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

for _ in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    flag=True
    tot=set()
    for i in range(n):
        if flag ==False:
            break
        el=l[i]
        if el == 0:
            continue
        else:
            el_k=el
            el_k_2=el_k
            while el_k>=1:
                if flag == False:
                    break
                p=0
                while el_k>=k:
                    el_k/=k
                    p+=1
                rr=k**p
                kal=el_k_2-rr
                el_k=kal
                el_k_2=el_k
                old=len(tot)
                tot.add(p)
                if len(tot) == old:
                    flag=False
                    break
    if flag:
        print("YES")
    else:
        print("NO")