for _ in range(int(input())):
    t=input()
    d={"R":0,"S":0,"P":0}
    for i in t:
        if i == "R":
            d["P"]+=1
        elif i == "S":
            d["R"]+=1
        else:
            d["S"]+=1
    k=sorted(d.items(),key=lambda x : x[1])
    print(len(t)*k[-1][0])