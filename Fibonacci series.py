num = int(input("Enter any integer number = "))
n1,n2 = 0,1
sum = 0
if num<=0:
    print('Re run & Enter any positive integer number = ')
else:
    for x in range(0,num):
        print(sum,end=" ")
        n1 = n2
        n2 = sum
        sum = n1+n2


