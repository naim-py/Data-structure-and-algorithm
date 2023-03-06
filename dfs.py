# Function to perform Depth First Search recursively
def dfs_rec(graph, node, visited):
    # Mark the current node as visited
    visited[node] = True
    print(node, end=' ')

    # Recur for all the vertices adjacent to this vertex
    for i in graph[node]:
        if not visited[i]:
            dfs_rec(graph, i, visited)


# Driver code to test the above function
if __name__ == '__main__':
    # Define the graph
    graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}

    # Mark all the vertices as not visited
    visited = [False] * len(graph)

    # Call the recursive function to perform DFS
    for i in range(len(graph)):
        if not visited[i]:
            dfs_rec(graph, i, visited)
