for _ in range(int(input())):
    num=int(input())
    if num % 2 == 0:
        print(*list(range(1,num+1))[::-1])
    else:
        k=list(range(1,num+1))[::-1]
        t=int(num/2)
        k[t],k[-1]=k[-1],k[t]
        print(*k)