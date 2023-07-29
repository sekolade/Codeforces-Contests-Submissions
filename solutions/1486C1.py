n=int(input())
low=0
high=n-1
dd={}
f=False
old=-1
while True:
    if low != high:
        if f:
            f=False
            ans=old
        else:
            print("?",low+1,high+1)
            ans=int(input())
        mid=(low+high)//2
        midpos=mid+1
        if ans > midpos:
            if midpos+1 == high+1:
                low=low
                high=mid
            else:
                print("?",midpos+1,high+1)
                ans1=int(input())
                if ans == ans1:
                    low=mid+1
                    high=high
                    f=True
                    old=ans1
                else:
                    low=low
                    high=mid
        else:
            if midpos == low+1:
                low=mid+1
                high=high
            else:
                print("?",low+1,midpos)
                ans1=int(input())
                if ans == ans1:
                    low=low
                    high=mid
                    f=True
                    old=ans1
                else:
                    low=mid+1
                    high=high
    else:
        print("!",low+1)
        break