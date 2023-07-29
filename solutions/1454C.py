for _ in range(int(input())):
    a=int(input())
    l=list(map(int,input().split()))
    dict={}
    for i in range(a):
        k=l[i]
        try:
            dict[k]+=[i]
        except:
            dict[k]=[i]
    best=99**9
    for i in dict:
        t=dict[i]

        result=len(t)+1

        for j in range(len(t)-1):

            if t[j+1] == t[j] +1 :
                result-=1
        if t[0] == 0:
            result-=1
        if t[-1]== a-1:
            result-=1
        best=min(best,result)

    print(best)