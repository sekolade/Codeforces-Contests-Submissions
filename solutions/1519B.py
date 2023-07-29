for _ in range(int(input())):
    m, n, k = list(map(int, input().split()))
    if m*n - 1 == k:
        print('YES')
    else:
        print('NO')