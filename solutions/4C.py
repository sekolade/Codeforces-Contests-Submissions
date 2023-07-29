a=int(input())
memory={}

for _ in range(a):
    k=input()
    if k not in memory:
        memory[k]=1
        print("OK")
    else:

        t=memory[k]
        memory[k]+=1
        print(f"{k}{t}")