from itertools import product
 
for _ in range(int(input())):
    a=int(input())
    x=set()
    x_=-9
    y_=-9
    y=set()
    for i in range(a):
        k=input()
        p=k.find("*")
        while True:
            p=k.find("*")
            if p != -1:
                x.add(p)
                x_=p
                y.add(i)
                y_=i
 
                k=k.replace("*",".",1)
            else:
                break
 
 
    if len(x) == 1:
        if x_ == a-1:
 
            x.add(x_-1)
        elif x_ == 0:
            x.add(x_+1)
        else:
            x.add(x_+1)
    if len(y) == 1:
        if y_ == a-1:
            y.add(y_-1)
        elif y_ == 0:
            y.add(y_+1)
        else:
            y.add(y_+1)
 
    t=product(x,y)
    l=[list("."*a) for _ in range(a)]
    for a,b in t:
        l[b][a]="*"
    for i in l:
        print(*i,sep="")