for _ in range(int(input())):
    n,l,r,s=list(map(int,input().split()))
    num=r-l+1
    minimum=int(num*(num+1)/2)
    maksimum=(n-num)*num+minimum
    if minimum<=s<=maksimum:
        t=list(range(1,num+1))
        n2,p,toplam=-1,0,minimum
        while toplam<s:
            if t[n2] < n-p:
                t[n2]+=1
                toplam+=1
            else:
                n2-=1
                p+=1
        jj=list(set(range(1,n+1)).difference(t))
        print(*jj[:l-1],*t,*jj[l-1:],sep=" ")
    else:
        print(-1)