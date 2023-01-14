def mergeSort(List2):
    n = len(List2)
    if n > 1:
        mid = n // 2
        left = List2[:mid]
        right = List2[mid:]
        ln = len(left)
        Rn = len(right)
        mergeSort(left)
        mergeSort(right)
        i = 0
        j = 0
        k = 0
        while i <ln and j <Rn:
            if left[i] < right[j]:
                List2[k] = left[i]
                i += 1
            else:
                List2[k] = right[j]
                j += 1
            k += 1
        while i <ln:
            List2[k] = left[i]
            i += 1
            k += 1
        while j <Rn:
            List2[k]=right[j]
            j += 1
            k += 1
List1 = [int(x) for x in input("Enter the elements for list:").split()]
mergeSort(List1)
print("After mergeSort :",List1)
