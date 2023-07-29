from math import log2
import math
def primeFactors(n):
    while n % 2 == 0:
        re.append(2)
        n = n / 2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i== 0:
            re.append(i)
            n = n / i
    if n > 2:
        re.append(n)
for _ in range(int(input())):
    n=int(input())
    p=0
    while (n/2).is_integer():
        p+=1
        n/=2
    re=[]
    primeFactors(n)
    if len(re) == 0 and p == 0:
        print("FastestFinger")
    elif len(re) == 0 and p !=0:
        if p == 1:
            print("Ashishgup")
        else:
            print("FastestFinger")
    elif len(re) != 0 and p==0:
        print("Ashishgup")
    else:
        if len(re) == 1 and p == 1:
            print("FastestFinger")
        else:
            print("Ashishgup")