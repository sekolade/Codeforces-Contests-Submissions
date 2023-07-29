for _ in range(int(input())):
    x,y,z=list(map(int,input().split()))
    n=0
    while True:
        if x%2 == 0:

            n+=1
            x= int(x/2)

        else:break
    while True:
        if y%2 == 0:

            n+=1
            y= int(y/2)

        else:break

    tt= 2**n


    if tt >= z :
        print("yes")
    else:print("no")