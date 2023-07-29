n=int(input())
l=sorted(map(int,input().split()))
for i in  range(n-1,-1,-2):
    print(l[i],end=" ")
k = 0 if n %2 == 0 else 1
for i in range(k,n,2):
    print(l[i],end=" ")