a=int(input())
l=list(map(int,input().split()))
turn=False
p=[]
for i in range(a-1):
    if turn :
        if l[i+1] > l[i]:
            p.append(i)
            break
    else:
        if l[i] > l[i+1]:
            p.append(i)
            turn=True
if len(p) == 0:
    print("yes")
    print(1,1)
else:
    t1=sorted(l)
    if len(p) == 1:
        p.append(a-1)
    l[p[0]:p[1]+1]=l[p[0]:p[1]+1][::-1]
    if t1 == l:
        print("yes")
        print(p[0]+1,p[1]+1)
    else:
        print("no")