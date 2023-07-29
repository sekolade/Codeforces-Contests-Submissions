for _ in range(int(input())):
    a,b,c=map(int,input().split())
    k,l=divmod(c,a)
    if l == 0:
        t=(a-1)*b
        t+=k
        print(t)
    else:
        t=(l-1)*b
        t+= k+1
        print(t)