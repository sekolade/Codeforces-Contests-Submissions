n=int(input())
ll=list(map(int,input().split()))
l=sorted(ll)
if n % 2 !=0:
    k=n//2
else:
    k=n//2-1
pp=[]
for i in range(k,n):
    pp.append(l[i])
    pp.append(-1)
pp.pop()
c=0
h=0
while h < k and c < len(pp):
    if pp[c] == -1:
        if pp[c-1] > l[h] and l[h] < pp[c+1]:
            pp[c]=l[h]
            c+=1
            h+=1
        else:
            c+=1
    else:
        c+=1
print(h)
for i in pp:
    if i != -1:
        print(i,end=" ")
if h != k:
    print(*l[h:k],end=" ")