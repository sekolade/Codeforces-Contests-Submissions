n=list(input())
num=int("".join(n))
po=["4","7"]
re=[]
def solve(k):
    p=int("".join(k))
    if p>=num:
        if k.count("4")==k.count("7"):
            re.append(p)
        else:
            return
    else:
        for i in po:
            h=k
            k+=i
            solve(k)
            k=h
solve("4")
solve("7")
if re:
    print(min(re))
else:
    p=int(len(n)/2)+1
    print("4"*p+"7"*p)