n=int(input())
start=input()


lights=[]
for i in range(n):
    lights.append(tuple(map(int,input().split())))

memory=[[False]*n for i in range(10000)]

for i in range(n):
    if start[i] == "1":

        memory[0][i]=1
    else:
        memory[0][i]=0
best=0
best=max(best,sum(memory[0]))

for d in range(1,10000):
    for l in range(n):
        ligth_num=l
        a,b=lights[ligth_num]
        h=(d-b)%a
        if d-b >= 0 and h== 0:
            old=memory[d-1][ligth_num]
            if old == 0:
                memory[d][ligth_num]=1
            else:
                memory[d][ligth_num]=0
        else:
            memory[d][ligth_num]=memory[d-1][ligth_num]
    best=max(best,sum(memory[d]))
print(best)