for _ in range(int(input())):
    n=int(input())
    x=input()
    l=list(x)
    p1=list(x+x)
    p2=list(x)+list(reversed((x)))
    if n% 2 == 0:
        best=["z"*5001]
        best_num=-1
        for i in range(n):
            if i % 2 == 0:
                #duz p1
                start=i
                end=i+n-1
                h=p1[start:end+1]
                if h < best:
                    best=h
                    best_num=i+1
            else:
                #rev p2
                start1=i
                end1=n-1
                end2=2*n-1
                kal=n-(end1-start1+1)
                start2=end2-kal+1
                h=p2[start1:end1+1]+p2[start2:end2+1]
                if h < best:
                    best=h
                    best_num=i+1
    else:
        best=["z"*5001]
        best_num=-1
        for i in range(n):
            if i % 2 != 0:
                #duz p1
                start=i
                end=i+n-1
                h=p1[start:end+1]

                if h < best:
                    best=h
                    best_num=i+1

            else:
                #rev p2
                start1=i
                end1=n-1
                end2=2*n-1
                kal=n-(end1-start1+1)
                start2=end2-kal+1
                h=p2[start1:end1+1]+p2[start2:end2+1]
                if h < best:
                    best=h
                    best_num=i+1
    print("".join(best))
    print(best_num)