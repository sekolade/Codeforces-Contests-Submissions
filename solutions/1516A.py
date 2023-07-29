t = int(input())
for kkk in range(t):
    [n,k] = [int(i) for i in input().split()]
    l = [int(i) for i in input().split()]
    for i in range(n-1):
        if l[i]>=k:
            l[i]-=k
            l[-1]+=k
            break
        l[-1]+=l[i]
        k-=l[i]
        l[i]=0
    for i in l:
        print(i," ",sep="",end="")
    print("")