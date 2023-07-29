a=int(input())
l=sorted(map(int,input().split()))
l2=[]
r=0
for i in l:
    if r <= i:
        l2.append(i)
        r+=i
print(len(l2))