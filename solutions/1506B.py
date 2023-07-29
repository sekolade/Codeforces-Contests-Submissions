for _ in range(int(input())):
    a,b=map(int,input().split())
    k=list(input())
    if k.count("*") == 1:
        print(1)
    elif k.count("*") ==2:
        print(2)
    else:
        l=[]
        for i in range(a):
            if k[i]=="*":
                l.append(i)
        r=2

        if l[-1]-l[0]<=b:
            print(r)
        else:
            p1=0
            p2=0
            flag=False
            while True:
                while l[p1+1]-l[p2] <=b:
                    p1+=1
                    if p1 == len(l)-1:
                        flag=True
                        break



                p2,p1=p1,p1

                if flag:
                    break
                else:
                    r+=1

            print(r)