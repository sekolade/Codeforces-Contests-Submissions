n=int(input())
l=list(map(int,input().split()))
p=[]
r=0
pp=[False,False]
if n == 1:
    pass
elif n ==2:
    if l[0] == 1 and l[1] == 2:
        r+=1
    if l[-1] == 1000 and l[-2] == 999:
        r+=1
else:
    yerel=0
    flag=False
    for i in range(1,len(l)-1):
        if l[i-1]+1==l[i] and l[i+1]-1==l[i]:
            yerel+=1
            flag=True
        else:
            flag=False
            start=i-yerel
            if start == 1:
                pp[0]=yerel
            end=i-1
            if end == len(l)-2:
                pp[1]=yerel
            r=max(r,yerel)
            yerel=0
        if flag == False:
            start=i-yerel
        else:
            start=i-yerel+1

        if start == 1:
            pp[0]=yerel

        if flag ==False:


            end=i-1
        else:
            end=i-1+1
        if end == len(l)-2:
            pp[1]=yerel
        r=max(r,yerel)
    if l[0] == 1 and l[1] == 2:
        if pp[0]:
            r=max(r,pp[0]+1)
        else:
            r=max(r,1)
    if l[-1] == 1000 and l[-2] == 999:
        if pp[1]:
            r=max(r,pp[1]+1)
        else:
            r=max(r,1)
print(r)