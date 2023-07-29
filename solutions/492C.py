n,r,avg=map(int,input().split())
l=[]
top=0
for i in range(n):
    a,b=map(int,input().split())
    top+=a
    l.append((a,b))
ne=avg*n
l.sort(key= lambda x:x[1])
res=0
for i in l:
    a,b=i
    inc=r-a
    t=inc*b
    if top + inc < ne:
        res+=t
        top+=inc
    elif top + inc >= ne:
        kk=max(ne-top,0)
        res+=kk*b
        break
print(res)