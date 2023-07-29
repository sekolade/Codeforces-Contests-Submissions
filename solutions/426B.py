n,m=map(int,input().split())
l=[]
for i in range(n):
    l.append(list(input()))
if n % 2 != 0:
    print(n)
else:
    start=n
    mid = n//2
    while start != 1:
        if l[0:mid][::-1] == l[mid:start]:
            start//=2
            mid=start//2
        else:
            break
    print(start)