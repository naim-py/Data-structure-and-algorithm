from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start):
        visited = [False] * len(self.graph)
        queue = []

        visited[start] = True
        queue.append(start)

        while queue:
            vertex = queue.pop(0)
            print(vertex, end=" ")

            for i in self.graph[vertex]:
                if not visited[i]:
                    visited[i] = True
                    queue.append(i)

# Example Usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("BFS Traversal:")
g.bfs(2)
