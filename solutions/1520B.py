for _ in range(int(input())):
    n=int(input())
    kk=str(n)
    digit=len(kk)
    result=9*(digit-1)
    ilk=int(kk[0])-1
    result+=int(ilk)


    bas=kk[0]
    if int(bas*digit) <= n:
        result+=1
    print(result)