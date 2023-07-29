
n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
res=[]
flag=True
def solve(t):
    global flag
    if flag:
        if t == n:
            p=0
            for i in range(n):
                p+=l[i]*res[i]
            if abs(p) % 360 == 0 or p == 0:
                print("YES")
                flag=False
        else:
            for i in [-1,1]:
                res.append(i)
                solve(t+1)
                res.pop()
solve(0)
if flag:
    print("NO")