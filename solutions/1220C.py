t=list(input())
minimum=t[0]
print("Mike")
old=0
for i in range(1,len(t)):

    if t[i] <= minimum:
        minimum=t[i]
        old=i
    if old < i:
        print("Ann")
    else:
        print("Mike")