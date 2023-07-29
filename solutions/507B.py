from math import sqrt,ceil
r,x,y,x_,y_=map(int,input().split())

ll=x_-x
rr=y_-y

re=sqrt((ll**2+rr**2))
ma=2*r
print(ceil(re/ma))