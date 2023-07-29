from sys import stdout
n,t=map(int,input().split())
k=int(input())

start=0
end=n-1
mid=int((start+end)/2)
print("?",start+1,mid+1)
stdout.flush()
while True:

    cevap=int(input())

    summ=mid-start+1
    sifir_sayisi=summ-cevap

    k-=sifir_sayisi

    if k > 0:

        start=mid+1
        end=end
        mid=int((start+end)/2)
        print("?",start+1,mid+1)
        stdout.flush()

    elif k <= 0:
        if k == 0:
            if start == mid:
                print("!",start+1)
                break

        k+=sifir_sayisi
        start=start
        end=mid

        mid=int((start+end)/2)



        print("?",start+1,mid+1)
        stdout.flush()