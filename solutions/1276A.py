import sys
input=sys.stdin.readline
for _ in range(int(input())):
    flag=False
    ans=[]
    l=list(input())
    px=0
    while px < len(l):
        el=l[px]
        if el == "o":
            t=px+2
            if t < len(l):
                if el+l[px+1]+l[px+2]=="one":
                    ans.append(px+1+1)
                    px+=3
                    continue
                else:
                    px+=1
            else:
                break
        elif el == "t":
            t=px+2
            if t < len(l):
                h=el+l[px+1]+l[px+2]
                if h == "two":
                    ans.append(px+1+1)
                    t =px+2+2
                    if t < len(l):
                        if l[px+3]+l[px+4] == "ne":
                            ans.pop()
                            ans.append(px+2+1)
                            px+=5
                        else:
                            px+=1
                    else:
                        break
                else:
                    px+=1
            else:
                break
        else:
            px+=1
    sys.stdout.write(str(len(ans)) + "\n")
    sys.stdout.write(" ".join(map(str,ans)) + "\n")