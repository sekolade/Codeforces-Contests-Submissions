dict={1:"011",2:"101",3:"111",0:"001"}
INF=99**9
n=int(input())
l=list(map(int,input().split()))
memory=[]
memory.append([INF,INF,INF])
po=dict[l[0]]
if po[0] == "1":
    memory[0][0]=0
if po[1] == "1":
    memory[0][1]=0
if po[2]=="1":
    memory[0][2]=1
# 0c  1g  2r
for i in range(1,n):
    t=l[i]
    po=dict[t]
    memory.append([INF,INF,INF])
    if po[0] == "1":
        memory[i][0]=min(memory[i-1][1],memory[i-1][2])

    if po[1] == "1":
        memory[i][1]=min(memory[i-1][0],memory[i-1][2])

    if po[2] == "1":
        memory[i][2]=min(memory[i-1][1],memory[i-1][2],memory[i-1][0])+1




print(min(memory[-1]))