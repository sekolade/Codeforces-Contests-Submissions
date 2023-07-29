n=int(input())
l=list(input())+["x"]
p=[]
te=1
res=0
deg=[]
po=["R","G","B"]
t=set(po)
for i in range(n):
    el=l[i]
    ind=i
    if l[i] == l[i+1]:
        te+=1

    else:
        end=i
        start=end-te+1
        pp=te//2
        if te % 2 == 0:
            for i in range(pp):
                deg.append(start)
                start+=2
        else:
            for i in range(pp):
                deg.append(start+1)
                start+=2
        te=1
        res+=pp
l.pop()
for i in deg:
    if i == 0:
        right=l[i+1]
        new=t.difference([right,l[i]])
        l[i]=new.pop()
    else:
        left=l[i-1]
        new=t.difference([left,l[i]])
        l[i]=new.pop()

print(res)
print(*l,sep="")