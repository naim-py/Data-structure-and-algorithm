# Binary Search in python
def binary_search(list2,item):
    first = 0
    last = len(list2)-1
    found = False
    while( first<=last and not found):
        mid = (first + last)//2
        if list2[mid] == item :
            found = True
        else:
            if item < list2[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found
list1 = [int(x) for x in input("Enter the elements for sortedlist:").split()]

num = int(input("Enter the search number:"))
print("The number {} is found :".format(num),binary_search(list1, num))

"""

def binary_search(arr, low, high, x):

	# Check base case
	if high >= low:

		mid = (high + low) // 2

		# If element is present at the middle itself
		if arr[mid] == x:
			return mid

		# If element is smaller than mid, then it can only
		# be present in left subarray
		elif arr[mid] > x:
			return binary_search(arr, low, mid - 1, x)

		# Else the element can only be present in right subarray
		else:
			return binary_search(arr, mid + 1, high, x)

	else:
		# Element is not present in the array
		return -1

# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 10

# Function call
result = binary_search(arr, 0, len(arr)-1, x)

if result != -1:
	print("Element is present at index", str(result))
else:
	print("Element is not present in array")

"""