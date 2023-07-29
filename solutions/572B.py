n,s=map(int,input().split())
l=[]
ll=[]
for i in range(n):
    pp=input().split()
    pp=[pp[0],int(pp[1]),int(pp[2])]
    if pp[0] == "B":
        ll.append(pp)
    else:
        l.append(pp)
ll.sort(key=lambda x: x[1],reverse=True)
l.sort(key=lambda x: x[1])
for i in range(len(l)-1):
    t=l[i]
    tt=l[i+1]
    if t[1]== tt[1]:
        l[i+1]=[t[0],t[1],t[2]+tt[2]]
        l[i]=False
for i in range(len(ll)-1):
    t=ll[i]
    tt=ll[i+1]
    if t[1] == tt[1]:
        ll[i+1]=[t[0],t[1],t[2]+tt[2]]
        ll[i]=False


p=0
px=0
r=[]
while p < s and px < len(l):
    if l[px] != False:

        r.append(l[px])
        px+=1
        p+=1
    else:
        px+=1
for i in range(-1,-len(r)-1,-1):
    print(*r[i])
p=0
px=0
while p < s and px < len(ll):
    if ll[px] != False:
        print(*ll[px])
        px+=1
        p+=1
    else:
        px+=1