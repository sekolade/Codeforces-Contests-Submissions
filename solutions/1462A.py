for _ in range(int(input())):
    x=int(input())
    l1=list(map(int,input().split()))
    result=[]
    if len(l1) %2== 0:
        k=int(len(l1)/2)
        l1_2_1=l1[0:k]
        l1_2_2=l1[k:]
        l1_2_2.reverse()
        for a in range(k):
            result.append(l1_2_1[a])
            result.append(l1_2_2[a])


        print(*result)





    else:


        k=int((len(l1)+1)/2)
        l1_2_1=l1[0:k]
        l1_2_2=l1[k:]
        l1_2_2.reverse()

        for a in range(len(l1_2_2)):
            result.append(l1_2_1[a])
            result.append(l1_2_2[a])
        result.append(l1_2_1[-1])

        print(*result)