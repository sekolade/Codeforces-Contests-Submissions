for _ in range(int(input())):
    n,x,t=map(int,input().split())
    k=t//x
    if k == 0:
        print(0)
    else:
        cc=n-k
        if cc > 0:

            cc*=k
            pp=k-1
            tt=(pp)*(pp+1)//2
            ans=tt+cc
            print(ans)
        else:
            hh=n-1
            ans=(hh)*(hh+1)//2
            print(ans)