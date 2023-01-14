#t= ann + bn + c
ns = [1,2,3,1,5]
duplicate = None
for i in range(len(ns)):
    for j in range(i+1,len(ns)):
        if ns[i] == ns[j]:
            duplicate= ns[i]
for i in range(len(ns)):
    if duplicate==ns[i]:
        print(i)