for _ in range(int(input())):
    n = int(input())
    l1 = []
    ll1 = []
    l2 = []
    ll2 = []
    for i in range(n):
        a, b = map(int, input().split())
        l1.append(a)
        ll1.append(a)
        l2.append(b)
        ll2.append(b)
    l1.sort()
    l2.sort()
    if len(l1) % 2 != 0:
        t1 = 1
    else:
        t1 = l1[len(l1) // 2] - l1[len(l1) // 2 - 1] + 1
    if len(l2) % 2 != 0:
        t2 = 1
    else:
        t2 = l2[len(l2) // 2] - l2[len(l2) // 2 - 1] + 1
    ans = t1 * t2
    print(ans)