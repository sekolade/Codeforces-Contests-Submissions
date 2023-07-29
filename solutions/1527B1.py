for _ in range(int(input())):
    n=int(input())

    t=list(map(int,input()))
    k0=t.count(0)
    k1=t.count(1)
    if k0 % 2 == 0:
        print("BOB")
    else:
        if k0 == 1:
            print("BOB")
        else:
            print("ALICE")