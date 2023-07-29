for _ in range(int(input())):
    a,b,p=map(int,input().split())
    cr=list(input())
    p1=-2
    pr=0
    old=""
    flag=True
    while p1 >= -len(cr):
        if cr[p1] != old:
            if cr[p1] == "A":
                pr+=a
                old="A"
            elif cr[p1] == "B":
                pr+=b
                old="B"
        if pr > p  :
            print(len(cr)+p1+2)
            flag=False
            break
        p1-=1
    if flag:
        print(1)