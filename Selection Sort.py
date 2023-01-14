def selectionSort(list2):
    n = len(list2)
    for i in range(0, n - 1):
        smallest = i
        for j in range(i + 1, n):
            if list2[j] > list2[smallest]:
                smallest = j
        list2[i], list2[smallest] = list2[smallest], list2[i]
        #print(list2)
list1 = [int(x) for x in input('Enter the list of numbers: ').split()]
selectionSort(list1)
print('After selectionSort :',list1)

