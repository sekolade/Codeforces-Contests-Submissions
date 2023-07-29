import io,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
n,m,k=map(int,input().split())
l=list(map(int,input().split()))
diff=[]
for i in range(n-1):
    diff.append((l[i+1]-l[i],i))
diff.sort(reverse=True)
c=0
pp=[]
px=0
while c < k-1:
    pp.append(diff[px][1])
    c+=1
    px+=1
pp.sort()
px=0
start_el=l[0]
end_el=start_el
res=0
c=0
while px < n:
    if c < len(pp):
        if px != pp[c]:
            end_el=l[px]
            px+=1
        else:
            end_el=l[px]
            res+=end_el-start_el+1
            px+=1
            start_el=l[px]
            end_el=start_el
            c+=1
    else:
        end_el=l[px]
        px+=1
print(res+end_el-start_el+1)