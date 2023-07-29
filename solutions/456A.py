
l=[]
a=int(input())
for _ in range(a):
    t=tuple(map(int,input().split()))
    l.append(t)
l.sort()
flag=True
for i in range(a-1):
    if l[i][1] > l[i+1][1]:
        print("Happy Alex")
        flag=False
        break
if flag:
    print("Poor Alex")