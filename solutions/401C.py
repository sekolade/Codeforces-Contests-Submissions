import sys
input=sys.stdin.readline
n,m=map(int,input().split())
if 2*(n+1) < m:
    print(-1)
elif (n-1)> m:
    print(-1)
else:
    t1=m//2
    t2=n
    pp=min(t1,t2)
    k="110"*pp
    if pp*2 < m:
        k+="1"*(m-2*pp)
    if pp < n:
        k=k.replace("110","1010",n-pp)
        h=k.count("0")
        if n-h == 1:
            if k[0] == "0":
                print(k+"0")
            else:
                print("0"+k)
        elif n-h == 2:
            print("0"+k+"0")
        else:
            print(k)
    else:
        print(k)