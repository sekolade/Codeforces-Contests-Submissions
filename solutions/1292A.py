import io,os,sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
n,q=map(int,input().split())
pos_x={i:[False,False] for i in range(1,n+1)}
pos_c_r={i:[False,False] for i in range(3,n+2)}
pos_c_l={i:[False,False] for i in range(n-1)}
t=0
for i in range(q):
    y,x=map(int,input().split())
    # pos x
    el=x
    if y == 1:
        ind=0
        next_ind=1
    else:
        ind=1
        next_ind=0
    if pos_x[el][ind] == True:
        pos_x[el][ind]=False
        if pos_x[el][next_ind]==True:
            t-=1
    else:
        pos_x[el][ind]=True
        if pos_x[el][next_ind]==True:
            t+=1
    # pos_c_r
    el=x+y
    if (y,x) != (1,1) and (y,x) != (2,n):
        if pos_c_r[el][ind] ==True:
            pos_c_r[el][ind]=False
            if pos_c_r[el][next_ind]==True:
                t-=1
        else:
            pos_c_r[el][ind]=True
            if pos_c_r[el][next_ind]==True:
                t+=1
    # pos cl
    el=x-y
    if (y,x) != (2,1) and (y,x) != (1,n):
        if pos_c_l[el][ind] ==True:
            pos_c_l[el][ind]=False
            if pos_c_l[el][next_ind]==True:
                t-=1
        else:
            pos_c_l[el][ind]=True
            if pos_c_l[el][next_ind]==True:
                t+=1
    if t > 0:
        sys.stdout.write("No" + "\n")
    else:
        sys.stdout.write("Yes" + "\n")