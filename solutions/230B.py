
a=int(input())
b=list(map(int,input().split()))
memory=[False]*(10**6+1)
memory[1]=False

def is_prime(a):
     return not (a < 2 or any(a % x == 0 for x in range(2, int(a ** 0.5) + 1)))

for i in b:
    if i % 2 == 0:
        if i == 4:
            print("YES")
        else:
            print("NO")
    else:
        k=i**(1/2)
        if k.is_integer():
            p=int(k)
            if memory[p]:
                print("YES")
            else:
                if is_prime(p):
                    print("YES")
                    memory[p]=True
                else:

                    print("NO")
        else:
            print("NO")