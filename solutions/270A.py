for _ in range(int(input())):
    k=int(input())
    t=180-k
    tt=360/t
    if tt.is_integer():
        print("YES")
    else:
        print("NO")