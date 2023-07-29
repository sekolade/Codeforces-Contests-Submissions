def b(d,t,l,h):
    if l > h:
        return None
    else:
        mid=int((l+h)/2)
        if d[mid] == t:
            return mid
        elif d[mid] > t:
            return b(d,t,l,mid-1)
        else:
            return b(d,t,mid+1,h)
for _ in range(int(input())):
    n=int(input())
    l=sorted(map(int,input().split()))
    t=sum(l)
    for i in range(n+2):
        p=t-l[i]
        if p %2 == 0:
            j=int(p/2)
            k=b(l,j,0,n+1)
            if k and k != i:
                for a in range(n+2):
                    if a != i and a!=k:
                        print(l[a],end=" ")
                print()
                n=-1
                break
    if n!=-1:
        print(-1)