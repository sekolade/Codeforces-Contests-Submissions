import io,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

n=int(input())
l1=[]
top1=0
l2=[]
top2=0
m=-1
for i in range(n):
    t=int(input())
    if t > 0:
        l1.append(t)
        top1+=t
        m=1
    else:
        l2.append(-t)
        top2-=t
        m=0
if top1> top2:
    print("first")
elif top1 < top2:
    print("second")
else:
    if l1 > l2:
        print("first")
    elif l1 < l2:
        print("second")
    else:
        if m == 1:
            print("first")
        elif m == 0:
            print("second")