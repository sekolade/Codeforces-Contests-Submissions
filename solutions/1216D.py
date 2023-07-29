import functools as f
n=int(input())
l=list(map(int,input().split()))
t=max(l)
l2=[]
r=0
for i in l:
    l2.append(t-i)
    r+=l2[-1]
g = lambda a,b:a if b==0 else g(b,a%b)   #Gcd for two numbers
gcd=f.reduce(lambda x,y:g(x,y),l2)
m1=int(r/gcd)
m2=int(r/m1)
print(m1,m2)