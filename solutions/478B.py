from math import comb

a,b=map(int,input().split())
t=a//b
t2=a%b
r=0


r+=comb(t+1,2)*(t2)
r+=comb(t,2)*(b-t2)
print(r,end=" ")


h=b-1
h2=a-h
print(comb(h2,2))