a=input()
dict={}
for i in a:
    try:
        dict[i]+=1
    except:
        dict[i]=1

t=0

for i in dict.values():
    if i%2==1:
        t+=1

print("First" if t== 0 else "First" if t%2 == 1 else "Second" )