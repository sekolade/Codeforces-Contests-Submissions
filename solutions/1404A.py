for _ in range(int(input())):
    n, k = map(int, input().split())
    l = list(input())
    f = True
    dd = {i: -1 for i in range(k)}
    for i in range(n):
        try:
            l[i] = int(l[i])
        except:
            pass
    for i in range(k):
        dd[i] = l[i]
    pe = 0 + k
    while pe < n:
        h = pe % k
        if l[pe] == "?":
            if dd[h] == "?":
                pass
            else:
                pass
        else:
            if dd[h] == "?":
                dd[h] = l[pe]
            else:
                if dd[h] != l[pe]:
                    f = False
                    break
        pe += 1
    if not f:
        print("NO")
    else:
        p = list(dd.values())
        ssc = p.count(0)
        bbc = p.count(1)
        sc = k // 2 - ssc
        bc = k // 2 - bbc
        if sc < 0 or bc < 0:
            print("NO")
        else:
            kk = p.count("?")
            if kk == sc + bc:
                print("YES")
            else:
                print("NO")