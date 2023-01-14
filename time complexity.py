import time
s = time.time()
n = [1,2,3,4,4,5,6]
duplicate = None
for i in range(len(n)):
    for j in range(i+1,len(n)):
        if n[i] == n[j]:
            duplicate = n[i]
print(duplicate)
e = time.time()
print("Run time = ",e-s)

