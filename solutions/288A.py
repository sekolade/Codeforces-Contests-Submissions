n,k=map(int,input().split())
ascii="abcdefghijklmnopqrstuvwxyz"
if k > n :
    print(-1)
elif n == 1 and k == 1:
    print("a")
elif n != 1 and k == 1:
    print(-1)
else:
    t1=k-2
    t2=n-t1
    tam=t2//2
    kal=t2%2
    r="ab"*tam+"a"*kal
    for i in range(t1):
        i+=2
        r+=ascii[i]
    print(r)