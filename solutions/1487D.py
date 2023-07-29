def binary(data,target,low,high):
    if low > high:
        return high
    else:
        mid=(low+high)//2
        if data[mid] > target:
            return binary(data,target,low,mid-1)
        else:
            return binary(data,target,mid+1,high)
arr=[4]
def solve(x):
    arr.append(arr[-1]+4*x)

import io,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
"*********************************************************"
for i in range(2,99**9):
    solve(i)
    if arr[-1] > 10**9:
        break
for _ in range(int(input())):
    n=int(input())
    p=binary(arr,n,0,len(arr)-1)
    if arr[p] == n:
        p-=1
    print(p+1)