def asd(x,y):
    c=(x-y)//y
    return c

for _ in range(int(input())):
    a,b=map(int,input().split())
    ans=0
    for i in range(2,99**9):
        bb=i
        tt=bb-1

        aa=(bb-1)*(bb+1)
        c1 = b-bb
        c2 = a-aa
        if c1 < 0 or c2 <0:
            break
        else:
            cc=asd(a,tt)
            cc=min(cc,b)
            ans+=cc-bb+1

    print(ans)