t="abcdefghijklmnopqrstuvwxyz"
dd={t[i]:i+1 for i in range(len(t))}
n,q=map(int,input().split())
l=list(input())
pas=[]
h=0
for i in l:
    c=dd[i]
    h+=c
    pas.append(h)
for i in range(q):
    s,e=map(int,input().split())
    if s != 1:
        print(pas[e-1]-pas[s-2])
    else:
        print(pas[e-1])