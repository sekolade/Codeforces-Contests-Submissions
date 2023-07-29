for _ in range(int(input())):
    a,b=map(int,input().split())
    k,l=a,b
    t=list(input())
    if a % 2 != 0 and b %2 != 0:
        print(-1)
    else:
        flag=True
        yari_indeksi=int((a+b)/2)-1
        if a% 2 != 0:
            if t[yari_indeksi+1] == "1":
                print(-1)
                flag=False
            else:
                t[yari_indeksi+1]="0"
                a-=1
        if b %2 != 0:
            if t[yari_indeksi+1] == "0":
                print(-1)
                flag=False
            else:
                t[yari_indeksi+1]="1"
                b-=1
        if flag:
            for i in range(k+l):
                if t[i] == "0":
                    if t[-i-1] =="0":
                        a-=2
                    elif t[-i-1]=="1":
                        print(-1)
                        flag=False
                        break
                    else:
                        t[-i-1]="0"
                        a-=2

                if t[i] == "1":
                    if t[-i-1] == "1":
                        b-=2
                    elif t[-i-1]== "0":
                        print(-1)
                        flag=False
                        break
                    else:
                        t[-i-1]= "1"
                        b-=2


            p,u=t.count("0"),t.count("1")
            p=k-p
            u=l-u
            if flag:
                for i in range(k+l):
                    if t[i] == "?":
                        if p >0:
                            t[i]="0"
                            t[-i-1]="0"
                            p-=2
                        elif u > 0:
                            t[i]="1"
                            t[-i-1]="1"
                            u-=2
                if p == 0 and u == 0:
                    print(*t,sep="")
                else:
                    print(-1)