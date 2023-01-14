def bubbleSort(list2):
    n=len(list2)
    for i in range(n-1):
        for j in range(n-1):
            if list2[j]<list2[j+1]:
                temp=list2[j]
                list2[j]=list2[j+1]
                list2[j+1]=temp
    return list2
list1=[int(x) for x in input("Enter the number of the list:").split()]
result=bubbleSort(list1)
print("After boubleSort:",result)
