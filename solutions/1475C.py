for _ in range(int(input())):
    b,g,k=map(int,input().split())
    bo=sorted(map(int,input().split()))
    gi=sorted(map(int,input().split()))
    dbo,dgi={},{}
    ss=1
    for i in range(k-1):
        if bo[i] == bo[i+1]:
            ss+=1
        else:
            dbo[bo[i]]=ss
            ss=1
    dbo[bo[-1]]=ss
    ss=1
    for i in range(k-1):
        if gi[i] == gi[i+1]:
            ss+=1
        else:
            dgi[gi[i]]=ss
            ss=1
    dgi[gi[-1]]=ss
    res=0
    for i in range(k):
        t1=dbo[bo[i]]
        t2=dgi[gi[i]]
        aa=t1+t2-1
        res+=k-aa
    print(res//2)