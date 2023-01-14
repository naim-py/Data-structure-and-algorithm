# t=a*n*n + b
ns =[1,2,3,4,5]
def find_dupulicate(ns):
    for i in range(len(ns)):
        for j in range(i+1,len(ns)):
            if ns[i]==ns[j]:
                print(ns[i]+"is duplicate")

find_dupulicate(ns)

