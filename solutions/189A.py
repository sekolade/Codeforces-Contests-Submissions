n,a,b,c=map(int,input().split())
memory=[False]*(n+1)

memory[0]=0
t=min(a,b,c)

for i in range(1,t):
    memory[i]=-9999999999



for i in range(t,n+1):
    maks=0
    if i-a >=0:
        maks=max(maks,memory[i-a]+1)
    if i-b >=0:
        maks=max(maks,memory[i-b]+1)
    if i-c >=0:
        maks=max(maks,memory[i-c]+1)

    maks=maks if maks !=0 else -9999999999
    memory[i]=maks
print(memory[n])