n,k=map(int,input().split())
j =n%(2*k+1)
t=n//(2*k+1)
start=k+1
if k+1 <= j <= 2*k:
    j= k+1-j
    j-=1
    print(t+1)
    for _ in range(t):
        print(start,end=" ")
        start+=2*k+1
    print(n+1+j)
elif 0<j<k+1:
    h=k+1-j
    j=-1
    start-=h
    print(t+1)
    for _ in range(t):
        print(start,end=" ")
        start+=2*k+1
    print(n+1+j)
else:
    print(t)
    for _ in range(t):
        print(start,end=" ")
        start+=2*k+1