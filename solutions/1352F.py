for _ in range(int(input())):
    n0,n1,n2=map(int,input().split())
    if n0 > 0 and n1 > 0 and n2 > 0:
        if n1 % 2 == 0:
            n1-=1
            ans="0"
            ans+="1"*(n2+1)
            ans+="01"*(n1//2)
            ans+="0"
            ans+="0"*n0
        else:
            ans="1"*(n2+1)
            ans+="01"*(n1//2)
            ans+="0"
            ans+="0"*n0
    elif n0 > 0 and n1 == 0 and n2 == 0:
        ans="0"*(n0+1)
    elif n0 > 0 and n1 > 0 and n2 == 0:
        ans="0"*(n0+1)
        ans+="10"*(n1//2)
        ans+="1"*(n1%2)
    elif n0 == 0 and n1 == 0 and n2 > 0:
        ans="1"*(n2+1)
    elif n0 == 0 and n1 > 0 and n2 > 0:
        ans="1"*(n2+1)
        ans+="01"*(n1//2)
        ans+="0"*(n1%2)
    elif n0 == 0 and n1 > 0 and n2 == 0:
        ans="01"
        n1-=1
        ans+="01"*(n1//2)
        ans+="0"*(n1%2)
    print(ans)