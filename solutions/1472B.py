for _ in range(int(input())):
    x=int(input())
    y=list(map(int,input().split()))
    if sum(y) % 2 !=0:
        print("NO")
    else:
        if y.count(2) %2 == 0 :
            print("YES")
        else:
            if y.count(1) >0:
                print("YES")
            else:
                print("NO")