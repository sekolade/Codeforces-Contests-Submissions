n=int(input())
r=0
for i in range(1,n+1):
    start=i
    say=n-i+1
    if say >=i:
        say=i
    r+=say
print(r)