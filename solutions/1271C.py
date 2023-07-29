import io,os,sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
n,sx,sy=map(int,input().split())


l_left_up=0
l_left_down=0
l_right_up=0
l_right_down=0
psol,psag,pyuk,pasag=0,0,0,0

for i in range(n):
    x,y=map(int,input().split())

    if x < sx:
        if y < sy:
            l_left_down+=1
        elif y == sy:
            psol+=1
        else:
            l_left_up+=1


    elif x == sx:
        if y < sy:
            pasag+=1
        elif y == sx:
            pass
            #imp
        else:
            pyuk+=1

    else:
        if y < sy:
            l_right_down+=1
        elif y == sy:
            psag+=1
        else:
            l_right_up+=1

best=0
h=-4
if l_left_up+l_left_down+psol>=best:
    best=max(best,l_left_up+l_left_down+psol)
    h=0

    #sol

if l_right_down+l_right_up+psag>=best:
    h=1

    #sag
    best=max(best,l_right_down+l_right_up+psag)


if l_right_down+l_left_down+pasag>=best:
    h=2

    #asag
    best=max(best,l_right_down+l_left_down+pasag)



if l_right_up+l_left_up+pyuk>=best:
    h=3

    #yuk
    best=max(best,l_right_up+l_left_up+pyuk)



print(best)





if h == 0:
    sys.stdout.write(str(sx-1) + " ")
    sys.stdout.write(str(sy) + "\n")
elif h == 1:
    sys.stdout.write(str(sx+1) + " ")
    sys.stdout.write(str(sy) + "\n")

elif h == 2:
    sys.stdout.write(str(sx) + " ")
    sys.stdout.write(str(sy-1) + "\n")

elif h == 3:
    sys.stdout.write(str(sx) + " ")
    sys.stdout.write(str(sy+1) + "\n")