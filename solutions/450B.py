x,y=map(int,input().split())
num=int(input())
num%=6
num=num if num != 0 else num+6
t,l=x,y
for _ in range(num-2):
    x,y=y,y-x
    x%=10**9+7
    y%=10**9+7
if num == 1:
    print(t%(10**9+7))
elif num == 2:
    print(l%(10**9+7))
else:


    print(y)