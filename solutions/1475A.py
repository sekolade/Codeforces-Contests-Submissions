from math import log
for _ in range(int(input())):
    if log(int(input()),2).is_integer():
        print("NO")
    else:print("YES")