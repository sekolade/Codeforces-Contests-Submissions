for _ in range(int(input())):
    a=int(input())
    l=list(map(int,input().split()))
    dict={}
    for i in range(a):
        k=l[i]
        try:

            dict[k][0] = dict[k][0]+1

        except:
            dict[k]=[1,i]
    r=[]
    flag=True
    for i in sorted(dict.keys()):
        if dict[i][0] == 1:
            print(dict[i][1]+1)
            flag=False
            break

    if flag:
        print(-1)