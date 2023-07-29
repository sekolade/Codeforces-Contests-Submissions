
for _ in range(int(input())):
    x=int(input())

#1 2 3 4 5 6 7 8 9


#49
    if x > 45:
        print(-1)
    else:



        l1=[9,17,24,30,35,39,42,44,45]
        for k in l1:
            if k >=x:
                c=l1.index(k)
                break
        n=9
        result=[]
        for a in range(c):
            result.append(n)
            n-=1

        kk=x-sum(result)
        result.reverse()
        result.insert(0,kk)
        print(*result,sep="")