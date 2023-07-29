n=int(input())
l="."+input()+"."
p=0
flag=True
for i in range(len(l)-1):
    if l[i] == "?" and l[i-1]+l[i+1] not in ["CY","YC","CM","MC","YM","MY"]:
        p+=1
    if l[i] == l[i+1] and l[i] != "?":
        flag=False
        break
if flag:
    if p > 0:
        print("YES")
    else:
        print("NO")
else:
    print("NO")