def solve(x,y,z):
    global k,low,high
    if y > x and y > z:
        if k == 3:
            k=2
            low=low
            high=mid-1
        elif k == 2:
            k=1
            low=mid+1
            high=high
        elif k == 1:
            k=2
            low=low
            high=mid-1
    elif y < x and y < z:
        print("!",mid+1)
        k=4
    elif y > x and y < z:
        k=2
        low=low
        high=mid-1
    elif y < x and y > z:
        k=1
        low=mid+1
        high=high
n=int(input())
low=0
high=n-1
k=3
while True:
    mid=(low+high)//2
    q1=mid-1
    if q1 < 0 or q1 > n-1:
        ans1=99**9
    else:
        print("?",q1+1)
        ans1=int(input())
    q2=mid
    if q2 < 0 or q2 > n-1:
        ans2=99**9
    else:
        print("?",q2+1)
        ans2=int(input())
    q3=mid+1
    if q3 < 0 or q3 > n-1:
        ans3=99**9
    else:
        print("?",q3+1)
        ans3=int(input())
    solve(ans1,ans2,ans3)
    if k == 4:
        break