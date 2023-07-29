for _ in range(int(input())):
    n=int(input())
    if n == 2:
        print(-1)
    else:
        nums1=list(range(1,n**2+1,2))
        nums2=list(range(2,n**2+1,2))

        p1=0
        p2=0

        r=[]
        result=[]
        while p1 < len(nums1):
           r.append(nums1[p1])
           if len(r) == n:

               print(*r)
               result.append(r)
               r=[]
           p1+=1

        while p2 < len(nums2):
            r.append(nums2[p2])
            if len(r) == n:
                print(*r)

                result.append(r)
                r=[]
            p2+=1