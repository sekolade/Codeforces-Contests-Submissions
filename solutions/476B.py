a=list(input())
b=list(input())
results=[]

def brute(start,end,r):
    if start<end:
        if b[start] == "?":
            brute(start+1,end,r+1)
            brute(start+1,end,r-1)
        else:
            brute(start+1,end,r)
    else:
        results.append(r)

r1=a.count("+")-a.count("-")
r2=b.count("+")-b.count("-")

isaret=[]
for i in range(len(b)):
    if b[i]=="?":
        isaret.append(i)
if isaret:
    brute(isaret[0],isaret[-1]+1,0)
    k=results.count(r1-r2)
    print(k/len(results))
else:
    if r1 == r2:
        print(1)
    else:print(0)