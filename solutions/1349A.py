from math import sqrt
import io,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
def sol(n):
    res={}
    while n % 2 == 0:
        if 2 not in res: res[2]=1
        else: res[2]+=1
        n = n / 2
    for i in range(3,int(sqrt(n))+1,2):
        while n % i== 0:
            if i not in res: res[i]=1
            else: res[i]+=1
            n = n / i
    if n > 2:
        if n not in res: res[n]=1
        else: res[n]+=1
    return res
def second_smallest(numbers):
    m1 = m2 = 99**9
    for x in numbers:
        if x <= m1:
            m1, m2 = x, m1
        elif x < m2:
            m2 = x
    return m2
n=int(input())
l=list(map(int,input().split()))
p=max(l)
dd={}
for i in range(n):
    el=l[i]
    p=sol(el)
    for a in p:
        if a not in dd:dd[a]=[p[a]]
        else: dd[a].append(p[a])
ans=1
for i in dd:
    uz=len(dd[i])
    k=0
    if uz == n-1:
        k=min(dd[i])
    elif uz ==n:
        k=second_smallest(dd[i])
    ans*=i**k
print(int(ans))