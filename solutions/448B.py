s=input()
base=input()
flag_array=False
flag_auto=False
flag_tree=False
ds={}
dbase={}
for i in s:
    try:
        ds[i]+=1
    except:
        ds[i]=1
for i in base:
    try:
        dbase[i]+=1
    except:
        dbase[i]=1
for i in dbase:
    el=i
    freq=dbase[i]
    if el not in ds:
        flag_tree=True
        break
    else:
        freq_s=ds[i]
        if freq_s >= freq:
            pass
        else:
            flag_tree=True
            break
if flag_tree == False:
    if len(s) != len(base):
        flag_auto=True
    c=0
    px=0
    for i in range(len(s)):
        el=s[i]
        ind=i
        if el == base[px]:
            c+=1
            px+=1
        if c ==len(base):
            break
    if c != len(base):
        flag_array=True
    if flag_array and flag_auto:
        print("both")
    elif flag_auto and not flag_array:
        print("automaton")
    else:
        print("array")
else:
    print("need tree")