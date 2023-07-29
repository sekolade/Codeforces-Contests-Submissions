a=int(input())
if a >= 25:
    text="aeiouaeiou"

    t=a-25
    flag=True
    for i in range(5,int(a/5)+1):

        y=i-5

        x=(t-5*y)/(5+y)
        if x.is_integer():

            flag=False
            break

    if flag:
        print(-1)
    else:
        x+=5
        y+=5

        x=int(x)
        y=int(y)
        n=0
        for _ in range(y):

            kk=text[n:n+5]

            if x ==5:

                print(kk,end="")
            else:
                kalan=x-5
                son_index=n+4
                for a in range(kalan):

                    if son_index+1+a <10:
                        kk+=text[son_index+1+a]
                    else:
                        son_index-=10
                        kk+=text[son_index+1+a]
                print(kk,end="")


            n+=1
            if n >5:
                n-=5


else:
    print(-1)