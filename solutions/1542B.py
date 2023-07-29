for _ in range(int(input())):
    n, a, b = map(int, input().split())
    f = False
    c = False
    if b == 1:
        print("Yes")
    else:
        if a != 1 and b != 1:
            c = True
        elif a == 1 and b != 1:
            if (n - 1) % b == 0:
                print("Yes")
                f = True
        elif b == 1 and a != 1:
            c = True
        else:
            print("Yes")
            f = True
        if c:
            k = 0
            h = pow(a, k)
            while h <= n:
                if (n - h) % b == 0:
                    print("Yes")
                    f = True
                    break
                else:
                    k += 1
                    h = pow(a, k)
        if not f:
            print("No")