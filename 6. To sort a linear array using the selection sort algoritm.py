def selection_sort(l):
    n= len(l)   # len hlo 6
    # i indicates how many items were sorted
    for i in range(0,n-1):
        # To find the minimum value of the unsorted segment

        index_min = i       # We first assume that the first element is the lowest
        # We then use j to loop through the remaining elements
        for j in range(i+1,n):
            # Update the min_index if the element at j is lower than it
            if l[j] < l[index_min]:
                index_min = j

        # After finding the lowest item of the unsorted regions, swap with the first unsorted item
        if index_min != i:      # i and index_min soman na hle sthan odolbodol krbe
            l[i], l[index_min] = l[index_min], l[i]

L = [6,1,4,9,2,1]
selection_sort(L)
print('Selection sort = ',L)
