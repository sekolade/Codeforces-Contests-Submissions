import sys
input = sys.stdin.readline
t="abcdefghijklmnopqrstuvwxyz"
tt={t[i]:i for i in range(len(t))}
for _ in range(int(input())):
    n,k=map(int,input().split())
    s1=list(input().strip())
    s2=list(input().strip())
    dd={i:0 for i in "abcdefghijklmnopqrstuvwxyz"}
    l1_a=[]
    l1_k=[]
    ye="YES"
    no="NO"
    for i in s1:
        dd[i]+=1
        if dd[i] == k:
            l1_k.append((k,i))
            dd[i]=0
    for i in dd:
        if dd[i] > 0:
            l1_a.append((dd[i],i))
            dd[i]=0
    l2_a=[]
    l2_k=[]
    for i in s2:
        dd[i]+=1
        if dd[i] == k:
            l2_k.append((k,i))
            dd[i]=0
    for i in dd:
        if dd[i] > 0:
            l2_a.append((dd[i],i))
            dd[i]=0
    f=True
    if l1_a != l2_a:
        sys.stdout.write(str(no) + "\n")
        f=False
    else:
        if len(l1_k) != len(l2_k):
            sys.stdout.write(str(ye) + "\n")
            f=False
        else:
            pp1=[0]*(len(t))
            for i in l1_k:
                pp1[tt[i[1]]]+=i[0]
            pp2=[0]*(len(t))
            for i in l2_k:
                pp2[tt[i[1]]]+=i[0]
            c1=""
            for i in range(len(t)):
                if pp1[i] !=0:
                    c1+=t[i]*pp1[i]
            c2=""
            for i in range(len(t)):
                if pp2[i] !=0:
                    c2+=t[i]*pp2[i]
            if len(c1) != len(c2):
                sys.stdout.write(str(no) + "\n")
                f=False
            else:
                for i in range(len(c1)):
                    if c2[i] >=c1[i]:
                        pass
                    else:
                        sys.stdout.write(str(no) + "\n")
                        f=False
                        break
    if f:
        sys.stdout.write(str(ye) + "\n")