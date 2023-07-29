a=int(input())
b=list(map(int,input().split()))
k1=b.count(100)
k2=b.count(200)
k2=k2%2
if k2 == 0:
    if k1%2 == 0:
        print("YES")
    else:
        print("NO")
else:
    if k1 >= 2:
        if (k1-2)%2 == 0:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")