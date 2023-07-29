from math import cos,sin,radians
def cot(x):
    return cos(x)/sin(x)
for _ in range(int(input())):
    t=int(input())
    t*=2
    print(cot(radians(180/t)))