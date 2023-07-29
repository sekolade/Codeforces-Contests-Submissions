for _ in range(int(input())):
    a=int(input())
    l=list(map(int,input().split()))
    dictt={}
    for i in l:
        try:
            dictt[i]+=1
        except:
            dictt[i]=1
    q=dict(sorted(dictt.items(), key=lambda j: j[1]))
    t=sum(q.values())
    p=0
    n=1
    r=99**9
    u=len(q)
    for i in q:
        r=min(r,t-q[i]*(u+1)+q[i]*n)
        p+=q[i]
        n+=1
    print(r)