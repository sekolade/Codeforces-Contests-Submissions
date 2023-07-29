def binary(data,target,low,high):
    if low > high:
        return low
    else:
        mid=(low+high)//2
        if data[mid] >= target:
            return binary(data,target,low,mid-1)
        else:
            return binary(data,target,mid+1,high)
from math import ceil,sqrt
def solve(x):
    return ceil( (-1 + sqrt(1+8*x))/2)
def solve2(x):
    return ( (-1 + sqrt(1+8*x))/2)
dd1=[0]
for i in range(3,50000,4):
    dd1.append(i)
    dd1.append(i+1)
dd2=[0]
for i in range(1,50000,4):
    dd2.append(i)
    dd2.append(i+1)

for _  in range(int(input())):
    a,b=map(int,input().split())

    t=abs(a-b)
    k=solve2(t)
    if t % 2 == 0:

        res=dd1[binary(dd1,k,0,len(dd1)-1)]
    else:
        res=dd2[binary(dd2,k,0,len(dd1)-1)]
    print(res)