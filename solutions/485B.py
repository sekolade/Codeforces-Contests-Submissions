n=int(input())
INF=99**9
x_l=INF
x_h=-INF
y_l=INF
y_h=-INF
for i in range(n):
    x,y=map(int,input().split())
    x_l=min(x,x_l)
    x_h=max(x,x_h)
    y_l=min(y,y_l)
    y_h=max(y,y_h)
xx=x_h-x_l
yy=y_h-y_l
print(max(xx,yy)**2)