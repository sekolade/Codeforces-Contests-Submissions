t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    ans=[]
    ans1=[]
    for i in range(len(arr)):
        if arr[i]%2!=0:
            ans.append(arr[i])
        else:
            ans1.append(arr[i])
    print(*(ans+ans1),sep=" ")