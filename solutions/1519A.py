import math
for t in range(int(input())):
  n, m,d=map(int,input().split())
  
  if min(n,m)*(d+1)>=max(n,m):
    print("YES")
  else:print("NO")