for _ in range(int(input())):
    x=int(input())
 
    if x >= 2020:
 
        y1=x//2020
        y2= x % 2020
        if y2 > y1:
            print("NO")
        else: print("YES")
    else:print("NO")