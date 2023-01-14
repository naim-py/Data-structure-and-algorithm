def merge_sort(arr):
    if len(arr)>1:
        left_arr = arr[:len(arr)//2]    # 2 diye vag krar por  bamer gula print krbe
        right_arr = arr[len(arr)//2:]   # 2 diye vag krar por  daner gula print krbe ,odd hle besi ta print krbe

        # recursion
        merge_sort(left_arr)    # bamer gula ke merge krar jonne
        merge_sort(right_arr)   # daner gula ke merge krar jonne

        # arpor left and right ke merge krte hbe
        #merge
        i=0     # left_arr index
        j=0     # right_arr index
        k=0     # merge array index
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i +=1

            else:
                arr[k] = right_arr[j]
                j +=1
            k +=1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j<len(right_arr):
            arr[k] = right_arr[j]
            j +=1
            k +=1

arr_test = [2,4,1,6,12,5,4,8,3]
print('Before merging = ',arr_test)
merge_sort(arr_test)
print('After Merging = ',arr_test)

