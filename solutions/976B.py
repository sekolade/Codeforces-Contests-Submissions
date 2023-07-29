n,m,k=map(int,input().split())

if k < n:
    print(1+k,1)
elif n<=k<m+n-1:
    print(n,k-n+2)
else:
    s=[n,m]

    k-=(m+n-1-1)
    h=k
    k//=m-1
    if k > 0:
        if k % 2 == 0:
            s[0]-=k
            s[1]=m
        else:
            s[0]-=k
            s[1]=2
    h%=m-1

    if h > 1:
        s[0]-=1
        if s[1] == m:
            s[1]-=h-1

        else:
            s[1]+=h-1
    elif h > 0:
        s[0]-=1
    print(*s)