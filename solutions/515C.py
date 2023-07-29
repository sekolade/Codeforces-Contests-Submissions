precalc={2:[2],3:[3],4:[3,2,2],5:[5],6:[3,5],7:[7],8:[2,2,2,7],9:[3,3,2,7]}
n=int(input())
num=input()
num=num.replace("1","",-1)
num=num.replace("0","",-1)
t=[]
for a in num:
    i=int(a)
    t+=precalc[i]
t.sort()
print(*reversed(t),sep="")