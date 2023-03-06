# at first open Adjacency List making

total_vertex = int(input("Enter no of vertex: "))
graph = {}  # dictionary
flag = True  # true initial value
# visited and queue are list
visited=[]
stack=[]

def DFS(graph,temp):     #root node=temp
    stack.append(temp)
    visited.append(temp)

    while stack:    #loop cholbe queue emty na hya pojonto
        #print krar age pop krte hbe left element so () 0 hbe na dan theke print hbe tai
        node = stack.pop()
        print(node,end=' ')
        #child gula graph a store kra ache,sekhan theke access krte hbe
        # child gula visited and queue modde rekhe dilam and agula age theke thakle r insert dorker nei tai loop chalabo
        for child in graph[node]:
            if child not in visited:
                stack.append(child)
                visited.append(child)


for i in range(total_vertex):
    vertex = input("Enter vertex: ")  # input vertex as a key
    graph[vertex] = list()  # insert to vertex as a key in dictionary,,list means input only key value
    while flag:
        child = input(
            f'Enter child of {vertex} (-1 for exist): ')  # input child value,there are no child if given -1 as a input
        if child != '-1':  # if child not equal -1 then append adjacency under that vertex
            graph[vertex].append(child)
        else:
            flag = False  # if given -1,so there are no child,then come out from loop
    flag = True  # for next loop so true flag
print(graph)
DFS(graph,'A') #graph and root node as parameter
''''
            A
        B       C
    D     E         F

A-B,C
B-D,E
C-F
D
E
F
There are no child of D,E,F 
For BFS
            A 
        B   -    C
    D   -   E
          F
 Adjacency         
{'A': ['B'], 'B': ['C', 'D', 'E'], 'C': ['B', 'E'], 'D': ['B', 'E'], 'E': ['B', 'C', 'D', 'F'], 'F': []}
BFS=A B C D E F 
'''
