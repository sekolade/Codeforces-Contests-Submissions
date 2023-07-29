from collections import deque
n=int(input())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
q1=deque(l1[1:])
q2=deque(l2[1:])
f_f_length=l1[0]
s_f_length=l2[0]
fi=0
old=[(q1.copy(),q2.copy())]
flag=True
while len(q1) != 0 and len(q2) != 0:
    fi+=1
    p1=q1.popleft()
    p2=q2.popleft()
    if p1 > p2:
        q1.append(p2)
        q1.append(p1)
    else:
        q2.append(p1)
        q2.append(p2)
    if (q1,q2) not in old:
        old.append((q1.copy(),q2.copy()))
    else:
        print(-1)
        flag=False
        break
if flag:
    if len(q1) == 0:
        print(fi,2)
    else:
        print(fi,1)