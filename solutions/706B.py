a=int(input())
l=sorted(map(int,input().split()))
ttt=max(l)
l_2=[0]*ttt
for i in range(a):
    if i == 0:
        l_2[:l[i]-1]=[i]*(l[i]-1)

    else:
        l_2[l[i-1]-1:l[i]-1]=[i]*(l[i]-l[i-1])

l_2[-1]=a
for _ in range(int(input())):
    kk = int(input())-1
    if kk +1<ttt:

        print(l_2[kk])
    else:
        print(a)