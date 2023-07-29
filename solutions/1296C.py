for _ in range(int(input())):
    n=int(input())
    l=list(input())
    ss=(0,0)
    p=0
    dd={ss:p}
    res=[]
    for i in l:
        p+=1
        if i == "R":
            ss=(ss[0]+1,ss[1])
        elif i == "L":
            ss=(ss[0]-1,ss[1])
        elif i == "U":
            ss=(ss[0],ss[1]+1)
        elif i == "D":
            ss=(ss[0],ss[1]-1)
        if ss in dd:
            res.append((p-dd[ss],dd[ss]))
            dd[ss]=p
        else:
            dd[ss]=p
    res.sort()
    if len(res) != 0:
        print(res[0][1]+1,res[0][1]+res[0][0])
    else:
        print(-1)