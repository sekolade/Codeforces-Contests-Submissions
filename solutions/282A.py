n=int(input())
k=0
for _ in range(n):
    s=input()
    if "+" in s:k+=1
    if "-" in s:k-=1
print(k)