n,x,y=map(int,input().split())
l=[]
for i in range(n):
    a,b=map(int,input().split())
    l.append((a,b))
dd=set()
for a,b in l:
    yf=b-y
    xf=a-x
    if xf == 0:
        dd.add("q")
    else:
        dd.add(yf/xf)
print(len(dd))