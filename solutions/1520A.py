for _ in range(int(input())):
    n=int(input())
    task=list(input())

    t=set()

    p1=0
    flag=True
    while p1 < n:
        g=task[p1]
        pre=len(t)
        t.add(g)
        if len(t)>pre:

            while p1+1 < n and  task[p1+1] == g:
                p1+=1
            p1+=1
        else:
            flag=False
            print("NO")
            break

    if flag:
        print("YES")