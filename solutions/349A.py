a=int(input())
b=list(map(int,input().split()))
l=[0,0,0]
flag=True
for i in b:
    if i == 25:
        l[0]+=1
    elif i == 50:
        if l[0]>0:
            l[0]-=1
            l[1]+=1
        else:
            print("NO")
            flag=False
            break

    elif i == 100:
        if l[0]>0 and l[1]>0:
            l[0]-=1
            l[1]-=1
            l[2]+=1
        elif l[0]>2:
            l[0]-=3
            l[2]+=1
        else:
            print("NO")
            flag=False
            break
if flag:
    print("YES")