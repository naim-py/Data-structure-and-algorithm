total_vertex = int(input("Enter no of vertex: "))
graph={} #dictionary
flag= True #true initial value
for i in range(total_vertex):
    vertex = input("Enter vertex: ") #input vertex as a key
    graph[vertex] = list()  #insert to vertex as a key in dictionary,,list means input only key value
    while flag:
        child = input(f'Enter child of {vertex} (-1 for exist): ') #input child value,there are no child if given -1 as a input
        if child != '-1':   #if child not equal -1 then append adjacency under that vertex
            graph[vertex].append(child)
        else:
            flag= False #if given -1,so there are no child,then come out from loop
    flag = True #for next loop so true flag
print(graph)

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

'''
