n,k=map(int,input().split())
d=list(map(int,input().split()))
o=list(input())
p=0
r=1
result=0
while p<n:
    if p+1 < n and o[p] == o[p+1]:
        r+=1
        p+=1
    else:
        start=p-r+1
        end=p
        h=sorted(d[start:end+1],reverse=True)
        if r > k:
            h=sorted(d[start:end+1],reverse=True)
            result+=sum(h[:k])
        else:
            h=d[start:end+1]
            result+=sum(h)
        p+=1
        r=1
print(result)