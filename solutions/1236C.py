n=int(input())
k=list(range(1,n**2+1))
num=int(n/2)
l=0
r=n**2-1
m=int(len(k)/2)
j=1
for i in range(n):
    print(*k[l:l+num],end=" ")
    print(*k[r+1-num:r+1],end=" ")
    l+=num
    r+=-num
    if n % 2 == 1:
        print(k[m],end=" ")
        if i % 2 ==0:
            m+=j
            j+=1
        else:
            m-=j
            j+=1
    print()