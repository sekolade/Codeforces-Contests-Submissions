from math import comb
for _ in range(int(input())):
    n=int(input())
    dict={}
    l=list(map(int,input().split()))
    for i in range(n):
        indeks=i
        eleman=l[i]
        istenen=eleman-indeks
        try:
            dict[istenen]+=1
        except:
            dict[istenen]=1
    r=0
    for i in dict:
        istenen=i
        sayi=dict[istenen]
        if sayi >=2:
            r+=comb(sayi,2)
    print(r)