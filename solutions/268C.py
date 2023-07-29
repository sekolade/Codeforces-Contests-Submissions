n,m=map(int,input().split())
x=0
y=m
print(min(n,m)+1)
while x<=n and y>= 0:
    print(x,y)
    x+=1
    y-=1