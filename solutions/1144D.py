n=int(input())
l=list(map(int,input().split()))
dict={}
for i in l:
    try:
        dict[i]+=1
    except:
        dict[i]=1
maks=0
eleman=0
for i in dict:
    if dict[i]>maks:
        maks=dict[i]
        eleman=i
indeks=[-1]
for i in range(n):
    if l[i] == eleman:
        indeks.append(i)
print(n-maks)
for i in range(1,len(indeks)):
    t=indeks[i]
    while t-1 > indeks[i-1]:
        if l[t-1] < eleman:
            print(1,t,t+1)
        elif l[t-1]>eleman:
            print(2,t,t+1)
        t-=1
k=indeks[-1]
while k+1 < n:
    if l[k+1] < eleman:
        print(1,k+2,k+1)
    elif l[k+1]>eleman:
        print(2,k+2,k+1)
    k+=1