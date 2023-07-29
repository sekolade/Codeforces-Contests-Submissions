def c(d,t,l,h):
    if l >h:
        print(l+1)
    else:
        m = int((l+h)/2)
        if d[m] >= t:
            c(d,t,l,m-1)
        else:
            c(d,t,m+1,h)

a,l1,b,l2=int(input()),list(map(int,input().split())),int(input()),list(map(int,input().split()))
l3=[0]*a
l3[0]=l1[0]
for i in range(1,a):
    l3[i]=l1[i]+l3[i-1]
for i in l2:
    c(l3,i,0,a-1)