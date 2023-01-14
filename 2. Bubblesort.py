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


''''
def bublesort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1],arr[j]

if __name__ == "__main__":
    arr = [12,34,13,43,25,6,5,50]
print("Before Bubblesort = ",arr)
bublesort(arr)
print('After Bublesort = ',arr)
'''