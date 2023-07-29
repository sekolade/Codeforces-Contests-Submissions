
n,s=map(int,input().split())
t=int(s/2)
k="1 "*(n-1)+str(s-(n-1))
kk="1"*(n-1)+str(s-(n-1))
if t > n-1:
    print("YES")
    print(k)
    print(t)
else:
    print("NO")