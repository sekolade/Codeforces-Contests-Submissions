for _ in range(int(input())):
    a=int(input())
    l=list(map(int,input().split()))

    t=[]
    for i in range(a):
        t.append((i+1,l[i]))

    t.sort(key=lambda x: x[1])
    t2=[]
    n=0
    for i in t:
        n+=i[1]
        t2.append(n)

    r=1
    p=[t[-1][0]]

    for i in range(a-1,0,-1):

        kucuk=t2[i-1]
        buyuk=t2[i]
        if 2*kucuk >=buyuk:
            r+=1
            p.append(t[i-1][0])
        else:
            break
    print(r)
    print(*sorted(p))