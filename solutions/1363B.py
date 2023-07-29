import sys
input = sys.stdin.readline
INF=99**9
for _ in range(int(input())):
    s=input().strip()
    le=len(s)
    best=INF
    for i in range(le+1):
        ns="0"*i+"1"*(le-i)
        nsr="1"*i+"0"*(le-i)
        yer=0
        yer2=0
        for i in range(le):
            if ns[i] != s[i]:
                yer+=1
            else:
                yer2+=1

        best=min(best,yer,yer2)
    print(best)