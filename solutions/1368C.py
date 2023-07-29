
n=int(input())
right=0
up=0
kk=[]
base_cor=[(1,1),(2,1),(1,2),(2,2)]
for i in base_cor:
    kk.append(i)
del base_cor[0]
for i in range(n):
    right+=1
    up+=1
    for x,y in base_cor:
        kk.append((x+right,y+up))
print(len(kk))
for i in kk:
    print(*i)