from random import randint

import math
INF=99**9
def pf(n):
    while n % 2 == 0:
        try:
            dd[2]+=1
        except:
            dd[2]=1
        n = n / 2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i== 0:
            try:
                dd[i]+=1
            except:
                dd[i]=1
            n = n / i
    if n > 2:
        try:
            dd[n]+=1
        except:
            dd[n]=1
def bf(ind):

    global say1,best
    if ind == len(l):
        best=min(best,max(say1,top/say1))

    else:
        say1*=l[ind]
        bf(ind+1)
        say1/=l[ind]
        bf(ind+1)

n=int(input())
dd={}
pf(n)
l=[]
top=1
for i in dd:
    l.append(i**dd[i])
    top*=i**dd[i]
say1=1
best=INF
bf(0)
print(int(top/best),int(best))