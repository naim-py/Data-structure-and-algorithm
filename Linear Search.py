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
