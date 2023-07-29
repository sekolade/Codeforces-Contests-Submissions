def binary(data,target,low,high):
    if low > high:
        return high
    else:
        mid=int((low+high)/2)
        if data[mid] <= target:
            return binary(data,target,mid+1,high)
        else:
            return binary(data,target,low,mid-1)
 
for _ in range(int(input())):
    a,b=map(int,input().split())
    l=[1]
    n=1
    for i in range(1,a-1):
       l.append(l[-1]+n)
       n+=1
    result=["a"]*a
    k=binary(l,b,0,len(l)-1)
    k+=1
    result[a-1-k]="b"
    result[-1-(b-l[k-1])]="b"
    print(*result,sep="")