for _ in range(int(input())):
    n,k=(map(int,input().split()))
    r=pow(n,0.5)
    r=int(r)
    if(n%2 and k%2 and k<=r):
        print("YES")
    elif n%2==0 and k%2==0 and k<=r:
        print("YES")
    else:
        print("NO")