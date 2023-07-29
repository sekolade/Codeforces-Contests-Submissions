for _ in range(int(input())):
    n=int(input())
    position=input()
    sheep_pos=[]
    h=0
    for i in range(n):
        if position[i] == "*":
            sheep_pos.append(i-h)
            h+=1
    sheep_pos.sort()
    if len(sheep_pos) % 2 == 1:
        mid=int(len(sheep_pos)/2)
        e=sheep_pos[mid]
        r=0
        for i in sheep_pos:
            r+=abs(i-e)
        print(r)
    else:
        if sheep_pos:
            best=99**9
            mid=int(len(sheep_pos)/2)-1
            e=sheep_pos[mid]
            r=0
            for i in sheep_pos:
                r+=abs(i-e)
            best=min(best,r)
            mid =int(len(sheep_pos)/2)
            e=sheep_pos[mid]
            r=0
            for i in sheep_pos:
                r+=abs(i-e)
            best=min(best,r)
            print(best)
        else:
            print(0)