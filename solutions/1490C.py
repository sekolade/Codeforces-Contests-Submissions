for _ in range(int(input())):
    x=int(input())
    kupkok= x**(1/3)

    if float.is_integer(kupkok):
        kupkok=int(kupkok)
    else:
        kupkok= int(kupkok)+1
    y=range(1,kupkok)
    def func():
        for k1 in y:
            c=(x-(k1**3))**(1/3)

            if float.is_integer(c) or c+ 0.000000000005 > int(c)+1:
                print("YES")
                return 0
        return 1


    if func():
        print("NO")