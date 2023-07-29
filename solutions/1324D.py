def binary(data,target,low,high):
    if low > high:
        return high
    else:
        mid=int((low+high)/2)
        if data[mid] <target:
            return binary(data,target,mid+1,high)
        elif data[mid] >= target:
            return binary(data,target,low,mid-1)
n=int(input())
l=list(map(int,input().split()))
ll=list(map(int,input().split()))
re1=[]
re2=[]
te=0
for i in range(n):
    re1.append(l[i]-ll[i])
    if l[i]-ll[i] > 0:
        te+=1
    re2.append(ll[i]-l[i])
re2.sort()
res=0
for i in re1:
    k=binary(re2,i,0,n-1)
    if k != -1:
        res+=k+1
print((res-te)//2)