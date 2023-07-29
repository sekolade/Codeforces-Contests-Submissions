n=int(input())
l=[[] for i in range(n)]
for i in range(n):
    for a in range(i):
        l[i]+=[a]

for i in range(n):

    print(((n-1-i)*2+1)*" ",*l[i],1*i,*list(reversed(l[i])))

for i in range(n):
    print(i,end=" ")
print(n,end=" ")
for i in range(n-1,0,-1):
    print(i,end=" ")
print(0)



for i in range(n-1,-1,-1):


    print(((n-1-i)*2+1)*" ",*l[i],1*i,*list(reversed(l[i])))