import sys


# Function to find the shortest possible route that visits all cities
def tsp_dp(dist, n):
    # Create a table to store the optimal sub-solutions
    memo = [[-1] * (1 << n) for i in range(n)]

    # Function to find the optimal solution for a given subset of cities
    def find_path(curr, mask):
        # Base case: all cities have been visited
        if mask == (1 << n) - 1:
            return dist[curr][0]

        # If the optimal sub-solution for the current subset of cities has already been computed
        if memo[curr][mask] != -1:
            return memo[curr][mask]

        # Compute the optimal sub-solution by exploring all possible next cities
        ans = sys.maxsize
        for i in range(n):
            if mask & (1 << i) == 0:
                ans = min(ans, dist[curr][i] + find_path(i, mask | (1 << i)))

        # Store the optimal sub-solution in the table
        memo[curr][mask] = ans
        return ans

    # Find the optimal solution for the entire set of cities
    return find_path(0, 1)


# Driver code to test the above function
if __name__ == '__main__':
    # Define the distance matrix between cities
    dist = [[0, 10, 15, 20],
            [10, 0, 35, 25],
            [15, 35, 0, 30],
            [20, 25, 30, 0]]

    # Find the shortest possible route that visits all cities
    n = len(dist)
    print("The shortest possible route that visits all cities is:", tsp_dp(dist, n))