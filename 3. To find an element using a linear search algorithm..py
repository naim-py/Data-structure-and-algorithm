def linearSearch(list2):
    n=len(list2)
    num=int(input("Enter the search number:"))
    f=0
    for i in range(n-1):
        if list2[i]==num:
            print("The number {} is found in position {} of the list.".format(num,i+1))

            f=1
            break
    if f==0:
        print("The number {} is not found of the list.".format(num))
list1 = [int(x) for x in input("Enter the elements for list:").split()]
linearSearch(list1)



''''
def linearsearch(arr, x):

    n = len(arr)
    for i in range(n):
        if arr[i] == x:
            return i
    return -1                   # ai liner kon kaj nai ,,na dileo hbe
arr = ['t','u','t','o','r','i','a','l']
x = 'a'
print("element found at index "+str(linearsearch(arr,x))) # akhan theke call krese
'''

"""
def search(arr):
    n= len(arr)
    for i in range(n):
        if arr[i]== x:
            return i

arr=[1,3,4,53,22,435,64]
x=1
print('element found at index '+str(search(arr)))
-----------------------------------



"""