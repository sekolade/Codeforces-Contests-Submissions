n,h=map(int,input().split())
l=list(map(int,input().split()))
result=1
for i in range(1,n):

    index=i


    part=sorted(l[0:index+1])
    r=0
    end=part[index]


    maks=end

    r+=2
    kalan=h
    if index >=2:

        while True:

            kalan-=maks
            index-=2
            if index>=0:
                maks=part[index]
                if maks <= kalan:
                    if index != 0:
                        r+=2
                    else:
                        r+=1
                else:
                    break
            else:
                break
    result=max(result,r)
print(result)