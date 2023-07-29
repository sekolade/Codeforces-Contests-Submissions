
def rec(data,start,stop,derinlik):
    if start<=stop:







        maks=0
        maks_indeks=0
        for i in range(start,stop+1):
            if data[i]>maks:
                maks=data[i]
                maks_indeks=i

        dict[maks]=derinlik

        rec(data,start,maks_indeks-1,derinlik+1)
        rec(data,maks_indeks+1,stop,derinlik+1)


for _ in range(int(input())):
    a=int(input())
    l=list(map(int,input().split()))
    dict={}
    rec(l,0,a-1,0)
    for i in l:
        print(dict[i],end=" ")
    print()