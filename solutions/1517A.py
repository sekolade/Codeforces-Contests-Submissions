for _ in range(int(input())):
    k=int(input())
    t=list(map(int,list(str(k//2050))))
    c=0
    for i in range(len(t)):
        c+=(10**(len(t)-i-1))*t[i]*2050
    if c == k:
        print(sum(t))
    else:
        print(-1)