for _ in range(int(input())):
    a,b=map(int,input().split())
    r=0
    if a==b:
        t=a//3
        l=a%3
        if l == 2:
            print(2*t+1)
        else:
            print(2*t)
    elif a > b:
        fark=a-b
        r+=fark
        a-=2*fark
        b-=fark
        if a == 0:
            print(r)
        elif a >0:
            t=a//3
            l=a%3
            if l == 2:
                print(2*t+1+r)
            else:
                print(2*t+r)
        else:
            u=-b
            print(r-u)






    else:
        fark=b-a
        r+=fark
        a-=fark
        b-=2*fark
        if a == 0:
            print(r)
        elif a >0:
            t=a//3
            l=a%3
            if l == 2:
                print(2*t+1+r)
            else:
                print(2*t+r)
        else:
            u=-a
            print(r-u)