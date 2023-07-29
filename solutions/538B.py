n=int(input())
dd={1:0,10:0,100:0,1000:0,10000:0,100000:0,1000000:0}
p=str(n)
for i in range(len(p)):
    d=len(str(n))-i
    el=p[i]
    sifir_say=d-1
    kk=10**sifir_say
    dd[kk]+=int(p[i])
res=[]
while True:
    pp=0
    for i in dd:
        if dd[i] > 0:
            dd[i]-=1
            pp+=i
    if pp == 0:
        break
    else:res.append(pp)
print(len(res))
print(*res)