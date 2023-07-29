a=int(input())
l1=sorted(map(int,input().split()))
l2=sorted(map(int,input().split()))
l3=sorted(map(int,input().split()))

p1=0
p2=0
flag=True
while p2<a-1:
    if l1[p1] == l2[p2]:
        p1+=1
        p2+=1
    else:
        print(l1[p1])
        flag=False
        break


if flag:
    print(l1[-1])


p1=0
p2=0
flag=True
while p2<a-2:
    if l2[p1] == l3[p2]:
        p1+=1
        p2+=1
    else:
        print(l2[p1])
        flag=False
        break
if flag:
    print(l2[-1])