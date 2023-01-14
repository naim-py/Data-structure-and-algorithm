def knapSack(C, wt, P, n):
    if n == 0 or C == 0:
        return 0
    if (wt[n-1] > C):
        return knapSack(C, wt, P, n-1)
    else:
        return max(
            P[n-1] + knapSack(
                C-wt[n-1], wt, P, n-1),
            knapSack(C, wt, P, n-1))
n = int(input("Enter the number of item: "))
P = [int(x) for x in input("Enter the profits: ").split()]
wt = [int(x) for x in input("Enter the weights: ").split()]
C = int(input("Enter the value of C : "))
print("\nThe maximum profit for 0/1 Knapsack using dynamic programming is:",knapSack(C, wt, P, n))
