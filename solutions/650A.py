def math(x):
    return (x*(x-1))//2
n=int(input())
left={}
right={}
both={}
for i in range(n):
    t=tuple(map(int,input().split()))
    try:
        left[t[0]]+=1
    except:
        left[t[0]]=1
    try:
        right[t[1]]+=1
    except:
        right[t[1]]=1
    try:
        both[t]+=1
    except:
        both[t]=1
res=0
for i in left:
    el=left[i]
    res+=math(el)
for i in right:
    el=right[i]
    res+=math(el)
for i in both:
    el=both[i]
    res-=math(el)
print(res)