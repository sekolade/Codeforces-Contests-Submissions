def binary(data,target,low,high):
    if low > high:
        return high
    else:
        mid=int((low+high)/2)
        if data[mid] > target:
            return binary(data,target,low,mid-1)
        else:
            return binary(data,target,mid+1,high)
#######################################################################
n=int(input())
l=sorted(map(int,input().split()))
ta=l[n-1]-1
res=1
l.pop()
while len(l) > 0:
    k=binary(l,ta,0,len(l)-1)
    if k != -1:
        t=l[k]
        for i in range(ta-l[k]):
            if k < len(l)-1:
                del l[k+1]
        del l[k]
        ta=t-1
    else:
        if ta+1 == 0:
            if len(l) == 0:
                break
            else:
                res+=1
                ta=l[-1]-1
                l.pop()
        else:
            k=0
            del l[k]
            ta-=1
print(res)